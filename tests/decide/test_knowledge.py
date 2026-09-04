import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
from tooling.decide.knowledge import extract_constraint_ids, parse_composition, parse_constraints


def test_extract_constraint_ids_plain_list():
    assert extract_constraint_ids("Bounded by C004, C027, C028.") == ["C004", "C027", "C028"]


def test_extract_constraint_ids_with_trailing_words():
    text = "Bounded by C004 measure, C027 spacing override tolerance, C028 target size."
    assert extract_constraint_ids(text) == ["C004", "C027", "C028"]


def test_extract_constraint_ids_range():
    assert extract_constraint_ids("Bounded by C001–C003, C066–C070.") == [
        "C001", "C002", "C003", "C066", "C067", "C068", "C069", "C070",
    ]


def test_extract_constraint_ids_hyphen_range():
    assert extract_constraint_ids("Bounded by C001-C003.") == ["C001", "C002", "C003"]


def test_extract_constraint_ids_none_found():
    assert extract_constraint_ids("Free of tight coupling once F26 and F30 are set.") == []


def test_parse_composition_f15(suite_snapshot):
    families = parse_composition(suite_snapshot["composition"])
    f15 = families["F15"]
    assert f15["name"] == "Density"
    assert f15["segments"]["F15.1"].startswith("Information density")
    assert f15["segments"]["F15.2"].startswith("Content-to-chrome ratio")
    assert f15["bounded_by"] == ["C004", "C027", "C028"]
    assert "F16" in f15["coupling"]


def test_parse_composition_f01_no_bound(suite_snapshot):
    families = parse_composition(suite_snapshot["composition"])
    f01 = families["F01"]
    assert f01["name"] == "Mandate"
    assert f01["bounded_by"] == []
    assert f01["coupling"] is None
    assert set(f01["segments"]) == {"F01.1", "F01.2", "F01.3", "F01.4"}


def test_parse_composition_f05_segment_f05_1(suite_snapshot):
    families = parse_composition(suite_snapshot["composition"])
    f05 = families["F05"]
    assert "F05.1" in f05["segments"]
    assert f05["segments"]["F05.1"].startswith("Pricing")


def test_parse_constraints_c046(suite_snapshot):
    constraints = parse_constraints(suite_snapshot["constraints"])
    c046 = constraints["C046"]
    assert c046["name"] == "Name, role, value"
    assert "programmatically determinable" in c046["text"]


def test_parse_constraints_c028_target_size(suite_snapshot):
    constraints = parse_constraints(suite_snapshot["constraints"])
    c028 = constraints["C028"]
    assert c028["name"] == "Target size minimum"
    assert "24" in c028["text"]


def test_parse_constraints_c046_no_section_bleed(suite_snapshot):
    """Regression: C046's text should NOT bleed into the next section heading."""
    constraints = parse_constraints(suite_snapshot["constraints"])
    c046 = constraints["C046"]
    assert "programmatically determinable" in c046["text"]
    # Should not include content from the next section (# PART C)
    assert "PART C" not in c046["text"]
    assert "# PART" not in c046["text"]
    # Should contain the key constraint description but not section content
    assert "custom controls expensive" in c046["text"]
    # Should not include any other constraint's name (C060 comes after the section)
    assert "European Accessibility Act" not in c046["text"]


def test_parse_constraints_c124_no_export_bleed(suite_snapshot):
    """Regression: C124 (last constraint) should NOT include export index/review sections."""
    constraints = parse_constraints(suite_snapshot["constraints"])
    c124 = constraints["C124"]
    assert "Third-party budget" in c124["name"]
    # Should not include the export index or anything after
    assert "EXPORT INDEX" not in c124["text"]
    assert "Review schedule" not in c124["text"]
    # C124's body should be reasonably short (just the constraint desc, not 5.6KB)
    assert len(c124["text"]) < 2000, f"C124 text is too long ({len(c124['text'])} chars)"
