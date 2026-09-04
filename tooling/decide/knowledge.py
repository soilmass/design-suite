"""Parses this suite's own Composition, Constraints, and Decision documents into
structured per-family knowledge for tooling/decide's context/apply subcommands.

Every function here takes an explicit file path — never hardcodes a location under
docs/ — so tests can run against a snapshot instead of the live repo (see
tests/decide/conftest.py), the same convention tooling/decision_completeness.py's
--registry flag already established.
"""
import re

CONSTRAINT_RANGE_RE = re.compile(r"C(\d{3})[–-]C(\d{3})")
CONSTRAINT_PLAIN_RE = re.compile(r"C(\d{3})")

FAMILY_RANGE_RE = re.compile(r"F(\d{2})[–-]F(\d{2})")
FAMILY_PLAIN_RE = re.compile(r"F(\d{2})(?:\.\d+)?")

COMPOSITION_FAMILY_HEADER_RE = re.compile(r"^### (F\d{2}) · (.+)$", re.M)
COMPOSITION_SEGMENT_RE = re.compile(r"^\*\*(F\d{2}\.\d+)\*\* (.+)$", re.M)
COMPOSITION_BOUNDED_RE = re.compile(r"^\*Bounded by\* — (.+?)\.\s*$", re.M)
COMPOSITION_COUPLING_RE = re.compile(r"^\*Coupling\* — (.+)$", re.M)

CONSTRAINT_HEADER_RE = re.compile(r"^\*\*(C\d{3}) · (.+?)\*\*(?: — .+)?$", re.M)
SECTION_BOUNDARY_RE = re.compile(r"^#{1,3} ", re.M)


def extract_constraint_ids(text):
    """Every C### id mentioned in text, sorted and deduplicated. Expands a
    "C###-C###" or "C###–C###" range (either dash) into every id in between
    before falling back to plain C### matches, so "C001–C003" yields
    C001/C002/C003 rather than just the two endpoints a plain findall would catch."""
    ids = set()
    remaining = text
    for m in CONSTRAINT_RANGE_RE.finditer(text):
        lo, hi = int(m.group(1)), int(m.group(2))
        for n in range(lo, hi + 1):
            ids.add(f"C{n:03d}")
        remaining = remaining.replace(m.group(0), "", 1)
    for m in CONSTRAINT_PLAIN_RE.finditer(remaining):
        ids.add(f"C{m.group(1)}")
    return sorted(ids)


def extract_family_ids(text):
    """Same idea as extract_constraint_ids, for F## family ids (never segments --
    a Decision round is always stated at whole-family granularity, e.g. "F05–F10")."""
    ids = set()
    remaining = text
    for m in FAMILY_RANGE_RE.finditer(text):
        lo, hi = int(m.group(1)), int(m.group(2))
        for n in range(lo, hi + 1):
            ids.add(f"F{n:02d}")
        remaining = remaining.replace(m.group(0), "", 1)
    for m in FAMILY_PLAIN_RE.finditer(remaining):
        ids.add(f"F{m.group(1)}")
    return sorted(ids)


def parse_composition(path):
    """Parse docs/composition-1.0.0.md into {family_id: {name, segments, coupling,
    bounded_by}}. segments maps segment id -> its full description-and-range text."""
    text = open(path, encoding="utf-8").read()
    headers = list(COMPOSITION_FAMILY_HEADER_RE.finditer(text))
    families = {}
    for i, h in enumerate(headers):
        fam_id, name = h.group(1), h.group(2)
        start = h.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        block = text[start:end]

        segments = {seg_id: desc.strip() for seg_id, desc in COMPOSITION_SEGMENT_RE.findall(block)}

        coupling_m = COMPOSITION_COUPLING_RE.search(block)
        coupling = coupling_m.group(1).strip() if coupling_m else None

        bounded_m = COMPOSITION_BOUNDED_RE.search(block)
        bounded_by = extract_constraint_ids(bounded_m.group(1)) if bounded_m else []

        families[fam_id] = {
            "name": name.strip(),
            "segments": segments,
            "coupling": coupling,
            "bounded_by": bounded_by,
        }
    return families


def parse_constraints(path):
    """Parse docs/constraints-1.0.0.md into {C### id: {name, text}}. text is
    everything in the constraint's block after its header line, up to the next
    constraint header or section boundary, whichever comes first."""
    text = open(path, encoding="utf-8").read()
    headers = list(CONSTRAINT_HEADER_RE.finditer(text))
    constraints = {}
    for i, h in enumerate(headers):
        cid, name = h.group(1), h.group(2)
        start = h.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)

        # Check for section boundary (Markdown heading) within this constraint's block
        section_match = SECTION_BOUNDARY_RE.search(text[start:end])
        if section_match:
            end = start + section_match.start()

        body = text[start:end].strip()
        constraints[cid] = {"name": name.strip(), "text": body}
    return constraints


DECISION_ROUND_HEADER_RE = re.compile(r"^## (D\d{3}) · (Round \d+ — .+)$", re.M)
DECISION_ANY_HEADER_RE = re.compile(r"^## D\d{3} ·", re.M)
BOUNDED_SENTENCE_RE = re.compile(r"Bounded by ([^.]+)\.")
COUPLING_ARROW_RE = re.compile(r"F\d{2}(?:\.\d+)?(?:↔F\d{2}(?:\.\d+)?)+(?:/F\d{2}(?:\.\d+)?)*")


def parse_decision_rounds(path):
    """Parse docs/decision-1.0.0.md into the list of "Round N" entries (D002-D014
    as of this writing). Ignores every other D### entry (D001, D020s, D050s, ...) --
    those aren't round headings and don't state a family list."""
    text = open(path, encoding="utf-8").read()
    round_headers = list(DECISION_ROUND_HEADER_RE.finditer(text))
    all_headers = list(DECISION_ANY_HEADER_RE.finditer(text))
    rounds = []
    for h in round_headers:
        did, title = h.group(1), h.group(2)
        start = h.end()
        # end of this round's block = start of the next ## D### heading of any kind
        later = [a.start() for a in all_headers if a.start() > h.start()]
        end = min(later) if later else len(text)
        block = text[start:end]
        # Strip coupling arrow expressions (e.g., "F02↔F22", "F04↔F31/F34/F39")
        # before extracting family IDs, to avoid capturing families mentioned in
        # explanatory asides that are controlled by other rounds.
        block_without_couplings = COUPLING_ARROW_RE.sub("", block)
        bounded_m = BOUNDED_SENTENCE_RE.search(block)
        rounds.append({
            "id": did,
            "title": title.strip(),
            "families": extract_family_ids(block_without_couplings),
            "guidance": block.strip(),
            "bounded_by": extract_constraint_ids(bounded_m.group(1)) if bounded_m else [],
        })
    return rounds


TARGET_FAMILIES = [
    "F01", "F02", "F05.1", "F11.1", "F15", "F17", "F22", "F31", "F32", "F40", "F64",
]


def _parent_family(family_or_segment_id):
    """"F05.1" -> "F05"; "F15" -> "F15"."""
    return family_or_segment_id.split(".")[0]


def _find_round(rounds, family_id):
    parent = _parent_family(family_id)
    for r in rounds:
        if parent in r["families"]:
            return r
    return None


def build_family_knowledge(composition_path, constraints_path, decision_path):
    """Assemble the full per-family knowledge dict for every id in TARGET_FAMILIES,
    unioning each family's Composition-level "Bounded by" (if any) with its
    governing Decision round's own "Bounded by" (if any) -- some families (like F64)
    have no family-level bound and rely entirely on the round-level one; some
    (like F15) state the same bound at both levels, which the union correctly
    de-duplicates rather than double-counting."""
    composition = parse_composition(composition_path)
    constraints = parse_constraints(constraints_path)
    rounds = parse_decision_rounds(decision_path)

    knowledge = {}
    for fid in TARGET_FAMILIES:
        parent = _parent_family(fid)
        comp = composition[parent]
        round_ = _find_round(rounds, fid)

        if fid == parent:
            segments = comp["segments"]
            name = comp["name"]
        else:
            segments = {fid: comp["segments"][fid]}
            name = comp["segments"][fid]

        bound_ids = set(comp["bounded_by"])
        if round_:
            bound_ids |= set(round_["bounded_by"])
        bounded_by = {cid: constraints[cid] for cid in sorted(bound_ids) if cid in constraints}

        knowledge[fid] = {
            "name": name,
            "segments": segments,
            "coupling": comp["coupling"],
            "round": {"id": round_["id"], "title": round_["title"], "guidance": round_["guidance"]} if round_ else None,
            "bounded_by": bounded_by,
        }
    return knowledge
