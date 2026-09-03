"""Shared harness for tests/decision_completeness/.

decision_completeness.py takes the ADR directory as a positional argument and
an optional --registry flag (defaulting to tooling/registry.yaml next to the
script itself), so unlike validate.py it *can* be pointed at an arbitrary
location without copying anything into a fake repo layout. Still, to keep
these tests isolated from this repo's own (evolving) tooling/registry.yaml,
`run_decision_completeness` below copies the *real, unmodified*
tooling/decision_completeness.py and a snapshot of the *real*
tooling/registry.yaml into a fresh temp directory, then invokes the tool
there via subprocess against a copy of the requested fixture directory. This
never touches or depends on the live state of either file in the repo.
"""
import os
import shutil
import subprocess
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(HERE))
REAL_TOOL = os.path.join(REPO_ROOT, "tooling", "decision_completeness.py")
REAL_REGISTRY = os.path.join(REPO_ROOT, "tooling", "registry.yaml")
FIXTURES_DIR = os.path.join(HERE, "fixtures")


@pytest.fixture
def run_decision_completeness(tmp_path):
    """Return a function `run_decision_completeness(case_name, extra_args=None)`
    that runs the real tooling/decision_completeness.py against
    fixtures/<case_name>/ (copied into a temp dir) using a snapshot of the
    real tooling/registry.yaml, and returns the finished
    subprocess.CompletedProcess (stdout/stderr captured as text).
    """

    def _run(case_name, extra_args=None):
        fixture_dir = os.path.join(FIXTURES_DIR, case_name)
        if not os.path.isdir(fixture_dir):
            raise FileNotFoundError(f"no such fixture: {fixture_dir}")

        work = tmp_path / case_name
        tool_dir = work / "tool"
        adrs_dir = work / "adrs"
        registry_path = work / "registry.yaml"
        tool_dir.mkdir(parents=True)
        shutil.copy(REAL_TOOL, tool_dir / "decision_completeness.py")
        shutil.copytree(fixture_dir, adrs_dir)
        shutil.copy(REAL_REGISTRY, registry_path)

        args = [
            sys.executable,
            "decision_completeness.py",
            str(adrs_dir),
            "--registry",
            str(registry_path),
        ]
        if extra_args:
            args += extra_args

        return subprocess.run(
            args,
            cwd=str(tool_dir),
            capture_output=True,
            text=True,
            timeout=30,
        )

    return _run
