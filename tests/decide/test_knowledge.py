import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
from tooling.decide.knowledge import extract_constraint_ids, parse_composition


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
