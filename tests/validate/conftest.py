"""Shared harness for tests/validate/.

validate.py resolves the docs it reads from its own file location
(``os.path.dirname(os.path.abspath(__file__))/../docs``) and has no flag or
env var to point it elsewhere -- it also hardcodes the exact nine document
filenames it opens, unconditionally, before any check runs. So to run it
against a synthetic fixture instead of the real docs/, the only option that
doesn't touch validate.py's production behavior is to give it the directory
layout it already expects: copy the *real*, unmodified tooling/validate.py
into a throwaway temp directory next to a copy of one fixture's docs/, then
invoke it there. That's what `run_validate` below does.
"""
import os
import shutil
import subprocess
import sys
import tempfile

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(HERE))
REAL_VALIDATE = os.path.join(REPO_ROOT, "tooling", "validate.py")
FIXTURES_DIR = os.path.join(HERE, "fixtures")


@pytest.fixture
def run_validate(tmp_path):
    """Return a function `run_validate(case_name)` that runs the real
    tooling/validate.py against the fixture at fixtures/<case_name>/docs and
    returns the finished subprocess.CompletedProcess (stdout/stderr captured
    as text). Never touches the repo's own tooling/registry.yaml -- the
    validate.py copy writes its registry.yaml into the temp dir instead,
    since it derives that path from its own (copied) location too.
    """

    def _run(case_name):
        fixture_docs = os.path.join(FIXTURES_DIR, case_name, "docs")
        if not os.path.isdir(fixture_docs):
            raise FileNotFoundError(f"no such fixture: {fixture_docs}")

        work = tmp_path / case_name
        tooling_dir = work / "tooling"
        docs_dir = work / "docs"
        tooling_dir.mkdir(parents=True)
        shutil.copy(REAL_VALIDATE, tooling_dir / "validate.py")
        shutil.copytree(fixture_docs, docs_dir)

        return subprocess.run(
            [sys.executable, "validate.py"],
            cwd=str(tooling_dir),
            capture_output=True,
            text=True,
            timeout=30,
        )

    return _run
