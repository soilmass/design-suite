# adr/

Architecture Decision Records for **this repository's own** process, tooling, and contribution
architecture — not to be confused with the `F##`-family ADRs `tooling/decision_completeness.py`
expects from a *downstream* team building an actual website with this suite. Different namespace,
different subject, different audience. A design-suite ADR never cites an `F##` family; a
downstream team's ADR never needs to know this directory exists.

## Index

| ID | Title | Status |
|---|---|---|
| [ADR-0001](0001-ai-agents-as-primary-contributors.md) | AI agents as primary contributors; AGENTS.md as their front door | Accepted |
| [ADR-0002](0002-anatomy-single-writer.md) | docs/anatomy-1.0.0.md is single-writer per batch, permanently | Accepted |
| [ADR-0003](0003-registry-regeneration-benign-conflict.md) | tooling/registry.yaml regeneration conflicts across concurrent PRs are benign by default | Accepted |
| [ADR-0004](0004-peer-review-via-dispatched-agent.md) | Second-reader review via an independently-dispatched agent, evidenced by a comment | Accepted |
| [ADR-0005](0005-no-direct-to-main.md) | No direct-to-main pushes, including the maintainer's own small fixes | Accepted |
| [ADR-0006](0006-citation-elaboration-vs-homonym-test.md) | The elaboration-vs-homonym test for judging a citation's correctness | Accepted |

## Format

One file per decision, `NNNN-slug.md`, numbered sequentially and never renumbered — the same
stability discipline `suite-architecture.md` applies to the suite's own IDs, applied here to a
different namespace. Each carries a small YAML header (`id`, `title`, `status`, `date`) and three
sections: **Context** (what forced the decision), **Decision** (what was decided and, where a real
alternative existed, what was rejected and why), **Consequences** (what actually happened as a
result — filled in with evidence once there's evidence, not speculation at write time).

Status is one of `accepted`, `superseded` (name the successor), or `rejected` (kept for the
record, not deleted — the same "don't delete, mark and point" discipline `suite-architecture.md`
uses for retired IDs).

## When to write one

See `AGENTS.md`'s "Do the work" section for the trigger criteria. Short version: write one when a
decision will bind how future contributors work here, not when documenting a one-off fix — a
one-off fix gets a PR description, not an ADR.
