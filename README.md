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
| `_desktop/` | Operating documents — scope scaffold (`mybizz-scope-list.md`), sessions log, facts log, daily ops, master task list, standing instruction, repo organization |
| `Budget/` | Budget data, strategy, risk analysis, learnings |
| `Models/` | AI model selection working documents |
| `prompts/` | Standing prompt/process documents (close-out process, learning, quality control, memory family) |

## Key documents

- `mybizz-scope-list.md` — the scope scaffold. Read at Phase 0 of every
  `mb-docs-manager` run; wins over every other document on scope.
- `sessions-log.md` — the sessions index; one row per closed session
  (session open/close routine).
- `facts-log.md` — the authoritative index of saved durable facts
  (fact save/recall routine).
- `repo-organization.md` — the correlation table of GBrain sources, GitHub
  repositories, and local paths (replaced `Repo organization.xlsx`).

## Naming note

The folder was renamed from `C:\_data-mybizz-mgt` to `C:\data-mybizz-mgt`
on 2026-09-14 to drop the leading underscore — the underscore was invalid
in GBrain source ids and awkward everywhere else. References elsewhere in
the corpus may still carry the old path until the document-management
skills sweep them.

## Kept fresh by

`mb-docs-manager`, `mb-align-docs`, and `mb-wikilinks` own document
management for this folder (register membership, cross-references,
wikilinks). `register-local.md` is the append-only document register.
