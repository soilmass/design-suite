# Changelog

Repository and infrastructure history — when the repo was created, when process documents were
established, when CI landed. Not a version history: this suite has no repo-wide version number.
Each document in `docs/` versions independently in its own front matter (`suite-architecture.md`
§6, "Versioning"), and that history lives in `tooling/registry.yaml`, not here. Restating
per-document version bumps in this file would be exactly the kind of copy §4 warns against — a
value in two places that drifts and nobody notices which copy is stale.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), scoped to
repository-level and infrastructure events rather than document content.

---

## [Unreleased]

_Nothing yet._

---

## 2026-09-03

### Added
- Repository created (`d5503b2`): the nine governed documents (Vocabulary, Constraints, Anatomy,
  Composition, Decision, Implementation, Verification, Diagnosis, Governance), `suite-architecture.md`
  as document 0, `tooling/validate.py` and the generated `tooling/registry.yaml`, Vale prose
  linting (`tooling/vale/`), `README.md`, `CONTRIBUTING.md`, and `ROADMAP.md`.
- CI enforcement of `tooling/validate.py` and the Vale prose lint, via
  `.github/workflows/validate.yml`, running on every pull request and on push to `main`. Closes
  the last `ROADMAP.md` Phase 1 gap: `G002`'s small-change test no longer depends on a
  contributor remembering a local command. PR #1 (`ci/validate-and-vale-on-pr`, `b45bd4e`),
  merged.
- `LICENSE` (MIT), this `CHANGELOG.md`, and `.editorconfig` — the repo previously had no license,
  which blocked real external contribution despite `CONTRIBUTING.md` inviting it. PR #2
  (`add-license-changelog-editorconfig`, `390fab3`; `2914308` then aligned `.editorconfig`'s
  Python/Markdown indentation and line-length conventions with Google's style guides), merged.
- GitHub pull request and issue templates (`.github/PULL_REQUEST_TEMPLATE.md`,
  `.github/ISSUE_TEMPLATE/`) encoding `CONTRIBUTING.md`'s change/reason/migration proposal shape
  and the `G020`–`G025` kind-of-change classification as the default instead of prose a
  contributor has to reconstruct by hand. PR #3 (`add-github-contribution-templates`, `3a1d4c1`),
  merged.
- `tooling/decision_completeness.py`: for a downstream team using this suite (not for this repo),
  joins their ADR directory against `tooling/registry.yaml` and reports which of the 67
  Composition families are decided versus still on default. Sample ADR fixtures under
  `tests/decision_completeness/fixtures/`. PR #4 (`decision-completeness-checker`, `5c160ae`;
  `238a82a` then fixed the tool to exit nonzero when it reports a real problem, matching
  `validate.py`'s own convention), merged.
- A regression test suite for `tooling/validate.py` under `tests/validate/`: a pytest harness
  (`conftest.py`) running the real, unmodified `validate.py` against a synthetic nine-document
  fixture suite, covering all five check categories plus a red/green dependency-direction pair.
  PR #5 (`test/validate-py-regression-suite`, `f6cbc97`), merged.
- Vale refused-terms warnings triaged: of 36 outstanding, 2 were genuine prose problems and
  reworded, 29 were false positives given narrowly scoped `Suite.RefusedTerms` exemption
  comments with a stated reason each, and 5 (in `docs/anatomy-1.0.0.md`) were left for the
  concurrent anatomy PR below to avoid a merge conflict. PR #7 (`vale-refused-terms-triage`,
  `5150bb9`), merged.
- A first slice of Anatomy volume 2 landed in `docs/anatomy-1.0.0.md`: component anatomy for
  Button, Card, Tooltip/Popover, Dialog, and Tabs — the first of the four gaps README's "What is
  not covered" names (components, tokens, information architecture, content) to be closed.
  Anatomy moves 1.0.0 → 1.1.0 (see `tooling/registry.yaml` for the ID-level detail); tokens,
  information architecture, and content remain open, tracked in `ROADMAP.md` Phase 2. PR #6
  (`anatomy-components-slice`, `4c99216`; `33b721c` then fixed a wrong-sense citation caught in
  review before merge), merged.
