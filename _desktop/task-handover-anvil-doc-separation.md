---
document: Task Handover — Anvil Canonical / Learnings / Project Documentation Separation
status: Queued, not started
---

# Task Handover — Anvil Canonical/Learnings/Project Documentation Separation

**Status:** Queued, not started

**Origin:** Includes but not limited to exploration of `https://github.com/anvil-works/anvil-agent-references` against the existing Mybizz spec/ADR library.

**Scope:** Includes but not limited to all `specifications-global`, `policy-global`, project-specific specs (mb-3-cs `docs/`), and the ADRs not yet reviewed for this purpose. Design-side documents (`DESIGN.md`, palette tokens, M3 component mapping, screen production standards) are included in this project — they form part of the core skills and specifications base and are not excluded from the audit.

---

## Objective

Install `anvil-agent-references` (`https://github.com/anvil-works/anvil-agent-references`) as a live Anvil-mechanics source in OpenCode, then re-architect the existing documentation library so Anvil framework mechanics are never duplicated by hand — only Mybizz's own decisions and empirically-discovered gotchas are.

**Single source of truth, always.** No fact about Anvil mechanics, Mybizz-wide policy, or project-specific behavior lives authoritatively in more than one place, at any point in this project or after it. Where this plan's own categories risk creating a second home for the same fact, the reference-only rule (see Bucket 3 / Class 3.3 below) is the mechanism that prevents it — not a principle to be balanced against convenience later.

---

## Step 1 — Install

Symlink the relevant `skills/` subfolders (`server-code`, `client-forms`, `data-models`, and any others shipped) into OpenCode's skill directory, and copy the required sections of the repo's `AGENTS.md` into the project's own `AGENTS.md` per the repo's own setup instructions. (Already scoped in a prior conversation — not re-derived here.)

**Status update (2026-08-09): this step has been elevated and executed separately — see `master-task-list.md` Section 6. Do not execute it again as part of this document; it is retained here only as part of the original full design context.**

---

## Step 2 — Audit taxonomy

Every existing spec, policy, and ADR gets classified, section by section (not whole-document), into exactly one of four buckets. This taxonomy applies uniformly and identically across every document type in scope — specs, policies, and ADRs alike. No document class is presumed in advance to land predominantly in any one bucket; the classification is determined by what the audit finds, not by what kind of document is being audited.

| # | Category | Definition | Worked example |
|---|---|---|---|
| 1 | **Pure Anvil mechanics** | Documented, current Anvil framework behavior, no Mybizz content | Form file structure, Uplink connection pattern, deployment environment branching |
| 2 | **Anvil-derived learnings** | Empirically discovered behavior/gotchas not documented anywhere by Anvil — found by building, not by reading | Skulpt module quirks table (`re`, `json`, `datetime` gaps vs CPython); `app_tables` resolution failure under a shared-template dependency model; the Globals Contract pattern |
| 3 | **Anvil mechanics + Mybizz addition riding on top** | A real Anvil mechanism, with a project-specific threshold/rule/example layered on it. The underlying Anvil mechanic is referenced by file path back to Bucket 1/2 source material — it is never re-written or restated inline; only the Mybizz-specific addition is authored text. | Background task decorator (Anvil mechanic, referenced by path) + the 22-second/75%-of-timeout threshold rule (Mybizz addition, authored here) |
| 4 | **Not Anvil mechanics at all** | Business logic, RBAC roles, naming, regulatory posture, integrations, architecture decisions — Anvil is irrelevant to whether this is true | Vault system, five-app model, nomenclature, Brevo/Stripe/Paystack patterns |

A section mixing two buckets is a defect in the source doc, not an audit edge case — split it during the pass.

---

## Step 3 — Target document structure

Re-file the four buckets into five document classes:

| Class | Contents | Source |
|---|---|---|
| **3.1** | Anvil canonical specs/methods *covered by* `anvil-agent-references` | Not authored — accessed directly via the installed skill. No local copy. |
| **3.2** | Anvil canonical specs/methods *not covered by* `anvil-agent-references` | Bucket 2 (learnings) content. New document class — needs a name/location decision. |
| **3.3** | Mybizz-specific additions riding on top of Anvil canon | Bucket 3 content, trimmed to the addition only, referencing 3.1/3.2 by file-path pointer — never restating the underlying Anvil mechanic inline |
| **3.4** | Mybizz global specs, not Anvil-canonical, not project-specific | Bucket 4 content currently in `specifications-global`/`policy-global` that's genuinely cross-project (Vault, RBAC model, nomenclature pattern, testing methodology) |
| **3.5** | Project-local specs, not Anvil-canonical, not Mybizz-global | Bucket 4 content specific to mb-3-cs only (its actual RBAC role matrix, its actual schema, its actual test plan) |

Rule for 3.3: it incorporates 3.1/3.2 content **only by reference**, never by restatement — this is the mechanism that prevents the original duplication problem from recurring, and is the direct expression of the single-source-of-truth requirement stated in the Objective.

---

## Step 4 — Deliverable

A docmap + documentation register covering 3.1–3.5: what exists, which class it belongs to, where it lives, what it points to. Same prosthetic-memory pattern as existing docmaps/inventories — not a new format to invent.

---

## Not yet designed (pick up here on resume)

- The actual workflow steps (sequencing, agent roles, checkpoints) for running the audit across the full document set
- The specific prompts for the audit pass — to be reconsidered when this task is undertaken, not decided in advance
- Where Class 3.2 physically lives (new top-level folder vs. a section convention in `specifications-global`) — undecided
- Confirmation, by actual sampling once the task starts, of how the ADR set distributes across the four buckets — no distribution is assumed ahead of running the audit

---

## Explicitly in scope

Design-side documents — `DESIGN.md`, palette tokens (`palette_selector_tokens.md`, `DESIGN_palette_section.md`), M3 component mapping, M3 theme spec, screen production standards — are core to this project's audit, on the same four-bucket basis as every other document.
