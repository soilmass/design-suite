```yaml
id: ADR-0005
title: No direct-to-main pushes, including the maintainer's own small fixes
status: accepted
date: 2026-09-03
```

# ADR-0005 · No direct-to-main pushes, including the maintainer's own small fixes

## Context

During a fast-moving batch of concurrent contributor agents, a small, mechanical, thoroughly
self-verified correction (hand-fixing fifteen `since` values in `tooling/registry.yaml` after the
concurrent-regeneration issue described in ADR-0003) was pushed directly to `main`, bypassing the
PR gate — a one-off expedience, not a considered exception. A subsequent governance
fit-for-purpose review caught this directly, comparing real `git log` history against
`CONTRIBUTING.md`'s own stated rule that the maintainer reviews every PR, and found the exception
was undocumented and unprincipled: nothing distinguished it from any other corrective change that
should have gone through review like every contributor's does.

## Decision

Every change, without exception, goes through a PR — including the maintainer's own corrective
fixes, however small or however thoroughly self-verified before pushing. `CONTRIBUTING.md`'s "the
maintainer reviews every PR" does not carry an unstated exception for the maintainer's own commits.
The one-off direct push that prompted this ADR is treated as the mistake it was, not as a precedent
narrowed by carve-outs (e.g. "except for registry data" or "except for single-line fixes") — a
carve-out is exactly the kind of unprincipled exception that made the original mistake possible.

## Consequences

Every subsequent maintainer-authored fix in this repository's history — including small ones, like
correcting a stale cross-reference or removing an out-of-date README bullet — has gone through a
branch, a PR, a real CI run, and a posted review comment (see ADR-0004) before merging, with no
exceptions since this ADR. This is a small, real cost (a branch and a PR for a one-line fix) traded
for a review trail that holds without a special case to remember.
