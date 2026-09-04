import os
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FIXTURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")


def test_cli_context_then_apply_end_to_end(tmp_path):
    repo = tmp_path / "target_repo"
    repo.mkdir()
    design_suite_dir = repo / ".design-suite"
    design_suite_dir.mkdir()
    import shutil
    shutil.copy(os.path.join(FIXTURES, "briefs", "valid.yaml"), design_suite_dir / "brief.yaml")

    context_result = subprocess.run(
        [sys.executable, "-m", "tooling.decide", "context", str(repo)],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    assert context_result.returncode == 0, context_result.stderr
    import yaml
    ctx = yaml.safe_load(context_result.stdout)
    assert "F01" in ctx["families"]
    assert "SaaS product" in ctx["brief"]["purpose"]

    apply_result = subprocess.run(
        [
            sys.executable, "-m", "tooling.decide", "apply", str(repo),
            os.path.join(FIXTURES, "decisions", "all_valid.yaml"),
        ],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    assert apply_result.returncode == 0, apply_result.stderr
    summary = yaml.safe_load(apply_result.stdout)
    assert len(summary["written"]) == 4
    assert summary["rejected"] == []
    assert os.path.isdir(repo / "adr")
    assert len(os.listdir(repo / "adr")) == 4


def test_cli_apply_exits_nonzero_on_rejection(tmp_path):
    repo = tmp_path / "target_repo"
    repo.mkdir()

    result = subprocess.run(
        [
            sys.executable, "-m", "tooling.decide", "apply", str(repo),
            os.path.join(FIXTURES, "decisions", "missing_bound_citation.yaml"),
        ],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    assert result.returncode == 1
