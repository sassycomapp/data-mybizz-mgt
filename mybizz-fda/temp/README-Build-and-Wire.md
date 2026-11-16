---
title: "README-Build-and-Wire"
doc-id: "mb-6f3008c8"
updated: "2026-11-15"
---
# Front Desk Assistant — Build & Wire Assembly Guide

This checklist walks you through assembling all **13 Python modules** and **Hetzner Cloud infrastructure files** into a working, production-ready Anvil application built on **`m3-custom-theme` (`v2.0.0`)**.

---

## 1. Repository Folder Layout

Organise your cloned Anvil Git repository using the exact structure below so client forms and server modules resolve cleanly:

```text
front-desk-assistant/
├── anvil.yaml
├── client_code/
│   ├── startup.py                     # Theme initialization (from ActionQueueForm.py header)
│   ├── ActionQueueForm/
│   │   └── __init__.py                # Main shell (Expressive NavigationRail) + Action Queue
│   ├── OnboardingWizardForm/
│   │   └── __init__.py                # 10-step setup wizard (WhatsApp QR, SMSGate, R2, BYOK)
│   ├── InboxAndLeadForm/
│   │   └── __init__.py                # Adaptive PaneLayout unified inbox & lead record
│   ├── CalendarSettingsForm/
│   │   └── __init__.py                # Google Calendar connection, working hours, booking link
│   ├── FollowUpsForm/
│   │   └── __init__.py                # 1-to-1 only no-response follow-up configuration
│   └── DashboardForm/
│       └── __init__.py                # Owner outcome metrics, pipeline summary, BYOK spend
└── server_code/
    ├── r2_manager.py                  # Cloudflare R2 bucket creation, encryption & archival
    ├── messaging_gateway.py           # Evolution API, SMSGate, 12s Redis debounce, OpenRouter BYOK
    ├── front_desk_pipeline.py         # AI classification/drafting, Google Calendar slots, approval queue
    ├── scheduled_jobs.py              # 15m channel heartbeat, hourly 1-to-1 follow-ups, nightly R2 backup
    ├── inbound_adapters.py            # Webform webhook, calendar booking webhook, email inbox poller
    ├── onboarding_and_paddle.py       # Workspace setup, CSV import, test lead, Paddle webhooks
    └── ui_backend_callables.py        # @anvil.server.callable endpoints powering all 7 client screens
```

*(Note: On your Hetzner Cloud VPS under `/opt/frontdesk/`, place `docker-compose.yml`, `Caddyfile`, and `.env` alongside the cloned `anvil_app/` folder.)*

---

## 2. Step-by-Step Anvil Editor Configuration

### Step A — Theme Dependency (`m3-custom-theme`)
1. Open your app in the Anvil Editor (or edit `anvil.yaml` locally).
2. Go to **Settings > Dependencies**.
3. Remove Anvil's built-in **Material 3 Theme** if present (never run both together).
4. Add dependency **`m3-custom-theme`** (App ID: `UGGJBAZUZ74XZ7VU`, version **`v2.0.0`**).
5. Ensure `startup.py` is set as your **Startup Module** so `m3x_theming.apply_saved()` and `m3x_theming.set_mode("system")` execute before `ActionQueueForm` opens.

### Step B — Data Tables Setup
Create the **7 Data Tables** specified in `Front-Desk-Data-Schema.md` with server-side permissions set to **No client access** (all reads/writes go through `@anvil.server.callable` functions):
1. `workspaces`
2. `channel_connections`
3. `contacts`
4. `leads`
5. `messages`
6. `action_queue`
7. `audit_events`

### Step C — Anvil App Secrets
Open **Settings > Secrets** and add the following keys (matching your `.env` file on Hetzner):
* `FERNET_MASTER_KEY` — 32-byte URL-safe base64 key (`python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"`)
* `EVOLUTION_URL` — `http://evolution-api:8080` (internal Docker network URL)
* `EVOLUTION_API_KEY` — Your strong random Evolution API master key
* `REDIS_URL` — `redis://redis:6379/0`
* `R2_ACCOUNT_ID` — Your Cloudflare Account ID
* `R2_ACCESS_KEY_ID` — Your Cloudflare R2 S3 API Access Key ID
* `R2_SECRET_ACCESS_KEY` — Your Cloudflare R2 S3 API Secret Access Key
* `PADDLE_WEBHOOK_SECRET` — Your Paddle Billing notification secret key

### Step D — Scheduled Background Tasks
Open **Settings > Scheduled Tasks** and register these three server functions from `scheduled_jobs.py`:
1. `job_check_channel_heartbeats` — Every **15 minutes**
2. `job_run_no_response_followups` — Every **1 hour**
3. `job_nightly_r2_backup_and_archive` — Daily at **02:00 UTC**

---

## 3. Hetzner Cloud Deployment Sequence

1. **Provision Server:** Spin up a **Hetzner Cloud CX33** (4 vCPU, 8 GB RAM, Ubuntu 24.04) in Falkenstein or Nuremberg with automated backups enabled.
2. **Firewall:** Allow inbound ports `22` (SSH), `80` (HTTP), and `443` (HTTPS) only. Keep PostgreSQL (`5432`), Redis (`6379`), Anvil (`3030`), and Evolution API (`8080`) bound strictly to internal Docker networking.
3. **DNS Records:** Point `app.yourdomain.com` and `wa.yourdomain.com` to your Hetzner IPv4 address (set Cloudflare proxy to **DNS Only / Grey Cloud** during initial startup so Caddy issues Let's Encrypt SSL certificates cleanly).
4. **Launch Stack:**
   ```bash
   cd /opt/frontdesk
   cp .env.example .env   # Fill in your generated secrets
   docker compose up -d
   ```

---

## 4. End-to-End Smoke Test Checklist

Run through these 6 checks before inviting your first January 2027 Founding Pass user:

1. **SSL & Login:** Visit `https://app.yourdomain.com` and verify the Material 3 `Professional Blue` UI loads cleanly in both light and dark modes.
2. **Onboarding & R2 Bucket:** Walk through `OnboardingWizardForm`, generate a workspace, and confirm bucket `fda-tenant-{workspace_id}` appears in your Cloudflare R2 dashboard.
3. **WhatsApp QR Pairing:** Click **Generate QR Code** on Step 6, scan with WhatsApp Business on your test Android phone, and verify the top-bar chip turns green (`WhatsApp: Connected`).
4. **SMSGate Linking:** Enter your test Android phone's SMSGate Cloud credentials on Step 6 and verify webhook registration succeeds (`SMS: Connected`).
5. **Inbound Test Lead:** Send a WhatsApp message or SMS to your test phone (or click **Run Test Lead Simulation** on Step 10). Confirm a draft appears in **Action Queue** within 15 seconds (after the 12-second burst debounce).
6. **One-Click Approval & Opt-Out:** Click **Approve & Send** on the queued draft and verify the reply arrives on your phone. Reply `STOP` from your test phone and verify the contact's `do_not_contact` flag flips to `True` immediately.
