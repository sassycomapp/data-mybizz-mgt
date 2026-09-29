---
title: "Model Selection 24 Sept"
doc-id: "mb-9390b739"
---
| Perplexity<br/>Model   | Comparative reasoning strength | OpenRouter output cost / 1M | Comment  |
| ---------------------- | ------------------------------ | --------------------------- | -------- |
| MiMo-V2.6 Pro          | 5                              | $0.87                       |          |
| MiMo-V2.5 Pro          | 5                              | $0.609                      | ?        |
| GPT-6 Luna             | 4                              | $0.50                       | Too busy |
| MiniMax M3             | 3                              | $0.96                       |          |
| Qwen3.8 Omni Flash     | 3                              | $0.47                       |          |
| DeepSeek Flash Latest  | 3                              | $0.60                       |          |
| Trinity Large Thinking | 3                              | $0.80                       |          |
| MiMo-V2.6 Flash        | 2                              | $0.28                       |          |
| GLM Flash Latest       | 2                              | $0.25                       | ok       |

| Claude<br/>Model           | Efficiency (1–5) |
| -------------------------- | ---------------- |
| MiMo-V2.6 Pro              | 5                |
| MiMo-V2.5 Pro              | 4                |
| Trinity Large Thinking     | 4                |
| GPT-6 Luna (≈GPT-5.6 Luna) | 3                |
| MiniMax M3                 | 3                |
| DeepSeek Flash Latest      | 3                |
| MiMo-V2.6 Flash            | 2                |
| Qwen3.8 Omni Flash         | 2                |
| GLM Flash Latest           | 1                |

| OpenAI<br/>Model           | Reasoning           |
| -------------------------- | ------------------- |
| **GPT-6 Luna**             | **5 — Very High**   |
| **MiMo-V2.6 Pro**          | **5 — Very High**   |
| **Qwen3.8 Omni Flash**     | **4 — High**        |
| **MiMo-V2.5 Pro**          | **4 — High**        |
| **MiniMax M3**             | **4 — High**        |
| **Trinity Large Thinking** | **3 — Medium High** |
| **DeepSeek Flash Latest**  | **3 — Medium High** |
| **MiMo-V2.6 Flash**        | **3 — Medium High** |
| **GLM Flash Latest**       | **3 — Medium High** |

| **Gemini<br/>Model**       | **Efficiency (1–5)** |
| -------------------------- | -------------------- |
| **MiMo-V2.6 Pro**          | **5**                |
| **MiMo-V2.5 Pro**          | **4**                |
| **Trinity Large Thinking** | **4**                |
| **GPT-6 Luna**             | **3**                |
| **MiniMax M3**             | **3**                |
| **DeepSeek Flash Latest**  | **3**                |
| **MiMo-V2.6 Flash**        | **2**                |
| **Qwen3.8 Omni Flash**     | **2**                |
| **GLM Flash Latest**       | **1**                |

<style>
</style>

|                        |            |        |        |        |       |     |       |         |
| ---------------------- | ---------- | ------ | ------ | ------ | ----- | --- | ----- | ------- |
|                        | Perplexity | Claude | OpenAI | Gemini | Total | Ave | Price | Comment |
| MiMo-V2.6 Pro          | 5          | 5      | 5      | 5      | 20    | 5.0 | 0.87  |         |
| MiMo-V2.5 Pro          | 5          | 4      | 4      | 4      | 17    | 4.3 | 0.61  | Meh     |
| GPT-6 Luna             | 4          | 3      | 5      | 3      | 15    | 3.8 | 0.5   |         |
| Trinity Large Thinking | 3          | 4      | 3      | 4      | 14    | 3.5 | 0.8   |         |
| MiniMax M3             | 3          | 3      | 4      | 3      | 13    | 3.3 | 0.96  |         |
| DeepSeek Flash Latest  | 3          | 3      | 3      | 3      | 12    | 3.0 | 0.6   |         |
| Qwen3.8 Omni Flash     | 3          | 2      | 4      | 2      | 11    | 2.8 | 0.47  |         |
| MiMo-V2.6 Flash        | 2          | 2      | 3      | 2      | 9     | 2.3 | 0.28  |         |
| GLM Flash Latest       | 2          | 1      | 3      | 1      | 7     | 1.8 | 0.25  |         |
