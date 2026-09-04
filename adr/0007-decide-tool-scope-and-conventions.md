```yaml
id: ADR-0007
title: tooling/decide's build authority and the conventions it establishes
status: accepted
date: 2026-09-04
```

# ADR-0007 · tooling/decide's build authority and the conventions it establishes

## Context

`AGENTS.md`'s "Find your task" section names a boundary that doesn't move: `audit/
tooling-audit-2.0.0.md` Part VI recommends exactly **one** tooling build (item 2, decision
completeness — `tooling/decision_completeness.py`, shipped) and explicitly warns that building
the rest of its gap register turns "a plan" into "a wish list." Any agent proposing a new tool is
supposed to check whether the audit already rated it not worth building before doing so.

`tooling/decide/` — a package helping an AI agent make and record the `D204` "first pass"
Composition decisions for a real project — is not in that register at all. The audit predates it
entirely; Part VI's gap register was written against the suite as it stood at `tooling-
audit-2.0.0.md`'s own date, before this capability was conceived. So the boundary's actual test
("did the audit already say no to this") doesn't apply cleanly — the audit never evaluated this
tool, favorably or otherwise, because it didn't exist yet to evaluate.

This is exactly the situation `AGENTS.md`'s own carve-out anticipates for a decision that will
shape future contributors' work: resolved unilaterally inside a task, or delegated. This one was
delegated. The suite's primary user was reframed this session from "a human or agent reading nine
documents" to "an AI agent that needs to make the decisions those documents describe" — a
deliberate strategic pivot the user requested directly ("help me figure out how this will
actually serve someone... and help me get to there"), refined through `superpowers:brainstorming`,
written up as `specs/2026-09-04-decision-making-tool-design.md`, and confirmed by the user at each
major fork before implementation began. The audit's Part VI boundary exists to stop an agent from
unilaterally deciding a new tool is worth building on its own initiative — it does not, and was
never meant to, block a tool the user explicitly commissioned as the suite's next phase.

## Decision

`tooling/decide/`'s existence is in scope, authorized by direct human delegation of exactly this
kind of call, not by a green light from the Part VI register. This ADR records that authority so
a future reader checking `AGENTS.md`'s boundary against this tool finds an answer instead of an
apparent contradiction.

Building it also introduced three standing conventions that bind whatever extends or consumes it
next, recorded here because they are exactly the kind of thing `AGENTS.md`'s "Record decisions"
section asks for — a new standing convention, not a one-off implementation detail:

1. **A downstream project's brief lives at `.design-suite/brief.yaml`**, with five required
   fields (`purpose`, `audience`, `brand`, `jurisdiction`, `constraints`). This is the one piece of
   per-project context `tooling/decide` cannot derive from the suite itself or from the target
   repository's own code — see `specs/2026-09-04-decision-making-tool-design.md`'s input model for
   why. Any future tool reading the same kind of project context should read this same file and
   schema rather than inventing a second one.
2. **An agent's decisions for a run are expressed as `decisions.yaml`**, a list of `{family,
   value, rationale, confidence}` entries — the artifact `context`'s output is meant to be turned
   into, and `apply`'s only accepted input. This is the shape any future extension to `apply`
   (e.g. supporting more than the current 11 target families) has to keep compatible with, or
   explicitly version.
3. **Generated ADRs land in the target project's own `<target-repo>/adr/` directory**, in the
   exact format `tooling/decision_completeness.py` already expected before this tool existed —
   `tooling/decide` did not invent a new ADR shape, it writes to the one the suite already
   specified. This convention was a constraint, not a choice: deviating from `decision_
   completeness.py`'s existing `front_matter()` contract would have broken the self-check `apply`
   runs as its own last step.

## Consequences

Future work extending `tooling/decide` (most concretely, growing `TARGET_FAMILIES` past the
current 11 — explicitly out of scope for this build, per `specs/2026-09-04-decide-tool-plan.md`'s
Global Constraints) inherits these three conventions rather than re-deciding them. A future agent
proposing an unrelated new tool still has to clear the Part VI boundary in the normal way; this
ADR is not a general exception to it, only the record of why this one specific, user-delegated
build did not need to.
