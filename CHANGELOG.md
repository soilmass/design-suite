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

## 2026-09-04

### Added
- `tooling/decide/`: a new package helping an AI agent make and record the `D204` "first pass"
  Composition decisions (`F01, F02, F05.1, F11.1, F15, F17, F22, F31, F32, F40, F64`) for a real
  downstream project — the suite's first capability built for an agent *acting on* the suite
  rather than reading it. Two CLI subcommands, `context` (surfaces every undecided target
  family's range, bounding Constraints, and governing Decision-round guidance) and `apply`
  (validates a `decisions.yaml` an agent produced against two mechanical guardrails, writes real
  ADRs matching `tooling/decision_completeness.py`'s existing format, self-checks the result).
  Built via 8 TDD tasks plus a whole-branch review and two independent-review fix waves — see
  `specs/2026-09-04-decision-making-tool-design.md` and `specs/2026-09-04-decide-tool-plan.md`
  for the full design and plan, and `adr/0007-decide-tool-scope-and-conventions.md` for the
  build's authority (this tool sits outside `audit/tooling-audit-2.0.0.md` Part VI's register,
  built on direct human delegation of that call) and the standing conventions it establishes
  (`.design-suite/brief.yaml`'s schema, `decisions.yaml`'s schema, the target-repo `adr/`
  location contract). PR #72, merged. `ROADMAP.md`'s rewrite around this as the flagship goal —
  replacing the three-phase structure that closed out in full before this pivot — is deliberately
  sequenced after this PR, not included in it, so the roadmap describes something real rather than
  something proposed; not yet done as of this entry.

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
- CI grew a second job, `pytest-suites`, running `python3 -m pytest tests/` (repo-root discovery,
  so any future `tests/<new-thing>/` suite is picked up with no further workflow edits) alongside
  the existing `validate.py`/Vale job — the regression suite from PR #5 existed and passed locally
  but nothing in CI had been running it. PR #8 (`ci/run-pytest-suites`, `5d9375b`), merged.
- An adversarial QA pass over `tooling/validate.py` and `tooling/decision_completeness.py` found
  and fixed seven real crash/mis-scoring bugs triggered by malformed or absent front matter (a
  YAML parse error, missing `version:`/`tier:` keys, a non-dict front matter body, an export
  namespace with zero actual IDs silently reading `ok` instead of `MISMATCH`, and a
  non-list `families:` value in an ADR producing garbage per-character problems instead of one
  clear message) — both tools previously assumed well-formed input throughout. Added
  `tests/decision_completeness/`'s first pytest coverage from scratch (`conftest.py` +
  `test_decision_completeness.py`, its `adrs`/`empty` fixtures had existed since PR #4 with
  nothing running them) plus twelve new fixtures under `tests/validate/`. PR #25
  (`fix/adversarial-qa-crash-guards`, `b0b39b8` + `e9b4f08`), merged.
- Anatomy volume 2 progressed through three more component/scope slices and closed both remaining
  README "What is not covered" gaps (tokens, information architecture, content), taking
  `docs/anatomy-1.0.0.md` from 1.1.0 to 1.5.0 (`exports: A-001–A-094`) and adding
  `docs/vocabulary-1.0.0.md` V-613–V-621 (1.0.3 → 1.1.0) for the content-element terms that didn't
  already exist:
  - Input controls, the second component slice — text input/textarea, checkbox, radio group,
    switch, select/combobox, slider, stepper, segmented control, dropzone, fieldset (`A-067`–
    `A-076`). PR #14 (`anatomy-input-controls-slice`, `c25bb5b`), merged.
  - The menu family (dropdown/context menu folded, command palette kept separate; `A-077`–`A-078`),
    and — closing issue #13 — Anatomy's tokens item settled from "deferred" to genuinely out of
    scope (Implementation's `T`-namespace and the DTCG spec it mandates already own a token's full
    structure). PR #22 (`anatomy-menu-slice-and-tokens-scope`, `987b2b4`), merged.
  - The content (issue #10) and information-architecture (issue #11) scoping questions resolved
    and written into Anatomy's Settled decisions — content as atomic elements rather than content
    types, IA to the component-entry shape only, rejecting the "site-as-graph" relational shape as
    out of scope. No new IDs; both issues closed. PR #34
    (`docs/anatomy-content-ia-scoping-resolution`, `b47b1cd`), merged.
  - The information-architecture slice drafted against that resolution — breadcrumb, pagination,
    facets, a folded navigation entry (global/local/utility, with hamburger menu as its overflow
    control), skip link (`A-079`–`A-083`). PR #36 (`docs/anatomy-ia-slice`, `54bba8f`), merged.
  - The content-elements slice — headline, deck, eyebrow, byline, body, pull-quote, stat/callout,
    caption, CTA text, list, metadata block (`A-084`–`A-094`), plus the nine new Vocabulary terms
    (`V-613`–`V-621`) eight of them needed with no prior term. PR #37
    (`docs/anatomy-content-elements-slice`, `e6fb65d`), merged.
  Still open, tracked in `ROADMAP.md` Phase 2: the remainder of Vocabulary's `H · Components` part
  (toasts and banners, callouts, badges and chips, avatars, progress and spinner, skeleton and
  empty/zero state, carousel, lightbox, toolbar).
- `CONTRIBUTING.md` gained a "Concurrent agent contribution" section — the single-writer
  constraint on Anatomy's `A-###` range, the `registry.yaml` regeneration/benign-conflict pattern,
  and why independent re-verification matters, each grounded in something that had actually
  happened in this repo's history by that point (11 merged PRs across two dispatched batches).
  PR #16 (`docs/contributing-concurrent-agents`, `4ac3008` + `66187d1`), merged.
- `AGENTS.md` added at the repo root — the front door for an AI agent contributing here cold: how
  to orient, the task-discovery cascade (`ROADMAP.md` → `proposal`-labeled issues → generating
  audit-shaped work), the Anatomy single-writer constraint, citation-verification discipline, the
  PR/review process including dispatching an independent peer-review agent, and known gotchas
  (GitHub's issue-closing keyword parser does plain substring matching, not negation-aware
  parsing; self-approval is blocked on this single-account repo). `CLAUDE.md` gained a pointer to
  read it first; `CONTRIBUTING.md`'s concurrent-agent section was trimmed to a stub pointing at it
  instead of duplicating it. PR #38 (`docs/agents-md-contribution-model`, `c5173dc` + `9f1b6ab`),
  merged.
- GitHub's pull request and issue templates gained a pointer to `AGENTS.md` as the front door for
  AI agent contributors, added to both issue templates and the PR template — additive prose only,
  `config.yml`'s contact-links config deliberately left untouched. PR #40
  (`docs/agents-md-template-pointers`, `9d0f915`), merged.
- `tests/decision_completeness/README.md` added, matching `tests/validate/README.md`'s existing
  structure and terseness (how to run the suite, how its fixtures are organized, how to add a
  case) — the fixture-based pytest suite PR #25 added had none. PR #41
  (`tests/decision-completeness-readme`, `8e2a74c`), merged.
- `adr/` added: six retroactive Architecture Decision Records recording this repository's own
  process precedents, previously scattered across closed PR bodies and comment threads with no
  durable, citable home — AI agents as primary contributors (`0001`), Anatomy's single-writer
  constraint (`0002`), the `registry.yaml` regeneration/benign-conflict pattern (`0003`), peer
  review via a dispatched agent (`0004`), the no-direct-to-main policy (`0005`), and the citation
  elaboration-vs-homonym test that adjudicated the V-195/V-348 dispute (`0006`) — plus an
  `adr/README.md` index. `AGENTS.md` gained a "Record decisions (ADRs)" section with concrete
  trigger criteria. PR #54 (`docs/retroactive-adrs`, `fa87ed4`; `d79d727` then added ADR-0001 and
  ADR-0004 as worked examples in that section's trigger bullet, caught by peer review), merged.
- The PR template's header comment gained a pointer to `adr/` alongside its existing `AGENTS.md`
  pointer, for decisions that bind future contributors. PR #55 (`docs/pr-template-adr-pointer`,
  `0767f6e`), merged.
- `ROADMAP.md`'s Phase 3 gained a concrete four-item task list — a worked example, on-ramp polish
  surfacing `audit/tooling-audit-2.0.0.md`'s "assembly, not new mechanism" framing, this
  `CHANGELOG.md` completeness check, and repository discoverability metadata gated on a separate
  human confirmation — now that Phase 1 and Phase 2 have both closed. PR #65
  (`roadmap/phase-3-scoping`, `9db70ca`), merged.

### Fixed
- `tooling/validate.py` was hardcoding every registry entry's `since` field to `1.0.0` on every
  regeneration, regardless of when an ID actually first appeared — silently false for anything
  added after the initial commit. Fixed to carry forward an existing entry's recorded `since`, and
  to stamp a genuinely new ID with its owning document's current front-matter version. PR #9
  (`fix/registry-since-provenance`, `36f8804`), merged. This couldn't retroactively fix IDs already
  recorded wrong under the old logic; `A-062`–`A-076` (stamped `1.0.0` by the two Anatomy slices
  that landed before this fix) were hand-corrected to their real landing versions (1.1.0, 1.2.0) in
  a follow-up chore, `29a857d`.
- `README.md`'s per-document version table had drifted from the real front-matter `version:` on
  seven of nine documents after several corrective/additive edits landed without a matching README
  update. PR #15 (`fix/readme-version-table-2026-09-03`, `f1033de`), merged.
- `ROADMAP.md`'s Phase 2 "Anatomy volume 2" bullet still described only the first component slice
  after two more had landed; corrected to the real state (three slices, tokens closed rather than
  deferred, content/IA still open). PR #30 (`docs/roadmap-anatomy-vol2-refresh-2026-09-03`,
  `d4bd02e`), merged.
- A correction-backlog round closed the findings from four self-generated audits (per `AGENTS.md`'s
  "generate audit-shaped work" step, before that file existed as such): issue #17 (an
  ownership-boundary read finding six places Decision, Implementation, Verification, and Diagnosis
  restated another document's owned fact instead of citing it), issue #20 (Diagnosis restating
  Constraints C026's 320px reflow figure twice with no citation), issue #21 (a second look at Vale
  refused-terms exemptions finding one, `F20.1`, whose exemption claimed coverage it didn't have),
  and issue #23 (a citation-correctness second read finding wrong-sense/mismatched citations across
  Composition, Decision, Implementation, and Vocabulary). Landed as:
  - Implementation citing Anatomy instead of restating it in eight `T`-entries, and declaring the
    resulting `Anatomy ^1` dependency (a side finding off issue #13). PR #19
    (`fix/implementation-anatomy-citations`, `ca318dd`), merged.
  - Vocabulary's `V-469` Vale-exemption comment corrected from `C042` (accessible authentication)
    to `C046` (name, role, value) — the ID that actually defines "accessible name". PR #26
    (`fix/vocabulary-accessible-name-citation-2026-09-03`, `6b833df`), merged.
  - Decision: removed two restated Constraints values (`D021`/C001, `D051`/C028), corrected `D012`'s
    misattributed `C039`–`C042` bound-set (that range is `F21`'s, not `F63`–`F67`'s), and added a
    missing `F51` citation to `D061`. PR #27 (`fix/decision-citation-restatements-2026-09-03`,
    `c39fabe`), merged.
  - Diagnosis: added the missing `C026` and `D111` citations behind two restated values, closing
    issue #20. PR #28 (`fix/diagnosis-c026-d111-citations`, `9a9707f`), merged.
  - Verification: added its first `D-###` citations despite declaring a Decision dependency —
    `C026` (X015), `D111` (X220), and a new "Verifies" column citing `D100`–`D109` against the
    Congruence audit table (X211–X219). PR #29
    (`fix/verification-decision-constraints-citations`, `f58ab87`), merged.
  - Composition's `F20.1` renamed "Responsive strategy" → "Adaptation strategy" and its Vale
    exemption removed — the family's three-way dial isn't the two-way distinction Vocabulary
    `V-611` disambiguates, so the exemption's coverage claim didn't hold. PR #31
    (`fix/f20-1-adaptation-strategy-rename`, `835bef7`), merged.
  - Implementation: six more citation errors corrected in and around the Part V enforcement table
    (`K058` restating C026, `K015` mis-citing C105 for a layout-shift trigger it doesn't cover, the
    C038 table row crediting the wrong K-ID, `K004` over-claiming C033, `K013`'s C042→C046
    Vale-exemption fix mirroring PR #26's, `K007`'s C027 misattribution). PR #32
    (`fix/implementation-enforcement-citations`, `5812680`), merged.
  Two further findings from issue #18 (a governance fit-for-purpose review: zero of 11 sampled PRs
  had checkable review evidence, and `CONTRIBUTING.md`'s org-tier trigger measured contributor
  headcount when the real strain observed was review falling behind concurrent-batch velocity)
  were fixed alongside the same round: Governance's `G082` now defines what counts as evidence of
  a citation review and reworks the tier-exit trigger to the observed one (PR #33,
  `fix/governance-g082-evidence-and-trigger`, `e320225`, merged), and `CONTRIBUTING.md`'s own
  restatement of that trigger was synced to match (PR #35,
  `docs/contributing-org-tier-trigger-sync`, `3909e32`, merged).
- CI's `actions/checkout` and `actions/setup-python` were pinned to floating major-version tags
  (`@v4`, `@v5`) while the workflow's Vale binary was already checksum-verified — a supply-chain
  gap, since a tag can be moved but a commit SHA cannot. Pinned both to the commit SHA each tag
  currently resolved to. PR #39 (`ci/pin-actions-to-sha`, `0003920`), merged.
- A fresh whole-suite read of `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, and `README.md` together
  (as their merged, standing state, not just as individual PR diffs) turned up three independent
  drifts: `README.md`'s document table and identifier count hadn't been resynced since the
  content-elements slice landed (seven of nine versions stale, count off by 42); `AGENTS.md`'s
  single-writer bullet pointed at "Known gotchas" for its reasoning when the reasoning actually
  lives in "Do the work"; and `CONTRIBUTING.md` still described `validate.py`/Vale as running "on
  the honor system" with CI enforcement merely "tracked," though it had run on every PR and push
  to `main` since PR #1. A fourth finding — `README.md`'s "What is not covered" Anatomy bullet
  overclaiming what still needed further volumes — needed editorial judgment and was filed as
  issue #44 instead of guessed at here. PR #45 (`docs/agents-crossref-sync`, `7440e07`), merged.
- `README.md`'s "What is not covered" Anatomy bullet, filed as issue #44 above, was rewritten:
  three of its four claims (tokens deferred, information architecture and content still open) no
  longer matched `docs/anatomy-1.0.0.md`'s state at 1.6.0 — tokens had been settled out of scope
  and both information architecture and content had shipped full slices. Reworded short, pointing
  to `ROADMAP.md` Phase 2 for the numeric specifics instead of restating them, closing issue #44.
  PR #51 (`docs/readme-anatomy-scope-bullet-issue44`, `9115c35`), merged.
- `README.md`'s adjacent "Decision completeness is unbuilt" bullet, found stale during PR #51's
  review, was removed rather than reworded — `tooling/decision_completeness.py` has existed since
  PR #4, is tested, and is documented, so it is no longer a gap for the "What is not covered"
  section to list. PR #53 (`docs/readme-decision-completeness-built`, `4b1e7d5`), merged.
- `README.md`'s document version table drifted again after six more Anatomy content slices and a
  Vocabulary patch landed since PR #15's sync (`Anatomy` 1.5.0 → actual 1.6.1, `Vocabulary` 1.1.0
  → actual 1.1.1), and the registered-identifier count was off by two (1,238 vs. the registry's
  1,240). PR #56 (`docs/readme-version-table-resync-2026-09-03`, `40c2a50`), merged.
- `CLAUDE.md`'s and `suite-architecture.md`'s "Stable identifiers" worked-example tables cited
  six IDs that don't exist anywhere in the suite (`V-204`, `A-118`, `T044`, `K019`, `X031`,
  `G004`) and two more that exist but mean something different than claimed (`C012`, `D007`).
  Replaced all nine examples in `suite-architecture.md` §3 with real, grepped-and-verified IDs, and
  removed `CLAUDE.md`'s duplicate copy of the table — the exact mechanism that had let the two
  drift independently — replacing it with a namespace-to-owner table pointing at
  `suite-architecture.md` §3 as the single source of truth. Resolved finding #1 of issue #57. PR
  #59 (`docs/stable-identifiers-table-fix-57`, `09ee192`), merged.
- `AGENTS.md`'s "Start here" reading order never named `README.md`, even though
  `CONTRIBUTING.md` — reached at step 2 of that same order — opens by pointing the reader to
  README's own "read in this order" section, a gap issue #57's second finding flagged. Added
  `README.md` as the first step in the order. PR #60 (`docs/agents-md-readme-reading-order`,
  `1efb929`), merged.
- `README.md`'s document version table drifted a third time after the ninth Anatomy slice
  (`A-106`–`A-111`, PR #63) closed Vocabulary's `H`-part entirely: synced `Anatomy` 1.6.1 → 1.9.0,
  the identifier count 1,240 → 1,255, and retired the "Only components remain partially open in
  Anatomy" bullet from "What is not covered" now that it no longer described anything true. PR #64
  (`docs/readme-resync-anatomy-volume-2-complete`, `f758896`), merged.
