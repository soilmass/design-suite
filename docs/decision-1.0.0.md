```yaml
document: Decision
version: 1.0.1
tier: 2
owns:
  - the order in which choices are set
  - how much each choice matters
  - what is traded against what
  - which combinations cohere
  - what to set absent a reason
exports: D001–D204
depends:
  - Composition ^1
  - Constraints ^1
reviewed: 2026-09-03
```

# Decision

Composition says sixty-seven choices exist. Constraints says where their ranges stop. Neither tells you what to do, which is what makes a complete inventory paralyzing rather than useful. This document is the procedure.

---

## What this document owns

Order, weight, tradeoff, coherence, and defaults. Everything that turns an enumeration into a sequence of decidable questions.

## What it does not own

| Question | Owner |
|---|---|
| What choices exist, and what are their ranges? | Composition |
| What may I not do? | Constraints |
| How does a decision become a token or component? | Implementation |
| How do I confirm the decision was realized? | Verification |
| What does this term mean? | Vocabulary |

This document sets *targets*; Constraints sets *floors*. When a target here appears to conflict with a floor there, the floor wins and the target was wrong.

---

## Notation

**Rounds** group families that must be decided together rather than in sequence.
**Leverage** is impression per unit of effort, not importance in the abstract.
**Tradeoffs** are written `A ↔ B` and name what is lost, not merely that something is.
**Coherence tests** are written as a mismatch and the reading it produces. They are diagnostic, not prohibitive — several are worth incurring deliberately.
**Defaults** are the setting that costs least to reverse, not the best setting.

---

# PART I — ORDER

## D001 · Three forces determine order

Order is not a preference. It falls out of three independent pressures, and where they disagree, they disagree in a specific priority.

**Bounding** — a range cannot be set before its floor is known. Constraint intake precedes everything.
**Inheritance** — a plane cannot be set before the planes it depends on. Purpose precedes structure precedes surface.
**Coupling** — coupled families cannot be sequenced against each other at all. They are decided in one sitting or they will be decided twice.

Priority when they conflict: bounding, then coupling, then inheritance. Coupling outranks inheritance, which produces the one genuinely surprising result in this document — see D004.

## D002 · Round 0 — Constraint intake

Before any family is set, determine which entries in Constraints apply. This is a factual question with a factual answer, and getting it wrong invalidates work downstream rather than merely degrading it.

Establish: operating jurisdictions, sector, headcount and turnover against the C060 microenterprise threshold, whether any public-sector or federally-funded status attaches, and whether subscriptions or negative-option billing are in scope.

Output: a list of applicable C IDs, dated. Re-run quarterly for the volatile entries.

## D003 · Round 1 — Purpose

**F01 first and alone.** F01 Mandate is the only family in Composition coupled to nothing. It can therefore be set in isolation, and every subsequent question resolves against it. A team that cannot state F01.2 in one sentence is not ready for Round 2.

**Then F02, F03, F04 together.** Audience, position, and risk posture interlock through F02↔F22 and F04↔F31/F34/F39. Setting them separately produces a site addressed to one audience in the register of another.

## D004 · Round 2 — Structure and naming, jointly

F11–F14, plus **F26 Naming**.

This is the surprise. Composition places Naming in Plane 5 and Structure in Plane 3, so inheritance says structure first. But F12↔F26 is a tight coupling: navigation labels *are* copy, and you cannot finalize a navigation model without knowing what the things are called. Coupling outranks inheritance, so naming is pulled forward two planes.

Practical consequence: do not wireframe with placeholder labels. The placeholder will survive to launch and it will be wrong.

## D005 · Round 3 — Inventory

F05–F10.

Depends on Round 1 and constrains everything after. What the site consists of determines how much there is to arrange, which is why it precedes arrangement rather than following it.

Set F05.1 pricing disclosure here, deliberately and early. It is the single loudest inventory decision and it cascades into F65, F66, and the entire commercial conduct cluster.

## D006 · Round 4 — The density cluster

F15, F16, F33, F30, F18 — decided as one.

Composition records F15↔F16↔F33 as tight and F15↔F30 as tight. That makes density, pacing, spacing scale, copy volume, and page composition a single five-way decision. Attempting them in sequence guarantees rework, because setting a spacing scale before knowing copy length means setting it twice.

The question to answer once, for all five: *how much does this site say per screen, and how much room does it give each thing it says?*

Bounded by C004 measure, C027 spacing override tolerance, C028 target size.

## D007 · Round 5 — The emphasis triangle

F17, F31, F32 — decided as one.

Hierarchy is not expressed by itself. It is expressed through type and color, which is why Composition records F17↔F31 and F17↔F32 as tight. Choosing a typeface before knowing how many levels of emphasis the site needs produces a family with the wrong weight range.

Bounded by C020, C021, C022, C023, C011.

## D008 · Round 6 — Remaining language

F22–F25, F27–F29. Free of tight coupling once F26 and F30 are set in earlier rounds.

## D009 · Round 7 — Remaining surface

F19, F34–F40. Shape, depth, imagery, iconography, texture, motion, craft.

F40 Craft is set here in name only. It is not a decision made once; it is a standard held across every subsequent round, and D203 treats it as such.

## D010 · Round 8 — Adaptation and access

F20, F59–F62.

Access is placed here, after surface and before substrate, for one reason: late enough that there is something concrete to evaluate, early enough that fixing it is still cheap. The access constraints — C023, C024, C026, C028, C030 through C033, C038, and C046 — cost little when satisfied by construction and a great deal when retrofitted. C046 is the reason: name, role, and value cannot be added to a custom control afterward, only rebuilt into it. Deferring this round past Round 9 is the most expensive scheduling error available.

## D011 · Round 9 — Substrate

F41–F45. Rendering, payload, instrumentation, infrastructure, maintenance.

Deliberately late. Substrate choices are frequently made first, by whoever set up the repository, and then silently constrain everything above. Making them here means they serve the decisions rather than foreclose them.

The exception: if F47 personalization is set high in Round 11, F41.1 rendering is already decided and the round is a formality. Know which situation you are in.

## D012 · Round 10 — Conduct

F63–F67. Bounded by C001–C003, C039–C042, C066–C070.

## D013 · Round 11 — Time

F46–F49. Requires Rounds 9 and 10 settled, because what a returning visitor sees depends on what state persists.

## D014 · Round 12 — Representation and social

F50–F58.

Last, and this is a real cost. Representation is decided after everything it represents, which means F51 link previews and F54 screenshot legibility are evaluated against a design already fixed. If either matters to acquisition, promote them into Round 7 and accept the rework elsewhere.

## D015 · Rounds are not phases

A round is a set of questions decided together, not a period of time. Rounds 4 and 5 in particular will iterate against each other, because emphasis reveals density problems and density reveals emphasis problems. What the ordering forbids is *finalizing* a later round before an earlier one, not thinking about it.

---

# PART II — LEVERAGE

## D020 · Leverage is impression per unit of effort

Not importance. F44 infrastructure is important and near-invisible; F40 craft is invisible individually and dominant in aggregate. Spend attention where the ratio is highest.

## D021 · High leverage

Set these carefully; they carry disproportionate impression.

**F40 Craft** — the only family coupled to no stylistic choice, therefore the only differentiator available at any aesthetic. Also the one most reliably skipped.
**F15 + F33 Density and space** — felt before anything is read.
**F31 Typography** — the largest single contributor to perceived character.
**F05.1 Pricing disclosure** — the loudest single content decision on most commercial sites.
**F64 Failure handling** — failure surfaces are read as a statement about competence, and they are cheap to design and almost never designed.
**F63 Responsiveness** — bounded by C001; the 100ms window is the difference between an interface that feels alive and one that does not.
**F22 Person** — determines whether anyone appears to be speaking.
**F17 Emphasis** — the difference between a page with a point and a page with contents.

## D022 · Moderate leverage

F02, F12, F13, F18, F32, F36, F39, F57, F58, F65, F66.

## D023 · Low leverage, and worth knowing it

**F37 Iconography** — consumes disproportionate design time for small return. Use an existing set.
**F38 Texture and ornament** — high variance, low expected value.
**F34 Shape** — registers, but the range of readings is narrow.
**F46–F49 Time** — near-zero leverage for a brochure site, high for anything with returning users. See D024.

## D024 · Leverage inverts by site type

The ranking above assumes a commercial site whose visitors mostly arrive once.

**Documentation and reference** — F27 terminology and F12 navigation rise to the top; F36 imagery and F39 motion fall to near zero.
**Application marketing where the app is the product** — F46–F49 time and F47 mutation rise sharply, because the site's job is to predict the product's behavior.
**Anything acquired through sharing** — F50–F54 representation moves from lowest leverage to highest, because most impressions never load the site.
**Editorial** — F31, F18, and F04 dominate; F05 and F65 fall away entirely.

Determine which of these you are before applying D021.

---

# PART III — TRADEOFFS

*Each names what is lost, not merely that a tension exists.*

## D050 · Density ↔ Craft
`F15 ↔ F40`
Every increment of density multiplies the adjacencies requiring optical attention, the states needing design, and the alignment relationships that can go wrong. High density and high craft are both achievable; together they cost superlinearly. Choosing both is choosing to spend the budget there rather than anywhere else.

## D051 · Density ↔ Target size
`F15 ↔ C028`
Packing controls tighter conflicts with the 24×24 floor and the platform conventions at C082. The floor wins. Density above a certain point is therefore not available, and discovering this late means rebuilding the component, not adjusting the padding.

## D052 · Motion ↔ Speed
`F39 ↔ C120`
Two costs, not one. Animation consumes frame budget under C103, and honoring C036 reduced-motion means every motion path needs a static counterpart — doubling the states to design and test, not halving them.

## D053 · Personalization ↔ Rendering
`F47 ↔ F41.1`
Per-visitor content forecloses static rendering, which is the cheapest path to a good LCP. The trade is measurable: choose personalization and accept a worse floor on C120, or choose static and accept that the site cannot know who is looking.

## D054 · Pricing disclosure ↔ Lead capture
`F05.1 ↔ F10.3`
Publishing prices removes a reason to make contact and filters out visitors who would not have bought. Withholding them captures more leads of lower quality and signals, to a meaningful fraction, that the answer is "more than you want to pay." There is no neutral setting; both are loud.

## D055 · Novelty ↔ Comprehension
`F04.1 ↔ C006, C043`
Every departure from convention spends working memory that C006 caps and consistency that C043 requires. The budget is finite and shared. Concentrating novelty in one place is affordable; distributing it across navigation, labeling, and interaction simultaneously is not.

## D056 · Typeface count ↔ Payload
`F31.1 ↔ F42, C104`
Each family and weight is bytes, a request, and a layout shift risk under C104. A variable font collapses the weight axis at the cost of a larger single file. Two families at four weights is a real performance decision disguised as a taste decision.

## D057 · Progressive disclosure ↔ Findability
`F13.3 ↔ F50, F52`
Content behind interaction is content a search engine and a language model may not reach. Deep disclosure improves the experience of a visitor already on the page at the cost of the visitor who never arrives.

## D058 · Navigation breadth ↔ depth
`F11.3 ↔ F11.4`
Bounded on the breadth side by C006. Wider navigation means fewer clicks and more simultaneous options; deeper means fewer choices per screen and more steps. The classic finding is that shallow-and-wide usually beats deep-and-narrow, but C006 places a hard ceiling on how wide.

## D059 · Copy volume ↔ Above-fold load
`F30 ↔ F16.3`
Everything asserted before the fold competes with everything else asserted before the fold. Adding a claim does not add a claim; it divides attention.

## D060 · Proof density ↔ Density
`F57 ↔ F15`
Logos, testimonials, and metrics consume the space that made the page feel confident. Past a threshold, proof reads as protesting.

## D061 · Single-page ↔ Representation
`F11.1 ↔ F50`
One page is one search result, one title, one meta description, and one link preview. Consolidating structure consolidates your entire surface in search to a single entry.

## D062 · Custom controls ↔ Access cost
`F41.3 ↔ C046`
C046 requires name, role, value, and state to be programmatically determinable. A native element supplies this free. A custom one costs a full implementation of the ARIA pattern, keyboard behavior, and focus management — routinely more work than the visual design it enabled.

## D063 · Optimistic UI ↔ Error honesty
`F63.3 ↔ F64.1`
Optimistic updates buy perceived speed against C001 and sell it back when reconciliation fails, because the correction must now undo something the visitor already believes happened. Worth it where failure is rare and reversal is cheap; not where either is untrue.

## D064 · Human presence ↔ Scale signaling
`F58 ↔ F03.4`
Named people, photographs, and bylines make a small operation credible and a large one look small. Whichever you are, the mismatch is the failure — see D103 and D104.

## D065 · Theme options ↔ Every color decision
`F32.5 ↔ F32, F35.3`
A second theme does not add a theme. It doubles every color decision, inverts the elevation model per C022 and F35.3, and doubles the contrast surface to verify. Ship one theme well before shipping two.

## D066 · Docs depth ↔ Terminology
`F06.1 ↔ F27`
Comprehensive documentation written in plain language reads as padded to the practitioners who need it most. Terse documentation in field vocabulary is unusable to everyone else. This is a genuine fork, not a middle to be found; pick the reader.

---

# PART IV — COHERENCE

*A mismatch and the reading it produces. Diagnostic rather than prohibitive — D110 covers the ones worth incurring.*

## D100 · Craft high, failure handling low
`F40 ↑ F64 ↓` → **demo-ware.** Polished on the happy path and abandoned one step off it. The most common incoherence in well-funded products, and the fastest to erode trust, because the visitor concludes the polish was for the pitch.

## D101 · Claim strength high, endorsement provenance low
`F25.1 ↑ F57.4 ↓` → **unbacked.** Absolute assertions beside unattributed testimonials read worse than either alone; the strong claim draws attention to the weak evidence.

## D102 · Pressure high, pricing withheld
`F65 ↑ F05.1 ↓` → **evasive.** Urgency about a price you will not name reads as a trap, whatever the intent.

## D103 · Institutional scale, no authorship
`F03.4 ↑ F58 ↓` → **faceless.** Frequently deliberate and frequently correct for enterprise buyers. Incoherent only when paired with a warm register at F23.

## D104 · Solo scale, formal register
`F03.4 ↓ F23.1 ↑` → **costume.** The corporate "we" from an evidently one-person operation is detected immediately and costs more credibility than it borrows.

## D105 · Dense layout, low craft
`F15 ↑ F40 ↓` → **cluttered.** Density reads as efficiency only when the alignment and spacing are exact. Without craft it reads as an absence of editing. This is D050 expressed as a symptom.

## D106 · Sparse layout, high copy volume
`F15 ↓ F30 ↑` → **endless.** Long copy in a generous layout produces a scroll with no visible end, and the generosity that signaled confidence now signals padding.

## D107 · Motion high, speed poor
`F39.1 ↑ C120 ✗` → **showy and slow.** Animation on a site that fails INP reads as ornament applied instead of engineering rather than in addition to it.

## D108 · Novelty distributed
`F04.1 ↑ across F12.2, F13.1, F39.2` → **unlearnable.** D055 exceeded. Any one of these is a signature; all three simultaneously exhausts the comprehension budget C006 allows.

## D109 · Expert audience, site-driven path
`F02.2 ↑ F13.2 ↓` → **condescending.** A guided linear path shown to people who know what they came for. The correct pairing is expert audience with search-first navigation at F12.1.

## D110 · Mismatches worth incurring

Three of the above are legitimate positions rather than errors.

**D103 faceless** is correct when the buyer is an institution that needs to know you will outlast your founders.
**D102 evasive** is correct — barely — when the price genuinely varies by an order of magnitude across customers, provided F05.1 states that plainly rather than staying silent.
**D106 endless** is correct for editorial long-form, where the scroll is the point and generosity aids sustained reading under C004.

The others are failures in every context I can construct.

## D111 · The general rule

Coherence is agreement across families about the same underlying question. Every test above reduces to one of three questions being answered inconsistently: *how big are we*, *how much do we mean it*, and *how much care went into this*. When a site reads as "off" without a nameable cause, one of those three is being answered two ways.

---

# PART V — DEFAULTS

## D150 · What a default is

The setting that costs least to reverse and fails least badly — not the best setting. Every default below is a placeholder for a decision you have not yet earned the information to make. Departing from one requires a reason; keeping one does not.

## D151 · Purpose and inventory
| Family | Default | Why |
|---|---|---|
| F05.1 Pricing | Public | Reversible in one direction only; withholding later is easy, revealing later is a story |
| F10.1 Account gate | Nothing behind login | Gates are additive; removing one retroactively wastes the work |
| F10.2 Purchase path | Self-serve | Sales-assisted is a hiring decision disguised as a design decision |

## D152 · Structure
| Family | Default | Why |
|---|---|---|
| F11.1 Topology | Flat until page count forces hierarchy | Premature hierarchy is the most common IA error |
| F12.2 Labeling | Literal | Novelty budget is better spent elsewhere per D055 |
| F13.1 Linearity | Open | Guided paths assume an intent you have not verified |
| F14.1 URLs | Readable, stable | Free at the start, expensive forever after |

## D153 · Arrangement and language
| Family | Default | Why |
|---|---|---|
| F15 Density | Comfortable | Compact is a specialization; start general |
| F18.4 Measure | 65ch | Center of the C004 range |
| F22.1 Speaker | We | Neutral; "I" and the company name are both marked choices |
| F29.1 Capitalization | Sentence case | Fewer edge cases than title case, and no house style to maintain |
| F30.2 Verbosity | Terse | Cutting is easier to review than expanding |

## D154 · Surface
| Family | Default | Why |
|---|---|---|
| F31.1 Typeface count | One | Every additional family is D056 |
| F31.4 Base size | 16px | C080 makes it a floor for inputs regardless |
| F32.1 Palette | One hue plus one neutral ramp | Expands cleanly; contracting does not |
| F32.5 Theme | Light only | D065 — earn the second theme |
| F33 Spacing base | 4px, hybrid progression | Dense at the low end where UI needs precision, geometric at the high end where layout needs range |
| F34.1 Radius | One small value | Consistency beats expressiveness at this leverage |
| F35.1 Depth | Bordered, not shadowed | Survives dark mode without an elevation model |
| F39.1 Motion | Minimal | Additive later; removing motion people have learned is disruptive |

## D155 · Substrate and conduct
| Family | Default | Why |
|---|---|---|
| F41.1 Rendering | Static | Cheapest LCP; forecloses least |
| F43.1 Analytics | Privacy-preserving | C066 compliance is near-free at this setting and expensive above it |
| F63.3 Optimism | Confirmed-only | D063 — optimism is earned by knowing your failure rate |
| F65.2 Urgency devices | None | Every one is a withdrawal from credibility |

## D156 · Families with no default

Some choices have no safe placeholder, because any setting is a real assertion.

**F01 Mandate** — cannot be defaulted. This is the definition of Round 1.
**F02 Audience** — a default here is an unexamined assumption that everything downstream inherits.
**F03.1 Positioning claim** — no neutral position exists.
**F40 Craft** — a standard, not a setting. See D203.
**F59–F62 Access** — floors, not defaults. Constraints owns these and there is nothing to choose.

## D157 · Failure states are not defaultable either

F64.2 requires 404, offline, empty, and error surfaces to be designed. The framework's default is not a default; it is an unmade decision that ships. Per D021, this is high-leverage and near-free, which makes shipping the framework default the worst available trade in this document.

---

# PART VI — DEPARTURE AND RECORD

## D200 · When to depart from a default

Three valid reasons, and one invalid one.

**Valid** — a constraint forces it. Evidence from your own users contradicts it. The default is incoherent with a decision already made in an earlier round.
**Invalid** — it looks better in isolation. Almost every default above looks worse than its alternative on a single screen and better across a whole site, which is the entire reason a system exists.

## D201 · Decision record

**Use the Architecture Decision Record convention rather than a parallel format.** ADRs — Michael Nygard's 2011 format, and the MADR variant — are the established way to record a decision with its context and consequences, and they come with tooling and platform support. One file per decision, numbered, immutable once accepted, superseded rather than edited.

The suite adds one required field. ADR's *consequences* section is bidirectional and in practice collects benefits, because benefits are what the author was thinking about. Departures from a default here require a separately headed **accepted cost**, naming the tradeoff being taken on:

```markdown
# 12. Theme: light and dark

Status: accepted
Date: 2026-09-03

## Context
F32.5. Default per D154 is light only.

## Decision
Ship both themes from launch.

## Consequences
Nocturnal primary use; 60% of sessions begin after 20:00.

## Accepted cost
D065 — every color decision doubled, elevation model inverted per
F35.3, contrast surface to verify doubled.
```

The accepted-cost section is the one that gets omitted and the one that matters. It is what makes a decision auditable later rather than merely recorded, and it is why the suite specifies a field rather than adopting ADR unchanged.

## D202 · Re-deciding

A decision is re-opened when its round's inputs change, not on a schedule. Changing F01 re-opens everything. Changing F02 re-opens Rounds 4 through 8. Changing a Round 9 substrate decision re-opens nothing above it, which is precisely why substrate is placed late.

## D203 · Craft is a standard, not a round

F40 is nominally set in Round 7 and actually enforced in every round. It is the only family that cannot be decided once, because it is the level of attention paid to all the other decisions rather than a decision of its own. A team that sets it high in Round 7 and then ships framework-default empty states has not set it at all.

## D204 · When the sixty-seven are still too many

For a first pass, decide eleven: F01, F02, F05.1, F11.1, F15, F17, F22, F31, F32, F40, F64. Take defaults for the rest. This covers every family in D021 and produces a coherent site, because those eleven are where the three coherence questions in D111 get answered.

---

## Settled decisions

**Coupling outranks inheritance.** D001 sets this priority, and D004 is the consequence: naming is pulled from Plane 5 into Round 2 because navigation cannot be finalized without it. The alternative — respecting plane order — means deciding navigation twice, which is worse than violating a layering model that was descriptive rather than binding.

**Access is Round 8, not last and not first.** First is impossible because there is nothing concrete to evaluate. Last is the expensive retrofit. Round 8 places it after surface exists and before substrate hardens, which is the cheapest point at which it can be done properly.

**Defaults are chosen for reversibility, not quality.** Several defaults in Part V are not what I would choose for a specific site. They are what costs least to be wrong about, which is the correct property for a placeholder. D200 exists because the temptation is to read them as recommendations.

**Leverage is stated as a single ranking with an inversion clause.** Publishing separate rankings per site type would be more accurate and would not be used, because the reader must classify their site before reading either way. D024 puts the classification step where it will actually be performed.
