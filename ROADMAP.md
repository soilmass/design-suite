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
- **Anatomy volume 2.** Components, tokens, information architecture, and content — the volumes
  `README.md` already flags as needed beyond the current rendering-primitives-only scope. Larger
  than the decision-completeness build and a natural first project for an outside contributor
  once Phase 1 exists.

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
