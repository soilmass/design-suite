# A worked example: a button's disabled state

This file is illustrative prose, not a governed document. It has no front matter, exports no
identifiers, and isn't part of `tooling/registry.yaml` — running `tooling/validate.py` processes
only `docs/*.md` and takes no notice of anything here. What it does do is cite real identifiers
from the nine governed documents, and every one of those citations is held to the same discipline
`AGENTS.md` asks of a citation inside `docs/`: grep the ID, confirm what it currently means, cite
only what it actually says.

The suite's ownership table (`suite-architecture.md` §2) asserts that nine documents interlock
without any one of them restating another's fact. That's easy to assert and hard to see happen.
This file picks one case small enough to walk in full — **a button's disabled state** — and
follows it through every document that has something to say about it, in the order those
documents' own tiers put them: foundational first, evaluative last.

Two of the nine don't appear below, and that's worth saying rather than leaving implicit.
Diagnosis reads an already-built site back into the model — there's nothing to diagnose in a case
that's being built, not inspected. Governance describes how the suite itself changes, not what a
button does; it cites no content IDs by design (`cites_no_ids: true`), so it has no part to play in
a content walkthrough. Nine documents, seven with something to say about this particular case.

---

## Vocabulary — naming it

Two terms are in play, and Vocabulary owns both, denotation only:

- **V-310 · Button** — "A control performing an action," distinguished from V-311 Link, which
  navigates to a location instead of performing one.
- **V-389 · Disabled** — "Non-interactive and not focusable." Vocabulary flags this one for a
  reason: it is explicitly distinguished from **V-390 · Read-only** — "Displayed and focusable but
  not editable." A disabled button isn't a quieter button; it's a control removed from the tab
  order and, on most platforms, unannounced. That distinction is the seed of everything that
  follows — Vocabulary doesn't explain the consequence, it just fixes the boundary so no later
  document can blur it.

Vocabulary stops there. It does not say what a button is made of, what disabling one costs, or
when to do it — those are five other documents' jobs, and the table in `docs/vocabulary-1.0.0.md`
("What it does not own") says so explicitly.

## Constraints — what's non-negotiable

**C046 · Name, role, value** (WCAG 4.1.2, A) is the floor here: for every interface component,
name and role must be programmatically determinable, and states and values must be able to be set
and reported. A disabled state is exactly a state in that sentence — if a button is disabled only
by paint (a grayed-out fill with the underlying element still focusable and operable, or the
reverse: inert markup with no visual or announced signal at all), C046 is violated regardless of
how it looks. Constraints itself names the cost this floor imposes on anything that isn't a native
element: "This is the constraint that makes custom controls expensive." A native
`<button disabled>` satisfies it for free; a custom control has to earn it — the specific move
Implementation names below at K001.

## Anatomy — what it's made of

**A-062 · Button** lists a button's parts — `container` · `label` · `leading icon` ·
`trailing icon` · `hit target` · `state matrix` — and that last parameter is where disabled lives:
a button isn't fully specified until it's specified across its whole state matrix, not just at
rest.

**A-057 · The state matrix** is what that parameter actually means, and it uses a button as its
own worked example. Disabled shows up twice in the matrix's dimensions: once as an `interaction
state` (rest, hover, focus, focus-visible, active, **disabled**) and once as a `permission state`
(available, **disabled**, read-only, hidden) — the same distinction Vocabulary drew between V-389
and V-390 reappears here as two different axes a control can be disabled *on*. A-057 puts a number
on why this matters: "a button has roughly 6 × 2 × 2 × 2 = 48 renderable combinations before
variants," which is offered as the reason systems collapse dimensions where they can, not as
license to skip the ones they don't collapse. Anatomy doesn't say whether to design all 48; it
only says what they are.

*(The same problem recurs elsewhere in Anatomy, not just Button: A-073 Stepper notes that "a
disabled (V-389) affordance with no visible or announced reason reads as broken rather than as a
floor or ceiling being respected" — the same V-389 boundary, applied to a different control, with
the same consequence.)*

## Composition — what the actual choice is

**F40 · Craft** is the family, and **F40.3 · State completeness** is the specific dial: "default
states only ←→ every state designed." This is the choice a team is actually making when it decides
whether a disabled button gets its own considered treatment (dimmed fill, removed shadow, a
`cursor: not-allowed`, a tooltip explaining why) or ships whatever the component library shipped by
default. Composition frames this as a range with two ends, not an instruction — it doesn't say
where on that range to sit. That's Decision's job, one tier up.

## Decision — how the choice actually gets set

Decision does two things with F40.3, and both matter for a disabled button specifically.

First, **D203 · Craft is a standard, not a round** — F40 is nominally set in Round 7 but "actually
enforced in every round... A team that sets it high in Round 7 and then ships framework-default
empty states has not set it at all." Disabled is exactly this kind of state: nobody schedules "design
the disabled button" as its own round, which is precisely why it's the one that ships undesigned.

Second, **D021** ranks F40 Craft among the families to set carefully because it carries
disproportionate impression, and names it "the one most reliably skipped" — the leverage argument
for why a disabled state is worth deciding deliberately rather than inheriting whatever a framework
or component library shipped, and cheap to get right relative to what skipping it costs later.

## Implementation — how it becomes a component

**K002 · Required states** is the concrete requirement: "Every interactive component provides all
of: rest, hover, focus-visible, active, disabled, loading... A component missing any of these does
not have a default for that state; it has an unmade decision that ships." Disabled is named
explicitly, in the same list F40.3 and A-057 both already pointed at — Implementation is where that
range and that parameter turn into an obligation on the shipped component.

**K001 · Native element first** is the specific route that satisfies C046 at close to zero cost: a
native `<button disabled>` supplies "name, role, value, state, keyboard behavior, and focus
management free." Building a custom disabled affordance instead — a `div` with a click handler and
a grayed-out class — reopens the whole C046 obligation as work Implementation now has to redo by
hand, which is the same tradeoff Decision's D062 names generally (`F41.3 ↔ C046`, custom controls
against access cost) applied here to one specific control.

## Verification — how you'd confirm it's right

**X010 · State matrix coverage** closes the loop: "Every component renders every state required
by K002 — rest, hover, focus-visible, active, disabled, loading, empty, partial, full, error. A
state with no test has no design." A disabled button that was never actually rendered and checked
— not just coded, not just styled in a mockup, but rendered and looked at — has, per X010's own
standard, not been designed at all, regardless of what F40.3 was set to on paper.

---

## What this shows

Seven documents, one control, one state, and not one fact restated twice. Vocabulary fixed what
"disabled" means and what it isn't. Constraints set the floor that state has to clear regardless of
what it looks like. Anatomy said where "disabled" sits in a button's own parts. Composition framed
the choice of whether to actually design it. Decision said when that choice gets made and why it's
worth making carefully. Implementation said what shipping it correctly requires, and named the
cheap path to satisfying Constraints' floor. Verification said how you'd know any of the above
actually happened. Each of those seven sentences names one fact this file did not have to look up
twice — that's the interlock the ownership table promises, shown once, on one small case, rather
than taken on its word.
