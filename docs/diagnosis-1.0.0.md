```yaml
document: Diagnosis
version: 1.0.2
tier: 3
owns:
  - how to read an existing site into the family set
  - how each family can be known, and how confidently
  - the protocol for a read, and the record it produces
exports: R001–R067
depends:
  - Vocabulary ^1
  - Anatomy ^1
  - Composition ^1
  - Constraints ^1
  - Decision ^1
reviewed: 2026-09-03
```

# Diagnosis

Reading a site you did not build. The reverse of Composition: given an artifact, recover the settings.

**Distinct from Verification.** Verification tests your site against your own record of what you decided. Diagnosis has no record — it works on any site, including the very common case of a site where nothing was decided at all.

---

## What this document owns

How each family can be known, how confidently, in what order, and what to write down.

## What it does not own

| Question | Owner |
|---|---|
| What choices exist? | Composition |
| What may not be done? | Constraints |
| What should the setting be? | Decision |
| How do I check my own site against my own intent? | Verification |

Diagnosis produces a reading, never a verdict. The moment a read includes "and they should have," it has become Decision applied to someone else's site without their constraints, and it is worth less than it appears.

---

# PART I — THE CENTRAL LIMIT

## R001 · The artifact under-determines the decision

A site with one typeface may have decided *one typeface* or may never have decided anything. Both produce identical evidence. **Diagnosis can recover the setting; it can never recover whether the setting was set.**

This is not a limitation to work around. It is the defining property of the activity, and every claim in a read must survive it. "They chose a single typeface" is unsupportable. "The site uses a single typeface" is supportable. The difference is the whole discipline.

## R002 · Deliberateness is never observable

The corollary. No amount of evidence distinguishes a considered choice from an unexamined default from a framework's factory setting. A read that attributes intent has stopped describing the artifact and started writing fiction about the organization.

The one partial exception: a departure from convention that costs something to implement is *weak* evidence of deliberateness, because defaults are free and deviation is not. Weak evidence, not proof.

## R003 · A read is dated

Sites change. A read is a photograph, and it should carry its date, the pages sampled, and the conditions — viewport, network, region, whether logged in. An undated read is unfalsifiable and worthless six months later.

---

# PART II — OBSERVABILITY CLASSES

*The organizing structure of this document. Composition treats all sixty-seven families as peers; from outside, they are not remotely equal. A read that reports all sixty-seven with the same confidence is lying about most of them.*

## R010 · The five classes

**Measured** — computed from the artifact by a tool. Reproducible; two readers get the same number.
**Observed** — plainly present, requires a person to look but not to reason.
**Inferred** — reasoned from several observations. Two competent readers may differ.
**Reported** — the site's own claim about itself. Evidence of what it says, never of what is true.
**Closed** — not knowable from outside at any confidence. Requires access to the organization.

## R011 · Measured

`F09` `F11` `F14` `F15` `F18` `F24` `F30` `F31` `F32` `F33` `F34` `F37` `F39` `F41` `F42` `F43` `F50` `F51` `F59` `F60` `F61` `F63`

Tooling per family is a Verification concern and the same instruments apply — CSS analysis for the surface families, crawl for topology and addressing, network inspection for payload and instrumentation, an accessibility rule engine for the access families, timing for responsiveness, word and readability counts for the language families.

**Confidence: high.** Report as numbers, not adjectives. "Forty-one distinct font sizes" beats "inconsistent typography," survives disagreement, and can be re-run.

**F39 splits.** Motion quantity and duration are measured from computed styles; motion *character* — sharp, smooth, springy, mechanical — is Observed per R012. Where a family spans two classes, record the segment-level class rather than forcing one onto the family. F20 and F63 split the same way and are listed under their dominant class.

## R012 · Observed

`F05` `F06` `F07` `F08` `F10` `F12` `F17` `F19` `F21` `F22` `F23` `F26` `F27` `F28` `F29` `F35` `F36` `F38` `F40` `F55` `F56` `F57` `F58` `F62` `F64` `F65` `F66` `F67`

Presence, absence, and plain characteristics. Two readers should agree, and where they do not, the family description was applied loosely.

**Confidence: high, conditional on sampling.** Most errors in this class are sampling errors, not judgement errors — the reader looked at three pages and reported on the site.

## R013 · Inferred

`F02` `F03` `F04` `F13` `F16` `F20` `F25` `F44` `F46` `F47` `F48` `F49` `F52` `F53` `F54`

Requires reasoning across observations, and several require *repeat visits over time*, which a single-session read cannot supply. The time families in particular — F46 through F49 — need either longitudinal access or archive evidence, and a read that reports them from one visit is guessing.

**Confidence: medium at best.** Every claim in this class carries its evidence inline or it is not a claim.

## R014 · Reported

`F03.1` `F03.3` `F45` `F62.1`

Positioning claims, editorial stance, maintenance practice, and stated conformance level are things the site asserts. Record them as assertions. A published accessibility statement is evidence of a statement, and the measured access families in R011 will say whether it is accurate — which is often the single most informative comparison in a whole read.

**Confidence: high about the claim, none about the fact.**

## R015 · Closed

`F01` `F01.2` `F01.3` `F02.3` `F45.3` `F65.3` — and, for every family, the question of deliberateness per R002.

Mandate, success definition, assumed intent, who can change what, and whether a preselected default was self-serving or thoughtless. A primary conversion can sometimes be inferred from prominence; a *mandate* cannot be inferred at all.

**Confidence: none.** Leave blank. A read with blanks in it is more credible than one without, and a reader who fills these has told you about themselves.

---

# PART III — THE PROTOCOL

## R020 · Scope first

Declare before looking: which pages, which templates, which states, which viewports, which region, logged in or out. A read of eight pages across five templates is useful; a read of "the site" is not reproducible.

**Minimum viable sample** — the entry page, one page of each template type, one form, one failure surface, and one representation surface. Five kinds, not five pages.

## R021 · Pass 1 — Automated
Run the measured families. Do this first: it is cheap, it is reproducible, and the numbers frame everything after. Capture CSS analysis output, payload figures, accessibility audit, field performance where available, and the crawl.

## R022 · Pass 2 — Structural
Topology, navigation, path, addressing. Follow the crawl rather than the navigation, because the difference between them is itself a finding.

## R023 · Pass 3 — Inventory
Which surfaces exist and how deep each goes. Fastest pass, and per Composition the absences carry more than the presences.

## R024 · Pass 4 — Reading
The language plane. Read continuous prose, not fragments. Person, register, sentence construction, claim structure, naming, terminology, headlines, mechanics. This pass cannot be shortened and cannot be automated past readability scoring.

## R025 · Pass 5 — Interaction
States, forms, errors, failure surfaces, responsiveness. **Deliberately break things** — submit an empty form, request a missing page, disconnect the network, resize to 320px (C026), navigate by keyboard only. This pass produces the highest finding-per-minute of any in the protocol, because it visits the surfaces least likely to have been designed.

## R026 · Pass 6 — Representation
How the site appears where it is not: search result, link preview, structured data, third-party listings, and what a summarizer says about it. Frequently divergent from the site itself, and the divergence is the finding.

## R027 · Pass 7 — Time
Return visit, archive evidence, dated content, changelog. Bounded by what a single session allows; state that bound rather than inferring past it.

## R028 · Pass 8 — Synthesis
Fill the family sheet. Every entry carries its observability class and its evidence. Blanks stay blank.

## R029 · Pass 9 — Congruence
Apply the congruence tests from Decision, with one modification: with no decision record available, you are testing the artifact's agreement *with itself* rather than with a stated intent. That is what those tests do anyway, which is why they transfer to external sites unchanged.

The three questions carry most of the value here (D111) — how big does this claim to be, how much does it appear to mean it, how much care went in — and disagreement between the answers is the finding.

---

# PART IV — THE READ RECORD

## R040 · One row per family

```
F31 · Typography
Class:      Measured
Evidence:   3 families, 9 weights, 41 distinct computed sizes
            across 8 sampled pages
Reading:    Declared scale not recoverable; distinct-size count
            is ~6x a typical scale length
Confidence: High
```

Four fields. **Evidence and reading are separate rows because they get conflated**, and once conflated the read cannot be checked by anyone else.

## R041 · Blanks are content

Closed families are recorded as closed, not omitted. An omitted family is indistinguishable from an overlooked one.

## R042 · Reads are comparable only within a protocol version

Two reads compare only if the sample scope, the tool versions, and this document's version match. State all three. A library of reads taken under different protocols is a pile of anecdotes.

---

# PART V — FAILURE MODES

*Diagnosis fails in specific, repeatable ways. Each of these has produced a confident wrong read.*

## R060 · Projection
Recording your own preference as their decision. Detection: any reading that would change if you personally liked the site more.

## R061 · Hindsight coherence
A shipped site looks intentional because it exists. Most of what you are reading was not decided. R001 and R002 exist to counter this, and it remains the most common failure.

## R062 · Homepage bias
The entry page is the most designed page on almost every site and is the least representative. Reading it as the site systematically overstates craft, hierarchy, and care.

## R063 · Sample-of-one
Reporting a family from a single instance. Most acute for F40 craft and F64 failure handling, both of which vary enormously across a site.

## R064 · Constraint mistaken for choice
A legal requirement, a platform mandate, or a perceptual floor is not a decision. Consent banners, target sizes, and reduced-motion paths are frequently read as design choices when they are Constraints entries. Check against C before attributing.

## R065 · Recency
Reading a partial redesign as the system. A site mid-migration presents two systems and reads as incoherent when it is merely unfinished. Look for the seam before concluding.

## R066 · The competitive-analysis trap
A read of a competitor tells you what they did. It carries no information about what you should do, because you do not have their mandate, audience, constraints, or resources — and the first two are Closed to you per R015. A read used as a target is a read misused.

## R067 · Tool-shaped findings
The measured families produce numbers, so reads over-report them and under-report the language and conduct planes, which produce no numbers and matter more. Detection: count findings per plane. If Surface and Substrate dominate, the read is describing the tooling.

---

# EXPORT INDEX

| ID | Entry |
|---|---|
| R001 | The artifact under-determines the decision |
| R002 | Deliberateness is never observable |
| R003 | A read is dated |
| R010 | The five observability classes |
| R011 | Measured |
| R012 | Observed |
| R013 | Inferred |
| R014 | Reported |
| R015 | Closed |
| R020 | Scope first |
| R021 | Pass 1 — Automated |
| R022 | Pass 2 — Structural |
| R023 | Pass 3 — Inventory |
| R024 | Pass 4 — Reading |
| R025 | Pass 5 — Interaction |
| R026 | Pass 6 — Representation |
| R027 | Pass 7 — Time |
| R028 | Pass 8 — Synthesis |
| R029 | Pass 9 — Congruence |
| R040 | One row per family |
| R041 | Blanks are content |
| R042 | Reads are comparable only within a protocol version |
| R060 | Projection |
| R061 | Hindsight coherence |
| R062 | Homepage bias |
| R063 | Sample-of-one |
| R064 | Constraint mistaken for choice |
| R065 | Recency |
| R066 | The competitive-analysis trap |
| R067 | Tool-shaped findings |

---

## Settled decisions

**Observability class is the organizing structure, not plane order.** Composition's planes describe how a site is built; they say nothing about how it can be seen. From outside, F31 typography and F01 mandate are not comparable evidence, and a document organized by plane would present them as though they were. Sorting by how a thing can be known is the same move Constraints makes by sorting on why a thing binds.

**Fifteen families are Inferred and six are Closed.** That is roughly a third of the family set at medium confidence or none. Stating it up front is the point: a read that returns sixty-seven confident answers has fabricated at least twenty-one of them.

**Diagnosis produces a reading, not a verdict.** No recommendations, no scoring, no grades. The moment a read includes what they should have done, it has applied Decision to an organization whose mandate and constraints are Closed — which R066 identifies as the most common way a read gets misused.

**The interaction pass instructs the reader to break things.** R025 is the highest-yield pass in the protocol precisely because failure surfaces, empty states, and 320px widths (C026) are the parts of a site least likely to have been designed, and they are invisible to anyone browsing normally.
