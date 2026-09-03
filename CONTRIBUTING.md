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

This project currently runs Governance's "small team" tier (`G082`): named review and recorded
rejections, but not yet the full proposal clock or named successors from the "organization" tier
(`G033`, `G013`) — those get added if and when the contributor base grows past what a maintainer
can review by hand. `ROADMAP.md` tracks that transition.

## Concurrent agent contribution

This project's contributors are, in real part, autonomous coding agents dispatched in parallel
batches — not a hypothetical: two batches so far, 11 merged PRs (#1–#9, #12, #14) and 3 open
scoping issues (#10, #11, #13), inside one afternoon. Everything above still applies to every PR
regardless of who opens it. What follows is additional, for failure modes that only show up when
several contributors edit the suite at once with no visibility into each other.

**Why this needs separate guidance.** A single human contributor rebases onto current `main`
before opening a PR, so races can't happen — there's only ever one editor's view of the tree at a
time. A batch of agents starts from one shared commit and works in parallel, isolated git
worktrees, opening several PRs before any of them can see what the others changed. That produces
two failure modes nothing in "Kinds of change" or "Review" above accounts for: two agents
computing the same "next" value from an append-only range, and two agents regenerating the same
derived file from diverging bases. Both have already happened here.

**Anatomy: one writer per batch.** `docs/anatomy-1.0.0.md`'s `A-###` IDs are sequential and
append-only, with no reservation mechanism — the next ID is just "one past whatever's in the file
on `main` right now." Two agents in the same batch adding Anatomy content both compute that same
next ID from the same starting point; whichever PR merges second either collides outright or
forces a rebase that renumbers IDs already cited elsewhere, and the suite's identifier-stability
rule (`suite-architecture.md`: an ID is assigned once and never reused) treats that as a real
break, not a merge nit.

In practice this has been kept to one Anatomy-editing agent per batch: PR #6
(`anatomy-components-slice`, A-062–A-066) landed alone in the first batch; PR #14
(`anatomy-input-controls-slice`, A-067–A-076) landed alone in the second. `ROADMAP.md` Phase 2
lists roughly forty more component terms as open, independently scopeable work — the constraint
isn't that Anatomy has no more open sub-areas, it's that the ID range itself is single-writer
regardless of how many sub-areas are open. Two Anatomy slices in a day means two sequential
batches, never two Anatomy agents in one.

**`registry.yaml`: same file, different bases, usually benign.** `tooling/registry.yaml`
regenerates on every `validate.py` run, so any PR touching `docs/` and any PR touching
`validate.py`'s own registry-generation logic both rewrite it — from whatever `main` looked like
when their worktree was created. PR #9 (`fix/registry-since-provenance`, changing how
`validate.py` computes each ID's `since` field) and PR #14 (adding A-067–A-076 and regenerating
the registry as a side effect) were both in the second batch, merged eight minutes apart. The
result wasn't a text conflict — it was subtler: PR #9's fix preserves whatever `since` value
already exists for a known ID rather than recomputing it (correct behavior in general), so once
A-062–A-076 had merged under the old, briefly-wrong logic, the new logic had no way to tell
"existing and correct" from "existing and stale" — it just carried the stale `1.0.0` forward. It
took a follow-up commit (`29a857d`), hand-correcting fifteen `since` values against a verified
known-wrong prior value, to fix.

Read this as the general shape, not a one-off: two PRs both touching `registry.yaml` is expected
and not a real logic conflict by default — resolve it by rebasing and re-running `validate.py`,
the same command "Before you open the PR" below already asks for. What made this instance land
wrong wasn't the regeneration, it was that regeneration ran, in order, across a boundary where the
generation logic itself was mid-change. When a batch includes both an agent editing `docs/` and an
agent editing `validate.py`'s registry code, plan on a `registry.yaml` re-check after the whole
batch lands, not just after each PR individually.

**Scoping a batch to avoid collisions.** Nothing stops two agents in the same batch from choosing
the same file — they can't see each other's diffs until their PRs land, and there's no lock. The
batches so far avoid this by stating explicit, non-overlapping file scope in each agent's task
description before dispatch, not by hoping the work happens to divide cleanly. The first batch's
eight PRs are a working example: the CI workflow (#1), `LICENSE`/`CHANGELOG.md`/`.editorconfig`
(#2), PR and issue templates (#3), the decision-completeness checker (#4), `validate.py`'s
regression tests (#5), the Anatomy component slice (#6), the Vale refused-terms triage (#7), and
pytest CI wiring (#8) — eight agents, eight disjoint areas, no two touching the same file.
`registry.yaml` is the one file that can't be scoped this way, because every `docs/`-touching PR
regenerates it as a side effect; say so explicitly in the batch's task descriptions rather than
assuming file-scope assignment alone covers it.

**Independent re-verification, not self-report.** "Review" above already requires a second reader
on every changed or added citation — that rule doesn't relax for an agent contributor, and an
agent's self-report specifically should be trusted less, not the same, as a human's: an agent can
run the wrong check, misread its own output, or be wrong about what a green result means, without
anything about the report itself looking off. Two concrete instances here, both caught only by
independently rerunning the work rather than trusting what the contributing agent reported:

- `238a82a` — `tooling/decision_completeness.py`'s `main()` always returned exit `0`, even when it
  had printed real `PROBLEM`s to stdout. A CI gate reading only the exit code — which is what "the
  tool passed" means in this repo — would never have caught it; a hand-built fixture with a known
  bad ADR did, on independent verification.
- `33b721c` — Anatomy's dialog scrim entry cited `V-195`, which resolves (`validate.py`'s own
  check would have passed it) but names a different sense of "scrim" than the one being described.
  Exactly the class of error `README.md`'s "citation correctness is unautomatable" already names —
  caught only because a second reader checked what V-195 actually says, not just that it resolves.

Neither failure was visible from the contributing agent's own report; both were only visible to
something that reran the check or reread the citation independently. Treat an agent's "`validate.py`
passes" or "citation resolves" as a claim to verify, not a result to relay.

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

Both currently run on the honor system; CI enforcement of both is tracked in `ROADMAP.md` Phase 1.

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
