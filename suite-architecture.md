# Suite Architecture

**Document 0.** The contract that lets the other documents change without breaking each other.

This is the same problem as decoupling a design system from brand and content, applied one level up. The failure modes are identical: a reference that breaks when something is renumbered, a fact stated in two places that drifts, and a dependency cycle where nothing can move without everything moving.

---

## 1. The dependency rule

One rule, and it does most of the work:

> **A document may cite downward. Never upward. Never sideways.**

Tiers, most stable at the bottom:

```
Tier 3   Verification · Diagnosis          evaluative
Tier 2   Decision · Implementation          operational
Tier 1   Anatomy · Composition              structural
Tier 0   Vocabulary · Constraints           foundational

Orthogonal   Governance                     process, cites no content
```

**Tier 0 depends on nothing.** Terms and floors are true regardless of how you organize choices. They must be independently readable.

**Governance is deliberately outside.** It describes how change happens, not what changes. If Governance needs to know a family ID, something is wrong in Governance.

**Sideways is banned even when tempting.** Decision and Implementation are both Tier 2 and will feel like they need each other. They don't: Decision says "set F15 to compact," Implementation says "compact is a 0.75 spacing multiplier." Neither needs to name the other.

**The test for a cycle:** if changing document A requires changing document B, and changing B requires changing A, one of them is holding a fact it doesn't own.

---

## 2. Ownership — one fact, one home

Every kind of statement has exactly one owning document. Others reference; they never restate.

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

**Boundary test.** Take any sentence in any document and ask which owner it belongs to. If more than one answer is defensible, you've found a boundary bug — the sentence is in the wrong place, or the boundary needs redrawing.

**The most common violation** will be Constraints and Composition. A contrast threshold is a Constraints fact; a family's range being *bounded by* that threshold is a Composition fact. Composition may say "bounded below by C012." It may not say "4.5:1."

---

## 3. Stable identifiers

Everything citable gets an ID. The rules matter more than the scheme.

| Namespace | Owner | Example |
|---|---|---|
| `V-###` | Vocabulary | `V-005` information architecture |
| `A-###` | Anatomy | `A-010` lightness vs luminance vs brightness |
| `F##` / `F##.#` | Composition | `F15`, `F15.2` |
| `C###` | Constraints | `C012` contrast is a luminance relationship |
| `D###` | Decision | `D007` Round 5 — the emphasis triangle |
| `T###` / `K###` | Implementation | `T004` type annotation, `K004` focus containment for overlays |
| `X###` | Verification | `X010` state matrix coverage |
| `R###` | Diagnosis | `R012` observed |
| `G###` | Governance | `G010` one named owner per document |

**Four rules, non-negotiable:**

1. **Assigned once.** An ID is bound to a meaning permanently.
2. **Never reused.** A retired ID stays retired. Reuse is worse than a gap.
3. **Never reordered.** ID order and display order are separate concerns. Sorting is a rendering decision.
4. **Additive by default.** New things get new IDs at the end. Nothing renumbers to make room.

This is the same lesson as spacing tokens: index-based naming doesn't survive insertion, so don't let position carry meaning.

**Splitting.** When a family splits, the old ID retires and points at its successors. `F43 → superseded by F43a, F43b`. Citations to F43 still resolve, to a note explaining where it went.

**Merging.** The surviving ID keeps its number; the absorbed ID retires pointing at it.

**Renaming.** Free. The name is not the identifier. Rename anything you like as long as the ID holds.

---

## 4. Reference discipline

**Cite by ID, never by content.** `See C012` is durable. `See the 4.5:1 contrast requirement` breaks silently when the requirement changes.

**Never copy a value across documents.** If a number appears in two files, it will diverge, and you will not notice which one is stale.

**Never quote another document's prose.** Quoting freezes a version. Cite the ID and let the reader resolve it against the current text.

**Cite the smallest unit that carries the meaning.** `F15.2` not `Plane 4`.

**No transitive citation.** If Verification needs a Constraints fact, it cites Constraints directly. It does not cite Composition's citation of Constraints.

---

## 5. Export surface

Each document has a public surface and an interior, exactly like a component API.

**Exported — others may cite, changes are breaking**
- IDs
- The one-line meaning attached to each ID
- The range or type of each entry

**Internal — others may not cite, changes are free**
- All prose, rationale, and explanation
- Examples
- Ordering and grouping
- Section headings
- The registers / moves-with / independence markers in Composition

The practical consequence: you can rewrite an entire document's prose without a version bump, provided every ID still means what it meant.

---

## 6. Versioning

Semantic versioning per document, independently.

**Major** — an ID was retired, or its meaning changed. Breaks citations. Requires a coordinated pass over dependents.
**Minor** — IDs added. Additive; safe. Dependents may adopt whenever.
**Patch** — prose, examples, corrections. Invisible to dependents.

**References pin the major only.** `depends: Composition ^2` means "any 2.x." Pinning minors creates the coordination problem you're trying to avoid.

**Change protocol for a major:**
1. Mark the ID deprecated, with a successor. Do not remove it.
2. Bump minor, publish, notify dependents.
3. Dependents migrate at their own pace.
4. Remove only after all dependents have moved — this is the major bump.

Deprecation is the whole mechanism. If you delete first and coordinate second, you've coupled the documents again.

---

## 7. The registry

The one shared artifact. Everything else is prose.

```yaml
- id: F15
  owner: composition
  name: Density
  meaning: How much is present per unit of space
  type: dial
  status: active
  since: 2.0

- id: C012
  owner: constraints
  name: Body text contrast floor
  meaning: Minimum luminance ratio for body-size text
  type: floor
  status: active
  since: 1.0

- id: F43
  owner: composition
  name: Speed
  status: superseded
  superseded_by: [F43a, F43b]
  since: 2.0
  until: 3.0
```

Small enough to hand-maintain, structured enough to validate against. The single check worth automating: **every cited ID resolves to an active or superseded entry.** That one test catches nearly every coupling failure before a reader does.

**The registry is generated, not authored.** An earlier version of this section proposed folding it into Vocabulary. That was wrong: the registry indexes F, C, and D IDs, so a Vocabulary that contained it would reference upward and break the rule in §1. The registry has no tier because nobody writes it — it is derived mechanically from the export index of each document, which also means it cannot drift from them. Vocabulary stays a Tier 0 document owning term meanings, and appears in the registry alongside everyone else.

---

## 8. Front matter

Every document opens with this block. Six lines, and they make the graph inspectable.

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

If `depends` ever lists a document at the same tier or higher, the rule in §1 has been broken and the suite has a cycle.

---

## 9. Migrating what exists

**Composition v2** — already ID'd F01–F68. Closest to compliant. Needs: front matter, and its inline constraint values (contrast, target sizes, the 100ms figure) extracted into Constraints and replaced with citations.

**Anatomy** — no IDs. Needs `A-###` assigned across Volume 1 before Volume 2 is written, or the numbering will have to be retrofitted across a larger surface.

**Vocabulary** — no IDs, and currently written as a peer document. Two changes: assign `V-###`, and reposition it as the registry rather than another reference to read.

**Everything unbuilt** — start with front matter and IDs from the first draft. The cost of adding them later scales with what's already been written, which is exactly the retrofit trap named in Composition Part III.

---

## 10. What this costs, honestly

Not all of this is worth it at every scale.

**Always worth it, cheap:**
- The dependency rule (§1). One sentence, prevents the worst failure.
- Ownership map (§2). One table, resolves most "where does this go" questions.
- Stable IDs (§3). Free if done from the start, expensive later.
- No restatement (§4). A habit, not machinery.

**Worth it once more than one person writes or reads these:**
- Export surface (§5)
- Versioning (§6)
- Front matter (§8)

**Worth it once the suite is large enough to lose track of:**
- The registry as a file (§7)
- Automated citation validation

**Over-engineering for a solo effort:**
- Formal deprecation windows. If you own every document, deprecate and migrate in the same sitting.
- Pinned versions. Useful when dependents update on different schedules; noise when they don't.

The honest floor: dependency direction, ownership, and stable IDs. Those three alone get most of the independence. The rest is insurance whose premium scales with how many people are involved.
