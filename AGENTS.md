# AGENTS.md

The front door for any AI agent contributing to this repository — human-dispatched, autonomously
scheduled, or picking this repo up cold with no other context. Read this first, in full, before
touching anything.

This file assumes no orchestrator is necessarily present to write you a bespoke task. If one is —
a human, or a session dispatching you with a detailed brief — follow that brief; it supersedes the
task-discovery steps below, though everything else here (citation discipline, review, the gotchas)
still applies regardless of who assigned the work.

---

## Start here

Read, in this order, before doing anything else:

1. `CLAUDE.md` — the technical model: tiers, stable IDs, versioning, front matter, the registry.
2. `CONTRIBUTING.md` — the process: kinds of change, PR shape, review.
3. `ROADMAP.md` — where the suite is headed and why, in that order.

If your task will touch anything under `docs/`, also read `suite-architecture.md` in full before
you write a word — it's short, and every rule in the three files above assumes it.

Do not skip this because a task looks small. A one-line citation fix and an eleven-entry Anatomy
slice both depend on the same tier/ID discipline, and getting it wrong either way produces a
correction someone else has to find later.

---

## Find your task

Work through this in order. Stop at the first step that gives you a real task.

**1. `ROADMAP.md`'s phases.** Read the whole file — it's short. Any item marked open or partial in
the current phase is the standing priority; earlier phases gate later ones on purpose (Phase 3
adoption/visibility waits for Phase 2 content coverage, which waits for Phase 1 infrastructure).
Don't skip ahead because a later phase looks more interesting than the current gap.

**2. Open GitHub issues labeled `proposal`.** `gh issue list --label proposal --state open`. These
are usually more actionable than a fresh ROADMAP item — a prior agent has often already done the
research (a scoping question, an audit finding) and the issue states exactly what's left to decide
or fix. Read the whole issue and its comments before starting; don't re-derive research that's
already there.

**3. If both are empty, generate audit-shaped work, not build-shaped work.** This is the answer to
"what do I do when there's nothing obvious left": re-read the suite against its own explicitly
stated rules and look for where reality has drifted from them. This isn't a fallback of last
resort — it's how a real, verified backlog of defects got found once the obvious work ran out.
Concretely, pick one and go deep rather than shallow across all of them:

- **Citation-correctness spot-check** — sample citations across the nine documents; for each, grep
  the cited ID's actual current definition and confirm the sentence citing it means the same
  thing, not just that the ID resolves. `validate.py` checks resolution; it cannot check meaning,
  which is exactly why this needs a reader, not a tool.
- **Ownership-boundary re-read** — pick a document, read it in full against
  `suite-architecture.md`'s ownership table, and look for a fact stated where it doesn't belong (a
  Composition entry secretly restating a Constraints number, a Verification check describing what
  something is made of instead of citing Anatomy for it).
- **Cross-document value-drift check** — grep for numbers (ratios, pixel values, percentages, WCAG
  criteria) across all nine documents and check whether any fact is stated as a bare value in more
  than one place instead of cited by ID from the one document that owns it.
- **Re-audit something already resolved, with fresh eyes.** A prior triage, exemption, or scoping
  call is not permanently above question — check whether its reasoning still holds the same way
  you'd check anyone else's work.

Report findings as a `proposal`-labeled issue (`.github/ISSUE_TEMPLATE/propose-change.yml` models
the shape) rather than fixing them inline, unless the finding is narrow and the fix is obviously
correct and low-risk — the same additive/corrective distinction `CONTRIBUTING.md` already draws
applies to whether you fix-and-PR or report-and-let-a-human-decide.

**4. Boundaries that don't move, regardless of what your search turns up:**

- `audit/tooling-audit-2.0.0.md` Part VI recommends exactly **one** tooling build and says
  building the rest of its gap register turns "a plan" into "a wish list." Don't propose a new
  tool because a gap looks buildable — check whether the audit already rated it not worth building
  first.
- `docs/anatomy-1.0.0.md` is single-writer, permanently, no matter how many component names or
  sub-areas remain open — see "Known gotchas" below for why.
- A decision that will shape many future contributors' work — a new document's organizing shape, a
  scoping call comparable to the information-architecture or content resolutions already recorded
  in Anatomy's Settled Decisions — gets opened as a `proposal` issue for a human to decide, not
  resolved unilaterally inside a task. The one exception: a human has explicitly delegated that
  specific call to you. If so, make it, and write the reasoning into the governed document's own
  Settled Decisions section the same way those two calls were recorded, so a future reader can see
  why, not just what.

---

## Do the work

`CONTRIBUTING.md` owns the actual process (kinds of change, PR shape, versioning) — read it, don't
expect it restated here. Three things worth emphasizing because getting them wrong is easy and the
mistake is subtle:

**Verify every citation you add, yourself, before you add it.** Grep the cited ID's actual current
text and confirm your sentence means the same thing — not that the ID exists. A real example: a
prior contribution cited `V-195` "Scrim," defined narrowly for text-over-imagery legibility, to
describe an unrelated modal-dialog backdrop. The ID resolved fine; `validate.py` passed; the
meaning was wrong. Nothing mechanical catches that class of error — you are the check.

**Respect the single-writer constraint on `docs/anatomy-1.0.0.md`.** Its `A-###` IDs are
sequential and append-only with no reservation mechanism — the next ID is just "one past whatever
`main` has right now." If you're working concurrently with anything else touching this file, stop;
only one Anatomy-editing task runs at a time, regardless of how many sub-areas are open. This is
true of any document's ID range in principle, but Anatomy is where it has actually bitten.

**Expect `tooling/registry.yaml` to show a diff even when you didn't mean to change it.** It
regenerates on every `validate.py` run. If your task and something else both touched `docs/`
around the same time, a conflict here is almost always benign — resolve by rebasing onto current
`main` and re-running `validate.py`, not by hand-merging the YAML.

---

## Open your PR

Follow `CONTRIBUTING.md`'s shape exactly — the change, the reason, the migration if breaking.
Classify your change correctly (additive / corrective / breaking per `G020`) since the review path
differs by kind. Reference any GitHub issue your work addresses in plain prose only — see "Known
gotchas" below before you write anything resembling a closing keyword near an issue number.

Never merge your own PR. State plainly in the PR body which issue(s) it addresses and what, if
anything, is still open — don't imply a broader resolution than what you actually did.

---

## Get reviewed

Every changed or added citation needs a second reader (`G025`) — a rule that doesn't relax because
you're confident, and doesn't relax because you already checked it once yourself. After opening
your PR:

**If your runtime can dispatch an independent sub-agent** (a Task or Agent tool, or equivalent),
do so, with this brief: read the PR's diff and description cold — no shared context with the agent
that wrote it — independently re-verify every citation and factual claim against the actual
current file content (not the PR's own assertions), re-run `python3 tooling/validate.py` from the
real branch, and post the findings as a **review comment**, not an approval. GitHub blocks
self-approval when every commit in a repo comes from one account, which is the normal case here —
a comment carrying named, checkable evidence (what was checked, against what, with what result) is
what `G082` itself now defines as sufficient evidence of review, precisely because a formal
approval isn't always mechanically available.

**If your runtime has no sub-agent dispatch capability,** say so plainly in the PR body, state
exactly what you verified yourself, and flag that a human second reader is still required before
merge. Don't skip the step silently — a PR that looks reviewed because nobody said otherwise is
worse than one that visibly says it isn't yet.

Either way: you do not merge. The maintainer does, once review — yours, a peer agent's, or a
human's — is genuinely on record.

---

## Known gotchas

**GitHub's issue-closing keyword parser does plain substring matching — it does not understand
negation.** Writing `not claiming "Closes #17"` in a PR body or commit message will still
auto-close #17, because the parser matches the literal substring regardless of the English
sentence around it. Reference issue numbers in plain prose only; close issues explicitly via `gh
issue close` when you mean to, never by writing out the phrase you're trying to avoid.

**Self-approval is blocked on a single-account repository.** If every commit comes from the same
GitHub account (the normal case here), that account cannot formally approve its own pull request.
This is not a bug to work around — it's why review evidence here is a comment with checkable
content, not a green checkmark.

**A citation that resolves is not a citation that's correct.** `validate.py` confirms an ID
exists; it has no way to confirm the sentence citing it means what the ID actually means. This is
the single most common real defect found in this suite's history — always the same shape: an ID
that's real, cited in a plausible-sounding sentence, that turns out to name something adjacent but
different. Grep the definition. Every time.
