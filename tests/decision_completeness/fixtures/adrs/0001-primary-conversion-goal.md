```yaml
id: ADR-0001
title: Primary conversion goal is trial signup
status: accepted
date: 2026-08-14
families:
  - F01
  - F01.2
deciders: [maya, chen]
```

# ADR-0001 · Primary conversion goal is trial signup

## Context

F01 Mandate is the only Composition family coupled to nothing, so Decision's
D003 requires it be set first and alone. We had never written down what this
site's single job is, and pages were quietly optimizing for three different
things.

## Decision

The site's mandate (F01) is conversion, and the primary conversion action
(F01.2) is a free trial signup, singular, above the fold on every page that
argues for the product.

## Consequences

Every other family that inherits from or couples to F01 -- audience,
position, risk posture per D003 -- gets decided against this, not against a
comprehension or credibility goal.
