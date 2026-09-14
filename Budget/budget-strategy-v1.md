# Budget Strategy — Metered AI Consumption

**Document class:** Policy. 
This document defines *how* AI-consumption budgeting is
strategized, planned, captured, and reviewed across the environment. It is not a
working file: it holds facilities, structures, rules, and premises — never quantities,
prices, or actuals. Working files (an Excel workbook for human consumption plus
original-format data files for agent consumption) are designed by this document and
built separately, per §12.

**Location:** all budget-related files live in `C:\_data-mybizz-mgt\Mgt\Budget\`.

**Nature:** iterative by design. This system improves over several revisions by
explicit decision — estimates sharpen against captured actuals, premises are revisited,
and structures extend as new consumers appear. It is expected to be wrong in places
and to say so openly (§11).

---

## §0 — Policy preamble

1. **Consumption is the planning primitive.** All budgeting, comparison, and
   strategizing happens in usage quantities (tokens, calls, cycles, runs). Monetary
   values are derived outputs (via §4 conversions), never the planning unit — prices
   change and vary by provider; usage patterns are what this environment controls.
   This rule exists because it was learned directly: a fixed token grant is consumed
   by usage patterns, not by price tags.
2. **Separation of concerns.** This document = policy and structure. Working files =
   data (constants values, per-use-case quantities, workload instances, captured
   actuals). A fact belongs in this document only if it is a rule, a definition, a
   category, or a premise — never if it is a count, a price, or a date-stamped value.
3. **Apples-to-apples discipline.** No comparison is made across units without the
   conversions defined in §4. The recurring failure mode this prevents is real and
   was demonstrated: "a search" is not a unit — it spans retrieval, optional
   expansion, rerank, and synthesis legs with different token masses per provider.
4. **Credential discipline carries over.** Budget artifacts (this document, the
   working files, captured exports) never contain credential values or key
   material — provider dashboards expose usage and cost, not secrets.
5. **Every premise is explicit.** No estimate exists without its premises written
   beside it (§6). Unlabeled numbers are treated as errors, not estimates.

---

## §1 — Scope: consumers and consumption

**In scope:** metered AI-provider consumption (embeddings, chat, rerank, extraction,
evaluation) attributable to a named consumer in this environment.

**Consumer classes** (the declared taxonomy — each consumption record names one):

| Component | Surface classes | Example operations |
|---|---|---|
| GBrain (core: search/query, sync, embed, recall/think) | interactive agent, scheduled, manual one-off | hybrid searches, embed passes, eval probes |
| GBrain dream-cycle (the 23-phase cycle) | manual one-off (invoked on demand by design) | extract_atoms, synthesize_concepts, propose_takes, embed, purge |
| gstack (skills and orchestration touching providers) | interactive agent | sync-gbrain stages, evals |
| memory-governor (and its mb-submit-memory front door) | manual one-off, PDLF step (when live) | candidate evaluation, GBrain writes |
| PostgreSQL (shared infrastructure) | always-on | storage/storage-adjacent metering if ever metered |
| Direct provider usage outside GBrain (agent sessions calling providers directly) | interactive agent | model calls not routed through GBrain |

**Out of scope (declared exclusions):** subscription costs (OpenCode, Claude Code,
hosting), infrastructure without metered AI usage. Exclusions may be added by
explicit revision of this document.

**Rule:** every consumption record — planned or actual — names a consumer class,
a surface class, and an operation from the usage-case catalogue (§5). Records that
cannot name all three are treated as unclassified and fixed before use.

---

## §2 — Consumption is measured, not priced

The budgeting pipeline runs in this order, and the order is policy:

1. **Plan and measure consumption** in usage quantities per §5–§7.
2. **Convert** to derived values via the §4 conversions only where comparison with
   provider-quoted figures is genuinely needed.
3. **Budget** derived costs per §9 — as outputs of quantities, never as inputs.

Rationale (standing): usage patterns are the controllable, comparable quantity;
prices move independently per provider and are the last thing applied, not the
first thing assumed. Model selection (§8) is the bridge between the two — it is
performed only once consumption profiles exist (§7), not before.

---

## §3 — Metrics constants table (structure)

A single table of fixed reference facts used by every conversion and estimate.

**Columns (working file):** Constant ID · Constant name · Value · Unit · Scope
(provider/component) · Source (measured / vendor-published / assumed) · Source
reference · Verification date · Verification method.

**Declared constant families (slots — values live in the working file):**

- Token-definition constants (e.g. provider tokenizer densities — the known case:
  Voyage counts roughly one token per character on dense text).
- Structural-size constants (chunk sizes in this brain, candidate-pool sizes per
  search mode, per-phase call counts of the dream cycle).
- Duration/rate constants where they affect consumption (worker deadlines that
  phases legitimately exceed, cache TTLs that suppress repeat consumption).
- Cost-rate constants per provider (the token↔dollar bridge inputs for §4).

**Policy:** constants carry a source class and a verification date without exception.
A constant that cannot name its source is demoted to "assumed" and treated as
provisional (§6 premises rules apply to it). The strategy document does not hold
constant values — the working file does; this section holds the constant families
and the rules above.

---

## §4 — Metrics conversions table (structure)

A single table of unit conversions enabling apples-to-apples comparison.

**Columns (working file):** Conversion ID · From unit · To unit · Factor · Formula
(where non-linear) · Provider/component scope · Source class · Verification date ·
Notes.

**Declared conversion families (slots — factors live in the working file):**

- Token→dollar per provider/model (the bridge required from day one: planned
  consumption is denominated in tokens, captured actuals arrive denominated in
  dollars — without this family the §11 comparison cannot join).
- Calls→tokens per usage case (e.g. one interactive search ≈ N tokens reranked,
  M tokens expanded, given the §3 pool-size constants — the number that made
  "a search" incomparable before this table existed).
- One dream cycle→its per-phase consumption mix (a profile reference, not a constant).
- Currency conversions between provider quote currencies, if ever needed.

**Policy:** conversions are defined here as families; factors live in the working
file with source class and verification date (same discipline as §3). A conversion
with an unverified factor may be used for planning but its outputs are labeled
provisional.

---

## §5 — Usage-case catalogue (list — unquantified by policy)

The declared catalogue of typical usage cases in this environment. Each entry names
a recurring consumption pattern, keyed to §1 consumer classes. This section is a
catalogue of names and definitions; quantities belong to §6/§7 and the working file.

| Use case | Definition | Consumer class | Surface |
|---|---|---|---|
| Interactive agent search | Hybrid retrieval (vector + keyword + optional expansion + rerank) issued by an agent during ordinary work | GBrain core | interactive agent |
| Bulk/scripted search | Same retrieval pattern under scripted or batch invocation | GBrain core | scheduled / manual one-off |
| Dream-cycle run | Full 23-phase cycle | GBrain dream-cycle | manual one-off |
| Dream-cycle single phase | A `--phase` targeted run | GBrain dream-cycle | manual one-off |
| Sync operation | Repo sync + embed refresh (standing script or per-source) | GBrain core | scheduled / manual one-off |
| Embedding batch | Embedding generation for new/changed content | GBrain core | follows sync/dream |
| Eval probe | Suspected-contradictions or other `gbrain eval` probes | GBrain core | manual one-off |
| Doc-suite construction | A full documentation suite run (research, drafting, verification, commits) | direct provider usage + GBrain queries | interactive agent |
| Governed memory submission | mb-submit-memory → governor → GBrain write | memory-governor | manual one-off (PDLF step when live) |
| Governor review resolution | Review-queue resolutions and their evaluation costs | memory-governor | manual one-off |
| Model-strategy evaluation | Benchmark/eval runs used to decide §8 model choices | direct provider usage | manual one-off |
| Unplanned/exploratory usage | Any consumption outside the above — captured as its own case rather than silently absorbed | any | any |

**Policy:** new usage cases enter the catalogue by explicit revision. Consumption
that does not map to a catalogue entry is recorded under the final row until
classified — never silently dropped.

---

## §6 — Estimated consumption per use case, with premises

For each §5 use case, the working file holds an estimate built exactly this way:

**Per-use-case estimate structure (working file):**

- Quantity range (low / expected / high) in usage units (§2).
- **Premises** — every assumption the range rests on, listed individually. Each
  premise is one of: measured (has a source record), vendor-published (sourced),
  or assumed (judgment, labeled).
- Provenance class of the estimate itself: measured / estimated / assumed.
- Review date.

**Rules:**

1. Estimates are discussed and agreed before acceptance — an estimate without
   agreed premises is not accepted into the working file.
2. Measured premises outrank assumed ones; when a measured value arrives, the
   assumption it replaces is retired, not blended.
3. Estimates are revised on §11 triggers, not on vibes.

---

## §7 — Anticipated workloads: routine and once-off task classes

Two declared task classes; every future anticipated task belongs to exactly one.

| Task class | Definition | Examples of the class (illustrative, not a volume statement) |
|---|---|---|
| **Routine** | Recurring work whose consumption profile repeats predictably | ordinary agent sessions; sync/embed operations; periodic dream cycles; scheduled doctor checks |
| **Once-off (episodic)** | Discrete bodies of work with a defined end, whose consumption is bounded by the work's scope | doc-suite constructions; memory-component suite runs; acceptance tests; upgrades and their verification passes; governed-submission campaigns |

**Estimation pattern:** each task class carries a per-execution consumption profile
composed from §5 use cases (quantified via §6). Anticipated project modules of work
are decomposed into task-class instances; instance counts are working-file data.

**Policy:** a task whose profile cannot be composed from the §5 catalogue forces a
catalogue revision first (§5's final row) — estimation never invents undeclared
consumption patterns.

---

## §8 — Model suitability strategy (framework — choices deferred)

Model and provider selection is performed only when §7 workload volumes exist to
decide against. This section defines the framework that will make that decision.

**Evaluation axes (declared):**

1. **Quality tier** — measured fitness for the operation (receipt-backed results
   where they exist; otherwise trial-verified).
2. **Cost tier** — derived cost per §3/§4 at the §7 volumes.
3. **Availability and continuity** — provider stability, sunset exposure,
   fail-open behavior of the consuming component when the provider fails.
4. **Budget posture** — fit against free allowances, grant pools, and caps
   (a one-time grant is a countdown, not an allowance — the duration math uses
   measured burn, never optimistic assumptions).

**Decision procedure (declared):** volumes from the working file → candidate
shortlist per axis → trial verification where receipts don't exist → decision
recorded with premises → revisited on §11 triggers.

**Standing principles (policy):**

- Free allowances are finite pools: their lifetime is computed from measured burn
  rates, and the exhaustion cliff carries a pre-decided fallback order (§11 may
  hold the current order; it is decided, not improvised).
- A provider sunset is a check failure — it triggers §8 review rather than silent
  degradation.
- Selection changes are recorded with the receipts that justified them.

---

## §9 — Cost budget structure (facility)

The budget table (working file) has this shape:

**Columns:** Period · Consumer class (§1) · Usage case (§5) · Task class (§7) ·
Planned quantity (usage units, §2) · Conversion (§4) · Derived budget value ·
Premises reference (§6) · Notes.

**Rules:**

1. Budget lines are composed from task-class instances (§7) and use-case profiles
   (§6) — a budget line that cannot trace its quantity to a §6 estimate with agreed
   premises is not accepted.
2. Derived values are recomputed when §4 factors are re-verified — quantities are
   the durable inputs; derived values move with the factors.
3. The budget states its period and its inclusive consumer scope (§1) on every line.

---

## §10 — Observability and metrics capture

**Capture sources (as they exist today — verified):**

| Source | Captures | Form |
|---|---|---|
| GBrain budget audit ledgers (`~/.gbrain/audit/budget-*.jsonl`) | per-call reservations and actuals: model, tokens, actual cost, caller label (labels distinguish cycle phases, evals, and interactive calls) | JSONL, append-only, per-week files |
| Provider dashboards (Voyage, Anthropic, OpenAI) | account-level usage and spend, grant-pool balances | dashboard / export |
| `gbrain doctor` | health and freshness signals that gate consumption quality | CLI output |
| Component-specific logs (sync logs, dream summaries) | operation-level context for the ledger rows | logs |

**Capture procedure (policy):**

1. **Cadence:** weekly capture (part of routine ops), plus after any once-off task
   class execution (§7) while its consumption is fresh.
2. **Method:** the GBrain ledgers are harvested programmatically (they are the
   system of record for GBrain-side actuals — never re-typed by hand); provider
   dashboard exports are saved alongside as original-format files.
3. **Destination:** originals land in the Budget folder as-is (agent consumption
   format); the Excel working file (§12) is refreshed from them — Excel is a view,
   never the store, and originals are never hand-edited.
4. **Attribution rule:** captured records must resolve to a §1 consumer class and a
   §5 use case; unresolved records are flagged in the working file's exceptions area
   until classified (§1's unclassified rule).

---

## §11 — Actuals-to-budget comparison (facility)

**Comparison structure (working file):** per period × consumer × usage case:
budgeted quantity (§9) · actual quantity (§10) · variance · variance ratio ·
explanation · action.

**Variance policy:**

| Condition | Trigger |
|---|---|
| Variance beyond the declared threshold (threshold value is a working-file premise) | Strategy revision: §6 premises for that use case are re-examined and re-agreed |
| A consumer class appears that isn't in §1 | §1 revision |
| A provider changes availability or pricing | §8 review |
| Free-allowance pool crosses its pre-decided cliff thresholds | §8 fallback order executes as already decided |

**The loop:** actuals → variance → premise revision → estimate revision → budget
revision. This loop is what makes the document iterative rather than design-once —
and the loop only works if the §6 premises were honest enough to be wrong in
public (§0.5).

---

## §12 — Working-files design (built after this document, per its definitions)

**File inventory (all in `C:\_data-mybizz-mgt\Mgt\Budget\`):**

| File | Format | Serves | Audiences |
|---|---|---|---|
| `budget-strategy.md` (this document) | Markdown | Policy and structure | developer + agents |
| Metrics constants + conversions + use-case estimates + budget + comparison tables | Excel workbook — one sheet per §3/§4/§6/§9/§11 table, from first build | Working data, human review, what-if analysis | developer (primary) |
| Captured originals (GBrain ledger harvests, provider dashboard exports) | JSONL / CSV as they arrive | System-of-record actuals for agent consumption | agents (primary) |

**Rules:**

1. The Excel workbook is a **view and working surface for humans** — it is refreshed
   from the original-format files; it is never treated as the store of record.
2. Original-format files are never hand-edited; corrections happen at the source
   (the ledger, the dashboard export) or as new records.
3. Every working-file table carries the columns declared in its governing section
   (§3–§11) — the working files implement this document's declared structures
   exactly, so agents can rely on the schema.
4. Working files are built once this document is approved — this document defines
   them; it does not contain them.

---

## §13 — Document governance

- **Versioning:** this document is versioned by revision date in the header area;
  each revision is an explicit developer decision recorded in the revision list below.
- **Revision triggers:** §11 variance triggers; new consumers/components (§1);
  provider changes (§8); structural lessons that change a definition (§3–§7).
- **Amendment rule:** definitions, categories, and rules change here; quantities,
  prices, and actuals change only in working files. A revision that moves data into
  this document is rejected on its face.
- **Review cadence:** reviewed at every §11 cycle, even when unchanged — "no change"
  is recorded as a decision, not silence.

---

## Revision list

| Version | Date | Decision summary |
|---|---|---|
| v0.1 | 2026-09-07 | Initial structure created: 14 sections, facility definitions only, per the developer's 10-step plan and the policy-not-data separation. First iteration of a planned multi-revision document. |
