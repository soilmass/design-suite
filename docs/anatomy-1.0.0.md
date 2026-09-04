```yaml
document: Anatomy
version: 1.9.0
tier: 1
scope: rendering primitives (color, typography, shape, space, motion, imagery, state), plus a first slice of component anatomy, plus input controls, plus menus, plus a first information-architecture slice, plus content elements, plus message surfaces, plus badges and chips, plus avatars, progress and spinner, skeleton, empty/zero state, carousel, lightbox, and toolbar, plus link, table, data grid, disclosure, accordion, and infinite scroll — completing Vocabulary's `H · Components` part
owns:
  - what each thing is made of, expressed as parameters
  - the range or type of each parameter
  - what is derived rather than chosen
exports: A-001–A-111
depends:
  - Vocabulary ^1
  - Constraints ^1
reviewed: 2026-09-03
```

# Anatomy

What each thing is made of. Where Vocabulary establishes what a term denotes, this document takes the thing apart: the parameters it consists of, what values those accept, what it composes into, and what can be derived rather than chosen.

**Scope of 1.1.0** — rendering primitives, plus a first slice of component anatomy: Button, Card, Tooltip/Popover, Dialog, and Tabs (A-062–A-066). The rest of components, tokens, information architecture, and content are not yet covered; they enter as additive minor versions with new A-IDs.

**Scope of 1.2.0** — adds a second slice of component anatomy, input controls: Text input, Checkbox, Radio group, Switch, Select and combobox, Slider, Stepper, Segmented control, Dropzone, and Fieldset (A-067–A-076). Menus, toasts and banners, badges and chips, avatars, and the rest of Vocabulary's `H · Components` part remain open; see **Settled decisions**.

**Scope of 1.3.0** — adds a third slice of component anatomy, the menu family: Menu, covering dropdown menu and context menu, and Command palette (A-077–A-078). Toasts and banners, callouts, badges and chips, avatars, breadcrumb and pagination, progress and spinner, skeleton and empty/zero state, facets, carousel, lightbox, toolbar, and hamburger menu remain open; see **Settled decisions**. This version also closes tokens as a settled out-of-scope finding rather than a deferral — see **Settled decisions**.

**Scope of 1.3.1** — no new A-IDs. Closes the other two scoping questions the first Settled decisions entry above left open, the same way 1.3.0 closed tokens: content and information architecture are each resolved to an organizing shape — see **Settled decisions**. Both remain uncovered by any A-ID; what changes is that a future contribution now has a settled shape to draft into rather than an open scoping discussion.

**Scope of 1.4.0** — adds a fourth slice of component anatomy, the first drawn from information architecture rather than from Vocabulary's `H · Components` part: Breadcrumb, Pagination, Facets, Navigation (folding global, local, and utility navigation, plus hamburger menu as a sub-part), and Skip link (A-079–A-083). This is the full candidate set the 1.3.1 information-architecture scoping resolution named; see **Settled decisions**. Toasts and banners, callouts, badges and chips, avatars, progress and spinner, skeleton and empty/zero state, carousel, lightbox, and toolbar remain open in the `H` part, and content elements remain the other settled-but-undrafted slice.

**Scope of 1.5.0** — adds a fifth slice, the first drawn from Vocabulary's `L · Content and language` part rather than from `H · Components`: content elements — Headline, Deck, Eyebrow, Byline, Body, Pull-quote, Stat/callout, Caption, CTA text, List, and Metadata block (A-084–A-094). This is the full candidate set the 1.3.1 content scoping resolution named; see **Settled decisions**. Closing this slice required a small companion Vocabulary addition — eight of the eleven candidates had no term at all, and a ninth ("stat") had only a partial match — recorded as V-613–V-621 in Vocabulary's own changelog, not restated here beyond the citations the entries below make. Toasts and banners, callouts, badges and chips, avatars, progress and spinner, skeleton and empty/zero state, carousel, lightbox, and toolbar remain the only open names, all in the `H` part; content is now fully drafted.

**Scope of 1.6.0** — adds a sixth slice, message surfaces: Toast and banner (A-095, folding V-346 and V-347 into one entry) and Callout (A-096, the `H`-part, severity-keyed sense of the term the 1.5.0 Settled decisions flagged as still open, distinct from A-090 Stat/callout's content-element sense of the same V-348). This is the fold-or-separate decision that note left for a future contribution to make. A re-verification against Vocabulary's `H` part, done while scoping this slice, found six names — Link, Table, Data grid, Accordion, Disclosure, and Infinite scroll — cited nowhere in this document and named in none of its prior "still open" notes; they join badges and chips, avatars, progress and spinner, skeleton and empty/zero state, carousel, lightbox, and toolbar as the seventeen names now tracked as open in the `H` part, correcting `ROADMAP.md`'s prior "~23" estimate to a verified count. See **Settled decisions** for both.

**Scope of 1.7.0** — adds a seventh slice, badges and chips: Badge (A-097) and Chip (A-098), both already partially characterized by A-096's own "Not folded with Badge or Chip" paragraph. Avatars, progress and spinner, skeleton and empty/zero state, carousel, lightbox, and toolbar remain open in the `H` part, alongside Link, Table, Data grid, Accordion, Disclosure, and Infinite scroll — the six names issue #48 surfaced, each still awaiting a human scoping call before it can be drafted. Fifteen names remain open in total. See **Settled decisions**.

**Scope of 1.8.0** — adds an eighth slice, the six names Phase 2 flagged as ready to draft without a human scoping call: Avatar (A-099), Progress and spinner (A-100, folding V-355 and V-356 into one entry), Skeleton (A-101), Empty and zero state (A-102, folding V-358 and V-359 into one entry), Carousel (A-103), Lightbox (A-104), and Toolbar (A-105) — seven entries covering nine of Vocabulary's `H` names. All nine already had Vocabulary IDs before this slice; none required a companion Vocabulary addition. Only Link, Table, Data grid, Accordion, Disclosure, and Infinite scroll — the six names issue #48 surfaced — remain open in the `H` part; see **Scope of 1.8.1** below for their scoping call. See **Settled decisions**.

**Scope of 1.8.1** — no new A-IDs. Resolves the scoping call issue #48 reserved for Link, Table, Data grid, Accordion, Disclosure, and Infinite scroll, which the issue's own closure left unmade: Link stands alone; Data grid stays separate from and extends Table rather than folding with it; Accordion composes from Disclosure rather than folding with it; Infinite scroll stands alone, reusing Progress and spinner's indeterminate construction. See **Settled decisions**. The six names remain undrafted — this entry settles their shape, not their anatomy.

**Scope of 1.9.0** — adds a ninth slice, the last six names in Vocabulary's `H · Components` part: Link (A-106), Table (A-107), Data grid (A-108), Disclosure (A-109), Accordion (A-110), and Infinite scroll (A-111). This is the full six-name set the 1.8.1 scoping resolution reserved, drafted to the shape that resolution already settled — none of its four calls (Link standalone; Data grid separate from and extending Table; Accordion composing from Disclosure; Infinite scroll standalone, reusing Progress and spinner's indeterminate construction) is reopened here. Vocabulary's `H · Components` part (V-310–V-364, 55 names) is now fully covered by this document; no component name remains open for a future Anatomy volume-2 slice. See **Settled decisions**.

## What this document does not own

| Question | Owner |
|---|---|
| What does this term mean? | Vocabulary |
| What may this parameter not be? | Constraints |
| What choices does it present? | Composition |
| What should it be set to? | Decision |
| How is it built? | Implementation |

Where a parameter has a floor, this document cites the constraint rather than restating its value.

---

## How to read this

Each entry follows the same shape:

> **Term**
> `param` · `param` · `param` — the irreducible controls
> **Ranges** — what each accepts
> **Composed of / composes into** — its position in the hierarchy
> **Derived** — values you can calculate rather than choose
> **Breaks when** — the specific failure

Not every entry needs every line. A parameter is listed only if changing it changes the result.

---

# A. Color

## A-001 · The color value

A color is never one thing. It is a set of coordinates plus the space those coordinates are read in.

### A-002 · sRGB
`r` · `g` · `b` · `alpha`
**Ranges** — each channel 0–255, or 0–1 normalized, or `00`–`ff` in hex. Alpha 0–1.
**Note** — Device-referred, not perceptual. Numerically equal steps produce unequal visual steps.

### A-003 · HSL
`hue` · `saturation` · `lightness` · `alpha`
**Ranges** — hue 0–360 (an angle, wraps), saturation 0–100%, lightness 0–100%.
**Breaks when** — you assume equal lightness means equal appearance. `hsl(60 100% 50%)` (yellow) and `hsl(240 100% 50%)` (blue) are both "50% light" and differ in perceived brightness by roughly a factor of five.

### A-004 · OKLCH
`lightness` · `chroma` · `hue` · `alpha`
**Ranges** — L 0–1 (0 black, 1 white), C 0 to about 0.37 depending on hue and gamut, H 0–360.
**Why it matters** — Perceptually uniform. Holding L constant across hues produces colors of genuinely equal apparent lightness, which is what makes a coherent palette possible.
**Breaks when** — you request a chroma the display can't produce; the browser gamut-maps it and the result differs from the number you wrote.

### A-005 · OKLab
`L` · `a` · `b` · `alpha`
**Ranges** — L 0–1, a and b roughly −0.4 to 0.4. Cartesian form of OKLCH; a is green–red, b is blue–yellow.
**Use** — Interpolation and mixing. OKLCH is better for picking, OKLab for blending.

### A-006 · Display P3
Same channel structure as sRGB, wider primaries. About 25% more coverage, concentrated in reds and greens.
**Composed of** — a color space definition (primaries + white point + transfer function).

---

## A-007 · Color components

### A-008 · Hue
`angle`
**Ranges** — 0–360, cyclic. Roughly: 0 red, 30 orange, 60 yellow, 120 green, 180 cyan, 240 blue, 300 magenta.
**Sub-parts** — hue in HSL and hue in OKLCH are *not the same angle*. OKLCH hue is perceptually corrected, so a given number lands on a different visible color.
**Derived** — temperature (warm 0–90 and 270–360; cool 90–270), though this is convention rather than physics.

### A-009 · Chroma / saturation
**Chroma** — absolute colorfulness. Unbounded in principle, gamut-limited in practice, and the ceiling *varies by hue and lightness*. Yellows reach high chroma only at high lightness; blues only at low.
**Saturation** — colorfulness relative to the maximum possible at that lightness. Normalized 0–100%.
**Consequence** — a "saturation" slider hides the fact that the achievable maximum moves. A chroma slider does not, which is why chroma is harder to use and produces better results.

### A-010 · Lightness vs luminance vs brightness
**Lightness (L)** — perceptual, 0–1, what OKLCH reports.
**Relative luminance (Y)** — physical, computed as `0.2126·R + 0.7152·G + 0.0722·B` on linearized channels. Green carries most of it; blue almost none.
**Brightness** — the subjective sensation, affected by surround, adaptation, and size.
**Breaks when** — these three are used interchangeably. Contrast math needs luminance; palette construction needs lightness.

### A-011 · Alpha
`opacity value`
**Ranges** — 0–1.
**Composed into** — `result = source·α + backdrop·(1−α)` per channel, over the linearized values.
**Distinction** — `opacity` on an element applies to the element *and all descendants as a group*, creating a stacking context. Alpha in a color value applies to that one paint operation only.

---

## A-012 · Gradient

`type` · `geometry` · `stops[]` · `interpolation space` · `hue method` · `repeat`

**Type** — linear, radial, conic.
**Geometry**
- linear: `angle` (0–360) or `to <side/corner>`
- radial: `shape` (circle/ellipse) · `size` (closest-side, closest-corner, farthest-side, farthest-corner, explicit) · `position` (x, y)
- conic: `from <angle>` · `at <position>`

**Stop** — the atom of a gradient.
`color` · `position` (0–100% or length) · optional `midpoint hint`
A stop with two positions creates a hard band. Two identical positions create a hard edge.

**Interpolation space** — `in oklab`, `in srgb`, `in hsl`, and so on. Determines the path taken between stops.
**Hue interpolation method** — `shorter`, `longer`, `increasing`, `decreasing`. Only meaningful in polar spaces. Controls which way around the wheel the transition travels.

**Derived** — the midpoint color. In sRGB, blue→yellow passes through gray. In OKLab, it passes through the colors you expected.
**Breaks when** — banding. Caused by 8-bit quantization across a long, low-contrast run. Fixed with noise, not with more stops.

### A-013 · Mesh gradient
`points[]` (each with `position x,y` · `color` · `influence radius`) · `resolution` · `interpolation`
Not native CSS. Implemented as layered radial gradients, an SVG filter chain, or a shader.

---

## A-014 · Color scale (ramp)

`hue` · `step count` · `lightness curve` · `chroma curve` · `step roles`

**Step count** — commonly 10, 11, or 12. Twelve is the Radix convention and maps cleanly onto roles.
**Lightness curve** — the L value at each step. Rarely linear; usually eased so the light end has finer gradations.
**Chroma curve** — the C value at each step. Typically an arc peaking in the middle, since chroma is unattainable at both extremes.
**Hue shift** — optional. Small rotations across the ramp (blues cooling as they darken) prevent the scale looking mechanical.

**Step roles** (the 12-step model)
1–2 app and subtle backgrounds · 3–5 component backgrounds at rest, hover, active · 6–8 borders, from subtle to strong · 9 the solid brand fill · 10 its hover · 11–12 text, low and high contrast.

**Derived** — every accessible pairing. In a well-built scale, the text steps clear C020 against the background steps automatically, in every hue.
**Breaks when** — the ramp is built by mixing with white and black in sRGB. Chroma collapses at the ends and the mid-steps go muddy.

---

## A-015 · Contrast

`foreground luminance` · `background luminance`
**Formula** — `(L_lighter + 0.05) / (L_darker + 0.05)`, yielding 1:1 to 21:1.
**Thresholds** — owned by Constraints: C020, C021, C022. Not restated here.

**APCA** — the alternative model.
`text luminance` · `background luminance` · `polarity` · `font size` · `font weight`
Outputs Lc, roughly −108 to +106. Polarity-aware, so it doesn't report light-on-dark and dark-on-light as equivalent when they aren't.

**Breaks when** — contrast is measured against the wrong backdrop. Text over a gradient, an image, or a translucent surface has no single background luminance.

---

## A-016 · Blend mode

`source` · `backdrop` · `formula` · `isolation group`
**Separable modes** — normal, multiply, screen, overlay, darken, lighten, color-dodge, color-burn, hard-light, soft-light, difference, exclusion. Applied per channel.
**Non-separable modes** — hue, saturation, color, luminosity. Operate on the color as a whole.
**Isolation** — `isolation: isolate` confines blending to a group, stopping it reaching the page background.

---

## A-017 · Dark theme

Not an inversion. A set of coordinated transformations:
`lightness curve inverted` · `chroma reduced 10–30%` · `elevation cue flipped` · `shadow weakened` · `pure black avoided` · `border prominence increased`

**Why chroma drops** — saturated color on dark backgrounds vibrates and appears to glow.
**Why elevation flips** — shadow is nearly invisible on dark surfaces, so raised elements get *lighter* instead.
**Why not #000** — maximum contrast against white text causes halation, particularly for astigmatic readers. Something around #0A0A0B to #18181B is standard.

---

# B. Typography

## A-018 · Glyph anatomy

The parts of a letterform, roughly outside-in:

`stem` — the main vertical stroke
`bar / crossbar` — the horizontal stroke in A, H, e
`bowl` — a curve enclosing space, as in b, d, o
`counter` — the enclosed space itself
`aperture` — the opening of a partially closed counter, as in c, e, s
`shoulder` — the curve springing from a stem, as in h, m, n
`arm` — a horizontal or upward stroke free at one end, as in E, K
`leg` — a downward stroke free at one end, as in K, R
`tail` — a descending stroke, as in Q, y
`spine` — the central curve of an S
`ear` — the small projection on a lowercase g
`link / loop` — the connector and lower bowl of a double-storey g
`spur` — the small projection at the base of a G
`serif` — the terminating stroke, itself divided into bracketed, unbracketed, slab, hairline, wedge
`terminal` — the end of a stroke without a serif: ball, teardrop, sheared, flat
`apex / vertex` — the top and bottom join of a pointed letter, as in A and V
`crotch` — the interior angle where strokes meet
`finial` — a tapered terminal
`swash` — an extended decorative stroke
`overshoot` — the amount round letters exceed the baseline and cap height so they appear the same size

---

## A-019 · Font metrics

`units per em` · `ascent` · `descent` · `line gap` · `cap height` · `x-height` · `advance width` · `left sidebearing` · `right sidebearing`

**Units per em** — the design grid, usually 1000 (PostScript) or 2048 (TrueType). All other metrics are expressed in these units.
**Ascent + descent + line gap** — determines the default line box height, and therefore what `line-height: normal` produces. This varies by font, which is why switching typefaces shifts your vertical rhythm.
**Advance width** — the horizontal distance the cursor moves after setting a glyph.
**Sidebearings** — the built-in space each side of a glyph. Tracking adds to these uniformly; kerning adjusts specific pairs.

**Derived** — apparent size. Two fonts at 16px look different sizes because their x-height to em ratio differs, commonly between 0.45 and 0.55.

---

## A-020 · Variable font axes

`tag` · `min` · `default` · `max` · `current value`

**Registered axes**
`wght` weight, 1–1000, default 400
`wdth` width, percentage of normal, default 100
`opsz` optical size, in points, usually 6–144
`ital` italic, 0 or 1, a discrete switch
`slnt` slant, degrees, typically −20 to 0

**Custom axes** — uppercase tags by convention (`GRAD`, `XTRA`, `YOPQ`, `CASL`, `MONO`). Defined per family.

**Composed into** — an instance. A named instance is a coordinate the designer labeled; you are free to use any coordinate between.
**Breaks when** — animating an axis and assuming it interpolates cheaply. Some axes trigger re-layout on every frame.

---

## A-021 · The text block

`font-family` · `font-size` · `font-weight` · `font-style` · `line-height` · `letter-spacing` · `word-spacing` · `text-align` · `text-indent` · `hyphens` · `text-wrap` · `max-width` · `font-feature-settings` · `font-variation-settings`

**font-size** — px, rem, em, or `clamp()`. Rem for anything that should respond to user preference.
**line-height** — accepts a unitless multiplier, a length, or a percentage. Unitless resolves against the element's own font size; length and percentage resolve once and are inherited as computed values, which is why they behave differently under nesting.
**Inverse relationship** — as size increases, line-height should decrease; as measure increases, line-height should increase.
**letter-spacing** — em units. Negative for large display text (−0.01 to −0.03em), positive for uppercase and small text (+0.02 to +0.1em).
**measure** — expressed in `ch` units or a max-width, bounded by C004.
**text-wrap** — `balance` for headings up to about six lines, `pretty` for body copy, `stable` for content that updates in place.

---

## A-022 · Type scale

`base size` · `ratio` · `step count` · `rounding rule` · `fluid range`

**Ratio** — 1.125 major second, 1.2 minor third, 1.25 major third, 1.333 perfect fourth, 1.414 augmented fourth, 1.5 perfect fifth, 1.618 golden.
**Derived** — `size(n) = base × ratio^n`.
**Rounding** — to whole pixels, or to the nearest 0.25rem. Unrounded scales produce values like 23.7px that render inconsistently.

**Fluid step**
`min size` · `max size` · `min viewport` · `max viewport`
**Derived slope** — `(maxSize − minSize) / (maxVw − minVw)`, giving `clamp(minSize, intercept + slope·100vw, maxSize)`.
**Breaks when** — the preferred term has no rem component. Text then ignores browser zoom entirely, which is an accessibility failure.

---

## A-023 · OpenType features

`tag` · `on/off or value`

`liga` standard ligatures · `dlig` discretionary · `calt` contextual alternates
`kern` kerning · `smcp` small caps · `c2sc` caps to small caps
`tnum` tabular figures · `pnum` proportional · `lnum` lining · `onum` oldstyle
`frac` fractions · `ordn` ordinals · `zero` slashed zero
`ss01`–`ss20` stylistic sets · `salt` stylistic alternates
`case` case-sensitive forms — raises punctuation to suit uppercase

**Effect** — `tnum` equalizes numeral advance widths, so a number changing in place does not reflow its container.

---

## A-024 · Font loading

`format` · `unicode-range` · `font-display` · `preload` · `size-adjust` · `ascent-override` · `descent-override` · `line-gap-override`

**format** — woff2 almost always. Roughly 30% smaller than woff.
**unicode-range** — splits a font into subsets loaded only when those characters appear.
**font-display** — `auto` · `block` (up to 3s invisible) · `swap` (fallback immediately, swap when ready) · `fallback` (100ms block, 3s swap window) · `optional` (100ms block, then never swap this visit).
**Metric overrides** — adjust a *fallback* font's metrics to match the webfont, so the swap causes no layout shift.

**Derived** — CLS contribution. A swap without metric overrides typically shifts every line below it.

---

# C. Shape, Surface, and Depth

## A-025 · The box

`width` · `height` · `padding (4)` · `border (4 × width/style/color)` · `margin (4)` · `box-sizing`

**Sizing keywords** — `min-content` (narrowest without overflow) · `max-content` (natural width, no wrapping) · `fit-content` (max-content clamped to available) · `stretch`.
**Logical equivalents** — `inline-size`, `block-size`, `padding-inline`, `margin-block`. These follow writing direction, so one declaration serves LTR and RTL both.

---

## A-026 · Corner

`top-left` · `top-right` · `bottom-right` · `bottom-left`, each with `horizontal radius` and `vertical radius` — eight values total.

**Elliptical corners** — `border-radius: 30px / 60px` sets differing horizontal and vertical radii, producing an ellipse quadrant rather than a circle quadrant.

**Superellipse (squircle)**
`a` · `b` · `n`
**Formula** — `|x/a|^n + |y/b|^n = 1`
**Ranges** — n = 2 is a perfect ellipse; n → ∞ approaches a rectangle; Apple's corner sits near n ≈ 4–5.
**Corner smoothing** — 0% is a circular arc, 100% is full continuous curvature. Figma exposes this directly; on the web it requires an SVG path, a mask, or `corner-shape` where supported.

**Continuity classes** — G0 positions meet · G1 tangents match · G2 curvature matches. A circular corner is G1: the curvature jumps instantly from zero to 1/r at the join, and the eye registers that discontinuity as a slight hardness even when it can't name it. A squircle is G2.

**Nested radius**
**Derived** — `inner = outer − gap`. If the gap between an outer container and inner element is 12px and the outer radius is 16px, the inner radius is 4px.
**Breaks when** — inner and outer radii are equal. The gap then appears to swell at the corners.

---

## A-027 · Stroke

`width` · `style` · `color` · `alignment` · `dash array` · `dash offset` · `linecap` · `linejoin` · `miter limit`

**Alignment** — inside, center, outside. CSS borders are effectively outside the padding box only; SVG strokes are centered by default. This is why a 1px CSS border and a 1px SVG stroke at the same nominal position don't line up.
**linecap** — butt, round, square.
**linejoin** — miter, round, bevel.
**miter limit** — the ratio at which a sharp miter is cut off to a bevel. Default 4.
**dash array** — alternating dash and gap lengths. `dashoffset` shifts the pattern along the path, which is how draw-on animations work.

**Derived** — a hairline. `1px` at DPR 2 renders as two device pixels; `0.5px` gives a true single-device-pixel line on those displays.

---

## A-028 · Shadow

`offset-x` · `offset-y` · `blur-radius` · `spread` · `color` · `alpha` · `inset`

**Ranges** — offsets any length, blur ≥ 0, spread positive or negative.
**Derived from physics**
- light source *angle* → the ratio of offset-x to offset-y
- light source *size* → blur radius. A point source gives a hard edge; a large source gives a soft one.
- occluder *distance* from the surface → both offset and blur increase together
- occluder *size* → spread

**Blur to sigma** — `box-shadow` blur radius is approximately 2σ of the Gaussian. `filter: blur(N)` sets σ = N directly. The same numeric value therefore produces a visibly different softness in each.

**Layered shadow** — the realistic construction. Three components:
- *contact* — near-zero offset, small blur, higher alpha. The dark line where the object meets the surface.
- *key* — directional offset, medium blur, medium alpha. The cast shadow.
- *ambient* — no or minimal offset, large blur, low alpha. Diffuse environmental occlusion.

A practical recipe stacks 3–6 shadows where blur roughly doubles at each layer and alpha roughly halves.

**Breaks when** — one shadow, high alpha, uniform blur. Reads as a sticker rather than an object.
**Also breaks when** — the shadow is pure black. Real shadows take a hue from the surface and the ambient light; a desaturated, slightly hue-shifted dark color reads correctly where `rgba(0,0,0,0.2)` reads gray and dead.

---

## A-029 · Elevation

`level` · `shadow set` · `surface color` · `border` · `z-index band` · `blur amount`

A level is a *bundle*, not a number. Typical five-level system: 0 flush, 1 raised card, 2 dropdown, 3 dialog, 4 toast.
**Light theme** — shadow carries the signal, surface stays constant.
**Dark theme** — surface lightness carries the signal, shadow does almost nothing. Roughly +2 to +4% lightness per level.
**Breaks when** — a system defines elevation only as shadow, then ships dark mode.

---

## A-030 · Blur

`type` · `radius/sigma` · `edge behavior`

**Types** — gaussian (`filter: blur()`) · backdrop (`backdrop-filter: blur()`) · directional/motion (SVG filter) · radial (composite).
**Edge behavior** — CSS blur samples transparent pixels outside the element, so edges fade. Clipping or a slight scale-up hides this.
**Cost** — backdrop blur is among the most expensive operations available, and repaints on every scroll frame over changing content.

---

## A-031 · Glass surface

`backdrop blur` · `backdrop saturation` · `fill color + alpha` · `border highlight` · `inner shadow` · `outer shadow` · `noise`

The full construction, in order: blur what's behind (10–40px), boost its saturation (150–200%, because blurring desaturates), lay a translucent fill (5–20% white or black), add a 1px highlight border brighter on the top edge, add a subtle inner shadow at the bottom, add an outer shadow to lift it, and add faint noise to suppress banding.
**Breaks when** — any layer is omitted. Blur plus fill alone reads as a smudge.

---

## A-032 · Fill

`type` · `value` · `origin` · `size` · `position` · `repeat` · `attachment` · `clip` · `blend mode`
**Types** — solid color, gradient, image, pattern, or several layered. Later declarations sit *beneath* earlier ones in `background` shorthand, which reverses the intuition.

---

## A-033 · Mask and clip

**Clip path** — `shape` · `reference box` · `fill rule`
Shapes: `inset()`, `circle()`, `ellipse()`, `polygon()`, `path()`, `url(#id)`. Hard-edged, binary.

**Mask** — `image` · `mode` (alpha or luminance) · `position` · `size` · `repeat` · `composite`
Soft-edged. A gradient mask produces a fade; a luminance mask uses brightness as the alpha channel. This is how scroll fades and text-reveal effects are built.

---

## A-034 · Noise and grain

`type` · `frequency` · `octaves` · `amplitude` · `monochrome` · `blend mode` · `opacity` · `scale`

**Types** — white (uncorrelated, harsh) · blue (high-frequency only, visually even, best for dithering) · value/Perlin (smooth, correlated) · simplex (Perlin's faster successor) · fBm (fractional Brownian motion, layered octaves).
**Octaves** — number of noise layers summed, each at doubled frequency and halved amplitude. More octaves means more detail.
**Implementation** — `feTurbulence` in SVG with `baseFrequency` and `numOctaves`, a repeated PNG, or a shader.
**Parameter ranges** — `baseFrequency` accepts 0 to 1, where higher values produce finer grain. Opacity and blend mode determine whether the result reads as surface texture or as signal.

---

## A-035 · Pattern

`motif` · `tile dimensions` · `repeat mode` · `offset` · `rotation` · `scale` · `color count` · `symmetry group` · `density`

**Repeat mode** — grid (aligned), brick/half-drop (offset by half a tile each row or column), mirror, random rotation.
**Symmetry group** — one of the 17 wallpaper groups. Determines which reflections, rotations, and glides the pattern possesses. p1 is pure translation; p4m is the four-fold mirrored structure most tilework uses.
**Truchet tile** — `tile set` · `rotation states` (usually 4) · `selection rule` (random or seeded). One asymmetric tile plus random rotation produces apparently non-repeating complexity.
**Seamlessness** — requires that the motif crossing each edge continues exactly at the opposite edge. The standard test is offsetting the tile by half its dimensions and checking the newly exposed seam.
**Derived** — apparent density = motif area / tile area.

---

# D. Space and Layout

## A-036 · Spacing scale

`base unit` · `progression` · `step count` · `naming scheme`

**Base unit** — 4px is the common atom, 8px the common increment.
**Progression** — linear (4, 8, 12, 16, 20…), doubling (4, 8, 16, 32, 64), or hybrid: dense at the low end where UI needs precision, geometric at the high end where layout needs range. The hybrid is what most mature systems converge on: 2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128.
**Naming** — numeric by value (`space-16`), numeric by index (`space-4`), or t-shirt (`space-md`). Value-based scales survive insertions; index-based ones don't.

**Derived** — the relationship between spacing and type. If line-height is 1.5 at 16px, the line box is 24px, and spacing values that are multiples of 24 keep vertical rhythm intact.

---

## A-037 · Grid

`columns` · `rows` · `column-gap` · `row-gap` · `template areas` · `auto-flow` · `auto-columns` · `auto-rows` · alignment set

**Track sizing functions** — `<length>` · `<percentage>` · `fr` · `min-content` · `max-content` · `auto` · `fit-content(n)` · `minmax(min, max)` · `repeat(count | auto-fill | auto-fit, ...)`

**A responsive-track pattern** composes three of the track-sizing functions above: `repeat()`'s `auto-fit` keyword collapses empty tracks so items stretch to fill the row, `minmax()` sets a floor below which a track will not shrink and a ceiling it may grow toward, and wrapping that floor in `min()` against the available width keeps a track from overflowing a container narrower than the floor. The floor value itself, and whether to use `auto-fit` or `auto-fill`, are choices with a range and a decision behind them, not a fact this document fixes.

**auto-fill vs auto-fit** — fill keeps empty tracks; fit collapses them. Identical when items fill the row, visibly different when they don't.

**Alignment — six properties on two axes**
Inline axis: `justify-items` · `justify-content` · `justify-self`
Block axis: `align-items` · `align-content` · `align-self`
`-items` sets the default for all children · `-self` overrides one child · `-content` distributes the tracks themselves within the container.
**Values** — start, end, center, stretch, baseline, space-between, space-around, space-evenly.

**auto-flow: dense** — backfills earlier gaps with later items. Reorders visually but not in the DOM, which breaks tab order.

---

## A-038 · Flex

`direction` · `wrap` · `justify-content` · `align-items` · `align-content` · `gap` · and per item `grow` · `shrink` · `basis` · `align-self` · `order`

**flex shorthand** — `flex: <grow> <shrink> <basis>`.
`flex: 1` = `1 1 0%` — all items equal width regardless of content
`flex: auto` = `1 1 auto` — items sized by content, sharing extra space
`flex: none` = `0 0 auto` — fixed to content

**Derived distribution** — free space is distributed in proportion to grow values; overflow is removed in proportion to shrink values *weighted by basis*.

**The overflow gotcha** — flex items default to `min-width: auto`, meaning they refuse to shrink below content size. Long strings and tables blow out layouts until `min-width: 0` is set.

**order** — changes visual order only. Focus order remains DOM order, so heavy use is an accessibility problem.

---

## A-039 · Position

`type` · `top` · `right` · `bottom` · `left` (or `inset`) · `z-index` · `containing block`

**static** — normal flow, offsets ignored.
**relative** — offset from its normal position; original space preserved.
**absolute** — removed from flow; positioned against the nearest positioned ancestor.
**fixed** — positioned against the viewport, unless an ancestor has a transform, filter, or `will-change`, in which case that ancestor becomes the containing block and fixed silently behaves as absolute.
**sticky** — relative until a threshold is crossed, then fixed within its parent. Requires a threshold value and a parent taller than the element; fails silently if the parent has `overflow: hidden` anywhere in the chain.

---

## A-040 · Stacking context

`trigger` · `z-index` · `descendant scope`

**Triggers** — root element · `position` other than static with `z-index` not auto · `opacity` < 1 · any `transform`, `filter`, `backdrop-filter`, `perspective`, `clip-path`, `mask` · `isolation: isolate` · `mix-blend-mode` other than normal · `contain: paint` · `will-change` on any of the above · a flex or grid child with `z-index` set.

**The rule** — z-index only compares siblings within the same context. A z-index of 9999 inside a context whose parent sits at z-index 1 will never rise above a sibling of that parent at z-index 2.
**Escape** — render into a portal at the document root.

---

## A-041 · Breakpoint

`value` · `unit` · `direction` · `basis`

**Direction** — `min-width` builds upward (mobile-first) · `max-width` builds downward. Mixing both in one system produces overlap bugs.
**Unit** — `em` respects user font-size preference; `px` does not.
**Basis** — viewport (media query) or container (container query). Container queries take `inline-size`, `block-size`, or style, and require the parent declare `container-type`.

**Common set** — 640 / 768 / 1024 / 1280 / 1536.

---

## A-042 · Fluid value

`min` · `preferred` · `max`
**Syntax** — `clamp(min, preferred, max)`
**The preferred term** — `intercept + slope × 100vw`
**Derived slope** — `(max − min) / (maxViewport − minViewport)`
**Derived intercept** — `min − slope × minViewport`

**Rule** — the preferred term must contain a `rem` component, or the value stops responding to browser zoom.

---

# E. Motion

## A-043 · Timing

`duration` · `delay` · `easing` · `iteration-count` · `direction` · `fill-mode` · `play-state` · `playback-rate`

**Duration bands**
- 100–150ms — state changes on small elements: hover, focus, toggle
- 200–300ms — most component transitions: dropdown, tooltip, accordion
- 300–500ms — full-screen or large-surface transitions: modal, page, sheet
- Over 500ms — only for deliberate, attention-directing choreography

**Derived** — duration should scale with distance travelled and element size. A 400px slide needs longer than a 40px one to feel like the same speed.

**direction** — normal, reverse, alternate, alternate-reverse.
**fill-mode** — none, forwards, backwards, both. Determines whether the element holds its final state.

---

## A-044 · Easing

### A-045 · Cubic-bézier
`x1` · `y1` · `x2` · `y2`
**Constraints** — x values must fall in 0–1 (time cannot run backward); y values are unbounded, and y outside 0–1 is what produces overshoot.
**Shape reading** — the steeper the curve at any point, the faster the motion at that moment.

**Reference values**
`ease` = (0.25, 0.1, 0.25, 1) — the CSS default, and rarely the right one
`ease-out` = (0, 0, 0.58, 1) — entrances
`ease-in` = (0.42, 0, 1, 1) — exits
`ease-in-out` = (0.42, 0, 0.58, 1) — on-screen movement
Sharper practical variants: out-quint (0.22, 1, 0.36, 1) · out-expo (0.16, 1, 0.3, 1) · back-out (0.34, 1.56, 0.64, 1), where y > 1 creates the overshoot.

### A-046 · linear()
`stops[]` — each a `value` with an optional `position` or position range.
Approximates any curve, including ones cubic-bézier cannot express: bounces, multi-stage springs, elastic settles. The single break in cubic-bézier's monopoly.

### A-047 · Spring
`stiffness` · `damping` · `mass` · `initial velocity` · `rest threshold`
**Ranges** — stiffness 100–400 typical · damping 10–40 · mass usually 1.
**Derived**
- damping ratio ζ = `damping / (2·√(stiffness·mass))`
- ζ < 1 underdamped, overshoots and oscillates
- ζ = 1 critically damped, fastest settle with no overshoot
- ζ > 1 overdamped, slow approach, no overshoot
- settle time ≈ 4 / (ζ · ω) where ω = √(stiffness/mass)

**Why springs** — they have no duration, so they can absorb an interruption mid-flight by carrying current position and velocity into the new animation. Duration-based easing cannot, which is why gesture-driven interfaces use springs.

---

## A-048 · Transform

`translate` (x, y, z) · `scale` (x, y, z) · `rotate` (x, y, z, angle) · `skew` (x, y) · `perspective` · `transform-origin` (x, y, z) · `transform-style` · `backface-visibility`

**Order matters** — transforms apply right to left, and each operates in the coordinate space left by the previous one. `translateX(100px) rotate(45deg)` and `rotate(45deg) translateX(100px)` land in different places.
**Individual properties** — `translate`, `rotate`, and `scale` now exist as standalone properties, applied in a fixed order regardless of declaration sequence, and independently animatable.
**transform-origin** — the pivot. Default 50% 50%. Moving it to a corner or an edge changes the entire character of a scale or rotation.

**Cost tiers**
- Composite only: `transform`, `opacity`, `filter` — GPU, no main-thread work
- Paint: `color`, `background`, `box-shadow`, `border-radius` — repaint, no reflow
- Layout: `width`, `height`, `top`, `margin`, `padding`, `font-size` — full reflow

**The scale-correction problem** — animating `scale` on a container also scales its border-radius and its children's text. The FLIP technique and layout-animation libraries counter-scale children to compensate.

---

## A-049 · Choreography

`sequence` · `stagger interval` · `overlap` · `direction of travel` · `anchor`

**Stagger interval** — 20–60ms between siblings. Below 20ms it reads as simultaneous; above about 80ms as a queue.
**Overlap** — the fraction of one animation still running when the next begins. Full sequencing feels slow; total overlap feels chaotic; 40–70% overlap reads as connected.
**Direction of travel** — elements should enter from the direction of their origin. A dropdown expands from its trigger, not from the screen edge.
**Anchor** — the transform-origin of the whole composition, usually the element that triggered it.

**Enter vs exit** — exits run at roughly 70–80% of entrance duration. Entering asks for attention; leaving should get out of the way.

---

## A-050 · Micro-interaction

Four parts, after Dan Saffer:
`trigger` — what initiates it, user-driven or system-driven
`rules` — what may happen, in what order, under what conditions
`feedback` — what is communicated back, visually, audibly, or haptically
`loops and modes` — what happens on repetition, and over time

**Feedback channels** — visual (color, position, scale, opacity) · haptic (impact style, intensity, duration) · audio (pitch, envelope, volume) · temporal (delay itself is a signal).

---

## A-051 · Scroll-driven animation

`timeline type` · `source` · `subject` · `range start` · `range end` · `attachment`

**Timeline types** — `scroll()` maps progress to the container's scroll position · `view()` maps progress to a subject's passage through the viewport.
**view() range keywords** — `cover`, `contain`, `entry`, `exit`, `entry-crossing`, `exit-crossing`, each with a start and end percentage.
**Runs off the main thread** where the animated properties are compositable, which is why scroll-linked effects built this way don't stutter.

---

## A-052 · Reduced motion

`preference state` · `substitution strategy`
**Strategies** — replace movement with a cross-fade · shorten duration toward zero · remove parallax and autoplay entirely · preserve state-change feedback.
**Not** — disabling all animation. Removing every transition destroys the feedback that told people something happened.

---

# F. Imagery and Icons

## A-053 · Raster image

`width` · `height` · `bit depth` · `channels` · `color profile` · `compression type` · `quality` · `chroma subsampling` · `progressive/interlaced` · `metadata`

**Bit depth** — 8 bits per channel standard; 10-bit needed for gradients without banding and for HDR.
**Chroma subsampling** — 4:4:4 full color detail · 4:2:2 half horizontally · 4:2:0 half in both directions. 4:2:0 is standard for photographs and visibly destroys sharp colored edges, which is why screenshots and text-bearing images should not use it.
**Color profile** — embedded ICC data. Missing profiles are assumed sRGB, which is how P3 photographs end up looking flat.

**Derived** — file weight ≈ pixels × bit depth × channels × compression ratio.

---

## A-054 · Responsive image

`src` · `srcset` · `sizes` · `width` · `height` · `loading` · `decoding` · `fetchpriority` · `alt`

**srcset descriptors** — `2x` density descriptors for fixed-size images · `800w` width descriptors for images whose display size varies.
**sizes** — tells the browser how much *layout space* the image will occupy, at each breakpoint, before CSS has been parsed. Required for `w` descriptors to work; omitting it makes the browser assume 100vw.
**`<picture>`** — `source` elements with `media` and `type` attributes for art direction and format negotiation, falling back to `img`.
**width and height attributes** — reserve the aspect ratio before load. The single highest-leverage fix for layout shift.

---

## A-055 · SVG

`viewBox` · `preserveAspectRatio` · `width` · `height` · `xmlns`

**viewBox** — `min-x min-y width height`. Defines the internal coordinate system, independent of rendered size.
**preserveAspectRatio** — `<align> <meetOrSlice>`. Align takes nine values from `xMinYMin` to `xMaxYMax`; `meet` fits inside, `slice` fills and crops.

**Path commands** — uppercase absolute, lowercase relative
`M` moveto · `L` lineto · `H` horizontal · `V` vertical
`C` cubic bézier · `S` smooth cubic · `Q` quadratic · `T` smooth quadratic
`A` elliptical arc (rx, ry, rotation, large-arc-flag, sweep-flag, x, y)
`Z` close path

**Presentation attributes** — `fill`, `fill-rule` (nonzero or evenodd), `fill-opacity`, `stroke`, `stroke-width`, `stroke-linecap`, `stroke-linejoin`, `stroke-dasharray`, `stroke-dashoffset`, `stroke-miterlimit`, `opacity`, `clip-path`, `mask`, `filter`, `vector-effect`.
**`vector-effect: non-scaling-stroke`** — keeps stroke width constant as the SVG scales.
**Structural** — `defs`, `symbol`, `use`, `g`, `pattern`, `linearGradient`, `radialGradient`, `clipPath`, `mask`, `filter`.

---

## A-056 · Icon

`canvas size` · `live area` · `padding` · `keyline shapes` · `stroke width` · `corner radius` · `terminal style` · `join style` · `optical volume`

**Canvas and live area** — a 24px canvas with a 20px live area, leaving 2px padding, is the common convention. Padding keeps icons from touching each other or their container.
**Keyline shapes** — the square, circle, and rectangles inscribed in the live area that all icons align to. The circle is drawn *larger* than the square so both read as the same size.
**Stroke width** — 1.5px or 2px on a 24px grid. Must stay constant across the set, including on diagonals, where it is optically thinner and sometimes needs compensation.
**Optical volume** — the total ink of an icon. Icons at the same nominal size but wildly different ink read as different weights and must be balanced by eye, not by bounding box.

**Optical size variants** — a 16px icon is not a 24px icon scaled down. Detail must be removed, stroke width proportionally increased, and corners opened.
**Pixel snapping** — a 1px stroke centered on a whole coordinate straddles two pixels and renders as two gray lines. Offsetting by 0.5 lands it on one crisp line.

---

# G. States and Interaction

## A-057 · The state matrix

Every component exists at the intersection of several independent dimensions. The full set to design is the product, not the sum:

`interaction state` — rest, hover, focus, focus-visible, active, disabled
`content state` — empty, loading, partial, full, overflowing, error
`selection state` — unselected, selected, indeterminate
`permission state` — available, disabled, read-only, hidden
`theme` — light, dark, high-contrast, forced-colors
`density` — comfortable, compact
`direction` — LTR, RTL

**Derived** — a button has roughly 6 × 2 × 2 × 2 = 48 renderable combinations before variants. This is why systems collapse dimensions where they can.

---

## A-058 · Focus ring

`color` · `width` · `offset` · `radius` · `style` · `contrast against element` · `contrast against background`

**Requirement** — C022 against *both* the adjacent element and the page background. A ring meeting it against only one disappears against the other.
**Offset** — 2px is standard. Zero offset makes the ring read as a border change rather than a focus indicator.
**Radius** — must follow the element's own radius plus the offset, or the ring will not sit parallel to the corner.
**Two-tone technique** — an inner light ring and an outer dark ring, so the indicator survives on any background.
**`:focus-visible`** — applies the ring only for keyboard focus. `:focus` alone shows it on mouse click, which is why people remove it, which is how keyboard users lose it.

---

## A-059 · Hit target

`visual size` · `hit size` · `spacing to neighbors` · `shape`

**Minimums** — C028, C029, C082.
**Decoupling** — the hit area can exceed the visual area via padding, a pseudo-element overlay, or negative margins. A 16px icon can carry a 44px target without looking oversized.
**Spacing** — adjacent targets need separation, or the effective target is smaller than its measurement. C028 permits a smaller target where spacing compensates.

---

## A-060 · Feedback loop

`trigger` → `acknowledgment` → `progress` → `resolution` → `recovery`

**Acknowledgment** — bounded by C001. A separate obligation from completing the action.
**Progress** — required past the point C003 sets. Determinate where possible; indeterminate spinners past that point read as failure regardless of what is happening.
**Resolution** — success needs confirmation proportional to the stakes. A saved draft needs a whisper; a deleted account needs a sentence.
**Recovery** — every failure state needs a stated cause and a next action. "Something went wrong" satisfies neither.

**Latency thresholds** — C001, C002, C003.

---

## A-061 · Form field

`label` · `input` · `placeholder` · `helper text` · `error message` · `required indicator` · `character count` · `prefix/suffix` · `clear affordance` · `autocomplete token` · `inputmode` · `pattern`

**Validation timing dimensions** — `on submit` · `on blur` · `on change while already invalid` · `on change always`
These dimensions are not mutually exclusive — a field can be validated on more than one of them at once, for example on blur and then again on change once it has already failed.

**inputmode** — text, numeric, decimal, tel, email, url, search. Controls the mobile keyboard.
**autocomplete** — a specific token vocabulary (`given-name`, `email`, `street-address`, `cc-number`, `one-time-code`). Not a boolean, and filling these in correctly is one of the largest usability wins available for the effort.

---

# H. Components

A first slice: five components whose parts are least reducible to the primitives already covered, chosen because most other components in Vocabulary's `H · Components` part compose from them or from a variant of them. The remaining entries in that part are a later, separately scoped addition — see **Settled decisions** below.

A-067–A-076 below are the second such addition: the input controls, the group most of the remaining `H` names sit beside rather than compose from. See **Settled decisions** for why this group and this boundary.

A-077–A-078 below are the third such addition: the menu family — dropdown menu, context menu, and command palette — the group whose anatomy leans most heavily on A-064 Tooltip and popover's placement machinery while still differing enough in interior structure to earn its own entries. See **Settled decisions** for why this group and this boundary.

A-079–A-083 below are the fourth such addition, and the first drawn from information architecture rather than from this part directly: Breadcrumb, Pagination, Facets, Navigation — folding global navigation, local navigation, and utility navigation, with hamburger menu as a sub-part of it rather than an entry of its own — and Skip link. See **Settled decisions** for why this group and this boundary.

## A-062 · Button

`container` · `label` · `leading icon` · `trailing icon` · `hit target` · `state matrix`

A button (V-310) is a container holding a label and optional icons, sized independently of its hit target and rendered across the state matrix.
**Sub-parts** — icon button (V-313) omits the label, leaving the icon to carry the name; ghost button (V-312) omits fill and border at rest, resolving them only on hover or focus; floating action button (V-314) is a button whose position is fixed rather than in flow; split button (V-315) is two adjoining containers sharing one visual boundary, each with its own hit target.
**Breaks when** — an icon-only container ships with no accessible name independent of the icon's visible form; the name, role, and value must each be determinable per C046 regardless of what is painted.

---

## A-063 · Card

`surface` · `media slot` · `header` · `body` · `actions` · `padding`

A card (V-331) is a bounded surface collecting content about one subject: an optional media slot, a header, a body of running text, and an optional row of actions, each inset by padding from the surface edge.
**Note** — the surface itself is a fill, a corner treatment, and either a border or a shadow; those parameters are not restated here.
**Breaks when** — the whole card is one interactive element while also containing a nested actionable control. Nested interactive elements have no single well-formed name/role pairing under C046, and the larger hit target intercepts input meant for the smaller one.

---

## A-064 · Tooltip and popover

`trigger` · `content` · `arrow` · `placement` · `offset` · `collision behavior` · `open delay` · `close delay` · `dismissal`

Tooltip (V-342) and popover (V-341) share one anatomy and diverge only in whether `content` may hold interactive descendants — see the compound entry at V-609.
**Placement** — an anchor side (top, right, bottom, left) plus an alignment (start, center, end); `collision behavior` substitutes an alternate side or shifts the position when the preferred placement has no room.
**Offset** — the gap between anchor and content edge, independent of `arrow` length, which is its own small triangle or notch pointing back at the trigger.
**Delay** — `open delay` and `close delay` are each a duration; an asymmetric pair (short to open, longer to close) lets a pointer cross a small gap to the content without it dismissing.
**Breaks when** — content reachable by pointer hover has no equivalent reachable by keyboard focus; C030 requires the function to be operable by keyboard, not merely visible to a mouse.

---

## A-065 · Dialog

`scrim` · `surface` · `header` · `body` · `footer` · `dismissal affordance` · `focus trap` · `initial focus` · `return focus`

Covers modal (V-337) and non-modal (V-338) dialogs, and drawer (V-339) and sheet (V-340) as edge-anchored variants of the same parts.
**Scrim** — a layer dimming the page behind the dialog, present for a modal dialog and absent for a non-modal one, whose page beneath stays operable. Vocabulary has no ID for this sense of the term yet — V-195 defines "scrim" only for text-over-imagery legibility, a different concept — so this is described in place rather than mis-cited; a dedicated disambiguation entry (in the style of V-609–V-612) is a candidate for a future Vocabulary addition.
**Focus trap** — V-404, required only where a scrim is present. A trap without an exit violates C031; every trap needs a stated escape hatch (V-406), conventionally the Escape key in addition to the dismissal affordance, not instead of it.
**Initial and return focus** — initial focus moves onto the dialog on open; return focus restores to the element that triggered it on close. Either one missing breaks the meaningful focus order required by C038.
**Breaks when** — the scrim dismisses the dialog on click but Escape does not, or the reverse; the two are expected as redundant paths to the same result, not alternatives that only sometimes work.

---

## A-066 · Tabs

`tablist` · `tab` · `indicator` · `panel` · `orientation` · `overflow behavior`

`tab` sub-parts — `label` · `icon` · `badge` · `state`

Tabs (V-334) switch between sibling panels in one context. The tablist is a single stop in the page's focus order; individual tabs are reached inside it by arrow key, a roving tabindex (V-403) rather than one tab stop each, which is what keeps the tab order in C038 meaningful as tab count grows.
**Indicator** — its position and length track the active tab. Animating it by transform rather than by recomputing `left`/`width` keeps the movement off the layout path.
**Overflow behavior** — scroll, wrap, or collapse into an overflow menu once tabs exceed the available inline size.
**Breaks when** — the indicator's position is read from layout geometry every frame instead of transformed directly; the animation then contends with layout on the main thread.

---

## A-067 · Text input

`container` · `value` · `caret` · `selection` · `placeholder` · `resize handle` · `state matrix`

Input (V-316) is a single-line text field holding one value; textarea (V-317) is the same construction spanning multiple lines, the only genuine addition being a `resize handle` and the wrapping behavior a single line does not need.
**Sub-parts** — textarea's resize handle: `none` · `vertical` · `horizontal` · `both`, set via the CSS `resize` property. The value area itself is otherwise the text block already covered earlier in this document.
**Note** — `label`, `placeholder`, and `helper text` are already anatomized as parts of the surrounding wrapper at A-061 Form field; this entry covers only the editable value surface, not that furniture.
**Breaks when** — computed font size falls below 16px on iOS Safari; C080 makes that an effective floor for input text, not a preference, because the browser zooms the viewport on focus below it.
**Also breaks when** — `autocomplete` is left unset or given an invented token; C086 requires the browser-specified vocabulary, not an author-chosen string, for autofill to work at all.

---

## A-068 · Checkbox

`indicator` · `label` · `hit target` · `state matrix`

Checkbox (V-323) is an independent binary choice: a small indicator toggled directly by activating it, paired with a label.
**Indicator states** — unchecked (empty) · checked (a mark, conventionally a check glyph) · indeterminate (V-388, a mixed glyph, conventionally a dash), the third reachable only by script, never set through direct interaction with the control itself.
**Distinguished from switch** — V-608 separates the two on timing, not shape: an activated switch's state applies right away, a checkbox's usually stands until the form containing it is submitted. The two should not stand in for each other as if that difference did not matter.
**Breaks when** — checked/unchecked is signaled by a hue change alone with no shape change; C023 requires a non-color distinction, and C022 requires the indicator to clear 3:1 contrast against its background at every state, not only at rest.

---

## A-069 · Radio group

`group container` · `radio[]` (each with `indicator` · `label`) · `state matrix`

Radio group (V-324) is a mutually exclusive choice among visible options: a group container holding two or more individually indicated options, of which exactly one is selected (V-387) at a time.
**Navigation** — the group is a single stop in the page's tab order; individual radios inside it are reached by arrow key, a roving tabindex (V-403) rather than one tab stop per option.
**Indicator** — a circle rendering two states, unselected (empty) and selected (a filled dot); no indeterminate state exists at the option level.
**Breaks when** — the options have no programmatic grouping tying them together as one control; C046 requires the group's role and each option's state to be determinable, which a set of unrelated radio inputs with no shared group semantics cannot provide.

---

## A-070 · Switch

`track` · `thumb` · `label` · `hit target` · `state matrix`

Switch (V-325) is a control taking effect immediately on toggle: a track holding a thumb at one of two end positions, paired with a label.
**States** — off (thumb at the track's start) and on (thumb at the track's end); no indeterminate state.
**Distinguished from checkbox** — V-608 separates the two on timing: a switch's toggle takes effect immediately, a checkbox's typically waits for a surrounding form to be submitted. The visual similarity between the two affordances does not make the timing interchangeable.
**Breaks when** — the on/off track colors are distinguished by hue alone; C011 makes any red-green-only pairing invisible to a meaningful share of any general audience, and C023 requires the thumb's position, not color, to carry the state regardless of which hues are chosen.

---

## A-071 · Select and combobox

`trigger` · `panel` · `option[]` · `placement` · `offset` · `collision behavior`

Select (V-321) and combobox (V-322) share one anatomy — a trigger opening a panel of options, positioned and collided the same way as a popover anchored to its trigger — and diverge only in what the trigger accepts: a select's is a fixed value display, a combobox's is a text input that filters the option list as it is typed into.
**Option** — `label` · `value` · `selected state` (V-387) · `disabled state` (V-389).
**Breaks when** — a custom-built trigger and panel do not expose role, name, and current value the way a native form control does for free; C046 requires all three be programmatically determinable regardless of what markup produces them.
**Also breaks when** — a combobox's typed value matches nothing in the option list with no stated outcome for what happens next — revert, allow free entry, or reject — left implicit rather than chosen.

---

## A-072 · Slider

`track` · `thumb` · `value` · `min` · `max` · `step` · `orientation` · `hit target`

Slider (V-326) is a control selecting a value along a range: a track spanning `min` to `max`, a thumb positioned along it at the current `value`, moving in increments of `step`.
**Orientation** — horizontal or vertical; on the vertical axis, increase runs bottom-to-top by convention.
**Range slider** — a variant carrying two thumbs and two values, each independently draggable, with a rule for whether they may cross.
**Breaks when** — dragging the thumb is the only means of setting a value; C037 requires a single-pointer alternative to any function using a dragging movement, met here by arrow-key stepping or a paired numeric input, not by the drag gesture alone.

---

## A-073 · Stepper

`decrement control` · `value` · `increment control` · `min` · `max` · `step` · `hit target`

Stepper (V-327) is a control incrementing and decrementing a value: two controls flanking the current `value`, each moving it by one `step` per activation, bounded by `min` and `max`.
**Breaks when** — a bound is reached and the control at that end gives no signal; a disabled (V-389) affordance with no visible or announced reason reads as broken rather than as a floor or ceiling being respected.

---

## A-074 · Segmented control

`track` · `segment[]` (each with `label` · `icon` · `state`) · `indicator` · `hit target`

Segmented control (V-328) is a compact row of mutually exclusive options: a track holding two or more segments, of which one is selected (V-387) at a time, with an indicator marking the current selection.
**Note** — the indicator tracks the selected segment the same way a tab indicator tracks the active tab; a segmented control differs in that it sets a value rather than switching which panel is visible.
**Breaks when** — segment count exceeds what the available inline width holds at a legible label size, with no defined overflow behavior of its own — unlike a tablist, which may scroll, wrap, or collapse into a menu, a segmented control that overflows has nowhere established to put the excess.

---

## A-075 · Dropzone

`region` · `accepted types` · `drag states` · `fallback control` · `hit target`

Dropzone (V-329) is a region accepting files by drag or click: a boundary indicating where a dragged file may be released, cycling through drag states as a file crosses it, paired with a `fallback control` for adding a file without a mouse.
**Drag states** — idle · drag-over (a file is above the region) · drag-reject (a file above the region does not match `accepted types`) · drop (an accepted file was released).
**Breaks when** — drag-and-drop is the only means of adding a file; C037 requires a single-pointer alternative to any function using a dragging movement, met here by the `fallback control` — ordinarily a standard file input — always present rather than revealed only once a drag is detected.

---

## A-076 · Fieldset

`legend` · `member controls[]` · `border or grouping treatment`

Fieldset (V-330) is a grouping of related controls with a group-level label: a `legend` naming the set, applying to the `member controls` it wraps, rendered with or without a visible boundary.
**Breaks when** — a set of related controls — a radio group, a set of checkboxes, an address split across street, city, and postal fields — has no group-level label; C039 requires input needing user data to carry a label or instruction, and for a set of controls it is the group itself that needs one, not only each member individually.

---

## A-077 · Menu

`trigger` · `panel` · `item[]` · `placement` · `offset` · `collision behavior`

`item` sub-parts — `label` · `icon` · `shortcut` · `submenu indicator` · `state`

Dropdown menu (V-343) and context menu (V-344) share one anatomy — a panel of items positioned and collided the same way as a popover anchored to its trigger (A-064) — and diverge only in what supplies that anchor: a dropdown menu's trigger is a persistent, visible control, while a context menu's is the point where a secondary click or long press occurred, so its panel is anchored to that point rather than to any element, and it is scoped to whatever the invoking event targeted.
**Navigation** — the panel is a single stop in the page's tab order; individual items are reached inside it by arrow key, a roving tabindex (V-403) rather than one tab stop each. A `submenu indicator` marks an item that opens a nested panel on a further arrow key or activation, returning focus to the parent item on close.
**Breaks when** — a context menu has no means of invocation reachable without a pointer; C030 requires all functionality to be operable through a keyboard interface, and a menu invoked only by secondary click or long press provides none on its own.
**Also breaks when** — an item's role, checked state, or disabled state is carried only by its visual treatment; C046 requires each to be programmatically determinable regardless of what markup produces the panel.

---

## A-078 · Command palette

`invocation` · `overlay` · `query input` · `result[]` · `section[]` · `initial focus` · `return focus`

`result` sub-parts — `label` · `icon` · `shortcut` · `group`

Command palette (V-345) is invoked by a global keyboard shortcut rather than anchored to any on-page trigger: opening it presents an overlay, typically centered or full-width, whose primary chrome is a `query input` filtering `result[]` as it is typed into. Results may be grouped into labeled `section[]` (recent, suggested, matched-by-category) before any query is entered.
**Distinguished from Menu (A-077)** — there is no element to anchor a panel against, so `placement`, `offset`, and `collision behavior` do not apply; the overlay's position is fixed relative to the viewport, not derived from a trigger's geometry.
**Initial and return focus** — initial focus moves onto `query input` on open; return focus restores to whatever held focus before invocation on close, the same obligation A-065 states for dialog.
**Breaks when** — either focus move is missing; C038 requires the resulting sequence to still make sense, and a palette that opens without moving focus into `query input`, or closes without restoring it, breaks that sequence.
**Also breaks when** — the query matches nothing and no state is defined for that case — the same unresolved-input gap A-071 names for combobox, here with no result list to fall back on at all.

---

## A-079 · Breadcrumb

`container` · `item[]` (each `label` · `href`) · `separator` · `current item` · `truncation behavior`

Breadcrumb (V-352) is a trail showing position within a hierarchy: an ordered list of items running from a root down to the level above the current page, each a link, separated by a `separator` glyph or character, ending in a `current item` that names the page itself and is not a link.
**Truncation behavior** — collapsing the middle of a long trail behind an ellipsis once depth exceeds the available inline width, the same overflow problem A-066 Tabs names for a tablist that outgrows its row.
**Breaks when** — the `current item` is rendered as a link pointing at the page already loaded, or the trail's structure is conveyed by visual nesting alone with no underlying list or landmark; C046 requires the current position, not only the links leading to it, to be programmatically determinable.

---

## A-080 · Pagination

`container` · `page control[]` (each `label` · `href or value` · `state`) · `previous control` · `next control` · `current indicator` · `overflow marker`

Pagination (V-353) is navigation between discrete pages of results: a row of `page control`s, of which the current one is selected (V-387) among its siblings, flanked by `previous control` and `next control`, with an `overflow marker` — an ellipsis — standing in for a run of skipped numbers once the total exceeds what the row can show.
**Boundary state** — `previous control` at the first page and `next control` at the last are disabled (V-389), not merely styled to look inactive.
**Breaks when** — the current page's state is carried by a color or weight change alone with no non-visual signal; C023 requires a non-color distinction and C046 requires that state to be programmatically determinable regardless of what markup produces the row.
**Also breaks when** — activating a page control replaces the result list without moving focus into it; a keyboard or screen-reader user who just changed pages is left exactly where they were, with no indication the content beneath them changed.

---

## A-081 · Facets

`facet[]` (each `label` · `member control[]` (each `option label` · `count` · `state`)) · `applied filter[]` (each a chip) · `clear control` · `result count`

A facet (V-360) is a single filterable dimension, usually shown with counts: a labeled group of `member control`s — most often checkboxes (A-068), sometimes a slider (A-072) for a range — each option carrying a `count` of how many results choosing it would leave. Facets composing together into one filtering interface is faceted navigation (V-536); this entry anatomizes the facet, not the pattern several of them compose into.
**Applied filter** — a chip (V-350) representing one active selection, removable independently of unchecking it inside its own facet, paired with a `clear control` that resets every facet at once.
**Breaks when** — a facet's `member control` is a custom-styled element that does not expose checked state as programmatically determinable; C046 requires it regardless of what markup produces the facet.
**Also breaks when** — the `result count` updates after a selection with no signal reaching anything other than sighted users watching the number change; a screen-reader user who just toggled a facet has no way to learn how many results remain, or whether the toggle had any effect at all.

---

## A-082 · Navigation

`container` (landmark) · `item[]` (each `label` · `href` · `icon` · `current state`) · `overflow control` (`trigger` · `panel`)

Global navigation (V-533), local navigation (V-534), and utility navigation (V-535) share one anatomy — a landmark (V-466) containing a list of items — and diverge only in scope: global navigation's items span the whole site, local navigation's items are scoped to the current section, and utility navigation's items are account, search, settings, and help functions rather than site or section content.
**Current state** — the item matching the page being viewed carries a `current state` distinct from its rest appearance, the same wayfinding (V-537) obligation a breadcrumb (A-079) and a tab (A-066) each meet in their own construction.
**Overflow control** — hamburger menu (V-364) folds into this entry rather than standing as one of its own: a `trigger` and disclosure `panel`, the same construction A-064 Tooltip and popover and A-077 Menu already anatomize, that appears once the item list no longer fits the available inline space and conceals the same items rather than presenting different ones.
**Breaks when** — the same navigation's set of items, their order, or its accessible name changes between the pages it appears on with no corresponding change in what it should contain; C043 requires repeated navigation to appear in the same relative order and be identified consistently.
**Also breaks when** — the overflow control opens only on hover, or is built without button semantics; C030 requires the disclosure to be operable through a keyboard interface, not only a pointer.

---

## A-083 · Skip link

`link` · `target` · `visibility trigger`

Skip link (V-405) is a link allowing keyboard users to bypass repeated navigation: the first focusable element on the page, ordinarily hidden until it receives focus, whose `target` is a landmark (V-466) — conventionally the main content region — reached by activating it.
**Visibility trigger** — focus. An off-screen or zero-size technique that hides the link at rest and reveals it on `:focus`, not `display: none`, which would remove it from the accessibility tree and from focus itself along with it.
**Breaks when** — the `target` is not itself focusable (a `<main>` or a plain `<div>` with no `tabindex="-1"`), so activating the link scrolls the viewport without moving focus; C038 requires the resulting sequence to still make sense, and a skip link that changes what's on screen without changing where focus continues from breaks exactly that sequence — the same gap A-078 names for a command palette that opens without moving focus into its query input.
**Also breaks when** — the link stays visually hidden even once focused; C032 requires keyboard focus to carry a visible indicator, and that applies to the skip link itself the same as any other focusable element.

---

# I. Content

A-084–A-094 below are the content-elements slice the scoping resolution recorded in **Settled decisions** names as the suite's other open resolution alongside information architecture: Headline, Deck, Eyebrow, Byline, Body, Pull-quote, Stat/callout, Caption, CTA text, List, and Metadata block — the full named candidate set from that resolution, each anatomized as an atomic content element rather than as a content type, per that resolution's own decision. See **Settled decisions** for the one fold within this slice and the small companion Vocabulary addition (V-613–V-621) it required.

## A-084 · Headline

`text` · `length range` · `required/optional` · `heading level`

Headline (V-613) is the primary title of a piece of content: a text string held to a length range appropriate to where it renders, ordinarily required, and mapped to a specific heading level rather than left to whichever element a stylesheet happens to size largest.
**Length range** — a floor and a ceiling, not a single number: below the floor a headline carries too little to orient a reader, above the ceiling it wraps past the number of lines its slot was built to hold.
**Breaks when** — the length range is violated with no defined outcome for the overflow; the headline either breaks its container's layout or gets truncated mid-word with nothing indicating anything was cut.
**Also breaks when** — the heading level is chosen for the visual size it produces rather than for its place in the page's outline; a heading hierarchy that skips levels or repeats to suit a design breaks the outline a screen-reader user is navigating by, independent of how the text looks.

---

## A-085 · Deck

`text` · `length range` · `required/optional`

Deck (V-505) is the supporting line beneath a Headline (A-084): a shorter text string, held to its own length range independent of the headline's, and optional wherever the headline alone orients the reader.
**Breaks when** — a deck renders with no headline above it; V-505 defines the term relationally, so a deck standing alone has nothing to support and reads as an orphaned subhead the content model never anticipated.

---

## A-086 · Eyebrow

`text` · `length range` · `required/optional`

Eyebrow (V-614) is a short label set above a Headline (A-084) naming its category or context: a text string kept shorter than the headline it precedes, ordinarily optional.
**Breaks when** — the eyebrow text is the only thing distinguishing two adjacent pieces of content that otherwise share a headline pattern, most often in a card list filtered to one category; a reader skimming by headline alone has no way to tell the cards apart, and neither does a screen-reader user whose list of headings does not include the eyebrow at all.

---

## A-087 · Byline

`text` · `length range` · `required/optional`

Byline (V-615) is a line naming the author of a piece of content: a text string, its length bounded in practice by a name's own length rather than by a fixed range, and optional wherever authorship is not attributed to an individual.
**Breaks when** — a byline names a role or a placeholder ("Staff Writer", "TBD") rather than an actual author with no stated reason; the element exists to answer "who wrote this," and an unresolved placeholder left in production answers a different question than the one it promises.

---

## A-088 · Body

`text` · `paragraph structure` · `length range` · `required/optional`

Body (V-616) is the main block of running text within a piece of content: prose composed of the text block (A-021) already anatomized here for typographic parameters, structured into paragraphs rather than shipped as one run, and held to a length range — a floor below which the content underserves what its headline promised, a ceiling above which the slot it renders in was not built to hold.
**Breaks when** — body text is truncated at a fixed character count with no visible indication anything was cut and no way to reach the rest; a preview built this way tells a screen-reader user the content ends where the truncation happens to land, not where the author ended it.
**Also breaks when** — the measure (V-136) the body renders at falls outside C004's 45–75 character range; body copy is exactly the sustained-reading case that constraint governs, and a body block inheriting an unrelated container's width has no guarantee of landing inside it.

---

## A-089 · Pull-quote

`text` · `source excerpt` · `length range` · `required/optional`

Pull-quote (V-617) is a short excerpt from Body (A-088), set apart and enlarged to draw a skimming reader back in: text sourced from the surrounding body rather than authored independently, held to a length range tighter than the body it is drawn from, and always optional.
**Breaks when** — the pull-quote text does not appear verbatim anywhere in the surrounding body; a reader who scans the pull-quote and then reads the body expects to find it there, and a pull-quote that paraphrases, or was never reconciled after an edit, reads as two different claims stitched together.
**Also breaks when** — the pull-quote is marked up as an unrelated second copy of the same text with no relationship declared to the body it repeats; assistive technology reading the page in sequence announces the same sentence twice with nothing indicating one is a repetition of the other.

---

## A-090 · Stat/callout

`value` · `label` · `text` · `length range` · `required/optional`

Stat (V-618) and callout (V-348) share one construction — a short block set apart from the surrounding body to draw attention to it — and diverge only in content: a stat's primary content is a `value`, a number or metric, paired with a short `label` naming what it measures; a callout's primary content is `text`, a sentence or two of supplementary information with no numeric value at its center.
**Breaks when** — a stat's `value` renders with no `label`, or a `label` with no `value`; a number alone ("40%") answers a different question than the same number with its unit and referent attached, and a reader arriving without the sentence that originally explained it has no way to recover the missing half.
**Also breaks when** — several stats appear together with inconsistent `value` formatting — one as "40%", a sibling as "0.4", a third as "40 percent" — reporting what should be directly comparable figures in forms that don't actually compare.

---

## A-091 · Caption

`text` · `length range` · `required/optional` · `associated media`

Caption (V-619) is text identifying or describing a piece of accompanying media — an image, chart, or embed — set adjacent to it rather than inside it, and distinct from that media's own alt text (V-292), which serves assistive technology in the media's absence rather than a sighted reader in its presence.
**Breaks when** — a caption is written as though it were alt text, or an image ships a caption with no alt text on the assumption the caption covers it; C024 requires the text alternative regardless, and the two serve different readers under different conditions — a caption disappears along with the image it captions if the image fails to load, alt text does not.
**Also breaks when** — a chart's caption states the takeaway but the data the chart encodes is not available in any text form; a caption that narrates a visual without the visual's own text alternative leaves a screen-reader user the narration but not the evidence behind it.

---

## A-092 · CTA text

`text` · `length range` · `required/optional`

CTA text (V-504) is the text carried by whatever control — ordinarily a Button (A-062) or a Link (V-311) — performs a call to action: a short, conventionally verb-led string, held to a length range tight enough to fit the control's own width without wrapping in typical placements.
**Breaks when** — the CTA text is generic ("Click here", "Learn more") and repeated identically across several controls on the same page, each leading to a different destination; a person tabbing through controls or scanning a list of links by their text alone has no way to tell them apart until they activate one.
**Also breaks when** — the length range is exceeded and the text wraps inside a control sized for one line; a two-line label breaks the fixed-height hit-target assumption A-062 and A-074 both make about their controls.

---

## A-093 · List

`item[]` (each `text`) · `list type` · `item count range` · `required/optional`

List (V-620) is a set of related items presented as a sequence: an `item[]` of short text entries, roughly parallel in grammatical form to each other, of a `list type` — ordered where sequence or rank carries meaning, unordered where it does not — bounded by an `item count range` the same way other content elements in this section are bounded by a length range.
**Breaks when** — a list is marked up as a run of paragraphs or line breaks rather than a semantic list structure; C046 requires the resulting group's role to be programmatically determinable, and a screen reader announcing a visually bulleted paragraph gives no indication of how many items it contains or where the list ends.
**Also breaks when** — the `item count range`'s ceiling is exceeded with no defined behavior for the overflow — no truncation, no "show more," no pagination — the same undefined-overflow failure A-084 Headline names for a title, here at list scale; a list long enough to exceed a reader's ability to hold its items in mind needs the same external structure C006 requires for a choice set or navigation breadth of comparable size.

---

## A-094 · Metadata block

`item[]` (each `label` · `value`) · `required/optional`

Metadata block (V-621) is a grouped set of secondary facts about a piece of content — publish date, category, reading time, author affiliation — presented together rather than scattered through the surrounding layout: an `item[]` of `label`/`value` pairs, each individually optional even where the block itself is required.
**Breaks when** — the block's items are grouped only by visual proximity, with no programmatic grouping tying them together; C046 requires a group's role to be determinable the same way it requires an individual control's, and a metadata block with no shared group semantics reads to assistive technology as unrelated scattered text rather than one set of facts about the content.
**Also breaks when** — a `value` is presented with no `label` and its meaning is not self-evident out of context — a bare date with no indication of whether it is a publish or an update date, a bare number with no indication of what it counts — the same value/label pairing failure A-090 names for a stat, here at the scale of a whole block rather than one figure.

---

# J. Message surfaces

A-095–A-096 below are the sixth addition to Vocabulary's `H · Components` part, physically placed after Section I because Content (A-084–A-094) was appended in the intervening fifth slice — the ID sequence and this section split are both artifacts of arrival order, not a claim that a toast, a banner, or a callout belongs to some category Button or Card does not. See **Settled decisions** for why this group and this boundary.

## A-095 · Toast and banner

`surface` · `icon` · `message text` · `action` · `dismissal affordance` · `intent` · `placement` · `duration` · `stacking`

Toast (V-346) and banner (V-347) share one construction — a surface carrying an optional icon, a short message, an optional action, and a dismissal affordance, keyed to an `intent` — and diverge only in `placement`, `duration`, and `stacking`, the same "shares a parameter set, diverges only in what's present, absent, or fixed" test A-065 already applied along a placement axis to fold modal, non-modal dialog, drawer, and sheet into one entry, and A-071, A-077, A-082, and A-090 have each since reused: a toast is a fixed-position overlay, commonly a page corner or edge, that removes itself after a `duration` and stacks above any toast already showing; a banner sits inline within the page or section it concerns, carries no default `duration` of its own, and does not stack, since a second banner in the same region ordinarily replaces or joins the first rather than layering above it.
**Intent** — info, success, warning, danger; carried by the surface's fill, border, or icon, not by the message text alone.
**Note** — the surface reuses the box, corner, and elevation parameters already anatomized at A-025–A-029; icon reuses A-056; where `action` is a control rather than a bare link, its text reuses A-092 CTA text. None of these is restated here.
**Breaks when** — a `duration` runs past roughly five seconds with no way to pause, stop, or hide the surface before it disappears; C035 requires exactly that of any auto-updating content held on screen that long, and a toast's countdown to removal is exactly this case. A banner carrying no default `duration` at all is unaffected — the obligation only attaches once a timer is present.
**Also breaks when** — `intent` is carried by the surface's hue alone with no icon or text distinguishing which one applies; C023 requires the same non-color distinction A-070 already cites for a switch's on/off state, and a toast or banner's severity is exactly that kind of state.

---

## A-096 · Callout

`surface` · `icon` · `intent` · `accent color` · `text`

Callout (V-348) — the `H`-part, general-purpose sense of the term the 1.5.0 Settled decisions flagged as still open, distinct from A-090 Stat/callout's content-element sense of the same V-ID: a surface set apart from the content around it, carrying an icon and an accent color, both keyed to an `intent` (info, success, warning, danger), around a short block of `text`.
**Distinguished from A-090 Stat/callout** — A-090 cites V-348 for a block of supplementary text embedded specifically within running Body (A-088) content, with no `intent`, `icon`, or `accent color` of its own. This entry cites the same ID for the richer, severity-keyed construction that note named as uncovered — one Vocabulary ID describing two constructions Vocabulary itself has not yet split into separate terms, not two different meanings mistakenly attached to one ID. That distinction matters because this document has a real precedent for the other case: A-065's Scrim citation was corrected specifically because V-195's imagery-legibility definition described an unrelated referent, not a narrower reading of the same one. V-348's "an inline box highlighting supplementary information" is not that — it is a fair one-line summary this entry's fuller construction still satisfies, the same relationship every Anatomy entry has to its own terser Vocabulary citation (V-310 Button says only "a control performing an action"; A-062 adds a state matrix and icon slots V-310 never mentions, and that has never been read as a mismatch).
**Not folded with A-095 Toast and banner** — a callout has no `dismissal affordance`, no `duration`, and no `placement` variance; it is a fixed part of whatever content it sits in, not a transient or page-level notification. That is a difference in construction, not only in which of a shared parameter set is present, absent, or fixed, so the fold test A-095 applies to toast and banner does not extend to callout.
**Not folded with Badge or Chip** — Badge (V-349) is a marker with no message text of its own, typically a count or a dot, attached to another element rather than standing apart from one; Chip (V-350) is a compact, often-removable tag representing a single attribute, filter, or selection, already partially anatomized as A-081 Facets' `applied filter`. Neither shares a parameter set with a callout's surface-plus-icon-plus-accent-plus-text construction — three different constructions wearing a similar "small, colored, meaningful" reputation, the same shape of near-miss A-068, A-069, and A-070 already rejected for checkbox, radio group, and switch.
**Breaks when** — `intent` is carried by the surface's accent color alone, with no icon or text distinguishing which one applies; C023 requires the same non-color distinction A-095 requires of a toast or banner.
**Also breaks when** — the accent color or icon fails C022's 3:1 non-text contrast against the surface it sits on; an accent that exists only to carry meaning and does not clear that floor reads as decoration rather than signal.

---

# K. Badges and chips

A-097–A-098 below are the seventh addition to Vocabulary's `H · Components` part, given their own section for the same reason Section J was: arrival order, not a claim that a badge or a chip belongs to some category Button, Card, or Callout does not. See **Settled decisions** for why this group and this boundary.

## A-097 · Badge

`host element` · `value` · `max value` · `position` · `intent/color` · `shape`

Badge (V-349) is a small marker attached to another element rather than standing apart from one: either a `value` — a short count, capped by a `max value` above which it renders a truncated form such as "9+" — or brief text, or no value at all, in which case it renders as a dot signaling presence alone. `position` anchors it to a corner of the `host element`; `shape` is typically a circle at rest, widening to a pill once its `value` needs more than one character. The `badge` sub-part A-066 Tabs already lists among a tab's sub-parts is this entry, not a distinct construction — a tab's badge is this entry's construction with the tab itself as `host element`.
**Breaks when** — the badge's `value` is not folded into its host's accessible name; C046 requires an interface component's name to be programmatically determinable and its states and values to be reported, and a badge rendered as a separate, unlabeled sibling node leaves its count or text out of both — absent from the host's name and unreported as one of its values.
**Also breaks when** — a dot-only badge (no `value`) carries its entire meaning in a fill-color change from the host's rest state, with no accompanying text; C023 requires a non-color means of conveying that same information, which a colored dot alone does not provide.

---

## A-098 · Chip

`label` · `leading element` · `remove control` · `state` · `hit target`

Chip (V-350) is a compact element representing a single attribute, filter, or selection: a `label` naming what it represents, an optional `leading element` — an icon (A-056) or a small image or initials representing a person or entity, an avatar (V-351) — and, where the chip is removable, a `remove control` carrying its own `hit target`, distinct from the hit target of the chip body itself.
**Sub-parts** — as A-081 Facets' `applied filter` already establishes, a chip may double as a toggle carrying a `state` — selected (V-387) or not — rather than only standing as a static tag; where it does, that state is the same value a checkbox (A-068) or segmented control (A-074) carries, not a separate vocabulary of its own.
**Distinguished from Badge (A-097)** — a chip's `label` is required; a badge's `value` may be absent entirely, leaving only a dot. A chip stands free, often removable and often interactive; a badge is fixed to a `host element` it does not stand apart from and, on its own, has neither a `remove control` nor an independent hit target. A-096 already found that neither shares a parameter set with the other, or with Callout; these two entries build the anatomy that finding anticipated rather than revisiting it.
**Breaks when** — a removable chip's `remove control` shares a hit target with the chip's own body, so activating one activates the other; C028's 24×24 minimum assumes the two are independently reachable and operable, not layered over the same region with no way to target one without the other.
**Also breaks when** — the `remove control`'s accessible name is the bare word "Remove," repeated identically across every chip in a group; a person tabbing through a filter row by name alone cannot tell one chip's remove control from the next without activating it first.

---

# L. Status, identity, and media

A-099–A-105 below are the eighth addition to Vocabulary's `H · Components` part, given their own section for the same reason Sections J and K were: arrival order, not a claim that an avatar, a progress indicator, a skeleton, an empty state, a carousel, a lightbox, or a toolbar belongs to some category Button, Card, or Callout does not. See **Settled decisions** for why this group and this boundary.

## A-099 · Avatar

`image source` · `initials fallback` · `icon fallback` · `size` · `shape` · `status indicator` · `group`

Avatar (V-351) is a small image or initials representing a person or entity: an `image source` where one exists, falling back to `initials fallback` — typically one or two letters derived from a name — and, where no name is available either, a generic `icon fallback` (A-056), each rendered at one of a fixed set of `size`s and a consistent `shape`, ordinarily a circle. `group` composes several avatars into an overlapping stack representing more people than are shown individually, the same "+N" overflow convention A-097 Badge's `max value` already establishes for a count too large to render in full.
**Status indicator** — a dot anchored to a corner of the avatar signaling presence (online, away, offline, busy); this is A-097 Badge's dot-only form — no `value`, presence alone — with the avatar as `host element`, not a separate construction.
**Breaks when** — the `image source` fails to load with no fallback rendering in its place, or the fallback that does render carries no accessible name identifying who or what the avatar represents; C024 requires a text alternative for non-text content, and a broken-image icon, or a silent set of initials with no accompanying name, answers a different question than whose avatar is being shown.
**Also breaks when** — the status indicator's state (online, away, offline, busy) is carried by hue alone with no shape or text distinguishing it; C023 requires a non-color means of conveying that same information, the same obligation A-097 already states for a dot-only badge's fill-color change.

---

## A-100 · Progress and spinner

`track` · `indicator` · `determinacy` · `value` · `max` · `label` · `size`

Progress bar (V-355) and spinner (V-356) share one construction — a `track` carrying an `indicator` that communicates ongoing work — and diverge only in `determinacy`: a determinate indicator's `indicator` fills in proportion to a `value` against a `max`, while an indeterminate indicator — a spinner, or a progress bar with no known `value` — loops or animates without one. A-060 Feedback loop already treats these as one continuum rather than two unrelated things: "Determinate where possible; indeterminate spinners past that point read as failure regardless of what is happening" — this entry gives that continuum its parameters.
**Breaks when** — an indeterminate `indicator` continues past roughly 4–5 seconds with nothing else changing; C003 sets that threshold directly — past it, an indeterminate indicator is read as failure regardless of what is actually happening, the specific case A-060 already names for progress in general.
**Also breaks when** — `value` and `max` are rendered only as a fill width, with no programmatically determinable value behind it; C046 requires an interface component's states and values to be reported, not only painted, and a progress bar built from unlabeled `div`s exposes neither its determinacy nor its current value to anything but sighted users watching the fill move.

---

## A-101 · Skeleton

`shape[]` · `animation` · `replacement content`

Skeleton (V-357) is a set of placeholder `shape[]` matching the layout of content still loading: a region shaped and positioned the way the eventual content will be, carrying an `animation` — typically a shimmer or pulse — signaling that loading is in progress, and replaced in place by `replacement content` once it arrives. Distinguished from A-100 Progress and spinner: a skeleton previews the *layout* of content not yet known to have loaded successfully; a progress bar or spinner signals only that work is occurring, with no claim about what the result will look like.
**Breaks when** — a skeleton has no defined transition to either its `replacement content` or an error state; C003 already establishes that an indeterminate signal read past roughly 4–5 seconds is read as failure regardless of what is happening, and a skeleton with no exit path is exactly that signal held indefinitely.
**Also breaks when** — the placeholder `shape[]` remain exposed to assistive technology as though they carried content, or the `replacement content` arrives with no programmatic indication that a loading state was ever present; C046 requires a component's state to be reported, and a loading state communicated only through shapes a screen reader cannot distinguish from meaningless empty regions does not meet it.

---

## A-102 · Empty and zero state

`illustration` · `message text` · `action` · `moment`

Empty state (V-358) is the view rendered when no content exists yet: an `illustration`, a short `message text` explaining why nothing is showing, and an optional `action` prompting the next step. Zero state (V-359) is not a separate construction — Vocabulary defines it as a subtype of empty state, scoped to a person's first encounter with the view — it is the same three parts at one specific `moment`: the very first time a person reaches the view, before anything could yet exist, rather than a later moment where content once existed and was filtered, searched, or cleared down to nothing.
**Moment changes the message and action, not the construction** — a zero-state `message text` and `action` orient a person toward creating something for the first time ("Add your first project"); an empty state reached later, say through A-081 Facets' filtering, orients a person toward undoing whatever emptied the view — A-081's own `clear control` — rather than toward creating something new. The parts are identical; only which moment produced the emptiness, and which action follows from it, differs — the same "shares a parameter set, diverges only in what's present, absent, or fixed" test A-095 applied to toast and banner, here applied to a parameter's value rather than its presence.
**Breaks when** — the `illustration` carries meaning the `message text` does not also state in words — which kind of content is missing, or why; C024 requires a text alternative for non-text content, and an illustration whose meaning exists only in the image excludes anyone not viewing it.
**Also breaks when** — the `action` is the only way to proceed but is rendered as styled text or a `div` rather than a focusable control; C030 requires all functionality to be operable through a keyboard interface, and an action reachable only by a pointer fails it regardless of how prominent it looks.

---

## A-103 · Carousel

`item[]` · `viewport` · `navigation control` · `pagination indicator` · `autoplay` · `pause control`

Carousel (V-361) is a horizontally paged sequence of items: an `item[]` shown one or a few at a time within a fixed `viewport`, advanced by a `navigation control` (previous/next) and, where more than a few items exist, a `pagination indicator` marking position within the sequence — the same active-position tracking A-066 Tabs' `indicator` already performs, applied here to items rather than panels. `autoplay`, where present, advances the carousel on a timer independent of any person's input.
**Breaks when** — `autoplay` runs with no `pause control` reachable before, or independent of, the first automatic advance; C035 requires exactly this of any auto-updating content lasting more than five seconds, and an autoplaying carousel advancing every few seconds is squarely that case.
**Also breaks when** — the only way to move between items is a drag or swipe gesture, with no `navigation control` reachable by a single pointer action or by keyboard; C037 requires a single-pointer alternative for any function that uses a dragging movement, and C030 requires the same function to be operable through a keyboard interface regardless of whether a pointer is present at all.

---

## A-104 · Lightbox

`trigger` · `media` · `navigation control` · `zoom control` · `caption`

Lightbox (V-362) is a full-screen overlay for viewing media: enlarged `media` opened from a `trigger` thumbnail, with a `navigation control` to move to the next or previous item where the trigger belongs to a set, an optional `zoom control`, and an optional `caption` (A-091). It reuses A-065 Dialog's `scrim`, `focus trap`, `initial focus`, `return focus`, and `dismissal affordance` in full — a lightbox is a full-screen overlay in exactly A-065's sense, not a distinct overlay construction — and none of those five parameters is restated here.
**Breaks when** — the lightbox opens with no `initial focus` moving onto it and no `focus trap` confining focus while it is open; A-065 already requires both of a scrim-bearing overlay, per C038's meaningful focus order and C031's prohibition on a trap with no escape, and a lightbox that skips either leaves keyboard focus either stranded behind the overlay or free to wander onto page content the scrim is meant to block.
**Also breaks when** — the enlarged `media` has no alt text (V-292) of its own, on the assumption that a `caption`, where present, covers it; A-091 Caption already makes exactly this distinction — C024 requires the text alternative regardless of whether a caption exists, and a caption disappears along with the media if it fails to load while alt text does not, the same gap A-091 names for an image generally, here in the specific case of a lightbox's enlarged view.

---

## A-105 · Toolbar

`container` · `item[]` · `orientation` · `overflow behavior`

Toolbar (V-363) is a grouped row of controls acting on the current context: a `container` holding an `item[]` of heterogeneous controls — buttons, toggles, selects — laid out along an `orientation`, horizontal or vertical. Like a tablist (A-066) or a radio group (A-069), the container is a single stop in the page's focus order; individual items inside it are reached by arrow key, a roving tabindex (V-403), rather than one tab stop per control, regardless of how many different control types the toolbar mixes together.
**Overflow behavior** — scroll, wrap, or collapse into an overflow menu once items exceed the available inline size, the same three options A-066 Tabs already names for a tablist that overflows.
**Breaks when** — the toolbar's items have no programmatic grouping identifying them as one toolbar, or an individual item's own selected or pressed state is not exposed as a state; C046 requires both a group's role and each control's state to be determinable, the same obligation A-069 Radio group already states for its own set of options.
**Also breaks when** — the `overflow behavior`'s collapsed menu opens only on hover, or is built without button semantics; C030 requires it to be operable through a keyboard interface, the same obligation A-082 Navigation's own overflow control already states, not only reachable by a pointer.

---

# M. Link, tabular data, and disclosure

A-106–A-111 below are the ninth and final addition to Vocabulary's `H · Components` part, given their own section for the same reason Sections J, K, and L were: arrival order, not a claim that a link, a table, a data grid, a disclosure, an accordion, or an infinite-scroll mechanism belongs to some category Button, Card, or Callout does not. Each entry drafts the shape the 1.8.1 scoping resolution already settled in **Settled decisions** — none of that resolution's four calls is reopened here. This slice closes Vocabulary's `H · Components` part entirely: after it, no component name in that part remains uncovered by an A-ID.

## A-106 · Link

`label` · `destination` · `leading icon` · `trailing icon` · `hit target` · `state matrix`

Link (V-311) shares Button's (A-062) construction in full — a label with optional leading and trailing icons, sized independently of its hit target and rendered across the state matrix — substituting a `destination` the activating action resolves to in place of an arbitrary action; where a button does something, a link's entire function is arriving somewhere else.
**Distinguished from Button (A-062)** — Vocabulary marks the two "→ distinguish" on exactly this axis: a button performs an action, a link navigates to a location. The same markup, and even the same visual treatment, can implement either; what makes a control a link rather than a button is a stated `destination`, not a class name or a shape.
**Breaks when** — an icon-only link ships with no accessible name independent of the icon's visible form, the same gap A-062 names for an icon-only button; C046 requires a component's name to be programmatically determinable regardless of what is painted.
**Also breaks when** — a link inside running text is distinguished from the surrounding non-link text by color alone, with no underline or other non-color cue present at rest; C023 requires a non-color means of conveying that same distinction.

---

## A-107 · Table

`caption` · `column header[]` · `row[]` (each optional `row header` · `cell[]`) · `cell–header association`

Table (V-332) is a two-dimensional structure of `row[]` read against `column header[]`: an optional `caption` naming what the table represents, a header labeling what each column holds, and a body of rows, each an array of `cell[]` optionally led by its own `row header` where the data reads meaningfully by row as well as by column. Every data `cell` carries a `cell–header association` back to whichever header or headers describe it — the relationship a sighted reader infers for free from position alone, and the one this parameter exists to make explicit.
**Breaks when** — a cell's association to its header exists only as visual position — the nearest label above it, or the leftmost cell in its row — with no association recorded structurally; C046 requires a component's structure, not only its appearance, to be programmatically determinable, and reading the grid one cell at a time with no recorded association loses exactly the meaning position alone supplied.
**Also breaks when** — the visual column order is produced by reordering cells independently of their underlying sequence, so a person reading in source order encounters a different arrangement than a person reading the rendered grid; C038 requires reading order to preserve meaning, and a table whose visual and structural orders diverge breaks that for anyone not reading it visually.

---

## A-108 · Data grid

`sort control` (per column header) · `sort state` · `filter control` · `resize handle` (per column header) · `edit affordance` (`edit state` · `commit control` · `cancel control`)

Data grid (V-333) builds on Table's (A-107) `column header[]`, `row[]`, `cell[]`, and `cell–header association` — reused here in full, the same relationship A-104 Lightbox has to A-065 Dialog — adding only what interaction actually requires: a `sort control` on a column header toggling that column's `sort state` (ascending, descending, or none); a `filter control`, scoped to one column or centralized above the grid, narrowing which rows display; a `resize handle` on a column header's trailing edge adjusting that column's width; and, where a cell is editable, an `edit affordance` opening an `edit state` in place of the cell's display value, resolved by a `commit control` or a `cancel control` rather than left to close on its own.
**Breaks when** — `sort state` is carried by an icon's rotation or fill color alone with no programmatically determinable value behind it; C046 requires a component's state to be reported, not only painted, and a sortable header exposing ascending/descending/none only as a glyph tells anything but a sighted user watching for it nothing about which state currently applies.
**Also breaks when** — dragging a `resize handle` is the only means of changing a column's width; C037 requires a single-pointer alternative to any function using a dragging movement, the same obligation A-072 Slider's thumb and A-075 Dropzone's drop target already meet in their own constructions.

---

## A-109 · Disclosure

`trigger` · `content` · `state`

Disclosure (V-336) is the atomic show/hide unit the rest of this section builds larger constructions from: a `trigger` that toggles whether `content` is shown, holding a `state` — expanded or collapsed — that the trigger's own appearance reflects, commonly a chevron or plus/minus icon that flips or rotates between the two.
**Composes into** — A-110 Accordion, whose `section[]` is an array of this entry.
**Breaks when** — the relationship between `trigger` and `content`, and the state itself, are carried only by the trigger's visual form with no programmatic association tying the two together or reporting whether `content` is currently shown; C046 requires exactly that pairing to be determinable, not only painted.
**Also breaks when** — activating the trigger changes what's visible somewhere outside the trigger's own immediate surroundings — a distant panel, or a region below the current scroll position — with no other signal that anything changed; C008 documents that a change made outside the current fixation, with no motion carrying the eye to it, is frequently not perceived at all, and a disclosure whose only feedback is the distant content itself appearing is exactly that case.

---

## A-110 · Accordion

`group container` · `section[]` (each a Disclosure, A-109) · `expansion mode`

Accordion (V-335) is a set of Disclosures (A-109) collected under one `group container`: each `section` is exactly A-109's `trigger`/`content`/`state` construction, unmodified — the same array shape A-081 Facets already established for its own `applied filter[]`, a list of an already-anatomized unit. What that array shape alone doesn't give Accordion, and what a group of Disclosures needs beyond a repeated Disclosure, is `expansion mode`: exclusive, where opening one `section` closes whichever other section was open, or independent, where each `section`'s `state` moves without affecting its siblings. That coordination belongs to the `group container`, not to any one `section` — the same relationship A-069 Radio group's group container has to its own `radio[]`, each of which stays as simple standing alone as it is inside the group, with the group alone owning whether exactly one member may be selected.
**Breaks when** — an exclusive `expansion mode` collapses a `section` whose `content` holds the current keyboard focus, with focus left inside now-hidden content rather than moved back to that section's own `trigger`; C038 requires the resulting focus sequence to still make sense, and focus stranded inside collapsed, invisible content satisfies that for no one.
**Also breaks when** — the `group container` exposes no programmatic grouping tying its `section[]` together as one coordinated set, only each section's own trigger/content pairing; C046 requires a group's role to be determinable the same way it requires an individual control's, the same obligation A-069 Radio group and A-105 Toolbar already state for their own containers.

---

## A-111 · Infinite scroll

`item[]` · `load trigger` · `loading indicator` · `end state`

Infinite scroll (V-354) appends further `item[]` to a list automatically as a person nears the end of what's currently loaded: a `load trigger` — ordinarily a scroll-position or viewport-intersection threshold near the bottom of the loaded items — fires a fetch, during which a `loading indicator` signals that more content is on its way. That indicator is not a construction of its own: it is A-100 Progress and spinner's `indicator` and `size`, held at indeterminate `determinacy`, since the amount of content still to come is unknown while a fetch is in flight — `value` and `max` have nothing to measure against here the way they do for a determinate bar. An `end state` replaces the `load trigger` once a fetch returns nothing further, so the mechanism stops asking.
**Distinguished from A-080 Pagination** — both address the same underlying need, reaching more of a long result set, but share no parameter set: pagination's `page control[]`, `current indicator`, and `overflow marker` describe discrete, individually addressable pages; infinite scroll has no page boundaries at all, only a continuously growing `item[]` with nothing in the middle to address directly. This entry is an alternative to A-080, not an extension of it the way A-108 Data grid extends A-107 Table.
**Breaks when** — the `loading indicator` runs past roughly 4–5 seconds with no `end state` reached and nothing else changing; C003 sets that threshold directly, the same obligation A-100 already states for its own indeterminate indicator, and a stalled fetch behind an infinite scroll's `load trigger` is exactly that indicator held past its own limit.
**Also breaks when** — newly appended `item[]` arrive below the current viewport with no motion or signal drawing attention to them, and no equivalent reaches anything other than sighted users watching the list grow; C008 documents that a change made outside the current fixation, with nothing carrying the eye to it, is frequently not perceived at all, and a list that grows silently below what's on screen is exactly that case for everyone, not only assistive-technology users.

---

# EXPORT INDEX

| ID | Entry |
|---|---|
| A-001 | The color value |
| A-002 | sRGB |
| A-003 | HSL |
| A-004 | OKLCH |
| A-005 | OKLab |
| A-006 | Display P3 |
| A-007 | Color components |
| A-008 | Hue |
| A-009 | Chroma / saturation |
| A-010 | Lightness vs luminance vs brightness |
| A-011 | Alpha |
| A-012 | Gradient |
| A-013 | Mesh gradient |
| A-014 | Color scale (ramp) |
| A-015 | Contrast |
| A-016 | Blend mode |
| A-017 | Dark theme |
| A-018 | Glyph anatomy |
| A-019 | Font metrics |
| A-020 | Variable font axes |
| A-021 | The text block |
| A-022 | Type scale |
| A-023 | OpenType features |
| A-024 | Font loading |
| A-025 | The box |
| A-026 | Corner |
| A-027 | Stroke |
| A-028 | Shadow |
| A-029 | Elevation |
| A-030 | Blur |
| A-031 | Glass surface |
| A-032 | Fill |
| A-033 | Mask and clip |
| A-034 | Noise and grain |
| A-035 | Pattern |
| A-036 | Spacing scale |
| A-037 | Grid |
| A-038 | Flex |
| A-039 | Position |
| A-040 | Stacking context |
| A-041 | Breakpoint |
| A-042 | Fluid value |
| A-043 | Timing |
| A-044 | Easing |
| A-045 | Cubic-bézier |
| A-046 | linear() |
| A-047 | Spring |
| A-048 | Transform |
| A-049 | Choreography |
| A-050 | Micro-interaction |
| A-051 | Scroll-driven animation |
| A-052 | Reduced motion |
| A-053 | Raster image |
| A-054 | Responsive image |
| A-055 | SVG |
| A-056 | Icon |
| A-057 | The state matrix |
| A-058 | Focus ring |
| A-059 | Hit target |
| A-060 | Feedback loop |
| A-061 | Form field |
| A-062 | Button |
| A-063 | Card |
| A-064 | Tooltip and popover |
| A-065 | Dialog |
| A-066 | Tabs |
| A-067 | Text input |
| A-068 | Checkbox |
| A-069 | Radio group |
| A-070 | Switch |
| A-071 | Select and combobox |
| A-072 | Slider |
| A-073 | Stepper |
| A-074 | Segmented control |
| A-075 | Dropzone |
| A-076 | Fieldset |
| A-077 | Menu |
| A-078 | Command palette |
| A-079 | Breadcrumb |
| A-080 | Pagination |
| A-081 | Facets |
| A-082 | Navigation |
| A-083 | Skip link |
| A-084 | Headline |
| A-085 | Deck |
| A-086 | Eyebrow |
| A-087 | Byline |
| A-088 | Body |
| A-089 | Pull-quote |
| A-090 | Stat/callout |
| A-091 | Caption |
| A-092 | CTA text |
| A-093 | List |
| A-094 | Metadata block |
| A-095 | Toast and banner |
| A-096 | Callout |
| A-097 | Badge |
| A-098 | Chip |
| A-099 | Avatar |
| A-100 | Progress and spinner |
| A-101 | Skeleton |
| A-102 | Empty and zero state |
| A-103 | Carousel |
| A-104 | Lightbox |
| A-105 | Toolbar |
| A-106 | Link |
| A-107 | Table |
| A-108 | Data grid |
| A-109 | Disclosure |
| A-110 | Accordion |
| A-111 | Infinite scroll |

---

## Settled decisions

**Components was the chosen slice of the four named in README's "What is not covered," over tokens, information architecture, and content.** Vocabulary's `H · Components` part (V-310–V-364) already names roughly forty-five components with no anatomy anywhere in the suite, which made this the gap with the most existing scaffolding and the clearest boundary to work inside. Information architecture and content are not rendering primitives in the sense the rest of this document is, and each looks like it wants its own organizing shape rather than a bolt-on section here; both remain left for a scoping discussion before either gets A-IDs, not attempted in this pass. Tokens do not remain open the same way — see the settled finding below.

**Tokens are settled out of scope for Anatomy, not deferred.** A later scoping pass, run specifically to close the "left for a scoping discussion" note above, found no parameter, range, or derived fact about a token that this document does not already own by another route. Implementation's `T`-namespace owns the token wrapper itself — the reference-tier structure, the naming grammar, and the DTCG-mandated envelope (`$value`, `$type`, `$description`, `$deprecated`, `$extensions`, and the reference/aliasing syntax) — none of which describes anything that renders; it describes a build pipeline's own bookkeeping, which is Implementation's stated ownership ("how a choice becomes a token, component, or line of code"), not this document's. Every value a token can hold, in turn, resolves to a parameter set already published under its own A-ID: a color-ramp step to A-014, spacing to A-036, a radius to A-026, a shadow to A-028, a duration or easing curve to A-043–A-047, typography to A-018–A-024, a breakpoint to A-041 — and the DTCG spec's composite types (border, shadow, gradient, typography, transition) don't introduce new value-parameters beyond these either, they wrap them. Even the two candidates that looked most like Anatomy-shaped derived facts turn out to already be stated here: a token's inner-radius-from-outer-radius derivation is A-026's own **Derived** line, and its multi-layer shadow requirement is A-028's own **Layered shadow** construction. Unlike A-001 "the color value" or A-020's variable font axes, which are genuinely prior to and independent of any particular format, a design token has no shape independent of the tooling decision to represent a value as referenceable, typed, buildable data — drafting an Anatomy entry for it would either re-derive the DTCG spec Implementation already cites correctly, or re-list parameters this document has already published under other A-IDs. Information architecture and content are unaffected by this finding and remain open questions for a future scoping pass, as stated above; only tokens close here.

**Five entries, not forty-five.** A-062–A-066 cover Button, Card, Tooltip/Popover, Dialog, and Tabs: the components most others in Vocabulary's `H` part either compose from directly (a card holding buttons, a dropdown menu sharing tooltip/popover placement anatomy) or differ from structurally (a dialog's scrim and focus trap, a tabs set's roving tabindex). This is a first slice, not the volume — the remaining names in V-310–V-364 (inputs and their variants, menus, toasts and banners, badges and chips, avatars, and the rest) are additive follow-up work under new A-IDs, each its own bounded contribution rather than one PR closing the whole part.

**Variant terms did not each get their own A-ID.** Icon button, ghost button, floating action button, and split button (V-312–V-315) are noted as sub-parts of A-062 rather than given separate entries, because none of them changes the parameter set — only which parameters are present, absent, or fixed. This mirrors how A-012 Gradient covers linear, radial, and conic without separate IDs, reserving a new entry for Mesh gradient (A-013) only because its parameters genuinely differ. The same reasoning folds non-modal dialog, drawer, and sheet (V-338–V-340) into A-065 rather than three further entries.

**Which choices exist among these parts, and how a choice becomes a built component, stayed out.** Several drafts of these entries drifted toward saying which affordance to prefer or how a state trap is coded; both were cut. Composition owns the range of choice, Implementation owns the build, and an entry that started prescribing either was rewritten back down to the parts and their ranges — this document's own boundary, not a new one invented for components.

**Second slice: input controls, ten entries covering twelve of Vocabulary's `H` names.** A-067–A-076 add Text input (folding V-316 Input and V-317 Textarea), Checkbox, Radio group, Switch, Select and combobox (folding V-321 and V-322), Slider, Stepper, Segmented control, Dropzone, and Fieldset. This group was chosen over menus, toasts and banners, badges and chips, and avatars — the other groups the first slice's settled decisions named as remaining — because inputs are what most other components in Vocabulary's `H` part are built to sit *beside* rather than compose from, and because a website's accessibility and legal exposure concentrates disproportionately in form controls, making this the highest-leverage remaining gap rather than only the most obvious one.

**Label, placeholder, and helper text (V-318–V-320) were deliberately left out of this slice**, not overlooked. A-061 Form field, already in this document before this contribution, lists `label`, `placeholder`, `helper text`, and `error message` as parameters of its wrapper; reopening those three names here would either duplicate A-061 or contradict it. The gap this leaves — A-061's parameter list names them in English without citing V-318, V-319, or V-320 by ID — is real but sits inside an existing entry this contribution does not touch. Noted here so it is not rediscovered as new.

**Checkbox, radio group, and switch stayed three entries, not one.** The precedent A-064 Tooltip/Popover and A-065's dialog family set folds variants that share an identical parameter set and diverge only in which parameters are present, absent, or fixed. These three don't clear that bar: a checkbox's indicator is a box with an optional mark, a switch's is a track and a thumb, and a radio's is a set of options with group-level navigation absent from either — three different constructions wearing a similar "toggle" reputation, which is exactly the confusion V-608 exists to correct. Select and combobox, by contrast, do clear that bar — the same trigger/panel/option construction, diverging only in whether the trigger accepts typed text — and were folded into one entry, A-071, on the same reasoning A-064 already established.

**Still open after this slice.** Menus (dropdown, context, command palette), toasts and banners, callouts, badges and chips, avatars, breadcrumb and pagination, progress and spinner, skeleton and empty/zero state, facets, carousel, lightbox, toolbar, and hamburger menu remain uncovered in Vocabulary's `H` part. Each is additive follow-up work under further new A-IDs, on the same terms this document has already set twice.

**Third slice: the menu family, two entries covering three of Vocabulary's `H` names.** A-077 Menu folds dropdown menu (V-343) and context menu (V-344) into one entry on the same "shares a parameter set, diverges only in what's present or fixed" test A-064 and A-071 already established; A-078 Command palette (V-345) stays separate because it has no anchor element at all — no `placement`, `offset`, or `collision behavior` to inherit from A-064's popover machinery — and adds a `query input` and `result[]` construction the other two don't have. This group was chosen over toasts and banners, callouts, badges and chips, avatars, breadcrumb and pagination, progress and spinner, skeleton and empty/zero state, facets, carousel, lightbox, toolbar, and hamburger menu — the full list the second slice's settled decisions left open — because it reuses more of this document's own published anatomy than any other remaining group (A-064's placement/offset/collision-behavior parameters, V-403's roving-tabindex pattern already used by A-066 and A-069) while still containing genuine new parts (`item`, `submenu indicator`, `query input`), making it the tightest-bounded remaining slice rather than only the next one on the list. It also carries the same order-of-magnitude accessibility exposure the second slice cited for input controls: a context menu with no keyboard-reachable equivalent, or a command palette that fails to move focus into its own query field, is a WCAG failure a screen-reader or keyboard-only user hits immediately, not an edge case.

**Still open after this slice.** Toasts and banners, callouts, badges and chips, avatars, breadcrumb and pagination, progress and spinner, skeleton and empty/zero state, facets, carousel, lightbox, toolbar, and hamburger menu remain uncovered in Vocabulary's `H` part. Each is additive follow-up work under further new A-IDs, on the same terms this document has already set three times.

**Content is settled as atomic content elements, not content types.** The scoping discussion the first Settled decisions entry above deferred (issue #10) resolves in favor of the same "primitives before composition" order this document already used for components: a future contribution gets A-IDs for content *elements* — Headline, Deck, Eyebrow, Byline, Body, Pull-quote, Stat/callout, Caption, CTA text, List, and Metadata block are the candidate set — each carrying a parameter set, a length range, and a required/optional status, the same shape as A-061 Form field or A-062 Button. This is chosen over content *types* (Article, Product listing, Case study, and the like): Section H's first slice could be scoped tightly because Vocabulary's `H · Components` part already named roughly forty-five components before any of them had anatomy; no equivalent closed list of content types exists anywhere in the suite, so there is nothing bounded to scope a types-first slice against. Types are not ruled out — they are a natural second slice once an element vocabulary exists to compose them from, the same relationship Section H's components have to the primitives in Sections A–G, just not first. **A known dependency, flagged for whoever writes that future slice rather than resolved here:** several of these candidate names have no Vocabulary ID yet — headline, body, byline, eyebrow, and caption do not appear in Vocabulary's `L · Content and language` part (V-500–V-513) or anywhere else, unlike deck (V-505) and call to action (V-504), which already exist. Anatomy may cite Vocabulary but not coin a term of its own, so the content-elements contribution will need a small companion Vocabulary addition alongside it. This entry adds no A-ID; it closes the scoping question the same way the tokens finding earlier in this section closed its own, leaving the content slice itself as separately scoped future work.

**Information architecture is settled to the component-entry shape only, narrower than the scoping research's hybrid recommendation.** The scoping discussion the first Settled decisions entry above deferred (issue #11) resolves in favor of Option A alone: IA anatomy will use the same component-entry template already proven three times (A-062–A-066, A-067–A-076, A-077–A-078). Breadcrumb (V-352), pagination (V-353), facets (V-360, the component; V-536 names the faceted-navigation pattern it belongs to), the nav-variant components — global navigation (V-533), local navigation (V-534), utility navigation (V-535) — and skip link (V-405) are the candidates that fit that template; hamburger menu (V-364) is a likely sub-part of a nav entry rather than its own, on the same "shares a parameter set, diverges only in what's present or fixed" test A-062 already applied to icon button, ghost button, floating action button, and split button. The "site-as-graph" relational shape the research also proposed as part of a hybrid — page nodes, link edges, depth, and path between them — is rejected for this document, not folded in alongside the component entries: a graph of pages and links is not "what a thing is made of, in parameters" (`suite-architecture.md` §2); it is closer to what Composition's F11–F14 already own as choices with ranges (F11 Topology's site shape and page count, F12 Navigation's model and cross-linking density, F13 Path's linearity and locus of control, F14 Addressing's URL legibility and canonical discipline), or to what Diagnosis does when reading a site's actual structure back. Mixing a second internal organizing shape into this document for one section would make Anatomy inconsistent with itself everywhere else it doesn't use that shape. Two further exclusions, made explicit rather than left silent: taxonomy (V-530) and ontology (V-531) are classification-scheme facts — what something is called or classified as — which is Vocabulary-shaped, not Anatomy-shaped, and stay out of this document; and the research-method and deliverable terms in Vocabulary's `M` part — card sorting (V-538), tree testing (V-539), mental model (V-540), journey map (V-542), wireframe (V-543), mockup (V-544), prototype (V-545), and fidelity (V-546) — are practitioner process artifacts, not something a website itself is made of, and are entirely out of scope for Anatomy. This entry adds no A-ID; it closes the scoping question the same way the content entry above closes its own, leaving the IA slice itself as separately scoped future work.

**Fourth slice: information architecture, five entries covering the full candidate set the IA scoping resolution above named.** A-079 Breadcrumb and A-080 Pagination stay separate entries rather than folding into one, on the same test A-068, A-069, and A-070 already set for checkbox, radio group, and switch: a breadcrumb's parts are a hierarchy trail ending in a non-link current item, a pagination's are a row of sibling page controls flanked by previous/next and an overflow marker — different constructions that share a passing resemblance ("a row of links marking position") without sharing a parameter set, not the same construction wearing two labels. A-081 Facets stays its own entry for the same reason, composed from A-068 Checkbox and A-072 Slider rather than duplicating either. A-082 Navigation folds global navigation (V-533), local navigation (V-534), and utility navigation (V-535) into one entry, on the same "shares a parameter set, diverges only in what's present or fixed" test A-071 and A-077 already established for select/combobox and the menu family: all three are a landmark containing a list of items, differing only in scope. Hamburger menu (V-364) folds into that same entry as its `overflow control` rather than getting an entry of its own, exactly as the scoping resolution above anticipated: it conceals the same items the surrounding navigation entry already anatomizes, adding a trigger-and-disclosure-panel construction this document has already published at A-064 and A-077, not a new one. A-083 Skip link stays separate: a single link with no siblings and no group, whose entire function is changing where focus lands next — closer in shape to a focus-management primitive than to any of the other four entries in this slice.

This is the whole named candidate set from the IA scoping resolution: breadcrumb, pagination, facets, the nav-variant trio, hamburger menu, and skip link. Nothing from that named set is deferred out of this pass — it was bounded tightly enough at scoping time that finishing it in one slice, the way the third slice finished the whole menu family in one pass, was more consistent than splitting it further with no boundary to split along. The site-as-graph shape, taxonomy, ontology, and the research-method and deliverable terms that same resolution rejected for this document stay rejected; nothing here reopens them.

**Still open after this slice.** Toasts and banners, callouts, badges and chips, avatars, progress and spinner, skeleton and empty/zero state, carousel, lightbox, and toolbar remain uncovered in Vocabulary's `H` part. Content elements (Headline, Deck, Eyebrow, Byline, Body, Pull-quote, Stat/callout, Caption, CTA text, List, and Metadata block) remain the other settled-but-undrafted slice, per the entry above this one. Each is additive follow-up work under further new A-IDs, on the same terms this document has already set four times.

**Fifth slice: content, eleven entries covering the full candidate set the content scoping resolution above named.** A-084–A-094 add Headline, Deck, Eyebrow, Byline, Body, Pull-quote, Stat/callout, Caption, CTA text, List, and Metadata block — the complete named candidate set, anatomized as atomic content elements per that resolution's own decision, not as content types. The resolution flagged a dependency rather than resolving it: eight of the eleven candidates — Headline, Eyebrow, Byline, Body, Pull-quote, Caption, List, and Metadata block — had no Vocabulary ID; Deck (V-505) and Call to action (V-504) already did; Callout (V-348) covers the "callout" half of the eleventh candidate but not its "stat" half, which named a genuinely distinct concept — a highlighted number or metric, not an inline box of supplementary text — and so was not folded into Callout's existing meaning rather than given its own term. Closing that dependency added nine new Vocabulary entries, V-613–V-621, appended to the end of Part L (Content and language) — physically after V-513 Colophon, numbered from V-613 because Vocabulary's IDs are flat and V-612 was the last one assigned regardless of part, not from the unused 514–529 range Part L's own numbering block would otherwise suggest — cited here by the entries above rather than restated.

Only one fold happened in this slice: Stat and Callout share one construction — a short block set apart from body text — and diverge only in whether the content at its center is a `value` or `text`, the same "shares a parameter set, diverges only in what's present or fixed" test A-071, A-077, and A-082 already applied; that test was checked and rejected for every other pair in the candidate set. Headline and Deck stay separate despite Deck's definition naming Headline directly, because a headline is required where a deck is not and each carries its own length range; the same reasoning keeps Eyebrow and Byline separate from Headline. Body and Pull-quote stay separate because a pull-quote's text is drawn from, not independent of, the body it excerpts — a sourcing relationship no other pair in this slice has. CTA text (A-092) stays scoped to the text parameter alone, not the whole control, because the control itself already has an entry — A-062 Button, or V-311 Link where the CTA is a link rather than a button — and duplicating either here would restate rather than cite.

**Still open after this slice.** Toasts and banners, callouts, badges and chips, avatars, progress and spinner, skeleton and empty/zero state, carousel, lightbox, and toolbar remain uncovered in Vocabulary's `H` part — the same nine names the fourth slice's own note above left open, unchanged by this slice, which drew from Vocabulary's `L` part instead. **Callout (V-348) as a standalone `H`-part component is not among them by omission:** A-090 Stat/callout above cites V-348 for the content-element sense of a callout — a short block of supplementary text embedded in running content — not for the general case a future `H`-part entry would still need to cover on its own terms: a callout with a severity or intent (info, warning, success, danger), an icon, and an accent color keyed to that severity is a richer construction than anything anatomized here, and stays open under the `H`-part list above rather than being treated as closed by implication. Content is otherwise fully drafted — every candidate the content scoping resolution named now has an A-ID. Only the `H`-part remainder above stays open for Anatomy volume 2, on the same terms this document has already set five times.

**Sixth slice: message surfaces, two entries covering three of Vocabulary's `H` names.** A-095 Toast and banner folds toast (V-346) and banner (V-347) into one entry on the same "shares a parameter set, diverges only in what's present, absent, or fixed" test A-065 established first, for modal, non-modal dialog, drawer, and sheet, and A-071, A-077, A-082, and A-090 have each since reused: both are a surface carrying an optional icon, a short message, an optional action, and a dismissal affordance, keyed to an intent, diverging only in placement (a toast is a fixed overlay; a banner sits inline in the page), duration (a toast times out; a banner ordinarily carries none), and stacking (a toast stacks above its siblings; a banner does not) — the same order of divergence A-065 already tolerated along a placement axis to fold four Vocabulary terms into one entry, applied here to two. A-096 Callout resolves the fold-or-separate question the fifth slice's own note above left open, and resolves it against folding with either candidate that note implied: against A-095, a callout carries no `dismissal affordance`, no `duration`, and no `placement` variance of its own — it is a fixed part of whatever content it sits in, not a transient or page-level notification, a difference in construction and not only in which of a shared parameter set is present, absent, or fixed. Against Badge (V-349) and Chip (V-350), which remain open below, the constructions differ even further: a badge is a marker with no message text of its own, typically a count or a dot, attached to another element rather than standing apart from one; a chip is a compact, often-removable tag representing a single attribute, filter, or selection, already partially anatomized as A-081 Facets' `applied filter`. None of the three — badge, chip, callout — clears the fold test against either of the others; three different constructions sharing a "small, colored, meaningful" reputation, the same shape of near-miss A-068, A-069, and A-070 already rejected for checkbox, radio group, and switch. A-096 cites the same V-348 A-090 Stat/callout already cites — not a new use of the ID, but the second, richer sense that entry's own note anticipated and named as still uncovered; see A-096 itself for why the two citations describe different constructions without conflicting.

**A re-verification against Vocabulary's full `H` part, done while scoping this slice, found the "still open" bookkeeping above was itself incomplete.** This document's citations of V-310–V-364 (55 names) account for 35 of them before this slice — the 32 `ROADMAP.md`'s Phase 2 entry already counts across the first four slices, plus Label, Placeholder text, and Helper text (V-318–V-320), folded into the pre-existing A-061 Form field rather than counted in that 32 — leaving 20 open, not the 14 named across the "still open" paragraphs above. The other six were cited nowhere in this document and named in none of those paragraphs: Link (V-311), Table (V-332), Data grid (V-333), Accordion (V-335), Disclosure (V-336), and Infinite scroll (V-354). Link is not entirely absent — A-092 CTA text names it in passing, "ordinarily a Button (A-062) or a Link (V-311)" — but it has no anatomy entry of its own, the same as the other five. Grouping, folding, and scoping these six is exactly the kind of call `AGENTS.md` reserves for a human decision rather than one made unilaterally inside a task, so it is opened as issue #48 rather than drafted here. `ROADMAP.md`'s "~23" figure for the remaining count is corrected in the same commit as this entry, to the verified total: 20 before this slice, 17 after — the 11 already named above (badges and chips, avatars, progress and spinner, skeleton and empty/zero state, carousel, lightbox, toolbar) plus the six this re-verification surfaced.

**Still open after this slice.** Badges and chips, avatars, progress and spinner, skeleton and empty/zero state, carousel, lightbox, and toolbar remain uncovered in Vocabulary's `H` part, unchanged by this slice apart from the removal of toasts, banners, and callouts. Link, Table, Data grid, Accordion, Disclosure, and Infinite scroll join the open list for the first time here, per the re-verification above — never covered, but also never previously named as open in this section; see issue #48. Content elements remain the other settled-but-undrafted slice, per the fourth and fifth slices' own notes. Seventeen names remain open in the `H` part in total; each is additive follow-up work under further new A-IDs, on the same terms this document has already set six times.

**Seventh slice: badges and chips, two entries covering two of Vocabulary's `H` names.** A-097 Badge and A-098 Chip were chosen over the ten other names still open after the sixth slice (avatars, progress and spinner, skeleton and empty/zero state, carousel, lightbox, toolbar) and the six issue #48 surfaced (Link, Table, Data grid, Accordion, Disclosure, Infinite scroll) for two reasons together, not either alone: both were already partially characterized by the sixth slice's own "Not folded with Badge or Chip" paragraph in A-096 — which had to describe both terms accurately enough to justify not folding Callout into either — leaving less new ground to cover than any other remaining name; and, unlike the six issue #48 names, neither carries an open scoping call. Table/Data grid raises a genuine fold-or-separate question (the pair carries a Vocabulary "→ distinguish" cross-reference, the same signal that preceded folds elsewhere in this document); Accordion and Disclosure carry no such marker between them — that claim, made here originally, did not hold up against a direct check of Vocabulary's text and is corrected by the scoping entry below — but the pair still raises a real composition question of its own. Link and Infinite scroll each raise a where-does-this-land question. Issue #48 itself reserves all six for a human scoping call on the same grounds `AGENTS.md` gives for tokens, content, and information architecture before them, and this slice does not make that call. A-097 and A-098 stay two entries rather than one: A-096 already tested Badge and Chip against Callout and against each other and found "none of the three... clears the fold test against either of the others" — a determination this slice builds anatomy from rather than re-litigates. Chip's `state` parameter is not new ground either; A-081 Facets' `applied filter` already used a chip this way, and A-098 cites that continuity instead of restating it.

**Still open after this slice.** Avatars, progress and spinner, skeleton and empty/zero state, carousel, lightbox, and toolbar remain uncovered in Vocabulary's `H` part, unchanged by this slice apart from the removal of badges and chips. Link, Table, Data grid, Accordion, Disclosure, and Infinite scroll remain open too, each still carrying its own scoping call per issue #48, not decided here. Content elements are unaffected by this slice and remain fully drafted, per the fifth and sixth slices' own notes. Fifteen names remain open in the `H` part in total; each is additive follow-up work under further new A-IDs, on the same terms this document has already set seven times.

**Eighth slice: avatars, progress and spinner, skeleton and empty/zero state, carousel, lightbox, and toolbar — seven entries covering nine of Vocabulary's `H` names.** These are the six names `ROADMAP.md` Phase 2 names as ready to draft without a human scoping call, distinct from the six issue #48 reserves for one (Link, Table, Data grid, Accordion, Disclosure, Infinite scroll, none of which this slice touches). All nine Vocabulary IDs this slice cites — Avatar (V-351), Progress bar (V-355), Spinner (V-356), Skeleton (V-357), Empty state (V-358), Zero state (V-359), Carousel (V-361), Lightbox (V-362), Toolbar (V-363) — already existed before this slice; none required a companion Vocabulary addition of the kind the fifth slice needed for content elements. A-099 Avatar is one entry for one name; A-103 Carousel, A-104 Lightbox, and A-105 Toolbar are each one entry for one name; two fold decisions account for the rest.

**A-100 Progress and spinner folds Progress bar (V-355) and Spinner (V-356).** Vocabulary marks the pair "→ distinguish," the same signal the seventh slice's own note observed "preceded folds elsewhere in this document" for Table/Data grid — and, further back, is exactly the signal Toast/Banner (V-346/V-347) and Tooltip/Popover (V-342/V-341) carried before A-095 and A-064 folded each pair. The fold test applied here is the one A-095 established: do the two share a parameter set, diverging only in what's present, absent, or fixed? They do — a `track` carrying an `indicator`, `label`, and `size` common to both — and this document had already treated them as one continuum before this slice existed to give it parameters: A-060 Feedback loop's own text reads "Determinate where possible; indeterminate spinners past that point read as failure regardless of what is happening," naming determinate progress and indeterminate spinners as two settings of the same thing, not two things. A-100's `determinacy` parameter is what that continuum needed and didn't yet have. This is a stronger case for folding than Toast/Banner was, not a weaker one — Toast and Banner are siblings under a common ancestor; Progress bar and Spinner are, on this document's own prior wording, already the same construction observed at two points along one axis.

**A-102 Empty and zero state folds Empty state (V-358) and Zero state (V-359).** This is a different, and easier, kind of fold than any of the above: Vocabulary does not merely flag the pair "→ distinguish," it defines one directly in terms of the other — its Zero state entry frames zero state as empty state's first-encounter subtype, a subtype relationship Vocabulary states outright, not a resemblance this slice had to establish itself. Where the toast/banner and progress/spinner folds required showing two nominally distinct siblings share a parameter set, this fold starts from that stated relationship. A-102 accordingly does not introduce a `V-359`-only parameter anywhere the `V-358` construction lacks one; the only thing that changes between the two is the value of a `moment` parameter (first-run versus later) and, downstream of that, what the `message text` and `action` say — the same "parameter's value, not its presence" distinction A-095 itself draws between a toast's fixed placement and a banner's inline one. The alternative considered and rejected was treating Zero state as a *sub-part* of Empty state the way icon button, ghost button, floating action button, and split button are sub-parts of A-062 Button, rather than giving it a place in the entry's own title. That precedent was set for variant terms that do not independently carry the weight of a two-word phrase in ordinary usage the way "zero state" does, and `ROADMAP.md`'s own Phase 2 entry already names the pair as "empty/zero state," one unit a reader would look up by either half; a title of "Empty state" alone, with zero state buried in prose, would cite V-359 without a reader being able to find it from the export index the way every other Vocabulary ID this document cites can be found.

**Skeleton (A-101) stays its own entry rather than folding with A-100 Progress and spinner**, despite both occupying the same "loading" moment in a page's lifecycle: a skeleton previews the *shape* of content not yet confirmed to exist in a given form — a set of `shape[]` matching a specific layout — while a progress bar or spinner communicates only that work is occurring, with no claim about what the result will look like. That is a difference in construction, not only in which of a shared parameter set is present, absent, or fixed, the same distinction A-096 Callout drew against A-095 Toast and banner to justify staying separate rather than folding.

**Scoping call: Link, Table/Data grid, Accordion/Disclosure, and Infinite scroll.** Issue #48 surfaced these six names and reserved grouping, folding, and landing them for a human scoping call, the same way tokens (issue #13), information architecture (issue #11), and content (issue #10) were each reserved and resolved before drafting. That issue was closed once the bookkeeping gap it actually reported — six names cited nowhere and named in none of this document's "still open" notes — was fixed; the scoping call itself was never made, leaving six "per issue #48" references in this section pointing at a closed issue that no longer reserves anything. This entry makes the call issue #48 existed to gate, using the tests this document has already established for a fold, a composition, and a where-does-this-land question.

*Link (V-311)* — no ambiguity: a standalone entry, the same shape as A-062 Button, which Vocabulary already distinguishes it from ("→ distinguish V-310") the same way it flagged every pair this document has since folded or kept apart. It is simply undrafted, not contested.

*Table (V-332) and Data grid (V-333) stay two entries, not one*, despite Vocabulary's "→ distinguish" marker being the same signal that preceded three folds in this document (Tooltip/Popover, Toast/Banner, Progress and spinner). That marker precedes a fold only when the pair also passes A-095's actual test — sharing a parameter set and diverging only in what's present, absent, or fixed. The obvious counter-reading is that it does: "sortable: yes/no" or "editable: yes/no" can be written as a boolean parameter present in one and absent in the other, satisfying the test's literal wording the same way A-100's `determinacy` does. That reading is rejected here because a present/absent *parameter* still describes the same *part* in both states — A-100's `track` and `indicator` exist whether `determinacy` is determinate or not; A-102's `illustration`, `message text`, and `action` exist at both values of `moment`. Sorting a column, filtering a set of rows, and editing a cell each require a part with no analog in a plain table at all — a sort control per header, a filter control, a cell-level edit affordance and its own commit/cancel state — not an existing table part switched off. A boolean flag can describe *that a capability exists*, but the capability itself is new structure, not a hidden or defaulted-off parameter of Table waiting to be turned on; this is the same distinction A-101 Skeleton drew against A-100 to justify staying separate, applied here to a pair whose Vocabulary marker alone would otherwise point toward folding. Data grid's own parameter list is the next slice's work, not settled here; what's settled is only that it will build on Table's core structural parameters rather than fold into a single entry with them, the same relationship A-104 Lightbox has to A-065 Dialog.

*Accordion (V-335) and Disclosure (V-336) stay two entries, not one, but for a different reason than Table/Data grid: this was never a fold question.* Vocabulary carries no "→ distinguish" marker between them at all — the seventh slice's note claiming otherwise is corrected above. Disclosure is the atomic unit: a single show-and-hide toggle. Accordion is a group of that unit: "vertically stacked collapsible sections," which is Disclosure repeated and stacked, not a different construction wearing a similar name. The array shape is the one A-081 Facets already established for its own `applied filter[]` (each a chip): Accordion's entry defines a `section[]` where each section is a Disclosure (A-1XX). But Facets' array is the weaker half of this precedent — each applied filter is independently removable, with no coupling between siblings, where Accordion's single-open-vs-multi-open behavior is exactly that coupling: opening one section can close another. A-069 Radio group is the closer precedent for that half: a `group container` holding two or more independently-simple options (`radio[]`, each carrying only `indicator` and `label`), with the group itself — not any option — owning the exactly-one-selected coordination. Accordion's group-level parameter is the same shape: each section stays as simple as a standalone Disclosure, and the array's container, not the sections themselves, owns whether expansion is exclusive or independent. Structurally a Facets-style array of an already-anatomized unit; behaviorally a Radio-group-style coordinating container over that array — citing both rather than Facets alone.

*Infinite scroll (V-354)* shares no parameter set with A-080 Pagination's `page control[]`, `current indicator`, and `overflow marker` — it is an alternative mechanism for the same underlying need (reaching more of a long result set), not a variant of pagination's own construction, so it is not folded with Pagination and does not extend it the way Data grid extends Table. What it reuses from A-100 Progress and spinner is narrower than a whole-construction borrowing: its own loading state has no known total while more content is still arriving, so it is `indicator` and `size` at A-100's indeterminate `determinacy` — the spinner half of that entry, not `value`/`max`, which infinite scroll's own entry will have no use for. It cites A-080 Pagination as the alternative mechanism a design chooses instead of, the way A-104 Lightbox cites A-065 Dialog for parameters it reuses without owning — narrower in what's reused than Lightbox's five, but naming which parameters rather than gesturing at the construction as a whole.

This entry resolves the scoping call; it does not draft the six entries themselves; that is the next slice's work, following the shape resolved here.

**Still open after this slice.** Link, Table, Data grid, Accordion, Disclosure, and Infinite scroll are the only names remaining open in the `H` part — no longer carrying an open scoping call, per the entry above, but not yet drafted. Content elements, information architecture, and tokens are unaffected by this slice and remain settled per the earlier entries in this section. Six names remain open in the `H` part in total, correcting the fifteen the seventh slice's own note above left open by the nine this slice closes; each is additive follow-up work under further new A-IDs, on the same terms this document has already set eight times.

**Ninth slice: Link, Table, Data grid, Disclosure, Accordion, and Infinite scroll — six entries covering the last six names in Vocabulary's `H · Components` part.** A-106–A-111 draft the anatomy the scoping entry above already settled, reopening none of its four calls. A-106 Link stands alone, parallel to A-062 Button, substituting a `destination` parameter for Button's own action-bearing construction. A-107 Table and A-108 Data grid stay two entries: A-107 anatomizes the row/column-header/cell structure common to both; A-108 reuses that structure in full and adds only what sorting, filtering, resizing, and editing actually require — a `sort control` and `sort state`, a `filter control`, a `resize handle`, and an `edit affordance` — the same relationship the scoping entry named to A-104 Lightbox's reuse of A-065 Dialog. A-109 Disclosure and A-110 Accordion stay two entries for the different reason the scoping entry gave: Disclosure is the atomic `trigger`/`content`/`state` unit; Accordion is a `group container` holding a `section[]` of that unit — structurally the array shape A-081 Facets already established for `applied filter[]` — with an `expansion mode` parameter on the group itself, exclusive or independent, the same exactly-one-selected coordination A-069 Radio group's own `group container` already owns over its `radio[]`, applied here to whether more than one section may stay open at once. A-111 Infinite scroll stands alone, sharing no parameter set with A-080 Pagination's `page control[]`, `current indicator`, and `overflow marker` — an alternative mechanism for reaching more of a long result set, not a variant of pagination's own construction — and reuses only A-100 Progress and spinner's `indicator` and `size` at indeterminate `determinacy` for its own `loading indicator`, narrower than Data grid's full-structure reuse of Table and narrower than Lightbox's five-parameter reuse of Dialog.

**Still open after this slice.** None. Vocabulary's `H · Components` part (V-310–V-364, 55 names) is now fully covered by this document. Content elements, information architecture, and tokens remain settled per the earlier entries in this section. No component name in Vocabulary's `H` part remains open for a future Anatomy volume-2 slice; the gap `ROADMAP.md` Phase 2 has tracked across all nine slices is closed.
