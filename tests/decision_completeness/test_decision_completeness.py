"""Regression tests for tooling/decision_completeness.py.

Run with:

    cd tests/decision_completeness && python3 -m pytest -v
    # or, from the repo root:
    python3 -m pytest tests/decision_completeness/ -v

Requires pytest and pyyaml, same as tests/validate/.

## How this is wired

Unlike validate.py, decision_completeness.py *can* be pointed at an
arbitrary ADR directory and registry path (it takes the ADR dir as a
positional argument and an optional --registry flag) -- it has no hardcoded
file list to work around. conftest.py's `run_decision_completeness` fixture
still copies the real, unmodified tooling/decision_completeness.py and a
snapshot of the real tooling/registry.yaml into a temp directory before
invoking it via subprocess, purely for isolation: these tests should not
depend on -- or be broken by -- the live registry changing as documents in
docs/ evolve. Every ADR fixture here cites real Composition family ids
(F01-F06) that exist in the actual registry today.

## This directory had zero tests before this file

`tests/decision_completeness/fixtures/adrs/` (3 ADRs) and
`fixtures/empty/` (an empty directory) already existed as "worked examples"
referenced from decision_completeness.py's own docstring and README.md, but
neither had ever been run under pytest. `test_baseline_*` below covers
those two pre-existing fixtures; everything else is new, adversarial
fixtures targeting front-matter and status shapes the original examples
never exercised.
"""


def problem_lines(stdout):
    return [ln for ln in stdout.splitlines() if ln.startswith("  - ")]


# ---------------------------------------------------------------------------
# Baseline: the pre-existing fixtures, previously untested by pytest at all.
# ---------------------------------------------------------------------------

def test_baseline_adrs_fixture_reads_clean(run_decision_completeness):
    """The 3-ADR worked example referenced by decision_completeness.py's own
    docstring and README.md. Confirms it actually runs clean against the
    real registry: 3 ADRs read, 0 malformed, and the families they address
    (F01, F09.4, F10.1, F10.2 -- via their parent families F01, F09, F10)
    show as addressed."""
    r = run_decision_completeness("adrs")
    assert r.returncode == 0
    assert "3 ADR(s) read, 0 malformed" in r.stdout
    assert "PASS -- no malformed ADRs, no unresolved citations" in r.stdout
    assert problem_lines(r.stdout) == []
    assert "3/67 addressed, 1 pending" in r.stdout


def test_baseline_empty_directory_fixture(run_decision_completeness):
    """The empty-ADR-directory case, also referenced by the tool's own
    docstring but never actually run under pytest. Zero ADRs, zero
    malformed, every family unaddressed, still a clean PASS -- an empty
    project isn't an error."""
    r = run_decision_completeness("empty")
    assert r.returncode == 0
    assert "0 ADR(s) read, 0 malformed" in r.stdout
    assert "0/67 addressed, 0 pending, 67 unaddressed" in r.stdout
    assert "PASS -- no malformed ADRs, no unresolved citations" in r.stdout


# ---------------------------------------------------------------------------
# Bug fixes: front matter that is syntactically valid YAML (or, in the YAML
# case, not even that) but semantically malformed in ways the original
# examples never exercised. Both fixtures below crashed or silently
# mishandled the input against the unfixed script; decision_completeness.py
# was patched alongside these fixtures/tests.
# ---------------------------------------------------------------------------

def test_families_as_bare_string_reported_cleanly_not_garbage(run_decision_completeness):
    """Bug fix: `families: F05` (a bare YAML scalar) instead of
    `families:\\n  - F05` (a one-element list). `fams = fm.get('families')`
    was truthy (a non-empty string passes `if not fams`), so load_adrs()
    happily stored the *string* "F05" as `families`. The join loop's `for
    cited in adr['families']` then iterated the string character by
    character, producing three bogus problems -- 'F' is not a Composition
    family/segment id, '0' is not..., '5' is not... -- instead of one clear
    one. Confirmed against the unfixed script (exact 3-line garbage output
    below, real transcript). Fixed by explicitly checking
    `isinstance(fams, list)` and treating a non-list as malformed, the same
    as an empty/missing families: key.

    Red (unfixed tooling/decision_completeness.py), transcript:
        SKIPPED  (nothing -- ADR was NOT marked malformed)
        ...
        3 PROBLEM(S)
          - 0001-bare-string.md: 'F' is not a Composition family/segment id
          - 0001-bare-string.md: '0' is not a Composition family/segment id
          - 0001-bare-string.md: '5' is not a Composition family/segment id
    """
    r = run_decision_completeness("adrs_families_not_a_list")
    assert r.returncode == 1
    assert "not a Composition family/segment id" not in r.stdout
    assert "SKIPPED  0001-bare-string.md: families: is not a list" in r.stdout
    assert "1 PROBLEM(S)" in r.stdout
    assert problem_lines(r.stdout) == [
        "  - malformed ADR 0001-bare-string.md: families: is not a list"
    ]
    assert "0/67 addressed" in r.stdout


def test_invalid_yaml_front_matter_reported_cleanly_not_a_crash(run_decision_completeness):
    """Bug fix: the fenced ```yaml block has an unterminated quoted scalar
    (`title: "unterminated quoted string`) -- not just semantically odd
    YAML, but YAML that doesn't parse at all. front_matter() called
    yaml.safe_load() with no try/except, so this crashed the whole tool
    with an uncaught yaml.scanner.ScannerError before a single ADR in the
    directory was scanned -- worse than any 'malformed ADR' report, since
    even ADRs that *would* have parsed fine never got the chance. Confirmed
    crashing against the unfixed script. Fixed by wrapping the
    yaml.safe_load call in try/except yaml.YAMLError and returning None,
    which folds into the existing 'no leading front matter block' malformed
    path."""
    r = run_decision_completeness("adrs_bad_yaml")
    assert r.returncode == 1
    assert "Traceback" not in r.stdout and "Traceback" not in r.stderr
    assert "ScannerError" not in r.stdout and "ScannerError" not in r.stderr
    assert "SKIPPED  0001-bad-yaml.md: no leading ```yaml front matter block" in r.stdout
    assert "1 PROBLEM(S)" in r.stdout


# ---------------------------------------------------------------------------
# Existing-and-correct behavior, previously untested: no code change, these
# just pin down surprising-but-sensible behavior the task specifically asked
# about.
# ---------------------------------------------------------------------------

def test_empty_families_list_is_malformed_same_as_missing(run_decision_completeness):
    """`families: []` -- the key is present, syntactically a list, but
    empty. `if not fams` treats an empty list the same as a missing key
    (both are falsy), so this is already correctly reported as malformed
    rather than silently addressing zero families with no diagnostic at
    all. No code change."""
    r = run_decision_completeness("adrs_empty_families_list")
    assert r.returncode == 1
    assert "SKIPPED  0001-empty-families.md: front matter has no families: list" in r.stdout
    assert problem_lines(r.stdout) == [
        "  - malformed ADR 0001-empty-families.md: front matter has no families: list"
    ]


def test_lowercase_family_id_still_resolves(run_decision_completeness):
    """`families:\\n  - f01` (lowercase) instead of `F01`. The join loop
    does `cited = str(cited).strip().upper()` before matching against the
    registry, so this already resolves correctly to F01 (Mandate) and
    counts as addressed. No code change -- confirms the normalization is
    real, not just present-looking."""
    r = run_decision_completeness("adrs_lowercase_family")
    assert r.returncode == 0
    assert "1/67 addressed, 0 pending, 66 unaddressed" in r.stdout
    assert "F01   Mandate                      ok           0001-lowercase.md (F01)" in r.stdout


def test_nonstandard_status_value_lands_in_pending_not_crash_or_silent_accept(run_decision_completeness):
    """`status: withdrawn` -- not one of the values decision_completeness.py's
    docstring names by example (accepted/proposed/rejected/superseded).
    Only `status == 'accepted'` ever counts as addressing a family, so any
    other string -- named in the docs or invented by a team -- correctly
    falls through to the 'pending' bucket, shown with its literal status
    value, rather than crashing on an unrecognized enum or silently being
    treated as accepted. No code change."""
    r = run_decision_completeness("adrs_nonstandard_status")
    assert r.returncode == 0
    assert "0/67 addressed, 1 pending, 66 unaddressed" in r.stdout
    assert "F02   Audience                     pending      0001-withdrawn.md [withdrawn]" in r.stdout


def test_one_accepted_one_rejected_same_family_prefers_accepted(run_decision_completeness):
    """Two ADRs address the same family (F03, Position): one accepted, one
    an earlier rejected alternative. `accepted = [e for e in entries if e[1]
    == 'accepted']` -- if that list is non-empty the family reports 'ok',
    sourced *only* from the accepted entries; the rejected ADR is correctly
    excluded from the family's 'by' listing (it did not, in fact, decide
    anything), and does not downgrade the family to 'pending' or cause any
    conflict/ambiguity report. This is sensible: no code change, but this
    exact scenario (task's own suggested case) had no coverage before."""
    r = run_decision_completeness("adrs_conflicting_status")
    assert r.returncode == 0
    assert "1/67 addressed, 0 pending, 66 unaddressed" in r.stdout
    line = "  F03   Position                     ok           0001a-accepted.md (F03)"
    assert line in r.stdout
    # the rejected ADR must not appear in F03's "by" listing
    for ln in r.stdout.splitlines():
        if ln.strip().startswith("F03 "):
            assert "0001b-rejected" not in ln


def test_nested_adr_directories_are_actually_scanned(run_decision_completeness):
    """decision_completeness.py's own docstring claims ADRs may live
    'anywhere under the directory you point this at (scanned recursively)'.
    This fixture puts a single ADR two directories deep
    (adrs_nested/deep/deeper/0001-nested.md) to verify that claim against
    real glob('**/*.md', recursive=True) behavior rather than trusting the
    docstring. No code change -- the claim holds."""
    r = run_decision_completeness("adrs_nested")
    assert r.returncode == 0
    assert "1 ADR(s) read, 0 malformed" in r.stdout
    assert "1/67 addressed, 0 pending, 66 unaddressed" in r.stdout
    assert (
        "F04   Risk posture                 ok           deep/deeper/0001-nested.md (F04)"
        in r.stdout
    )
