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

print("done")
