---
document: "data-mybizz-mgt — README"
doc-id: README
state: Live
date-created: 2026-09-14
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
| `register-local.md` | Append-only document register |
| `README.md` | This file |

Related folders that no longer live here: `Budget/` moved to `C:\_data-mybizz-exempt\Budget`
(out of scope); `Models/` moved to `C:\mybizz\Models`; `prompts/` moved to `C:\mybizz\prompts`.

## Key documents

- [[mybizz-scope-list|Mybizz Scope List]] — the scope scaffold. Read at Phase 0 of every
  `mb-doccycle` run; wins over every other document on scope. Lives at
  `C:\mybizz\mybizz-os-docs\os-reference-docs\`.
- [[2026-09-15-session-numbers-from-sessions-log|session numbers come from the sessions log]] — the sessions index; one row per closed session
  (session open/close routine). Lives at `C:\mybizz\logs\sessions-log\`.
- `facts-log.md` — the authoritative index of saved durable facts
  (fact save/recall routine). Lives at `C:\mybizz\logs\gbrain-logs\facts-log\`.
- [[repo-organization|Repo organization]] — the correlation table of GBrain sources, GitHub
  repositories, and local paths (replaced `Repo organization.xlsx`). Lives at
  `C:\mybizz\mybizz-os-docs\os-reference-docs\`.

## Naming note

The folder was renamed from `C:\_data-mybizz-mgt` to `C:\data-mybizz-mgt`
on 2026-09-14 to drop the leading underscore — the underscore was invalid
in GBrain source ids and awkward everywhere else. References elsewhere in
the corpus may still carry the old path until the document-management
skills sweep them.

## Kept fresh by

`mb-doccycle` owns document management for this folder (register
membership, cross-references, wikilinks). `register-local.md` is the
append-only document register.
