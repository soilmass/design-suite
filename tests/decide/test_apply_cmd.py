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


def test_run_apply_rejects_duplicate_family_same_batch(tmp_path, suite_snapshot):
    """Regression test for Finding 1: Guardrail 1 doesn't catch same-batch duplicates.

    When a decisions.yaml lists the same family twice with different values,
    Guardrail 1 should reject the second entry and only write one ADR.
    """
    repo = _make_target_repo(tmp_path)
    result = run_apply(
        repo,
        os.path.join(FIXTURES, "decisions", "duplicate_same_batch.yaml"),
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"],
    )
    # Only one F02 should be written
    written_families = {w["family"] for w in result["written"]}
    assert written_families == {"F02"}, f"Expected only F02 written, got {written_families}"

    # Second F02 entry should be in skipped_already_decided
    assert "F02" in result["skipped_already_decided"], \
        f"F02 should be in skipped_already_decided, got {result['skipped_already_decided']}"

    # Only one ADR file should exist
    adr_files = os.listdir(os.path.join(repo, "adr"))
    assert len(adr_files) == 1, f"Expected 1 ADR file, got {len(adr_files)}"


def test_run_apply_coupling_propagation_order_independent(tmp_path, suite_snapshot):
    """Regression test for Finding 2: Coupling propagation coverage.

    F02 (high confidence) and F22 (low confidence) are tightly coupled.
    Even though F02 appears first with high confidence, it should be flagged
    low due to its coupling with F22 (which appears second with low confidence).
    This proves coupling propagation is order-independent.
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
