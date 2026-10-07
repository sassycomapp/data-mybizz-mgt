---
title: "documentation-anomalies-task-list"
doc-id: "mb-9d553253"
updated: "2026-10-07"
---
# Documentation Anomalies — Task List

Found while drafting `mybizz-os-explainer.md`. Out of scope for that task; to be addressed later. No item here has been changed.

| # | Document | Finding | Proposed correction |
|---|---|---|---|
| 1 | `environment-explainer.md` (both copies) | Names `memory-functionality-audit.md` as the health procedure (§2, §9 rule 5, §10); that document no longer exists. The memory health check is `mb-memory-system-diagnostic`. | Replace with `mb-memory-system-diagnostic`. |
| 2 | `environment-explainer.md` (both copies) | History lines: "Created 2026-09-09 from the Sentinel scoping side conversation"; "verified live 2026-09-08/09"; "reactivated 2026-09-08"; a fixed count "54 documents". | Restate as current state; point to the library for counts. |
| 3 | `mybizz-os-docs\os-reference-docs\environment-explainer.md` | Now a copy of the PDLF version, so it says "this document in the PDLF library" while living in `mybizz-os-docs`. Two copies of one document exist. | Decide one home; point the other location to it. |
| 4 | `memory-master-explainer.md` | Treats `memory-functionality-audit.md` as the ecosystem's outside audit (§1, §8 "run the audit", companion line); the document no longer exists. | Name `mb-memory-system-diagnostic` as the health check. |
| 5 | `memory-master-explainer.md` §11 | "Maintenance rule": every memory-component session updates this document at close-out. The close-out decision removed master-explainer updates from close-out. | Reconcile the rule with `/mb-close-out`. |
| 6 | `pdlf-explainer.md` §1 | Refers to the retired `close-out-process`. | Refer to `/mb-close-out`. |
| 7 | `pdlf-explainer.md` §6 "Housekeeping" and §7B | Describes two separate end-of-step questions (commit and push; sync and embed). The orchestrator explainer now names `/mb-close-out` as end-of-step housekeeping. | Align with `/mb-close-out` and commit all. |
| 8 | `documentation-linking-explainer.md` §2, §5 | Mentions `mb-doc-check.roots`, which is deleted, including in "Adding a repository". | Remove; `mb-doc-check.sources` is the single list. |
| 9 | `documentation-linking-explainer.md` §7 | Opportunity "bringing the two dormant libraries" — already done. | Remove. |
| 10 | `doc-check-explainer.md` §2, §6 | "A second file lists the folders a link may point into" (roots, deleted); opportunity "two dormant libraries" (done). | Remove both. |
| 11 | `commit-all-repositories.md` | Tools table lists `.roots`. | Remove `.roots`. |
| 12 | `wsl-path-references.md` | Lists `mb-doc-check.roots` and `log-row.sh` (both deleted); repeats the Cupcake enable/disable procedure with line numbers (duplicate of `cupcake-reference.md`). | Remove deleted files; replace the procedure with a pointer. |
| 13 | `daily-ops.md` | "TEST mb-doc-check" says 143 tests; `doc-check-config.md` says 149. | Point to the configuration for the number. |
| 14 | `daily-ops.md` | Cross-references to sections that no longer exist: "see Fix below" (GBrain test), "see AFTER DOING WORK above" (sync_freshness fix). | Point to the current sections. |
| 15 | `daily-ops.md` | "MCP / GBrain not responding" restarts OpenCode from the makePDLF folder; the start procedure starts without a folder. | Align with section 1. |
| 16 | `daily-ops.md` | Grant section carries a history note "(verified 2026-09-11)". | Remove the date. |
| 17 | `opencode-reset-management.md` | Repeats the stop/restart procedure held in `daily-ops.md`. | Keep one; point from the other. |
| 18 | `project-docs-explainer.md` | Open question says mb4ecom and mb5pdlf are not under the commit hook; they are. | Remove. |
| 19 | `project-docs-reference.md`, `project-docs-config.md` | Say the close-out procedure invokes the skill at "Step 2a"; in `/mb-close-out` it is Step 3. | Update the step reference. |
| 20 | `mb-submit-memory-explainer.md`, `mb-submit-memory-config.md` | Say the skill has no repository source copy ("sole copy"); the source now exists at `C:\mybizz\mb-submit-memory\mb-submit-memory.md`. | Record the source and installed copies. |
| 21 | `mb-memory-system-diagnostic-explainer.md` | "Why the init-model check runs first" describes a contradiction about systemd that the PostgreSQL documents have since resolved; cites "62/62 RLS coverage" while the PostgreSQL configuration records 93/93. | Restate as current; point to the configuration for counts. |
| 22 | `gbrain-dream-cycle-config.md` (trigger surfaces), `gstack-explainer.md` | List `/sync-gbrain --dream` and `/sync-gbrain` as ways to run or update GBrain. The decision is that the dream cycle runs from the memory diagnostic and GBrain syncs through commit all. | Mark these as not used in this environment. |
| 23 | `repo-organization.md` | "Verified against gbrain sources list (22 sources)"; `mb-close-out` added a source. | Remove the count or update it. |
| 24 | `frontmatter conventions.md` | "Awaiting re-certification by the developer." | Re-certify or remove the note. |
| 25 | `mybizz-scope-list.md` | Notes mention only mb4ecom as an in-scope placeholder; `C:\dev\project-template` is listed twice (private data, and disposable/template). | Mention mb5pdlf; list the template once. |
| 26 | `config-manager-explainer.md` | Says the orchestrator's "draft lives here; it moves to its install location when built" — current build state of the orchestrator is unclear. | Verify and state current state. |
| 27 | `mb-compile-rules-explainer.md` | Open question that its two skill copies are kept in step by nothing; "19 source documents" is a fixed count. | Verify; point to the configuration for counts. |
| 28 | `sysdoc-creator-explainer.md` | Open items: missing skill-index register entry; file-name prefix differs from folder name. | Resolve or record as decided. |
| 29 | `graphify-explainer.md` | States mb-3-cs is paused and gives installed/upstream versions; both may have changed. | Verify; point to the configuration for versions. |
| 30 | `postgresql-config.md` (backups) | Instance A "Retention" and "Latest completed cycle" lines describe the old manual cycle; the Sunday task now runs both instances. | Update the backup section to the scheduled cycle. |
| 31 | `memory-master-explainer.md` §9, `mb-submit-memory-explainer.md` §2 | Describe the startup coupling as a live risk; the governor's permanent automatic start always starts it correctly, so the risk exists only for a manual start. | Restate as handled by the automatic start. |
| 32 | `memory-master-explainer.md` §9, `mb-submit-memory-explainer.md` §2 and §6 | Describe the default-source coupling as stopping every sync until reset by hand; `sync-gbrain.sh` now resets the default before every sync. | Restate as self-correcting at every sync. |
| 33 | `positioning-strategy.md`, `ceo-review-v2-roadmap-2026-06-26.md` (mb-3-cs) | Disagree on the size of the design: 36 data tables in one, 43 tables and 41 ADRs in the other. Both predate PDLF. | Mark the mb-3-cs product documents as pre-PDLF, or point to one current figure. |
| 34 | `~/.config/opencode/AGENTS.md` (global; Windows: `\\wsl.localhost\Ubuntu\home\dev-p\.config\opencode\AGENTS.md`), lines ~342–361 | **Priority: agents read this file in every session.** Its close-out routine adds a row to the sessions log; its "open session NNN" reads the sessions log; its fact-save routine calls the facts log "the authoritative index" and adds a row per fact. Both logs are retired, and the routine contradicts `/mb-close-out`. | Replace the three passages with: close out by `/mb-close-out`; open a past session by "open the last session about <topic>" (GBrain search of `sessions/` pages); facts are saved and recalled per `fact-save-and-recall.md`. Developer-run edit. |
| 35 | `C:\data-mybizz-mgt\README.md`, lines 30–33 | Describes both logs as current, with their locations. | Remove the two entries. |
| 36 | `C:\mybizz\mybizz-config-docs\facts\2026-09-15-session-numbers-from-sessions-log.md` (a governed fact) | States that session numbers come from the sessions log. Session numbers no longer exist: `/mb-close-out` names each page `sessions/<YYYY-MM-DD>-<short-slug>`, and past sessions are found by topic, not number. Existing numbered pages keep their names. | Retire the fact (not rewrite it): expire it in GBrain by its fact number, and delete the fact file. |
| 37 | `C:\dev\dev-root\docmap.md`, line 31 | Folder-tree row for `sessions-log/`, a folder that no longer exists. | Run `build-docmap.py --write`, which removes entries that no longer exist, then commit all. |
| 38 | `~/.config/opencode/AGENTS.md`, inside GStack's managed block | Tells agents to "Run `/sync-gbrain` after meaningful code changes"; GBrain is synced by commit all. The block is rewritten by GStack, so an edit inside it may not last. | Add a rule outside the block that GBrain is synced only by commit all, overriding the block's line. |
| 39 | `~/.config/opencode/AGENTS.md`, "Facts across documents" | Says "the eight documentation repositories". | Replace with "the documentation repositories on the commit-all list". |
