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
    decided = already_decided_families(adr_dir, TARGET_FAMILIES)

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

    # coupling propagation: a second pass, since a family's own stated confidence
    # can be overridden by a tightly-coupled sibling's low confidence, and that
    # sibling may appear later in the decisions list than the family it affects.
    for d, family, fam_knowledge, confidence in accepted_decisions:
        coupled = _coupled_target_families(fam_knowledge["coupling"])
        if coupled & low_confidence_families:
            confidence = "low"
            low_confidence_families.add(family)

        if not os.path.isdir(adr_dir):
            os.makedirs(adr_dir)
        adr_id = next_adr_id(adr_dir)
        title = f"{family}: {d['value'][:60]}" if len(d["value"]) <= 60 else f"{family}: {d['value'][:57]}..."
        content = render_adr(
            adr_id=adr_id,
            title=title,
            families=[family],
            context=d["rationale"],
            decision=d["value"],
            consequences="Recorded by tooling/decide; review before treating as final.",
            date=datetime.date.today().isoformat(),
        )
        filename = f"{adr_id.split('-')[1]}-{slugify(family + ' ' + d['value'][:40])}.md"
        with open(os.path.join(adr_dir, filename), "w", encoding="utf-8") as f:
            f.write(content)
        written.append({"family": family, "adr_id": adr_id, "confidence": confidence})

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exit_code = decision_completeness.main([adr_dir]) if os.path.isdir(adr_dir) else 1
    self_check_output = buf.getvalue()

    return {
        "written": written,
        "skipped_already_decided": skipped_already_decided,
        "rejected": rejected,
        "flagged_low_confidence": sorted(low_confidence_families),
        "self_check_passed": exit_code == 0,
        "self_check_output": self_check_output,
    }
