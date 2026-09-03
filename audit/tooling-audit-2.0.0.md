```yaml
document: Tooling Audit
version: 2.0.0
supersedes: 1.0.0
tier: n/a — assessment, not a suite document
covers: all eight suite artifacts as of 2026-09-03
volatility: high — recheck semi-annually, or on any trigger in Part VII
reviewed: 2026-09-03
```

# Tooling Audit

Where the suite duplicates something that exists, where it names a check without naming what runs it, where it is genuinely alone, and what happens when the tools it now depends on die.

---

## Method, and what changed from 1.0.0

Version 1.0.0 made five claims of novelty on the basis of not having found prior art. That is not the same as prior art not existing, and two of the five did not survive being searched for properly. This version tests each claim, states a confidence level, and names the nearest thing found even where the claim survives.

Three verdicts on prior art: **Superseded** — an equivalent exists and is better; adopt it. **Weakened** — something adjacent exists; the claim needs qualifying. **Holds** — searched and not found, with confidence stated.

Every tool named carries a **risk grade** in Part IV. Version 1.0.0 named tools without asking what happens when they go away, which is how a document that reduces coupling ends up creating it.

---

# PART I — CORRECTIONS TO 1.0.0

*Two errors, both from asserting rather than checking.*

## E1 · X209 is covered, and I said it was not

**1.0.0 said** — the component instance census is "not covered by CSS analysis — requires DOM or build-graph instrumentation."

**Correct as far as it went, and wrong in implication.** That instrumentation exists as shipping products. Omlet performs component analytics for React by static analysis of the codebase, automatically collecting reusable and custom components across projects, tracking adoption over time, and surfacing newly created custom components so a team can decide whether they belong in the system — which is exactly the X209 drift signal. It is built by the team behind Zeplin. `react-scanner` is the open-source static-analysis option. Preply's Design System Visual Coverage is open source and computes adoption as visual coverage using data attributes, working in production without performance cost; Mews published a comparison noting react-scanner lacks percentage coverage and visual-coverage overweights large components.

**Consequence** — X209 should cite the category and the options rather than being marked uncovered. The residual gap is narrower than stated: component census is solved for React codebases and unsolved for heterogeneous or non-React estates.

## E2 · The composition enumeration claim was too strong

**1.0.0 said** — nothing enumerates what a website consists of as settable choices; nearest priors are Garrett's planes and the Web Almanac.

**Missed** — GoodWeb, a framework from a scoping review of 69 website-evaluation studies published in JMIR Formative Research in 2019. It identifies eight umbrella attributes covering everything the reviewed literature evaluated: usability or ease of use, content, web design criteria, functionality, appearance, interactivity, satisfaction, and loyalty. Also missed: Nielsen's ten heuristics, which remain the dominant practitioner frame, with Shneiderman's Eight Golden Rules and Gerhardt-Powals' cognitive principles as specialized alternatives, and an established practice of running them with three to five evaluators.

**Assessment** — these are *evaluation* frames. They ask how good a website is against attributes, not what dimensions were set to produce it. GoodWeb's eight umbrella terms are outcomes; Composition's sixty-seven families are inputs. The distinction is real and the claim survives, but "nothing found" was wrong and the claim is downgraded accordingly in Part II.

---

# PART II — PRIOR ART, TESTED

| Claim | Verdict | Nearest prior | Confidence |
|---|---|---|---|
| N1 Composition enumeration | Weakened | GoodWeb, Nielsen heuristics, Garrett planes, Web Almanac | Moderate |
| N2 Coherence as a verification mode | Holds, qualified | Design-system drift literature | Low–moderate |
| N3 Constraints classified by why they bind | Holds | None found | Moderate |
| N4 Enforcement placement with published residue | Weakened | Coverage statistics are widely published | Low |
| N5 Document dependency architecture | Weakened | ADR, semver, acyclic dependency principle | Low |

## N1 · Composition enumeration — *weakened*

Evaluation frameworks are abundant and mature. What was not found is an enumeration of *settable* dimensions, particularly across language, representation, time, and social presence, which no evaluation frame covers. The honest claim is narrower than 1.0.0's: not that nobody has catalogued websites, but that existing catalogues answer "how good is this" rather than "what was decided."

## N2 · Coherence as a verification mode — *holds, qualified*

The design-system literature knows about drift and describes it in the same terms the suite does — components duplicated, tokens becoming inconsistent with code, accessibility quietly falling behind, decay unnoticed until it slows delivery. Supernova, Omlet, and the practitioner metrics literature all address it.

But drift and congruence are different questions. Drift asks *has the system leaked*; congruence asks *does the artifact agree with itself about how big we are, how much we mean it, and how much care went in*. Nothing found specifies the second as a repeatable check with named failure readings. Confidence is only low–moderate because informal design critique covers this ground constantly without writing it down, and an unwritten practice is hard to search for.

## N3 · Constraint classification by why it binds — *holds*

Accessibility references list requirements; legal trackers list obligations; none sort constraints by durability so that a physiological fact never acquires a revision cycle and a statute never gets treated as settled. Nothing found. Moderate confidence.

## N4 · Enforcement placement with published residue — *weakened*

The coverage statistic is not proprietary knowledge: estimates that automated tooling detects roughly a quarter to two fifths of WCAG violations circulate widely, and vendors publish them. What is less common is converting the residue into a named, owned, capped list with cadences. That is a practice difference, not a discovery. Downgrade the claim to "uncommonly done," not "not done."

## N5 · Document dependency architecture — *weakened*

Every mechanism has a prior, listed in Part V. Tiering is the acyclic dependency principle. Versioning is semver. One-fact-one-home is normalization. The registry is a schema registry. The assembly may be uncommon; the parts are all borrowed, and 1.0.0 should not have listed this as possibly novel without saying so.

**Overall.** The suite's contribution is assembly and completeness, not mechanism. That is a smaller claim than 1.0.0 implied and a more defensible one.

---

# PART III — TOOL MAP, ALL EIGHT ARTIFACTS

*Category first, instance second. The category is the durable half.*

## Suite Architecture
| Need | Category · instance |
|---|---|
| Version discipline | Semantic versioning |
| Dependency direction enforcement | Graph linting · `dependency-cruiser` |
| Registry serialization | Schema registry pattern · JSON Schema over the generated YAML |
| Markdown structure validation | Markdown linter · `remark-lint`, `markdownlint` |

## Vocabulary
| Need | Category · instance |
|---|---|
| Refused-term enforcement | Prose linter · Vale, with the Google and Microsoft style packages as priors |
| Adjacent prose rules | `textlint`, `write-good`, `alex` |
| Terminology management at scale | Controlled vocabulary standards · ISO 704, TBX |

## Anatomy
No tooling. It is a reference document and its correctness is checked against primary sources — MDN, the CSS and SVG specifications, caniuse. The only automatable check is that its constraint citations resolve, which `validate.py` already does.

## Constraints
| Need | Category · instance |
|---|---|
| Evaluation methodology | WCAG-EM |
| Screen reader behavioral basis | ARIA-AT |
| Rule engine | `axe-core` rulesets, mapped to success criteria |
| European technical standard | EN 301 549 |
| Legal change monitoring | **No tool.** Subscription services and counsel. See Part VI |

## Composition
No tooling, and this is expected — an enumeration of choices is not a computation. The adjacent artifacts are audit checklists, which answer a different question. See Part VI item 6 for the one buildable gap.

## Decision
| Need | Category · instance |
|---|---|
| Decision records | ADR · `adr-tools`, `log4brains`, MADR templates |
| Record completeness against the family set | **No tool.** See Part VI item 6 |

## Implementation
| Need | Category · instance |
|---|---|
| Token format | DTCG 2025.10 |
| Token transformation | Style Dictionary v4+, Terrazzo, Tokens Studio |
| Design-tool token round-trip | Figma Variables export to DTCG |
| Font metric overrides | `fontaine`, `next/font`, `@capsizecss/*` |
| Headless component primitives | Radix Primitives, Base UI, React Aria; copy-in via shadcn/ui |
| Focus containment | `focus-trap`, or the primitives above |
| Raw-value and z-index linting | `stylelint` |
| Dependency direction | `dependency-cruiser`, `eslint-plugin-boundaries` |
| Component documentation | Storybook autodocs |

## Verification
| Need | Category · instance |
|---|---|
| State and content matrix | Storybook with play functions; `faker` for volume |
| Pseudo-localization | `pseudo-localization`; pseudo-locale support in `i18next`, `formatjs` |
| Browser automation | Playwright |
| Visual regression | Chromatic, Playwright `toHaveScreenshot`, Argos, Lost Pixel, Percy |
| Accessibility rule engine | `axe-core`, `@axe-core/playwright`, Pa11y, Lighthouse |
| Markup and a11y linting | `eslint-plugin-jsx-a11y`, `html-validate` |
| Contrast assertion in token build | `culori`, `colorjs.io`; Leonardo for generation |
| Budgets | `size-limit`, Lighthouse CI |
| Field measurement | CrUX, `web-vitals`, any RUM provider |
| CSS drift metrics | `@projectwallace/css-analyzer` |
| Component census | Omlet; `react-scanner`; Preply Design System Visual Coverage |
| Congruence audit | **No tool.** See Part VI item 1 |

---

# PART IV — TOOL RISK REGISTER

*What 1.0.0 omitted. A document about reducing coupling should not introduce dependencies without grading them.*

| Tool | Backing | Risk | Exit |
|---|---|---|---|
| DTCG format | W3C community group, 40+ orgs | **Low** | It is the exit. Vendor-neutral by design |
| Style Dictionary | Amazon-originated, broad adoption | **Low** | Terrazzo consumes the same DTCG source |
| `axe-core` | Deque, commercially backed OSS, dominant | **Low** | Pa11y, Lighthouse use overlapping rules |
| Storybook | Well-funded, dominant | **Low** | Stories are close to portable test fixtures |
| Vale | Active OSS | **Low** | Rules are YAML; portable to any linter |
| Playwright | Microsoft | **Low** | Test intent portable; syntax is not |
| `stylelint` | Active OSS | **Low** | Rules re-expressible elsewhere |
| Project Wallace | Small team, active | **Moderate** | Metrics computable from any CSS parser; the ruleset is the value, not the tool |
| Radix Primitives | OSS, periodic maintenance concern | **Moderate** | Base UI, React Aria; the copy-in model already vendors the code, which is most of the mitigation |
| Chromatic / Percy | Commercial; Percy is BrowserStack-owned | **Moderate** | Playwright screenshot comparison covers the core need without a vendor |
| Omlet | Commercial, small | **Moderate–high** | `react-scanner` or Preply's open-source tool |
| Tokens Studio | Commercial | **Moderate** | DTCG output is portable |

## The governing rule

**Prefer a tool whose output is a standard format over a tool whose output is its own.** DTCG is the model: the pipeline can be replaced because the source file is not proprietary. Applied consistently, this is what keeps every moderate risk above from becoming a migration.

**Corollary for the two highest risks.** Omlet and Chromatic both hold data that is regenerable rather than authored — component usage and screenshots. Losing either costs history, not work. That is the right kind of dependency to accept.

---

# PART V — ADJACENT-FIELD PRIORS

*Patterns the suite uses, and where they come from. Naming them makes the suite legible to people arriving from those fields, and points at their tooling.*

| Suite mechanism | Prior | Field |
|---|---|---|
| Decision record | Architecture Decision Record, Nygard 2011; MADR | Software architecture |
| Independent document versioning | Semantic versioning | Package management |
| Downward-only citation | Acyclic Dependencies Principle | Software architecture |
| One fact, one home | Normalization; single source of truth | Database design |
| Deprecation before deletion | API versioning; W3C and RFC process | Standards |
| Generated registry | Schema registry; OpenAPI | Distributed systems |
| Floors versus targets | `shall` versus `should`; MoSCoW | Requirements engineering |
| Constraint volatility grading | Risk register; configuration management | Operations |
| Refused terms | Controlled vocabulary; terminology management | Technical writing, library science |
| Sampling for manual review | WCAG-EM | Accessibility |
| Three-tier tokens | Salesforce design system, origin of the term | Design systems |

Nothing in this table is a criticism. Borrowing a solved mechanism is correct. The failure mode 1.0.0 exhibited was borrowing without noticing, which forfeits the tooling and the literature that come with the name.

---

# PART VI — GAP REGISTER

*Searched for and not found. This is the build list, in order of value.*

**1 · Congruence checking.** X210–X219. Whether an artifact agrees with itself across scale, conviction, and care. No product, no open-source project, no established protocol. Remains a human reading with a written result. Highest-value gap and probably not automatable, which is why it needs a schedule rather than a tool.

**2 · Decision completeness.** Nothing reports which of the sixty-seven families have been decided and which are running on defaults. This is genuinely buildable: parse the ADR set, join against the generated registry, report unaddressed families. A weekend of work, and it converts Composition from a reference into a checklist that knows its own state. **Recommended build.**

**3 · Language-plane measurement.** F22–F30. Readability scoring exists — Flesch, Hemingway, Vale's readability rules — but nothing measures consistency of person, register, or claim strength across a site. Prose linting can enforce a term list; it cannot tell you the About page and the pricing page are speaking in different voices.

**4 · Representation-plane verification.** F50–F54. Individual tools exist for link previews, rich results, and structured data. Nothing runs them as one check across a site and reports what a person or a model actually sees when the site is not loaded.

**5 · Citation correctness.** X401. `validate.py` confirms an ID resolves; nothing confirms it is the intended one. Unautomatable in principle without semantic understanding of every sentence. Second reader, no alternative.

**6 · Legal change monitoring.** Constraints Part C is graded volatile and rechecked by hand. Commercial trackers exist for privacy and accessibility law but none map onto a constraint register. Manual, quarterly, per jurisdiction.

---

# PART VII — RECHECK PROTOCOL

Tool names are the most volatile content in the suite — more so than the legal constraints, which at least move on rulemaking cycles.

**Scheduled** — semi-annual pass over Parts III and IV.

**Triggered, immediately** — a named tool is archived or its repository goes quiet for two release cycles; a vendor acquisition; a license change; a specification version bump, such as Style Dictionary reaching full DTCG 2025.10 support in v5; or a category gaining a first credible entrant, which would apply to any gap in Part VI.

**Where the result goes** — into this document as a minor version, and into the owning suite document only if the *category* changed. A tool substitution within a category is a Part III edit and nothing else, which is the entire point of naming the category first.

---

## Settled decisions

**Novelty claims now carry confidence levels.** Version 1.0.0 asserted five and two did not survive contact with a proper search. Stating confidence makes the claims falsifiable and makes the audit re-runnable by someone else, which an unqualified list of assertions is not.

**The suite's contribution is restated as assembly, not mechanism.** Every individual pattern has a prior, catalogued in Part V. What was not found is the combination applied to this domain at this completeness. That is a real but modest claim, and it is the one the evidence supports.

**Tool risk is graded, and the grading rule is stated once.** Prefer tools whose output is a standard format. This is why DTCG adoption matters more than any tool choice downstream of it, and why the two highest-risk dependencies are acceptable — both hold regenerable data rather than authored work.

**One build is recommended and the rest are not.** Decision completeness — item 2 in Part VI — is small, high-value, and uses artifacts the suite already produces. Everything else in the gap register is either not automatable or not worth building against tools that may arrive. A gap register that recommends building six things is a wish list; one that recommends building one is a plan.
