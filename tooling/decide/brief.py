"""Loads and validates a downstream project's .design-suite/brief.yaml -- the
project-specific context (purpose, audience, brand, jurisdiction, hard
constraints) that tooling/decide's knowledge.py content alone can't supply."""
import yaml

REQUIRED_BRIEF_FIELDS = ["purpose", "audience", "brand", "jurisdiction", "constraints"]


class BriefError(Exception):
    pass


def load_brief(path):
    try:
        with open(path, encoding="utf-8") as f:
            raw = f.read()
    except OSError as e:
        raise BriefError(f"could not read brief at {path}: {e}")

    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        raise BriefError(f"{path} is not valid YAML: {e}")

    if not isinstance(data, dict):
        raise BriefError(f"{path} must parse to a mapping (got {type(data).__name__})")

    missing = [f for f in REQUIRED_BRIEF_FIELDS if f not in data]
    if missing:
        raise BriefError(f"{path} is missing required field(s): {', '.join(missing)}")

    constraints = data["constraints"]
    if isinstance(constraints, str):
        constraints = [constraints]
    elif not isinstance(constraints, list):
        raise BriefError(f"{path}: constraints must be a string or a list")
    data["constraints"] = constraints

    return data
