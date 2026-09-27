# **Agent's assessment of the plan:**

Plan-text fixes

1\. Obsolete registration vs append-only model (§10, §18) Replace "Removing obsolete registration" with retire-in-place semantics consistent with the four-event model:

Obsolete row (document gone): set state: Retired in place, superseded-by where known. Never delete the row .

Wrong-register row: retire the wrong row in place + append the correct row in the correct register.

Both are mechanical, safe, verifiable, and preserve append-only discipline. If the correct register or supersession target is not determinable → Requires human judgement.

Apply to §10's example list, §6's repair wording, and §18's "Obsolete registration" expected result.

2\. Register universe (§6) Add: "The register universe is discovered live using the maintainer's rule — each project library's root register-local.md, plus register-global.md for project-library-global. The current known inventory is the six files in register-paths.md. pdlf-register.md is outside the inventory; if a C:\\pdlf audit scope encounters it, surface as a finding for human judgement." §6's named libraries remain examples, not an exhaustive list.

3\. Anvil/anvil.yaml exclusion (add to §5, §15 governance header, §18) Add: "Any folder containing anvil.yaml is never documentation; anvil.yaml itself is never read, written, or touched. The estate scanner excludes such folders by class rule inherited from the scope authority." Add one §18 walkthrough: Anvil repo present → not scanned, no findings generated.

4\. Source repo (§17 + §19 Phase 3) Add: "Create source repo C:\\mybizz\\mb-doc-auditor (git init, GitHub remote — mandated by ADR adr-dev-tooling-source-repos-must-be-github-backed) containing the SKILL.md source, tool/, and tests/; install the SKILL.md copy to \~/.config/opencode/skills/mb-doc-auditor/." This makes Phase 3 include git init/commit/push — you'll be asked for authorization at that gate.

Pre-locked decisions (§16 deferrals)

5a. Audit-record location: C:\\mybizz\\mybizz-config-docs\\mb-doc-auditor\\doc-auditor-records.md — one append-only block per run (date, scope, checked, findings by classification, actions, terminal state); register row on creation, mirroring the maintainer run-log's treatment.

5b. Schedule trigger (D4): v1 = explicit request and defined audit condition only (condition stated by you at invocation). "Defined schedule" recorded as future/not established — no scheduler exists in this environment; building one is out of scope.

5c. Corpus-copy location (Phase 4): C:\\data-mybizz-mgt\\tmp-doc-auditor-walkthroughs\\ — tmp- prefix makes it O3-exempt; outside all six corpora; removed after walkthroughs.

5d. G-brain CLI boundary: add a "G-brain reader" capability to §16: read-only calls only (gbrain sources list, gbrain orphans) for G9/G10 verification within the selected scope; never writes to G-brain. CLI unavailable → classify as Can wait; audit still completes.

6\. Run-log reader lock: hard-wire to C:\\mybizz\\mybizz-config-docs\\mb-doc-maintainer\\doc-maintainer-run-log.md (the §10 path — not the unrelated doc-maintainer-log.md in the same directory). Absent or empty log → "no maintenance history available"; audit proceeds.

Next: say the word and these get applied to the plan document, then implementation can start.

\---

**User's response:**

All your recommendations are acceptable, and you can fold them into the plan

The folder for your installation files is this one: "C:\\mybizz\\mb-doc-auditor"

See this example: "C:\\mybizz\\mb-doc-maintainer"

Take note of this: This file "C:\\mybizz\\mb-doc-maintainer\\mb-doc-maintainer-skill.md" is not merely called "skill.md". when you install this skill.md file in its proper installation location, then it will be called "skill.md" and the front matter will include the relevant front matter material. (see the installed doc-maintainer skill.md fornt matter) However, in this specific location,("C:\\mybizz\\mb-doc-maintainer\\mb-doc-maintainer-skill.md") which I'm indicating here, the front matter only includes "title" and "doc-id". This is an important distinction, or you will have a blockage

This folder is home to the documentation for the mb-doc-auditor skill: "C:\\mybizz\\mybizz-config-docs\\mb-doc-auditor"

Add a phase at the end of your development to populate these three currently empty documents:

"C:\\mybizz\\mybizz-config-docs\\mb-doc-auditor\\doc-auditor-reference.md""C:\\mybizz\\mybizz-config-docs\\mb-doc-auditor\\doc-auditor-config.md"

"C:\\mybizz\\mybizz-config-docs\\mb-doc-auditor\\doc-auditor-explainer.md"

Following these examples:

"C:\\mybizz\\mybizz-config-docs\\mb-doc-maintainer\\doc-maintainer-reference.md""C:\\mybizz\\mybizz-config-docs\\mb-doc-maintainer\\doc-maintainer-config.md""C:\\mybizz\\mybizz-config-docs\\mb-doc-maintainer\\doc-maintainer-explainer.md"

Add a phase to your plan to apply MB-config-manager to MB-Doc-Auditor as follows:

"C:\\mybizz\\prompts\\config-setup-prompt.md"

"C:\\mybizz\\mybizz-config-docs\\mb-config-manager"

\---

**Agent's amendments to the plan:**

Amendments to "mb-doc-auditor — Complete Consolidated Plan.md"

A. D4 (§3) — trigger: "defined schedule" becomes future/not-established; v1 triggers = explicit request + defined audit condition (condition stated at invocation). No scheduler exists in the environment; building one is out of scope.

B. §6 — register universe: append: registers are discovered live using the maintainer's rule (each project library's root register-local.md; register-global.md for project-library-global); the current known inventory is the six files in register-paths.md; pdlf-register.md is outside the inventory — if a C:\\pdlf scope ever encounters it, surface as a finding for human judgement.

C. §10 + §18 — obsolete registration: replace "Removing obsolete registration" with retire-in-place: obsolete row → state: Retired in place (superseded-by where known), never row deletion; wrong-register row → retire in place + append the correct row in the correct register; correct register or supersession target not determinable → human judgement. §18 expected result updated to match.

D. §15 governance header + §5 — Anvil exclusion: "Any folder containing anvil.yaml is never documentation; anvil.yaml itself is never read, written, or touched. The estate scanner excludes such folders by class rule inherited from the scope authority." Add §18 walkthrough: Anvil repo present → not scanned, no findings.

E. §16 — capability locks:

Scope reader → C:\\mybizz\\mybizz-os-docs\\os-reference-docs\\mybizz-scope-list.md, read live.

Run-log reader → hard-wired to C:\\mybizz\\mybizz-config-docs\\mb-doc-maintainer\\doc-maintainer-run-log.md (not the unrelated doc-maintainer-log.md in the same directory); absent/empty → "no maintenance history available", audit proceeds.

Audit record → C:\\mybizz\\mybizz-config-docs\\mb-doc-auditor\\doc-auditor-records.md, one append-only block per run; register row on creation.

New row — G-brain reader: read-only CLI only (gbrain sources list, gbrain orphans) for G9/G10 within scope; never writes; CLI unavailable → Can wait, audit still completes.

Estate scanner exclusions: anvil.yaml folders, tmp-, stencils, quarantine, backups, catalogue, logs (maintainer's exempt classes).

F. §17 — installation rewritten:

Source repo C:\\mybizz\\mb-doc-auditor (git init + GitHub remote, per ADR adr-dev-tooling-source-repos-must-be-github-backed; git operations at your authorization).

Skill source file is mb-doc-auditor-skill.md — corpus two-field frontmatter only (title/doc-id = filename stem), mirroring mb-doc-maintainer-skill.md. Installation transforms it: \~/.config/opencode/skills/mb-doc-auditor/SKILL.md with OpenCode frontmatter (name: mb-doc-auditor, description with triggers). The source file is never installed verbatim under the SKILL.md name — this is the blockage you flagged, now written into the plan.

Documentation folder: C:\\mybizz\\mybizz-config-docs\\mb-doc-auditor.

G. §18/Phase 4 — corpus-copy location: C:\\data-mybizz-mgt\\tmp-doc-auditor-walkthroughs\\ (O3-exempt; outside all corpora; removed after walkthroughs).

H. §19 — two new phases appended:

Phase 7 — documentation suite: populate doc-auditor-config.md (the spec — single source of expected values), doc-auditor-reference.md, doc-auditor-explainer.md in the docs folder, following the doc-maintainer-\* three-doc examples; corpus two-field frontmatter; register row in the mybizz-config-docs register. Gate: suite matches the examples.

Phase 8 — config-management: named step adds the mb-doc-auditor row (state WIP) to config-manager-register.md (authority: your instruction, doc-maintainer S-1 precedent), then executes C:\\mybizz\\prompts\\config-setup-prompt.md with {system} = mb-doc-auditor: Phases 0–5 (suite build-out to the 8-file standard, install mb-config-doc-auditor with hash pair, formal run #1, per-item gate, close-out). That prompt's standing rules apply verbatim. Gate: exam result + dispositions recorded.

Notes

Phases 0–6 stay as written; 7–8 follow your "end of development" instruction. Phase 8 ends with the config-manager routine's standard asks (commit+push, sync-gbrain).

Time shape: Phases 0–6 are quick because tooling, contract, run-log, registers, and scope authority all exist and match. Phase 8 is its own full session per the proven prompt pattern.
