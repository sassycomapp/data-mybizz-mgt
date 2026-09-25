---
title: "mb-doc-auditor — Complete Consolidated Plan"
doc-id: "mb-doc-auditor — Complete Consolidated Plan"
---

# mb-doc-auditor — Complete Consolidated Plan

**Status:** Consolidated architectural plan. The auditor's functional requirements are established by the founding architecture and `mb-doc-auditor` specification. Implementation details not established by those documents are explicitly identified rather than invented.

## 1. Purpose

`mb-doc-auditor` periodically examines a defined wider documentation scope, measures it against the documented requirements on which G-brain depends, repairs safe and mechanically determinable problems, surfaces genuine ambiguity, and establishes whether the audited scope is healthy.

**What it is not:** a save-time maintainer, continuous maintenance system, general document-management system, work-generation engine, or replacement for `mb-doc-maintainer`.

**Standing boundaries:**

- **`mb-doc-maintainer`** — independent save-time maintenance. The auditor does not duplicate its normal responsibilities.
- **DocCycle** — completely outside this work. Do not modify, migrate, refactor, dismantle, retire, extract from, or incorporate it.
- **Developer** — receives only decisions that genuinely require human judgement.

**Governing principle:** Measure the documentation estate against the known requirements of G-brain, repair what can be safely repaired, use maintenance history as evidence rather than as a work queue, ask for human judgement only when genuinely necessary, and then finish.

## 2. Architectural role

The two skills have distinct operating scopes:

| Skill | Trigger | Primary scope | Primary question |
| --- | --- | --- | --- |
| `mb-doc-maintainer` | Stable document save event | Saved document and directly affected documentation | What does this saved change require to remain healthy? |
| `mb-doc-auditor` | Explicit request, schedule, or defined audit condition | Selected wider documentation estate | Is this scope still healthy for G-brain? |

The auditor must not be described as a save-event handler. A normal save is handled by `mb-doc-maintainer`; the auditor runs independently.

## 3. Foundation decisions

| # | Area | Decision |
| --- | --- | --- |
| D1 | Role | Deep, periodic, and on-demand corpus-integrity examination. |
| D2 | Authority | Measure only against the authoritative G-brain documentation contract and explicitly assigned MyBizz operating requirements. |
| D3 | Requirement ownership | The auditor does not define or change G-brain requirements. Contract changes are developer architectural decisions. |
| D4 | Trigger | Explicit request, defined audit condition (stated by the developer at invocation), substantial restructuring, migration, G-brain ingestion/indexing change, requirement change, repeated maintenance evidence, or evidence of possible degradation. Not every save. **v1 note (developer decision):** no scheduler exists in this environment; "defined schedule" is recorded as future/not established. Building a scheduler is out of scope. |
| D5 | Scope | Audit a defined scope appropriate to the purpose of the run. Do not default to the largest possible scan. |
| D6 | Run-log | `mb-doc-maintainer` run-log is investigative evidence only. It is never an automatic work queue. |
| D7 | Detection | A detected difference is not automatically work. Findings must be classified against G-brain requirements and operational consequence. |
| D8 | Repair | Automatic only when the requirement is explicit, the repair is mechanically determinable, safe, and independently verifiable. |
| D9 | Human judgement | Required for ambiguous semantics, multiple plausible repairs, destructive choices, unclear requirements, or any action that would require invented information. |
| D10 | Reporting | Concise summary by default; detailed evidence available on request. |
| D11 | Completion | Every audit must terminate in an explicit completion state. Deferred or irrelevant findings do not justify indefinite processing. |
| D12 | Boundaries | No DocCycle involvement; no duplication of normal maintainer save-time work; no general document-management role. |

## 4. G-brain documentation contract

### 4.1 Existing authoritative contract

The auditor consumes the existing G-brain documentation contract rather than creating a competing contract.

**Artifact:** `C:\mybizz\mybizz-config-docs\gbrain\gbrain-doc-contract.md`

The current contract established for the documentation architecture contains:

- **G1–G10:** canonical G-brain behaviour and ingestion requirements.
- **O1–O7:** explicit MyBizz operating requirements that may be stricter than G-brain but must not be looser.
- An explicit **not-established** section prohibiting the invention of additional requirements.
- An explicit **not-required** list defining anti-work-generation boundaries.
- Change control requiring developer decisions for contract changes.

The auditor must treat this contract as read-only authority during an audit. It may enforce the requirements as written but may not extend, reinterpret, or silently alter them.

### 4.2 Requirements currently relevant to the auditor

The auditor must be able to measure, as applicable to the selected scope:

- Valid YAML frontmatter where frontmatter is present.
- Valid frontmatter fence structure and non-empty document body.
- Missing-frontmatter severity according to the contract; missing frontmatter is not inherently an ingestion blocker.
- Conditional `slug` correctness when `slug:` exists.
- String type for `title`, `type`, and `slug` when present.
- Supported WikiLink grammar and resolution behaviour.
- Basename-uniqueness implications for bare-name WikiLinks.
- G-brain page-title resolution behaviour.
- Registered-source ingestion boundaries and overlapping-source constraints.
- Page-type and orphan behaviour where defined by the active G-brain schema.
- The explicit MyBizz frontmatter contract: permanent corpus documents contain exactly `title` and `doc-id`, with both values equal to the filename stem.
- The `tmp-` transient-file exemption.
- `doc-id` equal to the filename slug and filename-based references.
- Register schema and four-event registration discipline.
- Live-derived documentation scope.
- Required WikiLink display convention.
- Existing-link target existence.

The auditor must not create additional requirements for tags, wikilink density, MECE directory structure, numbering, dates, or other properties not established by the contract.

## 5. Audit scope

The auditor may examine:

- Document integrity.
- Frontmatter.
- Document registration.
- `register-local.md`.
- `register-global.md`.
- Links and WikiLinks.
- Document relationships.
- Naming and location consistency where explicitly required.
- Orphaned or inaccessible documents where relevant to the documented requirements.
- Cross-document integrity.
- G-brain ingestion and retrieval prerequisites.
- Accumulated maintenance problems.
- Patterns identified by the maintainer run-log.

The selected audit scope must be explicit for each run.

### Hard exclusion — Anvil

Any folder containing `anvil.yaml` is never documentation, and `anvil.yaml` itself is never read, written, or touched. The estate scanner excludes such folders by class rule, inherited from the scope authority (same rule as the maintainer). An Anvil repo present inside a scanned tree is not inspected, not scanned, and generates no findings.

### Deep audit does not mean maximum audit

The auditor should perform enough examination to establish meaningful health for the selected purpose. It must not scan everything merely because everything is technically scannable.

The audit scope must therefore be determined from:

1. The purpose of the audit.
2. The live documentation scope authority.
3. The relevant G-brain requirements.
4. Evidence indicating where deeper examination is warranted.

## 6. Register integrity

The auditor must verify registration against the documented operating requirements.

### `register-local.md`

Verify registration for local development-project libraries, including existing libraries such as:

- `makepdlf-project-library`
- `mb-3-cs-project-library`
- Future project libraries covered by the registration policy.

### `register-global.md`

Verify global registration for:

- `project-library-global`

The auditor should identify:

- Missing registrations.
- Incorrect registrations.
- Obsolete registrations.
- Registrations in the wrong location.
- Registration inconsistencies that affect G-brain documentation integrity.

Where the correct repair is mechanically determinable, safe, and verifiable, repair it automatically.

### Register universe

The register universe is discovered live using the same rule as the maintainer: each project library's root `register-local.md` (located by walking from the document's path), plus `register-global.md` for `project-library-global`. The libraries named above are examples, not an exhaustive list. The current known inventory is the six register files in `register-paths.md` (this folder): `data-mybizz-mgt`, `makepdlf-project-library`, `mb-3-cs-project-library`, `mybizz-config-docs`, `mybizz-os-docs`, and `project-library-global`. `pdlf-register.md` (under `C:\pdlf\pdlf-library`) is outside this inventory; if a C:\pdlf audit scope ever encounters it, surface it as a finding for human judgement rather than assuming its status.

## 7. Use of the maintainer run-log

The auditor may inspect the durable `mb-doc-maintainer` run-log to identify evidence such as:

- Repeated repairs to the same document.
- Repeated unresolved issues.
- Repeated ambiguous references.
- Repeated register corrections.
- Documents receiving unusually frequent maintenance.
- Recurring link repairs.
- Recurring frontmatter problems.
- Areas repeatedly producing maintenance problems.

The run-log is **evidence, not a work queue**.

A repeated event does not automatically create an audit task. The auditor must establish a reasoned connection between the evidence and the documented G-brain requirements before expanding investigation.

## 8. Processing model

The auditor follows this processing sequence:

```text
Identify audit scope
    ↓
Load authoritative G-brain requirements
    ↓
Examine relevant documentation
    ↓
Detect potential integrity conditions
    ↓
Determine which requirements are affected
    ↓
Classify each significant finding
    ↓
Repair safe, mechanically determinable issues
    ↓
Verify repairs and remaining conditions
    ↓
Summarise result
    ↓
FINISH
```

The auditor must not turn detection into an open-ended reconciliation loop.

## 9. Finding classification

Every significant finding must fall into exactly one category.

### Must fix

The condition violates a known G-brain or explicit operating requirement, or creates a concrete integrity problem that materially affects the audited purpose.

Safe mechanical repairs should normally be performed automatically.

### Can wait

The condition is real but does not require immediate correction for the current audit purpose or does not belong to the current action scope.

It must not automatically become a new work queue.

### Doesn't matter

The detected difference has no meaningful effect on the documented G-brain requirements.

No action is required.

### Requires human judgement

The auditor cannot safely determine the correct action without semantic or architectural judgement.

The developer receives a concise decision request.

## 10. Automation boundary

Automatic repair requires **all** of the following:

- The governing requirement is explicit.
- The intended result is mechanically determinable.
- The operation is safe.
- The result can be independently verified.

Examples include:

- Correcting known frontmatter errors.
- Restoring the required two-field frontmatter contract.
- Repairing mechanically determinable links.
- Converting references to the required WikiLink form where unambiguous.
- Correcting document registration.
- Retiring obsolete registration **in place** — registers are append-only (four-event model, O4/D4/D5 of the maintainer plan): an obsolete row's `state` is set to `Retired` (`superseded-by` where known); a row is never deleted. A row registered in the wrong location is retired in place there and the correct row is appended in the correct register. If the correct register or supersession target is not determinable, this becomes a human-judgement finding.
- Repairing known structural inconsistencies.

Human judgement is required when:

- Multiple plausible targets exist.
- Semantic meaning is ambiguous.
- A document relationship cannot be safely determined.
- A destructive decision is required.
- The G-brain requirement itself is unclear or contradictory.
- The proposed action would require invented information.

The auditor must never guess merely to avoid asking the developer.

## 11. Human decision requests

Human questions must expose the smallest useful decision.

Use a form such as:

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

Do not require the developer to interpret a large report to determine what decision is being requested.

## 12. Reporting

Every completed audit produces a concise summary containing:

- Audited scope.
- Important issues found.
- Actions performed.
- Unresolved issues.
- Whether human action is required.
- Whether the audited scope satisfies the known G-brain requirements.

Example:

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

### Reporting principle

> **Summary by default. Detail on request.**

The summary is not the only information retained. The completed audit must preserve sufficient evidence to answer subsequent queries about what was checked, what changed, why a finding was raised, why an issue was not acted upon, and which requirement caused an action.

## 13. Report querying

The developer must be able to request further detail from the completed audit.

Supported query classes include:

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

The normal output remains concise. Detailed evidence is provided only when requested.

## 14. Completion and terminal state

The auditor must be able to stop after establishing the health of the audited scope.

A successful run may end with:

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

Findings classified as **Can wait** or **Doesn't matter** do not prevent completion.

The existence of more detectable differences is not evidence that the audit is incomplete.

## 15. Skill specification

**Artifact:** `SKILL.md` for `mb-doc-auditor`.

The skill specification should contain these point-of-action sections:

1. **Governance header** — boundary rules first; no DocCycle involvement; no invented G-brain requirements; no work from mere difference; no automatic work queue from the maintainer run-log; no large routine reports; no endless reconciliation; no duplication of the maintainer; no general document-management role; any folder containing `anvil.yaml` is never documentation and `anvil.yaml` itself is never read, written, or touched.
2. **Invocation model** — explicit/on-schedule/on-condition audit; never save-time triggering.
3. **Requirement authority** — consume the authoritative G-brain documentation contract; do not modify it.
4. **Scope selection** — define the audit scope before examination; use the minimum sufficient scope.
5. **Estate examination** — document integrity, frontmatter, links, registration, relationships, ingestion/retrieval prerequisites, and other explicitly contracted invariants.
6. **Run-log evidence** — use maintainer history only to guide investigation.
7. **Finding classification** — Must fix / Can wait / Doesn't matter / Requires human judgement.
8. **Automation boundary** — repair only explicit, mechanical, safe, verifiable conditions.
9. **Human decisions** — concise decision requests where ambiguity remains.
10. **Reporting and querying** — concise summary first, detailed evidence on demand.
11. **Completion** — verify, summarise, and terminate.

The specification should remain operational and concise. It should not become a general exposition of documentation theory.

## 16. Tooling architecture

The implementation should use the minimum infrastructure required to perform the defined audit safely.

Where technically appropriate, existing `mb-doc-maintainer` tooling may be reused as shared implementation infrastructure. Reuse must not merge the responsibilities of the two skills.

The auditor requires, at minimum, capability for:

| Capability | Function |
| --- | --- |
| Scope reader | Obtain the current audit scope from the authoritative scope definition. **Locked:** `C:\mybizz\mybizz-os-docs\os-reference-docs\mybizz-scope-list.md`, read live at every run. |
| Contract reader | Load the G-brain documentation contract without altering it. **Locked:** `C:\mybizz\mybizz-config-docs\gbrain\gbrain-doc-contract.md`. |
| Estate scanner | Enumerate only the selected audit scope and applicable exceptions. Exclusions: any folder containing `anvil.yaml`; `tmp-` prefixed files; stencils; quarantine; backups; catalogue; logs (the maintainer's exempt classes). |
| Frontmatter checks | Validate contract-defined metadata and structural rules. |
| Link checks | Detect required WikiLinks, missing targets, and basename collisions. |
| Register checks | Compare registration against the defined registration model. |
| Run-log reader | Provide maintenance history as evidence when relevant. **Locked:** `C:\mybizz\mybizz-config-docs\mb-doc-maintainer\doc-maintainer-run-log.md` (the maintainer SKILL.md §10 path — not the unrelated `doc-maintainer-log.md` in the same directory). Absent or empty log → "no maintenance history available"; the audit proceeds. |
| G-brain reader | Read-only live verification of G9/G10 within the selected scope (e.g. `gbrain sources list`, `gbrain orphans`). **Read-only calls only — the auditor never writes to G-brain.** CLI unavailable or fails → classify as Can wait; the audit still completes. |
| Repair engine | Apply only safe, mechanically determinable repairs. |
| Verification | Independently verify repairs and remaining findings. |
| Audit record | Preserve sufficient evidence for later queries. **Locked:** `C:\mybizz\mybizz-config-docs\mb-doc-auditor\doc-auditor-records.md` — one append-only block per run (date, scope, checked, findings by classification, actions, terminal state); register row added on creation, mirroring the maintainer run-log's treatment. |
| Summary/reporting | Produce concise completion output and support detail-on-demand queries. |

Storage locations and boundaries were deferred by the original auditor specification; the locked values above were set by developer decision (2026-09-25) and are no longer open. Any future change to them is a developer decision.

## 17. Installation and verification

### Source repository

The skill's home is the source repository `C:\mybizz\mb-doc-auditor` (git init + GitHub remote, per ADR `adr-dev-tooling-source-repos-must-be-github-backed` — same pattern as `C:\mybizz\mb-doc-maintainer`). It contains the skill source file, `tool/`, and `tests/`.

**Skill source file convention (critical):** the source file is `mb-doc-auditor-skill.md` — not `SKILL.md`. In the source repo its frontmatter carries the corpus two-field contract only: `title: "mb-doc-auditor-skill"` and `doc-id: "mb-doc-auditor-skill"` (both = filename stem), mirroring `C:\mybizz\mb-doc-maintainer\mb-doc-maintainer-skill.md`. Installation transforms it:

- Installed path: `~/.config/opencode/skills/mb-doc-auditor/SKILL.md`
- Installed frontmatter: OpenCode skill frontmatter — `name: mb-doc-auditor` plus a `description` with trigger phrases (see the installed `mb-doc-maintainer/SKILL.md` frontmatter for the pattern).
- The source file is never installed verbatim under the `SKILL.md` name. Installing a file with corpus frontmatter as a skill entry point is a known blockage; the frontmatter conversion is part of installation, not an afterthought.

### Documentation folder

The auditor's documentation lives at `C:\mybizz\mybizz-config-docs\mb-doc-auditor\` (corpus documents with the two-field frontmatter, registered in the mybizz-config-docs register). Phase 7 populates the three-doc suite there.

### Verification

Verification should cover at least:

- OpenCode discovers the skill.
- The skill reads the authoritative G-brain documentation contract.
- An explicit audit examines only the selected scope.
- The maintainer run-log can be used as evidence without becoming a work queue.
- Safe mechanical findings are repaired automatically.
- Ambiguous findings are surfaced for human judgement.
- Requirements are never invented.
- The auditor does not invoke itself merely because a document was saved.
- The auditor does not duplicate normal maintainer save-time work.
- The summary is concise.
- Detailed evidence is retrievable on request.
- The audit terminates with a clear status.
- No unnecessary work is created.
- DocCycle remains untouched.

## 18. Test scenarios

The test suite should include at least:

### Healthy corpus

Expected result: audit completes with no actionable findings.

### Invalid frontmatter

Expected result: condition is classified against the applicable contract requirement; safe repair occurs automatically where determinable; verification follows.

### Missing frontmatter

Expected result: severity follows the G-brain contract and the MyBizz operating contract; no blanket rule is invented.

### Broken WikiLink

Expected result: repair automatically only when the target and intended relationship are mechanically determinable.

### Ambiguous basename

Expected result: ambiguity is not guessed away; human judgement is requested when required.

### Incorrect registration

Expected result: registration is corrected automatically when the proper row is mechanically determinable.

### Obsolete registration

Expected result: obsolete registration is retired **in place** when its status is determinable — `state: Retired` set on the existing row (`superseded-by` where known); the row is never deleted (append-only, four-event model). A wrong-register row is retired there and the correct row appended in the correct register. Not determinable → human judgement.

### Anvil repo present

Expected result: a folder containing `anvil.yaml` inside the audit scope is not inspected, not scanned, and generates no findings. `anvil.yaml` itself is never read.

### Absent or empty run-log

Expected result: the audit proceeds with "no maintenance history available" as the run-log evidence summary; no repair, no work generation, no error state.

### Maintainer run-log signal

Expected result: repeated maintenance history may guide investigation, but does not automatically create an audit task.

### Harmless inconsistency

Expected result: classify as **Doesn't matter** or **Can wait** where the documented requirements support that conclusion; audit still completes.

### Requirement ambiguity

Expected result: do not invent a rule; surface the requirement conflict or missing decision to the developer.

### DocCycle present

Expected result: no inspection or modification is required merely because DocCycle exists; the auditor remains independent.

## 19. Execution sequence

| Step | Work | Gate |
| --- | --- | --- |
| 0 | **Preflight** — verify the authoritative G-brain contract exists, is readable, and is the current source of requirements; verify the live scope authority; confirm `mb-doc-maintainer` remains independent; confirm DocCycle is untouched. | Preflight verified |
| 1 | **Phase 1 — skill specification** — write the operational `SKILL.md` from this consolidated plan and the auditor base specification. | Specification review |
| 2 | **Phase 2 — tooling** — implement the minimum audit, evidence, repair, verification, and reporting capabilities; reuse compatible maintainer utilities where technically appropriate without merging responsibilities. | Tool tests pass |
| 3 | **Phase 3 — installation** — install the skill to OpenCode and verify discovery. | Discovery verified |
| 4 | **Phase 4 — corpus-copy walkthroughs** — run controlled audits covering healthy, repairable, ambiguous, deferred, irrelevant, registration, link, frontmatter, anvil-exclusion, absent-run-log, and run-log-guided cases. Corpus copies live at `C:\data-mybizz-mgt\tmp-doc-auditor-walkthroughs\` (the `tmp-` prefix makes them O3-exempt; outside all six corpora; removed after walkthroughs). | Walkthroughs pass |
| 5 | **Phase 5 — operational verification** — perform an audit against the intended live scope, verify the terminal-state behaviour and detail-on-demand reporting, and confirm no unnecessary work is created. | Operational verification complete |
| 6 | **Phase 6 — completion report** — record final implementation state, known limitations, and any decisions intentionally left outside the skill. | Completion accepted |
| 7 | **Phase 7 — documentation suite** — populate the three currently empty documents in `C:\mybizz\mybizz-config-docs\mb-doc-auditor\`: `doc-auditor-config.md` (the spec — single source of expected values), `doc-auditor-reference.md`, and `doc-auditor-explainer.md`, following the maintainer examples (`doc-maintainer-config.md`, `doc-maintainer-reference.md`, `doc-maintainer-explainer.md`). Corpus two-field frontmatter; register row in the mybizz-config-docs register. | Suite matches examples |
| 8 | **Phase 8 — config-management** — apply `mb-config-manager` to `mb-doc-auditor` per `C:\mybizz\prompts\config-setup-prompt.md` with `{system}` = `mb-doc-auditor`. Named first step: add the `mb-doc-auditor` row (state `WIP`) to `config-manager-register.md` — authority: developer instruction, doc-maintainer S-1 precedent. Then the prompt's Phases 0–5 (suite build-out to the 8-file standard, install `mb-config-doc-auditor` with hash pair, formal run #1, per-item gate, close-out). That prompt's standing rules apply verbatim. | Exam result + dispositions recorded |

## 20. What mb-doc-auditor must not do

`mb-doc-auditor` must not:

- Invent G-brain requirements.
- Decide what G-brain should require.
- Treat every detected difference as work.
- Turn the maintainer run-log into an automatic work queue.
- Perform endless reconciliation.
- Create unnecessary metadata churn.
- Repeatedly rescan the same material without reason.
- Generate large reports by default.
- Require approval for safe mechanical repairs.
- Invent semantic relationships.
- Guess when human judgement is required.
- Become a general document-management system.
- Become a bureaucratic register-enforcement system.
- Duplicate normal save-time responsibilities of `mb-doc-maintainer`.
- Require `mb-doc-maintainer` to perform a corpus-wide audit after every save.
- Become a replacement for development work.
- Become another DocCycle.
- Modify, dismantle, migrate, refactor, or retire DocCycle.

## 21. Success criteria

`mb-doc-auditor` is successful when it can establish, for its defined audit scope, that:

- Documentation satisfies the known G-brain requirements.
- Required frontmatter is correct.
- Required links and WikiLinks are valid.
- Required registrations are correct.
- `register-local.md` and `register-global.md` are maintained according to the documented model.
- Known integrity problems have been repaired where safe.
- Ambiguous issues have been clearly surfaced for human judgement.
- Relevant maintainer run-log evidence has been considered without becoming a work queue.
- The developer receives a concise summary.
- Detailed information is available on request.
- The audit reaches a clear terminal state.
- No unnecessary maintenance work has been created.
- The implementation does not expand the auditor into a second DocCycle.

## 22. Final North Star

```text
G-brain
   │
   │ defines requirements
   ▼
mb-doc-maintainer ──────► protects current development
   │
   │
mb-doc-auditor ─────────► checks wider documentation health
   │
   ▼
Healthy documentation for G-brain
   │
   ▼
Developer builds the actual system
```

> **mb-doc-maintainer** protects what is currently being built.
>
> **mb-doc-auditor** periodically checks the wider estate.
>
> **G-brain** defines what matters.
>
> **The developer** builds the actual system.

The terminal test for every auditor decision is:

> **Does this preserve, restore, or verify something that G-brain actually requires?**

If not, it does not belong in the auditor.
