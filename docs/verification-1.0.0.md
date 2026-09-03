```yaml
document: Verification
version: 1.0.4
tier: 3
owns:
  - how to confirm something works
  - how to confirm it conforms
  - how to confirm it matches what was decided
  - how to confirm it is understood
  - who runs each check and when
exports: X001–X412
depends:
  - Vocabulary ^1
  - Anatomy ^1
  - Composition ^1
  - Constraints ^1
  - Decision ^1
  - Implementation ^1
reviewed: 2026-09-03
```

# Verification

Four different questions that get called testing, with four different methods and four different failure modes. Conflating them is why sites pass every check they run and are still wrong.

---

## What this document owns

The checks, their placement, their cadence, and their named owner. Plus an honest account of what checking cannot tell you.

## What it does not own

| Question | Owner |
|---|---|
| What may not be done? | Constraints |
| What should it be set to? | Decision |
| How is the check implemented in the codebase? | Implementation |
| How do I read an existing site I did not build? | Diagnosis |

---

## X001 · The four modes

**Correctness** — does it do what it is supposed to do? Failure is a bug. Automatable. Cheap.
**Conformance** — does it stay inside Constraints? Failure is an exclusion or a liability. Partly automatable.
**Coherence** — does the built thing match what was decided? Failure is drift. Barely automatable, and almost never checked.
**Comprehension** — do people understand it? Failure is the product not working despite all three above passing. Not automatable at all.

The modes are ordered by cost and inversely by how much they tell you. Correctness is cheapest and least informative; comprehension is most expensive and the only one that can invalidate the whole design.

## X002 · Passing is not evidence of quality

Every check in this document can pass on a site nobody can use. Checks establish a floor and detect regression. They do not establish that the thing is good, and a program that treats a green pipeline as a verdict has mistaken the floor for the ceiling.

---

# PART I — CORRECTNESS

## X010 · State matrix coverage
Every component renders every state required by K002 — rest, hover, focus-visible, active, disabled, loading, empty, partial, full, error. A state with no test has no design.
*Method* — story or fixture per state, snapshot per state.

## X011 · Content stress
Every slot rendered with: a 3-character string, a 90-character string, a string with combining characters and emoji, an empty value, and a null. Every collection rendered at 0, 1, 7, and 10,000.
*Method* — shared fixture set, applied to every component. Verifies K006 and K043.

## X012 · Pseudo-localization
Every screen rendered with expanded accented strings before any real translation exists. Catches K048 expansion failures and hardcoded strings K046 missed, at a fraction of the cost of discovering them during localization.

## X013 · Direction
Every screen rendered RTL. Verifies K012 and K049. Failures here are almost always a physical property that escaped the logical-property rule.

## X014 · Viewport matrix
Rendered at the narrowest supported width, the widest, and each declared breakpoint boundary — plus one width either side of each boundary, where the failures actually are.

## X015 · Zoom and reflow
Rendered at the equivalent width C026 requires. Verifies K058.

## X016 · Visual regression
Snapshot comparison across the matrix above. Catches unintended change, not incorrectness — a regression suite validates that nothing moved, never that it was right to begin with.

## X017 · Failure surfaces
404, offline, maintenance, timeout, and permission-denied rendered deliberately, not discovered accidentally. Verifies K016.

## X018 · Cold cache and slow network
First visit on a throttled connection, no warm cache, no service worker. This is a substantial fraction of real first impressions and almost never the condition anyone develops in.

---

# PART II — CONFORMANCE

## X100 · The automated set

Twenty-two of the constraints Implementation places are mechanically enforceable. These run per commit and block merge on failure. No cadence discussion is needed; they either pass or the build stops.

*Category first, tool second — the tool column is the most volatile content in this document and is rechecked semi-annually.*

| Check | Verifies | Category · current tool | Gate |
|---|---|---|---|
| X101 Contrast assertion over all token pairings | C020, C021, C022 | Color library in the token build · `culori`, `colorjs.io` | Commit |
| X102 Rem-component lint on type sizes | C025 | CSS linter · `stylelint` | Commit |
| X103 Input size floor assertion | C080 | CSS linter · `stylelint` | Commit |
| X104 Reflow render at 320px equivalent | C026 | Browser automation · Playwright | PR |
| X105 Text-spacing override injection | C027 | Browser automation · Playwright | PR |
| X106 Computed target-size assertion | C028 | Browser automation · Playwright | PR |
| X107 Focus-cycle test on every overlay | C031, C033 | Browser automation · Playwright, `@testing-library` | PR |
| X108 Outline-removal lint | C032 | CSS linter · `stylelint` | Commit |
| X109 Unpaired motion-token lint | C036 | Token build assertion · custom | Commit |
| X110 Missing name / alt lint | C024, C039 | Markup linter · `eslint-plugin-jsx-a11y`, `html-validate` | Commit |
| X111 Page title and lang lint | C044, C045 | Markup linter · `html-validate` | Commit |
| X112 Metric-override presence per family | C104 | Font loader · `fontaine`, `next/font`, `@capsizecss/*` | Commit |
| X113 Unsized-media lint | C105 | Markup linter · `eslint-plugin-jsx-a11y` | Commit |
| X114 Bundle and asset budget assertion | C121–C124 | Budget enforcement · `size-limit`, Lighthouse CI | PR |
| X115 Field measurement at 75th percentile | C120 | RUM · CrUX, `web-vitals` | Continuous |
| X116 Automated accessibility audit | broad | Rule engine · `axe-core`, `@axe-core/playwright`, Pa11y | PR |

## X117 · What the automated set does not cover

Automated tooling detects a minority of accessibility defects. Industry estimates put the mechanically detectable share of WCAG violations at roughly a quarter to two fifths, with expert manual review required for the remainder. A program reporting "zero accessibility violations" from automated tooling alone is reporting the state of its tooling, not the state of its product.

## X120 · The manual set

Ten constraints cannot be mechanically verified. Implementation states this as a liability rather than a footnote; this document discharges it. Each has a named owner and a stated cadence. Unowned, none of these happen.

**Run these inside WCAG-EM, not beside it.** The W3C Website Accessibility Conformance Evaluation Methodology defines how to select a representative sample of pages, how to conduct the evaluation, and how to report the result. The suite does not redefine any of that. What it adds is the cap in X131: WCAG-EM bounds rigour but not scope, and an unbounded manual programme is the kind that lapses.

| Check | Verifies | Method | Cadence |
|---|---|---|---|
| X121 Color-independence review | C023 | Grayscale pass over every state-bearing surface, via DevTools rendering emulation | Per release |
| X122 Keyboard-only traversal | C030 | Complete every primary task using no pointer | Per release |
| X123 Screen reader pass | C046 | One primary task per platform AT, against ARIA-AT expected behaviours rather than ad-hoc judgement | Per release |
| X124 Focus-order comparison | C038 | DOM order against visual order, per template | Per release |
| X125 Flash and motion review | C034, C035 | Human observation of any animated or auto-updating surface | On change |
| X126 Dragging alternative audit | C037 | Every drag operation attempted single-pointer | On change |
| X127 Error message review | C040 | Every error states cause and next action | Per release |
| X128 Redundant entry audit | C041 | Every multi-step flow walked for re-requested data | Per flow change |
| X129 Authentication review | C042 | Every auth path checked for a cognitive function test | On change |
| X130 Consistency audit | C043 | Repeated components compared across templates | Quarterly |

## X131 · The manual set is one page

That is the point. Ten checks, each a stated method and cadence, fitting on a single page that a named person owns. A manual program larger than this is aspirational and will lapse; one this size will not.

## X140 · Legal recheck

The volatile entries in Constraints — C060 through C070 — are rechecked quarterly per operating jurisdiction. This is a verification activity because the constraint can change without any code changing, which means a site can fall out of conformance while passing every test in this document.

---

# PART III — COHERENCE

*Does the built thing match what was decided? The mode with no established practice, and where drift actually lives.*

## X200 · Coherence requires a record

Coherence cannot be checked against intent held in someone's head. It is checked against the decision record Decision specifies — the setting, the default departed from, the reason, and the accepted cost. **Where no record exists, coherence is unverifiable and this entire part is inapplicable.** That is the strongest practical argument for keeping the record.

## X201 · Drift metrics

The computable half. Each compares a declared count against the count actually present in the shipped artifact.

**Do not build this.** CSS analysis tooling already extracts every color, font size, shadow, spacing value, and custom property from a stylesheet or a live URL, groups them, and reports which custom properties are declared versus actually used. Project Wallace is the current instance, available hosted and as `@projectwallace/css-analyzer` on npm, with two hundred–plus metrics. X202 through X208 are a query against its output, not a program to write.

| Metric | Declared | Measured | Drift signal |
|---|---|---|---|
| X202 Distinct font sizes | T031 scale length | CSS analyzer | More sizes than the scale has steps |
| X203 Distinct colors | Token count | CSS analyzer | Colors resolving to no token |
| X204 Distinct spacing values | T020 scale length | CSS analyzer | Values off the scale |
| X205 Distinct radii | T040 scale length | CSS analyzer | Ad-hoc corners |
| X206 Distinct durations | T060 scale length | CSS analyzer | Hand-tuned timings |
| X207 Raw value occurrences | Zero, per K040 | `stylelint` over component source | Any occurrence |
| X208 Z-index values off band | Zero, per K053 | `stylelint` | Any integer literal |
| X209 Component instance census | Documented components | Component analytics · Omlet, `react-scanner`, Preply Design System Visual Coverage | Undocumented components in production |

X209 needs different tooling from X202–X208 — static analysis of the codebase rather than of the stylesheet — and is currently solved for React estates and unsolved for heterogeneous ones.

**What no tool supplies** is the part that matters: which number is the threshold, who owns it, what happens when it rises, and the cadence in X410. A drift figure nobody owns is a statistic.

A system with a seven-step type scale rendering twenty-three distinct sizes has not drifted a little. It has stopped being a system, and no check in Parts I or II will say so.

## X210 · Congruence audit

The uncomputable half. Decision states a set of coherence tests — combinations that produce a specific misreading. Each becomes a periodic human check, because no tool can evaluate them.

| Check | Verifies | Tests | Reads as |
|---|---|---|---|
| X211 | D100 | Craft standard against failure surfaces | Demo-ware |
| X212 | D101 | Claim strength against endorsement provenance | Unbacked |
| X213 | D102 | Commercial pressure against pricing disclosure | Evasive |
| X214 | D103, D104 | Scale signaling against authorship presence | Faceless or costumed |
| X215 | D105 | Density against craft level | Cluttered |
| X216 | D106 | Layout generosity against copy volume | Endless |
| X217 | D107 | Motion quantity against measured speed | Showy and slow |
| X218 | D108 | Distribution of convention departures | Unlearnable |
| X219 | D109 | Audience expertise against path control | Condescending |

*Method* — one reviewer who did not build it, walking the primary journey, answering each as a yes or no with one sentence of evidence. Quarterly, or before any launch.

## X220 · The three questions

Per D111, Decision reduces every congruence failure to one of three being answered inconsistently: how big are we, how much do we mean it, how much care went into this. A faster version of X210, when time is short, is to answer those three from the artifact alone and check the answers against the decision record.

---

# PART IV — COMPREHENSION

*The only mode that can invalidate the design rather than the build. Requires people and cannot be shortened.*

## X300 · Task success
Can a representative person complete the primary task unaided? Measured as completion rate and time, not as satisfaction. Five participants surfaces most severe issues; it does not produce a rate you can quote.

## X301 · First-impression test
Five seconds on the landing view, then: what does this do, who is it for, what would you do next. Tests the arrangement and language planes directly, and is the cheapest study in this document.

## X302 · Findability
Tree testing on the structure without visual design, verifying the labeling scheme independently of how it looks.

## X303 · Comprehension of terms
Whether the vocabulary the site uses is the vocabulary its audience uses. Failures here read as an audience mismatch and are invisible to every other check.

## X304 · Assistive technology sessions
Task completion by people who use assistive technology daily. This is distinct from X123: a developer performing a screen reader pass verifies mechanics, and a daily user reveals whether the experience is usable. Both are needed, and the second cannot be substituted by the first.

## X305 · Comprehension is not preference
Asking people what they like produces preference data and answers no question this document poses. Observe behavior; record what happened rather than what was reported.

---

# PART V — THE SUITE ITSELF

## X400 · Mechanical validation
Every document's front matter present, tier correct, declared exports matching actual, dependency direction downward only, and every cited ID resolving. Automatable, and automated.

## X401 · Citation correctness is not citation resolution
Validation confirms that a cited ID exists. It cannot confirm the cited ID is the one intended — a document citing C020 where C022 was meant passes every mechanical check. This requires review, and it is the one suite defect that will accumulate silently.
*Method* — on any document change, a second reader confirms each new or modified citation says what the sentence claims. There is no alternative to this.

## X402 · Ownership audit
Each document holds only facts it owns. The test: take a sentence, ask which document owns the question it answers, and confirm that is the document it is in. Quarterly, and on every new document.

## X403 · Orphan check
Every exported ID is either cited by something or deliberately retained. An ID nothing references is either missing a citation or is content nobody needs.

---

# PART VI — CADENCE

## X410 · Placement

| When | What | Blocks |
|---|---|---|
| Every commit | Lint set, token assertions, X400 | Merge |
| Every pull request | X104–X107, X114, X116, X016 visual regression | Merge |
| Every release | X121–X124, X127 — the per-release manual set | Release |
| On relevant change | X125, X126, X128, X129 | Merge of that change |
| Quarterly | X130, X140 legal recheck, X201 drift metrics, X210 congruence, X402 | Nothing — reported |
| Annually | Standards recheck, X300–X304 comprehension round | Nothing — reported |
| Continuous | X115 field measurement | Alerts |

## X411 · Quarterly checks block nothing and must be reported

Nothing in the quarterly row can fail a build, which is exactly why each needs a named owner and a written result. A check that blocks nothing and reports to no one does not exist.

## X412 · Cadence is stated per check, not per program

"We test accessibility" is not a cadence. Each of the ten manual checks has its own frequency in X120 because they genuinely differ: a focus-order comparison is worth doing per release, and a consistency audit across templates is wasted effort at that frequency.

---

# PART VII — LIMITS

## What none of this establishes

**That the design is good.** Every check here can pass on a coherent, conformant, fast, comprehensible site that solves the wrong problem. Purpose is the one plane no test reaches.

**That conformance equals usability.** Meeting every criterion produces a floor, not an experience. A site can be perfectly conformant and miserable to use, and X304 exists because that combination is common.

**That automated accessibility results are accessibility results.** Per X117, the automated share is a minority of defects. The number produced by tooling is a tooling metric.

**That lab measurement predicts field measurement.** X115 is field data at the 75th percentile because lab conditions systematically flatter. A lab pass with a field failure is the normal case, not an anomaly.

**That a passing suite reflects a current suite.** Volatile constraints change without any code changing. X140 exists because conformance can lapse while everything stays green.

---

# EXPORT INDEX

| ID | Check | Mode |
|---|---|---|
| X001 | The four modes | Framing |
| X002 | Passing is not evidence of quality | Framing |
| X010 | State matrix coverage | Correctness |
| X011 | Content stress | Correctness |
| X012 | Pseudo-localization | Correctness |
| X013 | Direction | Correctness |
| X014 | Viewport matrix | Correctness |
| X015 | Zoom and reflow | Correctness |
| X016 | Visual regression | Correctness |
| X017 | Failure surfaces | Correctness |
| X018 | Cold cache and slow network | Correctness |
| X100 | The automated set | Conformance |
| X101 | Contrast assertion | Conformance |
| X102 | Rem-component lint | Conformance |
| X103 | Input size floor | Conformance |
| X104 | Reflow render | Conformance |
| X105 | Text-spacing override | Conformance |
| X106 | Target-size assertion | Conformance |
| X107 | Focus-cycle test | Conformance |
| X108 | Outline-removal lint | Conformance |
| X109 | Unpaired motion-token lint | Conformance |
| X110 | Missing name lint | Conformance |
| X111 | Title and lang lint | Conformance |
| X112 | Metric-override presence | Conformance |
| X113 | Unsized-media lint | Conformance |
| X114 | Budget assertion | Conformance |
| X115 | Field measurement | Conformance |
| X116 | Automated accessibility audit | Conformance |
| X117 | Coverage limit of the automated set | Conformance |
| X120 | The manual set | Conformance |
| X121 | Color-independence review | Conformance |
| X122 | Keyboard-only traversal | Conformance |
| X123 | Screen reader pass | Conformance |
| X124 | Focus-order comparison | Conformance |
| X125 | Flash and motion review | Conformance |
| X126 | Dragging alternative audit | Conformance |
| X127 | Error message review | Conformance |
| X128 | Redundant entry audit | Conformance |
| X129 | Authentication review | Conformance |
| X130 | Consistency audit | Conformance |
| X131 | The manual set is one page | Conformance |
| X140 | Legal recheck | Conformance |
| X200 | Coherence requires a record | Coherence |
| X201 | Drift metrics | Coherence |
| X202 | Distinct font sizes | Coherence |
| X203 | Distinct colors | Coherence |
| X204 | Distinct spacing values | Coherence |
| X205 | Distinct radii | Coherence |
| X206 | Distinct durations | Coherence |
| X207 | Raw value occurrences | Coherence |
| X208 | Z-index values off band | Coherence |
| X209 | Component instance census | Coherence |
| X210 | Congruence audit | Coherence |
| X211 | Craft against failure surfaces | Coherence |
| X212 | Claim strength against provenance | Coherence |
| X213 | Pressure against disclosure | Coherence |
| X214 | Scale against authorship | Coherence |
| X215 | Density against craft | Coherence |
| X216 | Generosity against copy volume | Coherence |
| X217 | Motion against measured speed | Coherence |
| X218 | Distribution of departures | Coherence |
| X219 | Expertise against path control | Coherence |
| X220 | The three questions | Coherence |
| X300 | Task success | Comprehension |
| X301 | First-impression test | Comprehension |
| X302 | Findability | Comprehension |
| X303 | Comprehension of terms | Comprehension |
| X304 | Assistive technology sessions | Comprehension |
| X305 | Comprehension is not preference | Comprehension |
| X400 | Mechanical validation | Suite |
| X401 | Citation correctness | Suite |
| X402 | Ownership audit | Suite |
| X403 | Orphan check | Suite |
| X410 | Placement | Cadence |
| X411 | Quarterly checks must be reported | Cadence |
| X412 | Cadence is per check | Cadence |

---

## Settled decisions

**Four modes, not one activity.** Correctness, conformance, coherence, and comprehension have different methods, owners, and failure consequences. Merging them under "testing" is what produces programs that automate the cheap mode thoroughly and never perform the expensive one at all.

**The manual set is capped at ten and fits on one page.** A larger manual program is aspirational. Ten checks with named methods and stated cadences is small enough to actually happen, and X131 states the cap as deliberate so that additions are argued for rather than accumulated.

**Coherence is the mode with no established practice, so it gets the most specification.** Part III is longer than Part II despite covering fewer checks, because conformance has an industry and coherence does not. The drift metrics in X201 are computable and rarely computed; the congruence audit in X210 requires a person and is essentially never run.

**Comprehension is annual and reported, not gated.** Gating a release on a research round is a promise nobody keeps, and a check that gets waived under deadline is worse than one that was never a gate. Annual and reported is honest about what it is.

<!-- vale Suite.RefusedTerms = NO --><!-- "clean bill" is the idiom "clean bill of health" (a verdict of full clearance), not the refused adjective describing an artifact's appearance -->
**Part VII exists because verification documents are read as guarantees.** Five things this document cannot establish are stated plainly, including the one most likely to be misread — that automated accessibility results are a minority of accessibility defects, not a clean bill.
<!-- vale Suite.RefusedTerms = YES -->
