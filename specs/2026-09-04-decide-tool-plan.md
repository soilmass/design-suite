# `tooling/decide` Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `tooling/decide`, a Python package that helps an AI agent make and record the 11 `D204` "first pass" Composition decisions for a real downstream project, producing ADR files `tooling/decision_completeness.py` already knows how to grade.

**Architecture:** Two CLI subcommands. `context` reads this suite's own documents (Composition, Constraints, Decision) plus a target project's brief and existing ADRs, and emits one YAML document describing every undecided target family — its range, its bounding Constraints (if any), and the Decision-round guidance that governs it. `apply` reads back a `decisions.yaml` an agent produced from that context, validates it against two mechanical guardrails, writes real ADR files, self-checks the result with `decision_completeness.py`, and writes a human-readable summary. Neither subcommand contains any judgment logic — the agent calling `context` then `apply` is the one deciding; this package only surfaces what it needs and enforces what can honestly be enforced by code.

**Tech Stack:** Python 3 (matching every other `tooling/*.py` script), PyYAML, pytest. No new dependencies.

## Global Constraints

- Every parsing function takes explicit file paths as arguments (never hardcodes a path to `docs/*.md`) — mirrors `decision_completeness.py`'s own `--registry` override and is required for tests to run against snapshotted fixtures instead of the live repo.
- Scope is exactly the 11 families `D204` names: `F01, F02, F05.1, F11.1, F15, F17, F22, F31, F32, F40, F64`. Nothing in this plan special-cases fewer or more; `TARGET_FAMILIES` is a single list constant one edit away from becoming all 67 later, but that edit is explicitly out of scope now.
- **Neither `context` nor `apply` decides anything.** `context` surfaces facts; `apply` validates and writes what an agent already decided. Do not add heuristic "pick a value" logic anywhere in this package — that was considered during design and rejected as dishonest scope (see `specs/2026-09-04-decision-making-tool-design.md`, "Process, per undecided family").
- **The two guardrails `apply` enforces are the only ones this plan implements, and they are the only ones that are honestly mechanical:** (1) an already-decided family (present with an `accepted` ADR in the target's existing ADR directory) is never re-decided or overwritten; (2) a decision for a family with one or more bounding Constraint IDs is rejected unless its `rationale` text cites every one of those IDs. A prior draft of this plan's source spec also proposed detecting semantic conflicts between a project's brief and a Constraint's actual bound (e.g. "brief says X, but C012 requires Y") — that requires free-text semantic judgment no deterministic function in this package can honestly perform, so it is cut from this plan. Flag it back to the calling agent's own judgment during `context` review; do not simulate it here.
- **This plan does not read the target repo's codebase for inferable context** (existing stack, existing tokens/palette, existing component patterns), though `specs/2026-09-04-decision-making-tool-design.md`'s input model describes it as a source alongside the brief. Reason for the cut: which files are worth inspecting and what to conclude from them varies by stack in a way that would require real per-framework logic to do honestly rather than a generic best-effort guess — and the actual calling agent (an AI coding agent already building inside that repo, per this suite's own primary-user framing) already has this context from its own normal exploration without `tooling/decide` duplicating it. `context`'s output is therefore exactly `{families, already_decided, brief}` — no `repo_hints` key — and the calling agent is expected to bring repo-derived context into its own reasoning when it produces `decisions.yaml`, the same way it's expected to bring the brief's content in.
- ADR file format is fixed by `tooling/decision_completeness.py`'s own docstring and `tests/decision_completeness/fixtures/`: a leading ` ```yaml ` front-matter fence as the first bytes of the file (`id`, `title`, `status`, `date`, `families`), then a Markdown body with `## Context`, `## Decision`, `## Consequences` headings. Every ADR this package writes must satisfy `decision_completeness.py`'s own `front_matter()` regex, unmodified.
- Every new module lives under `tooling/decide/`; every new test lives under `tests/decide/`, mirroring `tests/decision_completeness/`'s existing structure (`conftest.py` + one `test_*.py` per concern).
- Run `cd tooling && python3 validate.py` after every task that touches anything under `docs/` — this plan doesn't add or change any suite ID, so it should stay a no-op every time; if it isn't, something drifted and needs investigating before continuing.

---

### Task 1: `knowledge.py` — parse Composition family and segment text

**Files:**
- Create: `tooling/__init__.py` (empty, only if it doesn't already exist)
- Create: `tooling/decide/__init__.py` (empty)
- Create: `tooling/decide/knowledge.py`
- Test: `tests/decide/test_knowledge.py`
- Test: `tests/decide/conftest.py`

**Interfaces:**
- Produces: `parse_composition(path: str) -> dict[str, dict]` — keyed by family id (`"F01"`, `"F15"`, ...), each value `{"name": str, "segments": dict[str, str], "coupling": str | None, "bounded_by": list[str]}`. `segments` maps segment id (`"F01.1"`) to its full description-and-range line text (everything after the `**F01.1**` marker).
- Produces: `extract_constraint_ids(text: str) -> list[str]` — sorted, deduplicated `C###` ids found in `text`, expanding any `C###–C###` (or `C###-C###`) range into every id in between. Used again in Task 3.

- [ ] **Step 1: Write `tests/decide/conftest.py`, snapshotting the real suite docs**

```python
"""Shared harness for tests/decide/. Mirrors tests/decision_completeness/conftest.py:
snapshot the real, unmodified suite documents and tooling/registry.yaml into a fresh
temp directory per test, so tests exercise real content without depending on the
live repo's evolving state between test runs.
"""
import os
import shutil

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(HERE))
DOCS_DIR = os.path.join(REPO_ROOT, "docs")
REAL_REGISTRY = os.path.join(REPO_ROOT, "tooling", "registry.yaml")
REAL_DECISION_COMPLETENESS = os.path.join(REPO_ROOT, "tooling", "decision_completeness.py")
FIXTURES_DIR = os.path.join(HERE, "fixtures")


@pytest.fixture
def suite_snapshot(tmp_path):
    """Copy the real docs/composition-1.0.0.md, docs/constraints-1.0.0.md,
    docs/decision-1.0.0.md, tooling/registry.yaml, and tooling/decision_completeness.py
    into tmp_path, and return a dict of their new paths."""
    dest_docs = tmp_path / "docs"
    dest_docs.mkdir()
    paths = {}
    for name in ("composition-1.0.0.md", "constraints-1.0.0.md", "decision-1.0.0.md"):
        src = os.path.join(DOCS_DIR, name)
        dst = dest_docs / name
        shutil.copy(src, dst)
        key = name.split("-")[0]  # "composition", "constraints", "decision"
        paths[key] = str(dst)
    dest_tooling = tmp_path / "tooling"
    dest_tooling.mkdir()
    shutil.copy(REAL_REGISTRY, dest_tooling / "registry.yaml")
    paths["registry"] = str(dest_tooling / "registry.yaml")
    shutil.copy(REAL_DECISION_COMPLETENESS, dest_tooling / "decision_completeness.py")
    paths["decision_completeness"] = str(dest_tooling / "decision_completeness.py")
    return paths
```

- [ ] **Step 2: Write the failing tests for `extract_constraint_ids`**

```python
# tests/decide/test_knowledge.py
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
from tooling.decide.knowledge import extract_constraint_ids, parse_composition


def test_extract_constraint_ids_plain_list():
    assert extract_constraint_ids("Bounded by C004, C027, C028.") == ["C004", "C027", "C028"]


def test_extract_constraint_ids_with_trailing_words():
    text = "Bounded by C004 measure, C027 spacing override tolerance, C028 target size."
    assert extract_constraint_ids(text) == ["C004", "C027", "C028"]


def test_extract_constraint_ids_range():
    assert extract_constraint_ids("Bounded by C001–C003, C066–C070.") == [
        "C001", "C002", "C003", "C066", "C067", "C068", "C069", "C070",
    ]


def test_extract_constraint_ids_hyphen_range():
    assert extract_constraint_ids("Bounded by C001-C003.") == ["C001", "C002", "C003"]


def test_extract_constraint_ids_none_found():
    assert extract_constraint_ids("Free of tight coupling once F26 and F30 are set.") == []
```

- [ ] **Step 3: Run the tests to verify they fail**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_knowledge.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'tooling.decide'` (or similar; the module doesn't exist yet).

- [ ] **Step 4: Write `tooling/decide/__init__.py` and `tooling/__init__.py`**

```python
```

(Both empty files. `tooling/decide/__init__.py` makes `tooling/decide` a package.
`tooling/__init__.py` does not exist yet as of this plan — confirmed via
`ls tooling/__init__.py` before writing this plan. Every test in this plan
imports via `from tooling.decide.knowledge import ...`, which requires `tooling`
itself to resolve as a real package, not rely on Python's implicit
namespace-package behavior working out on every environment this runs in.)

- [ ] **Step 5: Write `tooling/decide/knowledge.py` with `extract_constraint_ids`**

```python
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
```

- [ ] **Step 6: Run the constraint-id tests to verify they pass**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_knowledge.py -v -k extract_constraint_ids`
Expected: PASS (5 tests).

- [ ] **Step 7: Write the failing test for `parse_composition`**

```python
# append to tests/decide/test_knowledge.py

def test_parse_composition_f15(suite_snapshot):
    families = parse_composition(suite_snapshot["composition"])
    f15 = families["F15"]
    assert f15["name"] == "Density"
    assert f15["segments"]["F15.1"].startswith("Information density")
    assert f15["segments"]["F15.2"].startswith("Content-to-chrome ratio")
    assert f15["bounded_by"] == ["C004", "C027", "C028"]
    assert "F16" in f15["coupling"]


def test_parse_composition_f01_no_bound(suite_snapshot):
    families = parse_composition(suite_snapshot["composition"])
    f01 = families["F01"]
    assert f01["name"] == "Mandate"
    assert f01["bounded_by"] == []
    assert f01["coupling"] is None
    assert set(f01["segments"]) == {"F01.1", "F01.2", "F01.3", "F01.4"}


def test_parse_composition_f05_segment_f05_1(suite_snapshot):
    families = parse_composition(suite_snapshot["composition"])
    f05 = families["F05"]
    assert "F05.1" in f05["segments"]
    assert f05["segments"]["F05.1"].startswith("Pricing")
```

- [ ] **Step 8: Run to verify these fail first, then pass**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_knowledge.py -v`
Expected: all pass now (the implementation from Step 5 already handles this — this step is confirming it, not writing new code). If any of the three new tests fail, fix `parse_composition` (most likely cause: the `COMPOSITION_BOUNDED_RE` end-of-line anchor not matching because of a trailing space or different dash — inspect `suite_snapshot["composition"]` directly with `grep "Bounded by" <path>` to see the exact bytes before adjusting the regex).

- [ ] **Step 9: Commit**

```bash
git add tooling/__init__.py tooling/decide/__init__.py tooling/decide/knowledge.py tests/decide/conftest.py tests/decide/test_knowledge.py
git commit -m "feat(decide): parse Composition family/segment text and constraint-id ranges"
```

---

### Task 2: `knowledge.py` — parse Constraints text for a given ID

**Files:**
- Modify: `tooling/decide/knowledge.py`
- Test: `tests/decide/test_knowledge.py`

**Interfaces:**
- Consumes: nothing new from Task 1 beyond the module itself.
- Produces: `parse_constraints(path: str) -> dict[str, dict]` — keyed by `C###` id, each value `{"name": str, "text": str}` where `text` is the constraint's full descriptive body (everything after its name/WCAG line, up to the next constraint or section).

- [ ] **Step 1: Write the failing tests**

```python
# append to tests/decide/test_knowledge.py
from tooling.decide.knowledge import parse_constraints


def test_parse_constraints_c046(suite_snapshot):
    constraints = parse_constraints(suite_snapshot["constraints"])
    c046 = constraints["C046"]
    assert c046["name"] == "Name, role, value"
    assert "programmatically determinable" in c046["text"]


def test_parse_constraints_c028_target_size(suite_snapshot):
    constraints = parse_constraints(suite_snapshot["constraints"])
    c028 = constraints["C028"]
    assert c028["name"] == "Target size minimum"
    assert "24" in c028["text"]
```

- [ ] **Step 2: Run to verify they fail**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_knowledge.py -v -k parse_constraints`
Expected: FAIL — `ImportError: cannot import name 'parse_constraints'`.

- [ ] **Step 3: Add `parse_constraints` to `tooling/decide/knowledge.py`**

```python
# append to tooling/decide/knowledge.py

CONSTRAINT_HEADER_RE = re.compile(r"^\*\*(C\d{3}) · (.+?)\*\*(?: — .+)?$", re.M)


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
```

- [ ] **Step 4: Run to verify they pass**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_knowledge.py -v`
Expected: all pass. If `C046`'s or `C028`'s text doesn't contain the expected substring, print `constraints["C046"]` / `constraints["C028"]` directly and compare against `grep -A2 "C046 ·" docs/constraints-1.0.0.md` / `grep -A2 "C028 ·" docs/constraints-1.0.0.md` to see what the regex actually captured.

- [ ] **Step 5: Commit**

```bash
git add tooling/decide/knowledge.py tests/decide/test_knowledge.py
git commit -m "feat(decide): parse Constraints text by id"
```

---

### Task 3: `knowledge.py` — parse Decision rounds and assemble full per-family knowledge

**Files:**
- Modify: `tooling/decide/knowledge.py`
- Test: `tests/decide/test_knowledge.py`

**Interfaces:**
- Consumes: `parse_composition`, `parse_constraints`, `extract_constraint_ids`, `extract_family_ids` from Tasks 1–2.
- Produces: `TARGET_FAMILIES = ["F01", "F02", "F05.1", "F11.1", "F15", "F17", "F22", "F31", "F32", "F40", "F64"]` (module-level constant).
- Produces: `parse_decision_rounds(path: str) -> list[dict]` — one entry per round, `{"id": str, "title": str, "families": list[str], "guidance": str, "bounded_by": list[str]}`.
- Produces: `build_family_knowledge(composition_path, constraints_path, decision_path) -> dict[str, dict]` — keyed by every id in `TARGET_FAMILIES`, each value:
  ```python
  {
      "name": str,                       # segment's own description if a segment id, else family name
      "segments": dict[str, str],        # for a plain family id, all its segments; for a segment id, just that one
      "coupling": str | None,
      "round": {"id": str, "title": str, "guidance": str},
      "bounded_by": dict[str, dict],      # C### id -> {"name": str, "text": str}, unioning Composition's
                                          # family-level "Bounded by" with the governing round's own
                                          # "Bounded by" (Task 3's key correctness requirement — see Step 5)
  }
  ```

- [ ] **Step 1: Write the failing tests for `parse_decision_rounds`**

```python
# append to tests/decide/test_knowledge.py
from tooling.decide.knowledge import parse_decision_rounds, TARGET_FAMILIES, build_family_knowledge


def test_parse_decision_rounds_round_1(suite_snapshot):
    rounds = parse_decision_rounds(suite_snapshot["decision"])
    round1 = next(r for r in rounds if r["id"] == "D003")
    assert round1["title"] == "Round 1 — Purpose"
    assert "F01" in round1["families"]
    assert "F02" in round1["families"]
    assert round1["bounded_by"] == []


def test_parse_decision_rounds_round_4_density_cluster(suite_snapshot):
    rounds = parse_decision_rounds(suite_snapshot["decision"])
    round4 = next(r for r in rounds if r["id"] == "D006")
    assert set(round4["families"]) == {"F15", "F16", "F33", "F30", "F18"}
    assert round4["bounded_by"] == ["C004", "C027", "C028"]


def test_parse_decision_rounds_round_10_conduct_range(suite_snapshot):
    rounds = parse_decision_rounds(suite_snapshot["decision"])
    round10 = next(r for r in rounds if r["id"] == "D012")
    assert set(round10["families"]) >= {"F63", "F64", "F65", "F66", "F67"}
    assert round10["bounded_by"] == ["C001", "C002", "C003", "C066", "C067", "C068", "C069", "C070"]
```

- [ ] **Step 2: Run to verify they fail**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_knowledge.py -v -k parse_decision_rounds`
Expected: FAIL — `ImportError`.

- [ ] **Step 3: Add `parse_decision_rounds` to `tooling/decide/knowledge.py`**

```python
# append to tooling/decide/knowledge.py

DECISION_ROUND_HEADER_RE = re.compile(r"^## (D\d{3}) · (Round \d+ — .+)$", re.M)
DECISION_ANY_HEADER_RE = re.compile(r"^## D\d{3} ·", re.M)
BOUNDED_SENTENCE_RE = re.compile(r"Bounded by ([^.]+)\.")


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
        bounded_m = BOUNDED_SENTENCE_RE.search(block)
        rounds.append({
            "id": did,
            "title": title.strip(),
            "families": extract_family_ids(block),
            "guidance": block.strip(),
            "bounded_by": extract_constraint_ids(bounded_m.group(1)) if bounded_m else [],
        })
    return rounds
```

- [ ] **Step 4: Run to verify they pass**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_knowledge.py -v -k parse_decision_rounds`
Expected: PASS (3 tests). If `round4["bounded_by"]` doesn't match, print `round4["guidance"]` and check the actual "Bounded by" sentence text against `extract_constraint_ids` directly — the two functions were already tested independently in Tasks 1 and this task's Step 3, so a mismatch here means the block-slicing (start/end) is capturing the wrong span, not the extraction logic.

- [ ] **Step 5: Write the failing tests for `build_family_knowledge`**

```python
# append to tests/decide/test_knowledge.py

def test_target_families_constant():
    assert TARGET_FAMILIES == [
        "F01", "F02", "F05.1", "F11.1", "F15", "F17", "F22", "F31", "F32", "F40", "F64",
    ]


def test_build_family_knowledge_f15_unions_family_and_round_bounds(suite_snapshot):
    knowledge = build_family_knowledge(
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"]
    )
    f15 = knowledge["F15"]
    assert f15["round"]["id"] == "D006"
    # Composition's own F15 entry and Round 4's "Bounded by" state the same three ids --
    # this asserts the union doesn't duplicate them.
    assert set(f15["bounded_by"].keys()) == {"C004", "C027", "C028"}
    assert f15["bounded_by"]["C028"]["name"] == "Target size minimum"


def test_build_family_knowledge_f64_gets_round_level_bound_composition_lacks(suite_snapshot):
    # F64's Composition entry alone has no "Bounded by" line -- its only mechanical
    # bound comes from Round 10 (D012)'s "Bounded by C001-C003, C066-C070."
    knowledge = build_family_knowledge(
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"]
    )
    f64 = knowledge["F64"]
    assert f64["round"]["id"] == "D012"
    assert set(f64["bounded_by"].keys()) == {
        "C001", "C002", "C003", "C066", "C067", "C068", "C069", "C070",
    }


def test_build_family_knowledge_segment_id_f05_1(suite_snapshot):
    knowledge = build_family_knowledge(
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"]
    )
    f05_1 = knowledge["F05.1"]
    assert f05_1["round"]["id"] == "D005"
    assert set(f05_1["segments"]) == {"F05.1"}
    assert f05_1["segments"]["F05.1"].startswith("Pricing")


def test_build_family_knowledge_f01_no_bounds_at_all(suite_snapshot):
    knowledge = build_family_knowledge(
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"]
    )
    assert knowledge["F01"]["bounded_by"] == {}
```

- [ ] **Step 6: Run to verify they fail**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_knowledge.py -v -k build_family_knowledge`
Expected: FAIL — `ImportError`.

- [ ] **Step 7: Add `TARGET_FAMILIES` and `build_family_knowledge` to `tooling/decide/knowledge.py`**

```python
# append to tooling/decide/knowledge.py

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
```

- [ ] **Step 8: Run the full test file to verify everything passes**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_knowledge.py -v`
Expected: all tests pass (should be 16 total across Tasks 1–3 by this point).

- [ ] **Step 9: Commit**

```bash
git add tooling/decide/knowledge.py tests/decide/test_knowledge.py
git commit -m "feat(decide): parse Decision rounds and assemble per-family knowledge"
```

---

### Task 4: `brief.py` — load and validate the project brief

**Files:**
- Create: `tooling/decide/brief.py`
- Test: `tests/decide/test_brief.py`
- Create: `tests/decide/fixtures/briefs/valid.yaml`
- Create: `tests/decide/fixtures/briefs/missing_purpose.yaml`
- Create: `tests/decide/fixtures/briefs/not_a_dict.yaml`

**Interfaces:**
- Produces: `REQUIRED_BRIEF_FIELDS = ["purpose", "audience", "brand", "jurisdiction", "constraints"]` (module constant).
- Produces: `load_brief(path: str) -> dict` — raises `BriefError(str)` (a new exception class this module defines) naming exactly what's wrong if the file is missing, isn't valid YAML, isn't a mapping, or is missing any required field. On success, returns the parsed dict with `constraints` normalized to a list (accepts a single string or a list in the source file, always returns a list).

- [ ] **Step 1: Write the fixture files**

`tests/decide/fixtures/briefs/valid.yaml`:
```yaml
purpose: >
  A marketing site for a small SaaS product. Primary goal is trial signups.
audience: Technical decision-makers evaluating developer tools, arriving with some context.
brand:
  - direct
  - technical
  - unglossy
jurisdiction: United States, no EU presence yet
constraints:
  - Must reuse the existing brand palette from the company's product UI
  - No pricing page yet -- pricing is handled by sales
```

`tests/decide/fixtures/briefs/missing_purpose.yaml`:
```yaml
audience: Technical decision-makers.
brand: [direct]
jurisdiction: United States
constraints: []
```

`tests/decide/fixtures/briefs/not_a_dict.yaml`:
```yaml
- this
- is
- a list, not a mapping
```

- [ ] **Step 2: Write the failing tests**

```python
# tests/decide/test_brief.py
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
from tooling.decide.brief import load_brief, BriefError

FIXTURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures", "briefs")


def test_load_brief_valid():
    brief = load_brief(os.path.join(FIXTURES, "valid.yaml"))
    assert "SaaS product" in brief["purpose"]
    assert brief["brand"] == ["direct", "technical", "unglossy"]
    assert isinstance(brief["constraints"], list)
    assert len(brief["constraints"]) == 2


def test_load_brief_missing_required_field():
    try:
        load_brief(os.path.join(FIXTURES, "missing_purpose.yaml"))
        assert False, "expected BriefError"
    except BriefError as e:
        assert "purpose" in str(e)


def test_load_brief_not_a_mapping():
    try:
        load_brief(os.path.join(FIXTURES, "not_a_dict.yaml"))
        assert False, "expected BriefError"
    except BriefError as e:
        assert "mapping" in str(e).lower()


def test_load_brief_missing_file():
    try:
        load_brief(os.path.join(FIXTURES, "does_not_exist.yaml"))
        assert False, "expected BriefError"
    except BriefError as e:
        assert "does_not_exist.yaml" in str(e)


def test_load_brief_normalizes_single_string_constraint():
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as f:
        f.write("purpose: x\naudience: y\nbrand: [z]\njurisdiction: US\nconstraints: one hard constraint\n")
        path = f.name
    try:
        brief = load_brief(path)
        assert brief["constraints"] == ["one hard constraint"]
    finally:
        os.unlink(path)
```

- [ ] **Step 3: Run to verify they fail**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_brief.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 4: Write `tooling/decide/brief.py`**

```python
"""Loads and validates a downstream project's .design-suite/brief.yaml -- the
project-specific context (purpose, audience, brand, jurisdiction, hard
constraints) that tooling/decide's knowledge.py content alone can't supply."""
import yaml

REQUIRED_BRIEF_FIELDS = ["purpose", "audience", "brand", "jurisdiction", "constraints"]


class BriefError(Exception):
    pass


def load_brief(path):
    try:
        with open(path, encoding="utf-8") as f:
            raw = f.read()
    except OSError as e:
        raise BriefError(f"could not read brief at {path}: {e}")

    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        raise BriefError(f"{path} is not valid YAML: {e}")

    if not isinstance(data, dict):
        raise BriefError(f"{path} must parse to a mapping (got {type(data).__name__})")

    missing = [f for f in REQUIRED_BRIEF_FIELDS if f not in data]
    if missing:
        raise BriefError(f"{path} is missing required field(s): {', '.join(missing)}")

    constraints = data["constraints"]
    if isinstance(constraints, str):
        constraints = [constraints]
    elif not isinstance(constraints, list):
        raise BriefError(f"{path}: constraints must be a string or a list")
    data["constraints"] = constraints

    return data
```

- [ ] **Step 5: Run to verify they pass**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_brief.py -v`
Expected: PASS (5 tests).

- [ ] **Step 6: Commit**

```bash
git add tooling/decide/brief.py tests/decide/test_brief.py tests/decide/fixtures/briefs/
git commit -m "feat(decide): load and validate the project brief"
```

---

### Task 5: `adr.py` — render an ADR matching `decision_completeness.py`'s expected format

**Files:**
- Create: `tooling/decide/adr.py`
- Test: `tests/decide/test_adr.py`

**Interfaces:**
- Consumes: nothing from earlier tasks.
- Produces: `render_adr(adr_id: str, title: str, families: list[str], context: str, decision: str, consequences: str, date: str) -> str` — the full file content as a string, front matter first.
- Produces: `next_adr_id(adr_dir: str) -> str` — scans `adr_dir` (same recursive `.md` scan `decision_completeness.py`'s `load_adrs` does) for the highest existing `ADR-####` id and returns the next one, zero-padded to 4 digits (`"ADR-0001"` if the directory is empty or has none).
- Produces: `slugify(text: str) -> str` — lowercase, non-alphanumeric runs collapsed to a single `-`, for building filenames.

- [ ] **Step 1: Write the failing tests**

```python
# tests/decide/test_adr.py
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
from tooling.decide.adr import render_adr, next_adr_id, slugify


def test_slugify():
    assert slugify("Primary conversion goal is trial signup") == "primary-conversion-goal-is-trial-signup"
    assert slugify("F31/F32: Typography & Color!!") == "f31-f32-typography-color"


def test_render_adr_front_matter_matches_decision_completeness_regex():
    import re
    content = render_adr(
        adr_id="ADR-0001",
        title="Primary conversion goal is trial signup",
        families=["F01"],
        context="This is the context.",
        decision="This is the decision.",
        consequences="This is the consequences.",
        date="2026-09-04",
    )
    # the exact regex tooling/decision_completeness.py's front_matter() uses
    m = re.match(r"```yaml\n(.*?)\n```", content, re.S)
    assert m is not None
    import yaml
    fm = yaml.safe_load(m.group(1))
    assert fm["id"] == "ADR-0001"
    assert fm["title"] == "Primary conversion goal is trial signup"
    assert fm["families"] == ["F01"]
    assert fm["status"] == "accepted"
    assert fm["date"] == "2026-09-04"
    assert "## Context" in content
    assert "## Decision" in content
    assert "## Consequences" in content
    assert "This is the context." in content


def test_next_adr_id_empty_dir(tmp_path):
    assert next_adr_id(str(tmp_path)) == "ADR-0001"


def test_next_adr_id_increments(tmp_path):
    (tmp_path / "0001-something.md").write_text(
        '```yaml\nid: ADR-0001\ntitle: x\nfamilies: [F01]\n```\n# x\n', encoding="utf-8"
    )
    (tmp_path / "0002-other.md").write_text(
        '```yaml\nid: ADR-0002\ntitle: y\nfamilies: [F02]\n```\n# y\n', encoding="utf-8"
    )
    assert next_adr_id(str(tmp_path)) == "ADR-0003"


def test_next_adr_id_ignores_malformed(tmp_path):
    (tmp_path / "0001-good.md").write_text(
        '```yaml\nid: ADR-0005\ntitle: x\nfamilies: [F01]\n```\n# x\n', encoding="utf-8"
    )
    (tmp_path / "0002-bad.md").write_text("not an ADR at all", encoding="utf-8")
    assert next_adr_id(str(tmp_path)) == "ADR-0006"
```

- [ ] **Step 2: Run to verify they fail**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_adr.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 3: Write `tooling/decide/adr.py`**

```python
"""Renders and locates ADR files in the exact format tooling/decision_completeness.py
expects (see its own module docstring): a leading ```yaml front-matter fence as the
first bytes of the file, then a Markdown body with Context/Decision/Consequences."""
import glob
import os
import re

import yaml

ADR_ID_RE = re.compile(r"ADR-(\d+)")


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug


def render_adr(adr_id, title, families, context, decision, consequences, date):
    front_matter = {
        "id": adr_id,
        "title": title,
        "status": "accepted",
        "date": date,
        "families": families,
    }
    fm_yaml = yaml.safe_dump(front_matter, sort_keys=False, default_flow_style=False)
    return (
        f"```yaml\n{fm_yaml}```\n\n"
        f"# {adr_id} · {title}\n\n"
        f"## Context\n\n{context}\n\n"
        f"## Decision\n\n{decision}\n\n"
        f"## Consequences\n\n{consequences}\n"
    )


def next_adr_id(adr_dir):
    """Highest existing ADR-#### id in adr_dir (recursive .md scan) + 1, or
    ADR-0001 if none exist. Files that don't parse as a valid ADR (malformed
    front matter, or no id: field) are silently skipped, same as
    decision_completeness.py's own load_adrs() skips malformed files rather
    than crashing on them."""
    highest = 0
    for path in glob.glob(os.path.join(adr_dir, "**", "*.md"), recursive=True):
        text = open(path, encoding="utf-8").read()
        m = re.match(r"```yaml\n(.*?)\n```", text, re.S)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError:
            continue
        if not isinstance(fm, dict):
            continue
        id_m = ADR_ID_RE.match(str(fm.get("id", "")))
        if id_m:
            highest = max(highest, int(id_m.group(1)))
    return f"ADR-{highest + 1:04d}"
```

- [ ] **Step 4: Run to verify they pass**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_adr.py -v`
Expected: PASS (5 tests).

- [ ] **Step 5: Commit**

```bash
git add tooling/decide/adr.py tests/decide/test_adr.py
git commit -m "feat(decide): render ADRs matching decision_completeness.py's format"
```

---

### Task 6: `context_cmd.py` — assemble and emit the context document

**Files:**
- Create: `tooling/decide/context_cmd.py`
- Test: `tests/decide/test_context_cmd.py`
- Create: `tests/decide/fixtures/existing_adrs_f01_decided/0001-mandate.md`

**Interfaces:**
- Consumes: `build_family_knowledge` (Task 3), `load_brief` (Task 4), `load_adrs` from `tooling/decision_completeness` (existing, imported not reimplemented — per this plan's Global Constraints).
- Produces: `run_context(target_repo: str, suite_composition_path: str, suite_constraints_path: str, suite_decision_path: str) -> dict` — the full context document as a plain dict (caller decides whether to print it as YAML or write it to a file; keeping this function's return value a dict, not a YAML string, keeps it directly testable without string-parsing). Shape:
  ```python
  {
      "families": {  # only undecided target families
          "F01": {"name": ..., "segments": ..., "coupling": ..., "round": ..., "bounded_by": ...},
          ...
      },
      "already_decided": ["F..."],  # target families with an existing accepted ADR
      "brief": {...},  # from load_brief, or {} if no brief.yaml found
  }
  ```
  Reads the brief from `<target_repo>/.design-suite/brief.yaml`; reads existing ADRs from `<target_repo>/adr/` if that directory exists, else treats the project as having no prior decisions. `bounded_by`'s constraint dicts (`{"name":..., "text":...}`) are preserved as-is from `build_family_knowledge` — no re-serialization needed since this is a plain dict, not yet YAML text.

- [ ] **Step 1: Write the fixture — an existing ADR deciding F01**

`tests/decide/fixtures/existing_adrs_f01_decided/0001-mandate.md`:
```markdown
​```yaml
id: ADR-0001
title: Single job -- drive trial signups
status: accepted
date: 2026-09-01
families:
  - F01
​```

# ADR-0001 · Single job -- drive trial signups

## Context

Pre-existing decision, present before this test runs tooling/decide against this fixture.

## Decision

F01 is already decided by this ADR.

## Consequences

None relevant to this test.
```

(Write this file with real triple-backtick fences, not the escaped ones shown here for
readability inside this plan document.)

- [ ] **Step 2: Write the failing tests**

```python
# tests/decide/test_context_cmd.py
import os
import shutil
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
from tooling.decide.context_cmd import run_context

FIXTURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")


def _make_target_repo(tmp_path, brief_fixture=None, existing_adrs_fixture=None):
    repo = tmp_path / "target_repo"
    repo.mkdir()
    if brief_fixture:
        design_suite_dir = repo / ".design-suite"
        design_suite_dir.mkdir()
        shutil.copy(
            os.path.join(FIXTURES, "briefs", brief_fixture), design_suite_dir / "brief.yaml"
        )
    if existing_adrs_fixture:
        shutil.copytree(os.path.join(FIXTURES, existing_adrs_fixture), repo / "adr")
    return str(repo)


def test_run_context_no_brief_no_adrs(tmp_path, suite_snapshot):
    repo = _make_target_repo(tmp_path)
    ctx = run_context(
        repo, suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"]
    )
    assert ctx["brief"] == {}
    assert ctx["already_decided"] == []
    assert set(ctx["families"]) == {
        "F01", "F02", "F05.1", "F11.1", "F15", "F17", "F22", "F31", "F32", "F40", "F64",
    }


def test_run_context_with_brief(tmp_path, suite_snapshot):
    repo = _make_target_repo(tmp_path, brief_fixture="valid.yaml")
    ctx = run_context(
        repo, suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"]
    )
    assert "SaaS product" in ctx["brief"]["purpose"]


def test_run_context_excludes_already_decided(tmp_path, suite_snapshot):
    repo = _make_target_repo(tmp_path, existing_adrs_fixture="existing_adrs_f01_decided")
    ctx = run_context(
        repo, suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"]
    )
    assert "F01" not in ctx["families"]
    assert ctx["already_decided"] == ["F01"]
    assert "F02" in ctx["families"]
```

- [ ] **Step 3: Run to verify they fail**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_context_cmd.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 4: Write `tooling/decide/context_cmd.py`**

```python
"""Assembles the context document tooling/decide's `context` subcommand emits:
every undecided target family's knowledge, the project's brief, and which target
families are already decided (so an agent doesn't re-derive what's already settled)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from decision_completeness import load_adrs

from .brief import load_brief, BriefError
from .knowledge import build_family_knowledge, TARGET_FAMILIES


def _already_decided(adr_dir):
    if not os.path.isdir(adr_dir):
        return set()
    adrs, _malformed = load_adrs(adr_dir)
    decided = set()
    for adr in adrs:
        if adr["status"] != "accepted":
            continue
        for cited in adr["families"]:
            cited = str(cited).strip().upper()
            if cited in TARGET_FAMILIES:
                decided.add(cited)
    return decided


def run_context(target_repo, suite_composition_path, suite_constraints_path, suite_decision_path):
    knowledge = build_family_knowledge(
        suite_composition_path, suite_constraints_path, suite_decision_path
    )

    adr_dir = os.path.join(target_repo, "adr")
    decided = _already_decided(adr_dir)

    brief_path = os.path.join(target_repo, ".design-suite", "brief.yaml")
    if os.path.isfile(brief_path):
        try:
            brief = load_brief(brief_path)
        except BriefError as e:
            brief = {"_error": str(e)}
    else:
        brief = {}

    families = {fid: knowledge[fid] for fid in TARGET_FAMILIES if fid not in decided}

    return {
        "families": families,
        "already_decided": sorted(decided),
        "brief": brief,
    }
```

- [ ] **Step 5: Run to verify they pass**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_context_cmd.py -v`
Expected: PASS (3 tests).

- [ ] **Step 6: Commit**

```bash
git add tooling/decide/context_cmd.py tests/decide/test_context_cmd.py tests/decide/fixtures/existing_adrs_f01_decided/
git commit -m "feat(decide): assemble the context document for the context subcommand"
```

---

### Task 7: `apply_cmd.py` — validate decisions, write ADRs, self-check, summarize

**Files:**
- Create: `tooling/decide/apply_cmd.py`
- Test: `tests/decide/test_apply_cmd.py`
- Create: `tests/decide/fixtures/decisions/all_valid.yaml`
- Create: `tests/decide/fixtures/decisions/missing_bound_citation.yaml`
- Create: `tests/decide/fixtures/decisions/unknown_family.yaml`

**Interfaces:**
- Consumes: `TARGET_FAMILIES`, `build_family_knowledge` (Task 3), `next_adr_id`, `render_adr`, `slugify` (Task 5), `load_adrs` and `main` from `tooling.decision_completeness` (existing).
- Produces: `run_apply(target_repo: str, decisions_path: str, suite_composition_path: str, suite_constraints_path: str, suite_decision_path: str) -> dict` — writes ADR files into `<target_repo>/adr/` for every decision that passes validation, and returns a summary dict:
  ```python
  {
      "written": [{"family": "F01", "adr_id": "ADR-0001", "confidence": "high"}, ...],
      "skipped_already_decided": ["F..."],
      "rejected": [{"family": "F...", "reason": "..."}, ...],
      "flagged_low_confidence": ["F..."],       # includes coupling-propagated flags
      "self_check_passed": bool,
      "self_check_output": str,
  }
  ```
- Produces: `DecisionsFileError(str)` exception, raised for a malformed `decisions.yaml` (not a mapping, no top-level `decisions:` list, or a decision entry missing `family`/`value`/`rationale`).

- [ ] **Step 1: Write the fixture files**

`tests/decide/fixtures/decisions/all_valid.yaml` (values are intentionally short — content quality isn't what this tool validates, citation and structure are):
```yaml
decisions:
  - family: F01
    value: "Single job: drive trial signups. Primary conversion is Start free trial. Success = conversion. Permanent."
    rationale: "Per brief.purpose (SaaS trial-signup site) and D003's F01-first-and-alone guidance."
    confidence: high
  - family: F02
    value: "One named segment: technical decision-makers. Assumes some field expertise. Arrives to find out specifics. Addressed as 'you'."
    rationale: "Per brief.audience and D003's F02/F03/F04-together guidance."
    confidence: high
  - family: F15
    value: "Content-dominant, moderate density, generous whitespace around code samples."
    rationale: "Per D006's density-cluster guidance, bounded by C004, C027, C028 -- generous target sizes and measure respected throughout."
    confidence: low
  - family: F64
    value: "404, offline, empty, and error surfaces all designed with cause/consequence/next-action stated."
    rationale: "Per D012 Round 10 guidance, bounded by C001, C002, C003, C066, C067, C068, C069, C070 -- forgiveness and failure clarity honored throughout."
    confidence: high
```

`tests/decide/fixtures/decisions/missing_bound_citation.yaml`:
```yaml
decisions:
  - family: F15
    value: "Content-dominant, moderate density."
    rationale: "Per D006's density-cluster guidance."
    confidence: high
```

`tests/decide/fixtures/decisions/unknown_family.yaml`:
```yaml
decisions:
  - family: F99
    value: "Not a real family."
    rationale: "N/A"
    confidence: high
```

- [ ] **Step 2: Write the failing tests**

```python
# tests/decide/test_apply_cmd.py
import os
import shutil
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
from tooling.decide.apply_cmd import run_apply, DecisionsFileError

FIXTURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")


def _make_target_repo(tmp_path):
    repo = tmp_path / "target_repo"
    repo.mkdir()
    return str(repo)


def test_run_apply_writes_adrs_for_valid_decisions(tmp_path, suite_snapshot):
    repo = _make_target_repo(tmp_path)
    result = run_apply(
        repo,
        os.path.join(FIXTURES, "decisions", "all_valid.yaml"),
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
    )
    written_families = {w["family"] for w in result["written"]}
    assert written_families == {"F01", "F02", "F15", "F64"}
    assert result["rejected"] == []
    adr_files = os.listdir(os.path.join(repo, "adr"))
    assert len(adr_files) == 4


def test_run_apply_reports_confidence(tmp_path, suite_snapshot):
    repo = _make_target_repo(tmp_path)
    result = run_apply(
        repo,
        os.path.join(FIXTURES, "decisions", "all_valid.yaml"),
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
    )
    f15_entry = next(w for w in result["written"] if w["family"] == "F15")
    assert f15_entry["confidence"] == "low"
    assert "F15" in result["flagged_low_confidence"]


def test_run_apply_rejects_missing_bound_citation(tmp_path, suite_snapshot):
    repo = _make_target_repo(tmp_path)
    result = run_apply(
        repo,
        os.path.join(FIXTURES, "decisions", "missing_bound_citation.yaml"),
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
    )
    assert result["written"] == []
    assert len(result["rejected"]) == 1
    assert result["rejected"][0]["family"] == "F15"
    assert "C004" in result["rejected"][0]["reason"] or "C027" in result["rejected"][0]["reason"] or "C028" in result["rejected"][0]["reason"]
    assert not os.path.isdir(os.path.join(repo, "adr")) or os.listdir(os.path.join(repo, "adr")) == []


def test_run_apply_rejects_unknown_family(tmp_path, suite_snapshot):
    repo = _make_target_repo(tmp_path)
    result = run_apply(
        repo,
        os.path.join(FIXTURES, "decisions", "unknown_family.yaml"),
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
    )
    assert result["written"] == []
    assert result["rejected"][0]["family"] == "F99"
    assert "not a target family" in result["rejected"][0]["reason"].lower()


def test_run_apply_skips_already_decided(tmp_path, suite_snapshot):
    repo = _make_target_repo(tmp_path)
    shutil.copytree(
        os.path.join(FIXTURES, "existing_adrs_f01_decided"), os.path.join(repo, "adr")
    )
    result = run_apply(
        repo,
        os.path.join(FIXTURES, "decisions", "all_valid.yaml"),
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
    )
    assert "F01" in result["skipped_already_decided"]
    written_families = {w["family"] for w in result["written"]}
    assert "F01" not in written_families
    assert "F02" in written_families


def test_run_apply_self_check_passes_when_all_target_families_decided(tmp_path, suite_snapshot):
    # all_valid.yaml only decides 4 of the 11 -- self-check against
    # decision_completeness.py's own *67-family* registry will still report
    # "not fully complete" (correctly -- most of the 67 remain undecided).
    # This test asserts self_check_output is present and well-formed, not that
    # it reports 100% (which would be a wrong expectation for a partial decision set).
    repo = _make_target_repo(tmp_path)
    result = run_apply(
        repo,
        os.path.join(FIXTURES, "decisions", "all_valid.yaml"),
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
    )
    assert isinstance(result["self_check_passed"], bool)
    assert "DECISION COMPLETENESS" in result["self_check_output"]


def test_run_apply_malformed_decisions_file_not_a_mapping(tmp_path, suite_snapshot):
    import tempfile
    repo = _make_target_repo(tmp_path)
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as f:
        f.write("- just\n- a\n- list\n")
        path = f.name
    try:
        try:
            run_apply(
                repo, path,
                suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
            )
            assert False, "expected DecisionsFileError"
        except DecisionsFileError:
            pass
    finally:
        os.unlink(path)
```

- [ ] **Step 3: Run to verify they fail**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_apply_cmd.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 4: Write `tooling/decide/apply_cmd.py`**

```python
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

from .adr import next_adr_id, render_adr, slugify
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


def _already_decided(adr_dir):
    if not os.path.isdir(adr_dir):
        return set()
    adrs, _malformed = decision_completeness.load_adrs(adr_dir)
    decided = set()
    for adr in adrs:
        if adr["status"] != "accepted":
            continue
        for cited in adr["families"]:
            cited = str(cited).strip().upper()
            if cited in TARGET_FAMILIES:
                decided.add(cited)
    return decided


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
    decided = _already_decided(adr_dir)

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
```

- [ ] **Step 5: Run to verify they pass**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_apply_cmd.py -v`
Expected: PASS (8 tests).

If `test_run_apply_self_check_passes_when_all_target_families_decided` fails because `decision_completeness.main`'s signature doesn't accept a list the way this code calls it, re-check `tooling/decision_completeness.py`'s actual `main(argv)` signature (Task 7's own file, Step 4 above, already shows the real call is `main([adr_dir])`, matching `main(argv)`'s expectation of `argv[0]` being the ADR directory).

- [ ] **Step 6: Run the full suite to confirm nothing else broke**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/ -v`
Expected: every test in the repo passes, including `tests/decision_completeness/` and `tests/validate/`.

- [ ] **Step 7: Commit**

```bash
git add tooling/decide/apply_cmd.py tests/decide/test_apply_cmd.py tests/decide/fixtures/decisions/
git commit -m "feat(decide): validate decisions, write ADRs, self-check, and summarize"
```

---

### Task 8: CLI entrypoint and end-to-end test

**Files:**
- Create: `tooling/decide/__main__.py`
- Test: `tests/decide/test_cli_end_to_end.py`
- Modify: `tooling/decide/README.md` (create — usage doc, matching `tests/decision_completeness/README.md`'s existing precedent for documenting a tool alongside its tests)

**Interfaces:**
- Consumes: `run_context` (Task 6), `run_apply` (Task 7).
- Produces: a runnable `python3 -m tooling.decide context <target-repo>` and `python3 -m tooling.decide apply <target-repo> <decisions-file>` from the repo root. `context` prints the context document as YAML to stdout (or to `--out <path>` if given). `apply` prints the summary as YAML to stdout (or to `--out <path>`), and exits `0` only if `rejected` is empty and `self_check_passed` doesn't regress anything `apply` itself just wrote (exits `1` if `rejected` is non-empty, since that means at least one decision needs the calling agent's attention before this run can be considered clean — `self_check_passed` being `False` is expected and not itself a failure exit, since a partial decision set against the full 67-family registry is the normal case, not an error, per Task 7 Step 5's own note).

- [ ] **Step 1: Write the failing end-to-end test**

```python
# tests/decide/test_cli_end_to_end.py
import os
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FIXTURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")


def test_cli_context_then_apply_end_to_end(tmp_path):
    repo = tmp_path / "target_repo"
    repo.mkdir()
    design_suite_dir = repo / ".design-suite"
    design_suite_dir.mkdir()
    import shutil
    shutil.copy(os.path.join(FIXTURES, "briefs", "valid.yaml"), design_suite_dir / "brief.yaml")

    context_result = subprocess.run(
        [sys.executable, "-m", "tooling.decide", "context", str(repo)],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    assert context_result.returncode == 0, context_result.stderr
    import yaml
    ctx = yaml.safe_load(context_result.stdout)
    assert "F01" in ctx["families"]
    assert "SaaS product" in ctx["brief"]["purpose"]

    apply_result = subprocess.run(
        [
            sys.executable, "-m", "tooling.decide", "apply", str(repo),
            os.path.join(FIXTURES, "decisions", "all_valid.yaml"),
        ],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    assert apply_result.returncode == 0, apply_result.stderr
    summary = yaml.safe_load(apply_result.stdout)
    assert len(summary["written"]) == 4
    assert summary["rejected"] == []
    assert os.path.isdir(repo / "adr")
    assert len(os.listdir(repo / "adr")) == 4


def test_cli_apply_exits_nonzero_on_rejection(tmp_path):
    repo = tmp_path / "target_repo"
    repo.mkdir()

    result = subprocess.run(
        [
            sys.executable, "-m", "tooling.decide", "apply", str(repo),
            os.path.join(FIXTURES, "decisions", "missing_bound_citation.yaml"),
        ],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    assert result.returncode == 1
```

- [ ] **Step 2: Run to verify they fail**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_cli_end_to_end.py -v`
Expected: FAIL — module has no `__main__`, so `python3 -m tooling.decide` errors out.

- [ ] **Step 3: Write `tooling/decide/__main__.py`**

```python
"""CLI entrypoint: python3 -m tooling.decide context <target-repo> [--out PATH]
                    python3 -m tooling.decide apply <target-repo> <decisions.yaml> [--out PATH]

Suite document paths default to this repo's own docs/*.md next to tooling/decide/
(the normal case: this tool runs from within the design-suite repo against a
downstream target-repo path) but can be overridden with --composition/--constraints/
--decision for testing or for a vendored copy of this suite elsewhere.
"""
import argparse
import os
import sys

import yaml

from .apply_cmd import run_apply
from .context_cmd import run_context

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_COMPOSITION = os.path.join(REPO_ROOT, "docs", "composition-1.0.0.md")
DEFAULT_CONSTRAINTS = os.path.join(REPO_ROOT, "docs", "constraints-1.0.0.md")
DEFAULT_DECISION = os.path.join(REPO_ROOT, "docs", "decision-1.0.0.md")


def _add_suite_path_args(p):
    p.add_argument("--composition", default=DEFAULT_COMPOSITION)
    p.add_argument("--constraints", default=DEFAULT_CONSTRAINTS)
    p.add_argument("--decision", default=DEFAULT_DECISION)
    p.add_argument("--out", default=None, help="write output here instead of stdout")


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python3 -m tooling.decide")
    sub = parser.add_subparsers(dest="command", required=True)

    context_p = sub.add_parser("context", help="emit the decision context for a target repo")
    context_p.add_argument("target_repo")
    _add_suite_path_args(context_p)

    apply_p = sub.add_parser("apply", help="validate and write decisions for a target repo")
    apply_p.add_argument("target_repo")
    apply_p.add_argument("decisions_path")
    _add_suite_path_args(apply_p)

    args = parser.parse_args(argv)

    if args.command == "context":
        result = run_context(args.target_repo, args.composition, args.constraints, args.decision)
        exit_code = 0
    else:
        result = run_apply(
            args.target_repo, args.decisions_path, args.composition, args.constraints, args.decision
        )
        exit_code = 1 if result["rejected"] else 0

    output = yaml.safe_dump(result, sort_keys=False, default_flow_style=False, width=100)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(output)
    else:
        print(output)

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run to verify the tests pass**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/decide/test_cli_end_to_end.py -v`
Expected: PASS (2 tests). If `test_cli_context_then_apply_end_to_end` fails with a YAML parse error on `context_result.stdout`, print `context_result.stdout` directly — the most likely cause is `bounded_by`'s nested constraint dicts not round-tripping cleanly through `yaml.safe_dump`'s default flow style; if so, this is a real bug in the summary/context serialization, not a test problem — fix `__main__.py`'s `yaml.safe_dump` call or the offending nested structure, don't loosen the test.

- [ ] **Step 5: Write `tooling/decide/README.md`**

```markdown
# tooling/decide

Helps an AI agent make and record the `D204` "first pass" Composition decisions
(`F01, F02, F05.1, F11.1, F15, F17, F22, F31, F32, F40, F64`) for a real
downstream project — not for this repo itself, the same way
`tooling/decision_completeness.py` (which this tool calls as a self-check) is
built for a downstream team, not for this suite's own documents.

Full design: `specs/2026-09-04-decision-making-tool-design.md`.

## Usage

From this repo's root, against a target project at `../my-project`:

```bash
# 1. Write ../my-project/.design-suite/brief.yaml (see tests/decide/fixtures/briefs/valid.yaml
#    for the required shape: purpose, audience, brand, jurisdiction, constraints).

# 2. Get the context for every undecided target family:
python3 -m tooling.decide context ../my-project --out context.yaml

# 3. Read context.yaml, decide each family, write decisions.yaml:
#    decisions:
#      - family: F01
#        value: "..."
#        rationale: "..., citing every constraint id context.yaml's bounded_by names"
#        confidence: high | low

# 4. Validate and write real ADRs:
python3 -m tooling.decide apply ../my-project decisions.yaml
```

`apply` exits `1` if anything in `decisions.yaml` was rejected (an unknown family,
an already-decided family, or a rationale missing a required constraint citation)
— check the `rejected` list in its output before re-running. `self_check_passed`
being `false` is normal for a partial decision set (this tool only ever decides
the 11 target families; `decision_completeness.py`'s own registry covers all 67)
— it is not itself a failure.

## Testing

`tests/decide/` — pytest, run from repo root: `python3 -m pytest tests/decide/ -v`.
Mirrors `tests/decision_completeness/`'s structure: `conftest.py` snapshots the
real suite documents into a temp directory per test so tests exercise real
content without depending on the live repo's state changing between runs.
```

- [ ] **Step 6: Run the entire test suite one final time**

Run: `cd /home/edox1/Public/design-suite && python3 -m pytest tests/ -v`
Expected: every test passes — `tests/decide/` (should be ~35 tests across all 8 tasks) plus every pre-existing suite (`tests/decision_completeness/`, `tests/validate/`).

- [ ] **Step 7: Run `validate.py` to confirm zero effect on the governed suite**

Run: `cd /home/edox1/Public/design-suite/tooling && python3 validate.py`
Expected: PASS, zero registry diff — `tooling/decide/` isn't under `docs/`, so this should be a no-op, confirming Task 8 (and every earlier task) didn't accidentally touch anything governed.

- [ ] **Step 8: Commit**

```bash
cd /home/edox1/Public/design-suite
git add tooling/decide/__main__.py tooling/decide/README.md tests/decide/test_cli_end_to_end.py
git commit -m "feat(decide): CLI entrypoint and end-to-end test"
```

---

## After this plan

Not part of this plan, tracked for a follow-up once this lands:
- Rewrite `ROADMAP.md` around this tool as the flagship goal (per `specs/2026-09-04-decision-making-tool-design.md`'s own closing section) — deliberately sequenced *after* this plan, not before, so the roadmap describes something real rather than something proposed.
- A second worked example: run this tool against a small synthetic target project for real, and publish the resulting `context.yaml` → `decisions.yaml` → written ADRs as a companion to `examples/end-to-end-walkthrough.md` — this is the artifact that actually proves the tool works end to end on a case a human didn't hand-narrate.
- Extending `TARGET_FAMILIES` beyond the 11 — explicitly out of scope until this is proven, per this plan's Global Constraints.
