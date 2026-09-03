```yaml
document: Composition
version: 1.0.3
tier: 1
owns:
  - what choices a website presents
  - the range or type of each choice
  - whether choices are independent or coupled
exports: F01–F67 and their segments
depends:
  - Vocabulary ^1
  - Constraints ^1  # 25 citations, all resolved
reviewed: 2026-09-03
```

# Composition

The choices a website presents. Every entry is something that gets set, whether or not anyone sets it deliberately.

---

## What this document owns

Three things: what the choices are, what range or type each has, and which choices are not independent of each other.

## What it does not own

| Question | Owner |
|---|---|
| What does this term mean? | Vocabulary |
| What is this thing made of, in parameters? | Anatomy |
| What may this choice not go below? | Constraints |
| How much does this choice matter, and in what order do I set them? | Decision |
| How does this become a token, component, or line of code? | Implementation |
| How do I confirm it was realized? | Verification |

If a sentence in this document answers a question in that table, it is in the wrong place.

---

## Notation

**Ranges** are written `low ←→ high`. Neither end is a recommendation; that judgment belongs to Decision. Where a range begins at absence, absence is a setting like any other — usually the loudest one.

**Coupling** records whether two families can be set independently.
*Tight* — they cannot. Changing one changes the other.
*Moderate* — they constrain each other without determining each other.
Absence of a coupling line means the family is independent.

**Bounded by** marks a range with a floor or ceiling that this document does not define. Constraints owns those values; only the citation appears here. A range with no *bounded by* line is unbounded in both directions.

**Structure.** Planes stack; each inherits from the ones below. Cross-cuts touch every plane and cannot be sequenced.

---

# PART I — PLANES

---

## Plane 1 — Purpose

### F01 · Mandate
**F01.1** Purpose singularity — one job ←→ many jobs
**F01.2** Primary conversion — a single most-wanted action ←→ none named
**F01.3** Success definition — conversion / comprehension / credibility / recruitment / retention
**F01.4** Time horizon — campaign ←→ permanent

### F02 · Audience
**F02.1** Breadth — one named segment ←→ anyone who arrives
**F02.2** Assumed expertise — explains from zero ←→ assumes the field
**F02.3** Assumed intent — arrives knowing ←→ arrives to find out
**F02.4** Address term — what the visitor is called
*Coupling* — tight with F22, F27. Audience is expressed almost entirely through language.

### F03 · Position
**F03.1** Positioning claim — new category / better alternative / cheaper / specialist / only option
**F03.2** Competitive posture — never mention rivals ←→ name and compare
**F03.3** Editorial stance — takes positions ←→ neutral
**F03.4** Scale signaling — reads as one person ←→ reads as an institution
*Coupling* — moderate with F25, F57.

### F04 · Risk posture
**F04.1** Convention appetite — meets expectations ←→ deliberately unfamiliar
**F04.2** Business model legibility — obvious ←→ concealed
**F04.3** Disclosure willingness — open ←→ withholding
*Coupling* — moderate with F31, F34, F39. Risk appetite surfaces in every stylistic decision.

---

## Plane 2 — Inventory

*What the site consists of. Each family is a depth range beginning at absence: no pricing page, a page saying "contact us," and a full public price list are three settings of one dial, not a checkbox.*

### F05 · Commercial surfaces
**F05.1** Pricing — absent ←→ "contact us" ←→ full public list
**F05.2** Plan comparison — none ←→ complete feature matrix
**F05.3** Case studies — none ←→ detailed and numerous
**F05.4** Customer logos — none ←→ prominent wall
**F05.5** Product access — none ←→ stills ←→ video ←→ demo ←→ trial ←→ open sandbox
**F05.6** Estimator or calculator — absent ←→ present
*Coupling* — moderate with F10, F57.

### F06 · Knowledge surfaces
**F06.1** Documentation — absent ←→ comprehensive reference
**F06.2** API reference — absent ←→ complete
**F06.3** Writing or blog — absent ←→ substantial body
**F06.4** Changelog — absent ←→ detailed and current
**F06.5** Roadmap — absent ←→ public and specific
**F06.6** Glossary — absent ←→ complete
**F06.7** Tutorials and examples — absent ←→ extensive
*Coupling* — moderate with F48.

### F07 · Institutional surfaces
**F07.1** About — absent ←→ substantive account
**F07.2** Team — absent ←→ named with photographs
**F07.3** Careers — absent ←→ full listings
**F07.4** Press kit — absent ←→ complete
**F07.5** Legal and terms — absent ←→ complete and readable
**F07.6** Privacy policy — absent ←→ specific and plain
**F07.7** Security — absent ←→ documented practice
**F07.8** Status — absent ←→ live with incident history
**F07.9** Accessibility statement — absent ←→ published including known gaps
*Coupling* — tight with F58 at F07.2. Moderate with F62 at F07.9.

### F08 · Contact surfaces
**F08.1** Contact — absent ←→ direct and human
<!-- vale Suite.RefusedTerms = NO --><!-- "responsive" here is support answering requests, not the layout term V-611 disambiguates; kept as the dial's short endpoint label, consistent with the rest of F08 -->
**F08.2** Support — absent ←→ staffed and responsive
<!-- vale Suite.RefusedTerms = YES -->
**F08.3** Community — absent ←→ active and linked
**F08.4** Newsletter — absent ←→ prominent
**F08.5** Social presence — absent ←→ many channels
**F08.6** Booking — absent ←→ direct calendar
*Coupling* — moderate with F67.

### F09 · Machine surfaces
**F09.1** Sitemap — absent ←→ complete and current
**F09.2** Robots directives — absent ←→ deliberate
**F09.3** Feeds — absent ←→ full-content
**F09.4** Structured data — absent ←→ comprehensive
**F09.5** Open Graph tags — absent ←→ per-page and designed
**F09.6** `llms.txt` — absent ←→ maintained
**F09.7** Canonical tags — absent ←→ disciplined
*Coupling* — tight with F50–F52. These exist to serve Representation.

### F10 · Gating
**F10.1** Account gate depth — nothing behind login ←→ almost everything
**F10.2** Purchase path — self-serve ←→ sales-assisted only
**F10.3** Data asked before value delivered — none ←→ extensive
**F10.4** Identity requirement — anonymous browsing permitted ←→ identification required
*Coupling* — moderate with F05, F65.
*Bounded by* — C042, C070.

---

## Plane 3 — Structure

### F11 · Topology
**F11.1** Site shape — single page / flat / hierarchical / hub-and-spoke / faceted
**F11.2** Page count — few long ←→ many short
**F11.3** Navigation breadth — top-level choice count
**F11.4** Navigation depth — clicks to the deepest item
*Coupling* — tight with F13. Moderate with F18.

### F12 · Navigation
**F12.1** Model — persistent global / contextual / progressive / search-first
**F12.2** Labeling scheme — literal / topical / task-based / audience-based / metaphorical
**F12.3** Wayfinding cues — breadcrumbs, current-state, section identity
**F12.4** Cross-linking density — dead ends ←→ heavily interlinked
*Coupling* — tight with F26. Labels are copy.
*Bounded by* — C006, C043, C044.

### F13 · Path
**F13.1** Linearity — one guided route ←→ open exploration
**F13.2** Locus of control — the site drives ←→ the visitor drives
**F13.3** Progressive disclosure depth — everything visible ←→ layered behind clicks
**F13.4** Entry assumption — homepage-first ←→ every page is page one
*Coupling* — tight with F11. Moderate with F17.

### F14 · Addressing
**F14.1** URL legibility — readable and stable ←→ opaque and generated
**F14.2** Canonical discipline — one address per thing ←→ duplicates tolerated
**F14.3** Durability — links rot ←→ permalinks maintained
**F14.4** Content model granularity — hand-built pages ←→ structured records
*Coupling* — tight with F49.

---

## Plane 4 — Arrangement

### F15 · Density
**F15.1** Information density — sparse ←→ packed
**F15.2** Content-to-chrome ratio — chrome-dominant ←→ content-dominant
**F15.3** Whitespace allocation — where the space is spent
*Coupling* — tight with F16 and F33. These three are near-inseparable: they measure amount-per-space, amount-per-scroll, and the underlying spacing scale. Moderate with F30, since density is partly a copy decision.
*Bounded by* — C004, C027, C028.

### F16 · Pacing
**F16.1** Scroll distance per idea — dense ←→ spacious
**F16.2** Section count per page
**F16.3** Above-fold load — how much is asserted before any scroll
*Coupling* — tight with F15.

### F17 · Emphasis
**F17.1** Hierarchy steepness — one dominant focus ←→ many co-equal peers
**F17.2** CTA count — per page and per screen
**F17.3** CTA placement — top only / repeated / terminal only
**F17.4** Repetition — how often the core claim recurs
**F17.5** Persistence on scroll — what stays fixed
*Coupling* — tight with F31, F32. Hierarchy is expressed through type and color. Moderate with F28, F54.

### F18 · Composition
**F18.1** Template count — distinct page layouts
**F18.2** Grid system — columns, gutter, or none
**F18.3** Reading path — single column ←→ multi-column ←→ non-linear
**F18.4** Measure — line length of body text
**F18.5** Alignment discipline — how many alignment edges exist
**F18.6** Section uniformity — identical rhythm ←→ every section different
*Coupling* — tight with F15.
*Bounded by* — C004, C038.

### F19 · Media balance
**F19.1** Image-to-text ratio
**F19.2** Media placement — inline / aside / full-bleed / background
**F19.3** Data presentation mode — prose / list / table / chart / interactive
*Coupling* — tight with F36.

### F20 · Adaptation
**F20.1** Adaptation strategy — reflow / rearrange / remove content
**F20.2** Breakpoint count
**F20.3** Sizing basis — viewport ←→ container
**F20.4** Input priority — touch-first / pointer-first / keyboard-first
*Coupling* — tight with F18. Moderate with F60.
*Bounded by* — C025, C026, C028, C082.

### F21 · Form design
**F21.1** Field count
**F21.2** Step count — single ←→ multi-step
**F21.3** Grouping — flat ←→ fieldset-organized
**F21.4** Validation timing — submit / blur / change / hybrid
**F21.5** Required-field strategy — mark required ←→ mark optional
*Coupling* — moderate with F10, F63.
*Bounded by* — C039, C040, C041, C042, C086.

---

## Plane 5 — Language

### F22 · Person
**F22.1** Speaker — we / I / the company name / nobody
**F22.2** Addressee — you / users / customers / unaddressed
**F22.3** Voice — active ←→ passive
**F22.4** Visibility — a person is evidently speaking ←→ no one is
*Coupling* — tight with F02. Moderate with F58.

### F23 · Register
**F23.1** Formality — legal-grade ←→ conversational
**F23.2** Contractions — never ←→ throughout
**F23.3** Humor — none ←→ central
**F23.4** Idiom — plain ←→ colloquial
*Coupling* — moderate with F04.

### F24 · Sentence
**F24.1** Length — short ←→ long
**F24.2** Variance — uniform ←→ highly varied
**F24.3** Verb density — nominalized ←→ verb-driven
**F24.4** Paragraph length
**F24.5** Reading level

### F25 · Claim structure
**F25.1** Assertion strength — hedged ←→ absolute
**F25.2** Quantification — vague ←→ numbered
**F25.3** Attribution — unsourced ←→ cited
**F25.4** Promise vs. description — what is guaranteed ←→ what is merely described
*Coupling* — moderate with F03, F57.

### F26 · Naming
**F26.1** Product name — literal ←→ invented
**F26.2** Feature names — descriptive ←→ branded
**F26.3** Tier names — numbered / sized / named
**F26.4** Navigation labels — conventional ←→ proprietary
*Coupling* — tight with F12. Moderate with F27.

### F27 · Terminology load
**F27.1** Jargon density — plain ←→ field-specific
**F27.2** Definition on first use — always ←→ never
**F27.3** Acronym policy — expanded ←→ assumed
*Coupling* — tight with F02.

### F28 · Headline strategy
**F28.1** Type — benefit / feature / provocation / plain description / question
**F28.2** Length
**F28.3** Load-bearing — headlines carry the argument alone ←→ body carries it
*Coupling* — moderate with F17.

### F29 · Mechanics
**F29.1** Capitalization convention — sentence / title / mixed
**F29.2** Number formatting
**F29.3** Date formatting
**F29.4** Punctuation policy — serial comma, dash usage, quotation style
**F29.5** Abbreviation style
*Bounded by* — C045.

### F30 · Copy volume
**F30.1** Words per screen
**F30.2** Verbosity per point — terse ←→ expansive
**F30.3** Label length — abbreviated ←→ full phrase
**F30.4** Redundancy — said once ←→ restated
*Coupling* — tight with F15.

---

## Plane 6 — Surface

### F31 · Typography
**F31.1** Typeface count — one ←→ several
**F31.2** Pairing relationship — contrasting ←→ harmonious ←→ none
**F31.3** Classification — serif / sans / mono / display, and what it borrows from
**F31.4** Base text size
**F31.5** Scale range — narrow ←→ wide gap between smallest and largest
**F31.6** Weight range — how many weights, how far apart
**F31.7** Case convention — where uppercase is used
*Coupling* — tight with F17. Moderate with F15.
*Bounded by* — C020, C025, C080, C084, C085.

### F32 · Color
**F32.1** Palette size — hue count in play
**F32.2** Chroma level — muted ←→ saturated
**F32.3** Neutral character — pure gray ←→ strongly tinted
**F32.4** Contrast level — soft ←→ stark
**F32.5** Theme options — light / dark / auto / high-contrast
**F32.6** Semantic assignments — which hues carry which meanings
*Coupling* — tight with F17, F35, F59.
*Bounded by* — C011, C012, C020, C022, C023.

### F33 · Space
**F33.1** Generosity — tight ←→ expansive
**F33.2** Rhythm — irregular ←→ strict
**F33.3** Scale progression — linear / geometric / hybrid
*Coupling* — tight with F15.

### F34 · Shape
**F34.1** Corner radius — sharp ←→ pill
**F34.2** Geometry — rectilinear ←→ organic
**F34.3** Border weight — hairline ←→ heavy
**F34.4** Cross-scale consistency — nested radii concentric or not
*Coupling* — moderate with F04, F35.

### F35 · Depth
**F35.1** Model — flat / bordered / shadowed / layered / glass / physical
**F35.2** Separation method — space / rule / border / surface change
**F35.3** Elevation cue — shadow-carried ←→ lightness-carried
*Coupling* — tight with F32. The elevation cue must invert by theme.
*Bounded by* — C022, C100.

### F36 · Imagery
**F36.1** Approach — photography / illustration / abstract / diagram / screenshot / none
**F36.2** Treatment — crop, filter, framing
**F36.3** Human depiction — real / stock / avatar / illustrated / absent
**F36.4** Set consistency — uniform ←→ heterogeneous
*Coupling* — tight with F19. Moderate with F58, F51.
*Bounded by* — C024, C101, C105.

### F37 · Iconography
**F37.1** Set — one family ←→ mixed sources
**F37.2** Style — stroke / filled / duotone
**F37.3** Stroke weight
**F37.4** Density of use — sparing ←→ every label
**F37.5** Optical sizing — one drawing scaled ←→ redrawn per size
*Coupling* — moderate with F34.
*Bounded by* — C022, C023, C024.

### F38 · Texture and ornament
**F38.1** Noise or grain — absent ←→ pronounced
**F38.2** Pattern use
**F38.3** Decoration level — nothing decorative ←→ heavily decorated
**F38.4** Borrowed material — what physical reference, if any
**F38.5** Ambient audio — absent ←→ present
*Coupling* — moderate with F04.

### F39 · Motion
**F39.1** Quantity — still ←→ constantly moving
**F39.2** Character — sharp / smooth / springy / mechanical
**F39.3** Transition treatment — hard cuts ←→ animated navigation
**F39.4** Loading treatment — blank / spinner / skeleton / progressive
**F39.5** Pointer feedback — system default ←→ custom cursor and hover response
*Coupling* — moderate with F04, F63.
*Bounded by* — C009, C034, C035, C036, C102, C103.

### F40 · Craft
**F40.1** Optical corrections — none ←→ systematic
**F40.2** Detail resolution — coarse ←→ fine
**F40.3** State completeness — default states only ←→ every state designed
**F40.4** Cross-surface consistency — finish varies by page ←→ uniform throughout
*Coupling* — moderate with F64, which shares the question of whether the unglamorous states were designed at all. Independent of every stylistic family: changing typeface, palette, or shape language does not change the level of finish. This is why craft is the one differentiator available at any aesthetic. Craft is not equally cheap at all settings — high density and high craft compound in cost — but cost is not coupling, and that tradeoff belongs to Decision.

---

## Plane 7 — Substrate

### F41 · Rendering
**F41.1** Model — static / server-rendered / client-rendered / hybrid
**F41.2** Platform — hand-built / framework / CMS / site builder
**F41.3** JavaScript dependence — works without ←→ requires it
*Coupling* — moderate with F61.
*Bounded by* — C030, C046.

### F42 · Payload
**F42.1** Total page weight budget
**F42.2** JavaScript budget
**F42.3** Font count and loading strategy
**F42.4** Image formats and delivery
**F42.5** Third-party script count
*Coupling* — tight with F31.3, F36. Type and imagery choices set most of the payload.
*Bounded by* — C104, C120, C121, C122, C123, C124.

### F43 · Instrumentation
**F43.1** Analytics posture — none / privacy-preserving / full
**F43.2** Consent mechanism — absent / banner / granular / native
**F43.3** Cookie usage
**F43.4** Tracking visibility — disclosed ←→ silent
*Coupling* — moderate with F65, F66.
*Bounded by* — C066, C067, C068.

### F44 · Infrastructure
**F44.1** Hosting and CDN
**F44.2** Domain structure — apex, subdomains, what lives where
**F44.3** Security posture — headers, transport, disclosed practice
**F44.4** Uptime visibility — status page, incident history

### F45 · Maintenance
**F45.1** Build cadence — how often it changes
**F45.2** Dependency posture — pinned ←→ current
**F45.3** Content update mechanism — who can change what, without whom

---

# PART II — CROSS-CUTS

---

## Cross-cut A — Time

*Part I describes a snapshot. These families describe a website as something that happens repeatedly.*

### F46 · Recurrence
**F46.1** First-visit vs. return treatment — identical ←→ divergent
**F46.2** Memory between sessions — none ←→ full state
**F46.3** Re-entry point — always the homepage ←→ where they left off
*Coupling* — moderate with F13.

### F47 · Mutation
**F47.1** Change with use — static ←→ accrues
**F47.2** Personalization accrual — none ←→ heavy
**F47.3** Volume tolerance — what the interface looks like at 0, 1, 7, and 10,000 items
*Coupling* — tight with F46.

### F48 · Cadence
**F48.1** Publish rate
**F48.2** Seasonal or campaign variation — none ←→ frequent
**F48.3** Maintenance visibility — evidently tended ←→ evidently abandoned
**F48.4** Dating — content dated ←→ undated
*Coupling* — moderate with F06.

### F49 · Accretion
**F49.1** Archive policy — grows ←→ pruned
**F49.2** Versioning — none ←→ full history
**F49.3** Correction policy — old content corrected / removed / left standing
**F49.4** Link durability over years
*Coupling* — tight with F14.

---

## Cross-cut B — Representation

*How the site appears where it isn't. For many sites this is where most impressions occur and the site never renders at all.*

### F50 · Search appearance
**F50.1** Title construction
**F50.2** Meta description — written ←→ auto-generated
**F50.3** Rich result eligibility
**F50.4** Sitelink structure
*Coupling* — tight with F09.

### F51 · Link preview
**F51.1** Preview image — designed ←→ default ←→ absent
**F51.2** Card title and description
**F51.3** Embed behavior in messaging and documents
*Coupling* — tight with F09. Moderate with F36.

### F52 · Machine summary
**F52.1** Structured data coverage
**F52.2** `llms.txt` presence and content
**F52.3** Framing durability — whether your positioning survives summarization
*Coupling* — tight with F09. Moderate with F25.

### F53 · Third-party listing
**F53.1** Directory presence
**F53.2** App store or marketplace listing
**F53.3** Review site presence
**F53.4** Comparison page handling — ignored ←→ actively supplied
*Coupling* — moderate with F57.

### F54 · Secondhand appearance
**F54.1** Screenshot legibility — how a cropped view reads
**F54.2** Quotability — whether copy survives extraction
**F54.3** Scaled appearance — how it reads at thumbnail size
*Coupling* — moderate with F17. A page built around a full-viewport hero screenshots badly.

---

## Cross-cut C — Social presence

*Whether other people are evident on the page.*

### F55 · Other visitors
**F55.1** Activity traces — none ←→ live
**F55.2** Counts — hidden ←→ displayed
**F55.3** Recency signals
**F55.4** Inhabitation — reads as empty ←→ reads as busy

### F56 · User contribution
**F56.1** Contribution channel — none / comments / reviews / full UGC
**F56.2** Moderation posture — open ←→ curated
**F56.3** Attribution — anonymous ←→ identified
*Coupling* — tight with F47.3. User content breaks volume assumptions faster than anything else.

### F57 · Endorsement
**F57.1** Testimonial presence and specificity
**F57.2** Logo wall — absent ←→ prominent
**F57.3** Ratings — hidden ←→ displayed
**F57.4** Provenance — unattributed ←→ fully sourced
*Coupling* — moderate with F03, F25.

### F58 · Authorship
**F58.1** Named people — none ←→ throughout
**F58.2** Bylines on content
**F58.3** Photographs of actual people
**F58.4** Evidence of human making — absent ←→ foregrounded
**F58.5** Making disclosure — origin concealed ←→ colophon, credits, and tooling named
*Coupling* — tight with F22. Moderate with F36, F41.2.

---

## Cross-cut D — Access

### F59 · Sensory independence
**F59.1** Contrast level across all pairings
**F59.2** Color independence — meaning carried by color alone ←→ never
**F59.3** Text alternatives — absent ←→ complete
**F59.4** Captions and transcripts
*Coupling* — tight with F32.
*Bounded by* — C020, C021, C022, C023, C024.

### F60 · Input independence
**F60.1** Hover dependence — hover-only paths exist ←→ none
**F60.2** Keyboard operability — partial ←→ complete
**F60.3** Focus order — arbitrary ←→ follows visual order
**F60.4** Target size
*Coupling* — moderate with F20.
*Bounded by* — C028, C029, C030, C031, C032, C033, C038, C082.

### F61 · Tolerance
**F61.1** Reduced motion — ignored ←→ first-class path
**F61.2** Forced colors and high contrast
**F61.3** Zoom — breaks ←→ usable at high magnification
**F61.4** Degraded network and no-JavaScript behavior
*Coupling* — moderate with F39, F41.
*Bounded by* — C025, C026, C027, C036.

### F62 · Conformance declaration
**F62.1** Stated level — none ←→ published
**F62.2** Gap acknowledgment — silent ←→ documented
**F62.3** Feedback channel for barriers
*Coupling* — moderate with F07.9.
*Bounded by* — C060, C061, C062, C063, C064, C065.

---

## Cross-cut E — Conduct

### F63 · Responsiveness
**F63.1** Acknowledgment latency
**F63.2** Feedback fidelity — silent ←→ every action confirmed
**F63.3** Optimism — confirmed-only ←→ optimistic updates
**F63.4** Feedback channels — visual only ←→ visual, audible, and haptic
*Coupling* — moderate with F39.
*Bounded by* — C001, C002, C003, C008.

### F64 · Failure handling
**F64.1** Error message quality — cause, consequence, and next action stated or not
**F64.2** Failure surfaces designed — 404, offline, empty, maintenance
**F64.3** Empty state treatment — blank ←→ instructive
**F64.4** Forgiveness — undo, drafts, autosave, confirmation
*Coupling* — moderate with F21.

### F65 · Pressure
**F65.1** Commercial intensity — soft ←→ insistent
**F65.2** Urgency and scarcity devices — absent ←→ heavy
**F65.3** Defaults and preselection — neutral ←→ self-serving
**F65.4** Choice architecture — how many options, how framed, what is recommended
*Coupling* — moderate with F10, F43.
*Bounded by* — C006, C066, C070.

### F66 · Exit
**F66.1** Unsubscribe friction
**F66.2** Data portability — none ←→ full export
**F66.3** Account deletion path
**F66.4** Cancellation path — self-serve ←→ requires contact
*Coupling* — tight with F65.
*Bounded by* — C067, C069.

### F67 · Aftercare
**F67.1** Support model — docs / ticket / chat / bot / human
**F67.2** Post-conversion craft — receipts, confirmations, onboarding
**F67.3** Notification frequency
**F67.4** Cross-surface continuity — with app, email, docs, invoices
*Coupling* — moderate with F45.
*Bounded by* — C081.

---

# PART III — EXPORT INDEX

*The public surface. These IDs and meanings are stable; all prose above is internal and may change without a version bump.*

| ID | Name | Meaning |
|---|---|---|
| F01 | Mandate | What the site exists to accomplish |
| F02 | Audience | Who it is addressed to and what it assumes of them |
| F03 | Position | How it locates itself against alternatives |
| F04 | Risk posture | Willingness to depart from convention and to disclose |
| F05 | Commercial surfaces | Depth of sales-facing material |
| F06 | Knowledge surfaces | Depth of explanatory and reference material |
| F07 | Institutional surfaces | Depth of organizational and legal material |
| F08 | Contact surfaces | Reachability, and through what channels |
| F09 | Machine surfaces | Completeness of non-human-facing artifacts |
| F10 | Gating | What requires an account, a conversation, or personal data |
| F11 | Topology | Overall shape and size of the site |
| F12 | Navigation | How movement between parts is offered |
| F13 | Path | Who directs the visit and how openly |
| F14 | Addressing | How things are named, located, and kept locatable |
| F15 | Density | How much is present per unit of space |
| F16 | Pacing | How much is present per unit of scroll |
| F17 | Emphasis | How importance is ranked and asserted |
| F18 | Composition | How a page is laid out |
| F19 | Media balance | Proportion and placement of non-text content |
| F20 | Adaptation | How layout responds to context and input |
| F21 | Form design | How input is requested |
| F22 | Person | Who speaks and who is addressed |
| F23 | Register | Formality and tonal range of the writing |
| F24 | Sentence | Construction of the prose itself |
| F25 | Claim structure | How assertions are made and supported |
| F26 | Naming | What things are called |
| F27 | Terminology load | Specialist vocabulary and its handling |
| F28 | Headline strategy | What headlines do and how much they carry |
| F29 | Mechanics | Orthographic and formatting conventions |
| F30 | Copy volume | Quantity of words |
| F31 | Typography | Typeface selection and typographic scale |
| F32 | Color | Palette construction and assignment |
| F33 | Space | Spacing scale and its application |
| F34 | Shape | Geometry of edges and corners |
| F35 | Depth | How layering and elevation are expressed |
| F36 | Imagery | Kind and treatment of pictures |
| F37 | Iconography | Icon system and its use |
| F38 | Texture and ornament | Non-structural surface treatment |
| F39 | Motion | Quantity and character of movement |
| F40 | Craft | Level of finish, and how uniformly it is applied |
| F41 | Rendering | How pages are produced and delivered |
| F42 | Payload | What is shipped over the wire |
| F43 | Instrumentation | What is measured and how consent is handled |
| F44 | Infrastructure | Where it runs and how it is secured |
| F45 | Maintenance | How and how often it changes |
| F46 | Recurrence | Treatment of repeat visits |
| F47 | Mutation | How the site changes through use |
| F48 | Cadence | Rate and visibility of ongoing activity |
| F49 | Accretion | What survives over years |
| F50 | Search appearance | How it renders in search results |
| F51 | Link preview | How it renders when shared |
| F52 | Machine summary | How it renders when summarized by software |
| F53 | Third-party listing | How it appears in others' catalogs |
| F54 | Secondhand appearance | How it survives being excerpted or screenshotted |
| F55 | Other visitors | Evidence that others are present |
| F56 | User contribution | Whether visitors can add anything |
| F57 | Endorsement | Third-party validation and its provenance |
| F58 | Authorship | Evidence of the humans behind it |
| F59 | Sensory independence | Whether meaning survives loss of a sense |
| F60 | Input independence | Whether operation survives a change of input method |
| F61 | Tolerance | Behavior under user preferences and degraded conditions |
| F62 | Conformance declaration | What is claimed about accessibility |
| F63 | Responsiveness | Speed and fidelity of feedback to input |
| F64 | Failure handling | Behavior when something goes wrong or is absent |
| F65 | Pressure | Intensity and honesty of the commercial ask |
| F66 | Exit | Difficulty of leaving |
| F67 | Aftercare | Treatment after the primary action |

---

## Settled decisions

Recorded so they are not relitigated.

**Inventory is not a separate type.** What looked like a presence/absence checklist was a range written badly. No pricing page, a page saying "contact us," and a full public price list are three settings of one dial. Every Plane 2 family is now a depth range beginning at absence, which is both more accurate and removes the type mismatch without splitting the document. Consequence: pricing disclosure moved from F10 to F05.1, and product access from F10 to F05.5, since both are questions of how deep a commercial surface goes rather than what is gated.

**Provenance is an outcome, with one dial hiding inside it.** Whether a site reads as templated, bespoke, individually authored, or machine-generated is fully determined by the other families — two sites with identical settings across all 67 cannot differ on it. What produces the reading is F41.2 platform and F04.1 convention appetite, both already present. But one genuine choice was concealed in the question: whether you *disclose* your origin, through a colophon, credits, or naming your tooling. That is now F58.5.

**Craft is independent of style but not of state.** The claim that F40 couples to nothing was too strong in one direction and correct in the other. Correct: no stylistic family constrains it. Changing typeface, palette, or shape language does not change your level of finish, which is what makes craft available at any aesthetic. Too strong: F40.3 state completeness and F64.2 failure surfaces are asking a version of the same question, so that coupling is now recorded as moderate. Separately, cursor and sound were removed from F40 — they were a junk drawer, not finish. Pointer feedback is now F39.5, interface sound is F63.4, and ambient audio is F38.5.

**F20.1 was renamed off "Responsive," not exempted.** The segment carried a Vale exemption claiming "Responsive strategy" named the same distinction Vocabulary V-611 disambiguates. It didn't: V-611 (via V-081/V-082) draws a strictly two-way line — layout scaling continuously versus layout switching between a fixed number of discrete arrangements. F20.1's dial has three values — reflow, rearrange, remove content — and "remove content" is a content-depth strategy, not a form of either responsive or adaptive layout scaling; it has no home in V-611 at all. An exemption citing V-611 as covering all three values was inaccurate, and widening V-611 itself to cover "remove content" would have papered over a real difference between a layout-scaling axis and a content-inclusion axis to save a name. The segment is now **Adaptation strategy**, matching the family name (F20 · Adaptation) instead of a narrower technical term two-thirds of its range doesn't fit. Per `suite-architecture.md` §3, the rename is free — `F20.1` did not move and nothing that cites it by ID needed to change — and it also removes the Vale exemption entirely, since the word "Responsive" no longer appears there to need one. The reflow/rearrange distinction inside the dial still corresponds to V-081/V-082 and V-611 remains the correct citation for anyone who needs *that* pair disambiguated; this document just no longer asserts it covers the whole segment.
