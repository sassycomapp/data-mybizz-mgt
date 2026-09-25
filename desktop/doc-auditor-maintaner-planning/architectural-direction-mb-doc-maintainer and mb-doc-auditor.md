---
title: "architectural-direction-mb-doc-maintainer and mb-doc-auditor"
doc-id: "architectural-direction-mb-doc-maintainer and mb-doc-auditor"
---
# Architectural Direction: mb-doc-maintainer and mb-doc-auditor

I want to establish a new documentation-maintenance architecture.

Before making any changes, read this entire brief carefully.

The most important instruction is:

> **Do not modify, dismantle, migrate, refactor, retire, or otherwise alter the existing DocCycle skill as part of this work.**

DocCycle is explicitly **out of scope**.

It may remain exactly as it is. It may sit unused. It may potentially be useful in the future.

The task now is to create two new, clearly bounded skills:

- `mb-doc-maintainer`

- `mb-doc-auditor`

The purpose of this brief is to explain **why** they are being created, what each one is responsible for, and—equally importantly—what they are NOT responsible for.

---

# 1. The problem we are correcting

The existing DocCycle has become too large and too demanding.

It is capable of finding enormous numbers of conditions, inconsistencies and potential issues across the corpus.

The problem is that this detection capability has gradually turned into a **work-generation system**.

In practice, the process becomes:

> detect → classify → report → ask for approval → modify → rescan → discover more → ask for more approval → modify → rescan again

The result is that DocCycle itself becomes something that requires substantial human attention and maintenance.

This is the opposite of what we want.

The purpose of documentation maintenance is to support **G-brain**.

The developer should not have to become the operator, approval engine, or human checksum for a documentation-maintenance system.

The fundamental principle is therefore:

> **DocCycle has been trying to maintain too many properties of the corpus. The new architecture will maintain only the invariants that G-brain actually depends upon.**

---

# 2. The fundamental objective

The objective is NOT:

> Make the existing maintenance process faster.

The objective is:

> **Make the maintenance system do substantially less work by limiting it to work that actually matters.**

Neither new skill should attempt to make the documentation corpus perfect.

The objective is to keep documentation:

- trustworthy;

- coherent;

- correctly structured;

- correctly linked;

- usable by G-brain.

Nothing more unless there is a demonstrable reason.

The governing principle is:

> **Neither skill exists to maintain every measurable property of the documentation. Both exist to preserve the invariants on which G-brain depends.**

---

# 3. The new architecture

The architecture is deliberately split into two different responsibilities.

## mb-doc-maintainer

**Protects what is currently being built.**

It is the continuous, event-driven or development-coupled maintenance mechanism.

It reacts to current canonical events such as:

- a document being created;

- a document being modified;

- a document being moved;

- a document being renamed;

- a document being deleted;

- a link being created;

- a link being changed;

- a link being removed.

Its question is:

> **"What just changed, and what does that change require to keep the affected documentation healthy for G-brain?"**

It should work locally and incrementally.

It should not routinely scan the entire corpus.

---

## mb-doc-auditor

**Periodically checks the wider estate.**

It is the deep-maintenance and corpus-integrity mechanism.

It runs on demand .

Its question is:

> **"Is this corpus, as a whole, still sufficiently healthy and integrated to serve G-brain?"**

It can examine a much wider area than mb-doc-maintainer.

It can find accumulated problems that incremental maintenance could not reasonably detect.

But it must still distinguish between:

- something that is detectable;

- something that is genuinely wrong;

- something that actually matters to G-brain;

- and something that requires action.

It must NOT become a large bureaucratic report generator.

---

# 4. The existing DocCycle

This distinction is critical.

## DO NOT turn DocCycle into one of the new skills.

Do not:

- refactor DocCycle;

- simplify DocCycle;

- migrate DocCycle;

- split DocCycle;

- delete DocCycle;

- rename DocCycle;

- modify its specifications;

- change its implementation;

- move its functionality into the new skills;

- attempt to make it compatible with the new architecture;

- or perform a "cleanup" of DocCycle while creating these skills.

None of that is required now.

**Leave DocCycle alone.**

The fact that DocCycle exists does not create a requirement to do anything with it.

It can simply remain dormant.

Its future can be decided later, independently of this work.

The immediate task is solely to establish the two new skills correctly.

---

# 5. Why we need two skills

The distinction is important because current development and deep corpus maintenance are fundamentally different problems.

### Current development

Something has just changed.

We know approximately what changed.

We know where it changed.

We want to protect the affected documentation immediately.

That is **mb-doc-maintainer**.

### Deep maintenance

We want to examine the wider corpus.

We are looking for problems that may have accumulated or escaped incremental maintenance.

That is **mb-doc-auditor**.

Do not collapse these into one system.

---

# 6. mb-doc-maintainer — required behaviour

The maintainer should ensure that documents created or changed during development remain usable by G-brain.

At minimum, it should deal with:

### New documents

- required front matter;

- mechanically determinable metadata;

- relevant document references;

- conversion of appropriate references into WikiLinks;

- verification that targets exist.

### Modified documents

- relevant new or changed references;

- front matter integrity;

- relevant WikiLinks;

- affected relationships.

### Moved or renamed documents

- affected references;

- mechanically determinable link updates;

- verification of the new relationship.

### Deleted documents

- directly affected references;

- genuinely broken relationships;

- human intervention where the correct replacement cannot be determined.

The maintainer should work from the event and its affected area.

It should not use an ordinary development event as an excuse to scan the entire corpus.

---

# 7. mb-doc-auditor — required behaviour

The auditor should periodically establish the health of a wider corpus.

It may examine:

- broken WikiLinks;

- stale references;

- missing or malformed front matter;

- orphaned documents;

- accumulated structural inconsistencies;

- relationships that incremental maintenance could not reasonably detect;

- cross-document or cross-corpus integrity;

- G-brain ingestion/retrieval prerequisites.

However:

> **Deep audit does not mean "find absolutely everything that differs from an ideal state."**

The auditor must always ask:

> **Does this condition materially affect G-brain?**

If not, it should not automatically become work.

---

# 8. The golden rule

This rule applies to BOTH skills:

# Detection is not a work queue.

A detection does not automatically mean:

> "Fix this."

Every finding must effectively fall into one of four categories:

### 1. MUST FIX

It affects an important G-brain invariant.

### 2. CAN WAIT

It is legitimate maintenance debt but does not currently affect useful operation.

### 3. DOESN'T MATTER

It has no meaningful effect on G-brain.

### 4. REQUIRES HUMAN JUDGEMENT

The system cannot safely determine the correct action.

Most detections should never become a human task.

---

# 9. Automation boundary

An operation should be automatic when:

- the affected object is known;

- the intended result is mechanically determinable;

- the operation is safe and reversible/recoverable;

- the result can be independently verified.

Examples include:

- adding required front matter;

- mechanically derived front-matter corrections;

- converting an unambiguous reference into a WikiLink;

- updating references after a mechanically verified rename;

- repairing an unambiguous broken reference.

Human intervention is appropriate when:

- semantic intent is ambiguous;

- there are multiple plausible targets;

- a rename/move has competing interpretations;

- a destructive action is proposed;

- a policy decision is required.

Human questions should be extremely concise.

For example:

> **X appears to have become Y.**  
> Proposed action: rename X to Y and update four references.  
> Risk: Low.  
> **Approve / Reject**

Do not produce a 100-item report where one decision would suffice.

---

# 10. Human attention is a constrained resource

The new architecture must explicitly treat human attention as scarce.

I am not the operator of the maintenance system.

I am not its approval engine.

I am not its human checksum.

I am the developer of the actual system.

The system should therefore bring me only things that genuinely require my judgement.

My attention should remain focused on:

- development;

- architecture;

- design;

- decisions that actually require human judgement.

Not routine documentation housekeeping.

---

# 11. The common processing principle

Both skills may use compatible mechanisms and tooling where useful.

The underlying logic is:

> **Identify → determine affected invariants → repair → verify → finish**

But their scope must remain different.

### mb-doc-maintainer

> **Current event → affected area → affected invariants → repair → verify → finish**

### mb-doc-auditor

> **Wider corpus → potential integrity problems → determine what actually matters → repair → verify → finish**

Do not turn the shared principle into a shared monolithic implementation unless that is technically useful.

Shared infrastructure is fine.

Shared responsibility is not.

---

# 12. Definition of success

## mb-doc-maintainer

Success means:

> **The documentation affected by current development has been returned to a healthy state for G-brain.**

In practical terms:

- required front matter is present;

- relevant links resolve;

- appropriate references are WikiLinks;

- affected relationships are intact;

- no important integrity issue introduced by the current event remains unresolved.

Then:

**DONE.**

It does not need to establish that the entire corpus is perfect.

---

## mb-doc-auditor

Success means:

> **The wider corpus has been examined sufficiently to establish that it is healthy for G-brain.**

It does not mean:

> "There are no detectable differences anywhere."

A corpus can be healthy while containing:

- deferred housekeeping;

- harmless inconsistencies;

- non-critical stale information;

- conditions that can safely wait.

The auditor must have a meaningful terminal state:

> **AUDIT COMPLETE — CORPUS HEALTHY**

It must not continue generating work indefinitely.

---

# 13. What we are NOT trying to achieve

Do not design either skill around:

- perfect documentation;

- exhaustive metadata consistency;

- zero findings;

- zero differences;

- continuous full-corpus scanning;

- maximum detection;

- maximum automation for its own sake;

- maximum rule enforcement;

- maximum reporting;

- theoretical completeness.

Those are precisely the patterns that caused the original problem.

The goal is:

> **Sufficient integrity to make G-brain trustworthy and usable.**

---

# 14. No artificial runtime target

Do not design around:

> "The process must take less than 30 minutes."

Runtime matters, but it is not the primary objective.

The primary objectives are:

1. correctness;

2. bounded human involvement;

3. appropriate scope;

4. minimal unnecessary work;

5. trustworthy G-brain documentation.

If a legitimate operation takes 40 minutes, that is acceptable.

If an unnecessary operation takes 2 minutes, it is still unnecessary.

Do not optimise the wrong work.

---

# 15. The architectural relationship

The final architecture should be understood as:

```text
                    G-BRAIN
                       ▲
                       │
             ┌─────────┴─────────┐
             │                   │
             │                   │
     MB-DOC-MAINTAINER     MB-DOC-AUDITOR
             │                   │
             │                   │
     Protects current       Checks wider
        development            estate
             │                   │
             └─────────┬─────────┘
                       │
                DOCUMENTATION
```

And from the developer's perspective:

```text
You build the system
       │
       ▼
Current changes
       │
       ▼
mb-doc-maintainer
       │
       ▼
Affected documentation remains healthy
       │
       ▼
You continue building
       │
       │
       ▼
Occasionally:
mb-doc-auditor
       │
       ▼
Wider corpus checked and cleaned
       │
       ▼
You continue building
```

The intended experience is:

> **"I finished working. The system quietly brought the affected documentation into a healthy state, told me whether anything important required my attention, and got out of the way."**

That is the desired architecture.

---

# 16. The most important architectural outcome

The system must maintain this hierarchy:

### G-brain

**The thing we are supporting.**

### mb-doc-maintainer

**Protects the integrity of what is currently being built.**

### mb-doc-auditor

**Periodically checks and restores the health of the wider corpus.**

### Developer

**Builds the actual system.**

The developer must NOT become the maintainer of the maintenance system.

---

# 17. Hard boundary against architectural regression

During implementation, continually ask:

> **"Are we creating another DocCycle?"**

If the answer is yes, stop and reconsider.

Warning signs include:

- broad scans triggered by local changes;

- large reports;

- many approval requests;

- work generated from harmless differences;

- attempts to enforce every possible consistency rule;

- processes that repeatedly rescan their own output;

- maintenance becoming a prerequisite for ordinary development;

- the skill becoming a project in its own right.

These are signs that the architecture is drifting back toward the original failure mode.

---

# 18. Implementation instruction

Before making changes:

1. Inspect the existing repository and skill structure.

2. Determine where skills are currently defined and how they are invoked.

3. Identify any existing functionality that can safely be reused.

4. Do not modify DocCycle.

5. Create `mb-doc-maintainer` according to the definition above.

6. Create `mb-doc-auditor` according to the definition above.

7. Keep their responsibilities clearly separated.

8. Avoid unnecessary infrastructure.

9. Avoid introducing functionality merely because it is technically possible.

10. Keep the resulting skill specifications concise, explicit and operational.

Do not start by redesigning the entire documentation system.

Do not start by modifying DocCycle.

Do not create a new monolith.

---

# 19. Final North Star

The entire purpose of this change can be reduced to four lines:

> **mb-doc-maintainer**  
> → protects what I am currently building.
> 
> **mb-doc-auditor**  
> → periodically checks the wider estate.
> 
> **G-brain**  
> → is the reason both exist.
> 
> **Me**  
> → build the actual system rather than maintaining the maintenance system.

The existing DocCycle does not need to participate in this architecture right now.

Leave it alone.

The immediate job is simply to create these two new, bounded capabilities and ensure that neither of them recreates the work-generation behaviour that we are deliberately moving away from.

**The objective is not to make DocCycle faster.**

**The objective is to stop making unnecessary work.**

And the ultimate test for every decision is:

> **Does this preserve something that G-brain actually needs?**

If not, it probably does not belong in these skills.
