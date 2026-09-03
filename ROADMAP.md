# Roadmap

Where this suite goes next, in order. Each phase gates the next — content coverage before
adoption push, contributor infrastructure before either, because opening the suite to outside
contributors before the infrastructure exists is how a document suite corrodes.

## Phase 1 — Contributor infrastructure

The suite is currently a single-owner, untracked project. Before anyone outside can contribute:

- **Give it its own repository.** `design-suite` is currently an untracked directory inside an
  unrelated repo. It needs its own git history and a GitHub remote before a PR from anyone else
  is possible.
- **`CONTRIBUTING.md`.** Operationalizes Governance's "small team" tier (`G082`) plus the
  proposal shape from `G030`/`G031` — a PR states the change, the reason, and the migration if
  it's breaking. See `CONTRIBUTING.md` itself for the full rules.
- **CI enforcement.** Done — `.github/workflows/validate.yml` runs `tooling/validate.py` and the
  Vale prose lint on every pull request and on push to `main`, so `G002`'s small-change test no
  longer depends on a contributor remembering a local command.

This phase is a gate, not a nice-to-have: without it, external PRs have nowhere to land and no
mechanical check to catch structural errors before a human has to.

## Phase 2 — Content coverage

Close the gaps the suite already knows about, in the order the suite itself recommends:

- **Decision-completeness checker.** Done — `tooling/decision_completeness.py`. Joins a
  downstream project's ADR directory against `tooling/registry.yaml` and reports which of the 67
  Composition families are decided versus still on default. Converts Composition from a reference
  into a checklist that knows its own state; see `README.md`'s command list for usage and
  `tests/decision_completeness/fixtures/` for the ADR format and worked examples.
- **Anatomy volume 2.** Partially done. Components, tokens, information architecture, and content
  — the volumes `README.md` already flags as needed beyond the current rendering-primitives-only
  scope. Five slices have landed: `docs/anatomy-1.0.0.md` is now 1.5.0, exports `A-001`–`A-094`.
  The first slice added `A-062`–`A-066` for Button, Card, Tooltip/Popover, Dialog, and Tabs; the
  second added `A-067`–`A-076` for the input controls — Text input, Checkbox, Radio group,
  Switch, Select and combobox, Slider, Stepper, Segmented control, Dropzone, and Fieldset; the
  third added `A-077`–`A-078` for the menu family — Menu (covering dropdown menu and context
  menu) and Command palette; the fourth added `A-079`–`A-083` for information architecture —
  Breadcrumb, Pagination, Facets, Navigation (folding global, local, and utility navigation, with
  hamburger menu as a sub-part), and Skip link; the fifth added `A-084`–`A-094` for content —
  Headline, Deck, Eyebrow, Byline, Body, Pull-quote, Stat/callout, Caption, CTA text, List, and
  Metadata block, drawn from Vocabulary's `L · Content and language` part rather than `H ·
  Components`. Counted against the current export index, the first four slices together cite 32
  of the 55 names in Vocabulary's `H · Components` part (`V-310`–`V-364`) — a little over half —
  with the navigation-variant and skip-link names the fourth slice covers sitting outside that
  part's own count; the fifth slice does not add to that count, since content draws from a
  different Vocabulary part entirely. Tokens are no longer an open gap: the scoping discussion the
  first slice deferred it to has since happened and closed negative (issue #13, closed) —
  `docs/anatomy-1.0.0.md`'s own **Settled decisions** section now records tokens as settled out of
  scope, not deferred, because every parameter, range, and derived fact a token could need already
  resolves to an existing A-ID (a color-ramp step to `A-014`, spacing to `A-036`, a radius to
  `A-026`, and so on) or to Implementation's `T`-namespace, which owns the token wrapper itself.
  Information architecture is no longer an open scoping question or even a scoped-but-undrafted
  one — issue #11 closed with a resolved organizing shape (component entries only, the same
  template the first three slices already used; the site-as-graph alternative the IA research also
  raised was rejected as Composition's or Diagnosis's shape, not Anatomy's), and the fourth slice
  drafted the full named candidate set against that shape. Content is no longer open either — issue
  #10 closed with content anatomized as atomic content elements (Headline, Deck, Eyebrow, Byline,
  Body, Pull-quote, Stat/callout, Caption, CTA text, List, Metadata block), and the fifth slice has
  now drafted the full named candidate set, citing a small companion Vocabulary addition
  (`V-613`–`V-621`) the same slice added alongside it for the eight candidates and one partial
  match (Stat, against the pre-existing Callout) that had no term yet. One nuance flagged rather
  than resolved: `A-090` Stat/callout cites the pre-existing Callout (`V-348`) for the
  content-element sense of a callout specifically; a general-purpose `H`-part Callout component —
  with a severity, an icon, and an accent color, the shape most callout implementations actually
  take — is not covered by this slice and stays open below. The remaining ~23 names in Vocabulary's
  `H` part (toasts and banners, callouts, badges and chips, avatars, progress and spinner, skeleton
  and empty/zero state, carousel, lightbox, and toolbar, among others) remain the one open gap,
  natural first projects for an outside contributor, each its own bounded, separately scoped
  contribution rather than one PR closing the whole gap. Phase 2 is not complete while those remain
  unbuilt.

Everything else in the gap register (language-plane consistency measurement, representation-plane
verification, citation-intent checking, legal-change monitoring) stays explicitly out of scope —
`audit/tooling-audit-2.0.0.md` Part VI rates them either unautomatable or not worth building
against tooling that may not arrive. A gap register recommending six builds is a wish list; one
recommending one is a plan.

## Phase 3 — Adoption / visibility

Deliberately last. Polish the on-ramp, add examples, and push for visibility only once the suite
can absorb outside contributions (Phase 1) and has closed its known content gaps (Phase 2).
Publicizing an incomplete, unprocessed suite invites contributors into a mess instead of a
project — the opposite of what adoption is meant to buy.

## What doesn't move

Independent of phase, these hold at every size per Governance's `G084`: identifier stability,
dependency direction, citation-correctness review, and the sunset criteria in `G043`. None of the
three phases above touch them, and none should.
