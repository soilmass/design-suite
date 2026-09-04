import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
from tooling.decide.knowledge import parse_decision_rounds, TARGET_FAMILIES, build_family_knowledge
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


def test_parse_decision_rounds_round_1(suite_snapshot):
    rounds = parse_decision_rounds(suite_snapshot["decision"])
    round1 = next(r for r in rounds if r["id"] == "D003")
    assert round1["title"] == "Round 1 — Purpose"
    assert "F01" in round1["families"]
    assert "F02" in round1["families"]
    assert round1["bounded_by"] == []


def test_parse_decision_rounds_round_4_density_cluster(suite_snapshot):
    rounds = parse_decision_rounds(suite_snapshot["decision"])
    round4 = next(r for r in rounds if r["id"] == "D006")
    assert set(round4["families"]) == {"F15", "F16", "F33", "F30", "F18"}
    assert round4["bounded_by"] == ["C004", "C027", "C028"]


def test_parse_decision_rounds_round_10_conduct_range(suite_snapshot):
    rounds = parse_decision_rounds(suite_snapshot["decision"])
    round10 = next(r for r in rounds if r["id"] == "D012")
    assert set(round10["families"]) >= {"F63", "F64", "F65", "F66", "F67"}
    assert round10["bounded_by"] == ["C001", "C002", "C003", "C066", "C067", "C068", "C069", "C070"]


def test_target_families_constant():
    assert TARGET_FAMILIES == [
        "F01", "F02", "F05.1", "F11.1", "F15", "F17", "F22", "F31", "F32", "F40", "F64",
    ]


def test_build_family_knowledge_f15_unions_family_and_round_bounds(suite_snapshot):
    knowledge = build_family_knowledge(
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"]
    )
    f15 = knowledge["F15"]
    assert f15["round"]["id"] == "D006"
    # Composition's own F15 entry and Round 4's "Bounded by" state the same three ids --
    # this asserts the union doesn't duplicate them.
    assert set(f15["bounded_by"].keys()) == {"C004", "C027", "C028"}
    assert f15["bounded_by"]["C028"]["name"] == "Target size minimum"


def test_build_family_knowledge_f64_gets_round_level_bound_composition_lacks(suite_snapshot):
    # F64's Composition entry alone has no "Bounded by" line -- its only mechanical
    # bound comes from Round 10 (D012)'s "Bounded by C001-C003, C066-C070."
    knowledge = build_family_knowledge(
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"]
    )
    f64 = knowledge["F64"]
    assert f64["round"]["id"] == "D012"
    assert set(f64["bounded_by"].keys()) == {
        "C001", "C002", "C003", "C066", "C067", "C068", "C069", "C070",
    }


def test_build_family_knowledge_segment_id_f05_1(suite_snapshot):
    knowledge = build_family_knowledge(
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"]
    )
    f05_1 = knowledge["F05.1"]
    assert f05_1["round"]["id"] == "D005"
    assert set(f05_1["segments"]) == {"F05.1"}
    assert f05_1["segments"]["F05.1"].startswith("Pricing")


def test_build_family_knowledge_f01_no_bounds_at_all(suite_snapshot):
    knowledge = build_family_knowledge(
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"]
    )
    assert knowledge["F01"]["bounded_by"] == {}


def test_parse_decision_rounds_f31_resolves_to_d007_not_d003(suite_snapshot):
    """Regression: F31 is mentioned in a coupling aside in Round 1 (D003)
    but actually governed by Round 5 (D007). _find_round should return D007, not D003."""
    rounds = parse_decision_rounds(suite_snapshot["decision"])
    # First verify F31 appears in D007's families (its real round)
    d007 = next(r for r in rounds if r["id"] == "D007")
    assert "F31" in d007["families"]
    # Now verify _find_round returns D007, not D003
    from tooling.decide.knowledge import _find_round
    result = _find_round(rounds, "F31")
    assert result["id"] == "D007", f"F31 should resolve to D007 but got {result['id']}"


def test_build_family_knowledge_f31_includes_round_bounds_from_d007(suite_snapshot):
    """Regression: F31's bounded_by should include Round 5's constraints (C011, C021, C022, C023)
    not just Composition's bounds. This was failing because F31 was wrongly mapped to D003."""
    knowledge = build_family_knowledge(
        suite_snapshot["composition"], suite_snapshot["constraints"], suite_snapshot["decision"]
    )
    f31 = knowledge["F31"]
    # F31 should be in D007, not D003
    assert f31["round"]["id"] == "D007", f"F31 round should be D007 but is {f31['round']['id']}"
    # D007's bounded_by constraints should be included
    bounded_ids = set(f31["bounded_by"].keys())
    # Check that D007's specific constraints are present
    assert "C011" in bounded_ids, f"C011 missing from F31 bounds. Got: {bounded_ids}"
    assert "C021" in bounded_ids, f"C021 missing from F31 bounds. Got: {bounded_ids}"
    assert "C022" in bounded_ids, f"C022 missing from F31 bounds. Got: {bounded_ids}"
    assert "C023" in bounded_ids, f"C023 missing from F31 bounds. Got: {bounded_ids}"


def test_parse_decision_rounds_f22_resolves_to_d008_not_d003(suite_snapshot):
    """Regression: F22 is mentioned in a coupling aside in Round 1 (D003)
    but actually governed by Round 6 (D008). _find_round should return D008, not D003."""
    rounds = parse_decision_rounds(suite_snapshot["decision"])
    # First verify F22 appears in D008's families (its real round)
    d008 = next(r for r in rounds if r["id"] == "D008")
    assert "F22" in d008["families"]
    # Now verify _find_round returns D008, not D003
    from tooling.decide.knowledge import _find_round
    result = _find_round(rounds, "F22")
    assert result["id"] == "D008", f"F22 should resolve to D008 but got {result['id']}"
