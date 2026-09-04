"""Validates a decisions.yaml an agent produced from `context`'s output, writes
real ADR files for everything that passes, self-checks the result with
tooling/decision_completeness.py, and returns a summary. Contains no judgment
logic of its own -- see this plan's Global Constraints for why."""
import datetime
import io
import os
import sys
import contextlib

import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import decision_completeness

from .adr import next_adr_id, render_adr, slugify, already_decided_families
from .knowledge import build_family_knowledge, TARGET_FAMILIES


class DecisionsFileError(Exception):
    pass


def _load_decisions(path):
    try:
        with open(path, encoding="utf-8") as f:
            raw = f.read()
    except OSError as e:
        raise DecisionsFileError(f"could not read {path}: {e}")
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        raise DecisionsFileError(f"{path} is not valid YAML: {e}")
    if not isinstance(data, dict) or "decisions" not in data:
        raise DecisionsFileError(f"{path} must be a mapping with a top-level 'decisions:' list")
    decisions = data["decisions"]
    if not isinstance(decisions, list):
        raise DecisionsFileError(f"{path}: 'decisions:' must be a list")
    for i, d in enumerate(decisions):
        if not isinstance(d, dict):
            raise DecisionsFileError(f"{path}: decisions[{i}] is not a mapping")
        for field in ("family", "value", "rationale"):
            if field not in d:
                raise DecisionsFileError(f"{path}: decisions[{i}] is missing '{field}'")
        for field in ("value", "rationale"):
            if not isinstance(d[field], str):
                raise DecisionsFileError(
                    f"{path}: decisions[{i}].{field} must be a string, "
                    f"got {type(d[field]).__name__}"
                )
    return decisions


def _coupled_target_families(coupling_text):
    """Which other TARGET_FAMILIES ids does this family's own Coupling prose
    mention? Used to propagate a low-confidence flag to a tightly coupled
    sibling, per this tool's spec (a flagged decision's coupling partners are
    themselves worth a second look)."""
    if not coupling_text:
        return set()
    from .knowledge import extract_family_ids
    mentioned = set(extract_family_ids(coupling_text))
    return {fid for fid in TARGET_FAMILIES if fid.split(".")[0] in mentioned or fid in mentioned}


def run_apply(target_repo, decisions_path, suite_composition_path, suite_constraints_path, suite_decision_path):
    decisions = _load_decisions(decisions_path)
    knowledge = build_family_knowledge(
        suite_composition_path, suite_constraints_path, suite_decision_path
    )
    adr_dir = os.path.join(target_repo, "adr")
    # Families already decided by a PRE-EXISTING ADR on disk, from before this run
    # started. Never mutated below -- kept separate from `seen_in_batch` so a
    # same-batch duplicate (a real input problem) is never conflated with "a prior
    # run already decided this" (expected, not an error). See Finding 3.
    decided = already_decided_families(adr_dir, TARGET_FAMILIES)
    seen_in_batch = set()

    written = []
    skipped_already_decided = []
    rejected = []
    low_confidence_families = set()

    accepted_decisions = []  # (decision_dict, computed_confidence) pairs that pass validation

    for d in decisions:
        family = str(d["family"]).strip().upper()

        if family not in TARGET_FAMILIES:
            rejected.append({"family": family, "reason": f"'{family}' is not a target family (see TARGET_FAMILIES)"})
            continue

        if family in seen_in_batch:
            rejected.append({
                "family": family,
                "reason": (
                    f"duplicate entry for {family} within this decisions.yaml "
                    f"-- only the first is considered"
                ),
            })
            continue
        seen_in_batch.add(family)

        if family in decided:
            skipped_already_decided.append(family)
            continue

        fam_knowledge = knowledge[family]
        required_bound_ids = set(fam_knowledge["bounded_by"].keys())
        rationale = str(d["rationale"])
        missing_citations = {cid for cid in required_bound_ids if cid not in rationale}
        if missing_citations:
            rejected.append({
                "family": family,
                "reason": (
                    f"rationale does not cite bounding constraint(s) "
                    f"{', '.join(sorted(missing_citations))}, required because {family} is bounded by them"
                ),
            })
            continue

        confidence = str(d.get("confidence", "high")).strip().lower()
        if confidence == "low":
            low_confidence_families.add(family)

        accepted_decisions.append((d, family, fam_knowledge, confidence))
        # seen_in_batch (added above) already guards against a same-batch
        # duplicate reaching this point twice -- `decided` stays pre-existing-only.

    # coupling propagation: repeated passes to a fixpoint, since a family's own
    # stated confidence can be overridden by a tightly-coupled sibling's low
    # confidence, and that sibling may itself only become low-confidence
    # *during this same propagation* -- via a chain of coupling relationships
    # rather than a single direct link (e.g. A coupled to B, B coupled to C,
    # only C starts low). A single forward pass over accepted_decisions would
    # only catch such a transitive chain when the intermediate family (B)
    # happens to be processed before the family it affects (A), making the
    # result depend on decisions.yaml's list order. Repeating the pass until a
    # full pass adds nothing new makes the result order-independent. The set
    # of target families is small (at most 11), so this is not a performance
    # concern.
    confidence_by_family = {family: confidence for _, family, _, confidence in accepted_decisions}
    changed = True
    while changed:
        changed = False
        for _, family, fam_knowledge, _ in accepted_decisions:
            if family in low_confidence_families:
                continue
            coupled = _coupled_target_families(fam_knowledge["coupling"])
            if coupled & low_confidence_families:
                low_confidence_families.add(family)
                confidence_by_family[family] = "low"
                changed = True

    for d, family, fam_knowledge, _ in accepted_decisions:
        confidence = confidence_by_family[family]

        if not os.path.isdir(adr_dir):
            os.makedirs(adr_dir)
        adr_id = next_adr_id(adr_dir)
        title = f"{family}: {d['value'][:60]}" if len(d["value"]) <= 60 else f"{family}: {d['value'][:57]}..."

        # Finding 5: persist `confidence` durably in the ADR itself (not just
        # stdout), so a human reviewing the batch knows where to look first.
        if confidence == "low":
            confidence_note = "Recorded with `confidence: low` -- worth a closer look during batch review."
        else:
            confidence_note = "Recorded with `confidence: high`."
        # Finding 6: record which Decision round governed this family.
        round_ = fam_knowledge.get("round")
        round_note = f"Decided per Decision's {round_['id']}." if round_ else None
        consequences = " ".join(
            filter(None, [
                "Recorded by tooling/decide; review before treating as final.",
                confidence_note,
                round_note,
            ])
        )

        content = render_adr(
            adr_id=adr_id,
            title=title,
            families=[family],
            context=d["rationale"],
            decision=d["value"],
            consequences=consequences,
            date=datetime.date.today().isoformat(),
        )
        filename = f"{adr_id.split('-')[1]}-{slugify(family + ' ' + d['value'][:40])}.md"
        with open(os.path.join(adr_dir, filename), "w", encoding="utf-8") as f:
            f.write(content)
        written.append({"family": family, "adr_id": adr_id, "confidence": confidence})

    # Always actually call decision_completeness.main(), even when adr_dir was
    # never created (every decision in the batch was rejected). Its own main()
    # already handles a nonexistent directory gracefully -- it prints an
    # explanatory ERROR line and returns 1 -- which gives self_check_output real,
    # honest content instead of silently claiming failure (self_check_passed:
    # false) with no explanation of why the checker never ran. See D4.
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exit_code = decision_completeness.main([adr_dir])
    self_check_output = buf.getvalue()

    return {
        "written": written,
        "skipped_already_decided": skipped_already_decided,
        "rejected": rejected,
        "flagged_low_confidence": sorted(low_confidence_families),
        "self_check_passed": exit_code == 0,
        "self_check_output": self_check_output,
    }
