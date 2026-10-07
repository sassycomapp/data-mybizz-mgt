---
title: "workflow-review-task-list-v2"
doc-id: "mb-d7fd1dda"
updated: "2026-10-07"
---
# Workflow Review — Task List

Version 2 — 2026-10-06. Updated and returned with every exchange.

Status: **Decided** · **Proposed** (Claude, awaiting David) · **Open** (David to decide) · **Research** (Claude) · **Struck** · **Done**

---

## 0. Working rules for this task

| #    | Rule                                                                                                     | Status  | David's feedback |
| ---- | -------------------------------------------------------------------------------------------------------- | ------- | ---------------- |
| 0.1  | Conversation only until David and Claude are of one mind. No terminal commands, no OpenCode prompts.     | Decided | Decided          |
| 0.2  | Every document move or change is proposed to David first, never sent straight to OpenCode.               | Decided | Decided          |
| 0.3  | Research before conclusions. No assumptions. Every statement says whether it is verified, and from what. | Decided | Decided          |
| 0.4  | This list is the single record. Updated every exchange. No narrative, no meta talk.                      | Decided | Decided          |
| 0.5  | Every one of David's stated preferences is recorded here.                                                | Decided | Decided          |
| 0.6  | All document names are lowercase kebab-case.                                                             | Decided | Decided          |
| 0.7  | Out of scope: ASUS, Edge and Realtek scheduled tasks.                                                    | Decided | Decided          |
| 0.8  | Separate later task: comprehensive backup plan, Google Drive sync, Google Calendar setup.                | Decided | Decided          |
| 0.9  | Google Calendar account: sassycomapp@gmail.com.                                                          | Decided | Decided          |
| 0.10 | Ask David for destination paths whenever a move needs one.                                               | Decided | Decided          |

---

## 1. daily-ops

| #   | Item                                                                                                                                              | Status  | David's feedback                  |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | --------------------------------- |
| 1.1 | daily-ops becomes David's personal manual, ordered by when it is needed: start a session, finish a session, weekly duties, when something breaks. | Decided | Decided                           |
| 1.2 | Tool installation details (i-have-adhd, Cupcake, AI provider table) move to each tool's own documents. Each move proposed to David first.         | Decided | Ask David for paths when required |
| 1.3 | daily-ops holds no reminders. Reminders live in Google Calendar.                                                                                  | Decided | Decided                           |
| 1.4 | Remove the GBrain "WASM error" fix.                                                                                                               | Decided | Decided                           |
| 1.5 | Remove the GStack GBrain material: `/sync-gbrain`, `/setup-gbrain`, the "no allowlisted changes" fix.                                             | Decided | Decided                           |
| 1.6 | Template: `C:\dev\project-template`, applied by hand when required. No GitHub repository `template-project-library`.                              | Decided | Decided                           |
| 1.7 | Starting OpenCode: `opencode web --hostname 0.0.0.0`, then choose the project inside OpenCode.                                                    | Decided | Decided                           |
| 1.8 | Remove `/context-save` and `/context-restore`. GStack extras, not part of David's design.                                                         | Decided | Decided                           |
| 1.9 | daily-ops is rewritten last, after sections 2–5 are settled.                                                                                      | Decided | Decided                           |

---

## 2. Close-out and commit

### 2A. Decisions

| #   | Item                                                                                                                                                                                                          | Status  | David's feedback |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------- |
| 2.1 | Two named processes only: **commit all** and **close out**.                                                                                                                                                   | Decided | Decided          |
| 2.2 | **commit all** = `commit-all.sh`: commits every repository (the `mb-doc-check` hook runs inside every commit), updates GBrain with `sync-gbrain.sh`, pushes. Unrelated to closing out.                        | Decided | Decided          |
| 2.3 | **close out**: closes the session and the task; saves everything that must be saved; processes the governor review queue; runs commit all. Definitive task list in 2B. `mb-doc-check` is included (critical). | Decided | Decided          |
| 2.4 | The close-out orchestrator executes the existing scripts and skills. It does not replace them.                                                                                                                | Decided | Decided          |
| 2.5 | Close out is on demand only, never automated at the end of a session. Recommended after every makePDLF step conclusion.                                                                                       | Decided | Decided          |
| 2.6 | Governor review queue processed at every close-out.                                                                                                                                                           | Decided | Decided          |
| 2.7 | Close out can be requested at any time: in makePDLF, in PDLF, or in any OpenCode session.                                                                                                                     | Decided | Decided          |

### 2B. Definitive close-out task list (proposed)

| #      | Step                                                                                                             | Done by       | Existing piece it uses                      | Status       |
| ------ | ---------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------- | ------------ |
| 2.8.1  | Write the session page in GBrain (`sessions/` page).                                                             | Agent         | `close-out-process.md` Step 1               | Agreed       |
| 2.8.2  | List candidate facts; route each as advisory or governed.                                                        | Agent         | `close-out-process.md` Step 2               | Agreed       |
| 2.8.3  | Project documents, only when in one of the five projects.                                                        | Agent         | `/mb-project-docs`                          | Agreed       |
| 2.8.4  | List changed files.                                                                                              | Agent         | `commit-all.sh --status`                    | Agreed       |
| 2.8.5  | Update the memory master explainer, only when a memory component was touched.                                    | Agent         | `close-out-process.md` Step 3               | Out of scope |
| 2.8.6  | One approval gate: facts, routing, changed files, project-document changes.                                      | David         | `close-out-process.md` Step 2               | Agreed       |
| 2.8.7  | Save advisory facts.                                                                                             | Agent         | GBrain `remember`                           | Agreed       |
| 2.8.8  | Governed facts: fact files written, then submitted to the governor.                                              | Agent + David | See 2.12                                    | Agreed       |
| 2.8.9  | One terminal block: governed submissions, `AGENTS.md` copy line, master-explainer commit, commit all.            | David         | `agents-from-reference.sh`, `commit-all.sh` | Agreed       |
| 2.8.10 | Inside commit all: `mb-doc-check` runs at every commit; any "hook is not installed" warning stops the close-out. | Script        | `commit-all.sh`, `mb-doc-check.py`          | Agreed       |
| 2.8.11 | Second terminal block only when governed facts landed in review: promote them.                                   | David         | `close-out-process.md` Step 5               | Agreed       |
| 2.8.12 | Verify and report: commit summary "All done", no hook warnings, review queue empty, fact numbers.                | Agent         | `close-out-process.md` Step 6               | Agreed       |

### 2C. Research results

| #    | Item                                                                                                                                                                                                                                                                              | Status   | David's feedback                                                   |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------ |
| 2.9  | The working method is `close-out-process.md` (2026-10-04). Verified from the document.                                                                                                                                                                                            | Done     |                                                                    |
| 2.10 | The same close-out is described three more times: `opening-and-closing.md`, `fact-save-and-recall.md`, daily-ops. Proposal: one procedure; the others point to it.                                                                                                                | Proposed | Agreed                                                             |
| 2.11 | Today David must paste `close-out-process.md`; it is not an installed skill. Proposal: install it as one skill, `/mb-close-out`, so David says "close out" only.                                                                                                                  | Proposed | Agreed but run /mb-close-out                                       |
| 2.12 | Two governed-fact paths disagree: `close-out-process.md` submits by David's terminal block with visibility `shared_all`; `mb-submit-memory` submits by the agent with visibility `project_local`. Which one works live is not yet verified.                                       | Research | Awaiting response from Claude                                      |
| 2.13 | Saying "close out" alone is not achievable under David's own rules: the agent never commits, pushes or uses credentials. The minimum is: say "close out", approve once, paste one block (two when governed facts land in review).                                                 | Open     | Agreed but run /mb-close-out                                       |
| 2.14 | sessions-log and facts-log. Verified: both last written 2026-09-23; facts-log columns differ from what `log-row.sh` writes; both live in `C:\mybizz\logs`, outside every repository. Session pages and facts already live in GBrain. Proposal: retire both logs and `log-row.sh`. | Proposed | Are these logs only for ceremony, or do they add meaningful value? |
| 2.15 | "open session NNN" needs the sessions-log. Proposal: replace with "open the last session about <topic>", found by GBrain search of `sessions/` pages.                                                                                                                             | Proposed | This question goes together with 2.14                              |
| 2.16 | `mb-submit-memory.md` still names the removed Docs Manager and mb-wikilinks. Cleaned up under 4.2.                                                                                                                                                                                | Decided  | Needs to be updated                                                |

---

## 3. Sunday maintenance

| #   | Item                                                                                                                                                                                                                                                                                                                                                                                  | Status   | David's feedback                                                         |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------ |
| 3.1 | Sunday 09:00: one Google Calendar reminder listing every Sunday task in order of execution, the dream cycle included.                                                                                                                                                                                                                                                                 | Decided  | 3.6 feedback                                                             |
| 3.2 | The separate 10:00 alarm is cancelled.                                                                                                                                                                                                                                                                                                                                                | Decided  | Cancel the alarm                                                         |
| 3.3 | Sunday 12:00: one Task Scheduler task runs the PostgreSQL backup cycle (both instances), then the GBrain export, one after the other.                                                                                                                                                                                                                                                 | Proposed | Time depends on the definitive list                                      |
| 3.4 | After 3.3 finishes: GBrain dream cycle, with its mandatory post-run verification. Manual.                                                                                                                                                                                                                                                                                             | Proposed | To Sunday maintenance list                                               |
| 3.5 | After 3.4: memory audit in OpenCode, David present.                                                                                                                                                                                                                                                                                                                                   | Proposed | Time depends on the definitive list                                      |
| 3.6 | Order reason: backup before the dream cycle protects against a bad run; the audit last checks the system after the dream cycle has changed it.                                                                                                                                                                                                                                        | Proposed | ???                                                                      |
| 3.7 | Configuration exams: a Google Calendar task-list entry, done on perceived drift or substantial change. Not scheduled.                                                                                                                                                                                                                                                                 | Decided  | Add to task list on Google Calendar                                      |
| 3.8 | The dream cycle never runs by itself. Verified from the dream-cycle configuration and reference: the old autopilot was removed 2026-09-06; on-demand only by design; absent from `sync-gbrain.sh`, `commit-all.sh`, `close-out-process.md` and Task Scheduler. Its only other trigger, `/sync-gbrain --dream`, leaves with 1.5. One live check remains: WSL crontab and timers today. | Done     | /sync-gbrain --dream` Must be written into daily-ops as a developer task |
| 3.9 | The decision "nothing gbrain-related is scheduled" is struck. The PostgreSQL documents are updated to match.                                                                                                                                                                                                                                                                          | Struck   | Strike this from known decisions                                         |











---

## 4. Task Scheduler and backups

| #   | Item                                                                                                                                                                           | Status   | David's feedback                                       |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- | ------------------------------------------------------ |
| 4.1 | Remove the `mb-doc-maintainer` logon task.                                                                                                                                     | Decided  | Agreed                                                 |
| 4.2 | Removed systems, replaced by `mb-doc-check`: mb-doc-maintainer, mb-doc-auditor, mb-align-docs, mb-wikilinks, mb-doc-manager, mb-doccycle. Remaining references are cleaned up. | Decided  | Agreed                                                 |
| 4.3 | DailyDevBackup stays and runs daily. Its content and retention follow the comprehensive backup plan (0.8).                                                                     | Decided  | Comprehensive backup plan to be decided                |
| 4.4 | OpenCodeSessionPrune stays and runs daily; its own backups keep 7 days.                                                                                                        | Decided  | Agreed                                                 |
| 4.5 | Backup purpose: loss of the whole machine. Content on GitHub is not backed up to disk; everything else is.                                                                     | Decided  | Comprehensive backup plan to be decided                |
| 4.6 | Every scheduled task runs as soon as possible after a missed start (PC off or asleep).                                                                                         | Proposed | No - Report to developer that scheduled run was missed |

---

## 5. Other documents and settings

| #    | Item                                                                                                                                                                                                                                                                                                                                                                                  | Status   | David's feedback           |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | -------------------------- |
| 5.1  | Keep `pdlf-explainer`; retire `pdlf-system-explainer`.                                                                                                                                                                                                                                                                                                                                | Decided  | Agreed                     |
| 5.2  | Environment explainer updates: (a) the "two-databases pothole" rewritten: port 5432 is GBrain's server on both sides, PDLF's ledger is on 5433; (b) dated "verified 2026-09-08/09" notes and the "created from the Sentinel side conversation" line removed (no history); (c) dated counts ("54 documents", "reactivated 2026-09-08") restated as current state.                      | Proposed | Explain what update        |
| 5.3  | A near-duplicate environment explainer exists in the `pdlf` source (`pdlf-environment-explainer.md`). One copy must be chosen.                                                                                                                                                                                                                                                        | Open     | I need to see both paths   |
| 5.4  | Remove `update-docs.py`.                                                                                                                                                                                                                                                                                                                                                              | Decided  | Agreed                     |
| 5.5  | The documentation repositories are fifteen: eight documentation libraries and seven skill-source repositories (`mb-project-docs`, `mb-memory-system-diagnostic`, `mb-compile-rules`, `mb-sentinel-review`, `mb-sysdoc-creator`, `mb-submit-memory`, `mb-archify-scope`). Verified from: `commit-all.sh`, `mb-doc-check.sources`, `doc-check-config.md`, `frontmatter conventions.md`. | Done     | Agreed                     |
| 5.6  | `mb-doc-check.roots` has no effect: the hook links to every folder in `roots` plus every folder in `sources`, and all eight `roots` folders are already in `sources`. Verified from `mb-doc-check.py` lines 1060–1071 and 1450. Proposal: delete `roots`; `sources` becomes the single list.                                                                                          | Proposed | Agreed.                    |
| 5.7  | Stale "eight" wording corrected: `commit-all.sh` header, `doc-check-config.md` settings rows, documentation-linking explainer.                                                                                                                                                                                                                                                        | Proposed | Clarify                    |
| 5.8  | Whether the hook is installed in all fifteen is not yet verified live; `commit-all.sh` prints a warning for any repository without it.                                                                                                                                                                                                                                                | Research | Awaiting Claude's response |
| 5.9  | mb4ecom and mb5pdlf: live projects, registered GBrain sources and GitHub repositories, in scope although empty. Removed from the scope list's exceptions.                                                                                                                                                                                                                             | Decided  | Agreed                     |
| 5.10 | mb4ecom and mb5pdlf READMEs state each project's placeholder purpose.                                                                                                                                                                                                                                                                                                                 | Decided  | Agreed                     |
| 5.11 | mb4ecom and mb5pdlf project libraries brought under `commit-all.sh` and the commit hook (seventeen repositories). Follows: add to `commit-all.sh`, `mb-doc-check.sources`, hook installed, `rollout-repo.sh` run once, `repo-organization`, `commit-all-repositories`, close the open items in `doc-check-config` and `project-docs-config`.                                          | Decided  | Agreed — yes               |

---

## 6. Files Claude still needs

| #   | File                                                                                   | For  | Status                |
| --- | -------------------------------------------------------------------------------------- | ---- | --------------------- |
| 6.1 | `mb-project-docs.md`                                                                   | 2B   | Done                  |
| 6.2 | `mb-submit-memory.md`                                                                  | 2B   | Done                  |
| 6.3 | `rollout-repo.sh`                                                                      | 5.5  | Done                  |
| 6.4 | `doc-check-config.md`, `doc-check-explainer.md`                                        | 5.5  | Done                  |
| 6.5 | `gbrain-dream-cycle-config.md`                                                         | 3.8  | Done                  |
| 6.6 | `memory-governor-reference.md` (`C:\mybizz\mybizz-config-docs\memory-governor\`)       | 2.12 | 3 Sent                |
| 6.7 | The latest run log in `C:\mybizz\logs\mb-submit-memory\` (`2026-09-30T165533+0200.md`) | 2.12 | 1 Sent                |
| 6.8 | `pdlf-environment-explainer.md` (`C:\pdlf\pdlf-library\pdlf-explainer-docs\`)          | 5.3  | 5 Sent. Paths in chat |

---

## 7. Order of execution

| Phase | Work                                                                           |
| ----- | ------------------------------------------------------------------------------ |
| 1     | Research: 2.12, 5.8, and the live check in 3.8.                                |
| 2     | David decides: 2.10, 2.11, 2.13, 2.14, 2.15, 3.3–3.6, 4.6, 5.2, 5.3, 5.6, 5.7. |
| 3     | Build the close-out skill (2B, 2.11).                                          |
| 4     | Task Scheduler: 4.1, 3.3, 4.4, 4.6.                                            |
| 5     | Google Calendar: 3.1, 3.7.                                                     |
| 6     | Document and settings changes: 5.1–5.11, 3.9, 4.2, 2.10, 2.14, 2.16.           |
| 7     | Rewrite daily-ops (section 1).                                                 |
