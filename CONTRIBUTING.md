# Contributing

This suite runs on its own `docs/governance-1.0.0.md`. What follows is that document's rules,
applied at the tier this project currently operates at — see `ROADMAP.md` Phase 1 for why now is
when this file exists at all. If something here and Governance ever disagree, Governance wins;
open a correction against this file.

## Before you propose anything

Read `README.md`'s "read in this order" section, then `suite-architecture.md` in full — it's
short and every rule below assumes it. The one you'll hit immediately: **a document may cite
downward, never upward, never sideways.** If your change would make Vocabulary reference
Composition, or Decision reference Implementation, stop — the fix is almost always to move the
fact, not to add the citation.

Check the ownership map in `suite-architecture.md` §2 before deciding which document a change
belongs in. If more than one document could defensibly own your fact, that's not a judgment call
to make silently — say so in the PR description and let review resolve it.

## Kinds of change

Governance (`G020`–`G025`) splits changes into three kinds with three different costs. Match
your PR to the right one — treating a breaking change as additive is how citations silently
start pointing at the wrong thing.

- **Additive** — a new entry, section, or document. Nothing existing changes meaning. No special
  process: write it, version it (front matter `version:` bump, minor), open the PR.
- **Corrective** — an error in an existing entry gets fixed. Meaning changes because the old
  meaning was wrong. Needs one reader other than you to confirm the correction is actually
  correct — say in the PR description who that will be, or expect the maintainer to be it.
- **Breaking** — an identifier's meaning changes, or an identifier is removed. Anything citing it
  may now be wrong. **Do not delete the old identifier.** Mark it deprecated with a named
  successor, publish that first, and let dependents migrate before the identifier is ever
  removed. See Governance `G023`/`G040`/`G041` for the full sequence.

## How to open a pull request

A PR is a proposed edit, not a discussion — per `G030`, if your idea needs a meeting or a design
doc before it's a diff, it isn't ready to propose yet. Every PR description contains, per `G031`:

1. **The change** — what identifier(s), document(s), or files are affected.
2. **The reason** — why this is correct or needed, not just that it is.
3. **The migration** — required only for breaking changes: what dependents need to do, and by
   when the old identifier gets removed. A breaking-change PR missing this isn't ready; a
   corrective or additive PR without a stated reason is a preference, not a proposal.

## Review

The maintainer reviews every PR. Per `G025`, **every changed or added citation gets a second
reader** — this is the one mandatory human review in Governance, because a citation that resolves
to the wrong identifier is syntactically fine and semantically broken, and nothing mechanical
catches that. For an external PR, the maintainer is that second reader; you don't need to
arrange one yourself.

This project currently runs Governance's "small team" tier (`G082`): named review, evidence of
that review left checkable against the change itself, and recorded rejections, but not yet the
full proposal clock or named successors from the "organization" tier (`G033`, `G013`) — those get
added when review starts falling behind change, per `G082`'s own tier-transition signal, not when
a headcount crosses some number. `ROADMAP.md` tracks that transition.

## Concurrent agent contribution

This project's contributors are, in real part, autonomous coding agents, often dispatched in
parallel batches with no visibility into each other. Full guidance — orientation, how to find a
task, the single-writer and `registry.yaml` constraints, review, and the specific gotchas this
project has actually hit — lives in `AGENTS.md`, not here. Read that; this section exists only so
this file's own table of contents doesn't silently drop the topic. Everything else in this file
still applies to every PR regardless of who opens it.

## Before you open the PR

```bash
cd tooling
pip install pyyaml
python3 validate.py
```

This checks front matter, tier correctness, declared exports against what's actually in the
document, dependency direction, every cross-reference, and Governance's orthogonality — and
regenerates `tooling/registry.yaml`. If your change adds or retires an ID, commit the regenerated
registry alongside it.

```bash
vale --config=tooling/vale/.vale.ini docs/
```

Prose lint against the refused-terms list in `tooling/vale/styles/Suite/RefusedTerms.yml`.

Both run in CI on every pull request and push to `main` (`.github/workflows/validate.yml`, per
`ROADMAP.md` Phase 1) — run them locally first so a problem is yours to fix before CI reports it.

## If your proposal is declined

Per `G032`, a declined proposal gets written down with its reason in the document it targeted —
usually its **settled decisions** section. This isn't a formality: without it, the same proposal
comes back in eight months and gets re-argued from zero by someone with no way to know it was
already settled. If the maintainer declines your PR, expect that note to be added as part of the
close-out, not just a closed-PR comment that disappears from view.

## Out of scope right now

`README.md`'s "What is not covered" section is the one place this is listed — read it before
proposing work in any of those areas, and open a discussion first rather than a PR. The one
carve-out: Anatomy volume 2 and the decision-completeness checker are back in scope under
`ROADMAP.md` Phase 2, with their own ID ranges assigned deliberately rather than bolted onto
what exists.
