# BODY-PDLF: Harmonized Contiguous Strategy for Software Planning & Development

Date: 2026-06-30
Producer: OpenCode (direct)
Operating environment: Anvil.works, OpenCode, GStack (59 skills), GBrain (PGlite), Matt Pocock Skills (18), PDLF (17 stages), de Bono BODY (BFT).

---

## Operating Environment

| Layer | Tool | Role |
|---|---|---|
| Substrate | Anvil.works | Web app platform: Data Tables, Anvil Designer, Anvil AI, server-side Python |
| Agent host | OpenCode | The agent runtime; skills discovered from `~/.config/opencode/skills/` |
| Workflow | GStack (59 skills) | Planning, building, reviewing, shipping pipelines |
| Memory | GBrain (PGlite, 263–565 pages, federated sources) | Vector search over project docs + mb-3-cs code + GStack working state |
| Discipline | Matt Pocock Skills (18 skills) | Engineering rigor: grilling, domain-modeling, TDD, triage, handoff |
| Construction doctrine | PDLF (17 stages, 5 phases) | The stage-gated build sequence — stage 7 explicitly names LifeOS/OpenCode/GStack/Matt Pocock/Anvil |
| Thinking doctrine | de Bono BODY (BFT) | Per-decision thinking: bones, muscle, nerves, fat, skin, health |

---

## Part A — Opinionated Review

### What is genuinely strong

1. **The memory layer is real and working.** GBrain has 100% embedding coverage, federated sources spanning docs + code + working state, and is wired into OpenCode as MCP tools. This is the part most teams never build. It is the single biggest asset and the foundation any strategy must protect.

2. **GStack's pipeline shape is correct.** `/office-hours → /plan-ceo-review → /plan-eng-review → /plan-design-review → /plan-devex-review` (or `/autoplan`) is a sound planning sequence, and `/review → /qa → /ship → /land-and-deploy` is a sound ship sequence.

3. **PDLF is the right construction skeleton.** Stage-gated with controlled backward reopens (17→13/8/9/10) is the correct discipline. The five-phase grouping (Discover→Define→Design→Build→Validate) maps onto every credible software lifecycle. Stage 7's explicit naming of the tools is not coincidental — PDLF was written *to orchestrate this exact stack*.

4. **The two-repo split is principled.** `project-library` (planning/docs/ADRs/wireframes) and `mb-3-cs` (live Anvil code + anvil.yaml) is a clean separation. The AGENTS.md hard rule on anvil.yaml protection is the right guardrail.

### Where the stack has real problems

**Problem 1 — Two orchestrators, neither fully in charge.**
PDLF is a 17-stage doctrine. GStack has its own pipeline (`/autoplan` runs CEO+eng+design+DX reviews). These two are not reconciled. The question "does `/autoplan` replace PDLF stages 6–12, or run inside them?" has no documented answer. In practice this produces either double-planning or silent skipping. Both are waste.

**Problem 2 — The thinking layer is implicit and thin.**
Neither GStack nor Matt Pocock skills contain an explicit per-decision thinking discipline. `/office-hours` asks six forcing questions (good for *initiative-scale* direction). `/grill-me` and `/grill-with-docs` run adversarial interviews (good for *stress-testing* a plan). But there is no tool that says "before you commit this ADR, pick the bones, audit the muscle, lay the nerves, check the fat." This is the BFT-shaped hole. The result: micro-decisions inside PDLF stages are unexamined.

**Problem 3 — No persistent ideal-state artifact.**
PDLF stage 12 (Design Lockdown) freezes a baseline. PDLF stage 9 (PRD) is written once. But there is no *living* done-definition that evolves as learnings arrive — which is what LifeOS's ISA provides. The PRD gets locked; reality drifts; nothing reconciles them until stage 17 (retrospective), which is too late.

**Problem 4 — The LEARN loop is not closed.**
GBrain indexes. GStack brain-sync pushes working state. `/retro` and `/learn` capture learnings. But nothing *feeds those learnings back as input to the next initiative's planning*. LifeOS's self-improvement loop is the missing nerve. Today, the retrospective doc sits in `gstack-outputs/` and is searchable by GBrain — but no skill explicitly pulls prior learnings into `/office-hours` or `/plan-ceo-review` at the start of the next initiative. The memory compounds in storage but not in practice.

**Problem 5 — Anvil is treated as a late-stage substrate, not a bone-level concern.**
PDLF puts Anvil at stage 14 (Frontend Assembly) and stage 16 (Integration). But Anvil Data Tables *is* the data model (PDLF stage 10), and Anvil's server-side Python *is* the architecture (PDLF stage 8). Treating Anvil as a frontend tool that shows up in Phase C means data-design decisions get made in the abstract and then re-made when they hit Anvil's actual table/column/relationship primitives. This is a structural inefficiency.

**Problem 6 — GBrain health score is misunderstood by its own metrics.**
The 65–70/100 score is "expected for documentation" per the operating guide, but the score is designed for entity-based knowledge bases (people/companies). The brain stores ADRs and code. The metrics that matter (embedding coverage, search recall, freshness) are all green; the metrics that drag the score down (links, timeline, orphans, graph_coverage) are structurally inapplicable. This is not a problem to fix by forcing ADRs into entity patterns — it's a problem to *stop worrying about*. The score is measuring the wrong thing for this use case.

### Net assessment

The stack has all the mechanical pieces but they are **layered, not integrated**. PDLF names the tools at stage 7 but doesn't prescribe *how* GStack skills map to PDLF stages. GStack pipelines don't reference PDLF. BFT and LifeOS/ISA concepts aren't present as tools at all. The result is a stack where each layer works in isolation but the *contiguity* — the seamless handoff from thinking → planning → building → shipping → learning → thinking — has gaps at every junction.

---

## Part B — The Single Harmonized Contiguous Strategy

**Name:** BODY-PDLF — a contiguous, stage-gated, memory-compounding software development strategy that runs BFT inside every PDLF stage, uses GStack/Matt Pocock skills as the workflow primitives, GBrain as the persistent ideal-state + learning memory, and Anvil as the bone-level substrate from stage 8 onward.

**One sentence:** *PDLF sequences the work; GStack + Matt Pocock skills execute the work; BFT examines each decision inside the work; GBrain holds the ideal state and the learnings so the next initiative starts smarter; Anvil is the substrate that makes the bones real from architecture onward.*

### The Contiguous Loop (5 junctions, 0 gaps)

```
┌─────────────────────────────────────────────────────────────────────┐
│  JUNCTION 0 — LEARN (before anything starts)                        │
│  GBrain query prior learnings + ADRs + ISAs for this domain         │
│  Output: a "prior context" brief fed into Junction 1                │
├─────────────────────────────────────────────────────────────────────┤
│  JUNCTION 1 — THINK (BFT, per-decision, every stage)                │
│  Bones → Muscle → Nerves → Fat → Skin → Health                      │
│  Runs INSIDE every PDLF stage below (not a separate phase)          │
├─────────────────────────────────────────────────────────────────────┤
│  JUNCTION 2 — PLAN (PDLF Phases A+B, stages 1–12)                   │
│  GStack /office-hours, /autoplan, Matt /domain-modeling, /grill-w-d │
│  Produces: ISA (living ideal-state) + locked baseline v1            │
├─────────────────────────────────────────────────────────────────────┤
│  JUNCTION 3 — BUILD (PDLF Phases C+D, stages 13–16)                 │
│  Anvil Designer + Data Tables, OpenCode + Matt /tdd, /review, /qa   │
│  Produces: release candidate, verified against ISCs                  │
├─────────────────────────────────────────────────────────────────────┤
│  JUNCTION 4 — SHIP & LEARN (PDLF Phase E, stage 17)                 │
│  /ship → /land-and-deploy → /canary → /retro                        │
│  Learnings written to GBrain; ISAs updated; feeds Junction 0        │
└─────────────────────────────────────────────────────────────────────┘
```

The loop is *contiguous* because Junction 4 explicitly feeds Junction 0 of the next initiative. The gap that exists today (learnings captured but not re-entered) is closed by making the LEARN query a mandatory first step.

### Stage-by-Stage Mapping: PDLF × BFT × GStack × Matt × GBrain × Anvil

| PDLF Stage | BFT applied | GStack skill | Matt skill | GBrain role | Anvil role |
|---|---|---|---|---|---|
| **0. LEARN** (pre-stage, added) | Health scan on prior work | `/context-restore` | — | Query prior ADRs + ISAs + learnings for this domain | — |
| **1. Ideation** | Bones (broad): what exists? | `/office-hours` | `/ask-matt` | Query: "what did we try before?" | — |
| **2. Concept Synthesis** | Bones (big bones picked) | `/plan-ceo-review` | `/grill-with-docs` | Store concept statement | — |
| **3. Concept Expansion** | Nerves — Exploring network | `/office-hours` (Builder mode) | `/prototype` | — | — |
| **4. Concept Definition** | Bones (key-type) | — | `/domain-modeling` | Store domain terms → `CONTEXT.md` | — |
| **5. Concept Distillation** | Fat removal (3-question test) | — | `/grill-me` | — | — |
| **6. Project Framing** | Muscle — purpose decomposition | `/spec` | `/to-prd` | Store PCD | — |
| **7. Platform & Framework Selection** | Muscle — channel muscle (welcome Anvil) | — | — | Query prior platform decisions | **Anvil chosen here, not at 14** |
| **8. Architecture & Standards** | Bones (big) + Muscle (logic) | `/plan-eng-review` | `/codebase-design` | Store ADRs → `adr/` | **Anvil Data Tables schema drafted here** |
| **9. Product Planning** | Nerves — Achieving network | `/autoplan` (or manual pipeline) | `/to-issues` | Store PRD + ISCs | — |
| **10. Data Design** | Bones (key-type big bone) | — | `/domain-modeling` | Store data model doc | **Anvil Data Tables created here** |
| **11. Design Sanity Audit** | Health scan (good in itself?) | `/plan-design-review` | `/grill-me` | Query: prior audit failures | Validate against Anvil table limits |
| **12. Design Lockdown** | Skin — ISA published | — | — | **Store ISA as living doc in GBrain** | Freeze Anvil schema v1 |
| **13. UX/UI Design** | Skin (tree/necklace structure) | `/design-consultation` → `/design-shotgun` → `/design-html` | — | Store wireframes → `wireframes/` | Anvil Material 3 theme |
| **14. Frontend Assembly** | Skin + Nerves (Organizing) | `/design-review` | — | — | **Anvil Designer: build forms, wire components** |
| **15. Feature Development** | Nerves (Achieving, TDD) | — | `/tdd` | Query: code patterns that worked | Anvil server code + OpenCode TDD |
| **16. Integration & Refinement** | Nerves (Organizing, A+B=C) | `/review` → `/qa` | — | — | Anvil deployment + GitHub sync |
| **17. Validation & Release** | Health (good in itself + good for me) | `/ship` → `/land-and-deploy` → `/canary` | — | **Store learnings + update ISA** | Production validation |
| **17b. LEARN** (post-stage, added) | Health scan on this initiative | `/retro` → `/learn` → `/context-save` | `/handoff` | **Embed learnings; mark ISAs done** | — |

### The five non-negotiable rules

**Rule 1 — BFT runs inside every stage, not as a stage.**
Before exiting any PDLF stage, the agent (or human) must be able to answer: *what were the big bones? which muscles drove the decision? which nerve network did I use? what fat did I cut? how did I present (skin)? is it healthy?* If any of these is blank, the stage isn't done. This closes the "unexamined micro-decisions" failure mode.

**Rule 2 — The ISA is the living ideal-state artifact, kept in GBrain.**
PDLF stage 12 (Lockdown) freezes a *baseline*, but the ISA — a 12-section done-definition decomposed into ISCs (Ideal State Criteria) — lives in GBrain and evolves. When stage 17 learnings arrive, the ISA is updated, not just filed. At Junction 0 of the next initiative, the prior ISA is queried. This closes the "ideal state drifts" failure mode. The ISA is the single artifact that survives across all junctions.

**Rule 3 — Anvil is a bone-level concern from stage 7, not a skin concern at stage 14.**
Anvil Data Tables is the data model. Stage 10 (Data Design) must produce *actual Anvil table definitions*, not abstract ER diagrams that get translated later. Stage 8 (Architecture) must account for Anvil's server-side Python and client-server boundary. The `anvil.yaml` protection rule is preserved — the agent never writes it — but the agent *does* design against Anvil primitives from stage 8 onward. This kills the "re-made at stage 14" waste.

**Rule 4 — LEARN is a mandatory junction, not an optional retrospective.**
Stage 17b is non-skippable. `/retro` produces a report; `/learn` captures the learning entries; `/context-save` persists the working state; and a GBrain embed is run so the learnings are searchable. The next initiative's Junction 0 query is meaningless if this junction was skipped. This is the nerve that makes the memory compound in practice, not just in storage.

**Rule 5 — GStack pipelines run inside PDLF, not instead of it.**
`/autoplan` does not replace PDLF stages 6–12; it *executes* them. `/office-hours` is the tool for PDLF stage 1. `/plan-eng-review` is the tool for PDLF stage 8. `/plan-design-review` is the tool for PDLF stage 11 (design dimension). The mapping table above is normative — when a GStack skill is listed for a PDLF stage, that's the prescribed execution tool. PDLF is the sequence; GStack is the executor; Matt Pocock skills supply the discipline primitives (TDD, domain-modeling, grilling) where GStack doesn't have a native equivalent.

### The three artifacts that must always exist

1. **The ISA** — living in GBrain, 12 sections, ISCs as verification items. Updated at Lockdown (stage 12) and at LEARN (stage 17b). Never deleted; superseded when a new initiative replaces it.
2. **The ADR set** — in `adr/`, one decision per file, created at stage 8 and added to whenever a backward reopen (17→8) occurs. GBrain-indexed.
3. **The Learning Log** — entries captured at stage 17b via `/learn`, GBrain-indexed, queried at stage 0 of every subsequent initiative.

### Where this strategy is opinionated (and might be wrong)

- **PDLF is the master orchestrator over GStack pipelines.** You could argue GStack's `/autoplan` is more mature and should lead. Counter: PDLF is *construction-complete* (ideation through release) whereas GStack's planning pipeline covers planning only and its build pipeline is thinner than PDLF's stages 13–17. PDLF's stage-gating is also the better discipline for the anvil.yaml protection rule.

- **BFT is forced into every stage as a checkpoint.** This adds overhead. Counter: the synthesis showed that omitting BFT produces "right goals, right plan, wrong thinking at each junction" — the most common real failure mode. The overhead is justified because the cost of an unexamined decision at stage 8 is paid every day until stage 17.

- **GBrain's health score is treated as irrelevant.** The operating guide already says this, but made explicit: do not chase the score. Do not force ADRs into entity-directory patterns to satisfy `graph_coverage`. The score measures the wrong thing. The metrics that matter are embedding coverage (100%, green), search recall (test periodically), and freshness (sync after every stage 17b).

- **LifeOS/TELOS is not used directly.** PDLF stage 7 names "Daniel Miessler LifeOS principles" but LifeOS is personal AI infrastructure, not a team software-build tool. The *principles* to borrow are: ideal-state-driven (ISA), memory-compounding (GBrain already does this), self-improvement loop (Junction 0+17b), and bitter-pilled engineering (continuous fat-trimming). Don't install LifeOS; steal its concepts.

### The daily and per-initiative cadence

**Per initiative (one full PDLF cycle):**
- Junction 0: query GBrain for prior context (5 min)
- Stages 1–5: BFT bones + exploring nerves; `/office-hours`, `/domain-modeling`, `/grill-with-docs`
- Stages 6–12: BFT muscle + achieving nerves; `/autoplan`, `/plan-eng-review`, Anvil schema draft at 8 and 10, ISA published at 12
- Stages 13–14: BFT skin; `/design-consultation`, `/design-html`, Anvil Designer assembly
- Stages 15–16: BFT nerves (organizing); `/tdd`, `/review`, `/qa`
- Stage 17: BFT health; `/ship`, `/land-and-deploy`, `/canary`
- Junction 17b: `/retro`, `/learn`, `/context-save`, GBrain embed

**Daily (inside active stages):**
- `/context-restore` at start
- Work the current PDLF stage with BFT checkpoints
- `/context-save` at end
- WSL maintenance sequence only when content changed: `git add -A && git commit && git push && gbrain sync && gbrain embed --stale`

### What to build first to make this real

Three concrete gaps need closing before the strategy is fully operational:

1. **A "Junction 0" prompt/skill** — a small skill or prompt template that runs the GBrain prior-context query and produces a brief. Today this is manual ("Instruction: search GBrain for X, Y, Z"). It should be a one-liner: `/prior-context <domain>`.

2. **An ISA template** in `docs/` — the 12-section done-definition, stored as a markdown template, indexed by GBrain, updated at Lockdown and LEARN. This doesn't exist yet in this workspace.

3. **A BFT checkpoint cheat-sheet** — a one-page reference (bones/muscle/nerves/fat/skin/health questions) that the agent can be prompted to apply at each PDLF stage exit. Not a skill; a reference doc in `docs/`.

These three are small. The strategy itself is mostly *alignment* — PDLF, GStack, Matt Pocock skills, GBrain, and Anvil are all already installed and working. The strategy's job is to prescribe *which tool runs at which stage, with which thinking discipline, feeding which memory artifact*. That's what the table above does.

---

## Appendix — Source materials consulted

- de Bono, *Masterthinker's Handbook* (BODY Frame Thinking) — full text
- Daniel Miessler LifeOS thesis (docs.ourlifeos.ai) + LifeOS v5.0.0 README (github.com/danielmiessler/LifeOS) — Algorithm v6.3.0, ISA, Memory v7.6, Telos, Pulse
- PDLF `initial.md` — 17 stages, 5 phases
- `gstack-skills-reference.md` — 59 skills catalog
- `gstack-reference.md` — GStack system, brain sync, artifact locations
- `gbrain-operating-guide.md` — GBrain PGlite, health score, sync
- `gbrain-reference.md` — GBrain commands, sources, troubleshooting
- `matt-skills-reference.md` — 18 Matt Pocock skills, governance overrides
- Comparative synthesis: `opencode-outputs/body-lifeos-comparative-synthesis.md`
