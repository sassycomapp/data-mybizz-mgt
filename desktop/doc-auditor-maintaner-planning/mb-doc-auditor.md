---
title: "mb-doc-auditor"
doc-id: "mb-doc-auditor"
---
# mb-doc-auditor

## 1. Definition

`mb-doc-auditor` is the periodic and on-demand deep-maintenance skill for the documentation estate supporting G-brain.

Its purpose is to examine the wider documentation estate, identify accumulated integrity problems, repair problems that can be safely repaired, and establish whether the corpus satisfies the documented requirements on which G-brain depends.

It is not a continuous maintenance system and it is not a replacement for `mb-doc-maintainer`.

`mb-doc-maintainer` protects the documentation affected by current development.

`mb-doc-auditor` examines the wider estate.

---

# 2. Primary Objective

The objective of `mb-doc-auditor` is:

> **Determine whether the documentation estate is in a healthy and usable state according to the explicit requirements of G-brain, and repair identified problems where safe and appropriate.**

The auditor should perform enough work to establish meaningful corpus health.

It must not perform work merely because additional differences can be detected.

---

# 3. G-brain Requirements Must Be Explicit

`mb-doc-auditor` must **not assume what G-brain requires**.

The skill must have access to an authoritative definition of the documentation requirements that G-brain depends upon.

This should take the form of a **G-brain documentation contract**, requirements file, configuration, or equivalent authoritative source.

The exact implementation may be determined during development, but the principle is mandatory.

```text
G-brain requirements
        ↓
mb-doc-auditor
        ↓
Measure corpus against those requirements
```

The requirements may define:

* Required front matter.
* Required document properties.
* Registration requirements.
* Link requirements.
* WikiLink requirements.
* Naming and location requirements.
* Relationships required by G-brain.
* Requirements for G-brain ingestion, indexing, retrieval, or navigation.
* Any other measurable documentation invariants on which G-brain depends.

The auditor may inspect and enforce only requirements that are explicitly defined by this source or otherwise explicitly included in its operating contract.

It must not invent requirements because they appear useful, tidy, conventional, or desirable.

### Fundamental distinction

The auditor determines:

> **Does this corpus satisfy the known requirements of G-brain?**

It does not determine:

> **What should G-brain require?**

Changes to G-brain's requirements are architectural decisions outside the auditor's authority.

---

# 4. Relationship With mb-doc-maintainer

The two skills have different scopes.

### mb-doc-maintainer

`mb-doc-maintainer` is triggered **when a document is saved**.

It examines the saved change and maintains the documentation directly affected by that change.

```text
Developer edits
      ↓
Document saved
      ↓
mb-doc-maintainer
      ↓
Maintain affected documentation
```

The maintainer should not continuously attempt to follow the developer while a document is being edited.

### mb-doc-auditor

`mb-doc-auditor` is invoked separately for wider examination.

```text
mb-doc-auditor
      ↓
Examine wider estate
      ↓
Identify accumulated or systemic issues
      ↓
Repair and verify
```

The auditor must therefore **not describe the maintainer as being triggered by "current events."**

Its correct trigger is:

> **Document save.**

The auditor is independent of those save events, although it may use the results of maintenance activity as evidence when deciding where to look more deeply.

---

# 5. When the Auditor Should Run

The auditor may be invoked:

* On explicit request.
* On a defined schedule.
* After substantial restructuring.
* After a migration.
* After changes to G-brain ingestion or indexing.
* After changes to documentation requirements.
* When repeated maintenance problems suggest a wider issue.
* When the run-log indicates accumulated unresolved problems.
* When there is evidence that corpus integrity may have degraded.

The auditor should not run merely because the maintainer has completed a normal save operation.

The maintainer handles normal incremental maintenance.

The auditor handles wider health.

---

# 6. Use of the mb-doc-maintainer Run-Log

`mb-doc-maintainer` should maintain a run-log containing useful information about its maintenance activity.

`mb-doc-auditor` may use this run-log as an **investigative guide**.

The run-log can provide signals such as:

* Repeated repairs to the same document.
* Repeated unresolved issues.
* Repeated ambiguous references.
* Repeated register corrections.
* Documents receiving unusually frequent maintenance.
* Patterns of link repair.
* Recurring front-matter problems.
* Areas of the corpus where maintenance repeatedly encounters problems.

These signals can help the auditor determine where deeper examination may be worthwhile.

However:

> **The run-log is evidence, not a work queue.**

A repeated maintenance event does not automatically mean that the auditor must investigate it.

The auditor should use judgement based on the documented G-brain requirements and the evidence available.

---

# 7. Scope of an Audit

An audit may examine the wider documentation estate, including:

* Document integrity.
* Front matter.
* Document registration.
* `register-local.md`.
* `register-global.md`.
* Links and WikiLinks.
* Document relationships.
* Naming and location consistency where required by G-brain.
* Orphaned or inaccessible documents where relevant.
* Cross-document integrity.
* G-brain ingestion and retrieval prerequisites.
* Accumulated maintenance problems.
* Patterns identified through the maintainer run-log.

The auditor should determine the appropriate scope for the audit rather than automatically performing the largest possible scan.

### Deep audit does not mean maximum audit.

The purpose is to establish meaningful health, not to generate the largest possible list of differences.

---

# 8. Register Integrity

The auditor must verify that document registration is consistent with the documented G-brain requirements.

This includes:

### `register-local.md`

Local development-project libraries, including projects such as:

* `makepdlf-project-library`
* `mb-3-cs-project-library`

and other project libraries that may be created in the future.

### `register-global.md`

The global document registration for:

`project-library-global`

The auditor should identify:

* Missing registrations.
* Incorrect registrations.
* Obsolete registrations.
* Documents registered in the wrong location.
* Registration inconsistencies affecting G-brain.

Where the correct repair is mechanically determinable, safe, and verifiable, the auditor should make the repair.

---

# 9. Finding Classification

Every significant finding should be classified into one of four categories:

### Must fix

The issue violates a known G-brain requirement or creates a concrete integrity problem.

### Can wait

The issue is real but does not need immediate correction.

It should not automatically become a new work queue.

### Does not matter

The detected difference has no meaningful impact on the documented requirements of G-brain.

No action is required.

### Requires human judgement

The correct action cannot safely be determined by the auditor.

The developer should receive a concise decision request.

---

# 10. Detection Is Not a Work Queue

The auditor may detect many differences during an audit.

That does not mean every difference requires action.

The governing principle is:

> **Detection is not a work queue.**

The auditor must distinguish between:

* Something that is different.
* Something that is technically imperfect.
* Something that actually violates a G-brain requirement.
* Something that requires human judgement.

Only the latter categories should create meaningful work.

The existence of additional detectable differences does not prevent an audit from reaching a terminal state.

---

# 11. Automatic Repair

The auditor may automatically repair a problem when:

* The relevant G-brain requirement is explicit.
* The correct repair is mechanically determinable.
* The repair is safe.
* The repair can be verified.

Examples include:

* Correcting known front-matter errors.
* Repairing mechanically determinable links.
* Converting required references to WikiLinks.
* Correcting document registration.
* Removing obsolete registration.
* Repairing known structural inconsistencies.

The auditor must not guess at semantic relationships or invent missing information.

---

# 12. Human Judgement

Human input is required when:

* Multiple possible repairs exist.
* Semantic meaning is ambiguous.
* A document relationship cannot be determined safely.
* A destructive decision is required.
* The G-brain requirement itself is unclear.
* The correct action requires architectural judgement.

The auditor should present the smallest useful decision.

For example:

```text
MB Doc Auditor

Issue:
architecture.md references two possible documents.

Proposed action:
Link to architecture-development.md.

Risk:
Low.

Approve / Reject
```

The auditor must not require the developer to interpret a large report to discover what decision is needed.

---

# 13. Summary Report

At the completion of an audit, the developer should receive a **concise summary**.

The summary should communicate:

* What area was audited.
* What important issues were found.
* What was repaired.
* What remains unresolved.
* Whether human action is required.
* Whether the audited scope now satisfies the known G-brain requirements.

For example:

```text
MB Doc Auditor

Scope:
makepdlf-project-library

Checked:
- Document integrity
- Front matter
- WikiLinks
- Registration
- G-brain requirements

Actions:
- Repaired 4 registrations.
- Corrected 2 broken WikiLinks.

Outstanding:
- 1 ambiguous document relationship requires human judgement.

Status:
Corpus healthy against defined G-brain requirements,
with 1 human decision outstanding.
```

---

# 14. Report Querying

The summary must **not be the only level of information available**.

The developer must be able to query the completed audit and request further detail.

Examples:

```text
Show me more detail about the registration changes.
```

```text
Why was this document considered non-compliant?
```

```text
Show me the G-brain requirement that caused this finding.
```

```text
What did the auditor check but decide did not require action?
```

```text
Show me the maintainer run-log entries that led you to investigate this area.
```

The auditor should then provide the relevant detail from the audit.

The normal interface remains concise.

Detailed evidence should be available **on demand**.

### Reporting principle

> **Summary by default. Detail on request.**

The developer should never have to read a large audit report simply to establish whether action is required.

---

# 15. Completion

An audit must have a clear terminal state.

It must not continue indefinitely because additional differences can always be discovered.

The auditor should be able to reach a state such as:

```text
AUDIT COMPLETE

Audited scope satisfies the defined G-brain requirements.

No outstanding issues requiring action.
```

Or:

```text
AUDIT COMPLETE

Audited scope satisfies the defined G-brain requirements
except for 2 issues requiring human judgement.
```

The existence of issues that are explicitly classified as "Can wait" or "Does not matter" does not prevent completion.

---

# 16. Shared Processing Model

The auditor follows the same fundamental principle as the maintainer:

```text
Identify
    ↓
Determine affected G-brain requirements
    ↓
Determine appropriate action
    ↓
Repair where safe
    ↓
Verify
    ↓
Summarise
    ↓
Finish
```

The difference is scope.

### Maintainer

```text
Saved document
    ↓
Affected documentation
```

### Auditor

```text
Audit scope
    ↓
Wider documentation estate
```

---

# 17. What mb-doc-auditor Must Not Do

`mb-doc-auditor` must not:

* Invent G-brain requirements.
* Decide what G-brain should require.
* Treat every detected difference as work.
* Turn the maintainer run-log into an automatic work queue.
* Perform endless reconciliation.
* Create unnecessary metadata churn.
* Repeatedly rescan the same material without reason.
* Generate large reports by default.
* Require approval for safe mechanical repairs.
* Invent semantic relationships.
* Guess when human judgement is required.
* Become a general document-management system.
* Become a bureaucratic register-enforcement system.
* Duplicate the normal save-time responsibilities of `mb-doc-maintainer`.
* Require the maintainer to perform a corpus-wide audit after every save.
* Become a replacement for development work.
* Become a more elaborate version of DocCycle.

---

# 18. Relationship With DocCycle

The existing DocCycle is outside the scope of this skill.

`mb-doc-auditor` must not modify, dismantle, migrate, refactor, or retire DocCycle as part of its own operation.

The existence of DocCycle does not define the architecture of the Auditor.

The Auditor has its own clearly defined purpose:

> **Maintain wider documentation health according to the explicit requirements of G-brain.**

DocCycle may remain available for future use if desired.

---

# 19. Success Criteria

`mb-doc-auditor` is successful when it can establish, for its defined audit scope, that:

* Documentation satisfies the known G-brain requirements.
* Required front matter is correct.
* Required links and WikiLinks are valid.
* Required registrations are correct.
* `register-local.md` is appropriately maintained.
* `register-global.md` is appropriately maintained.
* Known integrity problems have been repaired where safe.
* Ambiguous issues have been clearly surfaced for human judgement.
* Maintainer run-log evidence has been considered where relevant.
* The developer receives a concise summary.
* Detailed information is available on request.
* The audit reaches a clear terminal state.
* No unnecessary maintenance work has been created.

---

# 20. Governing Principle

The governing principle of `mb-doc-auditor` is:

> **Measure the documentation estate against the known requirements of G-brain, repair what can be safely repaired, use maintenance history as evidence rather than as a work queue, ask for human judgement only when genuinely necessary, and then finish.**

The architectural relationship is therefore:

```text
                    G-brain
                       │
                       │
              defines requirements
                       │
                       ▼
        ┌──────────────────────────┐
        │                          │
        ▼                          ▼
mb-doc-maintainer            mb-doc-auditor
        │                          │
   Document save              On-demand /
        │                     scheduled audit
        │                          │
        ▼                          ▼
Affected documentation       Wider documentation estate
        │                          │
        └──────────┬───────────────┘
                   │
                   ▼
        Healthy documentation
             for G-brain
```

**The maintainer protects what is currently being built.**

**The auditor checks the wider estate.**

**G-brain defines what matters.**

**The developer builds the actual system.**
