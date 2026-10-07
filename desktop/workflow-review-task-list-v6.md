---
title: "workflow-review-task-list-v6"
doc-id: "mb-010d1cb0"
updated: "2026-10-07"
---
# Workflow Review — Task List

Version 6 — 2026-10-06. Version 5 reorganised for execution. Nothing added, nothing removed.

Order: Section 1 holds the quick kills and the dependencies. Sections 2 to 6 run from quickest to most complex; every dependency of a task is finished in an earlier section. Version 5 item numbers are given in brackets.

---

## Section 1 — Quick kills and dependencies

### Task 1.1 — Execution checks (dependency for 6.1)
1. Confirm `memory-functionality-audit.md` is absent from `C:\mybizz\mybizz-os-docs`. [E1, 3.10]
2. Confirm no WSL scheduled job or timer runs the dream cycle. [E2, 3.8]
3. Report both results to David.

### Task 1.2 — Remove the `mb-doc-maintainer` scheduled task
1. Delete the logon task `mb-doc-maintainer` from Task Scheduler. [4.1]
2. Confirm it no longer appears in the Task Scheduler Library.

### Task 1.3 — Remove `update-docs.py`
1. Delete `update-docs.py` from `C:\mybizz\scripts`. [5.4]

### Task 1.4 — Delete `mb-doc-check.roots` (dependency for 3.3)
1. Delete `C:\mybizz\scripts\mb-doc-check.roots`. `mb-doc-check.sources` becomes the single list. [5.6]
2. Run `mb-doc-check.py check` on one repository and confirm it reports normally.

### Task 1.5 — Retire `pdlf-system-explainer`
1. Retire `pdlf-system-explainer.md`; `pdlf-explainer.md` is the one kept. [5.1]
2. Commit all.

### Task 1.6 — Replace the environment explainer in `mybizz-os-docs`
1. Save `C:\pdlf\pdlf-library\pdlf-explainer-docs\pdlf-environment-explainer.md` over `C:\mybizz\mybizz-os-docs\os-reference-docs\environment-explainer.md`. [5.3]
2. Keep the existing frontmatter of `environment-explainer.md` (its `doc-id` never changes).
3. Commit all.

### Task 1.7 — Retire the sessions-log and facts-log (dependency for 5.1)
1. Retire `C:\mybizz\logs\sessions-log\sessions-log.md`. [2.14]
2. Retire `C:\mybizz\logs\gbrain-logs\facts-log\facts-log.md`. [2.14]
3. Delete `C:\mybizz\scripts\log-row.sh`. [2.14]

### Task 1.8 — Clean `mb-submit-memory.md` (dependency for 5.1)
1. Remove the references to the retired Docs Manager and mb-wikilinks. [2.16]
2. Copy the cleaned source over the installed `SKILL.md`, keeping the installed frontmatter.
3. Commit all.

### Task 1.9 — Align two PDLF documents
1. `pdlf-objective-review.md`: name commit all (`sync-gbrain.sh`) as the GBrain sync, not `/sync-gbrain`. [5.12]
2. `pdlf-expl-orchestrator-agent.md`: end-of-step housekeeping is `/mb-close-out`, run after every makePDLF step and, once PDLF runs, after every PDLF step. [5.13, 2.5]
3. Commit all.

---

## Section 2 — Small tasks

### Task 2.1 — OpenCodeSessionPrune keeps 7 days of backups
1. Add a retention step to `opencode-session-prune.sh`: keep the last 7 days of folders in `C:\backup-wsl\opencode-session-prune\`, delete older ones. [4.4]
2. Run the script once by hand and confirm the result.
3. The task keeps its daily schedule.

### Task 2.2 — Google Calendar entries (account sassycomapp@gmail.com)
1. Cancel the separate 10:00 alarm. [3.2]
2. Create a weekly event, Sunday 09:00, listing in order: the 10:00 backup task; then `/mb-memory-system-diagnostic`, answering yes to the dream cycle at its end. [3.1, 3.4]
3. Create a task-list entry: configuration exams, to be run on perceived drift or substantial system change. [3.7]

---

## Section 3 — Medium tasks

### Task 3.1 — Bring mb4ecom and mb5pdlf into scope (dependency for 3.3)
1. Remove `C:\dev\dev-mb4ecom` and `C:\dev\dev-mb5pdlf` from the exceptions in `mybizz-scope-list.md`. [5.9]
2. Write each project library's README: what the project is for and that it is an unscoped placeholder. mb4ecom: a future project modelled largely on mb-3-cs. mb5pdlf: the future test project for makePDLF and PDLF. [5.10]
3. Add both project libraries to `commit-all.sh` and to `mb-doc-check.sources`. [5.11]
4. Install the commit hook in both. [5.11]
5. Run `rollout-repo.sh` once on each. [5.11]
6. Update `repo-organization.md` and `commit-all-repositories.md`. [5.11]
7. Close the matching open items in `doc-check-config.md` and `project-docs-config.md`. [5.11]
8. Commit all; confirm "All done" and no hook warning.

### Task 3.2 — Remove references to the retired documentation systems
1. Search the documentation repositories for: mb-doc-maintainer, mb-doc-auditor, mb-align-docs, mb-wikilinks, mb-doc-manager, mb-doccycle. [4.2]
2. Present the list of references to David.
3. Remove or rewrite each approved reference.
4. Commit all.

### Task 3.3 — Commit-all wording without counts (needs 1.4 and 3.1)
1. `commit-all.sh`: the header comment says it commits every repository on its list, with no count. [5.7]
2. `doc-check-config.md`: remove the `roots` row; the `sources` row states no count. [5.6, 5.7]
3. `documentation-linking-explainer.md`: replace "the eight" with "the repositories on the commit-all list". [5.7]
4. `commit-all-repositories.md` and `repo-organization.md`: replace "fifteen" with the same wording. [5.7]
5. Record the rule in `commit-all-repositories.md`: the list holds every documentation repository; Anvil code repositories, the memory governor's code and the Anvil reference clone stay off it, with the reasons. [5.7]
6. Commit all.

---

## Section 4 — Complex tasks

### Task 4.1 — The Sunday backup task
1. Write one script that runs, in order: the PostgreSQL backup cycle (both instances, five databases, both locations, hash-checked, two cycles kept), then `gbrain export` to `C:\backup-dream-cycle`. [3.3]
2. Give the PDLF ledger backup its password through a local password file, never through the agent.
3. Run the script once by hand; confirm every dump and the export.
4. Create the Task Scheduler task: Sunday 10:00, no catch-up after a missed start. [3.3, 4.6]
5. Update the PostgreSQL documents: the backups are scheduled; the decision "nothing gbrain-related is scheduled" is struck. [3.9]
6. Commit all.

### Task 4.2 — Missed-run report (needs 4.1)
1. Write one check that runs at logon. It looks at DailyDevBackup, OpenCodeSessionPrune and the Sunday backup task. [4.7]
2. If a task is overdue, or its last run did not finish, the check shows a Windows notification naming it. [4.6, 4.7]
3. Create the logon task in Task Scheduler.
4. Test it once with a deliberately overdue task.

---

## Section 5 — Most complex task

### Task 5.1 — Build the close-out skill `/mb-close-out` (needs 1.7 and 1.8)
1. Write the skill source from `close-out-process.md`, following the same pattern as the seven skill-source repositories. [2.11]
2. The skill runs these steps in order [2.8.1–2.8.12]:
   1. Write the session page in GBrain (`sessions/` page).
   2. List candidate facts; route each as advisory or governed.
   3. Run `/mb-project-docs` when in one of the five projects.
   4. List changed files with `commit-all.sh --status`.
   5. Present one approval gate: facts, routing, changed files, project-document changes.
   6. Save advisory facts with `remember`.
   7. Submit governed facts through `mb-submit-memory`, exactly as it works today. [2.12]
   8. Hand David one terminal block: the `AGENTS.md` copy line, then commit all.
   9. Stop on any "hook is not installed" warning.
   10. Hand David a second block only when governed facts landed in review: promote them.
   11. Verify and report: "All done", no hook warnings, review queue empty, fact numbers.
3. The skill never commits, pushes or uses credentials. [2.13]
4. The skill writes nothing to the sessions-log or facts-log. [2.14]
5. Install the skill and confirm OpenCode lists it.
6. Run `/mb-close-out` once on a real session and confirm every step.
7. Point `opening-and-closing.md` and `fact-save-and-recall.md` to the skill. [2.10]
8. In `opening-and-closing.md`, replace "open session NNN" with "open the last session about <topic>", found by GBrain search of `sessions/` pages. [2.15]
9. Retire `close-out-process.md` once the skill is proven.
10. Commit all.

---

## Section 6 — Final task

### Task 6.1 — Rewrite daily-ops (needs every task above)
1. Ask David for the destination path of each tool detail to be moved. [1.2]
2. Move the i-have-adhd, Cupcake and AI provider material to those documents. [1.2]
3. Remove: the GBrain "WASM error" fix; `/sync-gbrain`, `/setup-gbrain` and the "no allowlisted changes" fix; `/context-save` and `/context-restore`. [1.4, 1.5, 1.8]
4. Write the manual in this order [1.1]:
   1. Start a session: `opencode web --hostname 0.0.0.0`, then choose the project in OpenCode. [1.7]
   2. Finish a session: run `/mb-close-out`. [1.9]
   3. Commit all, outside a close-out: `commit-all.sh`. [2.2]
   4. Sunday maintenance: the 10:00 backup task runs by itself; then run `/mb-memory-system-diagnostic` and answer yes to the dream cycle at its end. [1.10, 3.4, 3.6]
   5. When something breaks: pointers to the reference documents.
   6. Template projects: `C:\dev\project-template`, applied by hand. [1.6]
5. No reminders in daily-ops. [1.3]
6. Present the draft to David; apply corrections.
7. Commit all.

---

## Appendix A — Working rules

1. Conversation only until David and Claude are of one mind. No terminal commands, no OpenCode prompts. [0.1]
2. Every document move or change is proposed to David first. [0.2]
3. Research before conclusions; every statement says whether it is verified, and from what. [0.3]
4. This list is the single record, updated every exchange, with no narrative. [0.4]
5. Every one of David's stated preferences is recorded here. [0.5]
6. All document names are lowercase kebab-case. [0.6]
7. Out of scope: ASUS, Edge and Realtek scheduled tasks. [0.7]
8. Separate later task: comprehensive backup plan (including DailyDevBackup content and retention), Google Drive sync, Google Calendar setup. [0.8, 4.3, 4.5]
9. Ask David for destination paths whenever a move needs one. [0.10]
10. No further scope is added to this task. [0.11]

## Appendix B — Standing decisions

1. Two named processes only: commit all and close out. [2.1]
2. Commit all = `commit-all.sh`: commits every repository on its list (the `mb-doc-check` hook runs inside every commit), updates GBrain with `sync-gbrain.sh`, pushes. [2.2]
3. Close out closes the session and the task, saves what must be saved, processes the governor review queue, and runs commit all. [2.3, 2.6]
4. The close-out executes the existing scripts and skills; it does not replace them. [2.4]
5. Close out is on demand only, at any time, in any layer. [2.5, 2.7]
6. The dream cycle never runs by itself; it is run from the memory diagnostic, not with `/sync-gbrain --dream`. [3.6, 3.8]
7. A scheduled task never catches up after a missed start; missed runs are reported. [4.6]
8. Backup purpose: loss of the whole machine; content on GitHub is not backed up to disk. [4.5]
9. DailyDevBackup and OpenCodeSessionPrune keep running daily. [4.3, 4.4]

## Appendix C — Verified facts

1. The close-out method is `close-out-process.md` (2026-10-04). [2.9]
2. `mb-submit-memory` is the governed path, per the master memory explainer. [2.12]
3. The memory audit is `/mb-memory-system-diagnostic`. [3.10]
4. The documentation repositories are fifteen: eight libraries and seven skill-source repositories. [5.5]
5. The commit hook is installed in all fifteen (commit-all log, 2026-10-06 09:44). [5.8]

## Appendix D — Struck

1. Master-explainer update as part of close-out: out of scope. [2.8.5]
2. Environment explainer history lines and dated counts: superseded by Task 1.6. [5.2]
3. History paragraph in `pdlf-expl-artifact-lifecycle.md`: out of scope. [5.14]
