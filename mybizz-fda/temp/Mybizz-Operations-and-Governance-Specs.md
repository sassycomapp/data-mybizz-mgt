---
title: "Mybizz-Operations-and-Governance-Specs"
doc-id: "mb-3d255dca"
updated: "2026-11-15"
---
# Mybizz Operations, Fair-Use & Governance Specifications

**Scope:** Mybizz-Live Ltd · Front Desk Assistant (MVP) & Mybizz CS (`mb-3-cs`)  
**Infrastructure:** Hetzner Cloud (EU) · Cloudflare R2 · Amazon SES · OpenRouter / Groq · Paddle  
**Replaces:** Sections 4–7 of legacy `Budget` (`mb-3afb1c99`), updated for Hetzner Cloud and the two-step bootstrapped launch.

---

## 1. Fair-Use Resource Limits (Per Client Workspace)

Every shared and managed resource carries a fair-use limit per client. Limits are set well above normal and heavy usage so legitimate customers never hit them, while protecting platform stability and unit margins. Fair-use terms are incorporated into the Client Service Agreement.

| Resource | Budgeted Use | Warning to Client | Hard Limit | Action at Hard Limit |
| :--- | :--- | :--- | :--- | :--- |
| **Database connections** | Up to 3 | None | 3 per client DB user | Further requests queue for a free connection. |
| **Database query time** | Under 1 second | None | 60 seconds per query | Query is cancelled and logged. |
| **Idle open transaction** | None | None | 120 seconds | Database session is terminated automatically. |
| **Database size (PostgreSQL)** | ~100 MB / year | 1 GiB | 2 GiB | Bulk imports pause for that client; David is notified via App 5 heartbeat. |
| **Container memory** | 1 GiB | At 80% memory use | 2 GiB container | App 5 scales container to 2 GiB max; David is notified if exceeded. |
| **Marketing email (Mybizz CS)** | ~10,000 / month | 20,000 / month | 25,000 / month | Marketing campaigns pause until next cycle; transactional emails continue. |
| **All email (Mybizz CS)** | ~12,000 / month | 40,000 / month | 50,000 / month | Non-auth sending pauses until next cycle; David is notified. |
| **Email reputation (SES)** | Bounces < 2%, Complaints < 0.05% | SES warning threshold | SES pause threshold | SES pauses that client's tenant only; App 5 notifies client and David. |
| **WhatsApp & SMS (Front Desk Assistant)** | 1-to-1 conversational replies & reminders | Rate burst warning | **Strict 1-to-1 only (0 bulk blasts)** | Bulk/broadcast sends are blocked at the API layer; `"STOP"`/`"UNSUBSCRIBE"` immediately sets `do_not_contact = True`. |
| **AI & voice spend (Mybizz CS)** | £5.60 / month | £5.60 / month | £16.80 / month | Natural voice & AI assists pause until next cycle; browser speech continues. |
| **AI BYOK spend (Front Desk Assistant)** | Client-paid (OpenRouter BYOK) | Client-configured ceiling | Client monthly ceiling | Falls back automatically to **Draft-Only Mode** when ceiling/quota is hit. |
| **AI request rate** | A few per minute | None | 20 requests / minute | Excess requests queue gracefully. |
| **Data transfer** | Within 150 GB / month | 150 GB / month | 500 GB / month | Client and David notified; fair-use overage terms apply. |
| **Client Cloudflare R2 storage** | Under 10 GB (free tier) | 8 GB | Client R2 account limit | Cloudflare bills client directly above 10 GB at $0.015/GB/month. |

---

## 2. Maintenance & Automation Schedule (App 5 & Hetzner)

Routine maintenance is automated via **App 5 (Mybizz Management App)** and scheduled cron/systemd workers on **Hetzner Cloud**. App 5 sends David one daily summary and immediate alerts only when human intervention is required.

| Maintenance Area | Frequency | Executor | Automated Behaviour |
| :--- | :--- | :--- | :--- |
| **Client container scaling** | On memory alert | App 5 | Containers exceeding 80% RAM are resized up to 2 GiB. |
| **Hetzner DB cluster scaling** | At 60 & 130 clients | App 5 / David | Primary + hot-standby Hetzner DB nodes scale from CX33 (8 GB) to CX43 (16 GB) at 60 clients and CCX33 (32 GB) at 130 clients during the Sunday 06:00 UK maintenance window. |
| **Disk & volume monitoring** | Continuous | Hetzner Cloud + App 5 | Automated alert at 75% volume usage to expand Hetzner Block Storage before disk saturation. |
| **Fair-use enforcement** | Continuous / Daily | App 5 | Measures DB size, email counts, AI spend, and data transfer against Section 1 caps. |
| **New client provisioning** | Per registration | App 5 | Provisions isolated container, PostgreSQL DB/user, Cloudflare R2 bucket, SES identity, and DNS records. |
| **WhatsApp / SMSGate heartbeat** | Every 15 minutes | App 5 / FDA Worker | Checks Evolution API session status and SMSGate device connectivity; creates high-priority Action Queue alert if a client's phone disconnects. |
| **Non-payment lifecycle** | Per failed webhook | App 5 | Driven by Paddle webhooks: grace warning on Day 1, suspension on Day 7, clean exit & R2 export on Day 37. |
| **Staged release roll-out** | Per approved release | App 5 | Deploys to Test Instance → 10% of clients → 100% of clients. Failed health checks trigger automatic rollback. |
| **Container image security** | Weekly & per build | GitHub Actions | Scans release images; fails builds with end-of-life packages; flags high/critical CVEs (CVSS >= 7.0) for patching within 14 days. |
| **Registry cleanup** | Per release | GitHub Actions | Prunes container images older than the last three releases. |
| **Raw email & webhook archival** | Daily | App 5 / Worker | Deletes processed raw inbound SES files from S3 after 7 days; archives webhook payloads and audit logs older than 30 days to the client's Cloudflare R2 bucket. |
| **Daily backup verification** | Daily | App 5 | Verifies arrival, timestamp, and file size of each client's encrypted nightly backup in Cloudflare R2. |
| **Monthly backup restore drill** | Monthly | Test Instance (App 5) | Restores one client's nightly R2 backup into a scratch database on Hetzner, verifies row counts against source, drops scratch DB, and logs proof. |
| **Domain & SSL certificate check** | Daily | App 5 | Verifies DNS resolution, Caddy TLS certificates, and domain expiry (warns client 30 days prior). |
| **App 5 uptime monitoring** | Every 1 minute | External Uptime Check | Monitors App 5 status endpoint and alerts David if App 5 fails or any active client heartbeat exceeds 30 minutes. |
| **Access key rotation** | Yearly | David (prompted by App 5) | App 5 sends rotation instructions 14 days before key expiry (~10 minutes). |
| **Statutory & tax deadlines** | Daily / Quarterly | FreeAgent + App 5 | Once Mybizz-Live Ltd is incorporated, App 5 reads FreeAgent's tax timeline daily and alerts David 30 days before VAT, Confirmation Statement, Annual Accounts, and Corporation Tax deadlines. |
| **Wise bank feed check** | Daily & every 90 days | App 5 + David | Verifies daily bank transaction sync in FreeAgent and reminds David 7 days before 90-day Open Banking consent expiry. |

### Hands-On Tasks Remaining for David

- Approve production releases (including security-patched images).
- Respond to escalated client support tickets (within 24 business hours; 4 hours for business-stopping faults).
- Act on abuse reports sent to `abuse@mybizz.live` using App 5's **Suspend** action.
- Rotate cloud/API access keys annually (~10 minutes) and keep backup payment cards active on Hetzner, Anvil, AWS, Groq, and Cloudflare.
- Maintain two FIDO2 hardware security keys (one daily carry, one secure backup).
- Renew Cyber Essentials certification and combined business insurance annually (after UK incorporation).
- Approve and submit VAT, Confirmation Statement, Annual Accounts, and Corporation Tax filings in FreeAgent.

---

## 3. Client Risks & Technical/Operational Safeguards

| Risk Scenario | Safeguard & Mitigation |
| :--- | :--- |
| **Noisy-neighbour DB load** | Each client connects via a dedicated PostgreSQL user capped at 3 connections, 60s query timeout, 120s idle transaction timeout, and 2 GiB storage cap. |
| **Client bad email list harms shared SES reputation** | Isolated SES tenant per client with automatic bounce (4%) and complaint (0.08%) CloudWatch alarms that pause only the offending tenant. |
| **WhatsApp number ban from spam** | Hard architectural block on bulk/broadcast WhatsApp or SMS messages; strict 1-to-1 inbound reply and booking reminder limits; instant `STOP` opt-out enforcement. |
| **Runaway AI/voice costs** | Mybizz CS caps AI/voice at £16.80/mo per client with a hard Groq org spend ceiling. Front Desk Assistant uses customer-owned OpenRouter BYOK keys with spend ceilings and automatic fallback to Draft-Only mode. |
| **Client website used for phishing/abuse** | Acceptable Use Policy, mandatory non-removable `Report abuse: abuse@mybizz.live` footer link, and one-click container suspension in App 5. |
| **Hetzner server or region outage** | Primary PostgreSQL node streams continuously to a live hot-standby node; nightly immutable backups sit in each client's Cloudflare R2 bucket. App 5's **Rebuild** procedure restores all containers onto fresh Hetzner nodes in an alternate EU location (Helsinki/Falkenstein/Nuremberg) with <= 24h RPO. |
| **Leaked infrastructure API keys** | Scoped Hetzner API tokens (read/resize vs. create/delete), encrypted Vault storage with mandatory per-session TOTP, and FIDO2 hardware security keys enforced across all vendor accounts. |
| **Ransomware or malicious backup deletion** | Cloudflare R2 Object Lock enabled on client backup buckets (7 days for daily backups, 28 days for weekly backups) so no key—including Mybizz's—can delete or overwrite locked backups. |
| **DDoS or bot attacks on client sites** | Every client domain is proxied through Cloudflare with WAF, DDoS mitigation, and bot protection enabled. |
| **Regulatory / Cyber Incident (UK/EU)** | Phased compliance: South African sole-proprietor tax/SARB compliance during Stage 1, followed by UK Ltd incorporation, ICO registration, Cyber Essentials certification, and combined £1m Professional Indemnity / £500k Cyber Liability / £1m Public Liability insurance before Mybizz CS scale-up. |

---

## 4. Phased Implementation Checklist

### Phase A: Stage 1 — South African Sole Proprietor & Front Desk Assistant Launch (Jan–Mar 2027)
1. **Hetzner Base Server:** Provision Hetzner Cloud VPS (Ubuntu 24.04, 4 GB+ RAM, EU region) with firewall rules, automated backups, Caddy TLS, PostgreSQL, Redis, Evolution API, and Anvil App Server.
2. **Cloudflare R2 Integration:** Configure programmatic per-tenant R2 bucket creation and automated 30-day webhook archival / daily backup export.
3. **Security Baseline:** Enable FIDO2 hardware security keys on Hetzner, Cloudflare, GitHub, OpenRouter, and Paddle; set up `abuse@mybizz.live` forwarding.
4. **Paddle Sole-Proprietor Onboarding:** Publish `Front-Desk-Assistant-Legal-Policies.md` on the landing page and complete Paddle Individual/Sole Proprietor KYC verification.
5. **Channel Safeguards:** Verify Evolution API burst debouncing (10–15s), SMSGate heartbeat checks, and `STOP` opt-out handling before onboarding Founding Pass clients.

### Phase B: Stage 2 — UK Incorporation & Mybizz CS Full Platform Readiness (Q1–Q2 2027)
6. **UK Company Formation:** Purchase UK registered office + director service address, complete GOV.UK One Login identity verification, and incorporate **Mybizz-Live Ltd** at Companies House.
7. **Banking, Tax & Accounting:** Open **Wise Business** account, register with HMRC for Corporation Tax (and UK VAT once appropriate), pay ICO data protection fee, and connect FreeAgent + Wise bank feed.
8. **Hetzner HA Database Cluster:** Provision primary + hot-standby PostgreSQL cluster on Hetzner Cloud with TLS, connection pooling, automated failover testing, and monthly R2 restore drills.
9. **Security & Insurance:** Complete NCSC Cyber Essentials certification (including cyber cover) and bind combined £1m PI / £500k Cyber / £1m Public Liability policy prior to scaling Mybizz CS.
10. **App 5 Automation & Observability:** Verify App 5's automated container resizing, fair-use enforcement, daily backup checks, FreeAgent tax deadline reminders, and 1-minute external uptime checks.
11. **Paddle UK Ltd Migration:** Create the Mybizz-Live Ltd Paddle seller profile with fixed local currency tiers (£119/mo, £1,190/yr, £119 assisted setup) and annual referral credit logic (capped at 5 months per renewal).
