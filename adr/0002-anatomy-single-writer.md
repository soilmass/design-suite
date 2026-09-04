```yaml
id: ADR-0002
title: docs/anatomy-1.0.0.md is single-writer per batch, permanently
status: accepted
date: 2026-09-03
```

# ADR-0002 · docs/anatomy-1.0.0.md is single-writer per batch, permanently

## Context

`docs/anatomy-1.0.0.md`'s `A-###` identifiers are sequential and append-only, with no reservation
mechanism — the next ID is computed as "one past whatever `main` currently has." Concurrent
contributors working in isolated git worktrees, per this repo's actual dispatch model, cannot see
each other's in-progress diffs until a PR lands. Two agents both adding Anatomy content in the
same batch would independently compute the same next ID from the same starting point; whichever
PR merges second either collides outright or forces a rebase that renumbers IDs already cited
elsewhere — and `suite-architecture.md`'s identifier-stability rule (an ID is assigned once and
never reused) treats a renumber as a real break, not a merge nit to shrug off.

This was not a hypothetical worked out in advance. It is the reason the first two dispatch
batches each contained exactly one agent touching Anatomy, discovered by necessity before it was
written down anywhere.

## Decision

Exactly one agent may add content to `docs/anatomy-1.0.0.md` (or touch `tooling/registry.yaml`,
which regenerates from it) per dispatch batch, regardless of how many independently-scopeable
sub-areas remain open. Multiple open component groups do not justify multiple concurrent Anatomy
writers — they justify multiple sequential batches. This constraint is permanent, not a
transitional rule to relax once tooling improves: the append-only, no-reservation ID scheme is a
deliberate feature of the suite's identifier-stability guarantee (`suite-architecture.md`), not
an incidental limitation.

The alternative considered and rejected: a reservation or locking mechanism (e.g. a claimed-ID-
range file) that would let two agents safely work on Anatomy in the same batch. Rejected as
unnecessary complexity for a suite this size — the actual cost of sequencing two Anatomy slices a
few hours apart instead of running them in parallel is small, and a locking mechanism is itself a
new failure surface (a stale lock, a claim nobody released) in a repository whose contributors
cannot always coordinate directly with each other.

## Consequences

Every Anatomy-touching dispatch since this constraint was recognized has held to one writer per
batch — six content-adding slices (`docs/anatomy-1.0.0.md` 1.1.0 through 1.6.0), zero ID
collisions. It is now written into
`AGENTS.md`'s "Do the work" section as standing guidance, not something an orchestrator has to
remember to state explicitly each time — though an orchestrator dispatching a batch still states
it explicitly as a courtesy, the same way this ADR does, because the cost of a contributor missing
it once is a real break, not a warning.
