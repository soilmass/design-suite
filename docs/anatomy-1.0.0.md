```yaml
document: Anatomy
version: 1.1.0
tier: 1
scope: rendering primitives (color, typography, shape, space, motion, imagery, state), plus a first slice of component anatomy
owns:
  - what each thing is made of, expressed as parameters
  - the range or type of each parameter
  - what is derived rather than chosen
exports: A-001–A-066
depends:
  - Vocabulary ^1
  - Constraints ^1
reviewed: 2026-09-03
```

# Anatomy

What each thing is made of. Where Vocabulary establishes what a term denotes, this document takes the thing apart: the parameters it consists of, what values those accept, what it composes into, and what can be derived rather than chosen.

**Scope of 1.1.0** — rendering primitives, plus a first slice of component anatomy: Button, Card, Tooltip/Popover, Dialog, and Tabs (A-062–A-066). The rest of components, tokens, information architecture, and content are not yet covered; they enter as additive minor versions with new A-IDs.

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
**measure** — expressed in `ch` units or a max-width. 45–75 characters, 66 as the classic target.
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

**The responsive card formula**
`repeat(auto-fit, minmax(min(100%, 280px), 1fr))`
Parts: `auto-fit` collapses empty tracks so items stretch · `minmax` sets the floor and lets them grow · the inner `min()` prevents overflow when the container is narrower than the floor.

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
**Better practice** — set breakpoints where the *content* breaks, not at device widths.

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
**Progress** — required past about 1 second. Determinate where possible; indeterminate spinners past 4–5 seconds read as failure regardless of what is happening.
**Resolution** — success needs confirmation proportional to the stakes. A saved draft needs a whisper; a deleted account needs a sentence.
**Recovery** — every failure state needs a stated cause and a next action. "Something went wrong" satisfies neither.

**Latency thresholds** — C001, C002, C003.

---

## A-061 · Form field

`label` · `input` · `placeholder` · `helper text` · `error message` · `required indicator` · `character count` · `prefix/suffix` · `clear affordance` · `autocomplete token` · `inputmode` · `pattern`

**Validation timing dimensions** — `on submit` · `on blur` · `on change while already invalid` · `on change always`
The usual correct combination: validate on blur, then re-validate on every change once a field has failed, so people see themselves fixing it.

**inputmode** — text, numeric, decimal, tel, email, url, search. Controls the mobile keyboard.
**autocomplete** — a specific token vocabulary (`given-name`, `email`, `street-address`, `cc-number`, `one-time-code`). Not a boolean, and filling these in correctly is one of the largest usability wins available for the effort.

---

# H. Components

A first slice: five components whose parts are least reducible to the primitives already covered, chosen because most other components in Vocabulary's `H · Components` part compose from them or from a variant of them. The remaining entries in that part are a later, separately scoped addition — see **Settled decisions** below.

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

---

## Settled decisions

**Components was the chosen slice of the four named in README's "What is not covered," over tokens, information architecture, and content.** Vocabulary's `H · Components` part (V-310–V-364) already names roughly forty-five components with no anatomy anywhere in the suite, which made this the gap with the most existing scaffolding and the clearest boundary to work inside. Tokens sit close enough to Implementation's `T`/`K` namespace — the build artifact a choice becomes — that drafting their anatomy risked duplicating ownership rather than filling a gap; information architecture and content are not rendering primitives in the sense the rest of this document is, and each looks like it wants its own organizing shape rather than a bolt-on section here. Both are left for a scoping discussion before either gets A-IDs, not attempted in this pass.

**Five entries, not forty-five.** A-062–A-066 cover Button, Card, Tooltip/Popover, Dialog, and Tabs: the components most others in Vocabulary's `H` part either compose from directly (a card holding buttons, a dropdown menu sharing tooltip/popover placement anatomy) or differ from structurally (a dialog's scrim and focus trap, a tabs set's roving tabindex). This is a first slice, not the volume — the remaining names in V-310–V-364 (inputs and their variants, menus, toasts and banners, badges and chips, avatars, and the rest) are additive follow-up work under new A-IDs, each its own bounded contribution rather than one PR closing the whole part.

**Variant terms did not each get their own A-ID.** Icon button, ghost button, floating action button, and split button (V-312–V-315) are noted as sub-parts of A-062 rather than given separate entries, because none of them changes the parameter set — only which parameters are present, absent, or fixed. This mirrors how A-012 Gradient covers linear, radial, and conic without separate IDs, reserving a new entry for Mesh gradient (A-013) only because its parameters genuinely differ. The same reasoning folds non-modal dialog, drawer, and sheet (V-338–V-340) into A-065 rather than three further entries.

**Which choices exist among these parts, and how a choice becomes a built component, stayed out.** Several drafts of these entries drifted toward saying which affordance to prefer or how a state trap is coded; both were cut. Composition owns the range of choice, Implementation owns the build, and an entry that started prescribing either was rewritten back down to the parts and their ranges — this document's own boundary, not a new one invented for components.
