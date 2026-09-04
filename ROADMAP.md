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
  scope. Seven slices have landed: `docs/anatomy-1.0.0.md` is now 1.7.0, exports `A-001`–`A-098`.
  The first slice added `A-062`–`A-066` for Button, Card, Tooltip/Popover, Dialog, and Tabs; the
  second added `A-067`–`A-076` for the input controls — Text input, Checkbox, Radio group,
  Switch, Select and combobox, Slider, Stepper, Segmented control, Dropzone, and Fieldset; the
  third added `A-077`–`A-078` for the menu family — Menu (covering dropdown menu and context
  menu) and Command palette; the fourth added `A-079`–`A-083` for information architecture —
  Breadcrumb, Pagination, Facets, Navigation (folding global, local, and utility navigation, with
  hamburger menu as a sub-part), and Skip link; the fifth added `A-084`–`A-094` for content —
  Headline, Deck, Eyebrow, Byline, Body, Pull-quote, Stat/callout, Caption, CTA text, List, and
  Metadata block, drawn from Vocabulary's `L · Content and language` part rather than `H ·
  Components`; the sixth added `A-095`–`A-096` for message surfaces — Toast and banner (folded
  into one entry) and Callout, the `H`-part, severity-keyed sense of the term the fifth slice had
  left open. Tokens are no longer an open gap: the scoping discussion the first slice deferred it
  to has since happened and closed negative (issue #13, closed) —
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
  Body, Pull-quote, Stat/callout, Caption, CTA text, List, Metadata block), and the fifth slice
  drafted the full named candidate set, citing a small companion Vocabulary addition
  (`V-613`–`V-621`) the same slice added alongside it for the eight candidates and one partial
  match (Stat, against the pre-existing Callout) that had no term yet. The nuance the fifth slice
  flagged rather than resolved — `A-090` Stat/callout cites the pre-existing Callout (`V-348`) for
  the content-element sense of a callout specifically, leaving a general-purpose `H`-part Callout
  component open — is resolved by the sixth slice's `A-096`, which cites the same `V-348` for that
  richer, severity-keyed construction and states in `docs/anatomy-1.0.0.md`'s own **Settled
  decisions** why it folds with neither Toast/Banner nor Badge/Chip.

  Counted against the current export index, the sixth slice's own re-verification against
  Vocabulary's `H · Components` part (`V-310`–`V-364`, 55 names) found this document's citations
  account for 35 of them — the 32 the first four slices cite (component-only; the fifth slice adds
  no `H`-part citations, since content draws from a different Vocabulary part entirely) plus
  Label, Placeholder text, and Helper text (`V-318`–`V-320`), folded into the pre-existing `A-061`
  Form field rather than counted in that 32 — leaving 20 open before the sixth slice, not the
  ~23 this entry previously estimated. The sixth slice closed 3 of those 20 (Toast, Banner,
  Callout), leaving 17: badges and chips, avatars, progress and spinner, skeleton and empty/zero
  state, carousel, lightbox, and toolbar (11 names, already flagged in `docs/anatomy-1.0.0.md`'s
  own **Settled decisions**), plus six names that re-verification found cited nowhere in the
  document and named in none of its "still open" notes — Link, Table, Data grid, Accordion,
  Disclosure, and Infinite scroll — tracked in issue #48 rather than assigned to a slice, since how
  they group is a scoping call for a human, the same way tokens, information architecture, and
  content each got their own scoping issue before being drafted. The seventh slice closes 2 of the
  first 11 — `A-097`–`A-098` for Badge and Chip, chosen because both were already partially
  characterized by the sixth slice's own "Not folded with Badge or Chip" paragraph and, unlike the
  six issue #48 names, neither carries an open scoping call of its own. 15 names remained after the
  seventh slice: avatars, progress and spinner, skeleton and empty/zero state, carousel, lightbox,
  and toolbar, plus the six still tracked in issue #48. The eighth slice closes all six of the first
  group — `A-099`–`A-105` for Avatar, Progress and spinner (folding Progress bar and Spinner into
  one entry), Skeleton, Empty and zero state (folding Empty state and Zero state into one entry),
  Carousel, Lightbox, and Toolbar — chosen because, unlike the six issue #48 names, none of the six
  carried an open scoping call, and all nine Vocabulary IDs the slice cites already existed with no
  companion Vocabulary addition needed. Only the six issue #48 names — Link, Table, Data grid,
  Accordion, Disclosure, and Infinite scroll — remain open, correcting this entry's prior "15 names
  remain" to the current count of six. The scoping call issue #48 reserved for these six — the
  issue itself closed once its bookkeeping finding was fixed, without that call actually being made
  — is resolved in `docs/anatomy-1.0.0.md`'s own **Settled decisions**, not here: Link stands alone;
  Data grid extends Table rather than folding with or separating from it; Accordion composes from
  Disclosure rather than raising a fold question at all; Infinite scroll stands alone, reusing
  Progress and spinner's construction for its own loading indicator. Ready to draft as a ninth
  slice. Each is additive follow-up work, a natural first project for an outside contributor, each
  its own bounded, separately scoped contribution rather than one PR closing the whole gap. Phase 2
  is not complete while those remain unbuilt.

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
