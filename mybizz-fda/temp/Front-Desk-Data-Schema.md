---
title: "Front-Desk-Data-Schema"
doc-id: "mb-b0bb9dbe"
updated: "2026-11-15"
---
# Front Desk Assistant — Anvil Data Tables Schema & Pipeline Spec

This specification defines the exact Anvil Data Tables structure and server pipeline (`front_desk_pipeline.py`) for **Front Desk Assistant** (running on Anvil App Server + PostgreSQL on Hetzner Cloud).

---

## 1. Anvil Data Tables Schema (Strict Workspace Isolation)

Every table below includes a `workspace` link column (`Link to workspaces`) so every query is strictly scoped to the authenticated user's workspace on the server.

### Table 1: `workspaces`
| Column Name | Anvil Type | Notes |
| :--- | :--- | :--- |
| `business_name` | Text | Company or consultant trading name |
| `owner_email` | Text | Primary owner sign-in email |
| `timezone` | Text | e.g., `Europe/London`, `Africa/Johannesburg` |
| `working_hours_json` | SimpleObject | `{"mon": ["09:00", "17:00"], ...}` |
| `services_json` | SimpleObject | List of services, durations, "from" prices, and qualifying questions |
| `faqs_json` | SimpleObject | Approved FAQ pairs (`[{"q": "...", "a": "..."}]`) |
| `tone_of_voice` | Text | `warm`, `formal`, `concise`, or `technical` |
| `approval_mode` | Text | Default: `approve_before_send` (also `draft_only`, `autonomous_low_risk`) |
| `openrouter_key_enc` | Text | Encrypted BYOK OpenRouter API key |
| `model_preset` | Text | `fast`, `balanced` (default), or `premium` |
| `monthly_spend_ceiling_gbp` | Number | Default: `15.00` |
| `monthly_spend_used_gbp` | Number | Reset monthly by scheduled task |
| `r2_bucket_name` | Text | Provisioned Cloudflare R2 bucket (`fda-tenant-{id}`) |
| `retention_days` | Number | Default: `30` (days before archiving raw webhooks to R2) |
| `google_refresh_token_enc` | Text | Encrypted OAuth2 refresh token for Google Calendar |
| `google_calendar_id` | Text | Default: `primary` |
| `booking_link` | Text | Public booking link or Google Calendar appointment URL |
| `subscription_status` | Text | `founding_pass`, `active`, `past_due`, `cancelled` |

### Table 2: `channel_connections`
| Column Name | Anvil Type | Notes |
| :--- | :--- | :--- |
| `workspace` | Link (`workspaces`) | Tenant link |
| `whatsapp_instance` | Text | Evolution API instance name |
| `whatsapp_status` | Text | `connected`, `disconnected`, `unconfigured` |
| `smsgate_login` | Text | SMSGate Cloud username |
| `smsgate_password_enc` | Text | Encrypted SMSGate Cloud password |
| `smsgate_status` | Text | `connected`, `disconnected`, `unconfigured` |
| `last_checked_at` | Date and Time | Updated every 15 minutes by heartbeat task |

### Table 3: `contacts`
| Column Name | Anvil Type | Notes |
| :--- | :--- | :--- |
| `workspace` | Link (`workspaces`) | Tenant link |
| `full_name` | Text | Extracted or entered contact name |
| `email` | Text | Normalized lowercase email (optional if `phone` present) |
| `phone` | Text | Normalized E.164 phone number, e.g. `+447700900077` (optional if `email` present) |
| `company` | Text | Optional company name |
| `source` | Text | `whatsapp`, `sms`, `email`, `webform`, `manual` |
| `do_not_contact` | True/False | Default: `False` (set `True` immediately on `STOP` / `UNSUBSCRIBE`) |
| `created_at` | Date and Time | Timestamp |

### Table 4: `leads`
| Column Name | Anvil Type | Notes |
| :--- | :--- | :--- |
| `workspace` | Link (`workspaces`) | Tenant link |
| `contact` | Link (`contacts`) | Linked contact |
| `status` | Text | `new_enquiry`, `responded`, `meeting_booked`, `proposal_quote`, `won`, `lost_not_fit`, `stalled` |
| `service_interest` | Text | Matched service name from catalogue |
| `urgency` | Text | `normal`, `high` |
| `summary` | Text | 1-sentence AI summary of the enquiry |
| `followup_count` | Number | Number of 1-to-1 follow-ups sent so far |
| `next_action` | Text | e.g., `Approve draft reply`, `Follow up in 2 days` |
| `next_action_at` | Date and Time | Used by the hourly follow-up scheduler |
| `updated_at` | Date and Time | Last activity timestamp |

### Table 5: `messages`
| Column Name | Anvil Type | Notes |
| :--- | :--- | :--- |
| `workspace` | Link (`workspaces`) | Tenant link |
| `lead` | Link (`leads`) | Linked lead |
| `contact` | Link (`contacts`) | Linked contact |
| `channel` | Text | `whatsapp`, `sms`, `email`, `webform` |
| `direction` | Text | `inbound` or `outbound` |
| `body` | Text | Message text (never overwritten once received or approved) |
| `external_message_id` | Text | Webhook deduplication ID |
| `approval_status` | Text | `received`, `pending_approval`, `approved_sent`, `auto_sent`, `rejected` |
| `delivery_status` | Text | `queued`, `sent`, `delivered`, `failed` |
| `ai_generated` | True/False | `True` if drafted by OpenRouter BYOK |
| `created_at` | Date and Time | Timestamp |

### Table 6: `action_queue`
| Column Name | Anvil Type | Notes |
| :--- | :--- | :--- |
| `workspace` | Link (`workspaces`) | Tenant link |
| `lead` | Link (`leads`) | Linked lead (optional for system/channel alerts) |
| `message` | Link (`messages`) | Draft message awaiting approval (optional) |
| `task_type` | Text | `approve_reply`, `urgent_enquiry`, `channel_disconnected`, `ai_error` |
| `title` | Text | Short summary shown in the Material 3 Action Queue |
| `priority` | Text | `high`, `normal` |
| `status` | Text | `open`, `completed`, `dismissed` |
| `created_at` | Date and Time | Timestamp |

### Table 7: `audit_events`
| Column Name | Anvil Type | Notes |
| :--- | :--- | :--- |
| `workspace` | Link (`workspaces`) | Tenant link |
| `actor` | Text | `ai_assistant`, `owner`, `system` |
| `action` | Text | e.g., `enquiry_classified`, `draft_created`, `reply_approved_and_sent`, `opt_out_recorded` |
| `object_type` | Text | `lead`, `message`, `appointment`, `channel` |
| `object_id` | Text | Row ID string |
| `summary` | Text | Redacted summary (no raw prompt logs) |
| `created_at` | Date and Time | Timestamp (entries >30 days archived to R2) |

---

## 2. How the Pipeline Enforces Your Core Rules

1. **The Model Proposes; Your App Validates & Executes:** OpenRouter returns strict JSON (`classification`, `extracted_contact`, `urgency`, `wants_booking`, `draft_reply`). Your Python code validates every field, checks deterministic Google Calendar availability, and enforces your **no-marketing / no-payment-collection** rules before saving.
2. **Never Overwrite Original Messages:** Inbound messages are stored with `approval_status="received"`. AI drafts are stored as separate rows with `approval_status="pending_approval"`. When the owner edits and approves a draft in the Material 3 Approval Queue, the edited text is saved as a final outbound record while the audit trail logs the event.
3. **Conservative Default (`approve_before_send`):** Unless the owner explicitly enables `autonomous_low_risk` (and even then, only when no custom pricing, commitment, or urgent flag is triggered), every AI draft lands cleanly in `action_queue` for one-click approval.
