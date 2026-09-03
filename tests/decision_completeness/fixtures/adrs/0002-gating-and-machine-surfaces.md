```yaml
id: ADR-0002
title: No account gate before the pricing page; full structured data
status: accepted
date: 2026-08-21
families:
  - F10.1
  - F10.2
  - F09.4
deciders: [chen]
```

# ADR-0002 · No account gate before the pricing page; full structured data

## Context

Sales wanted a signup wall on the docs. Support wanted the opposite. Neither
had looked at F10 Gating as a single family with a range, so the disagreement
kept resurfacing per feature rather than getting settled once.

## Decision

Account gate depth (F10.1) is set to "nothing behind login" for docs and
marketing pages; the purchase path (F10.2) stays self-serve. Structured data
(F09.4) is comprehensive -- product, pricing, and FAQ schema on every
relevant page, since organic discovery is load-bearing for this mandate.

## Consequences

Bounded by C042 and C070 per Composition's F10 entry -- Legal signed off that
neither bound is crossed by an open docs section.
