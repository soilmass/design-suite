import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
from tooling.decide.brief import load_brief, BriefError

FIXTURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures", "briefs")


def test_load_brief_valid():
    brief = load_brief(os.path.join(FIXTURES, "valid.yaml"))
    assert "SaaS product" in brief["purpose"]
    assert brief["brand"] == ["direct", "technical", "unglossy"]
    assert isinstance(brief["constraints"], list)
    assert len(brief["constraints"]) == 2


def test_load_brief_missing_required_field():
    try:
        load_brief(os.path.join(FIXTURES, "missing_purpose.yaml"))
        assert False, "expected BriefError"
    except BriefError as e:
        assert "purpose" in str(e)


def test_load_brief_not_a_mapping():
    try:
        load_brief(os.path.join(FIXTURES, "not_a_dict.yaml"))
        assert False, "expected BriefError"
    except BriefError as e:
        assert "mapping" in str(e).lower()


def test_load_brief_missing_file():
    try:
        load_brief(os.path.join(FIXTURES, "does_not_exist.yaml"))
        assert False, "expected BriefError"
    except BriefError as e:
        assert "does_not_exist.yaml" in str(e)


def test_load_brief_normalizes_single_string_constraint():
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as f:
        f.write("purpose: x\naudience: y\nbrand: [z]\njurisdiction: US\nconstraints: one hard constraint\n")
        path = f.name
    try:
        brief = load_brief(path)
        assert brief["constraints"] == ["one hard constraint"]
    finally:
        os.unlink(path)
