# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Contributing to this repository, in any capacity — read `AGENTS.md` first, in full, before this
file or anything else.** It's the front door for any agent: how to orient, how to find a task, and
how to get reviewed. What follows here is the technical model (tiers, IDs, versioning) `AGENTS.md`
assumes you already have.

## What this repo is

Nine documents that together define what a website consists of, what bounds it, how to
decide it, how to build it, how to check it, and how to read someone else's. `suite-architecture.md`
is document 0 — the contract that lets the other nine change independently without breaking
each other. Read it before editing any document in `docs/`; every rule below comes from it.

This is a documentation suite, not an app. There is no build/runtime — "development" here means
editing the Markdown documents and keeping the cross-document contract intact. This CLAUDE.md is
about contributing to *these documents*, not about how to use the design system they describe.

## Commands

```bash
cd tooling
pip install pyyaml
python3 validate.py                              # run before any commit
```

`validate.py` checks front matter, tier correctness, declared exports (`exports:` in front
matter) against IDs actually found in each document, dependency direction, every cross-reference,
and Governance's orthogonality (`cites_no_ids: true` documents must cite nothing). It also
**regenerates `tooling/registry.yaml`** as a side effect — if you add/retire an ID, re-run it and
commit the updated registry alongside the doc change.

```bash
vale --config=tooling/vale/.vale.ini docs/       # prose lint, refused-terms list
```

Refused-terms rules live in `tooling/vale/styles/Suite/RefusedTerms.yml`.

There is no single-test mode: `validate.py` parses and cross-checks all nine documents together
(IDs are only meaningful in the context of the whole registry), so it is always run whole-repo.

## Architecture

### Dependency tiers — cite downward only, never upward, never sideways

```
Tier 3   Verification · Diagnosis          evaluative
Tier 2   Decision · Implementation          operational
Tier 1   Anatomy · Composition              structural
Tier 0   Vocabulary · Constraints           foundational
Orthogonal  Governance                      process, cites no content
```

If a document's front matter `depends:` lists something at the same tier or higher, the suite
has a cycle — that's the one invariant `validate.py`'s check [2] exists to catch. Governance
cites no identifiers at all (`cites_no_ids: true`); if Governance ever needs to name a family ID,
something is wrong in Governance, not the family.

### Ownership — one fact, one home

| Fact type | Owner |
|---|---|
| What a thing is called | Vocabulary |
| What a thing is made of, in parameters | Anatomy |
| What choices exist, and their ranges | Composition |
| What is not negotiable, and why | Constraints |
| How to set a choice, and in what order | Decision |
| How a choice becomes a token, component, or line of code | Implementation |
| How to confirm it works, conforms, coheres, and is understood | Verification |
| How to read an existing site back into the model | Diagnosis |
| How decisions are made, changed, and retired | Governance |

If a sentence could defensibly belong to more than one owner, that's a boundary bug, not an
edge case — most often it's the Constraints/Composition boundary: a threshold (e.g. a contrast
ratio) is a Constraints fact; a family's range being *bounded by* that threshold is a Composition
fact. Composition may say "bounded below by C012," never repeat the number itself.

### Stable identifiers

| Namespace | Owner | Example |
|---|---|---|
| `V-###` | Vocabulary | `V-204` measure |
| `A-###` | Anatomy | `A-118` shadow spread |
| `F##` / `F##.#` | Composition | `F15`, `F15.2` |
| `C###` | Constraints | `C012` body text contrast floor |
| `D###` | Decision | `D007` order of operations |
| `T###` / `K###` | Implementation | `T044` token, `K019` component |
| `X###` | Verification | `X031` content stress check |
| `R###` | Diagnosis | `R012` observability class |
| `G###` | Governance | `G004` contribution path |

Non-negotiable rules: an ID is **assigned once** and **never reused**, even after retirement.
IDs are **never reordered** — display order is a rendering decision, ID order is not. New
entries are **additive only**, appended at the end; nothing is renumbered to make room. A split
family retires its old ID pointing at successors (`F43 → superseded by F43a, F43b`); a merge
keeps the surviving ID and retires the absorbed one. Renaming the human-readable name is free —
the ID is the only durable handle.

### Reference discipline

- Cite by ID (`See C012`), never by restating content (`See the 4.5:1 contrast requirement`) —
  the latter breaks silently when the value changes.
- Never copy a value across documents; a number that appears twice will drift and nobody will
  know which copy is stale.
- Never quote another document's prose — it freezes a version. Cite the ID and let the reader
  resolve current text.
- Cite the smallest unit that carries the meaning (`F15.2`, not the parent family).
- No transitive citation — if Verification needs a Constraints fact, it cites Constraints
  directly, not Composition's citation of it.

### Export surface vs. interior

Exported (citable by others; changing it is a breaking change): IDs, each ID's one-line meaning,
and the range/type of each entry. Internal (free to rewrite without a version bump): all prose,
rationale, examples, ordering/headings, and Composition's register/moves-with/independence
markers. Practically: you can rewrite a document's prose top to bottom without a version bump as
long as every ID still means what it meant.

### Versioning

Semantic versioning per document, independently:
- **Major** — an ID retired or its meaning changed. Breaking; requires a coordinated pass over
  dependents.
- **Minor** — IDs added. Additive, safe, dependents adopt whenever.
- **Patch** — prose/examples/corrections only, invisible to dependents.

`depends:` in front matter pins the **major only** (e.g. `Composition ^2` = "any 2.x"). Change
protocol for a major bump: mark the old ID deprecated with a successor named → bump minor,
publish → dependents migrate at their own pace → remove the old ID only once nothing depends on
it (that removal is the major bump). Deleting before dependents have migrated recouples the
documents.

Filenames carry the version the document was **created** at (e.g. `composition-1.0.0.md`); the
front matter `version:` is the current version. These diverge intentionally as documents are
patched — do not rename files to "fix" this, renaming breaks links.

### Front matter (required on every document in `docs/`)

```yaml
document: Composition
version: 2.1
tier: 1
owns:
  - what choices exist
  - the range of each choice
exports: F01–F68
depends:
  - Vocabulary ^1
  - Constraints ^1
reviewed: 2026-09-03
```

### The registry (`tooling/registry.yaml`)

Generated, not authored — never hand-edit it, run `validate.py` instead. It's the one shared
artifact across all nine documents; everything else is prose. It indexes every ID with its
owner, name, type, status (`active`/`superseded`), and the version it was introduced in
(`since`), plus `superseded_by` for retired IDs.

## Contributing conventions

Full contribution process (PR shape, review, kinds of change) is owned by `CONTRIBUTING.md`;
the roadmap and phase sequencing is owned by `ROADMAP.md`. Don't restate either here — read them.

- Run `python3 tooling/validate.py` before any commit; it's the whole test suite for this repo.
- Each document ends with a **settled decisions** section recording judgement calls and why —
  read it before reversing anything that looks arbitrary in that document.
- README's "What is not covered" section is the one place scope exclusions are listed — don't
  try to "complete" those unprompted, and don't copy that list here or anywhere else.
- `audit/tooling-audit-2.0.0.md` records where the suite duplicates existing standards vs. is
  genuinely novel — its conclusion is that the suite's contribution is assembly and completeness,
  not new mechanism. Read it before claiming a document "invented" something.
- `adr/` records this repository's own process/tooling decisions (why Anatomy is single-writer,
  how a contested citation gets adjudicated) — distinct from a downstream team's `F##`-family
  ADRs, which `tooling/decision_completeness.py` consumes and this repo has none of. `AGENTS.md`
  owns when to write one; don't restate that here either.
