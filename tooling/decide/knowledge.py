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
    everything in the constraint's block after its header line."""
    text = open(path, encoding="utf-8").read()
    headers = list(CONSTRAINT_HEADER_RE.finditer(text))
    constraints = {}
    for i, h in enumerate(headers):
        cid, name = h.group(1), h.group(2)
        start = h.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        body = text[start:end].strip()
        constraints[cid] = {"name": name.strip(), "text": body}
    return constraints
