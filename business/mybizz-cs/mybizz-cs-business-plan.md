---
title: "mybizz-cs-business-plan"
doc-id: "mb-a926628b"
updated: "2026-11-19"
---
# Mybizz CS — Business Plan

The revenue and the cost per client of Mybizz CS. The product and its prices are in [[[mb-3-cs-project-library:docs-local/mb-3-cs-concept]]](C:/dev/dev-mb-3-cs/mb-3-cs-project-library/docs-local/mb-3-cs-concept.md) section 9. All amounts are GBP and exclude VAT. Mybizz-Live Ltd's fixed costs and the monthly forecast are in `mybizz-live-budget.xlsx` (sheet Forecast B), in `C:\data-mybizz-mgt\business\mybizz-live`, which is the single source of every figure here.

---

## 1. Cash Flow

- Every client pays in advance, for the month or the year ahead.
- Hetzner, Ubicloud, Amazon SES and Groq charge Mybizz after use, on one bill at the end of each month.
- Each client's payment therefore reaches Mybizz before that client's costs fall due.

## 2. Per Client

| Per client, per month, at £119 | GBP |
|---|---|
| Subscription, before tax | £119.00 |
| Paddle's fee (5% + £0.38) | −£6.33 |
| Paid out to Mybizz | £112.67 |
| Amazon SES: email sent and received | −£1.00 |
| Groq: voice £0.25 and AI writing £0.50 | −£0.75 |
| Hetzner: application servers, at 45 clients | −£6.22 |
| Left toward the shared database and Mybizz-Live Ltd's fixed costs | £104.70 |

- An annual-plan client pays £1,190 once a year, less Paddle's fee of £59.88, and leaves £94.18 a month before costs.
- **Amazon SES at £1.00:** 2 broadcasts to 2,000 contacts, 1,000 business emails sent and 1,000 emails received each month, with room for almost double that volume.
- **Groq voice at £0.25:** 5 team members giving 20 voice commands a day on 22 working days, each billed at Groq's 10-second minimum.

## 3. Hosting

- **Database:** the Ubicloud database service with its standby, £116.22 a month, shared with Mybizz FDA and counted once in the budget.
- **Application server:** a Hetzner `CPX42` with backups and its IPv4 address, £69.96 a month. One server holds 12 client copies.
- **Always-running copy:** 1, the test copy, from Month 5, before the first clients. The two demo apps run on the Anvil Business account.
- **Heavy clients:** a client raised from 1 GB to 2 GB of memory takes 2 places on a server, so every 12 heavy clients add one more server at £69.96 a month.
- The hosting design is [[[default:specifications-global/spec-client-instance-hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md).
