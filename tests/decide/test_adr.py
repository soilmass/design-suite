import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
from tooling.decide.adr import render_adr, next_adr_id, slugify


def test_slugify():
    assert slugify("Primary conversion goal is trial signup") == "primary-conversion-goal-is-trial-signup"
    assert slugify("F31/F32: Typography & Color!!") == "f31-f32-typography-color"


def test_render_adr_front_matter_matches_decision_completeness_regex():
    import re
    content = render_adr(
        adr_id="ADR-0001",
        title="Primary conversion goal is trial signup",
        families=["F01"],
        context="This is the context.",
        decision="This is the decision.",
        consequences="This is the consequences.",
        date="2026-09-04",
    )
    # the exact regex tooling/decision_completeness.py's front_matter() uses
    m = re.match(r"```yaml\n(.*?)\n```", content, re.S)
    assert m is not None
    import yaml
    fm = yaml.safe_load(m.group(1))
    assert fm["id"] == "ADR-0001"
    assert fm["title"] == "Primary conversion goal is trial signup"
    assert fm["families"] == ["F01"]
    assert fm["status"] == "accepted"
    assert fm["date"] == "2026-09-04"
    assert "## Context" in content
    assert "## Decision" in content
    assert "## Consequences" in content
    assert "This is the context." in content


def test_next_adr_id_empty_dir(tmp_path):
    assert next_adr_id(str(tmp_path)) == "ADR-0001"


def test_next_adr_id_increments(tmp_path):
    (tmp_path / "0001-something.md").write_text(
        '```yaml\nid: ADR-0001\ntitle: x\nfamilies: [F01]\n```\n# x\n', encoding="utf-8"
    )
    (tmp_path / "0002-other.md").write_text(
        '```yaml\nid: ADR-0002\ntitle: y\nfamilies: [F02]\n```\n# y\n', encoding="utf-8"
    )
    assert next_adr_id(str(tmp_path)) == "ADR-0003"


def test_next_adr_id_ignores_malformed(tmp_path):
    (tmp_path / "0001-good.md").write_text(
        '```yaml\nid: ADR-0005\ntitle: x\nfamilies: [F01]\n```\n# x\n', encoding="utf-8"
    )
    (tmp_path / "0002-bad.md").write_text("not an ADR at all", encoding="utf-8")
    assert next_adr_id(str(tmp_path)) == "ADR-0006"


def test_already_decided_families_empty_dir_that_does_not_exist(tmp_path):
    from tooling.decide.adr import already_decided_families
    missing = str(tmp_path / "does_not_exist")
    assert already_decided_families(missing, ["F01", "F02"]) == set()


def test_already_decided_families_only_accepted_status_counts(tmp_path):
    from tooling.decide.adr import already_decided_families
    (tmp_path / "0001-accepted.md").write_text(
        '```yaml\nid: ADR-0001\ntitle: x\nstatus: accepted\nfamilies: [F01]\n```\n# x\n',
        encoding="utf-8",
    )
    (tmp_path / "0002-proposed.md").write_text(
        '```yaml\nid: ADR-0002\ntitle: y\nstatus: proposed\nfamilies: [F02]\n```\n# y\n',
        encoding="utf-8",
    )
    result = already_decided_families(str(tmp_path), ["F01", "F02", "F15"])
    assert result == {"F01"}


def test_already_decided_families_ignores_non_target_families(tmp_path):
    from tooling.decide.adr import already_decided_families
    (tmp_path / "0001-other.md").write_text(
        '```yaml\nid: ADR-0001\ntitle: x\nstatus: accepted\nfamilies: [F99]\n```\n# x\n',
        encoding="utf-8",
    )
    result = already_decided_families(str(tmp_path), ["F01", "F02"])
    assert result == set()


def test_already_decided_families_whole_family_matches_segment_citation(tmp_path):
    """Whole-family target (F01) should match if ADR cites any segment under it (F01.2)."""
    from tooling.decide.adr import already_decided_families
    (tmp_path / "0001-segment.md").write_text(
        '```yaml\nid: ADR-0001\ntitle: x\nstatus: accepted\nfamilies: [F01.2]\n```\n# x\n',
        encoding="utf-8",
    )
    # Target is whole family F01; ADR cites segment F01.2
    result = already_decided_families(str(tmp_path), ["F01"])
    assert result == {"F01"}


def test_already_decided_families_segment_does_not_match_parent_only(tmp_path):
    """Segment target (F05.1) should NOT match if ADR cites only parent family (F05)."""
    from tooling.decide.adr import already_decided_families
    (tmp_path / "0001-parent.md").write_text(
        '```yaml\nid: ADR-0001\ntitle: x\nstatus: accepted\nfamilies: [F05]\n```\n# x\n',
        encoding="utf-8",
    )
    # Target is segment F05.1; ADR cites only parent F05
    result = already_decided_families(str(tmp_path), ["F05.1"])
    assert result == set()


def test_already_decided_families_segment_matches_exact(tmp_path):
    """Segment target (F05.1) should match if ADR cites that exact segment."""
    from tooling.decide.adr import already_decided_families
    (tmp_path / "0001-exact.md").write_text(
        '```yaml\nid: ADR-0001\ntitle: x\nstatus: accepted\nfamilies: [F05.1]\n```\n# x\n',
        encoding="utf-8",
    )
    # Target is segment F05.1; ADR cites exact segment F05.1
    result = already_decided_families(str(tmp_path), ["F05.1"])
    assert result == {"F05.1"}
