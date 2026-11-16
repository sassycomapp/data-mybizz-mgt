---
title: "Front-Desk-Assistant"
doc-id: "mb-0a2208a3"
updated: "2026-11-15"
---
# Front Desk Assistant

**Lightweight AI front desk for consultants and service businesses**: 

It captures enquiries, responds in the owner’s voice, records contacts, books meetings, and runs 1-to-1 follow-up. 

## Product Role

MVP for Mybizz CS

## Product definition

**Working name:** "Front Desk Assistant"

**One-sentence promise:**

> Connect your inbox, messaging phone, and calendar, answer your wizard questions, and have a working lead-response and booking assistant in under 30 minutes.

The customer experiences value before they configure anything complex. The wizard creates a usable system from a small number of answers, then improves it as the user adds detail.

## Go-to-market

Sell the outcome, not the technology.

**Primary message:**

> **Never miss a qualified enquiry again. Your AI front desk responds, books calls, and follows up—using your inbox, WhatsApp, SMS, calendar, and rules.**

Do not lead with “AI agent,” “OpenRouter,” or “multi-agent orchestration.” Buyers care about missed leads, slow replies, manual scheduling, and lost revenue.

**Launch positioning:** Start with independent consultants and small agencies; Gmail plus website form, WhatsApp, and SMS; English-only US/UK/Canada/EU; custom lightweight SaaS built on Anvil (Material 3) with self-hosted integration APIs; Starter at $59/month. That gives you a clear buyer, a high-converting multi-channel surface, a credible price, and a product that reaches market quickly without pretending to be a complete business operating system.

## Target customer

“Consulting and Services” 

**Generally:**

- Independent consultants and coaches.
- Small agencies: marketing, design, development, recruitment, legal-adjacent advisory, accounting/bookkeeping.
- Fractional executives, advisors, and professional-service firms.
- Solo operators and teams of 1–10 people.

**Common workflow:**

enquiry → qualified response → booking → 1-to-1 follow-up → simple pipeline visibility

## Product Scope

Build only what supports the common workflow.

| Area            | Include                                                                                                                                                 | Exclude                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Assistant       | Guided setup wizard, business profile, service catalogue, tone-of-voice settings, FAQ/knowledge snippets                                                | Full RAG over large document libraries, complex custom agent builder                          |
| Inbox           | Gmail and Microsoft 365 email; WhatsApp (QR Linked Device via Evolution API); SMS (Android Gateway via SMSGate); unified lead inbox & message threading | Voice calls, Instagram/LinkedIn DMs, bulk SMS/WhatsApp marketing blasts (strictly prohibited) |
| Lead capture    | Website form/embed, inbound email parsing, inbound WhatsApp/SMS parsing, manual contact entry                                                           | Landing-page builder, ads integration, scraping                                               |
| CRM             | Lightweight contacts, companies optional, lead status, notes, activity timeline, tags, owner/user                                                       | Custom objects, complex pipelines, enterprise permissions                                     |
| Booking         | Google Calendar first; availability rules; booking link; meeting confirmation and rescheduling                                                          | Outlook calendar; complex resource scheduling                                                 |
| Responses       | AI-drafted replies, templates, approval mode, send-from-connected mailbox/WhatsApp/SMS                                                                  | Marketing campaigns, cold outreach, bulk messaging blasts (never permitted)                   |
| Follow-up       | Rule-based 1-to-1 sequences: no reply, meeting reminder, post-meeting follow-up                                                                         | Marketing automation, broadcast journeys                                                      |
| Storage/Archive | Per-tenant Cloudflare R2 bucket provisioning for automated backups and archiving old webhook payloads/logs                                              | End-user file sharing portal or general cloud drive                                           |
| Reporting       | New leads, response time, booked meetings, follow-ups due, pipeline by stage                                                                            | Advanced BI, forecasting, attribution                                                         |
| AI              | OpenRouter BYOK; model selection; prompt templates; usage tracking                                                                                      | Hosting customer model keys beyond OpenRouter                                                 |

## Define the CRM precisely

Do not call it a CRM in the marketing copy until it has a defined, useful minimum. Internally, build these objects:

- **Contact:** name, email (optional if phone present), phone (optional if email present—at least one required), company optional, source, tags, owner, consent/do-not-contact status.
- **Lead:** contact, service interest, status, urgency, estimated value optional, assigned user, next action, next-action date.
- **Message:** inbound/outbound, channel (`email`, `whatsapp`, `sms`, `webform`), thread ID, external message ID (for webhook deduplication), delivery status (`queued`, `sent`, `delivered`, `failed`), AI-drafted or human-sent, approval state.
- **Channel Connection:** workspace, WhatsApp instance name & status (`connected`/`disconnected`), SMSGate credentials (encrypted) & device status, R2 bucket name & status.
- **Appointment:** contact, service, start/end, calendar event ID, status, meeting link.
- **Workflow run:** trigger, steps, status, errors, approvals, timestamps.
- **Audit event:** actor, action, object, before/after summary, timestamp.

Use a very simple pipeline:

`New enquiry → Responded → Meeting booked → Proposal/quote → Won → Lost / Not a fit`

Do not build custom pipeline stages in v1. Let users tag leads, but keep the stage model fixed so reporting and automation remain reliable.

**The product produces this outcome immediately:**

A new enquiry arrives via email, form, WhatsApp, or SMS; the assistant classifies it, drafts a response, creates/updates the CRM record, proposes available times, and runs 1-to-1 follow-up if there is no reply.

## Product screens

Keep the interface small, built cleanly on the custom **Material 3 theme in Anvil**. A customer should be able to operate the product from roughly seven screens.

| Screen                 | Purpose                                   | Must-have elements                                                                                       |
| ---------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Onboarding wizard**  | Turn answers into a working configuration | Business profile, services, tone, calendar, WhatsApp/SMS & R2 storage setup, approval rules, test lead   |
| **Inbox / Leads**      | Show what needs attention                 | Channel health badges (Email/WA/SMS), new enquiries, drafts awaiting approval, urgent flags, lead status |
| **Lead record**        | Show one prospect’s history               | Contact details, channel source, messages, AI extraction, notes, timeline, next action                   |
| **Approval queue**     | Let the owner approve or edit AI output   | Draft, channel indicator, original enquiry, suggested action, edit/send/reject, reason if rejected       |
| **Calendar & booking** | Control availability and bookings         | Google connection, working hours, meeting types, buffers, booking link                                   |
| **Follow-ups**         | Configure simple 1-to-1 sequences         | Trigger, delay, message template, stop conditions, active/paused                                         |
| **Dashboard**          | Prove value                               | Leads, response time, bookings, follow-ups due, AI usage, channel/archive errors                         |

**The primary interface should be an action queue**: 

“Here are the five things that need you today.”

Do not begin with a general-purpose chat interface.

## Minimum data model

A simple but extensible schema is enough for launch.

- **Workspace:** business, owner, subscription status, locale, time zone, Cloudflare R2 bucket identifier.
- **User:** name, email, role, permissions.
- **Channel Connection:** workspace, WhatsApp session ID/status, SMSGate login/encrypted password/status, email provider status.
- **Contact:** name, email optional, phone optional, company, tags, consent/source, do-not-contact flag, owner.
- **Lead:** contact, status, source, service interest, urgency, budget, timeline, assigned user, next action.
- **Message:** channel, direction, subject, body, status, delivery status, external message ID, thread ID, AI-generated flag.
- **AI action:** type, input reference, model used, tokens/cost, result, approval status, error.
- **Appointment:** lead, meeting type, start/end, calendar event ID, status, reminders.
- **Workflow:** trigger, conditions, steps, active/paused, version.
- **Audit event:** actor, action, object, timestamp, before/after summary.

The important design rule is: **never overwrite the original enquiry or an owner-approved message.** Store drafts, approvals, edits, and sends as separate events. This gives you traceability and makes AI mistakes recoverable.

## Workflow engine: keep it narrow

Do not build a visual automation builder yet. Build three hard-coded, configurable workflow templates.

#### 1. New enquiry

Trigger: website form, inbound email, inbound WhatsApp message, or inbound SMS.

Steps:

- Buffer burst messages (10–15 second debounce on WhatsApp/SMS so multi-bubble messages are processed as one enquiry).
- Detect duplicate contact (match by email or normalized phone number).
- Extract structured details.
- Classify: new lead, existing client, spam, unsupported request.
- Create/update CRM record.
- Draft acknowledgement or tailored response.
- If urgent or high-value, notify owner.
- If approved/allowed, send reply on the originating channel.
- Offer booking link or available slots.

#### 2. No-response follow-up (1-to-1 only)

Trigger: an active inbound lead has not replied after a configured delay.

Steps:

- Check status and opt-out/do-not-contact rules.
- Send a short, non-pushy 1-to-1 follow-up on the active thread.
- Stop immediately upon any reply or after the configured number of attempts.
- Mark lead “stalled” after the final attempt.
- Notify owner if the lead showed buying intent.

#### 3. Booking lifecycle

Trigger: meeting booked, rescheduled, or not attended.

Steps:

- Send confirmation.
- Send reminder before the meeting.
- Create a post-meeting follow-up task or draft.
- Update lead status.
- Notify owner if a meeting is cancelled or rescheduled.

This gives you enough flexibility to feel like an “agent” without exposing customers to a complex, error-prone workflow editor.

## AI design

Use AI for a limited set of jobs, with deterministic business rules around it.

| Task                           | Recommended approach                                                |
| ------------------------------ | ------------------------------------------------------------------- |
| Spam/irrelevant classification | Rules first, then a cheap model                                     |
| Contact and lead extraction    | Structured output with validation                                   |
| Reply drafting                 | Retrieval from approved business profile, services, FAQs, templates |
| Meeting-slot selection         | Deterministic calendar logic; AI only phrases the message           |
| Follow-up decision             | Rules and lead status; not free-form AI judgement                   |
| Urgency detection              | Rules plus model classification, with owner notification            |
| Tone adaptation                | Model, constrained by approved style examples                       |

A major implementation rule: **the model proposes; your application validates and executes.** For example, the model may return a proposed meeting time, but the calendar service—not the model—must confirm availability and create the event.

## Prompt and knowledge structure

Give the model a tightly scoped context, rather than dumping an entire knowledge base into every prompt.

**Include:**

- Business name, description, audience, tone.
- Active services, prices or price ranges, delivery expectations.
- Booking rules and available slots.
- Qualification questions.
- Approved FAQ answers.
- Recent message thread.
- Extracted lead data.
- Strict instructions: do not invent facts, do not make commitments, do not request or process payments or customer financial data, do not provide legal/medical/financial advice, do not disclose internal information.

Use a retrieval layer only when the knowledge base grows. For launch, a structured “business profile + services + FAQs” store is enough and is easier to debug than full RAG.

## Approval and safety controls

**Your default should be conservative:**

- **Zero marketing or bulk blasts:** Front Desk Assistant is strictly a 1-to-1 enquiry response and booking assistant. It must **never** be used for marketing campaigns, cold outreach, or bulk SMS/WhatsApp blasts. Enforce hard rate limits and block batch/list sending at the application layer.
- **No payments or financial data:** The assistant never takes payments, generates payment links, or collects/stores customer credit card, banking, or sensitive financial details.
- New accounts begin in **approve-before-send** mode.
- AI cannot send custom pricing, proposals, contracts, or commitments without approval.
- Every outbound email includes the customer’s real identity and an unsubscribe/opt-out path where legally required. On WhatsApp and SMS, replying `"STOP"` or `"UNSUBSCRIBE"` immediately sets the lead to **Do Not Contact** and halts all automated messages.
- A lead can be manually marked “do not contact,” which immediately halts all sequences.
- The owner can undo or pause a workflow.
- All sends, bookings, and CRM updates appear in an activity feed.
- Failed integrations, disconnected phones (WhatsApp/SMSGate), and model errors create visible high-priority tasks in the Action Queue rather than silently disappearing.

## BYOK implementation

For launch, OpenRouter BYOK is a good way to avoid becoming an AI-cost reseller on day one. Make the experience guided:

Provide three presets:

- **Fast:** inexpensive model for classification, extraction, and simple acknowledgements.
- **Balanced:** default for replies and follow-ups.
- **Premium:** optional for complex, high-value enquiries.

**Also provide:**

- A connection test during onboarding.
- Clear display of the selected model and estimated cost per action.
- A monthly spend ceiling.
- Automatic fallback to draft-only mode if the key fails, quota is exhausted, or the model errors repeatedly.
- A usage page showing actions, model usage, and estimated spend.
- No logging of prompt or completion content by default; store metadata and redacted diagnostics only.

## What to exclude from launch

Be ruthless. These are strictly excluded from the product:

- **Marketing campaigns, cold outreach, and bulk SMS/WhatsApp blasts (prohibited permanently).**
- **Payments, invoicing, e-signature, and handling customer financial information (prohibited).**
- Voice calls, Instagram DMs, LinkedIn DMs.
- Custom AI agent builder.
- Large-document RAG.
- Multi-language translation at launch.
- Complex role hierarchies.
- White-label agency portal.
- Native mobile apps.
- Deep third-party CRM integrations.

## Metrics that prove value

Track metrics that a business owner understands—not model metrics.

- Percentage of new enquiries answered within 5, 15, and 60 minutes.
- Number of leads captured (broken down by Email, Form, WhatsApp, SMS).
- Meetings booked.
- Meeting-show rate.
- Follow-up completion rate.
- Leads moved from “new” to “qualified,” “booked,” “won,” or “lost.”
- Time saved from drafts approved without major edits.
- Revenue influenced by leads that reached a booked meeting.
- AI action success rate and failure reasons.

Show these on the dashboard from day one. Even with modest early numbers, “your assistant responded to 38 enquiries and booked 9 calls this month” is a compelling outcome.

## The onboarding wizard

The wizard takes no more than 10–15 minutes and produces a working configuration.

**Ask and provision in this order:**

1. **Business basics:** business name, website, services, typical client type, time zone, working hours.
2. **Communication style:** formal, warm, concise, technical; languages; signature; prohibited claims.
3. **Services and offers:** service names, starting price or “from” price, delivery timeframe, ideal client, qualifying questions.
4. **Lead rules:** what counts as a qualified lead, what should trigger an urgent notification, what should be politely declined.
5. **Calendar rules:** Google Calendar connection, availability, meeting duration, buffer time, booking link, meeting type.
6. **Connect messaging channels (Email required; WhatsApp & SMS optional):**
   - Connect Gmail or Microsoft 365 inbox.
   - **WhatsApp:** Generate an inline QR code via Evolution API so the owner can pair their company WhatsApp Business phone in 30 seconds.
   - **SMS:** Enter SMSGate Android app Cloud credentials to automatically register the tenant's SMS webhook.
7. **Storage & retention setup (Automated + Confirmed):** Automatically provision a dedicated, isolated **Cloudflare R2 bucket** (`fda-tenant-{workspace_id}`) for the client's workspace, allowing the owner to confirm their retention window (e.g., archive raw webhook payloads and backups older than 30/60/90 days to R2).
8. **Approval policy & usage acknowledgement:** Confirm 1-to-1 anti-spam policy (no bulk blasts), set default **approve-before-send** mode, and configure low-risk acknowledgement rules.
9. **Follow-up rules:** wait period, number of attempts, stop conditions, do-not-contact rules.
10. **Existing tools:** import contacts from CSV (with explicit consent confirmation).

**Show a “Your assistant is live” screen with:**

- Connected channels (Email, WhatsApp, SMS status badges) & Cloudflare R2 backup bucket confirmation.
- Booking link.
- Test lead simulation.
- First AI-drafted response.
- CRM record created.
- Follow-up sequence enabled or disabled.

## Allowed behavior

Use a constrained assistant, not an open-ended chatbot.

The assistant should have a small set of reliable actions:

- Classify enquiry: new lead, existing client, supplier, spam, unsupported request.
- Extract structured data: name, email, phone, company, service interest, budget, timeline, urgency, source.
- Create or update a CRM contact and lead record.
- Draft a reply based on business profile and approved service information.
- Suggest meeting slots and create a booking.
- Send a booking confirmation and reminder.
- Trigger a 1-to-1 follow-up when a lead goes quiet.
- Notify the owner for urgent, unusual, or high-value enquiries.
- Maintain an audit trail: what the AI saw, drafted, sent, booked, or changed.

**Not allowed behavior:**
Do **not** allow the assistant to send bulk/marketing messages, request or process payments/financial data, or invent pricing, legal advice, delivery dates, guarantees, or commitments.

## Human-in-the-loop design

**Approval as a first-class feature**

Three modes:

- **Draft only:** AI prepares everything; the owner sends.
- **Approve before send:** AI drafts and queues; owner approves with one click.
- **Autonomous for selected actions:** AI can send 1-to-1 acknowledgement messages, create CRM records, and send booking reminders; owner approval remains required for custom pricing, proposals, contractual commitments, or sensitive matters.

Default new accounts to **approve before send**. This reduces fear, protects reputation, and gives the customer confidence before enabling automation.

Every factual business claim should come from the customer’s configured service catalogue and approved content.

## Technical architecture

Keep the product deliberately simple, unified, and self-hosted on **Hetzner Cloud**.

- **Hosting Infrastructure:** Hetzner Cloud VPS (Ubuntu 24.04, 4 GB+ RAM) running Docker Compose behind **Caddy** for automatic SSL/HTTPS.
- **Front end & App Server:** Self-hosted **Anvil App Server** (`anvil-app-server`) running on the Hetzner VPS, built with your custom **Material 3 theme** (onboarding wizard, action queue, unified inbox, CRM board/list, calendar settings, templates, reporting).
- **Backend & Messaging Gateway Stack (Docker Compose on Hetzner):**
  - **Anvil Runtime / Python Backend:** Multi-tenant API, workflow engine, scheduler, integration adapters, webhook receivers, and audit log.
  - **Evolution API:** Self-hosted multi-tenant WhatsApp gateway managing per-client QR sessions and webhooks.
  - **SMSGate Integration:** Connects to each client's Android device running SMSGate (Cloud Server mode) via the official `android-sms-gateway` Python SDK.
  - **PostgreSQL:** Primary database with strict tenant isolation (`workspace_id`); stores contacts, leads, active messages, events, workflows, settings, and audit records.
  - **Redis:** Job queue, WhatsApp/SMS burst message debouncing, and Evolution API session cache.
- **Archival & Backup Storage (Cloudflare R2):**
  - One isolated **Cloudflare R2 bucket per tenant** created programmatically via the Cloudflare R2 API during onboarding.
  - Automated scheduled jobs export workspace database snapshots and offload raw webhook payloads/logs older than the retention threshold (e.g., 30 days) to the tenant's R2 bucket, keeping PostgreSQL fast and lean.
- **AI layer:** OpenAI-style API via OpenRouter BYOK wrapped in an internal `ModelProvider` interface. Store the customer’s key encrypted; never log prompts or completions by default; let the customer choose model and spend ceiling.
- **Integrations:** Gmail/Google Workspace, Microsoft 365/Graph, Google Calendar, website form embed, Evolution API (WhatsApp), SMSGate (SMS), and Cloudflare R2.
- **Observability:** Delivery status, channel connection health checks (WhatsApp/SMSGate heartbeat), model errors, archive job status, and a customer-visible activity feed.

## BYOK and cost control

BYOK is sensible for a fast launch, but it creates a support risk: customers may use weak models, exceed rate limits, expose keys, or blame your product for poor output.

Mitigation:

- Recommended model presets: “Fast/cheap,” “Balanced,” “High quality.”
- Show estimated monthly usage and remaining budget.
- Set a hard monthly spend ceiling and pause non-critical automation when reached.
- Use small, cheap models for classification, extraction, and drafting; reserving stronger models for complex replies.
- Cache extracted lead data and reusable business-profile context.
- Log token usage per tenant, workflow, and action.

Make BYOK the only option at launch.

## Billing, Privacy, and Compliance

The business needs a privacy policy, terms of service, data-processing terms where applicable, sub-processor disclosures, security practices, and a clear position on customer data.

**Important distinctions:**

- **Subscription Billing:** Handled externally by your billing merchant of record (e.g., Paddle) for SaaS subscriptions only. **Front Desk Assistant itself never takes payments or handles end-customer financial data.**
- **Mybizz:** Remains the software provider and data processor for account, usage, support, and transit message data hosted on Hetzner and Cloudflare R2.
- **Customer (Workspace Owner):** Remains the data controller responsible for the lawful basis and consent for contacts they import, email addresses/phone numbers they message, and personal data in their CRM records.
- **Sub-processors:** Disclose **Hetzner** (application & database hosting), **Cloudflare R2** (per-tenant encrypted backup and webhook archival storage), and **OpenRouter** (AI model routing, BYOK).

**For EU/UK/North America, implement a practical baseline from day one:**

- Data-processing agreement and sub-processor list.
- Clear retention and deletion controls (including automated archival to the tenant's Cloudflare R2 bucket and clean bucket deletion upon account termination).
- Encryption in transit (TLS via Caddy) and at rest (PostgreSQL, encrypted credentials, and Cloudflare R2 server-side encryption).
- Role-based access and audit logs.
- Export and delete account data.
- No training customer business data on foundation models by default.
- Strict prohibition of bulk marketing blasts; immediate automated opt-out (`STOP` / unsubscribe) handling across Email, WhatsApp, and SMS.

## Launch sequence

Single once-off launch, not staged.

---

# Changes to the design

Add Webchat facility
