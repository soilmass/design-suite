"""Assembles the context document tooling/decide's `context` subcommand emits:
every undecided target family's knowledge, the project's brief, and which target
families are already decided (so an agent doesn't re-derive what's already settled)."""
import os

from .adr import already_decided_families
from .brief import load_brief, BriefError
from .knowledge import build_family_knowledge, TARGET_FAMILIES


def run_context(target_repo, suite_composition_path, suite_constraints_path, suite_decision_path):
    knowledge = build_family_knowledge(
        suite_composition_path, suite_constraints_path, suite_decision_path
    )

    adr_dir = os.path.join(target_repo, "adr")
    decided = already_decided_families(adr_dir, TARGET_FAMILIES)

    brief_path = os.path.join(target_repo, ".design-suite", "brief.yaml")
    if os.path.isfile(brief_path):
        try:
            brief = load_brief(brief_path)
        except BriefError as e:
            brief = {"_error": str(e)}
    else:
        brief = {}

    families = {fid: knowledge[fid] for fid in TARGET_FAMILIES if fid not in decided}

    return {
        "families": families,
        "already_decided": sorted(decided),
        "brief": brief,
    }
