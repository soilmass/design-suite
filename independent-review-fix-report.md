# Independent Peer Review Fix Report — PR #72 (`tooling/decide/`)

Fixes for findings D1–D5 from the independent peer review comment on PR #72
("## Independent peer review — PR #72"), executed against branch head `7a99c64`
in this worktree.

## D1 — Coupling propagation order-dependence (fixed, with tests)

**Root cause:** `tooling/decide/apply_cmd.py`'s coupling-propagation pass did a
single forward loop over `accepted_decisions`, mutating `low_confidence_families`
while iterating it. A one-hop propagation (A directly coupled to an
already-flagged B) always worked, because B was seeded into
`low_confidence_families` before the pass started (from its own stated
`confidence: low`). A two-hop transitive chain (A coupled to B, B coupled to C,
only C starts low) only worked if B happened to be visited before A in that
single pass — otherwise A's check ran before B had been flagged, and A was
missed.

**Fix:** replaced the single pass with a `while` loop that repeats the pass
until a full pass adds nothing new to `low_confidence_families` (a fixpoint).
Also switched the final write loop to look up each family's resolved
confidence from a `confidence_by_family` dict built/updated during the
fixpoint loop, rather than trusting the tuple's original (possibly stale)
`confidence` value. Bounded by at most 11 target families, so the extra passes
have no meaningful performance cost.

**Reproduction of the maintainer's exact failure mode:** used real `*Coupling*`
prose from `docs/composition-1.0.0.md` among three of the 11 target families:
- F31's own Coupling line: "tight with F17. Moderate with F15." (F31 → F17, F15)
- F17's own Coupling line: "tight with F31, F32." (F17 → F31, F32)
- F15's own Coupling line mentions neither F17 nor F31.

Only F15 marked `confidence: low`. Correct behavior: F31 flags (direct coupling
to F15), then F17 flags (direct coupling to F31, which only became
low-confidence during the same pass) — a genuine two-hop transitive chain.

Two new fixtures with identical decisions, different list order:
- `tests/decide/fixtures/decisions/coupling_propagation_transitive_order_a.yaml` (F17, F31, F15)
- `tests/decide/fixtures/decisions/coupling_propagation_transitive_order_b.yaml` (F31, F17, F15)

New test:
`tests/decide/test_apply_cmd.py::test_run_apply_coupling_propagation_transitive_two_hop_order_independent`

**RED (before the fix):**
```
E       AssertionError: order a: expected ['F15', 'F17', 'F31'], got ['F15', 'F31']
```
(F17 was missed under order a — the exact order-dependent failure the maintainer
reproduced.)

**GREEN (after the fix):** both orders now produce `['F15', 'F17', 'F31']`, and
F17's written entry shows `confidence: low` in both.

**Docstring correction:** the existing
`test_run_apply_coupling_propagation_order_independent` claimed to prove
propagation is "order-independent," but only exercised the one-hop F02↔F22
case (a direct, mutual coupling — order genuinely doesn't matter there even
with the old single-pass code, since both ends are seeded before the pass
runs). Its docstring now says explicitly that it's a one-hop case and points to
the new transitive test for the genuine order-independence proof.

## D2 — Raw `KeyError` on a missing segment in a vendored `--composition` file (fixed, with test)

**Root cause:** `tooling/decide/knowledge.py`'s `build_family_knowledge` already
guarded the family-level lookup (`if parent not in composition: raise
KnowledgeError(...)`), but the segment-level lookup a few lines later
(`comp["segments"][fid]`, for a segment target id like `F05.1`) had no
equivalent guard, so a vendored `--composition` file with the parent family
present but that specific segment missing (e.g. renamed/removed) crashed with
a bare `KeyError`.

**Fix:** added `if fid not in comp["segments"]: raise KnowledgeError(...)`
immediately before the lookup, in the same wording style as the existing
family-level `KnowledgeError`.

**New test:** `test_build_family_knowledge_missing_segment_raises_clear_error`
in `tests/decide/test_knowledge.py`, corrupting a snapshot of the real
`docs/composition-1.0.0.md` by renaming `**F05.1**` to `**F05.9**` (same
corruption technique as the existing family-level test, which renames F01's
header).

**RED (before the fix):**
```
File ".../tooling/decide/knowledge.py", line 198, in build_family_knowledge
    segments = {fid: comp["segments"][fid]}
KeyError: 'F05.1'
```

**GREEN (after the fix):** `KnowledgeError` raised, message contains `F05.1`
and the corrupt file's path.

## D3 — "One edit away from all 67" claim corrected (documentation only)

`specs/2026-09-04-decide-tool-plan.md`'s Global Constraints section previously
claimed `TARGET_FAMILIES` is "a single list constant one edit away from
becoming all 67." Corrected to state plainly that this is not currently true:
`knowledge.py`'s round-family extraction over-captures family mentions from
explanatory prose in a Decision round's block (beyond the coupling-arrow
mentions that are already stripped), which would silently misassign at least
`F47`, `F65`, and `F66` to the wrong round if `TARGET_FAMILIES` were extended
today — and for `F65`/`F66` specifically, to a round with no `Bounded by` line
at all, incorrectly weakening guardrail 2 for them. Per the finding's
instructions, no code change was attempted — a general prose-vs-declaration
distinguisher was already considered and rejected as intractable during the
original design.

## D4 — `self_check_output` empty while `self_check_passed` claims failure (fixed, with test)

**Root cause:** `run_apply`'s line
`exit_code = decision_completeness.main([adr_dir]) if os.path.isdir(adr_dir) else 1`
meant that when every decision in a batch is rejected (and no pre-existing
`adr/` exists), `adr_dir` is never created, the `else 1` branch fires,
`decision_completeness.main` is never called, and `self_check_output` stays
`""` while `self_check_passed` reports `False` — contradicting the README's own
claim that `false` means the checker "found something actually wrong," never
that it didn't run.

**Fix:** removed the conditional; `decision_completeness.main([adr_dir])` is
now called unconditionally. Its own `main()` already handles a nonexistent
directory gracefully (prints `f"\nERROR: {adr_dir} is not a directory"`,
returns 1), so `self_check_output` now carries real, honest content.

**New test:** `test_run_apply_all_rejected_self_check_output_not_empty` in
`tests/decide/test_apply_cmd.py`, using the existing
`missing_bound_citation.yaml` fixture (one decision, rejected, so nothing is
written and no `adr/` dir is created).

**RED (before the fix):**
```
E       AssertionError: self_check_output must not be empty -- decision_completeness.main() should have run
E       assert '' != ''
```

**GREEN (after the fix):** `self_check_output` is non-empty and contains "not a
directory" (case-insensitive match on `decision_completeness.py`'s own ERROR
line).

## D5 — Design doc step 3 corrected to match the actual guardrail (documentation only)

`specs/2026-09-04-decision-making-tool-design.md`'s "Process, per undecided
family" step 3 previously described "a hard block on any
mechanically-checkable Constraint violation" — implying the tool checks
whether the chosen `value` numerically/semantically satisfies a bounding
Constraint. What's actually implemented (and correctly documented in the
plan's Global Constraints) is narrower: a citation-completeness check only —
the `rationale` must name every bounding Constraint ID; `value` is free text
and nothing mechanical checks it. Step 3 was rewritten to state this
accurately, reusing the plan's own reasoning ("free text has nothing
mechanical to check it against"). The Testing section's item describing "a
synthesized value that would violate a mechanically-checkable Constraint (must
refuse...)" — a test for a check that was never actually built this way — was
corrected to describe the citation-completeness test instead, with a pointer
back to step 3.

## Full `tests/decide/` suite result

```
66 passed in 12.78s
```
(63 pre-existing + 3 new: the D1 transitive test, the D2 missing-segment test,
the D4 all-rejected self-check test.)

## Full `tests/` suite result

```
96 passed in 21.88s
```
(93 pre-existing + 3 new, as above. `tests/decision_completeness/` and
`tests/validate/` untouched and still fully green.)

## `validate.py` result

```
cd tooling && python3 validate.py
...
[5] Roster
  constraints     tier 0    BUILT
  vocabulary      tier 0    BUILT
  anatomy         tier 1    BUILT
  composition     tier 1    BUILT
  decision        tier 2    BUILT
  implementation  tier 2    BUILT
  diagnosis       tier 3    BUILT
  verification    tier 3    BUILT
  governance      tier None BUILT
  -> 9 built, 0 remaining:

================================================================
PASS — no problems
================================================================
```
No diff to `tooling/registry.yaml`. Confirmed no-op, as expected — neither
`specs/2026-09-04-decide-tool-plan.md` nor
`specs/2026-09-04-decision-making-tool-design.md` lives under `docs/`.

## Files changed

- `tooling/decide/apply_cmd.py` — D1 (fixpoint propagation loop), D4 (unconditional self-check call)
- `tooling/decide/knowledge.py` — D2 (segment-level `KnowledgeError` guard)
- `tests/decide/test_apply_cmd.py` — D1 test + docstring correction, D4 test
- `tests/decide/test_knowledge.py` — D2 test
- `tests/decide/fixtures/decisions/coupling_propagation_transitive_order_a.yaml` — new, D1
- `tests/decide/fixtures/decisions/coupling_propagation_transitive_order_b.yaml` — new, D1
- `specs/2026-09-04-decide-tool-plan.md` — D3 (claim correction)
- `specs/2026-09-04-decision-making-tool-design.md` — D5 (step 3 + Testing section correction)

## Concerns

- **D6 (process gaps) was explicitly out of scope for this pass** — the review
  marks it "maintainer call, not a reviewer's." While working in this worktree
  I observed `CHANGELOG.md`, `adr/README.md`, and a new
  `adr/0007-decide-tool-scope-and-conventions.md` already modified/added on
  disk (not by me, and not part of git history at session start) addressing
  exactly that finding — apparently in progress concurrently, outside this
  session. I left those files untouched and did not include them in my
  commits; they are unrelated to D1–D5 and belong to whatever process is
  already handling D6.
- No other concerns. All five findings verified fixed with the maintainer's own
  reproduction case (D1) and RED→GREEN evidence (D1, D2, D4); D3/D5 are
  narrowly-scoped documentation corrections that don't touch code or governed
  `docs/` content, confirmed by `validate.py` staying a no-op.
