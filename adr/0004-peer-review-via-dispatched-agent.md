```yaml
id: ADR-0004
title: Second-reader review via an independently-dispatched agent, evidenced by a comment
status: accepted
date: 2026-09-03
```

# ADR-0004 · Second-reader review via an independently-dispatched agent, evidenced by a comment

## Context

`docs/governance-1.0.0.md`'s `G025` requires every changed or added citation to get a second
reader — the one mandatory human review this suite's governance model has, because a citation
that resolves to the wrong identifier is syntactically fine and semantically broken, and nothing
mechanical catches that (see ADR-0006 for a real instance). For a single autonomous agent working
with no human immediately present, "get a second reader" has no obvious default: there is no
second person to ask.

Two mechanical facts shaped the answer. First, this repository's commits all come from one GitHub
account, and GitHub refuses to let an account approve its own pull request — confirmed directly,
not assumed, when a formal `gh pr review --approve` was attempted and failed outright. Second, an
independently-dispatched sub-agent, given no shared context with the agent whose work it is
reviewing and told to re-derive every claim from the actual current files rather than trust the
PR's own narrative, behaves as a genuinely separate check — it has caught real defects a same-
context reviewer could not have (a tool silently returning exit 0 on real problems; a citation
resolving to a real but wrong-sense identifier; a factual claim in a PR body that didn't match the
file it described).

## Decision

After opening a PR, an agent whose runtime supports dispatching an independent sub-agent should do
so, with a fixed brief: read the diff and PR description cold, re-verify every citation and
factual claim against the actual current file content, re-run the repository's validator from the
real branch, and post the findings as a **PR review comment**, not a formal approval. A comment
with named, checkable evidence — what was checked, against what, with what result — is treated as
sufficient review evidence under `G082`'s own definition of what counts as evidence versus mere
invocation, precisely because a formal approval is not always mechanically available. If an
agent's runtime has no sub-agent dispatch capability, it states so plainly in the PR and flags that
a human second reader is still required — never silently skipping the step.

In every case, whoever authored the PR does not merge it. A maintainer (human or otherwise, distinct
from the author) merges once review — a dispatched peer's, or a human's — is genuinely on record.

## Consequences

This is now `AGENTS.md`'s standing review process, not a one-off arrangement. It has run
successfully across multiple dispatch rounds, including one case where the dispatched reviewer
raised a substantive, well-reasoned disagreement rather than a rubber-stamp — see ADR-0006, which
records how that specific disagreement was adjudicated. `docs/governance-1.0.0.md`'s `G082` was
separately tightened (a distinct, generic governance rule: evidence must be checkable) rather than
folded into this ADR, since `G082` states what any project at this governance tier must satisfy,
while this ADR records the specific mechanism this repository uses to satisfy it — a repo-specific
implementation choice, not a portable governance rule other projects using this suite would
necessarily copy verbatim.
