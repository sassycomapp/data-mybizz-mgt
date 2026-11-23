---
title: "narration-voices"
---
# Task Spec Sheet — Mybizz Narration Voices

**Task:** C2 in `marketing-plan.xlsx`
**Owner:** David
**Depends on:** A3 (Mybizz Google account)
**Unblocks:** every narrated video in the marketing plan (explainer, help and teardown videos, and the narration in long-form videos)

---

## 1. Result

Mybizz narrates its videos with Google's Gemini voices, through a free Gemini API key from Google AI Studio. The key costs nothing and needs no card and no billing account.

| Item | Value |
|---|---|
| Google account | `mybizzlive@gmail.com` |
| Google Cloud project name | Mybizz |
| Project ID | `mybizz-515510` |
| Project number | 81918688433 |
| API key name | Gemini API Key |
| Where the key is kept | David's password manager only; never in a file or a repository |
| Billing account | None |
| Google payments profile | Individual, South Africa, legal name David Coleman, profile ID 5401-0178-4710; holds no card |

---

## 2. How It Works

- **The voices.** Each presenter, Sarah and Brian, has one ready-made Gemini voice on the model Gemini 3.8 Flash TTS, chosen by ear as the closest match to the presenter's Google Flow voice, and kept for the life of the presenter (section 5). Designed voices (Voice Design) are not used, because Voice Design runs only on the paid tier.
- **The accent.** Gemini voices take their accent and delivery from the Style instruction sent with the text; the voices themselves are listed under English (US). Every English narration request carries the presenter's Style instruction (section 5), which asks for UK English, so every video sounds the same. Without it, the voices speak with an American accent. French, German, Spanish and Italian narrations carry the same Style instruction without the accent words.
- **The free allowance.** The free tier allows a limited number of narration requests per day per project; AI Studio shows the current limits under **Rate limits**. One request narrates a whole script section, so a full narration takes a few requests. The daily count resets at midnight Pacific time, which is 10:00 in South Africa (09:00 while the United States is on summer time).
- **Why free first.** Mybizz has no income until it sells, and selling needs the videos. The free key breaks that loop: the videos are made now at no cost.

---

## 3. Set-Up

1. Open `https://console.cloud.google.com` as `mybizzlive@gmail.com` and create the project **Mybizz**.
2. Open `https://aistudio.google.com` as `mybizzlive@gmail.com` and accept the terms.
3. **Get API key → Create API key**, in the **Mybizz** project. Save the key in the password manager.

**Check:** AI Studio's API keys page lists **Gemini API Key** under the Mybizz project, on the free tier.

---

## 4. Moving to Paid Voices

When Mybizz-Live has income and needs more narration than the free allowance:

1. Create a Google Cloud billing account of type **Business**, in the name of Mybizz-Live Ltd once registered, with a card that has funds. Google places a temporary card check of about £40, released within a week.
2. Link the billing account to the Mybizz project.
3. Set a £1 budget alert and a daily character limit, so spending is noticed at once and capped.

The voices stay the same, so no narration has to be redone.

---

## 5. The Presenter Voices

Chosen by ear in the AI Studio Playground (Gemini 3.8 Flash TTS, speech session), tasks 15 and 16 in `marketing-plan.xlsx`.

| Presenter | Model | Voice | Language setting | Style instruction (sent with every English narration) |
|---|---|---|---|---|
| Sarah | Gemini 3.8 Flash TTS (`gemini-3.8-flash-tts`) | Zuri | English (US) | A composed woman around 40 with a smooth, resonant mid-range voice, crisp UK English diction, and a welcoming tone. Assured, concise, and helpful, guiding viewers through software features with steady confidence and zero hype. |
| Brian | Gemini 3.8 Flash TTS (`gemini-3.8-flash-tts`) | Rami | English (US) | man in his late 30s with a crisp, resonant baritone voice and a clean, refined UK accent. Confident, direct, and engaging, delivering sharp marketing lines with steady authority and zero fluff. |

The Style instruction goes in the Style field (in code, the instruction part of the request), never in the script text, so it is never read aloud.
