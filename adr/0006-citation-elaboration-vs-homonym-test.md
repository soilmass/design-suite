```yaml
id: ADR-0006
title: The elaboration-vs-homonym test for judging a citation's correctness
status: accepted
date: 2026-09-03
```

# ADR-0006 · The elaboration-vs-homonym test for judging a citation's correctness

## Context

`tooling/validate.py` confirms a cited ID resolves; it has no way to confirm the citing sentence
means what the ID actually means. Two real incidents needed a human judgment call this suite had
no written standard for.

First: `docs/anatomy-1.0.0.md`'s dialog entry cited Vocabulary's `V-195` ("Scrim — a semi-
transparent layer placed over imagery to keep overlaid text legible") to describe a modal dialog's
interaction-blocking backdrop. The ID resolved; `validate.py` passed; the citation was wrong — a
modal backdrop and a text-legibility overlay technique are different things that happen to share
an English word. This was corrected by describing the backdrop in place and declining to cite
`V-195` at all.

Second, later: a new Anatomy entry for a severity-keyed message callout (icon, accent color,
`intent`) cited Vocabulary's `V-348` ("Callout — an inline box highlighting supplementary
information"). An independently-dispatched peer reviewer raised the same concern by analogy to the
first incident: Vocabulary's definition does not mention severity, icon, or accent color, so is
this the same class of error? The contributing agent pushed back with reasoning rather than either
capitulating or dismissing the concern, and the disagreement was escalated for a maintainer
ruling rather than resolved unilaterally by either agent — exactly the behavior `AGENTS.md` asks
for when a citation call is genuinely contested.

Adjudicating it required an actual test, not just a feeling that the two cases looked similar. The
test used: **does the Vocabulary definition, read cold, lead a reader to guess a different
referent than what's being described, or does it lead to the same referent with less detail?**
`V-195`'s "semi-transparent layer over imagery for text legibility" does not lead anyone to a
modal dialog's attention-blocking backdrop — a different thing, sharing a word. `V-348`'s "an
inline box highlighting supplementary information" is a fair one-line summary of a severity-keyed
callout; the icon, intent, and accent color describe *how* it highlights, not a different *what*.
That is also, provably, the normal relationship between every Anatomy entry and its own Vocabulary
citation — `V-310` Button's entire definition is "a control performing an action," and the Anatomy
entry citing it adds a state matrix, icon slots, and a hit-target obligation none of which appear
in that sentence, and this has never been read as a citation error. Requiring a Vocabulary
definition to already state every parameter Anatomy adds would invalidate every Anatomy entry in
the suite, since elaborating past Vocabulary's one-line denotation is the entire reason Anatomy
exists as a separate document.

## Decision

When judging whether a citation is correct, apply the elaboration-vs-homonym test: read the cited
document's definition cold, and ask whether it points a reader toward the same referent the citing
sentence describes (elaboration — correct, however much additional detail the citing document
adds) or toward a different one that merely shares a word or a surface resemblance (homonym
collision — wrong, regardless of how plausible the citing sentence otherwise reads). "The cited
definition doesn't mention every detail the citing sentence states" is explicitly *not* the test —
under that reading, no Anatomy entry would ever correctly cite Vocabulary.

## Consequences

The `V-348` citation was upheld, and the reasoning was folded into the Anatomy entry itself (its
"Distinguished from" paragraph now states the elaboration-vs-homonym distinction inline, citing
this same `V-195` precedent) so a future reader hits the standard directly rather than needing to
reconstruct it from a closed PR thread. This ADR exists so the standard is citable independently of
that specific paragraph, for the next citation dispute this suite's growth will eventually produce
— which will not be about Scrim or Callout specifically, and should not require rediscovering the
test from scratch.
