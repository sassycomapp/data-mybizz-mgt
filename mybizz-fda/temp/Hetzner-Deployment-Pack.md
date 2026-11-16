---
title: "Hetzner-Deployment-Pack"
doc-id: "mb-cef827b0"
updated: "2026-11-15"
---
# Hetzner Cloud Deployment Pack — Front Desk Assistant

This guide provides the complete setup for self-hosting your **Anvil App Server** (Material 3 Front Desk Assistant), **Evolution API** (multi-tenant WhatsApp), **PostgreSQL 16**, **Redis 7**, **Caddy** (automated SSL/HTTPS), and **Cloudflare R2** storage on a **Hetzner Cloud VPS**.

---

## 1. Provision Your Hetzner Cloud Server

1. Log into the **Hetzner Cloud Console** and create a new project (`frontdesk-prod`).
2. Click **Add Server**:
   - **Location:** Falkenstein (`fsn1`) or Nuremberg (`nbg1`) — EU/EEA, fully UK GDPR adequate.
   - **Image:** Ubuntu 24.04 LTS.
   - **Type:** Shared vCPU → **CX33** (4 vCPU, 8 GB RAM, 80 GB NVMe — ~€8.49/mo).
   - **Networking:** Public IPv4 + IPv6.
   - **SSH Key:** Add your public SSH key (disable password SSH login).
   - **Backups:** Enable automated Hetzner server backups (+20%).
3. In **Cloudflare DNS** for your domain (`yourdomain.com`), create two `A` records pointing to your Hetzner IPv4 address:
   - `app.yourdomain.com` → `<HETZNER_IP>` (**DNS Only / Grey Cloud** initially so Caddy obtains SSL certificates cleanly).
   - `wa.yourdomain.com` → `<HETZNER_IP>` (**DNS Only / Grey Cloud**).

---

## 2. Server Initialization & Firewall Setup (Ubuntu 24.04)

SSH into your new server (`ssh root@<HETZNER_IP>`) and run the following commands to install Docker, Docker Compose, and configure the UFW firewall:

```bash
apt update && apt upgrade -y
apt install -y curl git ufw ca-certificates gnupg

# Configure Firewall (Allow SSH, HTTP, HTTPS only)
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw --force enable

# Install Docker Engine & Docker Compose plugin
curl -fsSL https://get.docker.com | sh
systemctl enable --now docker

# Create application directory structure
mkdir -p /opt/frontdesk/{anvil_app,anvil_data,caddy_config}
cd /opt/frontdesk
```

---

## 3. Clone Your Anvil Application

Export/clone your Material 3 Anvil application into `/opt/frontdesk/anvil_app`:

```bash
cd /opt/frontdesk
git clone https://<YOUR_ANVIL_GIT_TOKEN>@anvil.works/git/<YOUR_APP_ID>.git anvil_app
```

*(Note: Ensure your `anvil_app` repository includes the `m3-custom-theme` dependency cloned into `/opt/frontdesk/anvil_deps/m3-custom-theme` if using local dependency resolution.)*

---

## 4. Configuration Files (`docker-compose.yml`, `Caddyfile`, `.env`)

Save the accompanying files (`docker-compose.yml`, `Caddyfile`, and `.env`) inside `/opt/frontdesk/`:

```bash
cd /opt/frontdesk
cp .env.example .env
nano .env   # Fill in your strong passwords, API keys, and Cloudflare R2 credentials
```

### Generate Strong Secrets

Run this command on the server to generate secure random secrets for `DB_PASSWORD`, `EVOLUTION_API_KEY`, and `ANVIL_ENCRYPTION_KEY`:

```bash
openssl rand -hex 24
```

---

## 5. Launch the Stack

Start all containers in detached mode:

```bash
cd /opt/frontdesk
docker compose up -d
```

Verify that all five services (`caddy`, `anvil-app`, `evolution-api`, `postgres`, `redis`) are healthy:

```bash
docker compose ps
docker compose logs -f anvil-app
```

---

## 6. Wiring Webhooks to Anvil Endpoints

Once `https://app.yourdomain.com` and `https://wa.yourdomain.com` are live:

1. **WhatsApp Webhooks (Evolution API):** Configured automatically in `docker-compose.yml` via `WEBHOOK_GLOBAL_URL=http://anvil-app:3030/_/api/webhooks/whatsapp`. All incoming customer WhatsApp messages are routed straight to your Anvil server endpoint with the `instance` field identifying the subscribing client (`tenant_id`).
2. **SMS Webhooks (SMSGate):** When a client enters their SMSGate Cloud login and password in your onboarding wizard, your Anvil server calls `register_webhook()` to point their Android phone to `https://app.yourdomain.com/_/api/webhooks/sms/{tenant_id}`.
3. **Cloudflare R2 Archival:** Place `r2_manager.py` inside your Anvil server modules (`server_code/r2_manager.py`) and configure an Anvil Scheduled Task (running nightly at 02:00 UTC) to export workspace backups and archive webhook payloads older than the tenant's retention threshold to their dedicated R2 bucket.
