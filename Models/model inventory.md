---
title: "model inventory"
doc-id: "mb-9377bd73"
updated: "2026-10-23"
date-created: 2026-09-29T103600+0200
---
# Model Inventory

Models in active use on this machine and their purposes, determined by direct
inspection of configuration files, authentication stores, environment variables,
and gbrain audit logs on 2026-09-29.

---

## Inventory

| Model | Purpose | Status |
|---|---|---|
| `openrouter/~z-ai/glm-flash-latest` | OpenCode interactive agent — chat, planning, execution | Active |
| `openai:text-embedding-3-large` (1536 dims) | GBrain embedding — converts pages/chunks into vectors for semantic search | Active; ADR-bound |
| `openai:gpt-5.2` | GBrain query expansion (`gbrain query` multi-query expansion) and GBrain chat/synthesis paths | Active |
| `anthropic:claude-sonnet-4-6` | GBrain Dream Cycle `propose_takes` phase — generating durable "takes" claims; likely also gbrain's other LLM paths (think/synthesize, subagent jobs) — inferred | Active |
| ZeroEntropy (`ZEROENTROPY_API_KEY`) | Re-ranking | **Not in use.** GBrain 0.46.1.0 does not support re-ranking. GBrain has deprecated ZeroEntropy — it does not exist in the pipeline, even though the key may still be registered |

---

## Evidence

- **OpenCode / GLM Flash Latest** — `~/.local/share/opencode/auth.json` contains
  only `openrouter` as an authenticated provider; no `model` override in
  `opencode.jsonc` (global or project level).
- **Embedding** — `~/.gbrain/config.json`: `embedding_model: openai:text-embedding-3-large`,
  `embedding_dimensions: 1536`. Confirmed by `gbrain config show` and
  `gbrain-explainer.md`. Binding constraint per
  `C:\mybizz\mybizz-os-docs\os-decisions\adr-openai-embedding-provider.md`:
  OpenAI must remain the embedding provider (Anthropic cannot perform embeddings
  at all; a provider switch requires re-embedding the entire corpus).
- **Query expansion / chat** — `~/.gbrain/config.json`:
  `expansion_model: openai:gpt-5.2`, `chat_model: openai:gpt-5.2`.
- **Claude Sonnet 4.6** — audit logs `~/.gbrain/audit/dream-budget-2026-W40.jsonl`
  (2026-09-28) and `dream-budget-2026-W28.jsonl` (2026-07-07): every Dream Cycle
  `propose_takes` call billed to `anthropic:claude-sonnet-4-6` (USD 0.012 per call,
  USD 5 budget). `ANTHROPIC_API_KEY` is a configured gbrain key (`gbrain config show`).
  No `models` override exists in config.json, and no `GBRAIN_MODEL` env var is set.
- **ZeroEntropy** — `ZEROENTROPY_API_KEY` present in the environment and injected
  into the gbrain MCP entry in `opencode.jsonc`, and accepted by gbrain
  (`gbrain config show` lists it) — but registration is vestigial. Nothing consumes it.

---

## Correction record — re-ranking

Supersedes the initial assessment made earlier on 2026-09-29, which had inferred
ZeroEntropy as the active re-ranker from the presence of `ZEROENTROPY_API_KEY`.

Per developer instruction, 2026-09-29:

- GBrain at the current version (0.46.1.0) **does not support re-ranking**.
- GBrain has **deprecated ZeroEntropy**. ZeroEntropy does not exist as a working
  component — the key may still be registered, but registration is not evidence
  of use.

---

## Not in use

- **Claude Code CLI** — not installed or configured: no `claude` binary on PATH,
  no `~/.claude.json`, no `~/.claude/settings.json` (`~/.claude` holds only
  gstack skills). Claude Sonnet 4.6 is consumed exclusively through gbrain's
  Anthropic key, not through a Claude agent harness.
- **Codex CLI / Gemini CLI** — no configuration directories present.
- **ZeroEntropy** — deprecated by gbrain (see correction record above).

---

## Certainty levels

| Entry | Certainty |
|---|---|
| Embedding | Clearly defined — config, docs, and ADR agree |
| Query expansion / chat | Clearly defined — config.json |
| Sonnet 4.6 in Dream Cycle | Clearly defined — audit logs |
| Sonnet 4.6 for other gbrain LLM paths | Inferred only — not separately proven by a log |
| Re-ranking | Developer-stated (2026-09-29): not supported in 0.46.1.0; supersedes inference |

---

## Pending note

GBrain upgrade is available: 0.46.1.0 → 0.59.3.0. Re-ranking support and the
ZeroEntropy status should be re-verified after any upgrade.
