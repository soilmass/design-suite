```yaml
document: Implementation
version: 1.0.3
tier: 2
owns:
  - what tokens must exist and what governs them
  - what every component must provide
  - how independence is built rather than intended
  - where each constraint is enforced
exports: T001–T084, K001–K083
depends:
  - Vocabulary ^1
  - Anatomy ^1
  - Composition ^1
  - Constraints ^1
reviewed: 2026-09-03
```

# Implementation

How a choice becomes a token, a component, and a check that fails the build.

**This document does not depend on Decision.** Both are tier 2, so citing it would be sideways and illegal under the architecture. The separation is real, not ceremonial: Decision says *set density to compact*; this document says *density is a single multiplier over the space scale, and here is what must exist for that to be true*. Neither needs to name the other.

**This document is a specification, not a theme.** T entries say what tokens must exist and what rules govern them, never what values they hold. Values are per-project, and putting them here would make the suite depend on one brand — the exact coupling Part IV exists to prevent.

---

## What this document owns

The buildable form of everything below it: token structure, component contracts, and the placement of every enforceable constraint.

## What it does not own

| Question | Owner |
|---|---|
| What does this term mean? | Vocabulary |
| What choices exist? | Composition |
| What may not be done? | Constraints |
| What should the value be? | Decision |
| How do I confirm it was built right? | Verification |

---

# PART I — TOKEN ARCHITECTURE

## T001 · Three tiers, one direction

**Primitive** — a raw value with no meaning. `color.blue.500`, `space.4`.
**Semantic** — a purpose, resolving to a primitive. `bg.surface.raised`, `text.muted`.
**Component** — a purpose scoped to one component, resolving to a semantic. `button.primary.bg`.

**References travel in one direction only: component → semantic → primitive.** No level skipping, no sideways references within a level, no cycles. This is the same rule the documents obey, for the same reason: a graph with cycles cannot be changed in one place.

This three-tier structure is established practice, not a derivation. It originated with the Salesforce design system team — who also coined the term "design token" — and is the shape used by Adobe Spectrum, Material, and most published systems. What is additive here is T080: nearly every system describes the reference direction and almost none enforce it.

## T002 · Naming grammar

`{category}.{concept}.{variant}.{scale}.{state}`

Category and concept are required; the rest appear only when they discriminate. State is always last and always a suffix, never infixed. Scales are named by value or by ordinal position, never by t-shirt size at the primitive tier — `space.4` survives an insertion, `space.md` does not.

## T003 · What gets a token

A value gets a token when it appears more than once **and** changing it should change every occurrence. A value appearing twice that should change independently is two hardcoded values, and tokenizing it creates a false coupling that is harder to find than a duplicate.

## T004 · Type annotation

Every token declares a type: `color`, `dimension`, `duration`, `cubicBezier`, `fontFamily`, `fontWeight`, `number`, `shadow`. Untyped tokens cannot be validated, transformed per platform, or checked for a category error like a duration used as a dimension.

**Use the DTCG format, version 2025.10.** The Design Tokens Community Group shipped its first stable specification on 28 October 2025, backed by more than forty organizations including Adobe, Figma, Google, Microsoft, Shopify, and Salesforce. Tokens carry `$value` and `$type` and reference each other by path, which is precisely the mechanism T001 requires and what makes semantic tokens portable between tools rather than tool-specific. Before it, every tool emitted a different JSON shape for the same value.

*Category first, tool second.* A token transformation pipeline turns the DTCG source into per-platform output. Style Dictionary has first-class DTCG support from v4, with full 2025.10 support in progress in v5; Terrazzo and Tokens Studio are the other established options. The format does not replace the pipeline — it makes the source file non-proprietary.

---

# PART II — REQUIRED TOKENS

*What must exist. Values are per-project.*

## Color

**T010 · Neutral ramp** — A stepped scale with monotonic lightness, authored in a perceptually uniform space. Steps carry assigned roles rather than positions on a gradient.
**T011 · Accent ramp** — Same structure as the neutral, so a hue swap is a value change rather than a restructure.
**T012 · Status ramps** — Success, warning, danger, info. Same structure again.
**T013 · Surface tokens** — One per elevation level, not one per color.
**T014 · Text tokens** — By prominence, not by color. `text.default`, `text.muted`, `text.inverse`.
**T015 · Border tokens** — By strength: subtle, default, strong.
**T016 · Focus ring token** — Satisfies C022 against **both** the element it surrounds and the background behind it, per A-058. A single ring color cannot do this on all surfaces; either a two-tone ring or a per-surface token is required.
**T017 · Overlay token** — For scrims and modal backdrops.
**T018 · Theme completeness** — Every semantic color token resolves in every theme. A missing value is a build failure, not a fallback.
**T019 · No raw color in components** — Components reference semantic tokens only. Enforced by lint, per K052.

## Space

**T020 · Space scale** — Hybrid progression, per A-036.
**T021 · Density multiplier** — One variable scaling the entire space scale. This is what makes comfortable and compact the same components rather than two sets. Bounded below by C028: the multiplier may not reduce any interactive target past the floor, which means targets are sized from their own token, not from padding alone.
**T022 · Gap tokens** — Distinct from inset tokens. Between-things and inside-things change independently.
**T023 · Measure token** — Line length, expressed in `ch`. Bounded by C004.

## Type

**T030 · Family tokens** — One per role: body, display, mono.
**T031 · Size scale** — Ordinal, with a rem component in every entry so browser zoom continues to work per C025.
**T032 · Line-height tokens** — Unitless, so they scale with size.
**T033 · Weight tokens** — Named by role, not by number, so a variable-font axis change does not rewrite every usage.
**T034 · Tracking tokens** — Expressed in em.
**T035 · Fallback metric overrides** — Required for every webfont family: `size-adjust`, `ascent-override`, `descent-override`, `line-gap-override`. This satisfies C104 and is the single highest-leverage token for layout stability.
**T036 · Feature settings** — At minimum a tabular-numerals token, applied to any number that changes in place.

## Radius and elevation

**T040 · Radius scale** — Ordinal.
**T041 · Nested radius derivation** — Inner radius is computed per A-026's nested-radius derivation, never authored as a second independent value. A function or a calc, not a literal token.
**T050 · Shadow tokens** — Composite, multi-layer, per A-028's layered-shadow construction. A single-layer shadow token guarantees the flat result described in Vocabulary V-233.
**T051 · Elevation is theme-aware** — Elevation resolves per A-029's light/dark split, encoded in the token layer so components never branch on theme.

## Motion

**T060 · Duration scale** — Ordinal, encoding A-043's distance-scaling relationship rather than leaving it to each usage.
**T061 · Easing set** — Named by role: entrance, exit, movement, emphasis.
**T062 · Reduced-motion counterpart** — Every motion token has a paired value for the reduced-motion path, drawn from A-052's substitution strategies — never zero across the board. Satisfies C036.

## Layout

**T070 · Breakpoint tokens** — In `em`, per A-041.
**T071 · Container width tokens**
**T072 · Z-index bands** — Named ranges per layer: base, raised, sticky, overlay, modal, popover, toast. Arbitrary integers in components are forbidden by K053.

## Governance of the token set

**T080 · Reference direction enforced** — A cycle or a skipped level fails the build.
**T081 · No orphans** — A primitive referenced by nothing is deleted, not kept in case.
**T082 · No aliasing across categories** — A space token may not reference a size token, however equal they look today.
**T083 · Deprecation before deletion** — A removed token is first marked deprecated with a successor, exactly as document IDs are.
**T084 · Token IDs are stable** — Renaming is free; reassigning meaning is not.

---

# PART III — COMPONENT REQUIREMENTS

## K001 · Native element first

A native element supplies name, role, value, state, keyboard behavior, and focus management free. A custom control supplies none of it and must implement all of it to satisfy C046. Building a custom control is a decision to write and maintain an accessibility implementation; it is not a styling decision, and it is routinely more work than the visual design that motivated it.

**Where a native element will not do, take a headless primitive rather than starting over.** Radix Primitives, Base UI, and React Aria each implement the C046 surface, keyboard behavior, and focus management that K004 and K011 also require, and leave styling entirely open. The copy-in model — vendoring primitives into your own repository rather than depending on a component library — is the established middle path and satisfies K060 better than either extreme. Declining these is a real decision with a real cost, and it should be made deliberately rather than by default.

## K002 · Required states

Every interactive component provides all of: rest, hover, focus-visible, active, disabled, loading. Every data-bearing component provides all of: empty, partial, full, error. A component missing any of these does not have a default for that state; it has an unmade decision that ships.

## K003 · Focus is separate from focus-visible

Rings are styled on `:focus-visible`, never on `:focus` alone. Satisfies C032 and prevents the removal that costs keyboard users the indicator entirely.

## K004 · Focus containment for overlays

Any component rendering over content traps focus while open, returns focus to its trigger on close, and closes on Escape. Satisfies C031 and C033.

## K005 · Target size is a component property

Interactive components size their hit area from a dedicated token, independent of visible dimensions. A 16px icon carries a compliant target through padding or a pseudo-element. Satisfies C028 and C082.

## K006 · Content tolerance

Every component renders correctly with: a 3-character string and a 90-character string in the same slot; a missing image; a null optional field; zero, one, seven, and ten thousand items in any collection; and strings containing characters the author did not anticipate.

## K007 · No fixed heights on text containers

Text expands under translation per C027 and under user spacing overrides. A container with a fixed height clips.

## K008 · API surface

Four channels, and the choice among them is the component's actual design:

**Props** — configuration with a bounded set of values. Variants, sizes, states.
**Slots** — arbitrary content the component positions but does not interpret.
**Tokens** — visual values, never passed as props. A `color` prop on a button reopens every decision the token layer closed.
**Context** — ambient concerns like theme, density, and direction. Never passed hand to hand through the tree.

## K009 · Leaf components contain no layout

A button has no margin. Spacing between components is the responsibility of whatever contains them. A component that positions itself cannot be reused, which is the placement coupling in Part IV.

## K010 · Overlays render through a portal

Escaping a stacking context by raising a z-index does not work, per Vocabulary V-064. Overlays render to a root-level container and take their band from T072.

## K011 · Controlled and uncontrolled

A component supporting internal state supports external control of the same state, with one clear default. Ambiguity here surfaces as a bug six months later in a form that needs to reset.

## K012 · Logical properties throughout

`margin-inline-start`, not `margin-left`. This is what makes RTL nearly free rather than a second layout.

<!-- vale Suite.RefusedTerms = NO --><!-- "accessible name" is WCAG's own defined term (V-469, C042), not the refused binary-adjective usage -->
## K013 · One accessible name per control

Provided by content, a label, or an explicit attribute — never by more than one at once, and never absent on an icon-only control.
<!-- vale Suite.RefusedTerms = YES -->

## K014 · Motion respects the reduced path

Every animated component reads the preference and takes the T062 counterpart. Satisfies C036.

## K015 · Loading is a state, not a wrapper

Components express loading internally rather than being replaced by a spinner. Replacement discards layout and causes the shift C105 describes.

## K016 · Errors state cause and next action

An error surface names what happened and what to do. Satisfies C040. "Something went wrong" satisfies neither half.

---

# PART IV — INDEPENDENCE AS BUILD RULES

*The axes a system must survive, expressed as things that can fail a build rather than things a team intends.*

## Brand independence

**K040 · No hardcoded visual values** — Color, spacing, radius, shadow, duration, and type values appear only in the token layer. Lint fails on a literal in a component.
**K041 · Font-swap survival** — Every family ships metric overrides per T035. A swap must not shift layout.
**K042 · Structural neutrality** — No component encodes a brand assumption in its structure. If a rebrand requires editing markup rather than tokens, the coupling is structural and the component is wrong.

## Content independence

**K043 · Slot tolerance** — Per K006, tested with fixtures rather than assumed.
**K044 · No content-shaped layout** — Grids and flex containers size from constraints, not from the content that happened to be there during design.
**K045 · Media reserves space** — Every image and embed declares dimensions or aspect ratio before load. Satisfies C105.

## Language independence

**K046 · No literals in components** — All user-facing strings resolve through the localization layer, including error text, empty-state copy, and `aria-label` values, which are the ones routinely missed.
**K047 · Formatting is delegated** — Dates, numbers, currency, and pluralization go through a formatter with a locale. Never string-concatenated.
**K048 · Expansion tolerance** — Layout survives a 35% increase in string length, verified by pseudo-localization rather than inspection.
**K049 · Direction independence** — Per K012, plus mirrored iconography for directional glyphs.

## Placement independence

*The axis systems skip, because the cost is invisible until enough components exist for the coupling to compound.*

**K050 · A component does not know its page** — No route checks, no page-name props, no conditional rendering by location.
**K051 · A component does not know its parent** — No assumptions about what contains it, its width, or its background. Container queries, not viewport queries, for anything that must adapt.
**K052 · A component does not know its siblings** — No first-child or last-child styling that assumes an order the consumer controls.
**K053 · No arbitrary z-index** — Bands only, per T072.
**K054 · Arbitrary nesting** — Components compose to any depth without special cases. If depth 3 needs a workaround, the boundary is drawn wrong.

## Input and capability independence

**K055 · Nothing hover-only** — Every hover-revealed affordance has a focus and touch equivalent.
**K056 · Nothing color-only** — Every state distinguished by color is also distinguished by shape, text, icon, or position. Satisfies C023.
**K057 · Keyboard parity** — Every pointer operation has a keyboard path, including drag, which requires a single-pointer alternative under C037.
**K058 · Zoom survival** — Usable at 400%, verified at a 320px equivalent width per C026.
**K059 · Forced-colors survival** — Components remain operable when author colors are replaced, which means borders and focus indicators may not be conveyed by background alone.

## Technical independence

**K060 · Tokens are plain values** — Serialized in a format with no framework dependency. This is what makes style-engine independence cheap while framework independence stays expensive.
**K061 · One-way component dependencies** — A shared component never imports from a feature. Enforced by a dependency-graph check.
**K062 · No browser storage assumptions in shared components** — State is passed in, not read from an environment the component cannot guarantee.

---

# PART V — CONSTRAINT ENFORCEMENT PLACEMENT

*Where each constraint is actually caught. The column that matters is the last one: anything not mechanically checkable needs a named human step, or it will not happen.*

<!-- vale Suite.RefusedTerms = NO --><!-- this table repeats each constraint's name verbatim, including C042 "Accessible auth" (WCAG's own criterion name); scoped to the whole table rather than one row to keep the table contiguous -->
| Constraint | Enforced at | Mechanism | Mechanical? |
|---|---|---|---|
| C020 Text contrast | Token layer | Ramp generation asserts pairings | Yes |
| C021 Enhanced contrast | Token layer | Same, higher threshold | Yes |
| C022 Non-text contrast | Token layer, T016 | Focus and border token assertions | Yes |
| C023 Color not alone | Component, K056 | Review; partial lint on state styling | Partial |
| C024 Text alternatives | Component, K013 | Lint for missing alt and name | Yes |
| C025 Resize text | Token layer, T031 | Lint for rem-free sizes | Yes |
| C026 Reflow | Build, K058 | Automated 320px-equivalent render | Yes |
| C027 Text spacing | Component, K007 | Automated override injection | Yes |
| C028 Target size | Token, T021 · Component, K005 | Computed-size assertion | Yes |
| C030 Keyboard operability | Component, K001 | Partial automation; manual pass required | Partial |
| C031 No keyboard trap | Component, K004 | Focus-cycle test | Yes |
| C032 Focus visible | Component, K003 | Lint for outline removal | Yes |
| C033 Focus not obscured | Integration | Scroll-and-focus test with sticky chrome | Partial |
| C034 Flash threshold | Content review | Human | No |
| C035 Pause, stop, hide | Component | Review | No |
| C036 Reduced motion | Token, T062 · Component, K014 | Lint for unpaired motion tokens | Yes |
| C037 Dragging alternative | Component, K057 | Review | No |
| C038 Focus order | Component, K009 | Partial; DOM-vs-visual comparison | Partial |
| C039 Labels | Component, K013 | Lint | Yes |
| C040 Error identification | Component, K016 | Review | No |
| C041 Redundant entry | Flow level | Review | No |
| C042 Accessible auth | Flow level | Review | No |
| C043 Consistent navigation | System level | Review | No |
| C044 Page titled | Route layer | Lint | Yes |
| C045 Page language | Document shell | Lint | Yes |
| C046 Name, role, value | Component, K001 | Automated audit plus manual AT pass | Partial |
| C080 iOS input zoom | Token, T031 | Assert input size floor | Yes |
| C081 Email rendering | Separate token export | Build target check | Yes |
| C104 Font swap shift | Token, T035 | Assert overrides exist per family | Yes |
| C105 Unsized media | Component, K045 | Lint for missing dimensions | Yes |
| C120 Web Vitals | CI | Lab and field measurement | Yes |
| C121–C124 Budgets | CI | Build-size assertion | Yes |
<!-- vale Suite.RefusedTerms = YES -->

## K070 · The partial and no rows are the whole problem

Twenty-two of the constraints above are mechanically enforceable and will hold. Ten are partial or manual and will not hold unless someone owns them by name and runs them on a stated cadence. A system that automates the twenty-two and leaves the ten to good intentions will pass every check it runs and fail the people the constraints exist for.

The manual set is small enough to list on one page. Do that, assign it, and schedule it. Verification owns what that check looks like.

---

# PART VI — STRUCTURE

## K079 · Tool names are the most volatile content here

Every tool named in this document should be rechecked semi-annually. Where a sentence names one, it names the category first so the sentence survives the tool being replaced. Naming a tool is not adopting a practice: the tool performs the mechanism, and the discipline around it — ownership, cadence, threshold — is what this document actually specifies.

## K080 · One token source, many outputs

Tokens are authored once and transformed per target: CSS custom properties for web, a flat stylesheet for email per C081, and whatever native targets exist. Authoring per-platform guarantees divergence.

## K081 · Layout primitives are separate from content components

Stack, grid, cluster, and container are their own layer. This is what makes K009 possible: components contain no layout because layout components exist to hold them.

## K082 · Feature components may import shared; never the reverse

Per K061, enforced by dependency graph rather than convention.

## K083 · Component documentation states its API and its states

Props, slots, tokens consumed, and every state from K002 rendered. A component whose empty and error states are undocumented has them undesigned.

---

## Settled decisions

**Implementation specifies structure, never values.** Putting a palette here would couple the suite to one brand and make every rule in Part IV unenforceable by the document that defines them. T entries therefore say "a neutral ramp with assigned step roles must exist," not what its steps are.

**Density is one multiplier, not a second component set.** T021 makes comfortable and compact the same components. The alternative — parallel sets — doubles the surface for every subsequent change and is the most common cause of a system that works until the second density arrives.

**Elevation is theme-aware at the token layer, not the component layer.** T051 places A-029's light/dark split inside the token so components never branch on theme, rather than leaving that split to be discovered late, once re-authoring every surface is expensive.

**Part V's manual rows are stated as a liability rather than a footnote.** K070 exists because enforcement tables are usually read as reassurance. Ten unenforceable constraints out of thirty-two is the actual state, and a document that presents the twenty-two automated ones without naming the remainder is misleading about what the system guarantees.
