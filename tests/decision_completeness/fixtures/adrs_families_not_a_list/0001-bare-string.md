```yaml
id: ADR-0001
title: families written as a bare scalar, not a YAML list
status: accepted
date: 2026-08-30
families: F05
```

# ADR-0001 · families written as a bare scalar, not a YAML list

## Context

`families:` is required to be a list of Composition ids (see
decision_completeness.py's own docstring), but nothing enforced that -- a
contributor writing a single-family ADR might type `families: F05` instead
of `families:\n  - F05`. YAML parses this to the plain string `"F05"`, not a
list containing one string.

## Decision

This should be reported as malformed (`families: is not a list`), not
silently iterated character-by-character (which used to produce three
bogus "'F' is not a Composition family/segment id" problems instead of one
clear one).

## Consequences

F05 should NOT be counted as addressed by this ADR.
