# Budget Strategy (v2)

**Document class:** Policy. Defines how AI-consumption budgeting is strategized,
captured, and reviewed. Not a working file — no quantities, prices, or actuals here.

**Companion working files:**

| File | Role |
|---|---|
| `budget-data-v2.md` | Constants, conversions, use-case catalogue, consumption estimates, model assignments, observability |
| `risk-analysis-v2.xlsx` | Per-skill-set and per-step risk-and-cost workbook (Foundation Data + stepwise pipeline) |
| `Model selection 8 Sept 2026 v2.md` | Model shortlist with pricing and selection rationale |

All files live in `C:\_data-mybizz-mgt\Mgt\Budget\` (model selection in `Mgt\Models\`).

---

## Principles

1. **Consumption is the planning primitive.** Budgeting happens in usage quantities
   (tokens, calls, runs, cycles). Dollars are derived outputs (via the conversions
   table in budget-data-v2.md), never the planning unit. Prices move per provider;
   usage patterns are what this environment controls.
2. **Every premise is explicit.** No estimate exists without its assumptions written
   beside it. Measured values outrank assumed ones; assumptions are retired when
   measurements arrive — never blended.
3. **Apples-to-apples via the conversions table.** No comparison across units without
   the conversion factors. ("A search" is not a unit — it spans retrieval, expansion,
   rerank, and synthesis legs with different token masses per provider.)
4. **A one-time grant is a countdown, not an allowance.** Free token pools are
   consumed by measured burn rates; their remaining lifetime is computed from actual
   usage, never from optimistic assumptions.
5. **A provider sunset is a check failure.** It triggers model-strategy review rather
   than silent degradation.
6. **Catch-all rule.** Consumption that doesn't map to a declared use case is recorded
   under "unplanned/exploratory" until classified — never silently dropped.

---

## Working-file roles

### budget-data-v2.md
Holds the constants and conversions tables (rates per model, token densities, pool
sizes, per-use-case token masses), the use-case catalogue (interactive searches,
dream-cycle phases, sync/embed, eval probes, doc-suite runs, governed submissions,
model-strategy evaluations, unplanned/exploratory), estimated consumptions per use
case with premises, model assignments per skill set, and the observability sources.

### risk-analysis-v2.xlsx
The per-row workbook. Two layouts:

- **Foundation rows** (pipeline groupings: Docs management, Memory management,
  Once-off, plus GBrain interactive search, Rerank, Embed): columns A–F = item,
  model, rate, estimated tokens per run, estimated cost per run, from date.
  Review columns (estimated runs, estimated cost, actual runs, assessed cost per
  actual runs) fill during the review period.
- **Stepwise rows** (PDLF steps 11, 12, 14, 15, 16): columns A–F = step, process,
  skill set, skill used, model, rate. Steps 13 (does not exist) and 17–46 (scoped,
  not developed) are out of scope until developed.

Premises/notes column carries the assumptions behind each row's numbers (e.g. the
dream-cycle per-phase model mix — extract_atoms = Anthropic, remainder = GLM; the
rerank grant's 200M-token pool).

### Model selection v2
The model shortlist: GLM 5.3 Flash (reasoner/general), Qwen3.8 Flash (coder),
OpenAI text-embedding-3-large (embeddings), Voyage rerank-2.5 (reranking, 200M
one-time token grant) — with pricing, benchmarks, and the rejected alternatives.

---

## Observability loop

1. **Capture** (weekly + after once-off tasks): harvest GBrain budget ledgers
   (`~/.gbrain/audit/budget-*.jsonl` — per-call model/tokens/cost, caller labels
   distinguish interactive/cycle/eval), save provider dashboard exports alongside.
2. **Refresh:** update the Excel workbook from the captured originals (originals
   are never hand-edited; Excel is a view, not the store).
3. **Compare:** actual vs estimated per skill-set row; variances beyond threshold
   trigger estimate revision (premises re-agreed, not silently adjusted).
4. **Review cadence:** the loop runs at every cycle even when unchanged — "no
   change" is recorded as a decision, not silence.

---

## Model-suitability framework (applied when volumes justify review)

Axes: quality tier (receipt-backed results preferred) · cost tier (derived at real
volumes) · availability/continuity (sunset exposure, fail-open behavior) · budget
posture (grant pools, caps). Decision: volumes → shortlist → trial verification
where receipts don't exist → decision recorded with premises. Provider sunsets and
grant-pool cliffs trigger this review automatically.

---

## Governance

- This document changes by explicit decision; quantities and actuals change only in
  the working files. A revision that moves data into this document is rejected.
- Reviewed at every observability cycle; "no change" is recorded, not silence.
- Version history: v1 (2026-09-07, full policy structure — superseded by this
  reduction), v2 (2026-09-08, reduced to pair with the working files).
