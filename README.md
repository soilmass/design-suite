# Design Suite

Nine documents describing what a website consists of, what bounds it, how to decide it, how to build it, how to check it, how to read someone else's, and how all of that changes.

**State as of 2026-09-03** — complete and validating. 1,196 registered identifiers, zero dangling references.

---

## Read in this order

New to the suite, read three: **Suite Architecture** for how the documents relate, **Composition** for what the choices are, **Decision** for how to set them. That is enough to use it.

| # | Document | Version | Tier | Answers |
|---|---|---|---|---|
| — | `suite-architecture.md` | 1.0.0 | — | How the documents depend on each other |
| 1 | `docs/vocabulary-1.0.0.md` | 1.0.2 | 0 | What does this term mean? |
| 2 | `docs/constraints-1.0.0.md` | 1.0.1 | 0 | What may not be done? |
| 3 | `docs/anatomy-1.0.0.md` | 1.2.0 | 1 | What is this made of? |
| 4 | `docs/composition-1.0.0.md` | 1.0.2 | 1 | What choices exist? |
| 5 | `docs/decision-1.0.0.md` | 1.0.2 | 2 | What should they be set to? |
| 6 | `docs/implementation-1.0.0.md` | 1.0.2 | 2 | How does that get built? |
| 7 | `docs/verification-1.0.0.md` | 1.0.3 | 3 | How do I confirm it? |
| 8 | `docs/diagnosis-1.0.0.md` | 1.0.1 | 3 | How do I read a site I did not build? |
| 9 | `docs/governance-1.0.0.md` | 1.0.0 | none | How does any of this change? |

Filenames carry the version at which a document was created. The version in front matter is current. They diverge as documents are patched, which is intentional — renaming files breaks links.

---

## The one rule

**Documents cite downward only.** Never upward, never sideways. Tier 0 depends on nothing; Governance sits outside and cites no identifiers at all. Everything else in the architecture follows from this.

---

## Running the checks

```bash
cd tooling
pip install pyyaml
python3 validate.py
```

Checks front matter, tier correctness, declared exports against actual, dependency direction, every cross-reference, and Governance's orthogonality. Regenerates `registry.yaml`. **Run before any commit.**

Prose linting for the refused-terms list:

```bash
vale --config=tooling/vale/.vale.ini docs/
```

Decision completeness — for a team using this suite, not for this repo. Joins your project's
ADR directory against `tooling/registry.yaml` and reports which of the 67 Composition families
are decided versus still on default:

```bash
python3 tooling/decision_completeness.py path/to/your/adrs
```

ADR format and sample fixtures: `tests/decision_completeness/fixtures/`.

---

## Contributing

Contributions are welcome. `CONTRIBUTING.md` has the process — kinds of change, what a pull
request needs to contain, review — and `ROADMAP.md` has where the suite is headed next and why
that order. If you are an AI agent, start at `AGENTS.md` instead: orientation, how to find a task
with no one assigning you one, and how to get reviewed.

---

## What is not covered

Stated so it is not discovered later.

- **Anatomy is rendering primitives only.** Components, tokens, information architecture, and content need further volumes. These enter additively with new identifiers.
- **Decision completeness is unbuilt.** Nothing reports which of the 67 families have been decided versus left on defaults. Small, high-value, and the one build recommended in `audit/`.
- **Congruence checking has no tool** and probably cannot have one. Human reading on a schedule.
- **Citation correctness is unautomatable.** The validator confirms an identifier resolves, never that it is the intended one. Second reader, no alternative.
- **Constraints Part C is legally volatile** and is a map of where obligations sit, not legal advice. Quarterly recheck per jurisdiction.

---

## Provenance

`audit/tooling-audit-2.0.0.md` records where the suite duplicates existing standards, where it names tools, and where it is genuinely alone. Its honest conclusion: the contribution is assembly and completeness, not mechanism. Every individual pattern has a prior, and they are catalogued there.

Each document ends with a **settled decisions** section recording judgement calls and why. Those exist to survive the person who made them — read them before reversing anything that looks arbitrary.

---

## License

MIT — see `LICENSE`.
