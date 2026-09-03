```yaml
document: Governance
version: 1.0.0
tier: none — orthogonal to the stack by design
owns:
  - who owns each document
  - how a document changes
  - how disagreement is resolved
  - when something is retired
exports: G001–G094
depends: []
cites_no_ids: true
reviewed: 2026-09-03
```

# Governance

How the suite changes, who may change it, and when it should stop existing.

**This document names no identifier from any other document.** It describes process, not content. If a rule here needed to know a specific family, constraint, or check, the rule would be content wearing a process costume, and it would belong in the document that owns the subject.

---

# PART I — PURPOSE

## G001 · Governance exists to make change cheap

Not to prevent change, not to approve it, not to record who authorized it. A suite of documents nobody can update becomes wrong slowly and then all at once, and the wrongness is invisible because the documents still exist and still look authoritative.

Every rule below is judged against one question: does it make a correct change faster or slower?

## G002 · The small-change test

**How long does it take a competent person to correct a typo, add a missing entry, or fix a wrong citation?**

If the answer is more than a few minutes of their own time, governance has failed regardless of how principled it looks. This is the single diagnostic for whether the rest of this document is working, and it should be re-asked whenever a rule is added here.

## G003 · What this is not

Not sign-off. Not a change advisory board. Not a record of permission. Approval processes protect against a failure mode — unauthorized change — that is far rarer in practice than the failure mode they cause, which is nobody changing anything.

---

# PART II — OWNERSHIP

## G010 · One named owner per document

A person, not a team, not a role title. The owner is answerable for the document being correct and current. Ownership can transfer; it cannot be shared, because shared ownership resolves to nobody noticing.

## G011 · Committees own nothing

A committee may advise, review, or object. It may not be the answer to "who owns this," because the answer needs a name that can be asked a question.

## G012 · The owner's four obligations

1. Keep the document internally correct.
2. Run its scheduled reviews and record the result.
3. Respond to proposals within the limit in Part IV.
4. Hand over deliberately, per the next entry.

Nothing else. An owner is not required to write every change, approve every change, or be consulted on every use.

## G013 · Continuity

Every document names a second person who can take it over. Not a co-owner — a successor. The test is whether the suite survives one person leaving, and it is worth running as a thought experiment annually: if the owner vanished today, who would notice, and how long until anyone did?

**A document whose owner has left and not been replaced is unowned**, whatever the file says, and unowned documents rot at a predictable rate.

## G014 · An unowned check is a failure, not a gap

Several documents specify periodic checks that block nothing. Those checks exist only if a named person runs them and writes down what happened. A check with no owner should be deleted from the document that specifies it rather than left as an aspiration, because an aspirational check makes the suite look more rigorous than it is — which is worse than not having it.

---

# PART III — CHANGE

## G020 · Three kinds of change

**Additive** — new entries, new sections, new documents. Nothing existing changes meaning.
**Corrective** — an error is fixed. Meaning changes because the old meaning was wrong.
**Breaking** — an identifier's meaning changes or an identifier is removed. Things that cite it may now be wrong.

The kinds have different costs and must have different processes, or the cheap ones inherit the expensive one's friction.

## G021 · Additive change passes without a gate

Write it, version it, publish it. No review required. Additive change cannot break a dependent, which is the entire reason the identifier rules exist.

## G022 · Corrective change takes one reader

Someone other than the author confirms the correction is correct. That is the whole process. Corrections are the most common change and the most valuable, and any process heavier than this suppresses them.

## G023 · Breaking change is coordinated, and slow on purpose

1. Mark the identifier deprecated, naming its successor. Do not remove it.
2. Publish. Dependents are now on notice and nothing has broken.
3. Dependents migrate on their own schedule.
4. Remove only when nothing cites it.

The slowness is the feature. Step 1 costs nothing and buys unlimited time, which is why deprecation exists and why deleting first is the one genuinely destructive act available in this suite.

## G024 · Anyone may propose; the owner decides; nobody may silently overrule

An owner declining a proposal is a normal outcome and must be recorded, per Part IV. An owner ignoring a proposal is not a decision, and Part IV puts a clock on it.

## G025 · The review that actually matters

Mechanical validation catches structural error and catches it completely. What it cannot catch is a citation that resolves but points at the wrong thing — the sentence is well-formed, the identifier exists, and the meaning is wrong.

**Every changed or added citation gets a second reader.** This is the only mandatory human review in this document, and it is mandatory because it is the one defect that accumulates silently and compounds.

---

# PART IV — CONTRIBUTION

## G030 · How to propose

Open a change against the document. Not a discussion, not a meeting request — a proposed edit, because a proposal that has to be transcribed by someone else usually is not.

## G031 · What a proposal contains

The change, the reason, and — if it is breaking — the migration for anything that cites the affected identifier. Three things. A proposal missing the third is not ready; a proposal missing the second is a preference.

## G032 · Rejection is recorded

A declined proposal is written down with its reason, in the document it targeted. Otherwise the same proposal returns every eight months and is re-argued from zero by people who have no way of knowing it was already settled.

## G033 · Two weeks, then it is the owner's problem

An open proposal with no response after two weeks escalates to the successor named under continuity. This exists because the most common failure of a contribution process is not rejection; it is silence, and silence teaches people to stop proposing.

---

# PART V — RETIREMENT

## G040 · Deprecate, never delete

Applies to identifiers, sections, and whole documents. A deleted thing takes its history with it and breaks every reference silently. A deprecated thing keeps resolving and explains where its meaning went.

## G041 · A deprecation carries a successor and a date

"Deprecated" alone is a dead end. Deprecated *in favor of* something, from a stated date, is a migration. If there is no successor, say so explicitly and give the reason — that is a legitimate outcome and a different one from having forgotten.

## G042 · Retiring a document

A document is retired when its question is no longer asked, its content has moved, or it has been wrong long enough that correcting it costs more than rewriting. Mark it superseded, name what replaced it, leave it readable. Do not remove it from the roster — a roster that hides retired documents cannot answer why something disappeared.

## G043 · Sunsetting the suite

Worth stating because nobody states it. The suite should be wound down when any of these is true for more than two review cycles:

- Nobody consults it before making a decision.
- Its scheduled reviews are not being run.
- The product it describes has changed enough that reads of it are misleading.
- Maintaining it costs more attention than the decisions it improves.

**A dead suite that still exists is worse than no suite**, because people cite it, trust it, and inherit its errors. Winding down deliberately — marking it superseded, dating it, saying what replaced it — is a legitimate and underused end state.

---

# PART VI — REALITY

## G050 · Documents describe practice or they are fiction

The suite has authority only insofar as it matches what is actually done. A rule everyone routes around is not a rule; it is a note about someone's preferences from an earlier year.

## G051 · Correction runs both ways

The obvious direction is documents correcting practice. The direction that is almost always missing is **practice correcting documents.**

When observed practice diverges from a document, the first question is not *how do we get compliance* but *which one is right*. Frequently the practice is right and the document has aged. A governance model with only one arrow produces a suite that is simultaneously authoritative and ignored.

## G052 · Divergence is a signal before it is a violation

Investigate before enforcing. A single team departing from a rule is probably an exception. Several teams departing from the same rule independently is evidence the rule is wrong, and treating it as a compliance problem destroys the information.

## G053 · The lapsed-check rule

When a scheduled check has not been run for two consecutive periods, do not reschedule it. Ask whether it should exist. A check nobody runs is telling you something about its value, and the honest responses are to give it an owner who will actually run it, reduce its frequency to one that will hold, or delete it.

---

# PART VII — CONFLICT

## G060 · Resolution order

When two documents disagree, **the one lower in the dependency stack wins.** This is not a convention; it follows from the architecture. The higher document depends on the lower, so if they disagree, the higher one has drifted from something it is built on.

## G061 · Reality outranks every document

If a document and an observed fact disagree, the fact wins and the document is corrected the same day. This ranks above the dependency order, and it is the only rule in this document with no exception.

## G062 · When the order does not resolve it

Two documents at the same level disagreeing means a boundary is drawn wrong — the same fact has two homes, which the architecture forbids. The resolution is not to pick a winner but to redraw the boundary so the fact has one owner. Escalate to both owners jointly; if they cannot agree where the fact lives, the disagreement is about scope and belongs here rather than in either document.

---

# PART VIII — CADENCE

## G070 · One calendar, not one per document

Every periodic obligation across the suite appears in a single calendar with its owner and frequency. Scattered across documents, periodic work is invisible in aggregate and nobody can see that it sums to more time than anyone has.

## G071 · Most of it blocks nothing, and must therefore be reported

Anything that can fail a build needs no cadence discussion. Everything else — the periodic reviews, the manual checks, the volatility rechecks — needs a named owner and a written result, because work that blocks nothing and reports to nobody does not happen.

## G072 · A missed period is recorded as missed

Not silently rolled forward. Three consecutive misses triggers G053 rather than a fourth reminder.

---

# PART IX — SCALE

## G080 · The adoption gradient

Not all of this is worth it at every size. The mistake in both directions is common: a solo practitioner implementing full deprecation windows, and a forty-person organization operating on shared understanding.

## G081 · One person

Keep: ownership is implicit, dependency direction, identifier stability, the small-change test, the sunset criteria.
Skip: deprecation windows — deprecate and migrate in the same sitting. Proposal clocks. Second-reader review, replaced by re-reading changed citations after a day's gap.

## G082 · A small team

Add: named owners, second-reader review on citations, the single calendar, recorded rejections.
Still skip: formal proposal process. A conversation and an edit is sufficient at this size.

## G083 · An organization

Add: everything. Successors, proposal clocks, coordinated breaking changes, the full cadence calendar with reporting.

## G084 · What never scales away

Four things hold at every size, and each of them fails silently rather than loudly:

- Identifier stability. The cheapest thing here and the most expensive to retrofit.
- Dependency direction. One cycle and the suite becomes unchangeable in one place.
- Citation correctness review. The defect that compounds.
- The sunset criteria. Nobody notices a suite dying from inside it.

---

# PART X — FAILURE MODES

## G090 · Governance theater
Process that produces artifacts of control rather than correct documents. Detection: apply the small-change test. If it has degraded since the last time it was asked, something was added here that should not have been.

## G091 · The fossilized suite
Every rule is followed, nothing has changed in a year, and the product has. Usually caused by change being expensive enough that people work around the documents instead of updating them. Detection: count corrective changes. Zero is not stability.

## G092 · The abandoned suite
Owners gone, reviews lapsed, documents still cited. The most damaging state because the documents retain authority they no longer deserve. This is what the sunset criteria exist to catch, and they only work if someone is running them.

## G093 · The single point of understanding
One person can explain why the suite is shaped as it is. When they leave, the documents remain and the reasoning does not, so subsequent changes are locally plausible and globally wrong. Mitigated by the settled-decisions sections in each document, which exist precisely to survive the person who settled them.

## G094 · Scope creep in the documents
Documents accumulating content they do not own, usually because a fact was easier to write where it was needed than to place where it belongs. Slow, cumulative, and it dissolves the boundaries that make independent change possible. Detection is the periodic ownership audit, and the fix is always to move the fact rather than to duplicate it.

---

# EXPORT INDEX

| ID | Entry |
|---|---|
| G001 | Governance exists to make change cheap |
| G002 | The small-change test |
| G003 | What this is not |
| G010 | One named owner per document |
| G011 | Committees own nothing |
| G012 | The owner's four obligations |
| G013 | Continuity |
| G014 | An unowned check is a failure |
| G020 | Three kinds of change |
| G021 | Additive change passes without a gate |
| G022 | Corrective change takes one reader |
| G023 | Breaking change is coordinated |
| G024 | Anyone may propose; the owner decides |
| G025 | The review that actually matters |
| G030 | How to propose |
| G031 | What a proposal contains |
| G032 | Rejection is recorded |
| G033 | Two weeks, then escalation |
| G040 | Deprecate, never delete |
| G041 | A deprecation carries a successor and a date |
| G042 | Retiring a document |
| G043 | Sunsetting the suite |
| G050 | Documents describe practice or they are fiction |
| G051 | Correction runs both ways |
| G052 | Divergence is a signal before it is a violation |
| G053 | The lapsed-check rule |
| G060 | Resolution order |
| G061 | Reality outranks every document |
| G062 | When the order does not resolve it |
| G070 | One calendar |
| G071 | Most of it blocks nothing, and must be reported |
| G072 | A missed period is recorded |
| G080 | The adoption gradient |
| G081 | One person |
| G082 | A small team |
| G083 | An organization |
| G084 | What never scales away |
| G090 | Governance theater |
| G091 | The fossilized suite |
| G092 | The abandoned suite |
| G093 | The single point of understanding |
| G094 | Scope creep in the documents |

---

## Settled decisions

**Governance cites no identifiers, and this is enforced rather than intended.** The front matter declares it and the validator checks it. A single content citation here would make every other document a dependency of the process document, which inverts the architecture and makes the process unchangeable without touching everything.

**Change is stratified into three kinds with three costs.** A single change process prices additive change — the safest and most common kind — at the cost of breaking change, which is how document suites stop accumulating corrections and start accumulating workarounds.

**Correction is explicitly bidirectional.** Most governance models only carry authority downward, from document to practice, which produces suites that are formally authoritative and actually ignored. Stating that practice may correct the document is what keeps the suite alive, and treating repeated divergence as evidence rather than violation is what makes that real.

**Sunset criteria are stated, which is unusual and deliberate.** Nearly every governance document assumes perpetuity. A suite that outlives its usefulness keeps being cited, and its errors get inherited by people who had no way to know it went stale. Naming the conditions for winding it down is the difference between a document set that ends deliberately and one that decays.

**The adoption gradient exists so the suite is usable by one person.** Everything here scales down except four things, and G084 names them because they are the four that fail silently — which means at small scale they are the only ones worth keeping and the easiest ones to skip.
