# tests/decision_completeness/

Regression tests for `tooling/decision_completeness.py` — the tool that joins a downstream
project's ADR set against the Composition family registry and reports which of the 67 families
are decided and which are still running on defaults.

## Running

```bash
pip install pytest pyyaml   # pytest 8.3.3 and pyyaml confirmed working in dev; any recent pytest 8.x should do
python3 -m pytest tests/decision_completeness/ -v
```

or, from inside this directory:

```bash
cd tests/decision_completeness && python3 -m pytest -v
```

## Layout

- `fixtures/<case-name>/` — a directory of ADR markdown files (fenced ` ```yaml ` front matter +
  Context/Decision/Consequences sections), one ADR per file, hand-written directly — there is no
  fixture-generating script here the way `tests/validate/` has `generate_fixtures.py`. Each case's
  ADRs cite real Composition family ids (`F01`–`F15` seen so far) that exist in the actual
  registry today.
- `conftest.py` — the `run_decision_completeness(case_name, extra_args=None)` fixture that runs
  the real, unmodified `tooling/decision_completeness.py` against a copy of `fixtures/<case_name>/`.
- `test_decision_completeness.py` — the tests themselves.

## Why the harness looks like this

Unlike `validate.py`, `decision_completeness.py` *can* already be pointed at an arbitrary ADR
directory and registry path — it takes the ADR dir as a positional argument and an optional
`--registry` flag, with no hardcoded file list to work around. `conftest.py` still copies the
real, unmodified `tooling/decision_completeness.py` plus a snapshot of the real
`tooling/registry.yaml` into a fresh temp directory before invoking it via `subprocess`, purely
for isolation: these tests should not depend on, or be broken by, the live registry changing as
documents in `docs/` evolve.

## The fixtures

- `adrs` and `empty` are the pre-existing worked examples the tool's own docstring and
  `README.md` already reference (3 ADRs; an empty directory). `test_baseline_*` covers them.
- Everything else is adversarial: front-matter shapes the original examples never exercised —
  `families:` as a bare scalar instead of a list, unparseable YAML, an empty `families: []`,
  a lowercase family id, a non-standard `status:` value, two ADRs contesting the same family, and
  an ADR nested several directories deep. Each maps to one test; see the module docstring and each
  test's own docstring in `test_decision_completeness.py` for what bug (if any) it pins down.

Unlike `validate.py`, `decision_completeness.py` sets a real exit code — `0` on a clean run, `1`
when it reports any problem — so tests here assert on `r.returncode` as well as `r.stdout`.

## Adding a new case

1. Make `fixtures/<case-name>/` and drop in one or more ADR `.md` files following the format in
   `tooling/decision_completeness.py`'s own docstring (fenced ` ```yaml ` front matter with at
   least `families:`, then `## Context` / `## Decision` / `## Consequences`). Cite real
   Composition family ids — check `tooling/registry.yaml` for what's current.
2. Add a `test_...` function in `test_decision_completeness.py` that calls
   `run_decision_completeness("<case-name>")` and asserts on `r.returncode` and `r.stdout` (use
   `problem_lines(r.stdout)` to isolate the itemized `  - ` lines).
3. Run `python3 -m pytest tests/decision_completeness/ -v` and confirm it passes.
