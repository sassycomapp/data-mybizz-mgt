---
title: "Improve doccycle prompt"
doc-id: "Improve doccycle prompt"
---
# Improve dock cycle prompt

I want you to conduct a rigorous architectural and operational review of **DocCycle**, with the specific objective of determining whether the current approach is fundamentally too complex, too expensive, and too labour-intensive for what it is actually intended to accomplish.

### Context

We recently amalgamated three separate skills/processes:

* Docs Manager
* Align Docs
* Wikilinks

They had been operating as somewhat disjointed processes, and they were sometimes conflicting with one another and failing to produce the correct result. The new amalgamated DocCycle skill now appears to produce the correct result, which is an important improvement.

However, there is a major problem: **performance and operational overhead**.

The previous three processes could take days to run. The new unified DocCycle is faster, but a single corpus can still take approximately **three hours** to process.

This raises the possibility that we are performing substantially more work than is actually necessary to maintain the health and integrity of the system.

### The fundamental problem

DocCycle is a support system for my canonical development work. It is not itself the primary development project.

Nevertheless, if maintaining the corpus requires a three-hour DocCycle run every time substantial development takes place, the maintenance system becomes a bottleneck for the development system.

That is not sustainable.

A further problem is that I cannot realistically read and approve everything produced by these processes. The volume of material generated is so large that I have increasingly found myself approving or agreeing to things simply to allow the process to continue, without being able to properly inspect them.

That defeats the purpose of human oversight.

There is also a communication problem: much of the generated material is written in compressed AI shorthand, fragments, or incomplete English. I have repeatedly requested full, clear English, but this has not been consistently achieved. Consequently, even when I do attempt to review the output, understanding it can require disproportionate effort.

The result is a system that may technically be doing useful work while becoming operationally self-defeating.

### What I want you to investigate

Do not simply optimise the existing DocCycle process.

First, step back and ask:

**What is DocCycle actually supposed to accomplish?**

My current hypothesis is that its core purpose is simply to maintain a **healthy, coherent, trustworthy base for G-brain** and to ensure that the relevant documentation, relationships, links, metadata, and supporting files remain sufficiently synchronised for the system to function correctly.

If that is correct, then we should design DocCycle around that outcome rather than around the assumption that every possible inconsistency must be discovered and corrected on every run.

Please test this hypothesis rather than accepting it.

### Questions I want answered

#### 1. Define the actual job of DocCycle

Determine what the minimum functional responsibilities of DocCycle really are.

Separate:

* essential functions;
* useful but non-essential functions;
* functions that could be performed less frequently;
* functions that may be redundant;
* functions that are producing diminishing returns;
* functions that exist primarily because of the architecture of the current system rather than because they are intrinsically necessary.

I want to know what DocCycle **must** do to maintain system integrity and what it merely **could** do.

#### 2. Analyse why the system takes so long

Analyse the likely causes of the three-hour runtime.

Look specifically for:

* repeated processing;
* unnecessary full-corpus scans;
* operations that could be incremental;
* operations that could be event-driven;
* operations that could be cached;
* operations that are being performed every time despite rarely changing;
* redundant validation;
* repeated discovery of the same issues;
* unnecessary regeneration;
* dependency chains that force unrelated work to run;
* operations whose cost is disproportionate to their value.

Do not assume that the current architecture is the correct architecture.

#### 3. Investigate incremental rather than exhaustive processing

Consider whether DocCycle should operate primarily on **changes rather than the entire corpus**.

For example, investigate whether the system could maintain a record of:

* new files;
* modified files;
* deleted files;
* renamed or moved files;
* changed relationships;
* changed metadata;
* changed links;
* unresolved items;
* previously validated items.

Determine whether this could allow the system to process only the affected portion of the corpus rather than repeatedly processing everything.

#### 4. Consider an event-driven or continuous architecture

I am considering whether DocCycle should cease being something that I manually execute as a large batch operation.

Instead, perhaps there should be a continuously running agent, daemon, watcher, or equivalent process that responds to relevant changes as they occur.

Evaluate this seriously.

For example:

**File changes → detect event → identify affected objects → perform only necessary maintenance → update system state → record result.**

Determine whether such an architecture is technically and operationally viable.

If it is viable, explain what it would look like.

If it is not viable, explain why and propose a better alternative.

#### 5. Consider a tiered maintenance model

Investigate whether DocCycle should be divided into different levels of maintenance, for example:

**Immediate / continuous**

* critical integrity checks;
* changed-file processing;
* broken links caused by recent changes;
* essential metadata updates.

**Periodic**

* broader consistency checks;
* relationship reconciliation;
* deeper validation.

**Occasional / scheduled**

* complete corpus audits;
* structural analysis;
* orphan detection;
* comprehensive rebuilding or reconciliation.

The purpose would be to avoid making an exhaustive audit a prerequisite for ordinary development work.

#### 6. Examine the Pareto possibility

I specifically want you to investigate whether approximately **20% of the current DocCycle work produces approximately 80% of the practical value**.

Do not assume that the Pareto principle applies.

Test the idea.

Identify which operations contribute most directly to maintaining a healthy G-brain foundation and which operations produce relatively little additional value.

If reducing the process would leave some material temporarily stale, determine whether that staleness actually matters.

The key question is:

> **What information must be current immediately, what can safely be eventually consistent, and what can simply be checked periodically?**

#### 7. Address the apparent paradox of perpetual unhealthiness

There is a conceptual problem that I want you to investigate carefully.

There is a finite number of files in the corpus. Yet every time DocCycle runs, it appears to discover additional things that were missed previously, things that are still out of sync, or things requiring further attention.

This creates the impression that we can never actually reach a stable, healthy state.

Determine why this is happening.

Is it because:

* the processes are not idempotent;
* the validation criteria keep generating new work;
* different subsystems disagree about what constitutes correctness;
* the corpus is genuinely changing;
* the process itself introduces changes;
* dependencies create cascading work;
* the system lacks a definitive source of truth;
* there is no explicit definition of "healthy";
* or something else?

A healthy system should have a meaningful **convergence condition**.

Define what "DocCycle complete" or "corpus healthy" should actually mean.

#### 8. Separate correctness from completeness

This distinction is particularly important.

Determine whether the system is currently trying to achieve **perfect completeness** when what is actually required is **functional correctness**.

For example, ask:

> Does every document need to be exhaustively analysed and perfectly synchronised before the system can be considered healthy?

Or:

> Does the system merely need to guarantee that changes which materially affect G-brain are correctly propagated?

These are very different engineering requirements.

#### 9. Reduce the human bottleneck

Design the proposed system so that I am not required to read enormous quantities of generated material.

Human intervention should occur only when:

* a genuine ambiguity exists;
* a potentially destructive action is required;
* a conflict cannot be resolved automatically;
* a significant architectural decision is required;
* or an exception requires human judgement.

Routine maintenance should be automated.

When human approval is required, the system should provide a concise explanation in **clear, complete English**, including:

1. What was found.
2. Why it matters.
3. What action is proposed.
4. What the consequences are.
5. What, if anything, I need to decide.

Do not use AI shorthand, fragments, unexplained abbreviations, or compressed technical prose.

### Most important architectural question

I want you to challenge the premise that **DocCycle should be a large process that is periodically run over the entire corpus**.

Consider whether DocCycle should instead become a **maintenance architecture** consisting of:

* change detection;
* incremental processing;
* state tracking;
* targeted reconciliation;
* continuous or event-driven maintenance;
* periodic deep audits;
* explicit health criteria;
* and exception-based human intervention.

If this is the wrong model, propose a better one.

### Deliverables

Produce the following:

#### A. Executive diagnosis

In clear, full English, explain what you believe is fundamentally wrong with the current approach.

Keep this concise.

#### B. What DocCycle actually needs to do

Define the minimum viable responsibilities of DocCycle.

#### C. Current architecture vs proposed architecture

Show the difference between the current operating model and the model you recommend.

#### D. Work classification

Classify existing DocCycle activities into:

* **Must happen immediately**
* **Can happen incrementally**
* **Can happen periodically**
* **Can happen occasionally**
* **Probably unnecessary**

Explain the reasoning for each classification.

#### E. Proposed maintenance architecture

Describe how the system could remain healthy without requiring a three-hour full-corpus run after every meaningful development session.

Include an event-driven/daemon approach if appropriate.

#### F. Definition of "healthy"

Establish concrete criteria that allow us to say:

> "The corpus is healthy enough. No further DocCycle processing is currently required."

This is essential. We must not design a system that can theoretically generate maintenance work forever.

#### G. Human interaction model

Define exactly when I should be asked to intervene and what information I should receive when I am.

#### H. Efficiency analysis

Identify the likely largest sources of wasted computation and human attention.

Prioritise them by potential impact.

#### I. Migration strategy

Explain how we could move from the current DocCycle implementation to the proposed architecture without destabilising the existing system.

Do not propose a complete rewrite unless there is a compelling reason.

#### J. Final recommendation

Give me a practical proposal for how DocCycle should operate going forward.

The recommendation should optimise for:

**Correctness + maintainability + speed + low human intervention**

rather than for theoretical perfection.

### Important constraints

Do not simply defend the existing architecture.

Do not assume that because a process currently finds problems, those problems all need to be found immediately.

Do not equate exhaustive processing with system health.

Do not optimise blindly for completeness at the expense of development velocity.

Do not produce an enormous report filled with low-value detail.

I need a **high-level architectural diagnosis followed by a practical engineering proposal**.

Most importantly, distinguish between:

> **"The system can detect this."**

and

> **"The system actually needs to detect this now."**

Those are not the same thing.

The ultimate objective is to establish a sustainable maintenance system in which G-brain remains trustworthy and sufficiently up to date **without DocCycle becoming a major development project in its own right.**
