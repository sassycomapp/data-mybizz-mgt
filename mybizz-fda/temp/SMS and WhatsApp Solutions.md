---
title: "SMS and WhatsApp Solutions"
doc-id: "mb-cbd028d5"
updated: "2026-11-15"
---
# SMS and WhatsApp Solutions

for Front Desk Assistant

Here is the complete, end-to-end blueprint for your **multi-tenant AI Front Desk Assistant SaaS**, combining **WhatsApp (via Evolution API)** and **SMS (via SMSGate)** on a low-cost **Hetzner Cloud VPS**.

---

1. System Architecture Overview
- **Hetzner Cloud VPS (Ubuntu 24.04, 4 GB RAM — ~€4.50–€7/mo):** Hosts your entire backend stack 24/7 inside Docker Compose so no connections ever drop.
- **WhatsApp Channel (Evolution API):** Your subscribing businesses log into your SaaS dashboard on their office computer, click *"Connect WhatsApp"*, and scan a QR code using WhatsApp Business on their company cell phone. Evolution API holds unlimited client WhatsApp sessions simultaneously at **$0 software cost**.
- **SMS Channel (SMSGate):** For businesses that also want traditional SMS handling, they install the free **SMSGate** Android app on their company cell phone (in Cloud Server mode) and link their credentials in your SaaS dashboard.
- **Unified Python AI Agent (FastAPI):** Both Evolution API and SMSGate send incoming customer messages as JSON webhooks to your Python backend. Your backend identifies which subscribing business (`tenant_id`) received the message, runs your AI booking assistant, and replies via the matching channel.

---

2. Server Setup & Docker Compose Stack (Hetzner)

Provision a **Hetzner Cloud CX22 or CPX21 (4 GB RAM, Ubuntu 24.04)** server, install Docker & Docker Compose, and create a project folder (`/opt/frontdesk-saas`) with the following `docker-compose.yml`.

This stack runs **Caddy** (automatic free SSL/HTTPS), **Evolution API** (WhatsApp), **PostgreSQL** (database), **Redis** (session cache), and your **Python FastAPI Agent**:

yaml

```
services:  caddy:    image: caddy:2-alpine    restart: unless-stopped    ports:      - "80:80"
      - "443:443"
    volumes:      - ./Caddyfile:/etc/caddy/Caddyfile      - caddy_data:/data  postgres:    image: postgres:16-alpine    restart: unless-stopped    environment:      POSTGRES_USER: saas_admin      POSTGRES_PASSWORD: ${DB_PASSWORD}      POSTGRES_DB: frontdesk_db    volumes:      - postgres_data:/var/lib/postgresql/data  redis:    image: redis:7-alpine    restart: unless-stopped    command: redis-server --appendonly yes    volumes:      - redis_data:/data  evolution-api:    image: atendai/evolution-api:latest    restart: unless-stopped    depends_on:      - postgres      - redis    environment:      SERVER_URL: https://wa.${DOMAIN}      AUTHENTICATION_API_KEY: ${EVOLUTION_API_KEY}      DATABASE_ENABLED: "true"
      DATABASE_PROVIDER: postgresql      DATABASE_CONNECTION_URI: postgresql://saas_admin:${DB_PASSWORD}@postgres:5432/frontdesk_db?schema=evolution      CACHE_REDIS_ENABLED: "true"
      CACHE_REDIS_URI: redis://redis:6379/1      WEBHOOK_GLOBAL_ENABLED: "true"
      WEBHOOK_GLOBAL_URL: http://python-agent:8000/webhooks/whatsapp      WEBHOOK_GLOBAL_WEBHOOK_BY_EVENTS: "false"
    volumes:      - evolution_instances:/evolution/instances  python-agent:    build: ./agent_app    restart: unless-stopped    depends_on:      - postgres      - evolution-api    environment:      EVOLUTION_URL: http://evolution-api:8080
      EVOLUTION_API_KEY: ${EVOLUTION_API_KEY}      PUBLIC_WEBHOOK_BASE: https://api.${DOMAIN}      DATABASE_URL: postgresql://saas_admin:${DB_PASSWORD}@postgres:5432/frontdesk_db

volumes:  caddy_data:  postgres_data:  redis_data:  evolution_instances:
```

Use code with caution.

**Matching `Caddyfile` (for automatic HTTPS):**

caddyfile

```
://yourdomain.com {    reverse_proxy python-agent:8000}://yourdomain.com {    reverse_proxy evolution-api:8080}
```

Use code with caution.

---

3. Unified Python Backend (Onboarding + Webhooks + Replies)

Your Python FastAPI app handles **client onboarding** (generating WhatsApp QR codes or registering SMSGate phones) and **routing incoming messages** to your AI agent.

*(Required packages: `fastapi`, `uvicorn`, `httpx`, `android-sms-gateway`)*

python

```
import os
import httpx
from fastapi import FastAPI, Request, BackgroundTasks
from android_sms_gateway import client as sms_client, domain as sms_domain

app = FastAPI()

EVOLUTION_URL = os.getenv("EVOLUTION_URL", "http://evolution-api:8080")
EVOLUTION_API_KEY = os.getenv("EVOLUTION_API_KEY")
PUBLIC_WEBHOOK_BASE = os.getenv("PUBLIC_WEBHOOK_BASE")

# --- 1. CLIENT ONBOARDING ENDPOINTS (Called by your SaaS Frontend) ---

@app.post("/tenants/{tenant_id}/whatsapp/connect")
async def connect_client_whatsapp(tenant_id: str):    """Creates a WhatsApp session for a subscribing company and returns the QR code."""
    headers = {"apikey": EVOLUTION_API_KEY, "Content-Type": "application/json"}    async with httpx.AsyncClient() as http:        res = await http.post(            f"{EVOLUTION_URL}/instance/create",            headers=headers,            json={                "instanceName": tenant_id,                "qrcode": True,                "integration": "WHATSAPP-BAILEYS",            },        )        return res.json()  # Contains base64 QR code image to render in your SaaS UI


@app.post("/tenants/{tenant_id}/sms/connect")
async def connect_client_smsgate(tenant_id: str, sms_login: str, sms_password: str):    """Registers your SaaS webhook on the client's SMSGate Android app (Cloud Mode)."""
    # Save sms_login & sms_password against tenant_id in your Postgres DB here
    webhook_url = f"{PUBLIC_WEBHOOK_BASE}/webhooks/sms/{tenant_id}"
    async with sms_client.AsyncAPIClient(sms_login, sms_password) as c:        await c.register_webhook(            sms_domain.Webhook(id=f"saas_{tenant_id}", url=webhook_url, event="sms:received")        )    return {"status": "sms_connected", "tenant_id": tenant_id}


# --- 2. UNIFIED AI AGENT HANDLER ---

async def process_and_reply(tenant_id: str, channel: str, sender: str, text: str):    # 1. Load company-specific booking rules & prompt using tenant_id from Postgres
    # 2. Run your AI front desk assistant
    ai_reply = await run_your_ai_agent(tenant_id=tenant_id, customer=sender, message=text)    # 3. Reply over the exact channel the customer used
    if channel == "whatsapp":        headers = {"apikey": EVOLUTION_API_KEY, "Content-Type": "application/json"}        async with httpx.AsyncClient() as http:            await http.post(                f"{EVOLUTION_URL}/message/sendText/{tenant_id}",                headers=headers,                json={"number": sender, "text": ai_reply},            )    elif channel == "sms":        # Fetch tenant's saved sms_login & sms_password from Postgres
        sms_login, sms_password = get_tenant_sms_creds(tenant_id)        msg = sms_domain.Message(            phone_numbers=[sender],            text_message=sms_domain.TextMessage(text=ai_reply),        )        async with sms_client.AsyncAPIClient(sms_login, sms_password) as c:            await c.send(msg)


# --- 3. INCOMING WEBHOOK RECEIVERS ---

@app.post("/webhooks/whatsapp")
async def whatsapp_webhook(request: Request, background_tasks: BackgroundTasks):    data = await request.json()    if data.get("event") == "messages.upsert":        msg_data = data.get("data", {})        key = msg_data.get("key", {})        if not key.get("fromMe"):            tenant_id = data.get("instance")            sender = key.get("remoteJid")            text = (                msg_data.get("message", {}).get("conversation")                or msg_data.get("message", {}).get("extendedTextMessage", {}).get("text")            )            if text:                background_tasks.add_task(process_and_reply, tenant_id, "whatsapp", sender, text)    return {"status": "ok"}@app.post("/webhooks/sms/{tenant_id}")
async def sms_webhook(tenant_id: str, request: Request, background_tasks: BackgroundTasks):    data = await request.json()    if data.get("event") == "sms:received":        payload = data.get("payload", {})        sender = payload.get("phoneNumber")        text = payload.get("message")        if text:            background_tasks.add_task(process_and_reply, tenant_id, "sms", sender, text)    return {"status": "ok"}
```

Use code with caution.

---

4. Client Onboarding Checklist (For Each Subscribing Business)

Give each subscribing company this 2-minute setup guide inside your SaaS dashboard:

1. **Phone Hardware:** Use a dedicated or front-desk Android phone with an active, RICA-registered SIM card and a standard SMS bundle + Wi-Fi/mobile data.
2. **Connect WhatsApp:**
   - Install **WhatsApp Business** on the phone.
   - On their office computer, log into your SaaS dashboard and click **Connect WhatsApp**.
   - Scan the displayed QR code via **WhatsApp Business > Linked Devices > Link a Device**.
3. **Connect SMS (Optional):**
   - Install **SMSGate** on the same Android phone and enable **Cloud Server** mode.
   - Enter the displayed SMSGate username and password into your SaaS dashboard.
   - Set **Settings > Apps > SMSGate > Battery** to **Unrestricted** and keep the phone plugged into power.

---

5. Total Monthly Cost Breakdown
- **Evolution API Software:** $0 (Open Source)
- **SMSGate Software:** $0 (Open Source)
- **Caddy SSL & Docker:** $0 (Open Source)
- **Hetzner Cloud VPS (4 GB RAM):** ~€4.50–€7/month (~R90–R140/month flat, supporting dozens of client companies)
- **Client Carrier Costs:** Paid directly by each subscribing business via their existing SIM card plan.

If you'd like to take the next step, I can provide the **`Dockerfile`** for the `python-agent` service and the exact **bash commands** to initialize the Hetzner Ubuntu server from scratch. Would that be helpful?
