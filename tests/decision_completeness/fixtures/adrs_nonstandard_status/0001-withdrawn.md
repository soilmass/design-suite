```yaml
id: ADR-0001
title: Withdrawn proposal for audience targeting
status: withdrawn
date: 2026-08-30
families:
  - F02
```

# ADR-0001 · Withdrawn proposal for audience targeting

## Context

`status: withdrawn` is not one of the values decision_completeness.py's own
docstring calls out by name (`accepted`, `proposed`, `rejected`,
`superseded`) -- a team might use its own status vocabulary.

## Decision

Only `status: accepted` should ever count as addressing a family. Any other
value -- named in the docstring or not -- should land in the "pending"
bucket alongside the ADR path and its literal status string, not crash and
not be silently treated as accepted.

## Consequences

F02 stays on default until an accepted ADR supersedes this one.
