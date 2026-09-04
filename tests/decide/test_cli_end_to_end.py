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


def test_cli_context_output_preserves_non_ascii_characters(tmp_path):
    """Regression test for Finding 4: context.yaml's yaml.safe_dump must pass
    allow_unicode=True, so the suite's em-dashes / arrows in cited prose come
    through readable rather than escaped as \\uXXXX sequences."""
    repo = tmp_path / "target_repo"
    repo.mkdir()

    result = subprocess.run(
        [sys.executable, "-m", "tooling.decide", "context", str(repo)],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "\\u" not in result.stdout, "non-ASCII characters should not be \\uXXXX-escaped"
    assert "—" in result.stdout or "↔" in result.stdout


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


def test_cli_apply_handles_missing_decisions_file(tmp_path):
    """Regression test: missing decisions file should exit 1 with clean error, not traceback."""
    repo = tmp_path / "target_repo"
    repo.mkdir()
    design_suite_dir = repo / ".design-suite"
    design_suite_dir.mkdir()
    import shutil
    shutil.copy(os.path.join(FIXTURES, "briefs", "valid.yaml"), design_suite_dir / "brief.yaml")

    result = subprocess.run(
        [
            sys.executable, "-m", "tooling.decide", "apply", str(repo),
            "/nonexistent/path/decisions.yaml",
        ],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    assert result.returncode == 1
    assert "Traceback" not in result.stderr, "Should have clean error message, not Python traceback"
    assert "Error:" in result.stderr or "could not read" in result.stderr, "Should have error message in stderr"


def test_cli_context_handles_bad_out_path(tmp_path):
    """Regression test for Finding 1a: a bad --out path (nonexistent parent dir)
    should exit 1 with a clean error message, not a raw FileNotFoundError traceback."""
    repo = tmp_path / "target_repo"
    repo.mkdir()

    result = subprocess.run(
        [
            sys.executable, "-m", "tooling.decide", "context", str(repo),
            "--out", str(tmp_path / "nonexistent_dir" / "context.yaml"),
        ],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    assert result.returncode == 1
    assert "Traceback" not in result.stderr, "Should have clean error message, not Python traceback"
    assert "Error:" in result.stderr


def test_cli_context_handles_composition_missing_target_family(tmp_path):
    """Regression test for Finding 1c: a --composition file missing an expected
    family (e.g. a stale/mismatched vendored suite copy) should exit 1 with a
    clean error message, not a raw KeyError traceback."""
    repo = tmp_path / "target_repo"
    repo.mkdir()

    real_composition = os.path.join(REPO_ROOT, "docs", "composition-1.0.0.md")
    text = open(real_composition, encoding="utf-8").read()
    assert "### F01 · Mandate" in text
    corrupted = text.replace("### F01 · Mandate", "### XX99 · Not Mandate")
    corrupt_path = tmp_path / "composition-corrupt.md"
    corrupt_path.write_text(corrupted, encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable, "-m", "tooling.decide", "context", str(repo),
            "--composition", str(corrupt_path),
        ],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    assert result.returncode == 1
    assert "Traceback" not in result.stderr, "Should have clean error message, not Python traceback"
    assert "Error:" in result.stderr


def test_cli_apply_handles_bad_composition_path(tmp_path):
    """Regression test: bad --composition path should exit 1 with clean error, not traceback."""
    repo = tmp_path / "target_repo"
    repo.mkdir()
    design_suite_dir = repo / ".design-suite"
    design_suite_dir.mkdir()
    import shutil
    shutil.copy(os.path.join(FIXTURES, "briefs", "valid.yaml"), design_suite_dir / "brief.yaml")

    result = subprocess.run(
        [
            sys.executable, "-m", "tooling.decide", "apply", str(repo),
            os.path.join(FIXTURES, "decisions", "all_valid.yaml"),
            "--composition", "/nonexistent/composition.md",
        ],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    assert result.returncode == 1
    assert "Traceback" not in result.stderr, "Should have clean error message, not Python traceback"
