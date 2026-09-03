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

### Added
- CI enforcement of `tooling/validate.py` and the Vale prose lint, via
  `.github/workflows/validate.yml`, running on every pull request and on push to `main`. Closes
  the last `ROADMAP.md` Phase 1 gap. Open as PR #1 (`ci/validate-and-vale-on-pr`), not yet merged.

---

## 2026-09-03

### Added
- Repository created (`d5503b2`): the nine governed documents (Vocabulary, Constraints, Anatomy,
  Composition, Decision, Implementation, Verification, Diagnosis, Governance), `suite-architecture.md`
  as document 0, `tooling/validate.py` and the generated `tooling/registry.yaml`, Vale prose
  linting (`tooling/vale/`), `README.md`, `CONTRIBUTING.md`, and `ROADMAP.md`.
