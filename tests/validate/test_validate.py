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


# ---------------------------------------------------------------------------
# Adversarial cases -- front matter that is syntactically valid YAML but
# semantically malformed in ways the fixtures above never exercise. Every
# case in this section was run against validate.py *before* being pinned
# down here; several of them crashed the (unfixed) script outright instead
# of reporting a clean PROBLEM -- those are noted as bug fixes below, with
# validate.py itself patched alongside the new fixture/test. The rest verify
# existing-and-correct behavior that simply had no regression coverage yet.
# ---------------------------------------------------------------------------

def test_missing_version_key_reported_cleanly_not_a_crash(run_validate):
    """Bug fix: front matter syntactically valid but missing the required
    `version:` key entirely used to crash validate.py with an unhandled
    KeyError in the [1] print statement (`fm['version']`), before any
    problem was ever printed. Confirmed against the unfixed script (real
    KeyError traceback, no PROBLEM(S) summary at all); fixed by having
    front_matter's caller use `fm.get('version', ...)` and explicitly flag
    the missing key as a problem."""
    r = run_validate("missing_version_key")
    assert r.returncode == 0
    assert "Traceback" not in r.stdout and "Traceback" not in r.stderr
    assert "PROBLEM(S)" in r.stdout
    assert "vocabulary: front matter missing 'version'" in r.stdout


def test_missing_tier_key_reported_cleanly_not_a_crash(run_validate):
    """Bug fix: same crash class as the version case above, but for the
    required `tier:` key (`fm['tier']` in the same print statement).
    Confirmed crashing with KeyError against the unfixed script; fixed the
    same way, and this case was already correctly detected as a tier
    mismatch (`declared_tier` computed via `.get()`) once the print
    statement itself stopped crashing."""
    r = run_validate("missing_tier_key")
    assert r.returncode == 0
    assert "Traceback" not in r.stdout and "Traceback" not in r.stderr
    assert "PROBLEM(S)" in r.stdout
    assert "vocabulary: tier None != 0" in r.stdout


def test_front_matter_yaml_that_parses_to_a_list_not_a_dict(run_validate):
    """Bug fix: the fenced ```yaml block is syntactically valid YAML but
    parses to a list, not a mapping. Confirmed crashing with
    `AttributeError: 'list' object has no attribute 'get'` on the unfixed
    script's very first `fm.get('tier')` call. Fixed by having
    front_matter() itself reject non-dict results, folding this into the
    existing 'no front matter' problem path."""
    r = run_validate("front_matter_not_a_dict")
    assert r.returncode == 0
    assert "Traceback" not in r.stdout and "Traceback" not in r.stderr
    assert "PROBLEM(S)" in r.stdout
    assert "vocabulary: no front matter" in r.stdout


def test_front_matter_invalid_yaml_syntax(run_validate):
    """Bug fix: the fenced ```yaml block is not parseable YAML at all (an
    unterminated quoted scalar). Confirmed crashing with an uncaught
    yaml.scanner.ScannerError before a single line of validator output was
    printed. Fixed by wrapping the yaml.safe_load call in front_matter() in
    try/except yaml.YAMLError, folding this into the same 'no front matter'
    path as the case above."""
    r = run_validate("front_matter_invalid_yaml")
    assert r.returncode == 0
    assert "Traceback" not in r.stdout and "Traceback" not in r.stderr
    assert "ScannerError" not in r.stdout and "ScannerError" not in r.stderr
    assert "PROBLEM(S)" in r.stdout
    assert "vocabulary: no front matter" in r.stdout


def test_no_front_matter_block_at_all(run_validate):
    """Bug fix: a document with no fenced ```yaml block at all -- not a
    malformed one, just absent. front_matter() already returned None for
    this case pre-fix, and check [1] already handled it gracefully
    ('no front matter'), but check [2]'s `d['fm'].get('depends')` had no
    equivalent guard and crashed with `AttributeError: 'NoneType' object has
    no attribute 'get'` as soon as it reached that document. Confirmed
    crashing against the unfixed script. Fixed by guarding with
    `(d['fm'] or {}).get(...)`, matching the same fix applied to the
    registry-build step and the [4b] orthogonality check, which had the
    identical latent bug for the same reason."""
    r = run_validate("no_front_matter_block_at_all")
    assert r.returncode == 0
    assert "Traceback" not in r.stdout and "Traceback" not in r.stderr
    assert "PROBLEM(S)" in r.stdout
    assert "vocabulary: no front matter" in r.stdout


def test_governance_declaring_illegal_depends_reported_not_crashed(run_validate):
    """Bug fix: governance (tier None) is given a `depends:` entry, which is
    illegal (governance cites no identifiers and sits outside the tier
    system). Confirmed crashing the unfixed script with
    `TypeError: '<' not supported between instances of 'int' and
    'NoneType'` in the verdict computation (`dt < mt` where `mt` -- governance's
    own tier -- is None), meaning the one case this check most needs to
    catch (governance breaking its own orthogonality-adjacent rule) crashed
    instead of being flagged. Fixed by short-circuiting to ILLEGAL whenever
    either side's tier is None."""
    r = run_validate("governance_with_illegal_depends")
    assert r.returncode == 0
    assert "Traceback" not in r.stdout and "Traceback" not in r.stderr
    assert "PROBLEM(S)" in r.stdout
    assert "ILLEGAL" in r.stdout
    assert "governance -> constraints: not downward" in r.stdout


def test_exports_declared_but_body_defines_nothing_is_a_mismatch(run_validate):
    """Bug fix: verification declares `exports: X001` but its body defines
    zero X-ids. The [1] MISMATCH loop (`for ns, v in sorted(byns.items())`)
    only ever iterated namespaces actually found in the body -- a namespace
    that is declared but never defined at all was never visited, so `ok`
    silently stayed True and the row printed 'ok'. Confirmed against the
    unfixed script: it printed 'declared X001 ... actual  ok' with zero
    problems reported. Fixed by iterating the union of declared and actual
    namespaces, not just the actual ones."""
    r = run_validate("exports_declared_but_zero_ids")
    assert r.returncode == 0
    assert "PROBLEM(S)" in r.stdout
    assert "MISMATCH" in r.stdout
    assert "verification: declares X001, actual" in r.stdout


def test_duplicate_id_check_is_exercised(run_validate):
    """Existing-and-correct behavior, previously untested: the DUPLICATE ID
    check (`if i in allids: problems.append(...)`) has no fixture anywhere
    in this suite before now. Composition defines F01 twice in its own
    body. No code change -- this only adds coverage for a check that was
    already working."""
    r = run_validate("duplicate_id")
    assert r.returncode == 0
    assert "PROBLEM(S)" in r.stdout
    assert "DUPLICATE ID F01 in composition and composition" in r.stdout


def test_depends_on_a_document_name_not_in_docs_at_all(run_validate):
    """Existing-and-correct behavior, previously untested: `depends:` names
    a document ('Nonexistent') that isn't in the TIER/DOCS dicts at all --
    not just a not-yet-built one, a nonexistent one (e.g. a typo). Confirms
    this is still cleanly flagged ILLEGAL and tagged [TARGET NOT BUILT], not
    silently skipped. No code change."""
    r = run_validate("depends_on_nonexistent_doc")
    assert r.returncode == 0
    assert "PROBLEM(S)" in r.stdout
    assert "ILLEGAL" in r.stdout
    assert "[TARGET NOT BUILT]" in r.stdout
    assert "anatomy -> nonexistent: not downward" in r.stdout


def test_tier_declared_as_wrong_type_not_just_wrong_value(run_validate):
    """Existing-and-correct behavior, previously untested: `tier:` is
    present but is a quoted string ("zero") rather than the expected int.
    The only existing tier-related fixture (dependency_direction_violation)
    exercises a *correct*-type tier used illegally in `depends:`; nothing
    exercised a tier of the wrong Python type in a document's own front
    matter. Confirms `declared_tier != TIER[name]` still catches this. No
    code change."""
    r = run_validate("tier_wrong_type")
    assert r.returncode == 0
    assert "PROBLEM(S)" in r.stdout
    assert "vocabulary: tier zero != 0" in r.stdout


def test_empty_exports_declared_while_body_defines_something(run_validate):
    """Existing-and-correct behavior, previously untested: the mirror image
    of the exports_declared_but_zero_ids bug fix above -- `exports:` is
    present but empty (parses to YAML null) while the body *does* define
    V-001. Unlike the bug case, this direction was already caught correctly
    (V-001 is in `byns`, so the MISMATCH loop actually visits it). No code
    change; documents the boundary precisely."""
    r = run_validate("empty_exports_declared")
    assert r.returncode == 0
    assert "PROBLEM(S)" in r.stdout
    assert "MISMATCH" in r.stdout
    assert "vocabulary: declares None, actual V-001" in r.stdout


def test_id_heading_with_extra_whitespace_is_not_recognized_as_defined(run_validate):
    """Known sharp edge, not fixed: composition's F01 heading has an extra
    space before the ` · ` separator ('### F01  · Widget mandate'). The
    defined() regex requires the exact single-space separator, so this ID is
    silently *not* extracted as defined -- every other document that
    legitimately cites F01 (decision, implementation, diagnosis) then
    reports a false 'dangling F01', and composition's own exports check
    reports a MISMATCH for an ID that a human reading the document would
    clearly see as defined. Documented here as strict-by-design behavior
    (loosening the definition regexes trades an easy-to-see false positive
    for a much harder-to-see false negative, and the suite's whole contract
    -- suite-architecture.md -- is exact ID formatting) rather than changed."""
    r = run_validate("composition_heading_double_space_before_middot")
    assert r.returncode == 0
    assert "PROBLEM(S)" in r.stdout
    assert "composition: declares F01, actual" in r.stdout
    assert "decision: dangling F01" in r.stdout
    assert "implementation: dangling F01" in r.stdout
    assert "diagnosis: dangling F01" in r.stdout
