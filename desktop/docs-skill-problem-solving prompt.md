# Investigate and Architect the Remedy

Use the attached **Docs-Skills Problem Inventory — 2026-09-21** as the primary statement of the problems we need to address.

The purpose of this session is **not to implement a solution**. It is to investigate and design a practical architectural remedy that we can review before implementation.

## The central objective

We need to resolve the problems identified in the problem inventory affecting:

- `mb-docs-manager`
- `mb-align-docs`
- `mb-wikilinks`
- their shared operating model
- their interaction with Cupcake

However, there is an important constraint:

> **Do not turn this into a mammoth redesign project.**

We need a solution that is comprehensive enough to address the important problems identified in the investigation, but sufficiently focused and achievable that an AI can realistically design and subsequently implement it.

Use the problem inventory to establish the **boundary of the work**. Do not expand the scope simply because a more ambitious redesign might be theoretically desirable.

## 1. Start from the problems, not from a predetermined solution

First, identify which of the documented problems and root causes actually need to be addressed by the architectural remedy.

Pay particular attention to the root causes identified as RC1–RC6:

- static-corpus assumptions versus a corpus in deliberate flux;
- governance being too distant from the point of failure;
- lack of canonical implementation;
- lack of version/supersession discipline;
- excessive execution ceremony;
- mismatch between Cupcake enforcement and documentation workflows.

Do not assume that every individual symptom requires a separate architectural solution.

Look for changes that solve **multiple related problems at once**.

Conversely, do not redesign a component merely because it appears in the problem inventory if the problem can be resolved more simply.

## 2. Investigate the three-skill architecture

One hypothesis I want us to investigate is whether the three separate skills should become a **single sequential documentation-management workflow**.

Conceptually, this might be:

**MB Docs Manager → MB Align Docs → MB Wikilinks**

The three capabilities could still remain logically distinct, but their execution might be orchestrated as one controlled workflow rather than three independently operating skills.

This is a **hypothesis, not a decision**.

Determine whether this architecture would actually address important problems in the inventory, particularly:

- inconsistent state between skills;
- duplicated run ceremony;
- excessive run duration;
- independent assumptions about corpus state;
- implementation drift;
- inconsistent governance;
- problems caused by running the skills independently over portions of a corpus.

Also determine which problems this architecture **would not** solve.

Do not combine the skills merely for the sake of combining them.

## 3. Keep the architecture proportionate

A key design objective is:

> **Solve the identified problems with the least unnecessary architectural complexity.**

For every significant proposed architectural change, ask:

- Which documented problem does this solve?
- Is it solving a root cause or merely a symptom?
- Could the same problem be solved more simply?
- Does this change introduce new complexity?
- Does it create a new dependency that we do not need?
- Is the change necessary for the eventual solution, or merely desirable?

Avoid designing an elaborate framework, orchestration platform, generalized pipeline, or new infrastructure unless the evidence shows that it is actually required.

The eventual implementation must remain realistically achievable by an AI working within the available environment.

## 4. Corpus scope and sequencing

Investigate what the correct execution scope should be.

The current skills generally operate independently and may work across different corpus areas. Determine whether the new architecture should:

- operate over a defined corpus sequentially;
- operate over smaller controlled corpus units;
- support both modes;
- or use another approach.

Do not assume that "one large corpus" is inherently correct.

The important question is:

> **What is the smallest scope over which the documentation-management operations need to be coordinated in order to produce a consistent result?**

Likewise, establish whether the logical sequence really is:

**Docs Manager → Align Docs → Wikilinks**

or whether another sequence, iteration, or validation point is required.

## 5. Cupcake must remain protective

Cupcake exists to protect the corpus against classes of errors that AI can introduce during normal work.

That intent must remain intact.

The goal is therefore **not** to weaken Cupcake until the documentation skills can operate.

Instead, investigate the smallest changes necessary to allow legitimate documentation-management operations to coexist with Cupcake's protections.

Use the documented Cupcake problems in the inventory as the starting point, particularly:

- commit/approval conflicts;
- bulk-write handling;
- grant/slip handling;
- the missing wikilinks handover mechanism;
- enforcement-state awareness;
- folder-scope gaps;
- the distinction between authored rules and compiled enforcement.

Where possible, prefer an architecture in which the documentation workflow naturally operates within Cupcake's intended safety boundaries.

Do not redesign Cupcake generally. Only investigate changes that are directly necessary to resolve the documented documentation-skill conflicts.

## 6. Close only the information gaps that matter

The problem inventory identifies several remaining uncertainties.

Before making architectural conclusions, determine whether any of those gaps are **material to the architecture**.

If an information gap does not affect the architectural decision, do not expand the investigation merely to eliminate uncertainty.

Where a gap does matter, investigate it.

The objective is not perfect knowledge of the entire system. It is sufficient understanding to design a sound, bounded remedy.

## 7. Produce an architecture for review

At the end of the investigation, produce:

### A. Problems being addressed

A concise mapping from the problem inventory to the problems the proposed architecture is intended to solve.

### B. Proposed architecture

Describe the proposed operating model for the three documentation capabilities and Cupcake.

Show:

- the major components;
- their responsibilities;
- their execution sequence;
- corpus scope;
- validation points;
- interaction with Cupcake.

### C. What remains separate

Explicitly identify functionality that should **not** be combined or redesigned.

### D. Problem-to-solution mapping

For each major proposed change, identify which documented problems/root causes it addresses.

### E. Problems deliberately left out

Identify inventory items that do not need to be solved as part of this architectural change, and explain why.

This is important for preventing scope creep.

### F. Implementation boundaries

Describe what would eventually need to change in:

- the three skills;
- shared documentation/run-discipline material;
- Cupcake rules;
- supporting files or procedures.

Do not implement those changes yet.

### G. Open questions

Identify only the questions that must be answered before implementation.

### H. Review recommendation

End with a concise proposal for what we should review and agree upon before moving to implementation.

## Most important constraint

Do not attempt to solve everything.

The goal of this session is to find a **small, coherent, implementable architecture that addresses the important problems documented in the investigation**.

If several problems can be eliminated by one well-chosen architectural change, prefer that over creating separate mechanisms for each problem.

Architectural changes are required to solve the problems. Every problem needs to be solved, prefer simplicity rather than expanding the project.

**No implementation, rewriting, deployment, or modification of the skills or Cupcake rules should take place in this session.**

The deliverable is a **bounded architecture proposal for review**.

Credo: Simple, secure, robust, fit for purpose
