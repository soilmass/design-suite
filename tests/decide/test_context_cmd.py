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
