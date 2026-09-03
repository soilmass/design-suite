```yaml
id: ADR-0001
title: "unterminated quoted string
status: accepted
families:
  - F06
```

# ADR-0001 · Unterminated quoted string in front matter

## Context

The front matter fence is present and the block looks superficially like
YAML, but the `title:` value's opening quote is never closed -- this is not
parseable YAML at all, not just YAML with the wrong shape.

## Decision

This should be reported as a malformed ADR (skipped, with a reason), not
crash the whole tool with an uncaught yaml.scanner.ScannerError before any
other ADR in the directory gets scanned.

## Consequences

F06 should NOT be counted as addressed by this ADR.
