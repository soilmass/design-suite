```yaml
id: ADR-0003
title: tooling/registry.yaml regeneration conflicts across concurrent PRs are benign by default
status: accepted
date: 2026-09-03
```

# ADR-0003 · tooling/registry.yaml regeneration conflicts across concurrent PRs are benign by default

## Context

`tooling/registry.yaml` regenerates from scratch on every `python3 tooling/validate.py` run —
every PR that touches `docs/`, and every PR that touches `validate.py`'s own registry-generation
logic, rewrites the whole file. Two concurrent PRs both producing a `registry.yaml` diff, based on
whatever `main` looked like when each one's worktree was created, will conflict at merge time
purely from both regenerating the file — with no relationship to whether the two PRs' actual
content conflicts at all.

This surfaced concretely: a PR fixing how `validate.py` computes each ID's `since` field (its
generation logic itself) and a PR adding new Anatomy IDs (which regenerates the registry as a
side effect) landed in the same batch, created minutes apart, neither able to see the other's
diff before its own PR was opened. The result was not a text conflict in the git sense — it was
subtler: the `since`-tracking fix correctly preserves whatever value already exists for a known
ID rather than recomputing it, which is right in general, but meant that once the new Anatomy IDs
had merged under the old, briefly-still-buggy logic, the fixed logic had no way to distinguish
"existing and correct" from "existing and stale" — it just carried the stale value forward. Fixing
it required a dedicated follow-up commit, hand-correcting the affected entries against a verified
known-wrong prior value.

## Decision

Treat a `registry.yaml` diff conflict between two concurrent PRs as benign and expected by
default — resolved by rebasing the losing PR onto the now-current `main` and re-running
`validate.py`, never by hand-merging the YAML. This is not a special case requiring its own
tooling; it is the same "before you open the PR" verification step every contributor already runs,
just re-run after a rebase instead of only before the first push.

The one situation this default does not cover: when one of the two concurrent PRs changes the
registry *generation logic itself* (as opposed to merely triggering a regeneration by adding
content), a rebase-and-rerun does not retroactively correct data that already merged under the old
logic. That case needs a deliberate, explicit follow-up check across the whole registry after
the logic-change PR lands, not an assumption that the next regeneration will silently self-heal.

## Consequences

`AGENTS.md`'s "Do the work" section states the general rule (expect a `registry.yaml` diff, resolve
by rebase and rerun) as standing guidance. The specific edge case — a concurrent batch containing
both a `docs/`-touching agent and a `validate.py`-registry-logic-touching agent — is flagged
explicitly in the same section, precisely because the general rule alone would not have caught it;
it took a maintainer noticing the `since` field was wrong on inspection, not an automated check,
since `validate.py` has no way to know a "carried forward" value is stale versus genuinely correct.
