---
title: "Model selection 15 Sept"
doc-id: "mb-07b6be19"
updated: "2026-10-01"
---
If we treat the current frontier (top-tier reasoning models like o3-pro / o4-high / Gemini 2.5 Pro) as 100% efficient at reasoning, then a reasonable ballpark is:

GLM 5.3 Flash ≈ 85–90% of frontier reasoning efficiency

DeepSeek V4 Flash 0731 ≈ 75–80% of frontier reasoning efficiency

Thumb-suck single numbers:

GLM 5.3 Flash: ~87% [In / Out Price 
$0.075 / $0.25per 1M; Context 1.3M]

DeepSeek V4 Flash 0731: ~78% [In / Out Price $0.04 / $0.10per 1M Context 1.3M]

Rationale in one line: GLM 5.3 Flash trades speed for noticeably stronger agentic/long-horizon reasoning, while DeepSeek V4 Flash 0731 is faster and very capable but sits a step below on complex, multi-step reasoning tasks.

----------------------------

Using the same “frontier = 100%” scale, but now for coding ability (understanding, generating, debugging, and refactoring code in realistic tasks):

GLM 5.3 Flash: ~88–92% → call it ~90%

DeepSeek V4 Flash 0731: ~85–90% → call it ~88%

Thumb-suck single numbers:

GLM 5.3 Flash: ~90% of frontier coding ability

DeepSeek V4 Flash 0731: ~88% of frontier coding ability

Why they’re so close here:

On straight coding tasks (generate functions, fix bugs, small refactors), DeepSeek V4 Flash 0731 is extremely strong and often feels on par with GLM 5.3 Flash.

GLM 5.3 Flash pulls ahead mainly on larger, multi-file, agentic coding (DeepSWE-style tasks, repo-level changes, maintaining state across many steps).Using the same “frontier = 100%” scale, but now for coding ability (understanding, generating, debugging, and refactoring code in realistic tasks):

GLM 5.3 Flash: ~88–92% → call it ~90%

DeepSeek V4 Flash 0731: ~85–90% → call it ~88%

Thumb-suck single numbers:

GLM 5.3 Flash: ~90% of frontier coding ability

DeepSeek V4 Flash 0731: ~88% of frontier coding ability

Why they’re so close here:

On straight coding tasks (generate functions, fix bugs, small refactors), DeepSeek V4 Flash 0731 is extremely strong and often feels on par with GLM 5.3 Flash.

GLM 5.3 Flash pulls ahead mainly on larger, multi-file, agentic coding (DeepSWE-style tasks, repo-level changes, maintaining state across many steps).