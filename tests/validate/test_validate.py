"""Regression tests for tooling/validate.py.

Run with:

    cd tests/validate && python3 -m pytest -v
    # or, from the repo root:
    python3 -m pytest tests/validate/ -v

Requires pytest and pyyaml (the same dependency validate.py itself needs --
``pip install pyyaml`` per README.md / CONTRIBUTING.md).

## How this is wired

validate.py has no CLI flag or env var to point it at an arbitrary docs
directory -- it derives DOCS_DIR from its own file location
(``os.path.dirname(os.path.abspath(__file__))/../docs``) and hardcodes the
nine document filenames it opens unconditionally. So every fixture under
fixtures/<case>/docs/ must contain all nine files (even the ones a given
case isn't about get a tiny, valid stub) or validate.py crashes with
FileNotFoundError before any check runs. conftest.py's `run_validate`
fixture copies the *real, unmodified* tooling/validate.py plus one fixture's
docs/ into a fresh temp directory shaped the way validate.py expects, then
invokes it there via subprocess -- this repo's own tooling/registry.yaml is
never touched by these tests.

## The exit-code quirk

validate.py never calls sys.exit(); it always returns 0, whether it found
problems or not. Pass/fail can only be read from stdout text ("PASS -- no
problems" vs "N PROBLEM(S)" plus the itemized "  - " lines). Tests below
assert on that text, not on returncode. test_validate_never_sets_a_nonzero_exit_code
below pins this down explicitly so it doesn't get "fixed" into a false
assumption later.
"""


def problem_lines(stdout):
    return [ln for ln in stdout.splitlines() if ln.startswith("  - ")]


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------

def test_happy_path_passes_clean(run_validate):
    r = run_validate("happy_path")
    assert r.returncode == 0
    assert "PASS — no problems" in r.stdout
    assert "PROBLEM(S)" not in r.stdout
    assert problem_lines(r.stdout) == []


def test_happy_path_roster_reports_all_nine_built(run_validate):
    """Category [5]: roster/summary."""
    r = run_validate("happy_path")
    assert "-> 9 built, 0 remaining:" in r.stdout
    for doc_name in (
        "vocabulary", "constraints", "anatomy", "composition",
        "decision", "implementation", "verification", "diagnosis", "governance",
    ):
        assert f"{doc_name}" in r.stdout
    assert "not built" not in r.stdout


def test_happy_path_registry_written_with_all_nine_ids(run_validate, tmp_path):
    """Category [4]: registry generation."""
    r = run_validate("happy_path")
    assert "[4] Registry written: 9 entries -> registry.yaml" in r.stdout

    registry_path = tmp_path / "happy_path" / "tooling" / "registry.yaml"
    assert registry_path.exists(), "validate.py should have written registry.yaml next to itself"

    import yaml
    entries = yaml.safe_load(registry_path.read_text())
    assert len(entries) == 9
    ids = {e["id"] for e in entries}
    assert ids == {
        "V-001", "C001", "A-001", "F01",
        "D001", "T001", "X001", "R001", "G001",
    }
    assert all(e["status"] == "active" for e in entries)


# ---------------------------------------------------------------------------
# Category [1]: front matter + declared exports vs. actual
# ---------------------------------------------------------------------------

def test_exports_mismatch_detected(run_validate):
    """composition declares exports F01-F05 but only defines F01 in its body."""
    r = run_validate("exports_mismatch")
    assert r.returncode == 0  # see module docstring: validate.py never sets a nonzero exit
    assert "PROBLEM(S)" in r.stdout
    assert "MISMATCH" in r.stdout
    assert "composition: declares F01-F05, actual F01–F01" in r.stdout


# ---------------------------------------------------------------------------
# Category [2]: dependency direction (downward only)
# ---------------------------------------------------------------------------

def test_dependency_direction_violation_detected(run_validate):
    """Vocabulary (tier 0) is made to depend on Anatomy (tier 1) -- upward, illegal."""
    r = run_validate("dependency_direction_violation")
    assert "PROBLEM(S)" in r.stdout
    assert "ILLEGAL" in r.stdout
    assert "vocabulary -> anatomy: not downward" in r.stdout


def test_dependency_direction_violation_fixed_passes_clean(run_validate):
    """Red/green pair for the fixture above: same suite, illegal `depends:`
    removed from vocabulary's front matter, nothing else changed."""
    r = run_validate("dependency_direction_violation_fixed")
    assert "PASS — no problems" in r.stdout
    assert "PROBLEM(S)" not in r.stdout
    assert "ILLEGAL" not in r.stdout


# ---------------------------------------------------------------------------
# Category [3]: cross-reference resolution
# ---------------------------------------------------------------------------

def test_dangling_reference_detected(run_validate):
    """vocabulary cites C999, which constraints (the only doc that could
    define a C-id) never defines."""
    r = run_validate("dangling_reference")
    assert "PROBLEM(S)" in r.stdout
    assert "vocabulary: dangling C999" in r.stdout
    assert "dangling: ['C999']" in r.stdout


# ---------------------------------------------------------------------------
# Category [4b]: orthogonality (cites_no_ids)
# ---------------------------------------------------------------------------

def test_orthogonality_violation_detected(run_validate):
    """governance declares cites_no_ids: true but its body names C001."""
    r = run_validate("orthogonality_violation")
    assert "PROBLEM(S)" in r.stdout
    assert "VIOLATION" in r.stdout
    assert "governance: declares cites_no_ids but cites ['C001']" in r.stdout


# ---------------------------------------------------------------------------
# The exit-code quirk, pinned down explicitly
# ---------------------------------------------------------------------------

def test_validate_never_sets_a_nonzero_exit_code(run_validate):
    """validate.py has no sys.exit() call anywhere; it always returns 0,
    problems or not. This is documented here so a future change to
    validate.py that starts setting a real exit code is a visible, deliberate
    decision (update these tests), not something a caller was silently
    relying on already."""
    clean = run_validate("happy_path")
    broken = run_validate("dangling_reference")
    assert clean.returncode == 0
    assert broken.returncode == 0
    assert "PASS — no problems" in clean.stdout
    assert "PROBLEM(S)" in broken.stdout
