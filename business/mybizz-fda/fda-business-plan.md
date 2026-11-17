---
title: "fda-business-plan"
updated: "2026-11-17"
doc-id: "mb-0defdbae"
---
# Mybizz FDA — Business Plan

**Mybizz Front Desk Assistant · mybizz.live · trading from January 2027**

---

## 1. Summary

Mybizz FDA is an AI front desk for consulting and service businesses. It answers every enquiry in the client's voice, books the meeting and follows up, on email, website, WhatsApp and SMS, with the client in control.

- **Price:** one fixed price of £45 a month, with the whole team included.
- **Place in Mybizz:** Mybizz FDA is the proof of concept of Mybizz CS. The two are separate products with separate sign-ups. The company plan, funding and budget are in `business/mybizz-live/mybizz-live-business-plan.md`.

---

## 2. The Problem

- Enquiries arrive by email, website, WhatsApp and SMS and wait hours for a reply, while the customer contacts a competitor.
- The person who should reply is busy delivering work.
- Booking a first call takes several messages back and forth.
- Customers who go quiet are never followed up.
- The business cannot see how many enquiries came in, how fast they were answered and how many became meetings.

---

## 3. The Product

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

## 4. Target Market

- **Who:** independent consultants and coaches; small agencies in marketing, design, development, recruitment, advisory, accounting and bookkeeping; fractional executives and advisers; service businesses that book appointments.
- **Size:** one person to a team of about ten.
- **Where:** the United Kingdom first, then the United States, Canada, the EU, the EEA and Switzerland.
- **Local prices (set in Paddle):** £45 (UK), $59 (US), C$79 (Canada), €55 (Europe), CHF 55 (Switzerland).

---

## 5. Competition

| Option | What the business gets | Limitation |
|---|---|---|
| Doing it by hand | Replies when the owner has time | Slow replies lose work; no follow-up |
| A booking link alone | Customers who are ready can book | Questions still wait; no follow-up |
| A shared-inbox or chatbot tool | One more inbox or a website bot | Usually one channel, priced per seat, no booking or follow-up |
| **Mybizz FDA** | Every channel answered, booked and followed up, under the owner's approval | One fixed price for the whole team |

---

## 6. Sales and Marketing

- **Approach:** direct, personal, one-to-one outreach by the founder, and building in public on LinkedIn and short video. No paid advertising.
- **Trial:** prospects test Mybizz FDA by enquiring through Mybizz's own front desk on mybizz.live.
- **Offer:** £45 a month, month to month, no contract, no setup fee.
- **Plans:** `fda-marketing-plan.md`, `fda-sniper-outreach-kit.md` and `fda-content-and-social-pack.md`, in `marketing`.

---

## 7. Operations

- **Hosting:** each client's copy runs in its own container on Mybizz's Hetzner servers in the EU, with its own database on a database pair (primary and live standby).
- **Management:** the Mybizz management app signs up clients, starts and updates their copies, watches their health and handles Paddle billing.
- **Costs the client pays directly:** AI on its own OpenRouter key, WhatsApp messages charged by Meta, SMS on its own phone plan, storage above Cloudflare's free tier.
- **Running the business:** `fda-operations-plan.md`.

---

## 8. Risks and Answers

| Risk | Answer |
|---|---|
| WhatsApp not yet available | Email, website form, website chat and SMS work from day one; WhatsApp is switched on after Meta verification |
| A server fails | A live standby database, nightly client backups and monitored servers |
| AI writes something wrong | Approval before sending by default; facts only from the client's own content |
