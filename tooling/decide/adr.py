"""Renders and locates ADR files in the exact format tooling/decision_completeness.py
expects (see its own module docstring): a leading ```yaml front-matter fence as the
first bytes of the file, then a Markdown body with Context/Decision/Consequences."""
import glob
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from decision_completeness import load_adrs

ADR_ID_RE = re.compile(r"ADR-(\d+)")


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug


def render_adr(adr_id, title, families, context, decision, consequences, date):
    front_matter = {
        "id": adr_id,
        "title": title,
        "status": "accepted",
        "date": date,
        "families": families,
    }
    fm_yaml = yaml.safe_dump(front_matter, sort_keys=False, default_flow_style=False)
    return (
        f"```yaml\n{fm_yaml}```\n\n"
        f"# {adr_id} · {title}\n\n"
        f"## Context\n\n{context}\n\n"
        f"## Decision\n\n{decision}\n\n"
        f"## Consequences\n\n{consequences}\n"
    )


def next_adr_id(adr_dir):
    """Highest existing ADR-#### id in adr_dir (recursive .md scan) + 1, or
    ADR-0001 if none exist. Files that don't parse as a valid ADR (malformed
    front matter, or no id: field) are silently skipped, same as
    decision_completeness.py's own load_adrs() skips malformed files rather
    than crashing on them."""
    highest = 0
    for path in glob.glob(os.path.join(adr_dir, "**", "*.md"), recursive=True):
        text = open(path, encoding="utf-8").read()
        m = re.match(r"```yaml\n(.*?)\n```", text, re.S)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError:
            continue
        if not isinstance(fm, dict):
            continue
        id_m = ADR_ID_RE.match(str(fm.get("id", "")))
        if id_m:
            highest = max(highest, int(id_m.group(1)))
    return f"ADR-{highest + 1:04d}"


def already_decided_families(adr_dir, target_families):
    """Every id in target_families with at least one accepted-status ADR citing
    it in adr_dir. Shared by tooling/decide's context and apply subcommands --
    both need to know what's already decided before doing anything else.

    Implements asymmetric rollup matching:
    - For whole-family targets (no '.' in the id, e.g. F01): a citation matches
      if it's either that exact id OR any segment under it (e.g. F01.2 counts as
      deciding F01). This matches decision_completeness.py's own rollup behavior.
    - For segment targets (has '.' in the id, e.g. F05.1): a citation matches
      only if it's that exact segment id. A citation of just the parent family
      (e.g. F05) does NOT count, preventing false "already decided" signals for
      segments that deserve deliberate independent decision.
    """
    if not os.path.isdir(adr_dir):
        return set()
    adrs, _malformed = load_adrs(adr_dir)
    decided = set()
    for adr in adrs:
        if adr["status"] != "accepted":
            continue
        for cited in adr["families"]:
            cited = str(cited).strip().upper()
            # Check against each target_family for a match (asymmetric rollup)
            for target in target_families:
                target = str(target).strip().upper()
                if "." in target:
                    # Segment target: match only if exact
                    if cited == target:
                        decided.add(target)
                else:
                    # Whole-family target: match if exact OR any segment under it
                    if cited == target or cited.startswith(target + "."):
                        decided.add(target)
    return decided
