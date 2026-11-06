---
title: "session-handover-2026-11-04"
updated: "2026-11-06"
doc-id: "mb-67a2e777"
---
# Session Handover — 4 November 2026

## 1. What Is Being Built

- David builds PDLF (his app factory) and builds `mb-3-cs` App 1 through it at the same time.
- PDLF is the primary objective. `mb-3-cs` is the vehicle.
- `mb-3-cs-project-context` and `project-library-global` are law. On a conflict, stop and ask.
- Credo: simple, secure, robust, fit for purpose. Do it once, do it right.

## 2. Where the PDLF Run Stands

- The PDLF run of `mb-3-cs` (run `app1`) is at Step 15, section 3, `/plan-eng-review`.
- Steps 11, 12 and 14 are complete.
- David answered D1 with A.
- Still to decide in Step 15:
  - R1: `created_at` on 7 tables. Recommended answer: add them through the new-columns migration prompt P11.
  - R2: a metadata column on the "core tables" under common aspect 4. Decide once the agent lists the tables.
- Then: answer the remaining review findings, check the reviewed plan, close out.
- The run pauses after the Step 16 `domain-locked` gate until Phase C is designed.
- Before the Step 16 gate: review the whole Phase B record from GitHub.

## 3. Held Files (send after Step 15 ends, already approved)

In the previous session's scratchpad folder `batch4/`, to be regenerated if lost:

| File | Path | Change |
|---|---|---|
| `adr-webhook-architecture.md` | `C:\dev\project-library-global\adr-global\` | Reconciliation hourly becomes every 5 minutes |
| `spec-component-properties.md` | `C:\dev\project-library-global\specifications-global\` | `SidesheetContent` approved as the Sidesheet of `NavigationDrawerLayout` and `NavigationRailLayout` |
| `sec-email-service-trust-boundary.md` | `C:\dev\project-library-global\security-global\cloud\` | Rewritten for Amazon SES and SNS |
| `sec-requirements-third-party-integration.md` | `C:\dev\project-library-global\security-global\requirements\` | Brevo becomes PayPal and Amazon SES |
| `sec-regulatory-compliance-cloud-processors.md` | `C:\dev\project-library-global\security-global\cloud\` | Brevo becomes AWS (SES) and Cloudflare |

The R1 and R2 schema fixes go out with these, with one commit line.

## 4. Working Pipeline (Governance)

- David and Claude settle concept and design together.
- Claude refines files and writes OpenCode prompts. David saves, commits and relays.
- David returns OpenCode's output. Claude assesses it.
- Only David commits. No agent has carte blanche.
- Known failure modes: OpenCode loops and goes in circles. Claude rushes and acts before thinking.
- Rules proposed (not yet approved):
  - every Claude proposal names the source line it serves;
  - every handover lists files and exact changes;
  - Claude ends each handover with "Checked against" and "Not checked";
  - OpenCode runs plan mode first, stops after the same failure twice, and touches only named files;
  - Anvil agent prompts are written by Claude, approved by David, and its changes reviewed after David pulls.
- Claude can read every `sassycomapp` repo (all public). This session could not write to GitHub.
- A read-only GitHub token was made by mistake and pasted in chat. David must delete it in GitHub: Settings, Developer settings, Personal access tokens, Fine-grained tokens.

## 5. Phase C: UI Concept (Under Discussion, Nothing Agreed)

David's concept, in his words:

1. Claude takes `DESIGN.md`, the M3 standards and the Anvil documentation on forms, and creates the forms for one feature (for example auth, analytics, blog). David and Claude scrutinise them until agreed. Claude may build a skill for this.
2. Claude puts the forms into `mb-3-cs-app1` and hands the Anvil agent a task instruction and specification sheet.
3. The Anvil agent verifies the UIs and wires up the forms.

Context David has set:

- The UI is built entirely on the full M3 custom theme dependency (`m3-custom-theme`), 100% Material 3 compliant. The old Anvil M3 theme and old UI standards are not the basis.
- Every UI is built from one known component set with known properties.
- The Anvil agent is Claude and works from HTML.
- The existing App 1 forms are wrong and will be replaced.
- OpenCode is not suited to producing the forms.
- The UI requirements and standards are written up where they are missing.

Claude's last three comments, awaiting David's view:

1. The Anvil agent should wire, not verify, because it is Claude checking Claude. The real check is David viewing the forms in Anvil.
2. The Anvil agent's strength is working inside the running app, so wiring suits it.
3. The form skill belongs to PDLF as a written step, so every app is built the same way.

## 6. Facts Established by Research

- **Magdoub wireframe skill** (`Magdoub/claude-wireframe-skill`, installed as `wireframe`, PDLF steps C22 and C26): a Claude Code skill. Its "five agents" are helper copies of the running agent, one per option, using Claude Code's `general-purpose` helper. It outputs generic HTML and CSS mockups with no knowledge of Anvil or M3. Its Polished variant breaks M3.
- **Anvil agent**: runs in the Anvil editor on the user's own Claude or ChatGPT account. Taught by `anvil-works/anvil-agent-references`. Accepts text, audio and images. Commits automatically; no other git operations. Cannot apply Data Tables schema changes (done by hand in the Data Tables view). Cannot read Secrets or edit table data.
- **Anvil forms** can be HTML templates (`form_template.html`) naming components such as `m3._Components.Card`. They display only inside Anvil. App 1 holds 91 forms in YAML and 2 in HTML.
- **`m3-custom-theme`** keeps Anvil's package name `m3` and component paths. Its new components (Dialog, Chip, Tabs, Snackbar, FloatingActionButton, ListItem, TopAppBar, NavigationBar, ButtonGroup, Badge, LoadingIndicator, and more to come) are documented in `m3-custom-theme-project-library/docs/components/`. Anvil's agent references cover only the base theme's components.
- **Current PDLF Phase C (C17–C28)** was planned for the old era: five Magdoub options per screen with colour variants, then screen HTML (C27), then PNG (C28) for Anvil's AI. To be redesigned once the UI concept is agreed.
- Relevant specs: `project-library-global/specifications-global/spec-screen-and-wireframe-production-standards.md`, `spec-screen-production-standard.md`, `spec-m3-design-standards.md`, `spec-m3_component_mapping.md`, `spec-ui-standards.md`, `spec-material-3-theme.md`.

## 7. Other Open Items

- David supplies the full M3 theme component list (from his separate theme session) before Phase C is built.
- The M3 theme project stays out of MyBizz, GBrain, close-out, commit-all and `repo-organization.md`.

## 8. How to Work With David

- Short replies. Simple sentences, numbered points under short headings. Concept level when he is conceptualising: no technical knots.
- Never restate what he said. Add only what is new.
- Check the source (repos, catalog, live system) before asking him anything or claiming anything.
- Never assume. Never act, write files, give commands or prompts without his express permission.
- Instructions in strict top-to-bottom order. Every command starts with `cd`.
- Every question carries a recommended answer and its reason.
