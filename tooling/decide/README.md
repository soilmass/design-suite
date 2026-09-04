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

`apply` exits `1` if anything in `decisions.yaml` was **rejected** — an unknown family, a
rationale missing a required constraint citation, or a family listed more than once within
the same `decisions.yaml` (only the first occurrence is considered; later ones are rejected
as duplicates) — check the `rejected` list in its output before re-running. A family already
decided by a *prior* `apply` run (a pre-existing ADR already on disk) is **not** a rejection:
it's expected, normal behavior — it lands in `skipped_already_decided` and does not affect
the exit code.

Every decision's `rationale` must cite, by id, every constraint listed in that family's
`bounded_by` in `context`'s output (e.g. write `C004` somewhere in the rationale if `C004`
is one of the bounding constraints) — a rationale missing one of these citations is rejected.

`self_check_passed` being `false` means `decision_completeness.py` found something actually
wrong with what `apply` wrote — a malformed ADR or an unresolved citation — never merely that
coverage is incomplete: deciding only 1 of the 11 target families (or the suite's full 67)
still reports `self_check_passed: true` as long as what was written is clean.

## Testing

`tests/decide/` — pytest, run from repo root: `python3 -m pytest tests/decide/ -v`.
Mirrors `tests/decision_completeness/`'s structure: `conftest.py` snapshots the
real suite documents into a temp directory per test so tests exercise real
content without depending on the live repo's state changing between runs.
