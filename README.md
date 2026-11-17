---
title: "README"
doc-id: "mb-8436565e"
updated: "2026-11-17"
---
# data-mybizz-mgt — README

The Mybizz management data folder — the desktop-level operating documents of
the Mybizz/PDLF operating system, plus Mybizz's business and marketing documents. Not an Anvil project and not a code repository: this is
the control surface the skills and agents read from and write to.

## Structure

| Item | Purpose |
|---|---|
| `business/mybizz-live/` | The company: budget, business plan, setup, launch and banking, tax |
| `business/mybizz-cs/` | Mybizz CS business plan |
| `business/mybizz-fda/` | Mybizz FDA business and operations plans |
| `marketing/` | Marketing for every Mybizz product |
| `security/` | Security and legal compliance briefs |
| `desktop/` | Operating documents: master task list, developer's duties |
| `assets/` | Images |
| `README.md` | This file |

Documents for building an app live in that app's project library, not here. Each fact has one home: product, brand and build facts live in the app's project library, and business and marketing facts live here. A document that needs a fact from the other side links to the fact's source document as `[[source-id:page-name]]` and never restates it. Finished marketing material, such as a post or an outreach message, is the one exception: it is written from the source when it is made and is never used as a source.

## Key documents

- [[[mybizz-os-docs:os-reference-docs/mybizz-scope-list|Mybizz Scope List]]](C:/mybizz/mybizz-os-docs/os-reference-docs/mybizz-scope-list.md) — the scope scaffold. Lives at
  `C:\mybizz\mybizz-os-docs\os-reference-docs\`.
- [[[mybizz-os-docs:os-reference-docs/repo-organization|Repo organization]]](C:/mybizz/mybizz-os-docs/os-reference-docs/repo-organization.md) — the correlation table of GBrain sources, GitHub
  repositories, and local paths (replaced `Repo organization.xlsx`). Lives at
  `C:\mybizz\mybizz-os-docs\os-reference-docs\`.

## Naming note

The folder was renamed from `C:\_data-mybizz-mgt` to `C:\data-mybizz-mgt`
on 2026-09-14 to drop the leading underscore — the underscore was invalid
in GBrain source ids and awkward everywhere else. References elsewhere in
the corpus may still carry the old path.

## Kept fresh by

This README is kept accurate by /mb-project-docs during close-out
(`/mb-close-out`); the repositories are committed, GBrain-updated and
pushed by commit-all.sh ([[[mybizz-os-docs:operating-procedures/commit-all-repositories]]](C:/mybizz/mybizz-os-docs/operating-procedures/commit-all-repositories.md)).
