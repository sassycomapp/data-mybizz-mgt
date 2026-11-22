---
title: "narration-voices"
---
# Task Spec Sheet — Mybizz Narration Voices

**Task:** C2 in `marketing-project-plan.xlsx`
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

- **The voices.** Gemini's voices are the same voice set Google sells in Cloud Text-to-Speech as Chirp 3 HD. Each presenter, Sarah and Brian, has one Gemini voice, chosen by ear as the closest match to the presenter's Google Flow voice, and kept for the life of the presenter.
- **The accent.** Gemini voices take their accent and delivery from the instruction sent with the text. Every narration request asks for a mild British accent and a calm, professional delivery, so every video sounds the same.
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
