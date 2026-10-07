---
title: "documentation-anomalies-task-list"
doc-id: "mb-9d553253"
updated: "2026-10-07"
---
# Documentation Anomalies — Task List

Version 2 — 2026-10-07. Every finding from version 1 (items 1–39) is kept, with its original number. The list is ordered for execution: dependencies first, then the quickest fixes, then the most complicated. A task that depends on another names it; that dependency is always in an earlier section.

Run commit all once at the end of each section, not after every task.

---

## Section 1 — Dependencies: decisions and checks other tasks wait on

### 1.1 — Decide one home for the environment explainer

Items:

- **Item 3.** `mybizz-os-docs\os-reference-docs\environment-explainer.md`. Finding: Now a copy of the PDLF version, so it says "this document in the PDLF library" while living in `mybizz-os-docs`. Two copies of one document exist. Correction: Decide one home; point the other location to it.

Steps:

1. Choose the one location to keep: `C:\pdlf\pdlf-library\pdlf-explainer-docs\pdlf-environment-explainer.md` or `C:\mybizz\mybizz-os-docs\os-reference-docs\environment-explainer.md`.
2. Record the decision; task 4.1 applies it.

### 1.2 — Decide how the master memory explainer is kept current

Items:

- **Item 5.** `memory-master-explainer.md` §11. Finding: "Maintenance rule": every memory-component session updates this document at close-out. The close-out decision removed master-explainer updates from close-out. Correction: Reconcile the rule with `/mb-close-out`.

Steps:

1. Decide whether memory-component sessions still update the master explainer, given that `/mb-close-out` does not.
2. Record the decision; task 4.2 applies it.

### 1.3 — Decide which mb-3-cs design figures are current

Items:

- **Item 33.** `positioning-strategy.md`, `ceo-review-v2-roadmap-2026-06-26.md` (mb-3-cs). Finding: Disagree on the size of the design: 36 data tables in one, 43 tables and 41 ADRs in the other. Both predate PDLF. Correction: Mark the mb-3-cs product documents as pre-PDLF, or point to one current figure.

Steps:

1. Decide whether the mb-3-cs product documents are marked as pre-PDLF, or which single figure is current.
2. Record the decision; task 3.13 apmbplies it.

### 1.4 — Verify three live states

Items:

- **Item 26.** `config-manager-explainer.md`. Finding: Says the orchestrator's "draft lives here; it moves to its install location when built" — current build state of the orchestrator is unclear. Correction: Verify and state current state.
- **Item 27.** `mb-compile-rules-explainer.md`. Finding: Open question that its two skill copies are kept in step by nothing; "19 source documents" is a fixed count. Correction: Verify; point to the configuration for counts.
- **Item 29.** `graphify-explainer.md`. Finding: States mb-3-cs is paused and gives installed/upstream versions; both may have changed. Correction: Verify; point to the configuration for versions.

Steps:

1. Check whether the `mb-config-manager` orchestrator is built and installed (item 26).
2. Check whether the two `mb-compile-rules` skill copies are identical, and the current number of rule sources (item 27).
3. Check Graphify's installed and upstream versions, and whether mb-3-cs is still paused (item 29).
4. Record the results; tasks 3.9, 3.10 and 3.11 use them.

### 1.5 — Re-certify the frontmatter conventions

Items:

- **Item 24.** `frontmatter conventions.md`. Finding: "Awaiting re-certification by the developer." Correction: Re-certify or remove the note.

Steps:

1. Read `frontmatter conventions.md` and confirm it is correct as it stands.
2. Record the decision; task 2.12 applies it.

### 1.6 — Decide the two sysdoc-creator open items

Items:

- **Item 28.** `sysdoc-creator-explainer.md`. Finding: Open items: missing skill-index register entry; file-name prefix differs from folder name. Correction: Resolve or record as decided.

Steps:

1. Decide whether the skill-index register entry is added, and whether the file-name prefix is kept or changed.
2. Record the decision; task 3.12 applies it.

---

## Section 2 — Quick fixes: one line or one passage, no dependencies left

### 2.1 — Retire the session-numbers fact in GBrain

Items:

- **Item 36.** `C:\mybizz\mybizz-config-docs\facts\2026-09-15-session-numbers-from-sessions-log.md` (a governed fact). Finding: States that session numbers come from the sessions log. Session numbers no longer exist: `/mb-close-out` names each page `sessions/<YYYY-MM-DD>-<short-slug>`, and past sessions are found by topic, not number. Existing numbered pages keep their names. Correction: Retire the fact (not rewrite it): expire it in GBrain by its fact number, and delete the fact file.

Steps:

1. The fact file is already deleted.
2. OpenCode: say "retire the governed fact that says session numbers come from the sessions log".

### 2.2 — Rebuild the docmap

Items:

- **Item 37.** `C:\dev\dev-root\docmap.md`, line 31. Finding: Folder-tree row for `sessions-log/`, a folder that no longer exists. Correction: Run `build-docmap.py --write`, which removes entries that no longer exist, then commit all.

Steps:

1. WSL terminal: `python3 /mnt/c/mybizz/scripts/build-docmap.py --write`.

### 2.3 — Remove `.roots` from the commit-all procedure's tools table

Items:

- **Item 11.** `commit-all-repositories.md`. Finding: Tools table lists `.roots`. Correction: Remove `.roots`.

### 2.4 — Remove the source count from repository organisation

Items:

- **Item 23.** `repo-organization.md`. Finding: "Verified against gbrain sources list (22 sources)"; `mb-close-out` added a source. Correction: Remove the count or update it.

### 2.5 — Correct the repository count in the global AGENTS.md

Items:

- **Item 39.** `~/.config/opencode/AGENTS.md`, "Facts across documents". Finding: Says "the eight documentation repositories". Correction: Replace with "the documentation repositories on the commit-all list".

### 2.6 — Add the GBrain sync rule outside GStack's block in the global AGENTS.md

Items:

- **Item 38.** `~/.config/opencode/AGENTS.md`, inside GStack's managed block. Finding: Tells agents to "Run `/sync-gbrain` after meaningful code changes"; GBrain is synced by commit all. The block is rewritten by GStack, so an edit inside it may not last. Correction: Add a rule outside the block that GBrain is synced only by commit all, overriding the block's line.

### 2.7 — Remove the two logs from the data-mybizz-mgt README

Items:

- **Item 35.** `C:\data-mybizz-mgt\README.md`, lines 30–33. Finding: Describes both logs as current, with their locations. Correction: Remove the two entries.

### 2.8 — Remove the resolved open question from the mb-project-docs explainer

Items:

- **Item 18.** `project-docs-explainer.md`. Finding: Open question says mb4ecom and mb5pdlf are not under the commit hook; they are. Correction: Remove.

### 2.9 — Correct the close-out step number in the mb-project-docs documents

Items:

- **Item 19.** `project-docs-reference.md`, `project-docs-config.md`. Finding: Say the close-out procedure invokes the skill at "Step 2a"; in `/mb-close-out` it is Step 3. Correction: Update the step reference.

### 2.10 — Four corrections in daily-ops

Items:

- **Item 13.** `daily-ops.md`. Finding: "TEST mb-doc-check" says 143 tests; `doc-check-config.md` says 149. Correction: Point to the configuration for the number.
- **Item 14.** `daily-ops.md`. Finding: Cross-references to sections that no longer exist: "see Fix below" (GBrain test), "see AFTER DOING WORK above" (sync_freshness fix). Correction: Point to the current sections.
- **Item 15.** `daily-ops.md`. Finding: "MCP / GBrain not responding" restarts OpenCode from the makePDLF folder; the start procedure starts without a folder. Correction: Align with section 1.
- **Item 16.** `daily-ops.md`. Finding: Grant section carries a history note "(verified 2026-09-11)". Correction: Remove the date.

### 2.11 — Correct the scope list's notes and duplicate entry

Items:

- **Item 25.** `mybizz-scope-list.md`. Finding: Notes mention only mb4ecom as an in-scope placeholder; `C:\dev\project-template` is listed twice (private data, and disposable/template). Correction: Mention mb5pdlf; list the template once.

### 2.12 — Apply the frontmatter re-certification

*Depends on: task 1.5.*

Items:

- **Item 24.** `frontmatter conventions.md`. Finding: "Awaiting re-certification by the developer." Correction: Re-certify or remove the note.

Steps:

1. Remove or update the "Awaiting re-certification" note per task 1.5.

---

## Section 3 — Small edits: one document, a few passages

### 3.1 — Remove `.roots` and the dormant-libraries line from the linking explainer

Items:

- **Item 8.** `documentation-linking-explainer.md` §2, §5. Finding: Mentions `mb-doc-check.roots`, which is deleted, including in "Adding a repository". Correction: Remove; `mb-doc-check.sources` is the single list.
- **Item 9.** `documentation-linking-explainer.md` §7. Finding: Opportunity "bringing the two dormant libraries" — already done. Correction: Remove.

### 3.2 — Remove the roots file and dormant-libraries line from the mb-doc-check explainer

Items:

- **Item 10.** `doc-check-explainer.md` §2, §6. Finding: "A second file lists the folders a link may point into" (roots, deleted); opportunity "two dormant libraries" (done). Correction: Remove both.

### 3.3 — Clean the WSL path references

Items:

- **Item 12.** `wsl-path-references.md`. Finding: Lists `mb-doc-check.roots` and `log-row.sh` (both deleted); repeats the Cupcake enable/disable procedure with line numbers (duplicate of `cupcake-reference.md`). Correction: Remove deleted files; replace the procedure with a pointer.

### 3.4 — Remove the duplicated stop/restart procedure

Items:

- **Item 17.** `opencode-reset-management.md`. Finding: Repeats the stop/restart procedure held in `daily-ops.md`. Correction: Keep one; point from the other.

### 3.5 — Align the PDLF explainer with `/mb-close-out`

Items:

- **Item 6.** `pdlf-explainer.md` §1. Finding: Refers to the retired `close-out-process`. Correction: Refer to `/mb-close-out`.
- **Item 7.** `pdlf-explainer.md` §6 "Housekeeping" and §7B. Finding: Describes two separate end-of-step questions (commit and push; sync and embed). The orchestrator explainer now names `/mb-close-out` as end-of-step housekeeping. Correction: Align with `/mb-close-out` and commit all.

### 3.6 — Mark `/sync-gbrain` as not used here, in the dream-cycle configuration and GStack explainer

Items:

- **Item 22.** `gbrain-dream-cycle-config.md` (trigger surfaces), `gstack-explainer.md`. Finding: List `/sync-gbrain --dream` and `/sync-gbrain` as ways to run or update GBrain. The decision is that the dream cycle runs from the memory diagnostic and GBrain syncs through commit all. Correction: Mark these as not used in this environment.

### 3.7 — Update the mb-submit-memory documents

Items:

- **Item 20.** `mb-submit-memory-explainer.md`, `mb-submit-memory-config.md`. Finding: Say the skill has no repository source copy ("sole copy"); the source now exists at `C:\mybizz\mb-submit-memory\mb-submit-memory.md`. Correction: Record the source and installed copies.
- **Item 31.** `memory-master-explainer.md` §9, `mb-submit-memory-explainer.md` §2. Finding: Describe the startup coupling as a live risk; the governor's permanent automatic start always starts it correctly, so the risk exists only for a manual start. Correction: Restate as handled by the automatic start.
- **Item 32.** `memory-master-explainer.md` §9, `mb-submit-memory-explainer.md` §2 and §6. Finding: Describe the default-source coupling as stopping every sync until reset by hand; `sync-gbrain.sh` now resets the default before every sync. Correction: Restate as self-correcting at every sync.

Steps:

1. Apply only the mb-submit-memory parts of items 31 and 32 here; their master-explainer parts belong to task 4.2.

### 3.8 — Update the memory diagnostic explainer

Items:

- **Item 21.** `mb-memory-system-diagnostic-explainer.md`. Finding: "Why the init-model check runs first" describes a contradiction about systemd that the PostgreSQL documents have since resolved; cites "62/62 RLS coverage" while the PostgreSQL configuration records 93/93. Correction: Restate as current; point to the configuration for counts.

### 3.9 — Update the mb-compile-rules explainer

*Depends on: task 1.4.*

Items:

- **Item 27.** `mb-compile-rules-explainer.md`. Finding: Open question that its two skill copies are kept in step by nothing; "19 source documents" is a fixed count. Correction: Verify; point to the configuration for counts.

### 3.10 — Update the Graphify explainer

*Depends on: task 1.4.*

Items:

- **Item 29.** `graphify-explainer.md`. Finding: States mb-3-cs is paused and gives installed/upstream versions; both may have changed. Correction: Verify; point to the configuration for versions.

### 3.11 — Update the configuration-management explainer

*Depends on: task 1.4.*

Items:

- **Item 26.** `config-manager-explainer.md`. Finding: Says the orchestrator's "draft lives here; it moves to its install location when built" — current build state of the orchestrator is unclear. Correction: Verify and state current state.

### 3.12 — Apply the sysdoc-creator decisions

*Depends on: task 1.6.*

Items:

- **Item 28.** `sysdoc-creator-explainer.md`. Finding: Open items: missing skill-index register entry; file-name prefix differs from folder name. Correction: Resolve or record as decided.

### 3.13 — Apply the mb-3-cs figures decision

*Depends on: task 1.3.*

Items:

- **Item 33.** `positioning-strategy.md`, `ceo-review-v2-roadmap-2026-06-26.md` (mb-3-cs). Finding: Disagree on the size of the design: 36 data tables in one, 43 tables and 41 ADRs in the other. Both predate PDLF. Correction: Mark the mb-3-cs product documents as pre-PDLF, or point to one current figure.

---

## Section 4 — Larger rewrites

### 4.1 — Rewrite the environment explainer

*Depends on: task 1.1.*

Items:

- **Item 1.** `environment-explainer.md` (both copies). Finding: Names `memory-functionality-audit.md` as the health procedure (§2, §9 rule 5, §10); that document no longer exists. The memory health check is `mb-memory-system-diagnostic`. Correction: Replace with `mb-memory-system-diagnostic`.
- **Item 2.** `environment-explainer.md` (both copies). Finding: History lines: "Created 2026-09-09 from the Sentinel scoping side conversation"; "verified live 2026-09-08/09"; "reactivated 2026-09-08"; a fixed count "54 documents". Correction: Restate as current state; point to the library for counts.

Steps:

1. Apply items 1 and 2 to the copy kept in task 1.1.
2. Replace the other copy's location with a pointer to the kept one (item 3).

### 4.2 — Update the master memory explainer

*Depends on: task 1.2.*

Items:

- **Item 4.** `memory-master-explainer.md`. Finding: Treats `memory-functionality-audit.md` as the ecosystem's outside audit (§1, §8 "run the audit", companion line); the document no longer exists. Correction: Name `mb-memory-system-diagnostic` as the health check.
- **Item 5.** `memory-master-explainer.md` §11. Finding: "Maintenance rule": every memory-component session updates this document at close-out. The close-out decision removed master-explainer updates from close-out. Correction: Reconcile the rule with `/mb-close-out`.
- **Item 31.** `memory-master-explainer.md` §9, `mb-submit-memory-explainer.md` §2. Finding: Describe the startup coupling as a live risk; the governor's permanent automatic start always starts it correctly, so the risk exists only for a manual start. Correction: Restate as handled by the automatic start.
- **Item 32.** `memory-master-explainer.md` §9, `mb-submit-memory-explainer.md` §2 and §6. Finding: Describe the default-source coupling as stopping every sync until reset by hand; `sync-gbrain.sh` now resets the default before every sync. Correction: Restate as self-correcting at every sync.

Steps:

1. Replace the memory-functionality audit with `mb-memory-system-diagnostic` (item 4).
2. Apply the maintenance-rule decision (item 5).
3. Restate the startup and default-source couplings as handled (master-explainer parts of items 31 and 32).

### 4.3 — Rewrite the PostgreSQL backup section for the Sunday task

Items:

- **Item 30.** `postgresql-config.md` (backups). Finding: Instance A "Retention" and "Latest completed cycle" lines describe the old manual cycle; the Sunday task now runs both instances. Correction: Update the backup section to the scheduled cycle.

---

## Section 5 — Done

- **Item 34.** The global `AGENTS.md` close-out, past-session and fact routines: replaced with `/mb-close-out`, topic-based session search, and the fact procedure, outside GStack's managed block. Done 2026-10-07.
- **Item 36 (file part).** The session-numbers fact file is deleted and committed. The GBrain part is task 2.1.

---

## Completeness check

Every item from version 1 appears above: items 1–33 and 35–39 in sections 1 to 4, item 34 and part of item 36 in section 5.
