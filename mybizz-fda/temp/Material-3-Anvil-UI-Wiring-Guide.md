---
title: "Material-3-Anvil-UI-Wiring-Guide"
doc-id: "mb-dc2bbe90"
updated: "2026-11-15"
---
# Front Desk Assistant — Material 3 Anvil Client Forms & UI Wiring Guide

**Target Theme:** `m3-custom-theme` (`v2.0.0` / dependency ID `UGGJBAZUZ74XZ7VU`)  
**Package Import:** `import m3.components as m3` (replaces default Anvil Material 3 Theme; never use both together)  
**Default Palette & Mode:** `professional_blue` (`light` baseline; `system` dark-mode watch via `m3x_theming`)

---

## 1. App Initialization & Theme Setup

Configure your startup module (`client_code/startup.py`) so every screen inherits your M3 Expressive tokens, adaptive width classes, and workspace palette cleanly without flashing default colours:

```python
import anvil
from m3._utils import m3x_theming, m3x_motion, m3x_adaptive

def init_app_theme(workspace_palette: str = "professional_blue"):
    # 1. Apply browser-cached theme immediately to prevent colour flash
    m3x_theming.apply_saved()
    # 2. Enforce workspace palette & follow device light/dark mode
    m3x_theming.set_palette(workspace_palette)
    m3x_theming.set_mode("system")
    # 3. Use M3 Expressive menus and calm standard motion for business ops
    m3x_theming.set_menu_style("standard")
    m3x_motion.set_scheme("standard")
```

### Design & Token Rules (`m3-custom-theme`)
* **Zero Hardcoded Colours:** Reference `%color:Primary%` in the Anvil Designer and `var(--m3x-*)` / `var(--anvil-m3-*)` in any custom Role CSS.
* **Status Badges:** Never communicate status by colour alone. Always pair `Chip` or `Badge` indicators with explicit status text (`Approved`, `Pending`, `Offline`, `Urgent`).
* **Responsive Breakpoints (`m3x_adaptive`):** Design every screen across `compact` (`< 600px`), `medium` (`600–839px`), and `expanded` (`840px+`) using `PaneLayout` and `NavigationRailLayout` rather than fixed pixel widths.

---

## 2. Main Application Shell (`MainLayout`)

Use `NavigationRailLayout` (`rail_style="expressive"`, `rail_adaptive=True`) as the single shell for all authenticated screens. On `compact` screens (`< 600px`), pair or swap to `NavigationBar` at the bottom for one-thumb mobile triage.

### Shell Anatomy
* **`TopAppBar` (Small):**
  * **Leading / Title:** `"Front Desk Assistant"` + active workspace name.
  * **Trailing Channel Health Chips (`m3.Chip`):** Three live status pills showing **Email**, **WhatsApp**, and **SMS** (`Connected` vs. `Offline` with `Badge` alert dot if disconnected).
  * **Trailing `AvatarMenu`:** Profile, Billing & Subscription (`£45/mo` or Founding Pass status), and Sign Out.
* **`NavigationRailLayout` Destinations (7 Core Screens):**
  1. **Action Queue** (Default landing screen — `"Here are the things that need you today"`) — with live `Badge` count of pending approvals & alerts.
  2. **Inbox / Leads** (Unified multi-channel lead inbox & threading)
  3. **Approval Queue** (Dedicated one-click review of AI-drafted replies)
  4. **Calendar & Booking** (Google Calendar availability, booking link & rules)
  5. **Follow-ups** (1-to-1 no-response & reminder sequence configuration)
  6. **Dashboard** (Response time, leads captured, bookings & OpenRouter BYOK spend)
  7. **Settings & Channels** (WhatsApp QR pairing, SMSGate setup, Cloudflare R2 retention & BYOK key)

---

## 3. Screen-by-Screen Component & Server Wiring Map

### Screen 1: Onboarding Wizard (`OnboardingWizardForm`)
* **Purpose:** Get a new user from signup to a live, tested assistant in under 30 minutes (`onboarding_and_paddle.py`).
* **M3 Components Used:**
  * `TopAppBar` with `LinearProgressIndicator(wavy=True)` showing step completion (1 to 10).
  * `Card` (`elevated`) housing one focused step at a time:
    * **Steps 1–4 (Business Profile, Tone, Services, Lead Rules):** `TextBox`, `TextArea`, `DropdownMenu` (timezone, tone preset), and `Chip` (input chips for qualification rules).
    * **Step 5 (Google Calendar):** `Button(text="Connect Google Calendar", shape="square")` + availability `TimePicker` and `Slider` (buffer minutes).
    * **Step 6 (Connect Channels — Email, WhatsApp, SMS):**
      * `Tabs` (`primary`) switching between **Email (Required)**, **WhatsApp (Optional)**, and **SMS (Optional)**.
      * **WhatsApp Tab:** `Button(text="Generate WhatsApp QR")` calls `create_whatsapp_instance(workspace_id)` and displays the returned `base64` QR image inside a `Card`, with a `LoadingIndicator` polling `check_whatsapp_status(workspace_id)` until `connected`.
      * **SMS Tab:** `TextBox` for SMSGate Cloud username & password (`hide_text=True`) + `Button(text="Link Android Phone")` calling `register_smsgate_device(workspace_id, login, password)`.
    * **Step 7 (Cloudflare R2 Storage & Retention):** Displays provisioned bucket name (`fda-tenant-{workspace_id}`) from `provision_workspace_r2_bucket()` + `ButtonGroup` (single choice: `30 Days`, `60 Days`, `90 Days` retention before archival).
    * **Step 8 (Anti-Spam Policy & OpenRouter BYOK):**
      * `Checkbox` confirming **strict 1-to-1 usage (no bulk SMS/WhatsApp blasts)** and **no payment/financial data collection**.
      * `TextBox` (`hide_text=True`) for OpenRouter API key + `ButtonGroup` (`Fast`, `Balanced`, `Premium`) + `Button(text="Test Connection")` calling `save_and_test_openrouter_key()`.
    * **Steps 9–10 (Follow-up Rules & CSV Contact Import):** `Switch` toggles, `FileLoader` (CSV upload calling `import_contacts_csv()`), and `Button(text="Send Test Enquiry")` calling `simulate_test_lead()`.
  * `Snackbar` feedback after every step save (`"Settings saved"`, `"WhatsApp connected"`).

---

### Screen 2: Action Queue (`ActionQueueForm` — Primary Home Screen)
* **Purpose:** Focused daily triage queue showing only items requiring human attention.
* **M3 Components Used:**
  * `TopAppBar` + `Chip` filter row (`All`, `Approvals`, `Urgent Leads`, `Channel Alerts`).
  * `Card` list (`ListItem` rows inside `Card` containers) sorted by priority:
    * **Draft Reply Awaiting Approval:** Shows contact name, channel `Chip` (`WhatsApp`, `SMS`, `Email`), incoming snippet, AI-proposed reply preview, and inline `SplitButton` (`Approve & Send` primary action + `Edit Draft` / `Reject` menu items) wired to `approve_and_send_draft()`.
    * **Channel Offline Alert:** Triggered by `job_check_channel_heartbeats()` if WhatsApp or SMSGate disconnects; action `Button` opens Settings → Channels.
    * **Urgent / High-Value Enquiry:** Highlighted with `Badge` (`Urgent`) and `Button(text="Open Lead")` opening `LeadRecordForm`.
  * **Empty State:** Calm `Card` with check icon, `"All caught up — zero items waiting for you"`, and `Button(text="Simulate Test Enquiry")`.

---

### Screen 3: Unified Inbox & Leads (`InboxLeadsForm`)
* **Purpose:** Browse and filter all multi-channel enquiries and lead threads.
* **M3 Components Used:**
  * `SearchBar` (search by contact name, email, phone, or keyword) + `Chip` filter bar (`New Enquiry`, `Responded`, `Meeting Booked`, `Proposal`, `Won`, `Stalled`).
  * `PaneLayout` (List-Detail adaptive layout — single pane on `compact`, side-by-side list + thread preview on `expanded`):
    * **Left Pane:** `ListItem` rows with `Avatar` (initials), headline (contact name), supporting text (latest message snippet), trailing timestamp, and channel `Chip` (`Email`, `WhatsApp`, `SMS`, `Webform`).
    * **Right Pane:** Embeds `LeadRecordForm` directly so clicking any lead shows full history without a full-page reload.
  * `FloatingActionButton(icon="add", text="New Contact")` for manual lead entry via a `Dialog`.

---

### Screen 4: Lead Record & Conversation Thread (`LeadRecordForm`)
* **Purpose:** Complete history, AI extraction summary, and reply composer for one prospect.
* **M3 Components Used:**
  * **Header `Card`:** Contact name, company, email/phone, pipeline stage `DropdownMenu` (`New enquiry → Responded → Meeting booked → Proposal/quote → Won → Lost`), and `Switch` (`Do Not Contact` — immediately halts all automated sequences).
  * **AI Extraction Summary (`Card` tonal):** Structured `Chip` tags for `Service Interest`, `Urgency`, `Timeline`, and `Source` (read-only audit of what AI extracted).
  * **Message Thread (`ListItem` timeline):** Chronological bubbles showing inbound vs. outbound messages, channel icon, delivery status (`Delivered`, `Sent`, `Failed`), and immutable audit events.
  * **Docked `Toolbar` Composer at Bottom:** `TextArea` for manual reply or editing an AI-drafted reply + `Button(text="Send Reply")` calling `send_outbound_message()`.

---

### Screen 5: Approval Queue (`ApprovalQueueForm`)
* **Purpose:** Dedicated side-by-side review screen for owners operating in **Approve-Before-Send** mode (default for all new accounts).
* **M3 Components Used:**
  * `PaneLayout` comparing **Original Customer Enquiry** (left `Card`) against **AI-Proposed Response & Calendar Slot** (right `Card`).
  * Editable `TextArea` pre-filled with the AI draft so the owner can tweak wording before sending.
  * Action `Toolbar`:
    * `Button(text="Approve & Send", size="medium")` → calls `approve_and_send_draft(action_id, edited_text)`.
    * `Button(text="Reject", appearance="outlined")` → opens a `Dialog` asking for an optional rejection reason (logged to `audit_events` without overwriting original data).

---

### Screen 6: Calendar & Booking Settings (`CalendarBookingForm`)
* **Purpose:** Deterministic availability rules and booking link management.
* **M3 Components Used:**
  * `Card` (Google Calendar connection status + `Button(text="Reconnect Calendar")`).
  * `ButtonGroup` (multiple choice for active working days `Mon–Sun`) + `TimePicker` for daily start/end hours.
  * `DropdownMenu` for default meeting duration (`15m`, `30m`, `45m`, `60m`) and `Slider` for buffer time between meetings (`0–30 mins`).
  * Read-only `TextBox` displaying the client's public booking link + `IconButton(icon="content_copy")` triggering `Snackbar("Booking link copied")`.

---

### Screen 7: Follow-Ups & Dashboard (`FollowUpsForm` & `DashboardForm`)
* **Follow-Ups Screen (`FollowUpsForm`):**
  * Three clean `Card` blocks matching your narrow workflow templates: **1. New Enquiry Auto-Acknowledgement**, **2. No-Response 1-to-1 Follow-Up**, and **3. Pre-Meeting Reminder**.
  * Each card uses a `Switch` (Active/Paused), `DropdownMenu` (wait delay: `4h`, `24h`, `48h`), `Slider` (max follow-up attempts: `1` to `3`), and editable `TextArea` template.
  * **Compliance Banner (`Card` tonal):** Explicitly notes that bulk broadcasts are disabled at the platform level and `"STOP"` replies automatically opt contacts out.
* **Dashboard Screen (`DashboardForm`):**
  * Top KPI `Card` grid (`metric-card` role): **Enquiries Answered < 5 mins (%)**, **Leads Captured**, **Meetings Booked**, **Follow-Ups Completed**, and **OpenRouter BYOK Monthly Spend vs. Ceiling** (`LinearProgressIndicator`).
  * Channel breakdown `Card` (Email vs. WhatsApp vs. SMS lead counts) + **Cloudflare R2 Backup Status** `ListItem` showing last nightly snapshot timestamp and archived record count.

---

## 4. Client-to-Server Callable Wiring Reference

| UI Screen | User Action | `@anvil.server.callable` Function | Module |
| :--- | :--- | :--- | :--- |
| **Onboarding Step 6 (WA)** | Click *Generate QR Code* | `create_whatsapp_instance(workspace_id)` | `messaging_gateway.py` |
| **Onboarding Step 6 (WA)** | Poll connection status | `check_whatsapp_status(workspace_id)` | `messaging_gateway.py` |
| **Onboarding Step 6 (SMS)** | Save SMSGate credentials | `register_smsgate_device(workspace_id, login, password)` | `messaging_gateway.py` |
| **Onboarding Step 7 (R2)** | Provision tenant bucket | `provision_workspace_r2_bucket(workspace_id)` | `r2_manager.py` |
| **Onboarding Step 8 (AI)** | Save & test OpenRouter key | `save_and_test_openrouter_key(workspace_id, api_key, tier)` | `onboarding_and_paddle.py` |
| **Onboarding Step 10** | Import contacts CSV | `import_contacts_csv(workspace_id, file_media, consent_ok)` | `onboarding_and_paddle.py` |
| **Onboarding Step 10** | Run test enquiry | `simulate_test_lead(workspace_id)` | `onboarding_and_paddle.py` |
| **Action / Approval Queue** | Approve & send AI draft | `approve_and_send_draft(workspace_id, action_id, final_text)` | `front_desk_pipeline.py` |
| **Lead Record** | Send manual reply | `send_outbound_message(workspace_id, lead_id, channel, text)` | `messaging_gateway.py` |
| **Dashboard / Settings** | View R2 backup archives | `list_workspace_r2_archives(workspace_id)` | `r2_manager.py` |
