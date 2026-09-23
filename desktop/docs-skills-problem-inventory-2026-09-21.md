# Docs-Skills Problem Inventory — 2026-09-21

Handoff document for the next session. Covers mb-docs-manager, mb-align-docs,
mb-wikilinks. Built from: the three installed skills and their auxiliary files,
every run record (mb-wikilinks run-log + working record 20260920T100155, align-docs
run-index and the 2026-09-19 run records, the abandoned 2026-09-17 sweep, docs-manager
logs listing), the learnings folders, the config-docs suites, session page
sessions/2026-09-21-012-mb-wikilinks-full-run, the developer's own note
(desktop/Agent disobediance issue.md), and this session's rulings.

Confidence marks: CONFIRMED (evidence in hand) / LIKELY (consistent sources) /
UNCERTAIN (inference, needs investigation). Facts in dispute are stated as disputes.

---

## 1. Plan (methodology used)

- Sources were examined in three layers: (1) the skills' own text — what they
  currently instruct; (2) the run records — what they actually did and what went
  wrong, from append-only logs and git history; (3) the developer's rulings —
  what the skills were supposed to do. Information that shows skill behaviour
  failing, deviating from intent, or producing unverified work was kept; trivia
  was dropped.
- History was reconstructed from the append-only run logs and git commits named
  after the skills (back to August). Conflicts between record and recollection
  are surfaced, not resolved silently.
- Every problem was treated as cross-skill until proven local: the three skills
  share one run frame, one scope list, one resolver universe, one developer.
- Confidence marks distinguish confirmed from inferred; "resolved" requires
  evidence the fix landed and held; "proposed but unvalidated" is kept separate.
- Root-cause grouping came after collection. Duplicates were merged as one
  problem with multiple manifestations.

## 2. Context reconstructed (short)

- The 2026-09-19 refactor gave mb-align-docs and mb-wikilinks a shared run frame
  (doc-skills-run-discipline.md), scope from mybizz-scope-list.md, es.exe-first
  search, and the [[basename|Display Text]] format. mb-docs-manager (v12,
  2026-09-17) was NOT refactored — it still self-contains its own older machinery.
- The full mb-wikilinks run (2026-09-20/21) applied 2,004 links + 16 pointer
  blocks across 15 cycles with zero renames/moves/deletes; every defect it hit is
  logged in the run log.
- The developer issued four structural rulings on 2026-09-20 (cross-corpus
  referencing normal; quarantine = retired-but-valuable still citable; F-MK1
  healed-prose pattern stands; the skills' charter is A/B/C only) — saved as
  governed facts and now governing the skills, but the skill TEXT still says the
  opposite in places.
- The developer's friction diagnosis (Agent disobediance issue.md): agent obeys
  task-internal rules over developer rules; long-context erosion of distant
  instructions; completion pressure beats asking; Cupcake binds because it is
  in-path; uncovered write paths were treated as permission.

## 3. Problem inventory

### Group A — cross-skill charter and governance

**A1. Skill text contradicts developer intent (the "rotten foundation").**
Skills: all three. CONFIRMED.
- Observed: mb-align-docs SKILL.md still carries the "Local→Local cross-project:
  never live — Quarantine copy" directionality row (mirrored in
  align-docs-reference.md and align-docs-explainer.md, which I rewrote on
  2026-09-20 — my own rewrite carried the stale rule). mb-wikilinks SKILL.md
  still treats quarantine references as drift items. Both superseded by the
  2026-09-20 rulings (facts 040/041) — text unchanged.
- Expected: skill text matches the developer's clarified model.
- Why it matters: the next agent will follow the written rule, not the ruling —
  this is the exact mechanism that produced the F-MK1 conflict and the risk of
  re-creating healed violations.
- Status: OPEN (corrections proposed, awaiting developer instruction).
- Dependencies: root cause RC1/RC2 below.

**A2. Skills mandate unreadable output at scale.**
Skills: all three. CONFIRMED.
- Observed: mb-wikilinks' report format is per-file/per-line by construction
  (190+ entries presented once); docs-manager's reporting standard ("no vague
  quantifiers — every folder and document named individually") is the same
  failure mode; align-docs' two-tier grouping helped but still produced walls.
  The developer repeatedly could not process the output and fell back to
  blanket approval — which removes the human check the approval gate exists to
  provide.
- Expected: reports in plain English, lead with the decision, short.
- Partial mitigation used in-session (unvalidated as standard): plain-English
  per-corpus report files + a 3-question decision protocol.
- Status: OPEN.

**A3. Run duration explosion (hours of work → days/weeks).**
Skills: all three. CONFIRMED.
- Observed: the wikilinks run spanned two days over 15 cycles; align-docs and
  docs-manager runs historically similar. Causes: full ceremony per
  leaf-folder cycle (backup→report→approval→apply→verify→commit→log→learnings);
  detection re-run after my own errors; detection on unvalidated foundations.
- Status: OPEN. Structural, not behavioural — the ceremony is per design.

**A4. Developer governance is not present at the point of failure.**
Skills: all three + environment. CONFIRMED.
- Observed: AGENTS.md/workchat rules sit at top-of-context and erode; skill
  text sits in-hand and wins; no skill carries the communication rules; no
  STOP-interrupt exists in any skill; Cupcake covered Edit-tool writes but not
  python-in-bash writes (I wrote every corpus file through python heredocs).
- Proposed fixes (unvalidated): put the developer's rules in the first lines of
  each skill file; add the STOP hard-interrupt; extend Cupcake to the
  python-in-bash path; one-corpus-per-session.
- Status: OPEN.

**A5. Sub-agent design contradiction.**
Skills: mb-docs-manager vs mb-align-docs. CONFIRMED.
- Observed: docs-manager Section 8 mandates five sub-agent files (they exist on
  disk — verified); align-docs V2.1 says write-classes are permission
  disciplines "never spawned as sub-agents (standing workchat rule 8)";
  workchat rule 8 says no sub-agents, ever.
- Status: OPEN — one of the two must change; developer decision.

**A6. GBrain sync discipline differs per skill.**
CONFIRMED, minor: docs-manager Hard Constraint 3 forbids sync (offers the
script at Phase 9); align-docs/wikilinks sync per source at close. Consequence:
docs-manager runs leave the brain stale unless the developer opts in.

**A7. Learnings override SKILL.md (docs-manager Section 4.2).**
LIKELY risk: agent-written learnings files steer future runs; learnings
accumulate without supersession marks (align-docs has 16, some superseding
others; wikilinks has pre-refactor learnings still containing the retired
plain-[[stem]] clause — marked superseded only in NEW learnings, not in the old
files). A future agent reading the old file may follow the retired rule.

### Group B — mb-docs-manager specific

**B1. Stale embedded scope copy + wrong pinned scaffold path.** CONFIRMED.
- Section 1.1/1.3: scaffold path stated as
  `C:\data-mybizz-mgt\_desktop\mybizz-scope-list.md` — no such path (folder
  renamed 2026-09-15, fact-57; scaffold since moved to
  mybizz-os-docs\os-reference-docs\ by the 2026-09-19 refactor). The embedded
  scope copy is the pre-2026-09-19 revision: `C:\pdlf` listed OUT of scope,
  mb4ecom-library out, memory-audit-reports in — all three contradict the
  current list.
- Impact: Phase 0 cannot read the scaffold at the stated path — the run either
  fails or proceeds on the stale embedded copy while believing it read the
  scaffold.
- The skill's own defence ("read the scaffold, not this summary... flag
  discrepancies for a SKILL.md update") does not cover the pinned PATH being
  wrong.

**B2. Pre-refactor skill body.** CONFIRMED. mb-docs-manager (v12, Sep 17) never
received the Sep 19 refactor: own resume/checkpoint/two-tier/commit-plan/grant
machinery in an older shape, no reference to doc-skills-run-discipline.md, own
scope model, own anomaly taxonomy. Alignment work unknown in scope.

**B3. Internal contradictions inside the skill.** CONFIRMED.
- Two log paths: Quick Reference says `C:\mybizz\logs\mb-docs-manager\`;
  Section 10 shows `C:\mybizz\logs\docs-manager\`.
- Active-repo sourcing: Section 1.1/3.1 say the 12-repo list from the scaffold
  drives the Phase 0 pre-flight; edge-case 14 says repositories are "derived
  from walk-time .git discovery, not from a maintained list".

**B4. Stale obsolete-destination path.** CONFIRMED text. Section 6 reference /
Phase 4b: "C:\dev\obsolete\ or C:\mybizz\Mgt\obsolete\" — "Mgt" is the
pre-rename name (fact-57). No 4b operation has exercised it yet (unexecuted).

**B5. Guaranteed approval noise.** LIKELY. Every run proposes a
`verified: <date>` bump on every docmap in scope — recurring low-value
findings the developer must approve.

**B6. docs-manager has not run since 2026-09-17.** CONFIRMED state. Its
last run predates the scope rewrite, this run's ~2,000 link edits, the
sessions/ folder appearing in project-library-global, config-setup-prompt's
move, and github-logs accumulation. Its next run will surface a large drift
backlog — expected, but the skill's scope copy (B1) is wrong for that run.

### Group C — mb-align-docs specific

**C1. Function-scope.md is locked at V2 (2026-09-10) and has no amendment
path.** CONFIRMED. SKILL.md V2.1 defers to it ("Full function rules:
mb-align-docs-function-scope.md"), but it predates: the shared run frame, the
es.exe mandate (SKILL.md Section 8 had to add it), the 2026-09-20 rulings, the
sub-agent ban, and the new format. The "locked" label has no defined procedure
for amendment — a process gap that guarantees drift.

**C2. Alignment-log semantics conflict.** CONFIRMED. align-docs-reference.md
(pre-refactor) says the log records every decision "including rejected and
skipped"; SKILL.md V2.1 says "one entry per approved-and-applied finding".
I carried the SKILL.md wording into my rewrite. Which is intended needs a
developer ruling — the difference is an audit-trail completeness question.

**C3. FM schema rules vs developer practice.** PARTIALLY RESOLVED, tension
remains. The 2026-09-19 run found the developer's own new standard violating
the schema (doc-id ≠ filename slug; a parent-doc relationship field vs "FM is
identity-only"). align-docs proposed heals; the record shows the standard was
committed with the conflicts surfaced. Rule-vs-reality tension will recur.

**C4. Register/home mismatches are a recurring class.** CONFIRMED recurring.
F-OS1 (os-docs register claiming files living elsewhere) resolved this
instance by RETURNING the explainers to os-docs (developer's choice) — but the
class recurred across corpora (desktop reconciliation, _desktop rows, dev-root
rows). Register rows assert a home; files move (developmental flux) → recurring
reconciliation work.

**C5. Census ambiguity vs developer's "same name, different folder is
legitimate" (F-MK3).** CONFIRMED ruling, not encoded: pol-testing-and-quality
exists twice (makepdlf + global), different content, developer says legitimate.
The blanket "colliding basenames never wikilinked" rule would bar legitimate
disambiguation-by-context conversions. Needs encoding with the F-MK3 nuance.

**C6. Count discrepancies inside align-docs runs.** CONFIRMED incident
(2026-09-19: "developer flagged the 21-vs-marker discrepancy"; reconciled to
24). The 2026-08-04 wikilinks learning already mandated count-from-the-list —
the class recurs; counting discipline needs a hard rule (every report's count
derived mechanically from the item list).

**C7. align-docs learnings: 16 files, no supersession marking.** LIKELY (see A7).

### Group D — mb-wikilinks specific

**D1. No canonical implementation — detection and apply are agent-improvised
each cycle.** CONFIRMED. The skill defines WHAT to detect but never HOW. Across
15 cycles I rebuilt the pipeline each time in python heredocs; the defects that
hit (CRLF stripping, space-in-filename splitting, self-ref filter silently lost
in one rewrite, substring collisions, double-occurrence tokens, malformed
bracket wrappers in corpus text, invisible-byte normalization, git add -A
sweeping a foreign file) are each implementation defects of a pipeline that is
rewritten per run. A canonical, tested detection/apply implementation (or
skill-level pseudocode with the hard invariants: backtick-first, line-precise,
byte-preserving, explicit-file staging) would have prevented most.

**D2. Skill-version churn.** CONFIRMED. Three versions in ten days (plain-stem
era → 2026-09-17 wide-sweep era → 2026-09-19 V2 refactor). The abandoned
2026-09-17 sweep burned a full run on a method voided two days later. The skill
has no version/deprecation discipline (not in git; superseded text remains
readable).

**D3. Low-yield vendor corpora run full ceremony.** LIKELY. anvil-docs: 6,309
tokens → 30 proposals; most candidates ambiguous. Expected outcome, but the
per-cycle ceremony cost stays constant.

**D4. Coincidental variant matches (right name, wrong meaning).** CONFIRMED
instance: README's `sessions-log.md` variant-matched a fact record about the
sessions log — the reference actually means the transient operations log.
Caught by judgment, not by the skill. Class remains open (no semantic-check
step).

**D5. Classes invented during the run, absent from the skill.** CONFIRMED:
PENDING-BUILD (unbuilt step refs = scheduled material, not missing docs);
historical/retired records; out-of-corpus-live references
(config-setup-prompt at C:\mybizz\prompts\ — cited 23×, unresolvable by
design); agents.md case-collision; blank-client-template app-name (from the
2026-08-04 learning, correctly applied). All should be treatment rules in the
skill, not run-time improvisation.

**D6. Vendor-clone targets.** UNCERTAIN policy question: links were created
into anvil-agent-references pages (registered source, but scope-list excepts
the clone as "supply"). If upstream changes, links drift. Needs a ruling:
convert into vendor clones or leave prose.

**D7. The 28 Global→Local flags from adr-global need re-examination under the
corrected model.** UNVALIDATED: they were recorded under the old rule; several
may be normal references per the 2026-09-20 rulings.

**D8. The skill's success metric was never demonstrated.** CONFIRMED gap:
end-of-run requires confirming `link_resolution_opportunity` /
`graph_signals_coverage` counters MOVED. I verified sync+extract+doctor ran,
but never showed the counters moving. Validation gap across all 15 cycles.
Related: gbrain doctor reports every source "never completed a full cycle"
(dream-cycle staleness) — the new links sit in chunks but resolver freshness
depends on the dream cycle, which has not run.

### Group E — shared infrastructure

**E1. Citations to non-corpus locations can never resolve.** CONFIRMED
(config-setup-prompt class). Options: register the location, move the file
back, or accept prose-only. Needs developer decision; recurs for any file
living outside registered sources.

**E2. Empty/pending files are excluded from the universe, so references to
them read as MISSING.** CONFIRMED (app-factory modules; makePDLF pending
steps). The PENDING-BUILD/derived-rendering classes cover it ad hoc; not in
skill text.

**E3. Case-insensitive filesystem vs case-sensitive matching.** CONFIRMED
(agents.md/AGENTS.md treated as distinct by the census but identical to
Windows).

**E4. es.exe coverage gaps.** CONFIRMED minor: WSL home (memory-governor)
not indexed (find fallback works and is reported); recycle-bin noise; stale
index risk mitigated by the report-the-fallback rule.

**E5. Dream cycle staleness.** CONFIRMED state: doctor reports all sources
never cycled (867h+). Not a skill defect, but resolver freshness for ~2,000
new links depends on it.

### Group F — Cupcake coexistence (added 2026-09-21)

Context: the developer disabled Cupcake (plugin rename + OpenCode restart,
per disable-enable-cupcake.md) to run the three documentation skills, and
stated this is not an acceptable standing solution. Investigation compared
the rules (project-library-global\rules-cupcake-global) and the cupcake
config-docs suite against the skills' actual workflows and this run's
observed behaviour.

**F1. The commit/push gate categorically conflicts with every skill's
mandatory per-cycle commit phase.** CONFIRMED.
- Rule: no_autonomous_commits_pushes_merges_releases_or_deployments — Deny
  any agent git commit/push "unless the developer has given explicit
  approval for that specific action in the current session".
- Observed enforcement: fact-56 (2026-09-15, lived) — "agent-run git
  commit/push ALWAYS denied by policy; developer terminal blocks only;
  question-tool approval does not satisfy it". This run performed 15
  commits + 15 pushes; impossible with Cupcake active.
- Root mismatch: the rule text's escape hatch (in-session approval) is NOT
  machine-verifiable — Cupcake evaluates PreToolUse calls mechanically and
  cannot know what was approved in chat. The written exception is
  unimplementable as written, so enforcement degrades to always-deny while
  the rule text says otherwise. This is a rule-design defect, not a
  Cupcake defect.
- Resolution directions (developer decision): a verifiable approval token
  the developer issues per commit set and Cupcake can read; or developer-
  terminal commits per cycle with the skills ending at a commit plan; or a
  documented always-deny stance with developer-terminal commits as the only
  path — the rule text and the enforcement must be made to say the same
  thing either way.

**F2. The bash-write rule names this run's exact write channel.** CONFIRMED.
- Rule: no_bash_mediated_file_writes_without_grant explicitly enumerates
  `python3 - <<` and `python3 -c` with `open(` — the precise channel this
  run used for every apply. The rule's own reason text records that the
  2026-09-11 enforcement review caught an agent doing bulk writes through
  Python heredocs — this run repeated that behaviour with enforcement off.
- With Cupcake on, every apply of this run would have been evaluated;
  denials per folder would have required grant slips (align-docs Phase 3a
  design).

**F3. The shared-library carve-outs would have covered most of this run —
the conflict is narrower than it looked.** CONFIRMED from rule text.
- Always-open (no slip needed): project-library-global, dev-root,
  mybizz-config-docs, mybizz-os-docs, logs, memory-audit-reports, /tmp, the
  cupcake/opencode control plane.
- Restricted (slip needed): makepdlf-project-library, mb-3-cs library,
  mb4ecom/mb5pdlf libraries, memory-governor, data-mybizz-mgt (not on the
  shared list — wait: data-mybizz-mgt is NOT on the shared-library list and
  IS a walk root; it is not in the restricted list either — the rule's
  restricted list omits it; a write to data-mybizz-mgt resolves outside cwd
  and outside shared libraries → denied without slip. CONFIRMED gap in the
  rule's own folder lists).
- Mapping to this run: ~1,577 of 2,004 writes (project-library-global,
  config-docs, os-docs) sit in always-open folders and would have flowed;
  ~427 writes (makePDLF 90, mb-3-cs 317, data-mybizz-mgt 20) would have
  needed ~3 slips — feasible per-cycle, but repeated per cycle across two
  days with ~30-minute slip expiry.
- The narrow read of the bash rule (writes outside the CURRENT PROJECT
  only) means a run whose cwd sat in a restricted folder would have needed
  slips even for shared-library targets — cwd-dependence the skills never
  state. UNVERIFIED (needs a live test with Cupcake re-enabled).

**F4. The wikilinks skill has no grant-handover section.** CONFIRMED gap:
align-docs (Phase 3a) and docs-manager (Phase 3a) both define the
slip-request design; mb-wikilinks SKILL.md has no equivalent — with Cupcake
on, a wikilinks run into restricted folders would hard-stop with no
designed recovery path.

**F5. Network rule vs git push is ambiguous.** UNCERTAIN: the rule blocks
"any tool call that performs an outbound network request (e.g. a fetch or
webfetch tool call)" to non-allowlisted domains. Whether Bash `git push`
to github.com is inspected depends on the compiled Rego, which was not
audited. If covered, this run's 15 pushes would each need a net-grant
github.com slip (count-limited, expiring) — a third categorical conflict.
If not covered, pushes flow. Needs one re-enable test to resolve.

**F6. Enforcement toggle is session-breaking.** CONFIRMED: disabling =
renaming the plugin + restarting OpenCode — mid-run toggle would lose the
session. That coarseness is itself why disablement persisted across the
whole run rather than being scoped to the conflicting operations. A finer
mechanism (per-policy suspension, session-scoped profile, or grant-based
bulk allowance) is the design gap, not the rules' existence.

**F7. No skill checks enforcement state at run start.** CONFIRMED gap:
neither doc-skills-run-discipline.md nor any skill reads whether Cupcake is
active before planning a run's write strategy. A run under disabled
enforcement silently loses the boundary (this run is the proof: the
git-add-A foreign-file sweep would have been blocked at commit time by the
commit gate).

**F8. Compiled-policy vs authored-rule fidelity unverified.** UNCERTAIN:
rules are authored as markdown in rules-cupcake-global and compiled to
Rego in ~/.config/cupcake/policies/opencode/ (mb-compile-rules pipeline).
Whether the compiled Rego implements each rule's stated exceptions (e.g.
the commit rule's in-session-approval escape hatch, which fact-56 says
never fires in practice) has not been verified. If the Rego hard-denes
where the markdown promises an exception, the two artifacts disagree — a
documented-behaviour vs actual-behaviour split that must be surfaced, not
assumed away.

**Further issues to be addressed (do not fit the existing groups):**
- The commit-gate escape hatch is unimplementable as designed (F1): either
  the mechanism gains a verifiable approval token, or the rule text drops
  the exception and the skills' commit phases are redesigned to hand a
  commit plan to the developer's terminal per cycle.
- data-mybizz-mgt is absent from both folder lists in the cross-project
  rule (neither always-open nor restricted) — its writes fall into an
  undefined zone; with Cupcake on, treatment would depend on the compiled
  Rego's default. CONFIRMED list gap.
- The doc skills' own grant-handover designs (align-docs, docs-manager)
  prove coexistence was designed — the failure is that (a) the slips'
  scale/expiry model fits surgical edits, not mass retrofits, and (b) the
  third skill never received the design. The fix is completion and scale
  design (per-run bulk allowance defined by the developer), not disablement.
- Cupcake's deny messages instruct "stop and obtain explicit developer
  approval" — but chat approval is not machine-readable back to Cupcake
  (see F1); the designed loop has a missing link: an approval surface
  Cupcake can verify.
- The 2026-09-11 enforcement review (cited in the bash rule's own reason)
already knew agents route bulk writes through Python heredocs — the
documentation-skill workflows that need bulk writes were foreseeable, yet
no bulk-compatible, verifiable path was designed for them. This is an
unresolved design gap, not a rule defect.

## 4. Problems believed to be resolved (with validation evidence)

- 2026-09-17 wide sweep voided cleanly — record intact in abandoned-runs. VALIDATED.
- V2.1 refactor of the two SKILL.md files + shared run frame + scope
  authority — in effect and exercised across 15 cycles. VALIDATED.
- Config-docs skill description files synced to V2.1 — commit bfc38b5. VALIDATED.
- disable-enable-cupcake FM-removal incident — resolved by relocation
  (commits 6460c13/ae44127). VALIDATED.
- workflow.md wrong retirement — corrected (commit 3f8ffd4). VALIDATED.
- F-OS1 explainers — resolved by returning them to os-docs (developer's
  choice; commit ae44127 shows the files returned). VALIDATED.
- All 15 conversion cycles' applications — validated by per-cycle gates
  (file gate, line gate, byte scan; counts verified per cycle).
- The four governed facts — promoted through the governor this close-out.

## 5. Problems with proposed but unvalidated solutions

1. Skill-text corrections for A1 (directionality row, quarantine rule,
   charter statement) — proposed, awaiting developer instruction.
2. Full re-creation of the three skills (developer's own suggestion) — the
   larger version of 1.
3. Point-of-action governance placement (rules at top of skill files),
   STOP hard-interrupt, Cupcake coverage of python-in-bash writes,
   one-corpus-per-session — proposed in-session, untested as durable changes.
4. Plain-English report format + 3-question decision protocol — worked
   in-session (developer engaged with every report after the change), not
   encoded in any skill.
5. Byte-exact apply-writer invariants (backtick-first, line-precise,
   bytes-preserved, explicit-file staging, never git add -A) — proven across
   the run's last cycles, exists only in learnings, not in skill text.
6. PENDING-BUILD + historical/retired + out-of-corpus-live treatment classes —
   used successfully, not encoded.
7. F-MK3 nuance ("same name, different folder is legitimate") for the census
   rule — ruled, not encoded.
8. Count discipline: every report's count derived mechanically from its own
   item list — mandated by a 2026-08-04 learning, still violated as late as
   2026-09-19 (21-vs-marker incident). Proposed hard rule, unvalidated.
9. Cupcake coexistence design (from Group F): a verifiable commit-approval
   mechanism (token or developer-terminal commit plan); a grant-handover
   section added to mb-wikilinks; a bulk-allowance design for mass-edit
   runs; github.com handling decided (allowlist entry, net-grant pattern,
   or developer-terminal pushes); enforcement-state preflight in
   doc-skills-run-discipline.md; data-mybizz-mgt added to one of the
   cross-project rule's folder lists. All proposed from evidence this
   session; none validated — and the honest test requires re-enabling
   Cupcake, which is the developer's action.

## 6. Cross-skill / root-cause relationships

RC1. **Skills were authored for a static corpus; the environment is a
multi-layer system in deliberate flux** (developer's layer model:
pre-makePDLF / makePDLF / PDLF / shipped estate). Every stale rule, remediation
posture, "missing document" false alarm, and register/home reconciliation
traces to this mismatch. A1, B1, C4, D5, E1, E2 all hang off RC1.

RC2. **Governance placement**: developer intent lives outside the failure
moment (AGENTS.md, workchat, standing instruction, separate procedures) while
task-internal rules live inside it. A2, A4, A7 hang off RC2. The mechanism is
documented in the developer's own note.

RC3. **No canonical implementation**: skills specify behaviour in prose; each
agent re-implements detection/apply per run; defects vary per implementation.
D1's whole defect family hangs off RC3.

RC4. **No version/supersession discipline for skill text, aux files, and
learnings**: skills not in git; "locked" aux doc unamendable; learnings
accumulate without supersession marks; config-docs suites drift. B2, C1, C7,
D2, E3 hang off RC4.

RC5. **Ceremony scale**: full lifecycle per cycle × many cycles × large corpora
= duration explosion and approval flooding. A3, B5, D3 hang off RC5.

RC6. **Enforcement-scope mismatch between Cupcake and the documentation
workflows**: the rules encode boundaries designed for coding-agent work
(commits, network, cross-project writes), while the doc skills mandate
per-cycle commit/push and mass-edit retrofits. Three concrete conflicts
(F1, F2/F3, F5), one design gap (F4), and one capability gap (approval
surface Cupcake can verify). Disabling Cupcake masks all six instead of
resolving them.

Consequence chains worth naming: RC1 + RC2 together produced the F-MK1
conflict and the 2026-09-17 voided run. RC3 + RC4 produced every
implementation defect in the run. RC5 is why the developer experienced days
where hours were expected.

## 7. Known information gaps and uncertainties

1. mb-align-docs' detector/writer/README aux files were not audited this
   session (only SKILL.md, function-scope head, and the templates list).
2. docs-manager's five run logs were listed but not read — earlier
   docs-manager defects (e.g. the "V7 run that performed a real delete",
   referenced in edge-case 18) are known only from the SKILL.md's own text.
3. Whether align-docs' F-OS3 register appends and FM heals all landed —
   commit ae44127 shows the files returned and register ops, but a row-level
   verification was not done.
4. Which of the 28 Global→Local adr-global flags should convert under the
   corrected model — developer ruling needed.
5. Vendor-clone linking policy (D6) — developer ruling needed.
6. Whether docs-manager's Phase 4b has ever executed in practice (the
   obsolete-move path) — its logs were not read.
7. The alignment-log semantics question (C2) — developer ruling needed.
8. The gbrain dream cycle has not run — resolver freshness for the new links
   unverified; the skill-level success counters were never demonstrated.
9. Compiled-Rego fidelity (F8): whether the compiled policies implement the
   authored rules' stated exceptions — unverified.
10. The live behaviour of the cross-project and bash-write rules under the
    actual run conditions (cwd-dependence, data-mybizz-mgt's undefined zone)
    — unverified until Cupcake is re-enabled for a controlled test.

## 8. Recommended next diagnostic step

In order of leverage:
1. Developer rulings on the open questions (A5 sub-agents; C2 log
   semantics; D6 vendor-clone targets; D7 G2L re-examination; E1
   out-of-corpus citations; the A1 text corrections; the Cupcake
   coexistence items in section 5.9) — these are decisions, not diagnostics.
2. Then the skill re-authoring the developer already proposed: re-create the
   three skills around the charter (A/B/C), the 2026-09-20 rulings, the
   point-of-action governance placement, the plain-English report standard,
   the byte-exact writer invariants, and the new treatment classes — with the
   skills under git so version churn (RC4) ends.
3. Before re-authoring: read the two unread sources (align-docs detector/writer
   aux files; docs-manager's five run logs) so the re-creation does not repeat
   their undocumented history.
4. After re-authoring: re-enable Cupcake and run the coexistence test —
   one small doc-skill cycle against a restricted folder with a grant slip,
   one developer-approved commit through whatever approval mechanism is
   designed — closing F1/F5's verification gap. Then run the dream cycle so
   resolver freshness catches up, and demonstrate the success counters
   moving — closing D8's validation gap.
