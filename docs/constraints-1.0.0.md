```yaml
document: Constraints
version: 1.0.1
tier: 0
owns:
  - what is not negotiable
  - why it binds
  - how fast it changes
exports: C001–C124
depends: []
reviewed: 2026-09-03
```

# Constraints

What bounds a website's choices, and why. This document cites nothing. It must be readable and true on its own.

---

## What this document owns

Three things: what may not be done, the reason it may not, and how volatile that reason is.

## What it does not own

| Question | Owner |
|---|---|
| What does this term mean? | Vocabulary |
| What is this thing made of, in parameters? | Anatomy |
| What choices exist within these bounds? | Composition |
| Which bound should I aim past, and by how much? | Decision |
| How do I enforce this in code? | Implementation |
| How do I confirm I'm inside it? | Verification |

A constraint states a floor or a prohibition. It never states a target. "4.5:1 minimum" belongs here; "we aim for 7:1 because our audience skews older" belongs to Decision.

---

## Notation

**Kind** — why it binds. This determines whether it can ever change.

*Perceptual* — a property of human beings. Does not change.
*Standard* — a published specification. Changes on a revision cycle.
*Legal* — a statute, rule, or judicial interpretation. Changes constantly and varies by jurisdiction.
*Platform* — a client, OS, or device behavior. Changes on release cycles.
*Physical* — a property of the medium or hardware.
*Elective* — not binding until adopted, fully binding afterward.

**Volatility** — how often the entry needs rechecking.

*Invariant* · *Slow* (annual) · *Volatile* (quarterly) · *Release-tied* · *Local* (set once, then held)

**Scope** — where it applies, when that is not everywhere.

---

## A note on the legal section

Part C is a map of where obligations sit, not legal advice, and I am not a lawyer. Every entry names its source and date so it can be checked. Jurisdiction, sector, and company size all change what applies. Treat Part C as a prompt to ask counsel a specific question, never as an answer.

---

# PART A — PERCEPTUAL

*Kind: perceptual. Volatility: invariant. These bind because of how people work, and no revision cycle will move them.*

**C001 · Acknowledgment window**
Input must produce visible acknowledgment within approximately 100ms or the system is perceived as unresponsive. Acknowledgment is a separate obligation from completion.

**C002 · Flow threshold**
Around 1 second, delay becomes consciously noticeable and the sense of direct operation breaks, though attention is retained.

**C003 · Attention threshold**
Around 10 seconds, attention departs the task. Progress indication is required well before this — from roughly 1 second — and indeterminate indicators past 4–5 seconds are read as failure regardless of what is happening.

**C004 · Measure for sustained reading**
Line lengths outside roughly 45–75 characters degrade sustained reading. Below the floor, the eye returns too often; above the ceiling, line re-entry errors rise. Approximately 66 characters is the long-standing single-column optimum.

**C005 · Reading rate**
Adult silent reading in a first language runs roughly 200–250 words per minute for ordinary prose, lower for technical material. Any claim about how long a page takes to read is bounded by this.

**C006 · Working memory limit**
People hold approximately four chunks in working memory simultaneously. Any choice set, navigation breadth, or multi-step process exceeding this requires external structure to remain usable.

**C007 · Foveal acuity**
Sharp vision covers roughly two degrees of the visual field. Anything requiring detail must be looked at directly. Peripheral signaling must use motion, high contrast, or size — never fine detail.

**C008 · Change blindness**
Changes made outside the current fixation, without motion, are frequently not perceived at all. A silent state change is often no change from the user's position.

**C009 · Vestibular sensitivity**
Large-field motion, parallax, and rapid zoom can induce nausea, dizziness, and migraine in susceptible people. This is a physiological response, not a preference.

**C010 · Photosensitivity**
Flashing can induce seizures. The threshold is codified at C034; the underlying constraint is physiological and absolute.

**C011 · Color vision deficiency**
Roughly 8% of males and 0.5% of females of Northern European descent have a red-green deficiency. Any distinction carried by red versus green alone is invisible to a substantial fraction of any general audience.

**C012 · Contrast is a luminance relationship**
Contrast cannot be evaluated for a foreground color alone. It requires both surfaces to be known, which means text over gradients, images, video, or translucency has no single contrast value and must be evaluated against its worst case.

---

# PART B — STANDARDS

*Kind: standard. Volatility: slow. Baseline: WCAG 2.2 Level AA, the current W3C Recommendation as of October 2023. WCAG 2.2 supersets 2.1, so conforming to 2.2 AA satisfies every regime in Part C that requires 2.1 AA. WCAG 3.0 remains a Working Draft with no compliance force; W3C Recommendation is not anticipated before 2028.*

## Contrast

<!-- vale Suite.RefusedTerms = NO --><!-- "bold" here is the CSS font-weight keyword in a size threshold, not the refused claim-strength adjective -->
**C020 · Text contrast minimum** — WCAG 1.4.3, AA
4.5:1 for body text. 3:1 for large text, defined as 24px and above, or 18.66px and above when bold.
<!-- vale Suite.RefusedTerms = YES -->

**C021 · Text contrast enhanced** — WCAG 1.4.6, AAA
7:1 for body text, 4.5:1 for large text.

**C022 · Non-text contrast** — WCAG 1.4.11, AA
3:1 for user interface components and the parts of graphics required to understand them. This covers borders of inputs, icon buttons, focus indicators, and chart elements carrying meaning.

**C023 · Color is not sufficient alone** — WCAG 1.4.1, A
Color may not be the only visual means of conveying information, indicating an action, prompting a response, or distinguishing an element.

## Text and reflow

**C024 · Text alternatives** — WCAG 1.1.1, A
All non-text content has a text alternative serving the equivalent purpose. Decorative content is marked so it is skipped.

**C025 · Resize text** — WCAG 1.4.4, AA
Text resizes to 200% without loss of content or functionality.

**C026 · Reflow** — WCAG 1.4.10, AA
Content reflows to a 320 CSS pixel equivalent width without two-dimensional scrolling. This is what 400% zoom on a 1280px viewport produces.

**C027 · Text spacing tolerance** — WCAG 1.4.12, AA
No loss of content or function when the user overrides to line-height 1.5×, paragraph spacing 2×, letter-spacing 0.12×, and word-spacing 0.16× of font size.

## Targets and input

**C028 · Target size minimum** — WCAG 2.2, 2.5.8, AA
24×24 CSS pixels, with defined exceptions for adequate spacing, inline targets, user-agent-controlled elements, and cases where the presentation is essential.

**C029 · Target size enhanced** — WCAG 2.5.5, AAA
44×44 CSS pixels.

**C030 · Keyboard operability** — WCAG 2.1.1, A
All functionality is operable through a keyboard interface.

**C031 · No keyboard trap** — WCAG 2.1.2, A
Focus that can enter a component can leave it.

**C032 · Focus visible** — WCAG 2.4.7, AA
Keyboard focus has a visible indicator.

**C033 · Focus not obscured** — WCAG 2.2, 2.4.11, AA
The focused element is not entirely hidden by author-created content such as sticky headers or cookie banners.

**C034 · Flash threshold** — WCAG 2.3.1, A
Nothing flashes more than three times in one second, unless below the general and red flash thresholds.

**C035 · Pause, stop, hide** — WCAG 2.2.2, A
Moving, blinking, or auto-updating content lasting more than five seconds can be paused, stopped, or hidden.

**C036 · Motion from interaction** — WCAG 2.3.3, AAA, plus `prefers-reduced-motion`
Motion animation triggered by interaction can be disabled unless essential. The media query is the mechanism; honoring it is the obligation.

**C037 · Dragging alternative** — WCAG 2.2, 2.5.7, AA
Any function using a dragging movement has a single-pointer alternative.

## Structure and forms

**C038 · Meaningful sequence and focus order** — WCAG 1.3.2 A, 2.4.3 A
Reading and focus order preserve meaning. Visual reordering that diverges from DOM order breaks this.

**C039 · Labels or instructions** — WCAG 3.3.2, A
Input requiring user data has a label or instruction. A placeholder is not a label.

**C040 · Error identification and suggestion** — WCAG 3.3.1 A, 3.3.3 AA
Errors are identified in text and, where known, a correction is suggested.

**C041 · Redundant entry** — WCAG 2.2, 3.3.7, A
Information previously entered is auto-populated or available for selection, rather than re-requested.

<!-- vale Suite.RefusedTerms = NO --><!-- "Accessible authentication" is WCAG's own success-criterion name (3.3.8), quoted verbatim -->
**C042 · Accessible authentication** — WCAG 2.2, 3.3.8, AA
No cognitive function test — remembering, transcribing, solving puzzles — is required for any step of authentication without an alternative.
<!-- vale Suite.RefusedTerms = YES -->

**C043 · Consistent navigation and identification** — WCAG 3.2.3, 3.2.4, AA
Repeated navigation appears in the same relative order, and components with the same function are identified consistently.

**C044 · Page titled** — WCAG 2.4.2, A
Every page has a title describing its topic or purpose.

**C045 · Language of page** — WCAG 3.1.1, A
The default human language is programmatically determinable.

**C046 · Name, role, value** — WCAG 4.1.2, A
For all interface components, name and role are programmatically determinable, and states and values can be set and reported. This is the constraint that makes custom controls expensive.

---

# PART C — LEGAL

*Kind: legal. Volatility: volatile — recheck quarterly. Jurisdiction- and sector-dependent. Sources and dates given for verification.*

## Accessibility obligations

**C060 · EU — European Accessibility Act**
Directive 2019/882. Enforceable since 28 June 2025 across all 27 member states. Technical standard is EN 301 549, which incorporates WCAG 2.1 Level AA. EN 301 549 was expected to update to reference WCAG 2.2 in late 2026.
*Scope* — e-commerce, banking, transport booking, e-books, telecoms, and related consumer services. Applies to businesses established anywhere, including US and UK, if they sell to EU consumers. Services already on the market before June 2025 have until 28 June 2030. Microenterprises — fewer than 10 employees and under €2M turnover — are exempt from service obligations but not product obligations, and this exemption does not extend to non-EU businesses serving the EU market. Each member state sets its own penalties.

**C061 · US public sector — ADA Title II**
DOJ 2024 final rule. Standard is WCAG 2.1 Level AA. Compliance dates were extended by one year in the DOJ Interim Final Rule of April 2026: 26 April 2027 for entities serving populations of 50,000 or more, 26 April 2028 for smaller entities and special district governments. The technical standard and covered scope were unchanged by the extension.

**C062 · US healthcare and education — Section 504**
HHS rule. 11 May 2026 for recipients with 15 or more employees, 10 May 2027 for smaller recipients. Not extended by the April 2026 DOJ action, which covered Title II only.

**C063 · US private sector — ADA Title III**
No formal regulatory deadline or codified technical standard. Courts and DOJ enforcement apply WCAG 2.1 Level AA in practice. Federal web accessibility suits have run in the thousands annually, concentrated in e-commerce, healthcare, and hospitality.

**C064 · US federal — Section 508**
Federal agencies and their vendors. Incorporates WCAG by reference through the Revised 508 Standards.

**C065 · Accessibility statement**
Required of EU public sector bodies under the Web Accessibility Directive. Elsewhere a strong practice rather than an obligation.

## Data and consent

**C066 · Prior consent for non-essential processing**
GDPR and the ePrivacy Directive. Consent must be freely given, specific, informed, and unambiguous, obtained before non-essential cookies or trackers are set, and withdrawable as easily as it was granted. Pre-ticked boxes, bundled consent, and refusal paths more burdensome than acceptance do not qualify.

**C067 · Data subject rights**
Access, rectification, erasure, and portability under GDPR, with analogues in CPRA and a growing set of US state statutes. Each implies a working interface, not a policy paragraph.

**C068 · Sale and sharing opt-out**
CPRA and similar state laws. Requires a functioning opt-out mechanism, and recognition of Global Privacy Control signals in several jurisdictions.

## Commercial conduct

**C069 · Subscription cancellation**
Unsettled and actively moving. The FTC's 2024 Negative Option Rule, known as Click-to-Cancel, was vacated in its entirety by the Eighth Circuit on 8 July 2025 in *Custom Communications, Inc. v. FTC*, on procedural grounds under the FTC Act's Magnuson-Moss requirements. That vacatur reinstated the narrow 1973 Negative Option Rule covering prenotification plans only.
The four substantive requirements did not disappear with the rule. The FTC has continued enforcing them under ROSCA and Section 5 of the FTC Act, including actions against Amazon and Uber. On 11 March 2026 the FTC issued an Advance Notice of Proposed Rulemaking to rebuild the rule, naming the same four requirements as likely building blocks: no misrepresentation, clear disclosure of material terms, express informed consent, and a simple cancellation mechanism.
Approximately 30 US states have their own automatic-renewal statutes, several stricter than the vacated federal rule.
*Practical floor* — cancellation no harder than signup, regardless of federal rulemaking status.

**C070 · Material terms before purchase**
Price, recurrence, duration, and total cost disclosed clearly and conspicuously before the transaction, under ROSCA, FTC Act Section 5, EU consumer directives, and state analogues.

---

# PART D — PLATFORM

*Kind: platform. Volatility: release-tied.*

**C080 · iOS input zoom**
Safari on iOS zooms the viewport when a form field with a computed font size below 16px receives focus. This makes 16px an effective floor for input text, not a preference.

**C081 · Email rendering**
Email clients support a fraction of CSS. Flexbox and Grid are unreliable, external stylesheets are frequently stripped, and table-based layout with inline styles remains the durable approach. Any token system extending to email crosses a hard capability boundary.

**C082 · Platform target conventions**
Apple Human Interface Guidelines specify 44×44pt. Android and Material specify 48×48dp. Both exceed the WCAG 2.2 AA floor at C028.

**C083 · Safe areas**
Notches, dynamic islands, rounded display corners, home indicators, and system bars occupy screen edges. Content placed in these regions is obscured or intercepted.

**C084 · OS text size settings**
Dynamic Type on iOS and font scale on Android are user settings that must be honored. Fixed pixel type ignores them.

**C085 · Browser minimum font size**
Users can set a minimum font size in browser preferences, which overrides author values below it.

**C086 · Autofill token vocabulary**
The `autocomplete` attribute takes a fixed, specified set of tokens. Invented values do not work, and correct values are among the cheapest usability improvements available.

---

# PART E — PHYSICAL

*Kind: physical. Volatility: slow.*

**C100 · Bit depth and banding**
8 bits per channel is the delivery standard. Long, low-contrast gradients band visibly at this depth. The remedy is noise, not additional color stops.

**C101 · Untagged color is assumed sRGB**
Images and colors without an embedded profile are interpreted as sRGB. Wide-gamut assets shipped untagged render desaturated.

**C102 · Animation cost tiers**
`transform`, `opacity`, and `filter` composite on the GPU. Paint-triggering properties cost a repaint. Geometry properties cost a full reflow. This ordering is a property of how browsers render, not a style preference.

**C103 · Frame budget**
16.7ms per frame at 60Hz, 8.3ms at 120Hz, inclusive of all main-thread work. Exceeding it drops frames.

**C104 · Font swap and layout shift**
A fallback font with different metrics shifts every line when the webfont loads. Metric override descriptors exist because this is unavoidable otherwise.

**C105 · Unsized media shifts layout**
Media without declared dimensions or aspect ratio reserves no space, so everything below it moves on load.

---

# PART F — ELECTIVE BUDGETS

*Kind: elective. Volatility: local. Not binding until adopted. Fully binding afterward — an unenforced budget is not a constraint, it is an opinion.*

**C120 · Core Web Vitals thresholds**
Externally defined by Google and used in ranking. Largest Contentful Paint good at 2.5s or under, poor above 4.0s. Interaction to Next Paint good at 200ms or under, poor above 500ms. Cumulative Layout Shift good at 0.1 or under, poor above 0.25. Measured at the 75th percentile of real users.

**C121 · Page weight budget**
Set per template, enforced in CI. Unset, it will drift upward monotonically.

**C122 · JavaScript budget**
Set separately from total weight, because script costs parse and execution time in addition to transfer.

**C123 · Font budget**
Families, weights, and total bytes. The most common uncontrolled source of both weight and layout shift.

**C124 · Third-party budget**
Count and weight of scripts you do not control. The only budget category whose contents can change without any deployment on your part.

---

# EXPORT INDEX

<!-- vale Suite.RefusedTerms = NO --><!-- this table repeats each entry's exported Name verbatim, including C042 "Accessible authentication" (WCAG's own criterion name); scoped to the whole table rather than one row to keep the table contiguous -->
| ID | Name | Kind | Volatility |
|---|---|---|---|
| C001 | Acknowledgment window | Perceptual | Invariant |
| C002 | Flow threshold | Perceptual | Invariant |
| C003 | Attention threshold | Perceptual | Invariant |
| C004 | Measure for sustained reading | Perceptual | Invariant |
| C005 | Reading rate | Perceptual | Invariant |
| C006 | Working memory limit | Perceptual | Invariant |
| C007 | Foveal acuity | Perceptual | Invariant |
| C008 | Change blindness | Perceptual | Invariant |
| C009 | Vestibular sensitivity | Perceptual | Invariant |
| C010 | Photosensitivity | Perceptual | Invariant |
| C011 | Color vision deficiency | Perceptual | Invariant |
| C012 | Contrast is a luminance relationship | Perceptual | Invariant |
| C020 | Text contrast minimum | Standard | Slow |
| C021 | Text contrast enhanced | Standard | Slow |
| C022 | Non-text contrast | Standard | Slow |
| C023 | Color is not sufficient alone | Standard | Slow |
| C024 | Text alternatives | Standard | Slow |
| C025 | Resize text | Standard | Slow |
| C026 | Reflow | Standard | Slow |
| C027 | Text spacing tolerance | Standard | Slow |
| C028 | Target size minimum | Standard | Slow |
| C029 | Target size enhanced | Standard | Slow |
| C030 | Keyboard operability | Standard | Slow |
| C031 | No keyboard trap | Standard | Slow |
| C032 | Focus visible | Standard | Slow |
| C033 | Focus not obscured | Standard | Slow |
| C034 | Flash threshold | Standard | Slow |
| C035 | Pause, stop, hide | Standard | Slow |
| C036 | Motion from interaction | Standard | Slow |
| C037 | Dragging alternative | Standard | Slow |
| C038 | Meaningful sequence and focus order | Standard | Slow |
| C039 | Labels or instructions | Standard | Slow |
| C040 | Error identification and suggestion | Standard | Slow |
| C041 | Redundant entry | Standard | Slow |
| C042 | Accessible authentication | Standard | Slow |
| C043 | Consistent navigation and identification | Standard | Slow |
| C044 | Page titled | Standard | Slow |
| C045 | Language of page | Standard | Slow |
| C046 | Name, role, value | Standard | Slow |
| C060 | EU — European Accessibility Act | Legal | Volatile |
| C061 | US public sector — ADA Title II | Legal | Volatile |
| C062 | US healthcare and education — Section 504 | Legal | Volatile |
| C063 | US private sector — ADA Title III | Legal | Volatile |
| C064 | US federal — Section 508 | Legal | Volatile |
| C065 | Accessibility statement | Legal | Volatile |
| C066 | Prior consent for non-essential processing | Legal | Volatile |
| C067 | Data subject rights | Legal | Volatile |
| C068 | Sale and sharing opt-out | Legal | Volatile |
| C069 | Subscription cancellation | Legal | Volatile |
| C070 | Material terms before purchase | Legal | Volatile |
| C080 | iOS input zoom | Platform | Release-tied |
| C081 | Email rendering | Platform | Release-tied |
| C082 | Platform target conventions | Platform | Release-tied |
| C083 | Safe areas | Platform | Release-tied |
| C084 | OS text size settings | Platform | Release-tied |
| C085 | Browser minimum font size | Platform | Release-tied |
| C086 | Autofill token vocabulary | Platform | Release-tied |
| C100 | Bit depth and banding | Physical | Slow |
| C101 | Untagged color is assumed sRGB | Physical | Slow |
| C102 | Animation cost tiers | Physical | Slow |
| C103 | Frame budget | Physical | Slow |
| C104 | Font swap and layout shift | Physical | Slow |
| C105 | Unsized media shifts layout | Physical | Slow |
| C120 | Core Web Vitals thresholds | Elective | Local |
| C121 | Page weight budget | Elective | Local |
| C122 | JavaScript budget | Elective | Local |
| C123 | Font budget | Elective | Local |
| C124 | Third-party budget | Elective | Local |
<!-- vale Suite.RefusedTerms = YES -->

---

## Review schedule

**Invariant** — no review. If one of these changes, the change is in the research, not the constraint.
**Slow** — annually, and on any WCAG revision. The next material event is WCAG 3.0 reaching Candidate Recommendation, projected Q4 2027, with no compliance force until well after.
**Volatile** — quarterly, per operating jurisdiction. C069 in particular has an open federal rulemaking.
**Release-tied** — on major browser and OS releases.
**Local** — whenever adopted or revised. Enforced continuously in CI, not reviewed on a calendar.

## Settled decisions

**Standards baseline is WCAG 2.2, not 2.1.** Every legal regime in Part C currently requires 2.1 AA. Building to 2.2 AA satisfies all of them, costs little beyond 2.1, and absorbs the expected EN 301 549 update without a second pass. Part B is therefore written at 2.2.

**Perceptual constraints are separated from standards constraints even where they overlap.** C010 photosensitivity and C034 flash threshold describe the same phenomenon. They are kept apart because one is a fact about people and the other is a testable number that could be revised. Collapsing them would attach a revision cycle to a physiological reality.

**Core Web Vitals are listed as elective.** They are externally defined and commercially consequential, but nothing prevents shipping a site that fails them. Treating them as binding is a choice, and the document should not pretend otherwise.
