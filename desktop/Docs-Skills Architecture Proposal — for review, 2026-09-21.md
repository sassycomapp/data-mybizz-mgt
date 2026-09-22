Investigation complete. All grounding read and verified: the three SKILL.md files, the shared run frame, the scope scaffold, the four relevant Cupcake authored rules, the compiled Rego policies, both grant scripts, and the developer's friction note. This file is the living deliverable for review; amendments are applied only on developer approval.

---

# Docs-Skills Architecture Proposal — for review, 2026-09-21

**The recommendation in one line:** convert the three skills into one workflow skill with three sequential phases (A structural → B content-consistency → C wikilink conversion), executed one corpus per cycle, on a git-backed source, with one canonical Phase-C detection tool and four small Cupcake coexistence amendments. No orchestration platform, no new infrastructure.

---

## New evidence gathered this session (beyond the inventory)

These findings resolve or sharpen several Group F uncertainties without needing the re-enable test, and they shaped the design below.

1. **F5 is resolved by inspection.** The compiled network policy (`cup-outbound_network_access_is_allowlist_only.rego`) inspects only WebFetch and Bash `curl`/`wget` URL hosts. A `git push` command carries no URL token and is never evaluated; `github.com` is on the allowlist regardless. Pushes flow under the network rule. The only thing blocking pushes is the commit rule.
2. **F1 is confirmed mechanically.** The compiled commit policy is a bare regex deny of `git commit|push|merge` with no grants channel and no implemented escape hatch. The authored rule's "unless the developer has given explicit approval in the current session" is dead text — the authored rule and the compiled enforcement already disagree. Any remedy must make them say the same thing.
3. **F2 is confirmed compiled and live.** The bash-write shapes (python heredoc/`-c`, perl, `sed -i`, redirects, `cp/mv/rm/tee/dd`) are folded into the cross-project policy with the same exempt list and the same grant channel. One accepted limitation matters for the docs skills: target extraction is token-based, so paths containing spaces may be missed.
4. **data-mybizz-mgt's compiled treatment is already "denied without a slip"** (outside cwd, not on the exempt list). The authored rule merely fails to document it. The fix is a folder-list amendment, not a behaviour change.
5. **The grant pattern is proven and reusable.** `mg-grant` issues folder slips (count + fixed 30-minute expiry, atomic regeneration, opa-checked); `net-grant` exists as a second working instance of the same pattern. A commit-allowance channel would clone this pattern, not invent machinery.

**Provenance note — two additional sources reviewed 2026-09-21 after the first draft:** the developer's friction note ([[Agent disobediance issue|Agent disobediance issue]], desktop) — grounding for RC2/A4 and the governance-header, STOP-interrupt, one-corpus-per-session, and coexistence-via-grants designs cited throughout; and the environment explainer (`mybizz-os-docs\environment-explainer.md`) — supplying the layer statement (section B), the finding-handling standard (B.1, D), and the chained-command and per-source-sync engineering rules (B.1, B.4).

**Verification findings from the developer's second-pass update (2026-09-21):** the quarantine move and rename are verified on disk — `C:\dev\project-library-global\quarantine\prior-mybizz-docs`; the live scope list contains NO quarantine exception (the stated addition did not land, and the list's own notes route treatment states through rules rather than the list — see G7); `C:\mybizz\skills-collective` does not exist, so the cross-project rule's always-open list carries a stale reference (corrected with the Cupcake amendments); and no skills source repository exists anywhere — the installed skills are plain copies in a non-git folder, with no skills repo registered — the direct evidence for G3.

## A. Problems being addressed

| Inventory item                                                                                 | Addressed by                                                                                                 |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| A1 stale skill text vs rulings                                                                 | Re-authoring; single git-versioned text ends the drift machine                                               |
| A2 unreadable reports                                                                          | Plain-English per-phase report + 3-question decision protocol, encoded                                       |
| A3 duration explosion                                                                          | Ceremony collapse (below); canonical tool removes defect re-runs                                             |
| A4 governance at point of failure                                                              | Governance header in the first lines of the skill; STOP interrupt; one-corpus-per-session; Cupcake preflight |
| A5 sub-agent contradiction                                                                     | No-sub-agent discipline adopted everywhere; the five docs-manager agent files retired                        |
| A6 sync discipline                                                                             | One close protocol: per-source sync for changed sources                                                      |
| A7 learnings override text                                                                     | Learnings become advisory; skill text authoritative; supersession marks                                      |
| B1–B4, B6 docs-manager stale body, wrong scaffold path, internal contradictions, obsolete path | Absorbed by re-authoring; embedded scope copy retired — the scaffold is read live at Phase 0                 |
| C1 locked function-scope doc                                                                   | Amendment path = commits to the git source                                                                   |
| C3–C7 recurring classes                                                                        | Encoded in Phase-B spec (F-MK3 nuance, count discipline, FM tensions surfaced not healed silently)           |
| D1 no canonical implementation (RC3)                                                           | Canonical Phase-C detection tool + governed apply channel                                                    |
| D2 version churn                                                                               | Git-backed source; every text change is a commit                                                             |
| D4 coincidental variant matches                                                                | Semantic-justification field required per candidate (already the proven format)                              |
| D5 improvised treatment classes                                                                | PENDING-BUILD, historical/retired, out-of-corpus-live encoded as Phase-C rules                               |
| D8 undemonstrated counters                                                                     | Close-protocol verification step; dream-cycle dependency reported honestly                                   |
| E2, E3 empty files, case collisions                                                            | Treatment classes; casefolded census                                                                         |
| F1 commit gate conflict                                                                        | Commit coexistence decision (below)                                                                          |
| F2/F3 bash-write conflict, undefined zone                                                      | Apply via governed file tools; collective slip block; data-mybizz-mgt list amendment                        |
| F4 wikilinks has no grant section                                                              | Handover procedure lives once in the run frame — all phases inherit it                                       |
| F6 session-breaking toggle                                                                     | No new toggle machinery; preflight catches accidental disablement                                            |
| F7 no enforcement-state check                                                                  | Enforcement-state preflight in the run frame                                                                 |
| F8 authored/compiled fidelity                                                                  | Fidelity check added to the rule-amendment procedure; commit rule text aligned with the chosen mechanism     |

## B. Proposed architecture

**Layer statement (standing rule 9.1):** this entire remedy operates in the **pre-makePDLF layer**. The docs skills are supporting systems that never ship; the environment explainer's shipping-boundary and runtime-self-sufficiency cautions therefore do not apply here, and the skills' outputs flow into higher layers only through the developer's review process.

### B.1 Components

1. **One workflow skill** (`mb-doccycle` — name approved by the developer 2026-09-21). Three phase specs, each absorbing one existing skill:
   - **Phase A — structure/navigational** (absorbs docs-manager): docmaps, projects-config-register, INDEX/README/AGENTS verification.
   - **Phase B — content consistency** (absorbs align-docs): cross-reference healing, front matter, register enforcement, directionality, missing-document investigation.
   - **Phase C — wikilink conversion** (absorbs wikilinks): reference conversion into `[[basename|Display Text]]`. Quarantine treatment (developer-ruled 2026-09-21): links to quarantine content remain as written prose — never converted to wikilinks, never deleted; stale paths are healed to the current quarantine location (`C:\dev\project-library-global\quarantine\prior-mybizz-docs`).
     Invocation: `(all)` = sequential corpus cycles; `(corpus)` = one cycle; `(phase corpus)` = phase-only run (this preserves the close-out hook use case, e.g. B after ordinary structural work); `(closeout)` = the bounded session-closeout pass (B.6).
2. **Upgraded shared run frame** (`doc-skills-run-discipline.md`). Cycle-level items run once: resume check, learnings load, scope read, Cupcake enforcement preflight. Per-phase items repeat: verified backup sized to that phase's write surface, detect, report, approve, apply, verify, commit plan, index row, learnings. Handover contracts made explicit: B-close is the gate before C; C's missing-document findings trigger one bounded B re-pass per cycle. **Finding-handling standard (adopted from the environment explainer):** every finding triages into exactly one of three kinds — legitimate-minimal (set aside; e.g. a register row asserting a home a file has legitimately left during development flux), illegitimate (a detector defect, corrected through the rule pipeline — an amendment is now a cheap commit to the git source), legitimate-requires-attention (decide and implement); an alarm raised with no cause is a defect in the detection logic itself, never noise to dismiss and never a file forced into a mold. This gives the register/home churn class (C4) and the missing-document false alarms (E1/E2) a principled home, and it is the structural counter to remediation-as-error on a corpus in deliberate flux (RC1).
3. **Canonical Phase-C tool**, git-backed beside the skill. It is read-only: it detects candidates and emits exact old-string → new-string pairs, enforcing the proven invariants (backtick-first, line-precise, byte-preserving, unique-context matching), with test fixtures built from the 15-cycle defect family (CRLF, spaces, self-ref filter, substring collisions, double-occurrence tokens, malformed brackets, invisible bytes). Apply happens through the governed file tools (Edit/MultiEdit), which Cupcake fully governs and which are byte-exact outside the replacement. Verify by diff against backup. Reads stay free everywhere, so detection needs no slip; only applies consume slips. This also removes the heredoc bulk-write channel entirely. Chained shell commands inside the tool verify each result before the next runs (the silent-cleanup pothole: `check=True` discipline, no failed step continues).
4. **Cupcake amendments — four, small:**
   - (i) **Commit coexistence**, developer decision between two stances: (a) a commit-allowance grant channel — clone of `mg-grant` (`git-grant --repo <path> --count N --minutes M`), a new grants-data file, and a policy amendment checking it — with the authored rule text rewritten to describe the verifiable token; or (b) documented always-deny with developer-terminal commits, the skills ending each phase at a commit plan. Either way the authored text and compiled policy are made to say the same thing. **RESOLVED (2026-09-21): stance (a) approved — the commit-allowance grant channel.**
   - (ii) **data-mybizz-mgt added to the authored folder lists** (RESOLVED 2026-09-21: restricted-with-slip, the developer adopted the recommendation; the compiled behaviour already denies-without-slip, so this is documentation plus routing, not a widening).
   - (iii) **Grant-handover procedure moved once into the run frame** — retires the duplicated Phase 3a copies and gives Phase C the section it never had. Per the developer's ruling (2026-09-21), slips are requested COLLECTIVELY, never one at a time, and their counts are determined before any apply: after detection and approval, the skill constructs ONE copy-pasteable block covering every slip the cycle needs — path slips per restricted folder (approved file count + buffer), the backup-root line, and the commit allowance (G1) — issued in a single developer action; one supplementary block only if a later count is exceeded.
   - (iv) **Post-compile fidelity check** added to the rule-amendment procedure: authored exceptions must map to compiled logic, verified at amendment time.
5. **Skill system source and homes (RESOLVED 2026-09-21, developer convention):** the doccycle skill system files — the workflow SKILL.md, the three phase specs, and the canonical tool — live in a source folder directly under `C:\mybizz\`, following the `archify` / `matt-pocock-skills-source` pattern (both GitHub-backed clones). The configured document suite lives in `C:\mybizz\mybizz-config-docs\mb-doccycle\` (config, reference, explainer created 2026-09-21, filename typos corrected; the remaining suite files — skill, exam-plan, exam-report, log, learnings — belong to the config-management build-out, not to this remedy). The installed copy in `~/.config/opencode/skills\mb-doccycle\` is a hash-verified copy checked by the config-manager each exam cycle. The shared run frame MOVES from `mybizz-os-docs\os-reference-docs\` into the doccycle suite (developer decision, option b), renamed to the suite's naming pattern at migration; the old register row is retired. Note: `doccycle-skill.md` is the config exam skill for doccycle, NOT the workflow skill source (developer correction). One item remains open: the GitHub remote for the new source folder under `C:\mybizz\` (see G3).

### B.2 Execution sequence

A → B → C on one corpus per cycle. Phase commits between phases (one commit plan per phase, one batch approval, covered by the cycle's commit allowance or handed to the developer's terminal). Bounded B re-pass after C's findings. Close: log row, learnings, per-source GBrain sync and embed, counter verification. Wide mode is a sequence of complete corpus cycles, one in flight.

### B.3 Corpus scope (the task's central question)

The smallest coordinated scope is **one target corpus plus project-library-global** — align-docs' existing rule, and the correct one: A's structural fixes change the paths B repoints and C converts, so all three must see the same corpus state; directionality validation needs both the target and global in the same run. Leaf folders are batching units inside C, never coordination units. The whole corpus set is deliberately not one cycle: a corpus cycle is already hours of work, sequential cycles give natural checkpoints and limit session loss, and the developer's own note names one-corpus-per-session as the working-scale answer. The corpora also map onto the environment explainer's layers — `makepdlf-project-library` is the makePDLF layer's estate, `pdlf-library` the PDLF layer's, `mb-3-cs-project-library` the shipped estate's dev workspace — so one corpus per cycle is the layer-consistent unit, and because cross-layer referencing is normal (2026-09-20 ruling), project-library-global must always be in the same run.

### B.4 Validation points

Backup verification is stop-cold per phase. Every apply requires an approval on record. Every edited file passes a diff gate against its backup. Every count is derived mechanically from its own item list. Commit plan precedes every commit. Close requires per-source sync evidence — `gbrain sources status` per source, never a blanket success report (the blanket-sync pothole) — and the counter check (or an honest statement of the dream-cycle limitation).

### B.5 What this architecture explicitly does not solve

- **Implementation drift (RC3/D1)** — solved by the canonical tool, not by the merge. The merge without the tool would repeat the heredoc defect family.
- **Residual run duration** — the inherent detection time stays; only the ceremony overhead was architectural.
- **The Cupcake conflicts** — solved by the amendments, not by the merge; a merged skill with no grant channel would still hard-stop.
- **Developer rulings** (D6, D7, C2, E1) — orthogonal; they change phase-spec content, not shape.

The merge is justified by evidence, not convenience: it eliminates the five-problem cluster the task names (inconsistent state, duplicated ceremony, independent corpus assumptions, inconsistent governance, partial-corpus runs), and it collapses the RC4 drift machine — the v12 docs-manager that never received the 2026-09-19 refactor is exactly what three independently-authored texts guarantee will happen again.

### B.6 Session close-out pass (developer direction 2026-09-21 — the doc-management procedure joins session close-out)

A bounded delta pass, never a full cycle. When a session has created files, moved files, or created new links, the `(closeout)` pass inventories exactly what that session changed, runs the three phases only over those touched files and folders, presents one grouped plain-English report, takes one approval, and uses the same collective block for slips and the commit allowance. Typical cost: minutes. Anything beyond the session's own changes is proposed for the next scheduled cycle instead of being absorbed into the close-out, so the close-out can never balloon into a run. This is the standing mechanism that keeps the navigation documents current while the corpus is in flux — the RC1 answer in daily operation — and it slots into the existing session close-out routine as an offered step.

## C. What remains separate

1. Cupcake's rule set and enforcement architecture — untouched beyond the four amendments.
2. GBrain operations (sync, embed, dream cycle) — close-protocol steps, not skill architecture.
3. The scope scaffold (`mybizz-scope-list.md`) — developer-owned, unchanged.
4. Register and docmap content — the developer's authoring domain; the skill verifies only.
5. Learnings — kept per-phase, made advisory, supersession marks added; not redesigned into a new system.
6. The mg-grant/net-grant infrastructure — reused as-is.
7. The close-out hook ("run B on the project just worked on?") — preserved as a phase-only invocation, alongside the new bounded `(closeout)` pass (B.6).

## D. Problem-to-solution mapping

| Change                                | Root causes and problems it removes                                                                                                   |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| One workflow skill, three phase specs | RC1 (one live scope read), RC2 (one governance header), A1–A7, B1–B6, C1, C3–C7, D2 (partly), RC5, and the five-problem merge cluster |
| Upgraded run frame                    | RC5, A3, A4, F4, F7, D8, and the false-alarm doctrine + three-kind flag taxonomy mapping RC1, C4, E1–E2; enforces the A→B→C order and the handover contracts |
| Canonical Phase-C tool                | RC3, D1, E2/E3/E4 as encoded rules, duration (no defect re-runs)                                                                      |
| Cupcake amendments                    | RC6, F1–F5, F8                                                                                                                        |
| Git-backed source                     | RC4, D2, C1, A7                                                                                                                       |

## E. Deliberately left out

1. D6 vendor-clone policy, D7 Global→Local re-examination, C2 alignment-log semantics, E1 out-of-corpus citations — developer rulings; the architecture is agnostic to their outcomes.
2. E5 dream-cycle staleness — operational gbrain item; the close protocol reports it.
3. B5 verified-date approval noise — dissolves into one grouped standard-tier item.
4. D3 low-yield vendor corpora — the per-cycle ceremony cost that made this painful is removed by the ceremony collapse.
5. F6 finer enforcement toggle — unnecessary once coexistence works; revisit only if a genuine need recurs.
6. A7 full learnings redesign — supersession marks and advisory precedence only.
7. Any new infrastructure: no scheduler, no orchestration platform, no generalized pipeline, no database.

## F. Implementation boundaries (not implemented in this session)

1. **Skills:** the workflow SKILL.md + three phase specs + absorbed aux files (finding/report/log templates) authored in the new source folder `C:\mybizz\mb-doccycle\`; the doccycle suite's remaining files (skill, exam-plan, exam-report, log, learnings) come through the config-management build-out (`config-setup-prompt`), not this remedy; the logs folder `C:\mybizz\logs\mb-doccycle\` is set up per the `mb-align-docs` example (run index, learnings, in-progress, last-completed-run, abandoned-runs); the three old skills retired after migration; the five docs-manager agent files retired.
2. **Shared material:** `doc-skills-run-discipline.md` upgraded (cycle frame, preflight, handover, report standard, count discipline, STOP interrupt, one-corpus-per-session) and MOVED into the doccycle suite (G3 option b), renamed to the suite's naming pattern; the mybizz-os-docs register row retired or updated.
3. **Cupcake:** rules authored in `C:\dev\project-library-global\rules-cupcake-global` following the existing file example, compiled to Rego via `mb-compile-rules`. One authored rule amended (commit mechanism per G1), one folder-list amendment; one new bin script (`git-grant`) plus its grants-data file; recompile and fidelity check; the cupcake config-docs suite updated; the stale `skills-collective` reference in the cross-project rule's always-open list corrected.
4. **Tool:** detection script + fixtures in the skills repo.
5. **Learnings:** one supersession sweep across the three existing folders.
6. **Config-docs:** the three skill doc suites replaced by the workflow suite.
7. **Unchanged:** scope list, grant infrastructure, GBrain, every other Cupcake rule.
8. **Pre-implementation reads** (inventory 8.3): the align-docs detector/writer aux files; docs-manager's five run logs.
9. **Acceptance test:** re-enable Cupcake; one controlled corpus cycle writing into a restricted folder with slips; one granted commit (or one developer-terminal commit); demonstrate the counters or their honest absence; run the dream cycle.

## G. Decisions — resolved 2026-09-21

1. **G1 commit coexistence — RESOLVED:** the commit-allowance grant channel is approved — a `git-grant` script cloned from `mg-grant` with configurable expiry, a new grants-data file, and a policy amendment; the authored rule text amended and compiled via `mb-compile-rules`.
2. **G2 data-mybizz-mgt — RESOLVED:** restricted-with-slip (the developer adopted the recommendation).
3. **G3 skill source homes — RESOLVED, one confirmation open:** the skill system files live in a source folder directly under `C:\mybizz\` per the developer's convention; the configured suite lives in `mybizz-config-docs\mb-doccycle\`; the shared run frame moves into the suite (option b). `doccycle-skill.md` is the config exam skill for doccycle, not the workflow skill source (developer correction). OPEN CONFIRMATION: the new source folder under `C:\mybizz\` needs its own private GitHub remote to satisfy the sealed GitHub-backed ADR and give the skill source off-machine backup — one-time `gh repo create sassycomapp/mb-doccycle --private --source=. --remote=origin --push`. Confirmation is needed because the earlier "no need to create a new GitHub repo" statement was made when we both believed `mybizz-config-docs` would host the source.
4. **G4 sub-agents — RESOLVED:** no sub-agents, no exceptions. The five docs-manager agent files are retired at migration; the read-only conditional-allow future option is dropped entirely (developer: "no exceptions").
5. **G5 / C2 alignment-log semantics — RESOLVED:** option B, approved-and-applied only. The run working record and the run index row carry the complete decision record.
6. **G6 name — RESOLVED:** `mb-doccycle` approved. Grammar: `(all)` / `(corpus)` / `(phase corpus)` / `(closeout)`.
7. **G7 quarantine — RESOLVED:** the exception is on the live scope list (verified); quarantine links remain as written prose, never converted.

## H. Review recommendation

Review and agree on: the one-workflow-three-phase shape. All seven section-G decisions are resolved; one confirmation remains — the GitHub remote for the new skill source folder under `C:\mybizz\` (G3). Then a Build planning session produces the implementation plan in this order: run frame upgrade and move → Phase-C tool (test-first against the defect fixtures) → phase specs and re-authoring in the source folder → Cupcake amendments → learnings sweep and config-docs suites → migration of run records and logs-folder setup. The acceptance test is the controlled Cupcake-on validation run.

---

**Completion report:** The proposal file is the living deliverable; amendments are applied on developer approval. The two suite filename typos were corrected on the developer's explicit instruction (2026-09-21). No other skill, run-frame, or Cupcake implementation was performed.

**Next Steps:** Developer confirms the single remaining item — the private GitHub remote for `C:\mybizz\mb-doccycle\` (G3). After that confirmation, a Build planning session converts section F into the implementation plan (actor: Build, planning only until approved).
