---
title: "README"
doc-id: "mb-8436565e"
updated: "2026-10-01"
---
# data-mybizz-mgt — README

The Mybizz management data folder — the desktop-level operating documents of
the Mybizz/PDLF operating system, plus the developer's budget, model, and
prompt working files. Not an Anvil project and not a code repository: this is
the control surface the skills and agents read from and write to.

## Structure

| Item | Purpose |
|---|---|
| `desktop/` | Operating documents — daily ops, master task list, deferred-and-unresolved-matters, dev-makepdlf-todo |
| `WIP/` | Working files |
| `archive/` | Archived material |
| `temp/` | Temporary files |
| `register-local.md` The use of registers has been discontinued. Please review | Append-only document register |
| `README.md` | This file |

Related folders that no longer live here: `Budget/` moved to `C:\_data-mybizz-exempt\Budget`
(out of scope); `Models/` moved to `C:\mybizz\Models`; `prompts/` moved to `C:\mybizz\prompts`.

## Key documents

- [[[mybizz-os-docs:os-reference-docs/mybizz-scope-list|Mybizz Scope List]]](C:/mybizz/mybizz-os-docs/os-reference-docs/mybizz-scope-list.md) — the scope scaffold. Read at Phase 0 of every
  `mb-doccycle` run; wins over every other document on scope. Lives at
  `C:\mybizz\mybizz-os-docs\os-reference-docs\`.
- [[[mybizz-config-docs:facts/2026-09-15-session-numbers-from-sessions-log|session numbers come from the sessions log]]](C:/mybizz/mybizz-config-docs/facts/2026-09-15-session-numbers-from-sessions-log.md) — the sessions index; one row per closed session
  (session open/close routine). Lives at `C:\mybizz\logs\sessions-log\`.
- `facts-log.md` — the authoritative index of saved durable facts
  (fact save/recall routine). Lives at `C:\mybizz\logs\gbrain-logs\facts-log\`.
- [[[mybizz-os-docs:os-reference-docs/repo-organization|Repo organization]]](C:/mybizz/mybizz-os-docs/os-reference-docs/repo-organization.md) — the correlation table of GBrain sources, GitHub
  repositories, and local paths (replaced `Repo organization.xlsx`). Lives at
  `C:\mybizz\mybizz-os-docs\os-reference-docs\`.

## Naming note

The folder was renamed from `C:\_data-mybizz-mgt` to `C:\data-mybizz-mgt`
on 2026-09-14 to drop the leading underscore — the underscore was invalid
in GBrain source ids and awkward everywhere else. References elsewhere in
the corpus may still carry the old path until the document-management
skills sweep them.

## Kept fresh by

`mb-doccycle` owns document management for this folder (register The use of registers has been discontinued. Please review
membership, cross-references, wikilinks). `register-local.md` The use of registers has been discontinued. Please review is the
append-only document register The use of registers has been discontinued. Please review.
