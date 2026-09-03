```yaml
id: ADR-0001
title: Decided several directories deep
status: accepted
date: 2026-08-30
families:
  - F04
```

# ADR-0001 · Decided several directories deep

## Context

decision_completeness.py's own docstring claims ADRs may live "anywhere
under the directory you point this at (scanned recursively)". This file
lives two directories below the ADR root to verify that claim directly
rather than trusting the docstring.

## Decision

F04 (Risk posture) is decided here, nested under adrs_nested/deep/deeper/.

## Consequences

Should still be found and counted by a top-level scan of adrs_nested/.
