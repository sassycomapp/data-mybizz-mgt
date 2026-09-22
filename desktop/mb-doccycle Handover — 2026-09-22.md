---
document: "mb-doccycle Handover — session bootstrap for WP2 onward"
doc-id: mb-doccycle-handover
state: Live
date-created: 2026-09-22
---

# mb-doccycle Handover — 2026-09-22

Bootstrap document for the next session. Read this first, then the two
companion files named below. The session that produced it (architecture →
decisions → plan → WP0–WP1, plus the Cupcake set-and-forget repair) is closed;
**the new session starts at WP2.**

## Status — what is complete and verified

- **Architecture: final.** "Docs-Skills Architecture Proposal — for review,
  2026-09-21.md" (this folder). All seven decisions (G1–G7) resolved in its
  section G.
- **Implementation plan: approved, live status inside.** "Docs-Skills
  Implementation Plan — for execution, 2026-09-21.md" (this folder). Work
  packages WP0–WP8, each gated.
- **WP0 — source home:** `C:\mybizz\mb-doccycle` created (SKILL.md placeholder,
  `phases\`, `tool\`, `tests\`), git repo published
  (github.com/sassycomapp/mb-doccycle, commit 799c528), logs folder
  `C:\mybizz\logs\mb-doccycle` per the mb-align-docs example, backup root
  `C:\backup-mb-doccycle`.
- **Cupcake set-and-forget package** (pulled forward from WP3, incident-driven
  2026-09-22): plugin amended — `failMode: open` is the environment default and
  skeleton-less folders fall back to the global-only home
  `~/.config/cupcake/fallback`; every skeleton made boot-safe by the
  input-gated `cup-noop-fallback.rego` placeholder; live-verified (ten clean
  evaluations from a skeleton-less folder, one real denial obeyed). All three
  cupcake docs + the incident log row updated. **WP3 therefore retains only:**
  the commit-allowance channel, the cross-project rule amendments
  (data-mybizz-mgt to restricted; stale skills-collective entry removed), and
  the post-compile fidelity check.
- **WP1 — run frame: closed.**
  `C:\mybizz\mybizz-config-docs\mb-doccycle\doccycle-run-discipline.md` written
  (developer-approved draft); the old `doc-skills-run-discipline.md` retired in
  place (frontmatter Retired + pointer) and its register-local.md row marked
  Retired with supersession.

## The new session starts at WP2

Phase-C canonical tool, test-first (plan file, WP2): write
`C:\mybizz\mb-doccycle\tool\doccycle-detect.py` — read-only detection emitting
exact old-string → new-string pairs; invariants: backtick-first, line-precise,
byte-preserving, unique-context matching; `check=True` on chained steps — plus
`tests\` fixtures from the 15-cycle defect family (CRLF, spaces in paths,
self-references, substring collisions, double-occurrence tokens, malformed
brackets, invisible bytes). Gate: developer reviews the tool, the passing
tests, and a sample detection report.

Before WP4 (re-authoring), do the two pre-implementation reads (plan F.8):
the align-docs detector/writer aux files, and docs-manager's five run logs.

## Session rules (from the run frame — carried into every session)

Plain English, never AI shorthand; every handed action carries its complete
commands at the point of use. STOP is absolute. One corpus per session.
Uncertainty asks, never acts. A Cupcake denial is obeyed, never worked around.
Slips are requested collectively — one block, counts pre-determined.

## Standing decisions in force

Commit-allowance grant channel (G1, approved); data-mybizz-mgt
restricted-with-slip (G2); skill system files directly under `C:\mybizz`, doc
suite in `mybizz-config-docs`, run frame moved into the suite (G3); no
sub-agents, no exceptions (G4); alignment log records approved-and-applied
only (G5); name `mb-doccycle`, grammar `(all)` / `(corpus)` / `(phase corpus)`
/ `(closeout)` (G6); quarantine links remain as prose, never converted (G7).

## Open items at handover

1. **Commit and push (developer-terminal):** `mybizz-config-docs` (new run
   frame) and `mybizz-os-docs` (register row + retired doc). The agent never
   commits.
2. **gbrain sync:** run the sync script, then verify per source with
   `gbrain sources status` (mb-doccycle is registered, federated off).
3. Suite documents (`doccycle-config.md`, `doccycle-reference.md`,
   `doccycle-explainer.md`) exist and are empty — completed at WP5 to the
   adjacent suites' standard.
4. `doccycle-skill.md`, exam plan/report, log, and learnings come through the
   config-management build-out later, developer-driven (context files named in
   the plan's parallel track).
5. The three old skills (mb-docs-manager, mb-align-docs, mb-wikilinks) remain
   installed until WP7 — **do not invoke them**; their text is superseded and
   partially wrong (pre-ruling).

## Key paths

| Artifact | Path |
|---|---|
| Architecture proposal (final) | `C:\data-mybizz-mgt\desktop\Docs-Skills Architecture Proposal — for review, 2026-09-21.md` |
| Implementation plan (live status) | `C:\data-mybizz-mgt\desktop\Docs-Skills Implementation Plan — for execution, 2026-09-21.md` |
| Run frame (live) | `C:\mybizz\mybizz-config-docs\mb-doccycle\doccycle-run-discipline.md` |
| Retired old run frame | `C:\mybizz\mybizz-os-docs\os-reference-docs\doc-skills-run-discipline.md` (Retired in place) |
| Skill source home | `C:\mybizz\mb-doccycle` (GitHub: sassycomapp/mb-doccycle) |
| Logs / records home | `C:\mybizz\logs\mb-doccycle` (run-index, learnings, in-progress, last-completed-run, abandoned-runs) |
| Backup root | `C:\backup-mb-doccycle` |
| Cupcake suite (updated 2026-09-22) | `C:\mybizz\mybizz-config-docs\cupcake\` (config, reference, explainer, log) |
| Repo register (Cupcake column) | `C:\mybizz\mybizz-os-docs\os-reference-docs\repo-organization.md` |
| Scope authority | `C:\mybizz\mybizz-os-docs\os-reference-docs\mybizz-scope-list.md` |
| Grant tools | `mg-grant` / `mg-revoke` (path slips), `git-grant` (commit allowance — built at WP3) |
