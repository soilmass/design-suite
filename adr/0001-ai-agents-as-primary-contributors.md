```yaml
id: ADR-0001
title: AI agents as primary contributors; AGENTS.md as their front door
status: accepted
date: 2026-09-03
```

# ADR-0001 · AI agents as primary contributors; AGENTS.md as their front door

## Context

This project's stated contribution model, from its first commit, was that contributors would be
autonomous coding agents rather than (or in addition to) human developers. For the first several
dispatch rounds, every agent received a hand-written, bespoke task prompt — exact file scope,
exact citations to verify, exact PR shape — because nothing in the repository itself told a fresh
agent how to orient, how to find a task with nobody assigning one, or how to get reviewed without
a human standing by. That worked, but it meant every round of work depended on someone (a human,
or a session with full conversation history) writing that brief from scratch each time.

Two things this session actually needed answered, repeatedly, before any content work could
happen: what does a contributor read first, and what does it do when the obvious backlog is
empty.

## Decision

Write `AGENTS.md` as the canonical, self-contained onboarding document for any agent — human-
dispatched or fully autonomous — assuming no orchestrator is necessarily present. It covers, in
order an agent actually needs them: what to read first, a priority cascade for finding a task
(`ROADMAP.md` → `proposal`-labeled issues → generating audit-shaped work), the citation-
verification discipline, PR shape, and the review mechanism (ADR-0004). `CLAUDE.md` — already the
technical/structural reference every Claude Code session auto-loads — gets a one-line pointer at
its very top sending the reader to `AGENTS.md` first.

The alternative considered and rejected: keep folding agent-specific guidance into
`CONTRIBUTING.md`'s existing "Concurrent agent contribution" section indefinitely. Rejected
because that section was already duplicating content that belonged in one canonical place, and a
process document mixing "here's how a human proposes a change" with "here's how an autonomous
agent finds its own work" was becoming two documents wearing one name.

## Consequences

Every subsequent dispatch round in this repository's history could hand an agent a much shorter,
task-specific brief and rely on `AGENTS.md` for the general discipline — verified directly: the
first PR opened against `AGENTS.md` itself was reviewed by an agent that had read nothing but the
document and the diff, and a later round included an agent given no task at all beyond "follow the
cascade," which independently re-verified the whole recent backlog itself rather than trusting a
summary, and correctly reported it could find nothing legitimate left to do — a genuine negative
result, not a failure to produce one (see `AGENTS.md`'s "Find your task" step 3, which names this
outcome as acceptable precisely because this instance proved it happens rather than remaining
theoretical). `CONTRIBUTING.md`'s concurrent-agent section was trimmed to a stub pointing here,
removing the duplication this ADR's Context section flags.
