# Budget Data (v2)

Working data file. Policy and structure: see `budget-strategy-v2.md`.
Per-skill-set risk-and-cost workbook: see `risk-analysis-v2.xlsx`.
Model shortlist and pricing: see `../Models/Model selection 8 Sept 2026 v2.md`.

---

## Table of metrics constants & conversions

The objective of this section is to reduce all the various inputs to simple
constants which can be used in the document: `risk-analysis-v2.xlsx`.

### Constants (rates per model)

| Constant | Value | Unit | Source | Verified |
|---|---|---|---|---|
| GLM 5.3 Flash — input | $0.075 | per M tokens | Model selection v2 (promo until Sep 9 → $0.50 after) | 2026-09-08 |
| GLM 5.3 Flash — output | $0.25–0.50 | per M tokens | Model selection v2 | 2026-09-08 |
| Qwen3.8 Flash — input | $0.15 | per M tokens | Model selection v2 | 2026-09-08 |
| Qwen3.8 Flash — output | $0.47 | per M tokens | Model selection v2 | 2026-09-08 |
| Voyage rerank-2.5 | $0.05 | per M tokens | gbrain recipe (price_last_verified 2026-08-15) | 2026-08-15 |
| Voyage rerank-2.5-lite | $0.02 | per M tokens | gbrain recipe (verified 2026-08-15) | 2026-08-15 |
| OpenAI text-embedding-3-large | $0.13 | per M input tokens | OpenAI published rate (verify on dashboard) | 2026-09-08 |
| Voyage token density | ~1 token per character | ratio (dense text) | gbrain source comment | 2026-08-15 |
| Voyage free grant | 200M tokens (one-time, cumulative; all reranker models share the pool) | tokens | Developer-reported from Voyage dashboard — **verify balance on dashboard** | 2026-09-08 |
| Dream-cycle budget cap | $0.30 | per cycle (observed actual: $0.02–0.14) | gbrain budget ledger (verified) | 2026-09-06 |
| Eval probe (suspected-contradictions, per query) | ≈$0.0035–0.004 | per query | gbrain budget ledger (verified) | 2026-09-06 |

### Conversions

| From | To | Factor / formula | Scope | Notes |
|---|---|---|---|---|
| Tokens (any model) | Dollars | tokens ÷ 1,000,000 × rate (per model, from constants above) | per model | The bridge between planned consumption (tokens) and captured actuals (dollars) |
| Interactive search | Tokens | ≈12.5K–37.5K per search | GBrain core | Pool ≈ 25 chunks × 0.5–1.5K tokens (balanced mode, searchLimit 25); verified band |
| Dream cycle (full, 23 phases) | Dollars | ≈$0.02–0.14 per cycle (capped at $0.30) | GBrain dream-cycle | Measured 2026-08-16 + 2026-09-06 acceptance run |
| Eval probe | Dollars | ≈$0.0035–0.004 per query | GBrain core | Haiku judge, per query |
| Characters (dense text) | Tokens (Voyage) | ≈1 token per character | Voyage rerank | Per gbrain source |
| Sync/embed day | Dollars | ≈$0.14 per ordinary day | GBrain core | Measured 2026-08-26 |

---

## Typical usage cases

A list of usage cases which are typical for our usage (catalogue — quantities in
the sections below / the xlsx):

- GBrain: search/query, sync, recall/think
- GBrain: interactive search/query (dominant daily consumer — feeds Rerank + Embed)
- GBrain: Embedding
- GBrain: Reranking (200M one-time grant pool — shared across all reranker models)
- GBrain: eval probes (suspected-contradictions and other `gbrain eval` runs)
- GBrain: dream-cycle (the 23-phase cycle)
- GStack skills: Developing makePDLF steps
- Matt Pocock skills: Developing makePDLF steps
- Magdoub-wireframe skills: Developing makePDLF steps
- Anvil-agent-references: Developing makePDLF steps
- Archify: Developing makePDLF steps & Describing MybizzOS
- Graphify: Codebase memory management
- memory-governor: Memory governance
- mb-submit-memory: Memory management
- mb-sentinel-review: Developing makePDLF steps
- mb-align-docs: Documentation management
- mb-docs-manager: Documentation management
- mb-wikilinks: Documentation management
- mb-sysdoc-creator: Documentation management
- mb-compile-rules: Cupcake management
- Opencode agent sessions: Plan Agent (Reasoner), Build Agent (Reasoner), Build Agent (Coder)

---

## Typical estimated consumptions based on anticipated workloads

Anticipated workloads going forward in terms of usage quantities, separating
routine and once-off work. Per-row estimates, review periods, and actuals:
see `risk-analysis-v2.xlsx` (columns A–F = Foundation Data; review columns fill
during the review period; the Premises/Notes column carries per-row assumptions).

---

## Models best suited for the work

In terms of the quality of work and the anticipated costs. Full pricing and
selection rationale: `../Models/Model selection 8 Sept 2026 v2.md`.

| Model | Role | Notes |
|---|---|---|
| GLM 5.3 Flash (OpenRouter) | Reasoner / general-purpose / default | $0.075 in / $0.25–0.50 out per M; 1M context; promo until Sep 9 |
| Qwen3.8 Flash (OpenRouter) | Coder / specialized | $0.15 in / $0.47 out per M; 1M context; route coding-heavy tasks here |
| OpenAI text-embedding-3-large | Embeddings | $0.13/M input; 1536 dims; matches gbrain config (verified) |
| Voyage rerank-2.5 | Reranking | $0.05/M tokens; 200M one-time grant pool (shared across all Voyage reranker models); gbrain ≥0.46.3 required |

---

## Observability and metrics

The observability, metrics, and data sources used for budgetary purposes:

| Source | Captures | Format | Cadence |
|---|---|---|---|
| GBrain budget audit ledgers (`~/.gbrain/audit/budget-*.jsonl`) | Per-call reservations and actuals: model, tokens, actual cost; caller labels distinguish interactive / cycle / eval | JSONL (append-only, per-week files) | Weekly harvest + after once-off tasks |
| Voyage dashboard | Grant-pool balance (200M), per-request token usage | Dashboard / export | Weekly |
| Anthropic console | extract_atoms usage (dream cycle) | Dashboard | After dream runs |
| OpenAI usage dashboard | Embedding + chat usage | Dashboard | Weekly |
| OpenRouter dashboard | GLM / Qwen usage (reasoner + coder) | Dashboard | Weekly |
| `gbrain doctor` | Health and freshness signals that gate consumption quality | CLI output | On demand |

**Capture procedure:** harvest the GBrain ledgers programmatically (system of
record for GBrain-side actuals — never re-typed); save provider dashboard exports
alongside as original-format files; refresh the Excel workbook from the originals.
Originals are never hand-edited. All files live in `C:\_data-mybizz-mgt\Mgt\Budget\`.
