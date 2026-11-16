---
title: "fda-business-plan"
updated: "2026-11-16"
---
# Mybizz FDA — Business Plan

**Mybizz Front Desk Assistant · mybizz.live · trading from January 2027**

---

## 1. Summary

Mybizz FDA is an AI front desk for consulting and service businesses. It answers every enquiry in the client's voice, books the meeting and follows up, on email, website, WhatsApp and SMS, with the client in control.

Mybizz FDA has two jobs:

1. **A product in its own right:** one fixed price of £45 a month, with the whole team included.
2. **The funding engine of Mybizz:** Mybizz FDA's income pays for the registration of Mybizz-Live Ltd and the build of Mybizz CS. Mybizz has no lender, no loan and no start-up capital.

Mybizz FDA is also the proof of concept of Mybizz CS. The two are separate products with separate sign-ups.

| Key figure (forecast, Jan 2027 – Apr 2028) | Value |
|---|---|
| Funding | Self-funded from sales; no loans |
| Price | £45 a month per client |
| Clients needed to cover fixed monthly costs | about 5 |
| Active clients at April 2028 | about 42 |
| Revenue over 16 months | about £22,100 |
| Net profit over 16 months | about £17,200 |
| Cash available for Mybizz-Live Ltd and Mybizz CS at April 2028 | about £17,000 |

The full model is `fda-forecast.xlsx`. Every figure above recalculates when its inputs change.

---

## 2. The Business

| Item | Detail |
|---|---|
| Operator | David trading as Mybizz, a sole proprietor, until Mybizz-Live Ltd is registered; Mybizz-Live Ltd from then on |
| Brand and web address | Mybizz, mybizz.live |
| Product | Mybizz FDA |
| Merchant of record | Paddle (checkout, sales tax and VAT, invoices) |
| Banking | Wise |
| Hosting | Mybizz's own Hetzner Cloud servers in the EU |

### The founder
The founder spent most of his working life setting up and running life-support operations at remote sites, from the Congo jungle to Antarctica, where systems had to be simple, self-contained and dependable. Mybizz FDA applies the same discipline to a small business's front desk: no enquiry goes unanswered.

---

## 3. The Problem

- Enquiries arrive by email, website, WhatsApp and SMS and wait hours for a reply, while the customer contacts a competitor.
- The person who should reply is busy delivering work.
- Booking a first call takes several messages back and forth.
- Customers who go quiet are never followed up.
- The business cannot see how many enquiries came in, how fast they were answered and how many became meetings.

---

## 4. The Product

- Every enquiry from every channel arrives in one action queue, sorted, with a reply drafted in the client's voice and in the customer's language.
- New clients start in approve-before-send mode: a team member approves each reply with one click, and every approval records who gave it.
- Real free times from each team member's Google Calendar, booked automatically.
- A short, polite follow-up when a customer goes quiet, stopping the moment the customer replies.
- A website chat bubble, with voice, on the client's own website.
- A dashboard of response times, meetings booked, results by channel and activity by team member.
- Each client has its own copy of Mybizz FDA with its own database; nightly backups go to the client's own storage.

**Firm rules:** one to one only, never bulk messages; never handles payments; STOP means stop; the website chat always says it is an AI.

**Channels at launch:** email, website form, website chat with voice, and SMS. WhatsApp is built from the start and is switched on for every client once Mybizz-Live Ltd is registered and verified by Meta.

The full product definition is the concept document in the Mybizz FDA project library.

---

## 5. Target Market

- **Who:** independent consultants and coaches; small agencies in marketing, design, development, recruitment, advisory, accounting and bookkeeping; fractional executives and advisers; service businesses that book appointments.
- **Size:** one person to a team of about ten.
- **Where:** the United Kingdom first, then the United States, Canada, the EU, the EEA and Switzerland.
- **Local prices (set in Paddle):** £45 (UK), $59 (US), C$79 (Canada), €55 (Europe), CHF 55 (Switzerland).

---

## 6. Competition

| Option | What the business gets | Limitation |
|---|---|---|
| Doing it by hand | Replies when the owner has time | Slow replies lose work; no follow-up |
| A booking link alone | Customers who are ready can book | Questions still wait; no follow-up |
| A shared-inbox or chatbot tool | One more inbox or a website bot | Usually one channel, priced per seat, no booking or follow-up |
| **Mybizz FDA** | Every channel answered, booked and followed up, under the owner's approval | One fixed price for the whole team |

---

## 7. Sales and Marketing

- **Approach:** direct, personal, one-to-one outreach by the founder, and building in public on LinkedIn and short video. No paid advertising while Mybizz FDA funds Mybizz-Live Ltd.
- **Trial:** prospects test Mybizz FDA by enquiring through Mybizz's own front desk on mybizz.live.
- **Offer:** £45 a month, month to month, no contract, no setup fee.
- **Plans:** `fda-marketing-plan.md`, `fda-sniper-outreach-kit.md` and `fda-content-and-social-pack.md`.

---

## 8. Operations

- **Hosting:** each client's copy runs in its own container on Mybizz's Hetzner servers in the EU, with its own database on a database pair (primary and live standby).
- **Management:** the Mybizz management app signs up clients, starts and updates their copies, watches their health and handles Paddle billing.
- **Costs the client pays directly:** AI on its own OpenRouter key, WhatsApp messages charged by Meta, SMS on its own phone plan, storage above Cloudflare's free tier.
- **Running the business:** `fda-operations-plan.md`.

---

## 9. Financial Forecast (January 2027 – April 2028)

### Assumptions
- New clients: 6 a month in January to March 2027, 5 a month in April to June, 3 in July and August, then 2 a month.
- Monthly churn: 3%.
- Paddle fees: 5% plus £0.38 per payment.
- Per-client costs: £1.50 a month for hosting, email and voice, plus 20% non-recoverable VAT.
- Fixed costs: Hetzner servers £20 a month and Anvil, domain and accounting £121.73 a month, each plus 20% non-recoverable VAT.
- Mybizz-Live Ltd registration and bank set-up: £150 plus VAT in February 2027, paid from Mybizz FDA's income.
- No marketing spend and no founder salary.

### Results
| Figure | Value |
|---|---|
| Lowest month-end cash | positive in every month |
| Active clients at April 2028 | about 42 |
| Revenue over 16 months | about £22,100 |
| Net profit over 16 months | about £17,200 |
| Cash at April 2028 | about £17,000 |

---

## 10. Risks and Answers

| Risk | Answer |
|---|---|
| Slow first sales | Fixed costs are about £170 a month; about 5 clients cover them |
| WhatsApp not yet available | Email, website form, website chat and SMS work from day one; WhatsApp is switched on after Meta verification |
| A server fails | A live standby database, nightly client backups and monitored servers |
| AI writes something wrong | Approval before sending by default; facts only from the client's own content |
| The founder's time | Self-service setup with help videos; Mybizz's own front desk answers prospects |
