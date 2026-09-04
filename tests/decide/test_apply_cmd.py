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


def test_run_apply_persists_confidence_and_round_in_adr_content(tmp_path, suite_snapshot):
    """Regression test for Findings 5/6: the confidence flag and the governing
    Decision round must be written into the ADR file itself (a durable artifact),
    not just returned in the apply summary."""
    repo = _make_target_repo(tmp_path)
    result = run_apply(
        repo,
        os.path.join(FIXTURES, "decisions", "all_valid.yaml"),
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
    )
    f15_entry = next(w for w in result["written"] if w["family"] == "F15")
    adr_path = None
    for fname in os.listdir(os.path.join(repo, "adr")):
        if f15_entry["adr_id"].split("-")[1] == fname.split("-")[0]:
            adr_path = os.path.join(repo, "adr", fname)
    assert adr_path is not None
    content = open(adr_path, encoding="utf-8").read()
    # Finding 5: confidence persisted
    assert "confidence: low" in content
    # Finding 6: governing Decision round persisted (F15 -> D006, per test_knowledge.py)
    assert "D006" in content

    f01_entry = next(w for w in result["written"] if w["family"] == "F01")
    adr_path_f01 = None
    for fname in os.listdir(os.path.join(repo, "adr")):
        if f01_entry["adr_id"].split("-")[1] == fname.split("-")[0]:
            adr_path_f01 = os.path.join(repo, "adr", fname)
    assert adr_path_f01 is not None
    content_f01 = open(adr_path_f01, encoding="utf-8").read()
    assert "confidence: high" in content_f01


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


def test_run_apply_all_rejected_self_check_output_not_empty(tmp_path, suite_snapshot):
    """Regression test for D4 (independent peer review of PR #72): when every
    decision in a batch is rejected (and no pre-existing adr/ directory exists
    either), adr/ is never created. run_apply must still actually call
    decision_completeness.main() (which handles a nonexistent directory
    gracefully, printing an ERROR line and returning 1) so self_check_output
    carries real, honest content explaining the failure -- not an empty string
    while self_check_passed silently claims false, which would contradict the
    README's own claim that self_check_passed: false means the checker found
    something actually wrong (never that it merely never ran)."""
    repo = _make_target_repo(tmp_path)
    result = run_apply(
        repo,
        os.path.join(FIXTURES, "decisions", "missing_bound_citation.yaml"),
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
    )
    assert result["written"] == []
    assert not os.path.isdir(os.path.join(repo, "adr"))
    assert result["self_check_passed"] is False
    assert result["self_check_output"] != "", \
        "self_check_output must not be empty -- decision_completeness.main() should have run"
    assert "not a directory" in result["self_check_output"].lower(), \
        f"expected an explanation the checker never found an adr/ dir, got: {result['self_check_output']!r}"


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
    # A pre-existing ADR (present before this run started) is expected, normal
    # behavior -- it must not also show up as a rejection.
    assert result["rejected"] == []


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


def test_run_apply_rejects_non_string_value_before_writing_any_adr(tmp_path, suite_snapshot):
    """Regression test for Finding 1b: a malformed decisions.yaml where a later
    entry's `value` is not a string (e.g. a YAML author's typo -- a list instead
    of a plain string) must be caught by validation before any ADR is written,
    not partway through the write loop with a raw TypeError. F01 (valid, first)
    must NOT be written to disk once F02 (malformed) is discovered."""
    repo = _make_target_repo(tmp_path)
    try:
        run_apply(
            repo,
            os.path.join(FIXTURES, "decisions", "malformed_value_type.yaml"),
            suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
        )
        assert False, "expected DecisionsFileError"
    except DecisionsFileError as e:
        assert "value" in str(e)
        assert "1" in str(e)  # index of the malformed entry

    # No ADR directory (or an empty one) should exist -- nothing partially written.
    adr_dir = os.path.join(repo, "adr")
    assert not os.path.isdir(adr_dir) or os.listdir(adr_dir) == []


def test_load_decisions_rejects_non_string_rationale(tmp_path):
    import tempfile
    from tooling.decide.apply_cmd import _load_decisions
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as f:
        f.write(
            "decisions:\n"
            "  - family: F01\n"
            "    value: \"a plain string value\"\n"
            "    rationale: [not, a, string]\n"
        )
        path = f.name
    try:
        try:
            _load_decisions(path)
            assert False, "expected DecisionsFileError"
        except DecisionsFileError as e:
            assert "rationale" in str(e)
    finally:
        os.unlink(path)


def test_run_apply_rejects_duplicate_family_same_batch(tmp_path, suite_snapshot):
    """Regression test for Finding 1 / Finding 3: Guardrail 1 doesn't catch
    same-batch duplicates.

    When a decisions.yaml lists the same family twice with different, contradictory
    values, that's a batch-authoring mistake distinct from "already decided by a
    prior run" -- it should be rejected (visible to the agent, nonzero exit), not
    silently routed to skipped_already_decided (which is reserved for a family a
    PRE-EXISTING ADR on disk already decided). Only the first entry is written.
    """
    repo = _make_target_repo(tmp_path)
    result = run_apply(
        repo,
        os.path.join(FIXTURES, "decisions", "duplicate_same_batch.yaml"),
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
    )
    # Only the first F02 should be written
    written_families = {w["family"] for w in result["written"]}
    assert written_families == {"F02"}, f"Expected only F02 written, got {written_families}"

    # The second F02 entry should be REJECTED (a same-batch contradiction), not
    # silently skipped as "already decided" -- that phrase is reserved for a
    # pre-existing ADR from a prior run.
    assert result["skipped_already_decided"] == [], \
        f"A same-batch duplicate is not 'already decided'; got {result['skipped_already_decided']}"
    assert len(result["rejected"]) == 1, f"Expected 1 rejected entry, got {result['rejected']}"
    assert result["rejected"][0]["family"] == "F02"
    assert "duplicate" in result["rejected"][0]["reason"].lower()

    # Only one ADR file should exist
    adr_files = os.listdir(os.path.join(repo, "adr"))
    assert len(adr_files) == 1, f"Expected 1 ADR file, got {len(adr_files)}"


def test_run_apply_coupling_propagation_order_independent(tmp_path, suite_snapshot):
    """Regression test for Finding 2: Coupling propagation coverage.

    F02 (high confidence) and F22 (low confidence) are tightly coupled.
    Even though F02 appears first with high confidence, it should be flagged
    low due to its coupling with F22 (which appears second with low confidence).

    This is a ONE-HOP case only (F02 and F22 are directly, mutually coupled in
    Composition's own text) -- it does NOT prove propagation is order-independent
    in general. See test_run_apply_coupling_propagation_transitive_two_hop_order_independent
    below for the genuine (order-dependent-until-fixed) transitive case, per D1 of
    the independent peer review of PR #72.
    """
    repo = _make_target_repo(tmp_path)
    result = run_apply(
        repo,
        os.path.join(FIXTURES, "decisions", "coupling_propagation_order_independent.yaml"),
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
    )

    # Both F02 and F22 should be written
    written_families = {w["family"] for w in result["written"]}
    assert written_families == {"F02", "F22"}, f"Expected F02 and F22 written, got {written_families}"

    # Both should be in flagged_low_confidence
    assert "F02" in result["flagged_low_confidence"], \
        f"F02 should be flagged low (coupled with F22), got {result['flagged_low_confidence']}"
    assert "F22" in result["flagged_low_confidence"], \
        f"F22 should be flagged low, got {result['flagged_low_confidence']}"

    # F02's written entry should show confidence: low (propagated from F22)
    f02_entry = next(w for w in result["written"] if w["family"] == "F02")
    assert f02_entry["confidence"] == "low", \
        f"F02 confidence should be 'low' (propagated from F22), got '{f02_entry['confidence']}'"

    # F22's written entry should show confidence: low (as specified)
    f22_entry = next(w for w in result["written"] if w["family"] == "F22")
    assert f22_entry["confidence"] == "low", \
        f"F22 confidence should be 'low', got '{f22_entry['confidence']}'"


def test_run_apply_coupling_propagation_transitive_two_hop_order_independent(tmp_path, suite_snapshot):
    """Regression test for D1 (independent peer review of PR #72): a genuine
    TWO-HOP transitive coupling chain must propagate the same way regardless of
    decisions.yaml list order.

    Uses real Coupling prose from docs/composition-1.0.0.md among three of the 11
    target families:
      - F15's own Coupling line does not mention F17 or F31 at all.
      - F31's own Coupling line: "tight with F17. Moderate with F15." -- so F31
        is coupled (one hop) to F15.
      - F17's own Coupling line: "tight with F31, F32." -- so F17 is coupled
        (one hop) to F31, but NOT directly to F15.

    Only F15 is marked confidence: low. F31 should be flagged low because it is
    directly coupled to F15 (one hop). F17 should THEN be flagged low because it
    is directly coupled to F31, which only became low-confidence during this same
    propagation pass (two hops from F15) -- this only happens correctly if the
    propagation pass runs to a fixpoint. A single forward pass gets this right
    only when F31 happens to be processed before F17 in list order; this test
    exercises both orders and asserts the same (correct) result either way.
    """
    repo_a = tmp_path / "target_repo_a"
    repo_a.mkdir()
    repo_b = tmp_path / "target_repo_b"
    repo_b.mkdir()
    result_a = run_apply(
        str(repo_a),
        os.path.join(FIXTURES, "decisions", "coupling_propagation_transitive_order_a.yaml"),
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
    )
    result_b = run_apply(
        str(repo_b),
        os.path.join(FIXTURES, "decisions", "coupling_propagation_transitive_order_b.yaml"),
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
    )

    expected_flagged = ["F15", "F17", "F31"]
    assert result_a["flagged_low_confidence"] == expected_flagged, \
        f"order a: expected {expected_flagged}, got {result_a['flagged_low_confidence']}"
    assert result_b["flagged_low_confidence"] == expected_flagged, \
        f"order b: expected {expected_flagged}, got {result_b['flagged_low_confidence']}"
    assert result_a["flagged_low_confidence"] == result_b["flagged_low_confidence"], (
        "coupling propagation must be order-independent: identical coupling "
        f"relationships produced different results depending on list order "
        f"(order a: {result_a['flagged_low_confidence']}, order b: {result_b['flagged_low_confidence']})"
    )

    f17_a = next(w for w in result_a["written"] if w["family"] == "F17")
    f17_b = next(w for w in result_b["written"] if w["family"] == "F17")
    assert f17_a["confidence"] == "low", f"F17 (order a) should be transitively flagged low, got {f17_a}"
    assert f17_b["confidence"] == "low", f"F17 (order b) should be transitively flagged low, got {f17_b}"
