```yaml
id: ADR-0001
title: Family id cited in lowercase
status: accepted
date: 2026-08-30
families:
  - f01
```

# ADR-0001 · Family id cited in lowercase

## Context

`families:` cites `f01` in lowercase instead of the canonical `F01`. IDs are
always uppercase by convention (see CLAUDE.md's stable identifiers table),
but a contributor might type it lowercase by habit.

## Decision

F01 (Mandate) should still resolve and count as addressed -- the join logic
uppercases before matching against the registry.

## Consequences

None -- this is a formatting nit, not a real decision.
