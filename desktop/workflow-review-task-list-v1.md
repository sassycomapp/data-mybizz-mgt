---
title: "workflow-review-task-list-v1"
doc-id: "mb-73daefb5"
updated: "2026-10-07"
---
# Workflow Review — Task List

Version 1 — 2026-10-06. Updated and returned with every exchange.

Status: **Decided** · **Research** (Claude) · **Open** (David to decide) · **Done**

---

## 0. Working rules for this task

| #   | Rule                                                                                                     |
| --- | -------------------------------------------------------------------------------------------------------- |
| 0.1 | Conversation only until David and Claude are of one mind. No terminal commands, no OpenCode prompts.     |
| 0.2 | Every document move or change is proposed to David first, never sent straight to OpenCode.               |
| 0.3 | Research before conclusions. No assumptions. Every statement says whether it is verified, and from what. |
| 0.4 | This list is the single record. Updated every exchange. No narrative, no meta talk.                      |
| 0.5 | Every one of David's stated preferences is recorded here.                                                |
| 0.6 | All document names are lowercase kebab-case.                                                             |
| 0.7 | Out of scope: ASUS, Edge and Realtek scheduled tasks.                                                    |
| 0.8 | Separate later task: backup redesign, Google Drive sync, Google Calendar setup.                          |

---

## 1. daily-ops

| #   | Item                                                                                                                                              | Status  | Feedback                          |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | --------------------------------- |
| 1.1 | daily-ops becomes David's personal manual, ordered by when it is needed: start a session, finish a session, weekly duties, when something breaks. | Decided | Agreed                            |
| 1.2 | Tool installation details (i-have-adhd, Cupcake, AI provider table) move to each tool's own documents. Each move proposed to David first.         | Decided | ask David For paths when required |
| 1.3 | daily-ops holds no reminders. Reminders live in Google Calendar, with an alarm.                                                                   | Decided | Agreed                            |
| 1.4 | Remove the GBrain "WASM error" fix.                                                                                                               | Decided | Agreed                            |
| 1.5 | Update or remove the GStack GBrain material: `/sync-gbrain`, `/setup-gbrain`, the "no allowlisted changes" fix.                                   | Decided | Agreed                            |
| 1.6 | Template: `C:\dev\project-template`, applied by hand when required. No GitHub repository `template-project-library`.                              | Decided | Agreed                            |
| 1.7 | Starting OpenCode: `opencode web --hostname 0.0.0.0`, then choose the project inside OpenCode.                                                    | Decided | Agreed                            |
| 1.8 | Remove `/context-save` and `/context-restore`. GStack extras, not part of David's design.                                                         | Decided | Agreed                            |
| 1.9 | daily-ops is rewritten last, after sections 2–6 are settled.                                                                                      | Decided | Agreed                            |

---

## 2. Close-out and commit

| #    | Item                                                                                                                                                                                                                                                                                        | Status   | Feedback                                                                                                           |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------ |
| 2.1  | Two named processes only: **commit all** and **close out**.                                                                                                                                                                                                                                 | Decided  | Agreed                                                                                                             |
| 2.2  | **commit all**: runs through every repository, stages, commits, updates GBrain, pushes. Unrelated to closing out.                                                                                                                                                                           | Decided  | Updates G brain means sync-gbrain.sh                                                                               |
| 2.3  | **close out**: David says "close out" and nothing else. It closes the session and the task, saves everything that must be saved (GBrain, governed memory through the memory governor and `mb-submit-memory`, project documents), processes the governor review queue, then runs commit all. | Decided  | Agreed But provide a definitive list of tasks. Must include MB-do-check (Critical)                                 |
| 2.4  | Prefer one close-out orchestrator over existing scripts and skills. Rewrite only where research shows it is needed.                                                                                                                                                                         | Decided  | The close-out orchestrator executes the existing scripts and skillsIt does not replace them                        |
| 2.5  | Close out after every makePDLF step conclusion.                                                                                                                                                                                                                                             | Decided  | Agreed in principle, but close out is on demand only not automated at the end of a session                         |
| 2.6  | Governor review queue processed at every close-out.                                                                                                                                                                                                                                         | Decided  | Agreed                                                                                                             |
| 2.7  | Close-out for PDLF running real steps is a separate matter for the PDLF layer, later.                                                                                                                                                                                                       | Decided  | Close out can be requested by the developer at any time, whether that be in makePDLF, PDLF or an open code session |
| 2.8  | Map what exists today: `close-out-process.md`, `opening-and-closing.md`, `commit-all.sh`, `log-row.sh`, `agents-from-reference.sh`, `mb-project-docs`, `mb-submit-memory`, governor review. Separate the working method from leftovers.                                                     | Research | Awaiting Claude's response                                                                                         |
| 2.9  | sessions-log and facts-log: real value or ceremony. Verified: both last written 2026-09-23; facts-log rows use a different format from `log-row.sh`.                                                                                                                                        | Research | Awaiting Claude's response                                                                                         |
| 2.10 | "open session NNN": still in use or a leftover. Depends on 2.9.                                                                                                                                                                                                                             | Research | Dependent upon research based on 2.9                                                                               |

---

## 3. Sunday maintenance

| #   | Item                                                                                                                                                                                                        | Status   | Feedback                                                                                                                                                                                                                                                                                                                                                                                                           |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 3.1 | One Sunday Task Scheduler task, 12:00 noon: database backup cycle (both PostgreSQL instances), then GBrain export, one after the other.                                                                     | Decided  | Time is dependent upon the definitive list of proposed tasks                                                                                                                                                                                                                                                                                                                                                       |
| 3.2 | Reminder Sunday 10:00 AM that the task will run (Google Calendar alarm).                                                                                                                                    | Decided  | Cancel the alarm But add the decided list of Sunday maintenance tasks to the calendar                                                                                                                                                                                                                                                                                                                              |
| 3.3 | Memory audit weekly on Sunday, after the backup task, never at the same time. Reminder by notification.                                                                                                     | Decided  | Time is dependent upon the definitive list of proposed tasks. Add the decided list of Sunday maintenance tasks to the calendar                                                                                                                                                                                                                                                                                     |
| 3.4 | Configuration exams: Google Calendar entry, done on perceived drift or substantial system change. Not scheduled.                                                                                            | Decided  | Add to task list on Google Calendar                                                                                                                                                                                                                                                                                                                                                                                |
| 3.5 | GBrain dream cycle: never runs by itself. David gets a reminder to run it.                                                                                                                                  | Decided  | To Sunday maintenance list                                                                                                                                                                                                                                                                                                                                                                                         |
| 3.6 | Dream cycle frequency for the reminder.                                                                                                                                                                     | Open     | No separate reminder, simply add to Sunday maintenance list<br/>I think that as Sunday is the maintenance day, I should get a reminder on Sunday morning at nine a.m. And the reminder of the dream cycle should be included in that reminder. So that reminder should maybe list everything that needs to be done on maintenance day in order of execution and include the dream cycle as a note in that reminder |
| 3.7 | Where the dream cycle runs today. Verified absent from: `sync-gbrain.sh`, `commit-all.sh`, `close-out-process.md`, Task Scheduler. Not yet checked: WSL cron, WSL systemd timers, OpenCode plugins, skills. | Research | Awaiting Claude's response                                                                                                                                                                                                                                                                                                                                                                                         |
| 3.8 | The recorded decision "nothing gbrain-related is scheduled": keep or change for the backup task. Recommendation to follow.                                                                                  | Research | Strike this from known decisions                                                                                                                                                                                                                                                                                                                                                                                   |

---

## 4. Task Scheduler and backups

| #   | Item                                                                                                                                                                                       | Status  | Feedback                                |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | --------------------------------------- |
| 4.1 | Remove the `mb-doc-maintainer` logon task.                                                                                                                                                 | Decided | Areed                                   |
| 4.2 | Removed systems, replaced by `mb-doc-check`: mb-doc-maintainer, mb-doc-auditor, mb-align-docs, mb-wikilinks, mb-doc-manager, mb-doccycle. Any remaining references to them are cleaned up. | Decided | Agreed                                  |
| 4.3 | DailyDevBackup stays, runs daily, keeps 7 days.                                                                                                                                            | Decided | Comprehensive backup plan to be decided |
| 4.4 | OpenCodeSessionPrune stays, runs daily; its own backups keep 7 days.                                                                                                                       | Decided | Agreed                                  |
| 4.5 | Backup purpose: loss of the whole machine. Content on GitHub is not backed up to disk; everything not on GitHub is. Detailed redesign belongs to the later task (0.8).                     | Decided | Comprehensive backup plan to be decided |

---

## 5. Other documents and settings

| #   | Item                                                                                                                                                                                                                                                                                                                                      | Status   | Feedback                   |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | -------------------------- |
| 5.1 | Keep `pdlf-explainer`; retire `pdlf-system-explainer`. Verified: identical apart from five step-file links and formatting.                                                                                                                                                                                                                | Decided  | Agreed                     |
| 5.2 | Update the environment explainer.                                                                                                                                                                                                                                                                                                         | Decided  | Explain what update        |
| 5.3 | Remove `update-docs.py`.                                                                                                                                                                                                                                                                                                                  | Decided  | Agreed                     |
| 5.4 | Linking coverage: which repositories are documentation repositories, and whether the commit hook, `commit-all.sh`, `mb-doc-check.roots`, `mb-doc-check.sources` and the linking explainer agree. Verified so far: `commit-all.sh` header says "eight" but lists fifteen; `roots` lists eight; `sources` lists fifteen. No conclusion yet. | Research | Awaiting Claude's response |
| 5.5 | mb4ecom and mb5pdlf: live projects, registered GBrain sources and GitHub repositories, in scope although empty. Removed from the scope list's exceptions.                                                                                                                                                                                 | Decided  | Agreed                     |
| 5.6 | mb4ecom and mb5pdlf READMEs state each project's placeholder purpose.                                                                                                                                                                                                                                                                     | Decided  | Agreed                     |
| 5.7 | mb4ecom and mb5pdlf project libraries brought under `commit-all.sh` and the commit hook, consistent with 5.5.                                                                                                                                                                                                                             | Open     | Agreed<br/>Yes             |

---

## 6. Files Claude still needs

| #   | File                                                                                           | For | Files sent |
| --- | ---------------------------------------------------------------------------------------------- | --- | ---------- |
| 6.1 | `mb-project-docs.md` (skill source, `C:\mybizz\mb-project-docs\`)                              | 2.8 | 4          |
| 6.2 | `mb-submit-memory.md` (skill source, `C:\mybizz\mb-submit-memory\`)                            | 2.8 | 4          |
| 6.3 | `rollout-repo.sh`                                                                              | 5.4 | 2          |
| 6.4 | `doc-check-config.md`, `doc-check-explainer.md` (`C:\mybizz\mybizz-config-docs\mb-doc-check\`) | 5.4 | 3          |
| 6.5 | `gbrain-dream-cycle-config.md` (`C:\mybizz\mybizz-config-docs\gbrain-dream-cycle\`)            | 3.7 | 3          |

---

## 7. Order of execution

| Phase | Work                                                 |
| ----- | ---------------------------------------------------- |
| 1     | Research: 2.8, 2.9, 2.10, 3.7, 3.8, 5.4.             |
| 2     | David decides the Open items: 3.6, 5.7.              |
| 3     | Agree the close-out design (section 2).              |
| 4     | Task Scheduler changes: 4.1, 3.1, 4.3, 4.4.          |
| 5     | Document changes: 5.1, 5.2, 5.3, 5.5, 5.6, 5.7, 4.2. |
| 6     | Rewrite daily-ops (section 1).                       |

## Additional feedback

Google calendar: sassycomapp@gmail.com
