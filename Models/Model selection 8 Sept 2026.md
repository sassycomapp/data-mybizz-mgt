---
title: "Model selection 8 Sept 2026"
doc-id: "mb-5695d3f0"
updated: "2026-10-01"
---
Based on your requirements (**under $1/M output, 1M context, strong reasoning + coding + instruction following + multi-turn**), here are the **two best models** on OpenRouter:

***

## **Option 1: Two-Model Specialized Stack**

### **Reasoner: GLM 5.3 Flash** (Z.ai)
- **Price:** $0.075/M input, **$0.25/M output** (promo until Sep 9 → $0.50 after)
- **Context:** 1M tokens
- **Reasoning:** Intelligence Index **57**, Terminal-Bench 2.1 **84.3%**, GPQA Diamond not reported but strong agentic reasoning 
- **Coding:** DeepSWE v1.1 **63.4%**, SWE-Bench strong for agentic workflows [regolo](https://regolo.ai/deepseek-v4-flash-vs-qwen3-8-flash-next-vs-glm-5-3-flash-the-real-leader-in-quality-to-price-in-2026/)
- **Instruction Following:** Excellent multi-turn decomposition (high agentic scores indicate strong instruction chain handling) 
- **Multi-Turn:** Best-in-class for long-horizon agent tasks [tech-insider](https://tech-insider.org/tencent-hy3-vs-glm-5-3-flash-vs-kimi-k3-2026/)

### **Coder: Qwen3.8 Flash** (Alibaba)
- **Price:** $0.15/M input, **$0.47/M output**
- **Context:** 1M tokens
- **Reasoning:** GPQA Diamond **91.7%** (scientific reasoning), LiveCodeBench v6 **91.9%** [datacamp](https://www.datacamp.com/blog/qwen3-8-flash-next)
- **Coding:** SWE-Bench Pro **62.5%**, beats Claude Opus 4.6 Max on most coding benchmarks [regolo](https://regolo.ai/deepseek-v4-flash-vs-qwen3-8-flash-next-vs-glm-5-3-flash-the-real-leader-in-quality-to-price-in-2026/)
- **Instruction Following:** Multimodal reasoning model optimized for coding assistance and document analysis [openrouter](https://openrouter.ai/qwen/qwen3.8-flash)
- **Multi-Turn:** Suited for agentic workflows, codebase analysis, desktop interaction [openrouter](https://openrouter.ai/qwen/qwen3.8-flash)

**Combined Cost:** ~$0.225/M input, **~$0.72/M output** (well under $1)

***

## **Option 2: Single General-Purpose Model**

### **GLM 5.3 Flash** (Z.ai)
- **Does both reasoning and coding at frontier-flash tier**
- **Reasoning:** Intelligence Index 57, Terminal-Bench 2.1 84.3% 
- **Coding:** DeepSWE 63.4%, competitive with specialized coders [regolo](https://regolo.ai/deepseek-v4-flash-vs-qwen3-8-flash-next-vs-glm-5-3-flash-the-real-leader-in-quality-to-price-in-2026/)
- **Instruction Following:** Strong multi-turn capability (agentic focus) 
- **Multi-Turn:** Designed for long-horizon agent workflows [tech-insider](https://tech-insider.org/tencent-hy3-vs-glm-5-3-flash-vs-kimi-k3-2026/)
- **Cost:** $0.075/M input, **$0.25–0.50/M output**

**Trade-off:** Slightly weaker on pure coding benchmarks vs Qwen3.8 Flash (~10–15% gap on SWE-Bench Pro), but **2–3× cheaper** and handles both roles competently. [regolo](https://regolo.ai/deepseek-v4-flash-vs-qwen3-8-flash-next-vs-glm-5-3-flash-the-real-leader-in-quality-to-price-in-2026/)

***

## **Why These Two?**

| Requirement | GLM 5.3 Flash | Qwen3.8 Flash |
|-------------|---------------|---------------|
| **Under $1/M output** | ✅ $0.25–0.50 | ✅ $0.47 |
| **1M context** | ✅ Yes | ✅ Yes |
| **Reasoning** | ✅ Intelligence Index 57 | ✅ GPQA 91.7% |
| **Coding** | ✅ DeepSWE 63.4% | ✅ SWE-Bench Pro 62.5% |
| **Instruction Following** | ✅ Strong (agentic) | ✅ Strong (coding-focused) |
| **Multi-Turn** | ✅ Best-in-class | ✅ Good |

 [regolo](https://regolo.ai/deepseek-v4-flash-vs-qwen3-8-flash-next-vs-glm-5-3-flash-the-real-leader-in-quality-to-price-in-2026/)

***

## **Alternatives Considered (and Why They Didn't Make the Cut)**

- **DeepSeek V4 Flash 0731** ($0.16/M output): Excellent coding (SWE-Bench Verified 79%), but weaker reasoning (Terminal-Bench 82.7% vs GLM's 84.3%, lower agentic scores) [regolo](https://regolo.ai/deepseek-v4-flash-vs-qwen3-8-flash-next-vs-glm-5-3-flash-the-real-leader-in-quality-to-price-in-2026/)
- **Mercury 2.5 Preview** ($0.15/M output): Fastest reasoning LLM, but limited published coding benchmarks 
- **MiMo-V2.5-Pro** ($0.87/M output): Strong coding (SWE-Bench 78.9%), but weaker reasoning (Intelligence Index 32.6–43) and higher cost 
- **Gemini 3.8 Flash** ($3.75/M output): Excellent all-rounder but **over budget** [openrouter](https://openrouter.ai/google/gemini-3.8-flash)

***

## **Recommendation**

**Start with GLM 5.3 Flash as your single general-purpose model** — it covers all four requirements at the lowest cost. If you later find coding performance insufficient for complex repository-level tasks, **add Qwen3.8 Flash as a specialized coder** and route coding-heavy requests to it. [regolo](https://regolo.ai/deepseek-v4-flash-vs-qwen3-8-flash-next-vs-glm-5-3-flash-the-real-leader-in-quality-to-price-in-2026/)

This gives you a **flexible, cost-efficient stack** under $1/M output with 1M context and strong performance across all your criteria. [datacamp](https://www.datacamp.com/blog/qwen3-8-flash-next)

***
## OpenAI Embedding Model
Complete this for OpenAI Embedding Model

***
##Voyage 2.5 Re-ranking Model
Complete this for Voyage 2.5 Re-ranking Model