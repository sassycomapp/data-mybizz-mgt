# Docs-Skills Implementation Plan — for execution, 2026-09-21

Companion to: "Docs-Skills Architecture Proposal — for review, 2026-09-21.md" (this folder).
All seven architecture decisions are resolved in the proposal's section G; this plan converts
the proposal's section F into gated execution.

**Status: approved by the developer 2026-09-21.** Each work package ends at a gate; the next
package starts only on the developer's approval. All git commits before the Cupcake amendment
lands (WP3) are developer-terminal, issued as one copy-pasteable block per work package; the
commit-allowance channel takes over from WP3.

**Facts verified at planning time:**

- Cupcake is currently disabled (`cupcake.js.disabled`; no active plugin). WP0 re-enables it;
  implementation runs under enforcement from WP0 onward.
- The three old learnings folders hold 45 files (align-docs 16, wikilinks 3, docs-manager 26)
  for the WP6 sweep.
- The logs-folder example `C:\mybizz\logs\mb-align-docs` is: `run-index.md`, `learnings\`,
  `in-progress\`, `last-completed-run\`, `abandoned-runs\`, plus historical per-run records.

---

## WP0 — Source home, enforcement on, first developer block

**Status: agent-side scaffolding executed 2026-09-21; developer block pending.**

Agent-side (done): created `C:\mybizz\mb-doccycle\` (SKILL.md placeholder, `phases\`, `tool\`,
`tests\`), `C:\mybizz\logs\mb-doccycle\` per the `mb-align-docs` example, and the backup root
`C:\backup-mb-doccycle\`.

Developer block (pending — one sequence):

1. Publish the source home (developer terminal):

```
cd /mnt/c/mybizz/mb-doccycle
git init
git add -A
git commit -m "Initial commit"
gh repo create sassycomapp/mb-doccycle --private --source=. --remote=origin --push
```

2. Re-enable Cupcake:

```
mv ~/.config/opencode/plugin/cupcake.js.disabled ~/.config/opencode/plugin/cupcake.js
```

3. Restart OpenCode (the toggle is session-breaking; this plan file and the proposal file carry
   the state into the new session).

**Gate:** the developer confirms the repo exists with the skeleton pushed, and enforcement is
active. Grant slips are issued per work package from WP1 onward as pre-determined collective
blocks.

## WP1 — Shared run frame upgrade and move

**Purpose:** one document defining the whole cycle, moved into the doccycle suite.

Actions:

1. Rewrite the run frame as `doccycle-run-discipline.md` inside
   `C:\mybizz\mybizz-config-docs\mb-doccycle\`, covering: cycle-level items run once (resume,
   learnings, scope read, Cupcake enforcement preflight), per-phase items, the collective grant
   handover (one block per cycle: path slips, backup root, commit allowance), plain-English
   report standard and 3-question decision protocol, count discipline, STOP interrupt,
   one-corpus-per-session, the false-alarm doctrine and three-kind flag taxonomy, per-source
   sync verification via `gbrain sources status`, and the `(closeout)` bounded delta pass.
2. Update the mybizz-os-docs register row for `doc-skills-run-discipline` to Retired with a
   pointer to the new home.

**Gate:** the developer reviews the upgraded run-frame draft before it is written to the suite.

## WP2 — Phase-C canonical tool (test-first)

**Purpose:** the detection pipeline becomes tested code instead of per-run improvisation.

Actions:

1. Write `tool\doccycle-detect.py`: read-only, detects candidates, emits exact old-string →
   new-string pairs with line numbers, enforcing the proven invariants (backtick-first,
   line-precise, byte-preserving, unique-context matching), with `check=True` on every chained
   step.
2. Write `tests\` fixtures from the fifteen-cycle defect family: CRLF preservation, spaces in
   paths, self-references, substring collisions, double-occurrence tokens, malformed brackets,
   invisible bytes.
3. All tests pass; one read-only dry run against a small real sample to show the output format.

The tool never writes. Apply happens through the governed file tools (Edit/MultiEdit), verify
by diff against backup.

**Gate:** the developer reviews the tool, the passing tests, and a sample detection report.

## WP3 — Cupcake amendments

**Purpose:** the four coexistence changes, authored and compiled the standard way.

Actions:

1. Author the commit-allowance channel: amend
   `no_autonomous_commits_pushes_merges_releases_or_deployments.md` to define the verifiable
   allowance; create `bin\git-grant` (clone of `mg-grant` with configurable `--minutes`); amend
   the compiled commit policy to check the new grants-data file.
2. Amend `no_cross_project_filesystem_access_by_default.md`: add `C:\data-mybizz-mgt` to the
   restricted list; remove the stale `skills-collective` entry from the always-open list.
3. Compile everything via `mb-compile-rules`; run the post-compile fidelity check (authored
   exceptions map to compiled logic).
4. Update the cupcake config-docs suite and append one log row per its incident rule.

**Gate:** the developer reviews the amended authored rules; the compile and fidelity evidence
is shown before any live test.

## WP4 — Workflow skill and phase specs (the re-authoring)

**Purpose:** the single workflow skill, absorbing all three old skills under the 2026-09-20
rulings.

Actions:

1. Pre-implementation reads first (inventory 8.3): the align-docs detector and writer aux
   files, and docs-manager's five run logs.
2. Author in `C:\mybizz\mb-doccycle\`: `SKILL.md` with the governance header in its first lines
   (communication rules, STOP interrupt, one-corpus-per-session), the charter, and the
   invocation grammar `(all)` / `(corpus)` / `(phase corpus)` / `(closeout)`; then
   `phases\A-structure.md`, `phases\B-consistency.md`, `phases\C-conversion.md`.
3. Every proven-but-unencoded item rides this re-authoring: plain-English report standard,
   byte-exact writer invariants, treatment classes (PENDING-BUILD, historical/retired,
   out-of-corpus-live), the F-MK3 same-name-different-folder nuance, the quarantine rule
   (links remain as prose, never converted), count discipline, learnings advisory precedence,
   and the option-B alignment log (approved-and-applied only).

**Gate:** the developer reviews the SKILL.md and the three phase-spec drafts — the largest
review of the plan.

## WP5 — Suite documents

**Purpose:** the three configured documents the developer created, completed to the adjacent
suites' standard.

Actions: complete `doccycle-config.md`, `doccycle-reference.md`, `doccycle-explainer.md` in
`mybizz-config-docs\mb-doccycle\` following the sibling suites, describing the system as built
(not as intended).

**Gate:** the developer reviews the three completed documents.

## WP6 — Learnings sweep and records

**Purpose:** end the learnings drift and set up the doccycle record home.

Actions:

1. Sweep the 45 learnings files across the three old folders: mark superseded entries (the
   retired plain-`[[stem]]` clause among them), and list still-valid learnings for a fresh
   start.
2. Seed `C:\mybizz\logs\mb-doccycle\learnings\` with the still-valid items only, each marked
   with its source.
3. Old run logs, run indexes, and records stay in place as historical archives — nothing
   deleted, nothing moved.

**Gate:** the developer reviews the supersession list before any file is edited.

## WP7 — Install and retirement

**Purpose:** doccycle goes live; the three old skills go away.

Actions:

1. Copy `SKILL.md` into `~/.config/opencode/skills/mb-doccycle/` (copy, never move), record the
   source and install hash pair.
2. Back up the three old skill folders to `C:\backup-mb-doccycle\`, then remove them —
   including the five docs-manager agent files.
3. Confirm old run logs remain as archives.

**Gate:** the developer confirms the retirement timing, since muscle memory and existing run
records reference the old commands.

## WP8 — Acceptance test (Cupcake on)

**Purpose:** prove the coexistence design works live.

Actions: one controlled corpus cycle against a restricted folder using the collective slip
block; one commit through the `git-grant` allowance; per-source sync status evidence; the
counter check or its honest absence; a dream-cycle run to close the resolver-freshness gap.

**Gate:** the developer judges the acceptance test; on a pass, doccycle is operational.

---

## Parallel track (not this plan's work)

The config-management build-out for doccycle (`doccycle-skill.md`, exam plan and report, log,
learnings, via `config-setup-prompt`) runs as its own engagement after WP7, on the developer's
instruction, with the two context documents named in the review
(`config-manager-agent.md`, `config-setup-prompt.md`).

---

**Next steps:** WP0 gate → WP1 draft for review → WP2 tool and tests → WP3 Cupcake amendments
→ WP4 re-authoring → WP5 suite documents → WP6 learnings sweep → WP7 install and retirement →
WP8 acceptance test.

Actor assignments: agent executes all work-package actions; the developer holds every gate,
runs all developer-terminal git commands before WP3, issues the pre-determined collective
slip blocks, and re-enables Cupcake in WP0.
