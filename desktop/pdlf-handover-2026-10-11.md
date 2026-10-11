---
title: "pdlf-handover-2026-10-11"
doc-id: "mb-f8ce64fe"
updated: "2026-10-11"
---
# PDLF Handover — 2026-10-11

## Purpose

This document lets a new Claude session continue PDLF work without the previous conversation. Read it fully before doing anything.

## Roles

David is the project manager acting as developer, not a programmer. He dictates by speech-to-text, so names can arrive garbled; all his document names are lowercase kebab-case. Claude is the Chief Engineer: it resolves technical questions itself and asks David only about intent. His stored preferences apply (short plain replies, numbered steps labelled WSL terminal / OpenCode / Back to Claude, no commands until everything is settled, terminal over OpenCode, ask before any tool that reaches outside the conversation, never defer work).

## The system

- PDLF is the application development system that builds Anvil.works apps. It lives at `C:\pdlf` (WSL `/mnt/c/pdlf`) and runs on mybizz-os.
- `pdlf-library/pdlf-explainer-docs/pdlf-intent.md` is the single statement of what PDLF is meant to be. Where anything disagrees with it, the intent wins.
- Three documents steer the build: `app-factory/pdlf-build-plan.md` (the blueprint; moves to `obsolete/` when PDLF is built), `pdlf-library/docs-local/pdlf-built-report.md` (what has been built; kept), `pdlf-library/docs-local/orchestrator-run-plan.md` (the order the orchestrator runs steps).

## The app-factory layout (completed today)

`stepwise/` is retired. Every step lives in `app-factory/`, in its phase folder:

- `phase-a-init`: 01–10 (01 orchestrator; 02–10 entry points)
- `phase-b-discover-and-define`: 11–16 (also holds `pdlf-phase-b-review.md`)
- `phase-c-design-and-plan`: 17–28
- `phase-d-scaffold-and-assemble`: 29–34
- `phase-e-build-and-verify`: 35–40b
- `phase-f-ship-and-monitor`: 41–46
- `phase-g`: remaining apps, created when designed

Files are named number first: `16-domain-modeling.md`, `16-build-notes.md`, `16-decision-tree.html`. Each step has a module file `NN-module.md` beside it (placeholder until the step is compiled). Lettered steps are lowercase (35a, 38a, 40b, 42a). Modules 13 and 25 are kept although those numbers are unused. Phase letters shifted by one (old A–E are now B–F).

`AGENTS.md` has three standing rules: all PDLF work happens in `C:\pdlf`; a module file is written only by compiling its step's files, on David's instruction; `output/` serves one application at a time.

## Decisions settled today

- Step numbers stay global (01–46). Per-phase renumbering was considered and rejected: the step number is the step's identity across the ledger, gates, receipts and all documents.
- 13 and 25 stay.
- `stepwise-development-process.md` and `proc-stepwise-closeout.md` are in `obsolete/`.

## How work is done

- Repositories Claude needs, with David's local paths:
  - `sassycomapp/pdlf` → `/mnt/c/pdlf`
  - `sassycomapp/mybizz-os-docs` → `/mnt/c/mybizz/mybizz-os-docs`
  - `sassycomapp/mybizz-config-docs` → `/mnt/c/mybizz/mybizz-config-docs`
  - `sassycomapp/project-library-global` → `/mnt/c/dev/project-library-global`
- Access: the four are public, so Claude clones each with `git clone --depth 1 https://github.com/sassycomapp/<repo>.git` into its own workspace. Ask David before cloning. To refresh a clone later: `git fetch --depth 1 origin && git reset --hard FETCH_HEAD` (a plain pull fails). If David has made them private again, attaching them with `add_repo` was refused in the past; ask him to make them public for the session.
- Method used successfully: Claude clones the repositories, makes all moves and edits locally, produces one patch per repository plus an `apply.sh` that checks every patch (`git apply --check --index`) before applying any, and sends them as a zip. David saves it to `C:\temp\` and runs it in WSL. Nothing is committed by the script.
- Only David commits: `bash /mnt/c/mybizz/scripts/commit-all.sh "message"` (commit, GBrain sync, push for all repositories). Its hook gives documents doc-ids, repairs links on moves (across repositories), and blocks a commit that deletes a document while adding new ones (override `MB_DELETE_OK=1`).
- Link form: `[[[source:slug|Title]]](C:/path.md)`.
- Docmap: `python3 /mnt/c/mybizz/scripts/build-docmap.py --write`.
- Ledger: PostgreSQL 15 on Windows, port 5433, via the PowerShell bridge. GBrain: PostgreSQL 16 on WSL, port 5432.

## Open items, in order

1. `app-factory/README.md` and `pdlf-library/README.md`: rewrite for the new layout (they were deliberately left until last; both still describe the old layout).
2. The testing component (L4).
3. The Cupcake proof (L1).
4. Act on `pdlf-phase-b-review.md`: correct Steps 11–16 to the intent, then build-plan entries for Steps 17–46, written and approved before any step file is touched.
5. Pre-project content, during Phase A testing.

## Minor loose ends

- `C:\pdlf\stepwise\` remains as an empty folder Windows would not let WSL remove. David will delete it later, perhaps after a restart.
- GBrain still shows stale entries `desktop/pdlf-discovery` and `desktop/pdlf-intent-map`; both documents are in `obsolete/`. Clear only if David wants it.
- GBrain offers an upgrade (0.59 → 0.60); not acted on.
