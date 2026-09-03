#!/usr/bin/env python3
"""Generator for tests/validate/fixtures/*.

Not part of the pytest run itself -- it materializes the static, synthetic
"fake suite" fixtures that test_validate.py points validate.py at. Re-run
this after editing the fixture bodies below; it overwrites the fixture
directories deterministically. It does not touch tooling/validate.py or
anything under docs/.
"""
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")

# ---------------------------------------------------------------------------
# Building blocks. Every fixture needs all nine documents because validate.py's
# DOCS dict hardcodes nine filenames and opens each unconditionally -- give it
# fewer and it crashes with FileNotFoundError before any check runs at all.
# ---------------------------------------------------------------------------

def fm(**kw):
    lines = ["```yaml"]
    for k, v in kw.items():
        if k == "depends":
            if not v:
                lines.append("depends: []")
            else:
                lines.append("depends:")
                for d in v:
                    lines.append(f"  - {d}")
        elif k == "owns":
            lines.append("owns:")
            for o in v:
                lines.append(f"  - {o}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("```")
    return "\n".join(lines) + "\n"

def doc(front_matter, heading, body):
    return front_matter + "\n" + f"# {heading}\n\n" + body + "\n"

# --- canonical, mutually-consistent "good" bodies for each of the 9 docs ---

def vocabulary_body(exports="V-001", extra_cite=""):
    return doc(
        fm(document="Vocabulary", version="1.0", tier=0,
           owns=["what this fixture term denotes"], exports=exports,
           depends=[], reviewed="2026-09-03"),
        "Vocabulary (fixture stub)",
        "**V-001 · Widget** — a placeholder term for fixture testing.\n"
        f"{extra_cite}\n"
    )

def constraints_body(exports="C001", extra_cite=""):
    return doc(
        fm(document="Constraints", version="1.0", tier=0,
           owns=["what may not be done, fixture stub"], exports=exports,
           depends=[], reviewed="2026-09-03"),
        "Constraints (fixture stub)",
        "**C001 · Widget floor**\n"
        "A placeholder constraint for fixture testing.\n"
        f"{extra_cite}\n"
    )

def anatomy_body(exports="A-001", depends=None, extra_cite=""):
    depends = depends if depends is not None else ["Vocabulary ^1"]
    return doc(
        fm(document="Anatomy", version="1.0", tier=1,
           owns=["what this fixture is made of"], exports=exports,
           depends=depends, reviewed="2026-09-03"),
        "Anatomy (fixture stub)",
        "## A-001 · The widget value\n\n"
        "A placeholder anatomy entry. See V-001.\n"
        f"{extra_cite}\n"
    )

def composition_body(exports="F01", depends=None, extra_cite=""):
    depends = depends if depends is not None else ["Vocabulary ^1", "Constraints ^1"]
    return doc(
        fm(document="Composition", version="1.0", tier=1,
           owns=["what choices exist, fixture stub"], exports=exports,
           depends=depends, reviewed="2026-09-03"),
        "Composition (fixture stub)",
        "### F01 · Widget mandate\n\n"
        "Bounded below by C001. See V-001.\n"
        f"{extra_cite}\n"
    )

def decision_body(exports="D001", depends=None, extra_cite=""):
    depends = depends if depends is not None else ["Composition ^1", "Anatomy ^1"]
    return doc(
        fm(document="Decision", version="1.0", tier=2,
           owns=["how to set a choice, fixture stub"], exports=exports,
           depends=depends, reviewed="2026-09-03"),
        "Decision (fixture stub)",
        "## D001 · Set the widget first\n\n"
        "Uses F01 and A-001.\n"
        f"{extra_cite}\n"
    )

def implementation_body(exports="T001", depends=None, extra_cite=""):
    depends = depends if depends is not None else ["Anatomy ^1", "Composition ^1"]
    return doc(
        fm(document="Implementation", version="1.0", tier=2,
           owns=["how a choice becomes code, fixture stub"], exports=exports,
           depends=depends, reviewed="2026-09-03"),
        "Implementation (fixture stub)",
        "## T001 · Widget token\n\n"
        "Realizes A-001 per F01.\n"
        f"{extra_cite}\n"
    )

def verification_body(exports="X001", depends=None, extra_cite=""):
    depends = depends if depends is not None else ["Decision ^1", "Implementation ^1"]
    return doc(
        fm(document="Verification", version="1.0", tier=3,
           owns=["how to confirm it, fixture stub"], exports=exports,
           depends=depends, reviewed="2026-09-03"),
        "Verification (fixture stub)",
        "## X001 · Widget check\n\n"
        "Confirms D001 was realized as T001.\n"
        f"{extra_cite}\n"
    )

def diagnosis_body(exports="R001", depends=None, extra_cite=""):
    depends = depends if depends is not None else ["Composition ^1", "Decision ^1"]
    return doc(
        fm(document="Diagnosis", version="1.0", tier=3,
           owns=["how to read a site back, fixture stub"], exports=exports,
           depends=depends, reviewed="2026-09-03"),
        "Diagnosis (fixture stub)",
        "## R001 · Read the widget back\n\n"
        "Cross-check against F01 and D001.\n"
        f"{extra_cite}\n"
    )

def governance_body(exports="G001", cites_no_ids=True, extra_cite=""):
    return doc(
        fm(document="Governance", version="1.0", tier="none",
           owns=["how decisions change, fixture stub"], exports=exports,
           depends=[], cites_no_ids=str(cites_no_ids).lower(), reviewed="2026-09-03"),
        "Governance (fixture stub)",
        "## G001 · Change is proposed as a diff\n\n"
        "A placeholder governance rule. Cites nothing by design.\n"
        f"{extra_cite}\n"
    )

FILENAMES = {
    "vocabulary": "vocabulary-1.0.0.md",
    "anatomy": "anatomy-1.0.0.md",
    "composition": "composition-1.0.0.md",
    "constraints": "constraints-1.0.0.md",
    "decision": "decision-1.0.0.md",
    "implementation": "implementation-1.0.0.md",
    "verification": "verification-1.0.0.md",
    "diagnosis": "diagnosis-1.0.0.md",
    "governance": "governance-1.0.0.md",
}

def base_suite():
    """The known-good minimal suite: every check should pass on this."""
    return {
        "vocabulary": vocabulary_body(),
        "constraints": constraints_body(),
        "anatomy": anatomy_body(),
        "composition": composition_body(),
        "decision": decision_body(),
        "implementation": implementation_body(),
        "verification": verification_body(),
        "diagnosis": diagnosis_body(),
        "governance": governance_body(),
    }

def write_case(name, docs):
    d = os.path.join(ROOT, name, "docs")
    os.makedirs(d, exist_ok=True)
    for key, text in docs.items():
        with open(os.path.join(d, FILENAMES[key]), "w", encoding="utf-8") as f:
            f.write(text)
    print(f"wrote {name}: {sorted(docs)}")

# ---------------------------------------------------------------------------
# Case 1: happy path -- everything should validate clean.
# ---------------------------------------------------------------------------
write_case("happy_path", base_suite())

# ---------------------------------------------------------------------------
# Case 2 [check 1, front matter/exports]: composition declares a wider export
# range (F01-F05) than what the document body actually defines (only F01).
# ---------------------------------------------------------------------------
s = base_suite()
s["composition"] = composition_body(exports="F01-F05")
write_case("exports_mismatch", s)

# ---------------------------------------------------------------------------
# Case 3 [check 2, dependency direction] -- broken: Vocabulary (tier 0) is
# made to depend on Anatomy (tier 1), an upward citation. Illegal.
# Case 3b: the corrected version of the *same* fixture (Vocabulary depends on
# nothing again) -- this is the red/green pair.
# ---------------------------------------------------------------------------
s = base_suite()
s["vocabulary"] = vocabulary_body()
# monkey-patch: re-render vocabulary with an illegal upward dependency
s["vocabulary"] = doc(
    fm(document="Vocabulary", version="1.0", tier=0,
       owns=["what this fixture term denotes"], exports="V-001",
       depends=["Anatomy ^1"], reviewed="2026-09-03"),
    "Vocabulary (fixture stub)",
    "**V-001 · Widget** — a placeholder term for fixture testing.\n"
)
write_case("dependency_direction_violation", s)

s_fixed = base_suite()  # vocabulary depends: [] again, everything else identical
write_case("dependency_direction_violation_fixed", s_fixed)

# ---------------------------------------------------------------------------
# Case 4 [check 3, cross-reference resolution] -- vocabulary cites C999,
# which is never defined anywhere in the suite (constraints only defines
# C001). Dangling reference.
# ---------------------------------------------------------------------------
s = base_suite()
s["vocabulary"] = vocabulary_body(extra_cite="\nSee also C999 for the related floor.\n")
write_case("dangling_reference", s)

# ---------------------------------------------------------------------------
# Case 5 [check 4b, orthogonality] -- governance declares cites_no_ids: true
# but its body actually names C001. Violation.
# ---------------------------------------------------------------------------
s = base_suite()
s["governance"] = governance_body(extra_cite="\nThis illegally names C001 directly.\n")
write_case("orthogonality_violation", s)

# ---------------------------------------------------------------------------
# Adversarial cases -- syntactically valid YAML, semantically malformed in
# ways the happy-path/error fixtures above never exercise. Each of these was
# run against the real validate.py by hand before being added here; several
# of them crashed it (see tooling/validate.py's front_matter()/registry/[2]/
# [4b] fixes) rather than reporting a clean PROBLEM. Now fixed, they're
# regression fixtures pinning the fix down.
# ---------------------------------------------------------------------------

# Case 6 -- front matter is syntactically valid YAML but missing the required
# `version:` key entirely. Used to crash validate.py with an unhandled
# KeyError in the [1] print statement (`fm['version']`).
s = base_suite()
s["vocabulary"] = doc(
    fm(document="Vocabulary", tier=0,
       owns=["what this fixture term denotes"], exports="V-001",
       depends=[], reviewed="2026-09-03"),
    "Vocabulary (fixture stub)",
    "**V-001 · Widget** — a placeholder term for fixture testing.\n"
)
write_case("missing_version_key", s)

# Case 7 -- same crash class as Case 6, but for the required `tier:` key
# (`fm['tier']` in the same print statement).
s = base_suite()
s["vocabulary"] = doc(
    fm(document="Vocabulary", version="1.0",
       owns=["what this fixture term denotes"], exports="V-001",
       depends=[], reviewed="2026-09-03"),
    "Vocabulary (fixture stub)",
    "**V-001 · Widget** — a placeholder term for fixture testing.\n"
)
write_case("missing_tier_key", s)

# Case 8 -- the fenced ```yaml block parses to a YAML *list*, not a mapping
# (valid YAML, wrong shape). Used to crash with AttributeError on the first
# `fm.get(...)` call.
s = base_suite()
s["vocabulary"] = (
    "```yaml\n- just\n- a\n- list\n```\n\n"
    "# Vocabulary (fixture stub)\n\n"
    "**V-001 · Widget** — a placeholder term for fixture testing.\n"
)
write_case("front_matter_not_a_dict", s)

# Case 9 -- the fenced ```yaml block is not even parseable YAML (an
# unterminated quoted scalar). Used to crash with an uncaught
# yaml.scanner.ScannerError before any check ran.
s = base_suite()
s["vocabulary"] = (
    "```yaml\n"
    'document: "Vocabulary\n'
    "version: 1.0\n"
    "tier: 0\n"
    "exports: V-001\n"
    "depends: []\n"
    "```\n\n"
    "# Vocabulary (fixture stub)\n\n"
    "**V-001 · Widget** — a placeholder term for fixture testing.\n"
)
write_case("front_matter_invalid_yaml", s)

# Case 10 -- a document with no fenced ```yaml block at all (front_matter()
# already returned None for this pre-fix; the crash was downstream, in
# check [2]'s `d['fm'].get('depends')`, since nothing there guarded against
# a doc whose fm is None).
s = base_suite()
s["vocabulary"] = (
    "# Vocabulary (fixture stub)\n\n"
    "**V-001 · Widget** — a placeholder term for fixture testing.\n"
)
write_case("no_front_matter_block_at_all", s)

# Case 11 -- governance (tier None) declares a `depends:` entry. Illegal by
# the tier rule, but used to crash check [2] with TypeError comparing
# `dt < mt` when mt (governance's own tier) is None, instead of reporting
# ILLEGAL like every other bad dependency.
s = base_suite()
s["governance"] = doc(
    fm(document="Governance", version="1.0", tier="none",
       owns=["how decisions change, fixture stub"], exports="G001",
       depends=["Constraints ^1"], cites_no_ids="true", reviewed="2026-09-03"),
    "Governance (fixture stub)",
    "## G001 · Change is proposed as a diff\n\n"
    "A placeholder governance rule. Cites nothing by design.\n"
)
write_case("governance_with_illegal_depends", s)

# Case 12 -- a document declares a non-empty `exports:` range but its body
# defines zero matching IDs. The [1] MISMATCH check only ever looped over
# namespaces found in the body (`byns`); a namespace that is declared but
# never defined at all was never visited, so this silently printed "ok".
s = base_suite()
s["verification"] = doc(
    fm(document="Verification", version="1.0", tier=3,
       owns=["how to confirm it, fixture stub"], exports="X001",
       depends=["Decision ^1", "Implementation ^1"], reviewed="2026-09-03"),
    "Verification (fixture stub)",
    "No checks defined in the body at all.\n"
)
write_case("exports_declared_but_zero_ids", s)

# ---------------------------------------------------------------------------
# Cases below exercise checks that already worked correctly but had no
# fixture pinning them down -- verifying existing-and-correct behavior, not
# fixing a bug.
# ---------------------------------------------------------------------------

# Case 13 -- the DUPLICATE ID check (line 63 of validate.py) was never
# exercised by any existing fixture. Composition defines F01 twice.
s = base_suite()
s["composition"] = composition_body() + "\n### F01 · Widget mandate\n\nDuplicate entry defining F01 again.\n"
write_case("duplicate_id", s)

# Case 14 -- `depends:` names a document that isn't in DOCS at all (a typo
# or a genuinely nonexistent document, as opposed to a real one from another
# tier). Confirms this is still cleanly flagged ILLEGAL + [TARGET NOT BUILT],
# not silently ignored.
s = base_suite()
s["anatomy"] = doc(
    fm(document="Anatomy", version="1.0", tier=1,
       owns=["what this fixture is made of"], exports="A-001",
       depends=["Vocabulary ^1", "Nonexistent ^1"], reviewed="2026-09-03"),
    "Anatomy (fixture stub)",
    "## A-001 · The widget value\n\nA placeholder anatomy entry. See V-001.\n"
)
write_case("depends_on_nonexistent_doc", s)

# Case 15 -- `tier:` is present but is a string, not the expected int (or
# 'none' for governance). Confirms the `declared_tier != TIER[name]` check
# catches a type mismatch, not just a value mismatch.
s = base_suite()
s["vocabulary"] = doc(
    fm(document="Vocabulary", version="1.0", tier='"zero"',
       owns=["what this fixture term denotes"], exports="V-001",
       depends=[], reviewed="2026-09-03"),
    "Vocabulary (fixture stub)",
    "**V-001 · Widget** — a placeholder term for fixture testing.\n"
)
write_case("tier_wrong_type", s)

# Case 16 -- the mirror image of Case 12: `exports:` is present but empty
# (parses to None) while the body *does* define V-001. Confirms this
# direction of the mismatch was already caught (the MISMATCH check's `for
# ns in byns` loop does run here, since V-001 is in byns).
s = base_suite()
s["vocabulary"] = doc(
    fm(document="Vocabulary", version="1.0", tier=0,
       owns=["what this fixture term denotes"], exports="",
       depends=[], reviewed="2026-09-03"),
    "Vocabulary (fixture stub)",
    "**V-001 · Widget** — a placeholder term for fixture testing.\n"
)
write_case("empty_exports_declared", s)

# Case 17 -- an ID heading with an extra space before the ` · ` separator
# (e.g. pasted from a source that normalizes whitespace differently). The
# defined() regexes require the exact separator, so this ID is silently
# *not* recognized as defined -- everything that legitimately cites it
# reports a false "dangling" reference instead. Documented here as known,
# strict-by-design behavior (the fix would be to loosen definition regexes,
# which trades a hard-to-see false negative for an easy-to-see false
# positive -- not changed, since the suite's whole contract is exact
# formatting; see suite-architecture.md).
s = base_suite()
s["composition"] = doc(
    fm(document="Composition", version="1.0", tier=1,
       owns=["what choices exist, fixture stub"], exports="F01",
       depends=["Vocabulary ^1", "Constraints ^1"], reviewed="2026-09-03"),
    "Composition (fixture stub)",
    "### F01  · Widget mandate\n\nBounded below by C001. See V-001.\n"
)
write_case("composition_heading_double_space_before_middot", s)

print("done")
