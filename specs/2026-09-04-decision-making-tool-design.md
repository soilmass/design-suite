# Design: `tooling/decide.py` — a decision-making tool for AI agents

**Date:** 2026-09-04
**Status:** Approved, not yet built

## Why this exists

The suite's own audit (`audit/tooling-audit-2.0.0.md`) reaches an honest conclusion: the suite's
contribution is assembly and completeness, not new mechanism. Every document in it explains its
own piece well. What none of them do — and what `tooling/decision_completeness.py` only checks
for after the fact — is help anyone actually *make* the 67 Composition decisions for a real
project. An agent using this suite today has to read Composition's range, read whichever
Constraints bound it, read Decision's guidance for when to set it, and synthesize a specific value
by hand, once per family, informed by nothing the suite can hand it directly.

This is the gap Phase 4 closes: a tool that does that synthesis, for a real project, and produces
the artifact `decision_completeness.py` already knows how to grade.

## Primary user

An AI coding agent building a real site — not a human reading documentation, not this suite's own
contributors. The suite has spent its whole history so far serving the second audience; this is
the first capability built for the first.

## Scope for v1

`D204` (Decision) already names a fast path: 11 of the 67 Composition families cover every
coherence question `D111` raises and produce a genuinely coherent site on their own —
`F01, F02, F05.1, F11.1, F15, F17, F22, F31, F32, F40, F64`. Building for exactly these 11, using
the suite's own stated shortcut rather than inventing a new one. Nothing about the architecture is
specific to eleven; extending to all 67 is a config change once this is proven, not a redesign.

Out of scope for v1, explicitly:
- The other 56 Composition families.
- Anything past Decision — generating actual tokens/components (Implementation), or checking
  built output (Verification). This tool's job ends at a written, self-consistent decision record.
- A GUI or web interface. This is a CLI tool, matching every other `tooling/*.py` script in this
  repo.

## Where it lives

`tooling/decide.py`, sibling to `tooling/decision_completeness.py`. Same precedent: built for a
downstream team using this suite, not for this repo's own governed documents. Reuses
`decision_completeness.py`'s existing logic for "what's already decided" rather than
reimplementing it — `decide.py` should import from it, not duplicate its ADR-scanning code.

## Inputs

**1. A project brief** — `.design-suite/brief.yaml` in the target repo. Captures what no codebase
could tell you: site type/purpose, audience, brand words, jurisdiction, hard external constraints
(e.g. "must use existing brand palette X"). Exact schema is an implementation-plan decision, not
fixed here, but it needs at minimum: `purpose`, `audience`, `brand` (free-text words/adjectives),
`jurisdiction`, `constraints` (free-text list of anything externally imposed that isn't already
one of this suite's own `C###` Constraints).

**2. The target repo itself** — read for what's inferable: existing stack (`package.json` or
equivalent), any existing palette/typography values, any existing component patterns. Informs
decisions but never overrides the brief where the two conflict — the brief is the authoritative
statement of intent; the repo is evidence of what's already been built toward it.

**3. This suite** — read the same way any contributor reads it: Composition's ranges (including
each family's `Bounded by` citation where one exists — confirmed present for `F15`, `F31`, `F32`
in the v1 set; absent for `F01`, `F02`, `F11.1`, `F17`, `F22`, `F40`, `F64`, which have no
mechanical constraint and rely on judgment alone), the cited Constraints' actual bounds, and
Decision's round guidance for each family (which round sets it, what it's coupled to).

**4. The target repo's existing ADR directory** — via `decision_completeness.py`'s own scan, so
`decide.py` only surfaces the real remainder, not families already decided.

## Process, per undecided family

1. Look up the family's range from Composition, its bounding Constraints (if any), and which
   Decision round sets it.
2. Synthesize a specific value from the family's range, informed by the brief and repo context.
3. **Hard block on an incomplete citation, not on a value-level Constraint violation.** Where a
   family has one or more `Bounded by` Constraint IDs, the tool refuses to write a decision whose
   `rationale` doesn't name every one of them — a citation-completeness check, not a compliance
   check. It does **not** verify that the chosen `value` actually satisfies any of those
   Constraints numerically or semantically (a numeric range, a WCAG ratio, an enumerated set):
   `value` is free text an agent writes, and there is nothing mechanical to check free text
   against. A value that cites every bounding Constraint ID while genuinely violating one of them
   passes this guardrail — the citation discipline is the only thing enforced here, same as it is
   between this suite's own nine documents. Where a family has no bounding Constraint at all, this
   step is a no-op — the agent's own rationale is the only check that exists, same as it is for a
   human deciding today.
4. Write a real ADR into the target repo's ADR directory, in the exact format
   `tests/decision_completeness/fixtures/` already validates: YAML front matter
   (`id`/`title`/`status`/`date`/`families`), Markdown body (Context/Decision/Consequences). One
   ADR per family or a sensibly grouped set (e.g. one ADR for `F31`+`F32` if the rationale is
   genuinely shared) — exact grouping is an implementation-plan decision.
5. Every ADR's Context or Decision section names which Constraint(s) bounded the choice (by ID)
   and which Decision round guidance shaped it — the same citation discipline this suite's own
   nine documents already hold each other to, applied to output this tool produces for someone
   else's project.

## Output: the session summary

Because the chosen mode is full autonomy with after-the-fact review (not a per-decision human
gate), the tool's other required output is a single human-readable summary: which families got
decided, the value chosen for each, and a **confidence/stakes flag** per decision — so a human
reviewing the batch knows where to look first rather than re-reading eleven roughly-equal
paragraphs. A decision is flagged when: the brief didn't clearly determine it (the tool had to
infer or default), it touches a family with no mechanical Constraint check, or it's tightly
coupled to a family that itself got flagged (per Composition's own `Coupling` notes — e.g. `F22`
is tightly coupled to `F02`; a low-confidence `F02` should propagate suspicion to `F22`).

After all 11 are written, the tool runs `decision_completeness.py` against its own output as a
self-check and includes that result in the summary — the tool should never claim done while its
own output would fail the completeness checker that already exists for exactly this purpose.

## Error handling

- Brief missing or malformed: refuse to run, name exactly what's missing (mirrors
  `decision_completeness.py`'s existing "malformed ADR, skipped, with a reason" pattern rather
  than crashing).
- A family already decided (present in the existing ADR directory): skip it, note the skip in the
  summary, never overwrite an existing human or prior-run decision silently.
- A family whose only Constraint-satisfying values are excluded by something in the brief (e.g. a
  brief constraint conflicts with a `Bounded by` Constraint): refuse to write a decision for that
  family, surface the conflict explicitly in the summary rather than picking a value quietly.

## Testing

Same discipline as `decision_completeness.py`: a `tests/decide/` fixture suite under pytest,
covering at minimum:
- A clean run producing all 11, passing `decision_completeness.py` afterward.
- A malformed brief (missing required field, bad YAML).
- A family already decided in the target ADR directory (must be skipped, not re-decided).
- A decision for a bounded family whose `rationale` doesn't cite every one of its `Bounded by`
  Constraint IDs (must refuse, not write it) — a citation-completeness check; the tool does not
  attempt to check whether `value` itself satisfies those Constraints (see step 3 above).
- A brief-vs-Constraint conflict (must refuse and surface it, not guess).
- The coupling-based confidence propagation (a flagged `F02` produces a flagged `F22`).

## Open questions for the implementation plan

- Exact `brief.yaml` schema (fields beyond the minimum four named above).
- One ADR per family vs. grouped ADRs for tightly-coupled families.
- Exact confidence-flag vocabulary and where it lives (front matter field vs. summary-only).
- Whether `decide.py` needs its own CLI flags beyond "target repo path" (e.g. `--dry-run`,
  `--family F31` to redo a single one).

## What happens to `ROADMAP.md`

Replaced. The three-phase structure (contributor infrastructure → content coverage →
adoption/visibility) is done and stays recorded in `CHANGELOG.md`, not restated. The new roadmap's
single goal is this tool, staged as real milestones: brief schema → single-family decision logic
→ all 11 families → self-verification loop → a second worked example, this one *produced by* the
tool against a real (even if small/synthetic) target project, not just narrated by a human the way
`examples/end-to-end-walkthrough.md` is.
