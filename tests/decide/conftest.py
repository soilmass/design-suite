"""Shared harness for tests/decide/. Mirrors tests/decision_completeness/conftest.py:
snapshot the real, unmodified suite documents and tooling/registry.yaml into a fresh
temp directory per test, so tests exercise real content without depending on the
live repo's evolving state between test runs.
"""
import os
import shutil

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(HERE))
DOCS_DIR = os.path.join(REPO_ROOT, "docs")
REAL_REGISTRY = os.path.join(REPO_ROOT, "tooling", "registry.yaml")
REAL_DECISION_COMPLETENESS = os.path.join(REPO_ROOT, "tooling", "decision_completeness.py")
FIXTURES_DIR = os.path.join(HERE, "fixtures")


@pytest.fixture
def suite_snapshot(tmp_path):
    """Copy the real docs/composition-1.0.0.md, docs/constraints-1.0.0.md,
    docs/decision-1.0.0.md, tooling/registry.yaml, and tooling/decision_completeness.py
    into tmp_path, and return a dict of their new paths."""
    dest_docs = tmp_path / "docs"
    dest_docs.mkdir()
    paths = {}
    for name in ("composition-1.0.0.md", "constraints-1.0.0.md", "decision-1.0.0.md"):
        src = os.path.join(DOCS_DIR, name)
        dst = dest_docs / name
        shutil.copy(src, dst)
        key = name.split("-")[0]  # "composition", "constraints", "decision"
        paths[key] = str(dst)
    dest_tooling = tmp_path / "tooling"
    dest_tooling.mkdir()
    shutil.copy(REAL_REGISTRY, dest_tooling / "registry.yaml")
    paths["registry"] = str(dest_tooling / "registry.yaml")
    shutil.copy(REAL_DECISION_COMPLETENESS, dest_tooling / "decision_completeness.py")
    paths["decision_completeness"] = str(dest_tooling / "decision_completeness.py")
    return paths
