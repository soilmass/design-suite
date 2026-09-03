# tests/validate/

Regression tests for `tooling/validate.py` — the validator that CLAUDE.md, README.md, and
CONTRIBUTING.md all call "the whole test suite for this repo," and which itself had zero tests
until this directory.

## Running

```bash
pip install pytest pyyaml   # pytest 8.3.3 and pyyaml confirmed working in dev; any recent pytest 8.x should do
python3 -m pytest tests/validate/ -v
```

or, from inside this directory:

```bash
cd tests/validate && python3 -m pytest -v
```

## Layout

- `fixtures/<case-name>/docs/` — synthetic, minimal nine-document "fake suites." Every case needs
  all nine files (see below for why) even when the case is only exercising one of them; the other
  eight are tiny, mutually-consistent, and valid.
- `conftest.py` — the `run_validate(case_name)` fixture that runs the real, unmodified
  `tooling/validate.py` against `fixtures/<case_name>/docs/`.
- `test_validate.py` — the tests themselves, one section per check category.
- `generate_fixtures.py` — the (idempotent) generator that wrote everything under `fixtures/`.
  Not part of the pytest run; re-run it by hand if you change a fixture body in that script.

## Why the harness looks like this

`validate.py` has no CLI flag or environment variable to point it at an arbitrary docs directory —
it derives `DOCS_DIR` from its own file location
(`os.path.dirname(os.path.abspath(__file__))/../docs`), and its `DOCS` dict hardcodes the exact
nine filenames it opens unconditionally, before any check runs. Give it fewer than nine files and
it crashes with `FileNotFoundError`, not a check failure.

So `conftest.py`'s `run_validate` fixture copies the **real, unmodified** `tooling/validate.py`
into a fresh temp directory next to a copy of one fixture's `docs/`, then runs it there via
`subprocess`. This never touches the repo's real `tooling/registry.yaml` — the copied
`validate.py` writes its registry next to *itself*, i.e. into the temp directory, since that path
is derived from `__file__` the same way `DOCS_DIR` is. `tooling/validate.py` itself was never
edited to make any of this possible.

## The exit-code quirk

`validate.py` never calls `sys.exit()`. It always exits `0`, whether it found problems or not —
pass/fail is only readable from stdout text (`PASS — no problems` vs. `N PROBLEM(S)` plus itemized
`  - ` lines). Every test here asserts on that text, not on `returncode`, and
`test_validate_never_sets_a_nonzero_exit_code` pins the behavior down explicitly so a future
change to `validate.py` that starts setting a real exit code is a visible, deliberate decision
rather than something a caller was silently relying on already.

## Coverage

One or more tests per check category, per `validate.py`'s own five-part console output:

| # | Check | Fixture(s) | Test(s) |
|---|---|---|---|
| 1 | Front matter + declared exports vs. actual | `exports_mismatch` | `test_exports_mismatch_detected` |
| 2 | Dependency direction (downward only) | `dependency_direction_violation` (+ `_fixed`) | `test_dependency_direction_violation_detected`, `test_dependency_direction_violation_fixed_passes_clean` |
| 3 | Cross-reference resolution | `dangling_reference` | `test_dangling_reference_detected` |
| 4 / 4b | Registry generation / orthogonality | `happy_path`, `orthogonality_violation` | `test_happy_path_registry_written_with_all_nine_ids`, `test_orthogonality_violation_detected` |
| 5 | Roster / summary | `happy_path` | `test_happy_path_roster_reports_all_nine_built` |

Plus a clean-pass baseline (`test_happy_path_passes_clean`) and the exit-code regression test.

`dependency_direction_violation` / `dependency_direction_violation_fixed` is the red/green pair:
identical suites except vocabulary's illegal `depends: [Anatomy ^1]` is removed in the `_fixed`
copy, which is the only difference between a run that reports 1 problem and a run that reports
none.
