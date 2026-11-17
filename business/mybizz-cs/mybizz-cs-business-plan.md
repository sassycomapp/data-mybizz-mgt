---
title: "mybizz-cs-business-plan"
doc-id: "mb-a926628b"
updated: "2026-11-17"
---
# Mybizz CS — Business Plan

The revenue and the cost per client of Mybizz CS. The product and its prices are in [[[mb-3-cs-project-library:docs-local/mb-3-cs-concept]]](C:/dev/dev-mb-3-cs/mb-3-cs-project-library/docs-local/mb-3-cs-concept.md) section 9. All amounts are GBP and exclude VAT. Mybizz-Live Ltd's fixed costs and the monthly forecast are in `mybizz-live-budget.xlsx` (sheet Forecast B), in `C:\data-mybizz-mgt\business\mybizz-live`, which is the single source of every figure here.

---

## 1. Cash Flow

- Every client pays in advance, for the month or the year ahead.
- Hetzner, Amazon SES and Groq charge Mybizz after use, on one bill at the end of each month.
- Each client's payment therefore reaches Mybizz before that client's costs fall due.

## 2. Per Client

| Per client, per month, at £119 | GBP |
|---|---|
| Subscription, before tax | £119.00 |
| Paddle's fee (5% + £0.37) | −£6.32 |
| Paid out to Mybizz | £112.68 |
| Amazon SES: email sent and received | −£1.00 |
| Groq: voice £0.25 and AI writing £0.50 | −£0.75 |
| Hetzner: hosting, database and backups, at 45 clients | −£2.35 |
| Left toward Mybizz-Live Ltd's fixed costs | £108.58 |

- An annual-plan client pays £1,190 once a year, less Paddle's fee of £59.87, and leaves £94.18 a month before costs.
- **Amazon SES at £1.00:** 2 broadcasts to 2,000 contacts, 1,000 business emails sent and 1,000 emails received each month, with room for almost double that volume.
- **Groq voice at £0.25:** 5 team members giving 20 voice commands a day on 22 working days, each billed at Groq's 10-second minimum.

## 3. Hosting on Hetzner

- **Database server pair with backups:** £20.09 a month, fixed. The second server is a live standby that takes over if the first one fails.
- **Application server with backups:** £21.42 a month for each server. One server holds 12 client copies.
- **Always-running copies:** 3 (two demo apps and the test copy), from May 2027, before the first clients.
- **Heavy clients:** a client raised from 1 GB to 2 GB of memory takes 2 places on a server, so every 12 heavy clients add one more server at £21.42 a month.
