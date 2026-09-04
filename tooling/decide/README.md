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
