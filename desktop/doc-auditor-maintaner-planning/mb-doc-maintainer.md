---
title: "mb-doc-maintainer"
doc-id: "mb-doc-maintainer"
---
# mb-doc-maintainer

## 1. Definition

`mb-doc-maintainer` is the continuous documentation-maintenance skill for the development environment.

Its job is to maintain the integrity of documentation **as development takes place**, while keeping its scope limited to the documentation affected by the developer's work.

It exists to ensure that saved documentation remains suitable for use by G-brain.

It is not a documentation auditor, corpus-cleaning system, document-management system, or replacement for `mb-doc-auditor`.

---

# 2. Primary Objective

The objective of `mb-doc-maintainer` is:

> **When a document is saved, ensure that the affected documentation remains compliant with the documented requirements of G-brain, structurally coherent, correctly registered, and usable by G-brain.**

The maintainer must do the minimum work necessary to achieve this objective.

It must not create additional maintenance work merely because something can be detected.

---

# 3. G-brain Requirements Must Be Explicit

`mb-doc-maintainer` must **not assume what G-brain requires**.

The skill must have access to an explicit, authoritative definition of the documentation requirements that G-brain depends upon.

This should take the form of a **G-brain documentation contract**, requirements file, configuration, or equivalent authoritative source.

The exact implementation may be determined during development, but the principle is mandatory:

```text
G-brain requirements
        ↓
mb-doc-maintainer
        ↓
Measure saved documentation against those requirements
```

The requirements should define, where applicable:

- Required front matter.

- Required document properties.

- Required registration information.

- Link requirements.

- WikiLink requirements.

- Naming or location requirements.

- Relationships that G-brain depends upon.

- Any other measurable documentation invariants required for reliable G-brain operation.

The maintainer may enforce only requirements that are explicitly defined by this source or otherwise explicitly provided as part of its operating contract.

It must not invent requirements because they appear useful, tidy, conventional, or desirable.

### Important distinction

`mb-doc-maintainer` determines:

> **Does this saved documentation satisfy the known requirements of G-brain?**

It does not determine:

> **What should G-brain require?**

The latter is an architectural or system-design decision and is outside the maintainer's authority.

---

# 4. Trigger

The primary trigger is:

> **Document save.**

The maintainer should operate on the **saved state of a document**, not on the document while the developer is actively editing it.

This is intentional.

The developer must be able to modify a document without the maintainer continually attempting to follow incomplete changes.

The operating model is:

```text
Developer edits
      ↓
Developer saves
      ↓
mb-doc-maintainer triggered
      ↓
Inspect saved change
      ↓
Determine affected requirements
      ↓
Repair where appropriate
      ↓
Verify
      ↓
Present concise summary
      ↓
Wait for next save
```

If multiple saves occur in rapid succession, the maintainer should coalesce them where practical and operate against the latest saved state rather than repeatedly processing intermediate states.

---

# 5. Scope of Work

The maintainer works from the saved change and determines what documentation is actually affected.

It should normally examine:

- The saved document.

- Its directly affected references.

- Files directly affected by a move or rename.

- Links affected by the change.

- The appropriate local or global register.

- Any other files directly required to restore a documented G-brain invariant.

It must not automatically expand a local change into a corpus-wide investigation.

### Core principle

> **Maintain what changed, not everything that exists.**

---

# 6. Document Creation

When a new document is saved, the maintainer should determine whether it satisfies the G-brain documentation requirements.

Where required, it should:

- Add or correct required front matter.

- Establish required metadata.

- Ensure the document is correctly located.

- Ensure required references are valid.

- Convert applicable document references to WikiLinks.

- Verify that referenced targets exist.

- Register the document in the appropriate register.

Repairs should be automatic when they are mechanically determinable, safe, and verifiable.

---

# 7. Document Modification

When an existing document is saved, the maintainer should inspect the changes and affected relationships.

It should check only the requirements relevant to the change and the document's established relationships.

Where necessary it should:

- Correct required front matter.

- Repair affected links.

- Convert appropriate references to WikiLinks.

- Verify referenced files.

- Update registration information.

- Restore any directly affected G-brain invariant.

It should not use an ordinary document save as justification for scanning the entire corpus.

---

# 8. Document Move or Rename

When a document is moved or renamed, the maintainer should identify directly affected references and registration records.

Where the correct repair is mechanically determinable, it should:

- Update references.

- Update WikiLinks.

- Update the appropriate register.

- Verify affected links.

- Verify the document's new location.

- Remove obsolete registration where appropriate.

If the correct target or relationship cannot be determined safely, the maintainer must ask the developer rather than guess.

---

# 9. Document Deletion

When a document is deleted, the maintainer should identify directly affected documentation.

It should:

- Remove the document from the appropriate register.

- Identify affected references.

- Repair references where the correct replacement is known.

- Report unresolved references where a human decision is required.

It must not invent replacement documents or relationships.

---

# 10. Link Maintenance

For links affected by a saved change, the maintainer should verify:

- The target exists.

- The reference points to the intended document.

- The reference is represented using the required WikiLink form.

- The relationship satisfies the applicable G-brain requirement.

A link that technically resolves is not automatically considered semantically correct.

Where semantic correctness cannot be established mechanically, the maintainer should surface the issue for human judgement rather than inventing a relationship.

---

# 11. Register Maintenance

`mb-doc-maintainer` is responsible for maintaining the document registers.

There are two register levels.

### `register-local.md`

`register-local.md` maintains registration of documents belonging to a local development-project library.

Examples include:

- `makepdlf-project-library`

- `mb-3-cs-project-library`

Other project libraries may be created in the future and must follow the same principle.

The maintainer must determine the applicable local register from the document's project/library context.

### `register-global.md`

`register-global.md` maintains registration of documents belonging to:

`project-library-global`

The maintainer must keep the appropriate global registration current when documents are:

- Created.

- Moved.

- Renamed.

- Deleted.

- Otherwise changed in a way that affects their registration.

Register maintenance is part of normal documentation maintenance.

It must not become a separate approval bureaucracy.

If registration can be updated mechanically and safely, the maintainer should update it automatically.

If the correct registration cannot be determined safely, it should ask for human judgement.

---

# 12. Classification of Findings

Every finding should be classified into one of four categories:

### Must fix

The saved change violates a known G-brain requirement or creates a concrete integrity problem.

The maintainer should repair it automatically where safe.

### Can wait

The issue is real but does not need to be resolved as part of the current maintenance event.

It should not automatically become a new work queue.

### Does not matter

The difference has no meaningful impact on the documented requirements of G-brain.

No action is required.

### Requires human judgement

The maintainer cannot safely determine the correct action.

The developer should receive a concise decision request.

---

# 13. Automation Boundary

The maintainer should act automatically when all of the following are true:

- The required action is explicitly supported by the G-brain requirements.

- The correct change is mechanically determinable.

- The change is safe.

- The change can be verified.

Human input is required when:

- The correct semantic relationship is ambiguous.

- Multiple valid repairs are possible.

- A destructive decision is required.

- The G-brain requirement itself is unclear.

- The action would require inventing information.

The maintainer must never guess merely to avoid asking a question.

---

# 14. Summary Report

After maintenance, the developer should receive a **concise summary**, not a large diagnostic report.

The summary should tell the developer:

- What was checked.

- What was changed.

- What remains unresolved.

- Whether human action is required.

For example:

```text
MB Doc Maintainer

Saved: architecture.md

Actions:
- Added missing front matter.
- Converted 3 document references to WikiLinks.
- Updated register-local.md.

Status:
- G-brain requirements satisfied.
- No human action required.
```

If a decision is required:

```text
MB Doc Maintainer

Saved: architecture.md

Issue:
Reference to "X" could refer to two documents.

Proposed action:
Link to X-development.md.

Risk:
Low.

Approve / Reject
```

---

# 15. Report Querying

The summary must **not be the only available level of information**.

The developer must be able to query the maintenance result and request further detail.

For example:

```text
Show me more detail on the WikiLink changes.
```

or:

```text
Why did you change register-local.md?
```

or:

```text
Show me the G-brain requirement that caused this front matter change.
```

or:

```text
What did you check but decide did not need changing?
```

The maintainer should then provide the relevant detail from its maintenance operation.

The normal interface remains concise.

Detailed information should be available **on demand**, rather than being pushed into every report.

---

# 16. Reporting Principle

> **Summary by default. Detail on request.**

The maintainer must not overwhelm the developer with information that has no immediate decision value.

The developer should never have to read a large report simply to discover that nothing important requires attention.

---

# 17. Processing Model

The fundamental processing model is:

```text
Identify change
      ↓
Determine affected G-brain requirements
      ↓
Determine affected documentation
      ↓
Repair what can be safely repaired
      ↓
Update required registration
      ↓
Verify
      ↓
Summarise
      ↓
Finish
```

The process must terminate.

Detection is not a work queue.

Finding additional differences does not, by itself, justify continuing the maintenance operation.

---

# 18. What mb-doc-maintainer Must Not Do

`mb-doc-maintainer` must not:

- Perform a full corpus audit after every save.

- Attempt to make the entire documentation estate perfect.

- Search the entire corpus for unrelated problems.

- Process historical inconsistencies unrelated to the current change.

- Create maintenance work merely because something differs.

- Invent G-brain requirements.

- Invent semantic relationships.

- Guess when the correct action is uncertain.

- Generate large routine reports.

- Require human approval for safe mechanical repairs.

- Turn register maintenance into a bureaucratic approval process.

- Repeatedly rescan unchanged material without a specific reason.

- Become a general document-management system.

- Duplicate the responsibilities of `mb-doc-auditor`.

- Become a smaller version of DocCycle.

---

# 19. Relationship With mb-doc-auditor

The two skills have deliberately different scopes.

```text
Development
     │
     ▼
Document saved
     │
     ▼
mb-doc-maintainer
     │
     └── Maintains the affected documentation

Occasionally
     │
     ▼
mb-doc-auditor
     │
     └── Examines the wider documentation estate
```

### mb-doc-maintainer asks:

> **Did this saved development change leave the affected documentation compliant with the requirements G-brain depends upon?**

### mb-doc-auditor asks:

> **Is the wider documentation estate healthy and usable by G-brain?**

The maintainer protects the developer's current work.

The auditor protects the wider estate.

Neither should become a substitute for the other.

---

# 20. Success Criteria

`mb-doc-maintainer` is successful when, after a relevant document is saved:

- The affected documentation satisfies the applicable G-brain requirements.

- Required front matter is correct.

- Affected links resolve correctly.

- Applicable references are WikiLinks.

- The appropriate register is current.

- Safe mechanical problems have been repaired automatically.

- Genuine ambiguity has been surfaced clearly.

- The developer receives a concise summary.

- Further detail is available on request.

- No unnecessary corpus-wide work has been created.

The maintainer does **not** need to establish that the entire corpus is healthy.

That is the responsibility of `mb-doc-auditor`.

---

# 21. Governing Principle

The governing principle of `mb-doc-maintainer` is:

> **Maintain the saved change against the known requirements of G-brain, repair what can be safely repaired, ask only when judgement is genuinely required, and then stop.**

Its purpose is to keep documentation maintenance almost invisible so that the developer can spend their time building the actual system.

**G-brain is the reason the maintainer exists.**

**The developer is not the maintenance system.**
