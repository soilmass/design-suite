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
  scope. Three component slices have landed: `docs/anatomy-1.0.0.md` is now 1.3.0, exports
  `A-001`–`A-078`. The first slice added `A-062`–`A-066` for Button, Card, Tooltip/Popover,
  Dialog, and Tabs; the second added `A-067`–`A-076` for the input controls — Text input,
  Checkbox, Radio group, Switch, Select and combobox, Slider, Stepper, Segmented control,
  Dropzone, and Fieldset; the third added `A-077`–`A-078` for the menu family — Menu (covering
  dropdown menu and context menu) and Command palette. Counted against the current export index,
  the three slices together cite 28 of the 55 names in Vocabulary's `H · Components` part
  (`V-310`–`V-364`) — a little over half. Tokens are no longer an open gap: the scoping
  discussion the first slice deferred it to has since happened and closed negative (issue #13,
  closed) — `docs/anatomy-1.0.0.md`'s own **Settled decisions** section now records tokens as
  settled out of scope, not deferred, because every parameter, range, and derived fact a token
  could need already resolves to an existing A-ID (a color-ramp step to `A-014`, spacing to
  `A-036`, a radius to `A-026`, and so on) or to Implementation's `T`-namespace, which owns the
  token wrapper itself. Information architecture and content remain open on the same terms as
  before, each with its own unresolved scoping issue — content is issue #10, information
  architecture is issue #11, both still open. The remaining ~27 names in Vocabulary's `H` part
  (toasts and banners, callouts, badges and chips, avatars, breadcrumb and pagination, progress
  and spinner, skeleton and empty/zero state, facets, carousel, lightbox, toolbar, hamburger
  menu, and others), plus information architecture and content, remain natural first projects for
  an outside contributor, each its own bounded, separately scoped contribution rather than one PR
  closing the whole gap. Phase 2 is not complete while those three remain open.

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
