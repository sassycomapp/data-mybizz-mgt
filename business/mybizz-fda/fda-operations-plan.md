---
title: "fda-operations-plan"
updated: "2026-11-17"
doc-id: "mb-458de800"
---
# Mybizz FDA — Operations Plan

How Mybizz FDA is run day to day: what runs by itself, what the developer does by hand, and the steps to launch. The technical limits and the server design are in the project library's architecture reference.

---

## 1. What Runs by Itself

The Mybizz management app (App 5) and scheduled jobs on each client's copy do this work. App 5 sends the developer one daily summary and an immediate message only when a decision is needed.

| Area | How often | Done by | What happens |
|---|---|---|---|
| New client set-up | Each registration | App 5 | Creates the client's container, database, R2 bucket, email address and keys; sends the Owner the sign-in link |
| Channel health | Every 15 minutes | Client copy | Checks email, SMS phone and WhatsApp; a broken channel becomes a high-priority item in the client's action queue |
| Client backups | Nightly | Client copy | Encrypted backup to the client's own R2 bucket; App 5 checks each backup arrived |
| History clean-up | Nightly | Client copy | Records older than 30 days move to the client's R2 bucket |
| Container memory | On alert | App 5 | Raises a container from 1 GiB to 2 GiB above 80% use and tells the developer |
| Server security updates | Daily | Each server | Installs security patches; restarts only in the Sunday 06:00 UK window |
| Disk space | Continuous | App 5 | Alerts the developer at 75% use |
| Uptime | Every minute | Outside uptime check | Alerts the developer if App 5 fails or a client copy stops reporting for 30 minutes |
| Non-payment | Each Paddle notice | App 5 | Warning on day 1, suspension on day 7, final backup and removal on day 37 |
| Releases | Each approved release | App 5 | Test client first, then every client; a failed health check rolls the client back |
| Restore drill | Monthly | Test client copy | Restores one backup into a scratch database, checks it, deletes it |

---

## 2. What the Developer Does by Hand

- Approve each release.
- Answer support emails within one working day; within four hours when a client cannot work at all.
- Act on reports to `abuse@mybizz.live`, using App 5's Suspend action.
- Keep the outreach going: the routine in `fda-sniper-outreach-kit.md`.

---

## 3. Risks and Safeguards

| Risk | Safeguard |
|---|---|
| One client overloads the database | Each client's database user is limited to 3 connections, 60-second queries and 2 GiB of data |
| A WhatsApp number is banned | Meta's official service only; one-to-one replies only; STOP enforced at once |
| AI costs run away | The client's own key and monthly ceiling; draft-only when the ceiling is reached |
| The client's SMS phone goes offline | Checked every 15 minutes; flagged in the client's action queue |
| A server or EU location fails | A live standby database in a second EU location; nightly client backups; servers rebuilt from the release image |
| A key leaks | Keys limited to one purpose; hardware security keys on every supplier account |
| Backups deleted by an attacker | R2 Object Lock keeps daily backups 7 days and weekly backups 28 days |

---

## 4. Launch Steps

### Mybizz FDA launch
1. **Servers:** set up the Hetzner application server, the database pair, Caddy, monitoring and the provisioning runner; test a full backup and restore.
2. **Email:** set up Amazon SES for `in.fda.mybizz.live` and `reply.fda.mybizz.live`.
3. **Google:** submit Mybizz FDA's calendar access for Google verification.
4. **Abuse address:** set up `abuse@mybizz.live`.
5. **Paddle:** add the £45 Mybizz FDA price in Paddle, once the company steps in `business/mybizz-live/mybizz-live-business-plan.md` are done.
6. **Mybizz's own front desk:** run Mybizz's own Mybizz FDA copy on mybizz.live so prospects can test it.
7. **Final checks:** run a test enquiry on every launch channel; confirm STOP stops every automatic message; confirm approvals record who gave them.

The WhatsApp channel is switched on for every client once Mybizz-Live Ltd is registered and verified by Meta; the company steps are in `business/mybizz-live/mybizz-live-business-plan.md`.
