```yaml
document: Vocabulary
version: 1.0.3
tier: 0
owns:
  - what each term denotes
  - which terms are distinct from which
  - which terms may not be used
exports: V-001–V-612
depends: []
reviewed: 2026-09-03
```

# Vocabulary

What the words mean. This document cites nothing and defines only — no parameters, no ranges, no guidance.

---

## What this document owns

Denotation. One sentence per term establishing what it refers to. Plus two things only a naming document can do: fixing the boundary between terms that get confused, and refusing the terms that carry no information.

## What it does not own

| Question | Owner |
|---|---|
| What is this thing made of, in parameters? | Anatomy |
| What choices exist around it? | Composition |
| What may it not be? | Constraints |
| What should it be set to? | Decision |
| How is it built? | Implementation |
| How is it checked? | Verification |

The boundary is strict and worth stating twice: **"shadow" is a Vocabulary entry, "a shadow has offset, blur, and spread" is Anatomy, "how much shadow" is Composition, "shadows may not carry meaning alone" is Constraints, and "default to bordered rather than shadowed" is Decision.** Five documents, five sentences, one word.

## Citation

Other documents cite a V-ID only where a term is genuinely contested or confusable. Citing every term would be unreadable and would make this document a dependency of every sentence rather than of the vocabulary. Part II is the subset most likely to need citing.

---

# PART I — TERMS

## A · Practice

**V-001 · Design** — Deciding how something works and what it communicates, then giving that decision form.
**V-002 · User experience** — The whole of a person's encounter with a product, including everything outside the interface.
**V-003 · User interface** — The surface a person perceives and operates.
**V-004 · Interaction design** — The design of behavior over time.
**V-005 · Information architecture** — The structure and labeling of content so it can be found and understood.
**V-006 · Visual design** — The use of form, color, type, space, and image to create hierarchy and tone.
**V-007 · Content design** — Treating words, structure, and sequence as the primary design material.
**V-008 · Service design** — Design of the whole system around a product, including its human and offline parts.
**V-009 · Front-end development** — Implementation of an interface in the browser's own materials.
**V-010 · Design engineering** — Designing in the medium by building the working artifact rather than a representation of it.
**V-011 · Craft** — Attention paid at a level of detail nobody requested.
**V-012 · Affordance** — What an object permits a person to do.
**V-013 · Signifier** — The perceptible cue advertising an affordance.

## B · Systems

**V-020 · Design system** — The whole apparatus of principles, tokens, components, patterns, documentation, and the process governing them.
**V-021 · Design language** — The recognizable consistency of a system's visual and behavioral decisions.
**V-022 · Style guide** — A document specifying visual rules.
**V-023 · Pattern library** — A catalog of recurring solutions with guidance on when each applies.
**V-024 · Component library** — The implemented, reusable code components.
**V-025 · Design token** — A named stored value representing a design decision.
**V-026 · Primitive token** — A token holding a raw value with no purpose attached.
**V-027 · Semantic token** — A token named for its purpose, resolving to a primitive.
**V-028 · Component token** — A token scoped to a single component.
**V-029 · Theming** — Substituting token values to change appearance without changing structure.
**V-030 · Variant** — A named configuration of a component.
**V-031 · Slot** — A designated opening in a component where arbitrary content is inserted.
**V-032 · Composition** — Building complex interfaces by nesting single-purpose components.
**V-033 · Atomic design** — A taxonomy of component granularity: atoms, molecules, organisms, templates, pages.
**V-034 · Density** — How much information occupies a given area.
**V-035 · Single source of truth** — The one location where a decision is recorded and from which all uses derive.
**V-036 · Drift** — Divergence between a system's specification and its implementations over time.
**V-037 · Deprecation** — Marking something as no longer to be used while it still exists.

## C · Page and layout

**V-050 · Viewport** — The visible region of the page in the browser window.
**V-051 · Document flow** — The default placement of elements before positioning is applied.
**V-052 · Above the fold** — What is visible before scrolling.
**V-053 · Hero** — The large introductory block at the top of a page.
**V-054 · Container** — A width-constraining wrapper.
**V-055 · Gutter** — The space between columns.
**V-056 · Margin** — Space outside an element's border. → distinguish V-057
**V-057 · Padding** — Space inside an element's border. → distinguish V-056
**V-058 · Inset** — Padding applied evenly on all sides; in positioning, distance from each edge.
**V-059 · Safe area** — The region of a screen guaranteed unobstructed by hardware or system chrome.
**V-060 · Bleed** — Content extended past the container to the viewport edge.
**V-061 · Sticky** — Scrolling normally until a threshold, then pinning.
**V-062 · Fixed** — Positioned relative to the viewport, unaffected by scroll.
**V-063 · Z-index** — The stacking order of overlapping elements.
**V-064 · Stacking context** — A group whose z-index values are compared only against each other.
**V-065 · Portal** — Rendering an element elsewhere in the document to escape a containing context.
**V-066 · Overflow** — Behavior when content exceeds its container.
**V-067 · Box model** — Every element as content, padding, border, and margin.
**V-068 · Flexbox** — A one-dimensional layout model distributing items along a single axis.
**V-069 · Grid** — A two-dimensional layout model of rows and columns.
**V-070 · Track** — A single row or column in a grid.
**V-071 · Subgrid** — A nested grid inheriting its parent's track definitions.
**V-072 · Intrinsic sizing** — Sizing derived from content.
**V-073 · Extrinsic sizing** — Sizing imposed from outside the element.
**V-074 · Aspect ratio** — A locked proportional relationship between width and height.
**V-075 · Gap** — Space between grid or flex items.
**V-076 · Margin collapse** — Adjacent vertical margins merging into the larger of the two.
**V-077 · Baseline grid** — A horizontal rhythm aligning text baselines to a repeating interval.
**V-078 · Modular scale** — A set of sizes generated by repeatedly applying a ratio.
**V-079 · Spacing scale** — The restricted set of spacing values a system permits.
**V-080 · Whitespace** — Area containing nothing, treated as a material rather than an absence.
<!-- vale Suite.RefusedTerms = NO --><!-- this defines the term Part III refuses in its vague sense; the technical sense is exact and citable as V-611 -->
**V-081 · Responsive design** — Layout adapting continuously to viewport size. → distinguish V-082
<!-- vale Suite.RefusedTerms = YES -->
**V-082 · Adaptive design** — Layout switching between a fixed number of discrete arrangements. → distinguish V-081
**V-083 · Breakpoint** — A width at which layout rules change.
**V-084 · Media query** — Conditional CSS based on viewport or device characteristics.
**V-085 · Container query** — Conditional CSS based on an ancestor's size rather than the viewport's.
**V-086 · Mobile-first** — Writing base styles for small viewports and layering upward.
**V-087 · Fluid** — Scaling continuously with available space.
**V-088 · Logical property** — A property defined relative to writing direction rather than physical sides.
**V-089 · Gestalt principles** — The perceptual rules by which elements are grouped: proximity, similarity, closure, continuity, common region, figure and ground.
**V-090 · Visual weight** — How much attention an element commands.
**V-091 · Hierarchy** — The ordered arrangement of importance, expressed so it reads without effort.
**V-092 · Optical center** — The position slightly above true center where the eye expects a centered element.
**V-093 · Bento layout** — A grid of unequal rounded cells each holding one idea.
**V-094 · Masonry** — A staggered grid packing items vertically without aligned rows.

## D · Typography

**V-100 · Typeface** — The design of a set of letterforms. → distinguish V-101
**V-101 · Font** — A specific instance or file of a typeface at a given weight and style. → distinguish V-100
**V-102 · Font family** — The grouped set of related weights, widths, and styles.
**V-103 · Font stack** — The ordered list of fonts a browser attempts.
**V-104 · Serif** — A typeface with finishing strokes on letter terminals.
**V-105 · Sans-serif** — A typeface without them.
**V-106 · Slab serif** — A typeface whose serifs are thick and rectangular.
**V-107 · Monospace** — A typeface in which every character occupies identical width.
**V-108 · Display type** — A design intended for large sizes.
**V-109 · Text type** — A design intended for extended reading at small sizes.
**V-110 · Variable font** — A single file containing continuous variation along one or more axes.
**V-111 · Axis** — A dimension of variation in a variable font.
**V-112 · Optical size** — Adjustment of letterform proportions for the size at which text is set.
**V-113 · Weight** — Stroke thickness.
**V-114 · Italic** — A separately drawn cursive companion design. → distinguish V-115
**V-115 · Oblique** — A mechanically slanted version of an upright design. → distinguish V-114
**V-116 · Baseline** — The line letters sit on.
**V-117 · X-height** — The height of a lowercase x.
**V-118 · Cap height** — The height of a capital letter from the baseline.
**V-119 · Ascender** — The part of a lowercase letter rising above x-height.
**V-120 · Descender** — The part dropping below the baseline.
**V-121 · Counter** — The enclosed or partly enclosed space within a letter.
**V-122 · Aperture** — The opening of a partially closed counter.
**V-123 · Terminal** — The end of a stroke that is not a serif.
**V-124 · Stem** — The main vertical stroke.
**V-125 · Bowl** — A curved stroke enclosing a counter.
**V-126 · Shoulder** — A curve springing from a stem.
**V-127 · Spine** — The central curve of an S.
**V-128 · Ear** — The small projection on a lowercase g.
**V-129 · Apex** — The junction at the top of a pointed letter.
**V-130 · Overshoot** — The amount by which round letters exceed the baseline and cap height so they appear equal in size.
**V-131 · Em** — A relative unit equal to the current font size.
**V-132 · Rem** — A relative unit equal to the root font size.
**V-133 · Type scale** — The finite ordered set of sizes a design uses.
**V-134 · Leading** — Vertical space between baselines. → distinguish V-135
**V-135 · Line-height** — The CSS property setting the line box height, of which leading is the visible result. → distinguish V-134
**V-136 · Measure** — Line length.
**V-137 · Tracking** — Uniform spacing adjustment across a run of text. → distinguish V-138
**V-138 · Kerning** — Adjustment of space between two specific letters. → distinguish V-137
**V-139 · Sidebearing** — The built-in space on each side of a glyph.
**V-140 · Ligature** — Two or more characters drawn as a single glyph.
**V-141 · Small caps** — Capital forms drawn at approximately x-height and properly weighted.
**V-142 · Lining figures** — Numerals of uniform height aligned to cap height.
**V-143 · Oldstyle figures** — Numerals with ascenders and descenders.
**V-144 · Tabular figures** — Numerals of identical width. → distinguish V-145
**V-145 · Proportional figures** — Numerals with individual natural widths. → distinguish V-144
**V-146 · Stylistic set** — An alternate collection of glyph designs within a font.
**V-147 · Rag** — The uneven edge of unjustified text.
**V-148 · River** — A vertical channel of whitespace running through justified text.
**V-149 · Widow** — A short final line stranded at the end of a paragraph. → distinguish V-150
**V-150 · Orphan** — A single line stranded at the top or bottom of a column. → distinguish V-149
**V-151 · Hanging punctuation** — Punctuation set outside the text edge so the optical margin stays straight.
**V-152 · Optical alignment** — Adjustment away from mathematical alignment so elements appear aligned.
**V-153 · Subsetting** — Shipping only the glyphs a document uses.
**V-154 · FOUT** — A flash of fallback text before a webfont loads and replaces it.
**V-155 · FOIT** — A period of invisible text while a webfont loads.
**V-156 · Metric override** — Adjustment of a fallback font's metrics to match the webfont it precedes.
**V-157 · Hinting** — Instructions in a font for rendering cleanly at small sizes.
**V-158 · Antialiasing** — Smoothing letterform edges with partial pixels.
**V-159 · Line clamp** — Truncation after a set number of lines.

## E · Color

**V-170 · Hue** — Position on the color wheel.
**V-171 · Saturation** — Colorfulness relative to the maximum attainable at a given lightness. → distinguish V-172
**V-172 · Chroma** — Absolute colorfulness, unbounded and gamut-limited in practice. → distinguish V-171
**V-173 · Lightness** — Perceived light or dark. → distinguish V-174
**V-174 · Luminance** — Physical light emitted, weighted by human sensitivity per channel. → distinguish V-173
**V-175 · Tint** — A hue mixed with white.
**V-176 · Shade** — A hue mixed with black.
**V-177 · sRGB** — The historical baseline web color space.
**V-178 · Display P3** — A wider-gamut space covering roughly 25% more than sRGB.
**V-179 · HSL** — A cylindrical model of hue, saturation, and lightness that is not perceptually uniform.
**V-180 · OKLCH** — A perceptually uniform cylindrical model of lightness, chroma, and hue.
**V-181 · OKLab** — The Cartesian form of OKLCH, used for interpolation.
**V-182 · Color space** — A defined range and encoding of representable colors.
**V-183 · Gamut** — The set of colors a device or space can reproduce.
**V-184 · Gamut mapping** — Translating out-of-range colors into a reproducible set.
**V-185 · Color ramp** — An ordered series of steps within one hue.
**V-186 · Step role** — The assigned purpose of a position in a ramp.
**V-187 · Palette** — The complete set of colors a design uses.
**V-188 · Semantic color** — A color assigned a fixed meaning.
**V-189 · Contrast ratio** — The measured luminance relationship between two colors.
**V-190 · APCA** — A perceptual contrast model accounting for polarity, size, and weight.
**V-191 · Alpha** — Transparency of a color value. → distinguish V-192
**V-192 · Opacity** — Transparency applied to an element and all its descendants as a group. → distinguish V-191
**V-193 · Blend mode** — The formula used when compositing one layer over another.
**V-194 · Isolation** — Confining blending to a group so it does not reach the page background.
**V-195 · Scrim** — A semi-transparent layer placed over imagery to keep overlaid text legible.
**V-196 · Gradient** — A continuous transition between colors.
**V-197 · Color stop** — A color and its position within a gradient.
**V-198 · Interpolation space** — The color model in which a transition is calculated.
**V-199 · Hue interpolation method** — Which direction a transition travels around the hue wheel.
**V-200 · Banding** — Visible stepped stripes in a gradient caused by insufficient bit depth.
**V-201 · Dithering** — Adding fine noise to break up banding.
**V-202 · Halation** — The bleeding glow perceived around light text on very dark backgrounds.
**V-203 · Color vision deficiency** — Reduced ability to distinguish certain hues.

## F · Shape, surface, depth

**V-220 · Border radius** — The rounding of a corner, measured as a radius.
**V-221 · Superellipse** — A shape between a rectangle and an ellipse, defined by an exponent.
**V-222 · Squircle** — A superellipse used as a corner treatment.
**V-223 · Corner smoothing** — The degree to which a corner approaches continuous curvature.
**V-224 · Curvature continuity** — Whether curvature matches across a join, classed G0, G1, or G2.
**V-225 · Nested radius** — The relationship keeping concentric corners parallel.
**V-226 · Stroke** — A line drawn along a path.
**V-227 · Hairline** — A line as close to one device pixel as the display allows.
**V-228 · Keyline** — A thin structural line used to separate or align.
**V-229 · Outline** — A line drawn outside the border that does not affect layout.
**V-230 · Ring** — An offset outline leaving a visible gap.
**V-231 · Drop shadow** — A shadow cast outside an element.
**V-232 · Inner shadow** — A shadow cast inside an element.
**V-233 · Layered shadow** — Multiple stacked shadows approximating real light falloff.
**V-234 · Key shadow** — The directional component representing the dominant light source.
**V-235 · Ambient shadow** — The diffuse component representing environmental light.
**V-236 · Contact shadow** — The dark line where an object meets the surface beneath it.
**V-237 · Elevation** — The conceptual height of a surface above the base plane.
**V-238 · Backdrop blur** — Blurring of content behind a translucent element.
**V-239 · Glassmorphism** — Translucent blurred surfaces implying frosted glass.
**V-240 · Neumorphism** — Soft dual-shadow embossing on a matching background.
**V-241 · Skeuomorphism** — Imitation of real-world materials in an interface.
**V-242 · Flat design** — Removal of depth cues in favor of color and shape alone.
**V-243 · Mask** — Hiding parts of an element based on another image's alpha or luminance. → distinguish V-244
**V-244 · Clip path** — Cutting an element to a geometric shape with a hard edge. → distinguish V-243
**V-245 · Noise** — A fine random texture.
**V-246 · Blue noise** — Noise containing only high frequencies, visually even and preferred for dithering.
**V-247 · Perlin noise** — Smooth correlated noise generated from a gradient lattice.
**V-248 · Octave** — One layer of noise in a summed series of increasing frequency.
**V-249 · Pattern** — A repeating arrangement of shapes.
**V-250 · Motif** — The smallest meaningful repeating unit of a pattern.
**V-251 · Tiling** — Repeating a unit so its edges align.
<!-- vale Suite.RefusedTerms = NO --><!-- "seamless" here names a precise geometric property (edges that match), not the refused vague usage -->
**V-252 · Seamless tile** — A unit whose opposite edges match exactly.
<!-- vale Suite.RefusedTerms = YES -->
**V-253 · Truchet tile** — A square tile with rotationally asymmetric contents, producing complexity under random rotation.
**V-254 · Wallpaper group** — One of the seventeen possible symmetry structures for a repeating plane pattern.
**V-255 · Ornament** — Decoration serving expression rather than function.

## G · Imagery and icons

**V-270 · Raster** — A pixel-based image.
**V-271 · Vector** — A shape-based image defined by paths.
**V-272 · SVG** — An XML vector format that is stylable and animatable.
**V-273 · Path** — Line data defining a vector shape.
**V-274 · Bézier curve** — A curve defined by anchor points and control handles.
**V-275 · Bit depth** — Bits used per color channel.
**V-276 · Chroma subsampling** — Storing color detail at lower resolution than brightness detail.
**V-277 · Color profile** — Embedded data declaring which color space an image uses.
**V-278 · Device pixel ratio** — Physical pixels per CSS pixel.
**V-279 · Density descriptor** — A srcset value expressing an image's intended pixel ratio.
**V-280 · Width descriptor** — A srcset value expressing an image's intrinsic width.
**V-281 · Art direction** — Serving different crops or compositions at different sizes, not merely different resolutions.
**V-282 · Object-fit** — How an image fills its box.
**V-283 · Focal point** — The region of an image that must survive cropping.
**V-284 · Lazy loading** — Deferring off-screen resource loading.
**V-285 · Placeholder** — What occupies space before content arrives.
**V-286 · LQIP** — A tiny low-quality stand-in shown during load.
**V-287 · Icon** — A small symbolic graphic representing an object or action.
**V-288 · Icon grid** — The frame and keyline shapes an icon set aligns to.
**V-289 · Live area** — The region of an icon canvas the artwork may occupy.
**V-290 · Optical volume** — The total ink of an icon, balanced by eye rather than by bounding box.
**V-291 · Pixel snapping** — Aligning shapes to whole pixels so strokes render crisply.
**V-292 · Alt text** — A text alternative conveying an image's content and purpose.
**V-293 · Decorative image** — An image carrying no information, marked so assistive technology skips it.
**V-294 · Open Graph image** — The preview image shown when a link is shared.

## H · Components

**V-310 · Button** — A control performing an action. → distinguish V-311
**V-311 · Link** — A control navigating to another location. → distinguish V-310
**V-312 · Ghost button** — A button with no fill or border until interacted with.
**V-313 · Icon button** — An action control with no visible text label.
**V-314 · Floating action button** — A persistent control floating above content for a primary action.
**V-315 · Split button** — A primary action with an attached menu of related actions.
**V-316 · Input** — A single-line text field.
**V-317 · Textarea** — A multi-line text field.
**V-318 · Label** — Persistent text naming a control. → distinguish V-319
**V-319 · Placeholder text** — Example text inside an empty field that disappears on entry. → distinguish V-318
**V-320 · Helper text** — Persistent guidance accompanying a field.
**V-321 · Select** — A control for choosing from a fixed list.
**V-322 · Combobox** — A text input combined with a filtered list of options.
**V-323 · Checkbox** — An independent binary choice. → distinguish V-325
**V-324 · Radio group** — A mutually exclusive choice among visible options.
**V-325 · Switch** — A control taking effect immediately on toggle. → distinguish V-323
**V-326 · Slider** — A control selecting a value along a range.
**V-327 · Stepper** — A control incrementing and decrementing a value.
**V-328 · Segmented control** — A compact row of mutually exclusive options.
**V-329 · Dropzone** — A region accepting files by drag or click.
**V-330 · Fieldset** — A grouping of related controls with a group-level label.
**V-331 · Card** — A bounded surface collecting content about one subject.
**V-332 · Table** — Row-and-column display of structured content. → distinguish V-333
**V-333 · Data grid** — A table with interaction: sorting, filtering, resizing, editing. → distinguish V-332
**V-334 · Tabs** — Switching between sibling panels in one context.
**V-335 · Accordion** — Vertically stacked collapsible sections.
**V-336 · Disclosure** — A single show-and-hide toggle.
**V-337 · Modal** — A layer blocking interaction until resolved. → distinguish V-338
**V-338 · Non-modal dialog** — A dialog leaving the page beneath operable. → distinguish V-337
**V-339 · Drawer** — A panel sliding in from an edge.
**V-340 · Sheet** — A drawer entering from the bottom edge.
**V-341 · Popover** — A floating panel anchored to a trigger, containing interactive content. → distinguish V-342
**V-342 · Tooltip** — A small non-interactive label appearing on hover or focus. → distinguish V-341
**V-343 · Dropdown menu** — A list of actions opened from a trigger.
**V-344 · Context menu** — A menu opened by secondary click or long press, scoped to its target.
**V-345 · Command palette** — A keyboard-invoked search across available actions.
**V-346 · Toast** — A brief self-dismissing message. → distinguish V-347
**V-347 · Banner** — A persistent inline message about status or consequence. → distinguish V-346
**V-348 · Callout** — An inline box highlighting supplementary information.
**V-349 · Badge** — A small count or status marker attached to another element.
**V-350 · Chip** — A compact element representing an attribute, filter, or selection.
**V-351 · Avatar** — A small image or initials representing a person or entity.
**V-352 · Breadcrumb** — A trail showing position within a hierarchy.
**V-353 · Pagination** — Navigation between discrete pages of results.
**V-354 · Infinite scroll** — Automatic loading of further content on scroll.
**V-355 · Progress bar** — Determinate indication of completion. → distinguish V-356
**V-356 · Spinner** — Indeterminate indication that work is occurring. → distinguish V-355
**V-357 · Skeleton** — Placeholder shapes matching the layout of content still loading.
**V-358 · Empty state** — The view when no content exists yet.
**V-359 · Zero state** — The first-run form of an empty state.
**V-360 · Facet** — A single filterable dimension, usually with counts.
**V-361 · Carousel** — A horizontally paged sequence of items.
**V-362 · Lightbox** — A full-screen overlay for viewing media.
**V-363 · Toolbar** — A grouped row of controls acting on the current context.
**V-364 · Hamburger menu** — A three-line icon concealing navigation.

## I · States and interaction

**V-380 · State** — The current condition of a component, which its appearance communicates.
**V-381 · Rest** — The idle appearance.
**V-382 · Hover** — A pointer positioned over an element.
**V-383 · Focus** — An element being the keyboard's current target.
**V-384 · Focus-visible** — Focus arrived at by keyboard rather than pointer.
**V-385 · Focus ring** — The visible indicator of focus.
**V-386 · Active** — An element currently being pressed.
**V-387 · Selected** — Chosen among siblings.
**V-388 · Indeterminate** — A binary control in a mixed or partial state.
**V-389 · Disabled** — Non-interactive and not focusable. → distinguish V-390
**V-390 · Read-only** — Displayed and focusable but not editable. → distinguish V-389
**V-391 · Dirty** — Modified since load. → distinguish V-392
**V-392 · Touched** — Visited and left, whether or not modified. → distinguish V-391
**V-393 · Feedback** — The system's response confirming an action registered.
**V-394 · Acknowledgment** — Immediate indication that input was received, distinct from completing it.
**V-395 · Latency** — Delay between action and response.
**V-396 · Perceived performance** — How fast something feels, independent of how fast it is.
**V-397 · Optimistic UI** — Updating as though a request succeeded, reconciling if it did not.
**V-398 · Debounce** — Waiting until input stops before acting. → distinguish V-399
**V-399 · Throttle** — Limiting how often an action fires during continuous input. → distinguish V-398
**V-400 · Hit area** — The region that responds to pointer input, which may exceed the visible element.
**V-401 · Drop target** — A region accepting a dragged item.
**V-402 · Tab order** — The sequence in which focus moves.
**V-403 · Roving tabindex** — Treating a group as one tab stop navigated internally by arrow keys.
**V-404 · Focus trap** — Confinement of focus within a region while it is open.
**V-405 · Skip link** — A link allowing keyboard users to bypass repeated navigation.
**V-406 · Escape hatch** — A reliable means of leaving any state.
**V-407 · Progressive disclosure** — Revealing complexity only when needed.
**V-408 · Direct manipulation** — Acting on an object itself rather than through a separate control.
**V-409 · Forgiveness** — Designing so mistakes are cheap and recoverable.

## J · Motion

**V-420 · Transition** — An animation between two states caused by a change.
**V-421 · Animation** — A defined keyframe sequence not requiring a state change.
**V-422 · Keyframe** — A defined point in an animation's timeline.
**V-423 · Duration** — How long a motion takes.
**V-424 · Easing** — The rate of change over time.
**V-425 · Ease-in** — Starting slow and accelerating.
**V-426 · Ease-out** — Starting fast and decelerating.
**V-427 · Cubic-bézier** — An easing curve defined by two control points.
**V-428 · Spring** — Physics-based motion defined by stiffness, damping, and mass rather than duration.
**V-429 · Damping ratio** — The value determining whether a spring overshoots, settles critically, or approaches slowly.
**V-430 · Overshoot** — Passing a target before settling.
**V-431 · Interruptibility** — Whether an in-progress animation can be redirected mid-flight.
**V-432 · Stagger** — Offsetting the start of animations across a group.
**V-433 · Choreography** — The arrangement of what moves when across a transition.
**V-434 · Shared element transition** — Animating an element so it appears to persist across a navigation.
**V-435 · Anticipation** — A small counter-movement preceding the main move.
**V-436 · Follow-through** — Secondary movement continuing after the primary stops.
**V-437 · Transform** — Translation, scale, rotation, or skew applied to an element.
**V-438 · Transform origin** — The pivot point of a transform.
**V-439 · Compositing** — The stage at which transformed and faded layers are combined, typically on the GPU.
**V-440 · Layout animation** — Animation of properties that change geometry and force reflow.
**V-441 · Jank** — Visible stutter caused by missed frames.
**V-442 · Frame budget** — The time available to produce one frame.
**V-443 · Scroll-driven animation** — Motion whose progress is tied to scroll position rather than time.
**V-444 · Micro-interaction** — A small contained moment of feedback, comprising trigger, rules, feedback, and loops.

## K · Accessibility

**V-460 · Accessibility** — The property of being usable by people with disabilities.
**V-461 · WCAG** — The Web Content Accessibility Guidelines.
**V-462 · POUR** — WCAG's four principles: perceivable, operable, understandable, robust.
**V-463 · Success criterion** — A single testable WCAG requirement.
**V-464 · Conformance level** — A grade of WCAG coverage: A, AA, or AAA.
**V-465 · Semantic HTML** — Use of elements according to their meaning rather than their appearance.
**V-466 · Landmark** — A structural region assistive technology can navigate between.
**V-467 · ARIA** — Attributes supplementing HTML semantics where native elements are insufficient.
**V-468 · Role** — What an element is, semantically.
<!-- vale Suite.RefusedTerms = NO --><!-- "accessible name" is WCAG's own defined term (see also C046, K013); not the refused binary-adjective usage -->
**V-469 · Accessible name** — The label announced by assistive technology.
<!-- vale Suite.RefusedTerms = YES -->
**V-470 · Live region** — An area whose updates are announced without moving focus.
**V-471 · Screen reader** — Software conveying an interface as speech or braille.
**V-472 · Target size** — The minimum dimensions of an interactive region.
**V-473 · Reflow** — Content rearranging at high zoom without two-dimensional scrolling.
**V-474 · Forced colors** — A user mode replacing author colors with a system palette.
**V-475 · Reduced motion** — A user preference requesting less or no animation.
**V-476 · Keyboard trap** — A state focus can enter but not leave.
**V-477 · Cognitive load** — The mental effort an interface demands.
**V-478 · Plain language** — Writing at the lowest reading level the content permits.
**V-479 · Assistive technology** — Any tool mediating between a person and an interface.
**V-480 · Overlay** — A third-party script claiming to remediate accessibility automatically.

## L · Content and language

**V-500 · Microcopy** — Small functional text: labels, hints, errors, empty states.
**V-501 · Voice** — The consistent personality of a product's language. → distinguish V-502
**V-502 · Tone** — How voice adapts to a situation. → distinguish V-501
**V-503 · Register** — The level of formality.
**V-504 · Call to action** — Text and control prompting the primary next step.
**V-505 · Deck** — The supporting line beneath a headline.
**V-506 · Information scent** — How well a label predicts what lies behind it.
**V-507 · Content-first design** — Designing around actual content rather than fitting content to a layout.
**V-508 · Internationalization** — Building so a product can be adapted to other languages and regions. → distinguish V-509
**V-509 · Localization** — Adapting it. → distinguish V-508
**V-510 · Pseudo-localization** — Testing with expanded accented placeholder strings to reveal layout breakage.
**V-511 · Text expansion** — Growth in string length under translation.
**V-512 · RTL** — A right-to-left writing direction.
**V-513 · Colophon** — A statement of how and by whom something was made.

## M · Information architecture

**V-530 · Taxonomy** — A classification scheme for content.
**V-531 · Ontology** — Definitions of things and their relationships.
**V-532 · Sitemap** — The map of pages and their hierarchical relations.
**V-533 · Global navigation** — Navigation present site-wide. → distinguish V-534
**V-534 · Local navigation** — Navigation specific to a section. → distinguish V-533
**V-535 · Utility navigation** — Account, search, settings, and help.
**V-536 · Faceted navigation** — Filtering by multiple independent attributes simultaneously.
**V-537 · Wayfinding** — Knowing where you are, where you can go, and how to return.
**V-538 · Card sorting** — A method in which participants group content, revealing their model.
**V-539 · Tree testing** — Testing findability in a structure without visual design.
**V-540 · Mental model** — A person's internal understanding of how a system works.
**V-541 · User flow** — The sequence of steps completing a task.
**V-542 · Journey map** — The end-to-end experience over time, including what lies outside the product.
**V-543 · Wireframe** — Low-fidelity structure without visual styling.
**V-544 · Mockup** — Static high-fidelity visual design.
**V-545 · Prototype** — An interactive model of intended behavior.
**V-546 · Fidelity** — How closely an artifact resembles the finished product.
**V-547 · Canonical URL** — The single authoritative address for a piece of content.

## N · Implementation

**V-560 · DOM** — The live tree representing a document in the browser.
**V-561 · Cascade** — The rules determining which conflicting declaration applies.
**V-562 · Specificity** — The weight of a selector.
**V-563 · Custom property** — A CSS variable.
**V-564 · Utility class** — A single-purpose class.
**V-565 · Scoped styles** — Styles that cannot leak outside their component.
**V-566 · Reset** — A stylesheet flattening browser defaults.
**V-567 · Progressive enhancement** — Building a working baseline and layering improvements. → distinguish V-568
**V-568 · Graceful degradation** — Building the full experience and ensuring acceptable failure. → distinguish V-567
**V-569 · Feature query** — Conditional CSS applied only where a feature is supported.
**V-570 · Polyfill** — Code supplying a missing browser capability.
**V-571 · Server-side rendering** — Generating markup on the server.
**V-572 · Hydration** — Attaching behavior to server-rendered markup.
**V-573 · Critical CSS** — The minimum styles required for first paint, inlined.
**V-574 · Render blocking** — Resources that must load before anything paints.
**V-575 · FOUC** — A flash of unstyled content before styles arrive.
**V-576 · Core Web Vitals** — A defined set of user-experience metrics.
**V-577 · LCP** — Largest Contentful Paint.
**V-578 · INP** — Interaction to Next Paint.
**V-579 · CLS** — Cumulative Layout Shift.
**V-580 · Virtualization** — Rendering only the visible portion of a long list.
**V-581 · Bundle size** — The weight of shipped JavaScript.
**V-582 · Structured data** — Machine-readable markup describing page content.
**V-583 · Autocomplete token** — A specified value telling the browser what a field expects.
**V-584 · Content Security Policy** — A declaration restricting what resources a page may load.

---

# PART II — DISAMBIGUATION

*The pairs that cause real errors, not merely imprecision. Each states the boundary and the consequence of crossing it.*

**V-600 · Typeface / font** `V-100 / V-101`
A typeface is a design; a font is an instance of it. Consequence: "how many fonts" and "how many typefaces" are different budget questions, and conflating them hides that one family at six weights is six files.

**V-601 · Leading / line-height** `V-134 / V-135`
Leading is the visible space between baselines; line-height is the CSS property producing it, which distributes space above and below the text. Consequence: a line-height of 1.5 does not put 0.5em between lines; it puts 0.25em above and below each.

**V-602 · Kerning / tracking** `V-138 / V-137`
Kerning adjusts one specific pair; tracking adjusts every gap uniformly. Consequence: "the kerning is bad" almost always means the tracking is wrong, and applying tracking will not fix an actual kerning fault.

**V-603 · Saturation / chroma** `V-171 / V-172`
Saturation is relative to the maximum attainable at that lightness; chroma is absolute. Consequence: holding saturation constant across hues does not hold colorfulness constant, because the attainable maximum moves.

**V-604 · Lightness / luminance** `V-173 / V-174`
Lightness is perceptual; luminance is physical, weighted heavily toward green. Consequence: contrast math requires luminance, palette construction requires lightness, and using either in the other's place produces confidently wrong numbers.

**V-605 · Alpha / opacity** `V-191 / V-192`
Alpha applies to one paint operation; opacity applies to an element and every descendant as a group and creates a stacking context. Consequence: setting opacity on a parent to fade a background also fades the text and can silently break z-index.

**V-606 · Mask / clip path** `V-243 / V-244`
A mask uses a gradient or image's alpha or luminance and can be soft; a clip path is a hard-edged geometric cut. Consequence: fades require masks, and attempting them with clip paths produces jagged edges.

**V-607 · Label / placeholder** `V-318 / V-319`
A label persists; placeholder text vanishes on entry. Consequence: a placeholder used as a label leaves a filled field unlabeled, failing both the user reviewing their entry and the screen reader.

**V-608 · Checkbox / switch** `V-323 / V-325`
A switch takes effect immediately; a checkbox usually awaits submission. Consequence: using a switch inside a form with a save button promises an immediacy the form does not deliver.

**V-609 · Tooltip / popover** `V-342 / V-341`
A tooltip is a non-interactive label; a popover contains interactive content. Consequence: putting a link or button inside a hover-triggered tooltip makes it unreachable by keyboard and by touch.

**V-610 · Disabled / read-only** `V-389 / V-390`
Disabled is unfocusable and often unannounced; read-only is focusable, announced, and copyable. Consequence: disabling a field to indicate "not now" hides both the value and the reason from anyone using a screen reader.

<!-- vale Suite.RefusedTerms = NO --><!-- this entry is the disambiguation Part III's "Responsive" refusal points to; the term is being defined, not used loosely -->
**V-611 · Responsive / adaptive** `V-081 / V-082`
Responsive scales continuously; adaptive switches between fixed arrangements. Consequence: "make it responsive" is frequently used to request either, and the two have different testing surfaces.
<!-- vale Suite.RefusedTerms = YES -->

**V-612 · Focus / focus-visible** `V-383 / V-384`
Focus occurs on click as well as by keyboard; focus-visible is limited to keyboard arrival. Consequence: styling plain focus makes rings appear on mouse click, which is why people remove them, which is how keyboard users lose the indicator entirely.

---

# PART III — REFUSED TERMS

*Words that appear to describe and do not. None may be used in this suite as though they carried information. Each has a replacement that is checkable.*

<!-- vale Suite.RefusedTerms = NO --><!-- this table is the source the rule is generated from; every refused word necessarily appears here once, verbatim -->
| Refused | Why | Say instead |
|---|---|---|
| Clean | Describes the speaker's reaction, not the artifact | The specific property: sparse, aligned, low-contrast, few colors |
| Modern | Dates itself, and means whatever is current | The actual attribute, or the year of the reference |
| Intuitive | Means "familiar to me"; unfalsifiable | Matches an existing convention, or measured task success |
| Minimal | Confuses quantity with quality | Few elements, or restrained palette, or short copy — say which |
| Bold | Weight, color, size, or claim strength | Name the dimension |
| Elevated | Marketing word imported into design | Nothing; delete the sentence |
| Seamless | Almost always means "we did not test the seams" | The specific transition being described |
| Delightful | An intended reaction, not a property | The mechanism intended to produce it |
| Best practice | Appeal to consensus that may not exist | The source, the evidence, or the constraint |
| Accessible | Used as a binary when it is a set of criteria | The conformance level and which criteria are met |
| Responsive | Used for any adaptation at all | Responsive, adaptive, or fluid — see V-611 |
| Optimized | Says nothing about for what | The metric and the target |
| Pixel-perfect | Meaningless across device pixel ratios | Matches the specification within a stated tolerance |
| User-friendly | Unmeasurable and self-congratulatory | The task, the audience, and the success measure |
<!-- vale Suite.RefusedTerms = YES -->

## Enforcement

A refused-terms list that people are asked to remember is a list people forget. Prose linting makes it a check.

**Category first, tool second.** A prose linter runs configurable vocabulary rules over markdown and source comments in CI. Vale is the current instance, and ships the Google and Microsoft writing style guides as ready-made packages; `textlint`, `write-good`, and `alex` cover adjacent ground.

This table is published alongside the document as a Vale vocabulary — `RefusedTerms.yml` — so the rule and its enforcement cannot drift apart. Terms are `warning` rather than `error`: every entry has a legitimate use somewhere, and a refusal that blocks the build teaches people to disable the linter.

---

## Settled decisions

**Vocabulary does not host the registry.** An earlier draft of the architecture proposed it. That would place F, C, and D identifiers inside a Tier 0 document, making it depend upward and inverting the whole dependency rule. The registry is generated from every document's export index and belongs to no tier because nobody authors it. Corrected in Suite Architecture §7.

**Definitions carry no guidance.** Several entries here were considerably longer in earlier drafts, because a definition naturally wants to explain when to use the thing. That explanation belongs to Decision and the parameters belong to Anatomy. Each entry was cut to the sentence establishing denotation, which is why this document is shorter than the term count suggests.

**Disambiguation is a first-class part, not an appendix.** The thirteen pairs in Part II account for a large share of the errors that survive review, because both parties believe they are agreeing. Fixing a boundary is a naming act, and no other document in the suite can perform it.

**Refused terms are listed with replacements, not merely banned.** A prohibition without an alternative gets ignored under deadline. Every entry in Part III names something checkable to say instead.
