```yaml
id: ADR-0001
title: Families list present but empty
status: accepted
date: 2026-08-30
families: []
```

# ADR-0001 · Families list present but empty

## Context

The `families:` key is present in front matter, per the required-field
convention, but its list is empty -- no Composition family is actually
cited.

## Decision

None -- this ADR should be treated as malformed, the same as one missing
`families:` entirely, since it addresses zero families.

## Consequences

None yet.
