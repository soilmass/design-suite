<!--
This template mirrors CONTRIBUTING.md — read that in full first if you haven't.
AI agent contributor? Read AGENTS.md first.
A PR is a proposed edit, not a discussion (G030): fill this in as a diff's
cover letter, not as a starting point for back-and-forth.
-->

## Kind of change

Per Governance G020 — pick one, it sets the review path below:

- [ ] Additive — new entry, section, or document. Nothing existing changes meaning. (G021: no gate.)
- [ ] Corrective — an existing entry was wrong; meaning changes because the old meaning was wrong. (G022: needs a second reader.)
- [ ] Breaking — an identifier's meaning changes or an identifier is removed. (G023: deprecate, don't delete.)

## The change

What identifier(s), document(s), or files are affected.

## The reason

Why this is correct or needed — not just that it is. (A corrective or additive PR without this is a preference, not a proposal — CONTRIBUTING.md, "How to open a pull request".)

## Migration

Required only if you checked **Breaking** above. What dependents need to do, and when the old identifier is removed once nothing cites it (G023). Leave this section out entirely for additive or corrective changes.

## Ownership ambiguity (if any)

If more than one document could defensibly own the fact this PR touches, say so here rather than resolving it silently — let review settle it.

## Second reader

If this is a **corrective** change, name who's confirming the correction, per CONTRIBUTING.md ("Corrective" — G022). For an external PR this can be left to the maintainer, who serves as second reader by default (CONTRIBUTING.md, "Review").

## Before opening

- [ ] `cd tooling && python3 validate.py` passes
- [ ] `vale --config=tooling/vale/.vale.ini docs/` passes
- [ ] If this adds or retires an ID, the regenerated `tooling/registry.yaml` is committed alongside it
