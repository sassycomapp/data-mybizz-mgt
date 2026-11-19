---
title: "fda-operations-plan"
updated: "2026-11-19"
doc-id: "mb-458de800"
---
# Mybizz FDA — Operations Plan

How Mybizz FDA is run day to day: what runs by itself, what the developer does by hand, and the steps to launch. The technical limits and the server design are in [[[mb-1-fda-project-library:docs-local/mb-1-fda-architecture-reference]]](C:/dev/dev-mb-1-fda/mb-1-fda-project-library/docs-local/mb-1-fda-architecture-reference.md).

---

## 1. What Runs by Itself

The Mybizz management app (App 5) and scheduled jobs on each client's copy do this work. App 5 sends the developer one daily summary and an immediate message only when a decision is needed.

The schedules, limits and alerts are in [[[mb-1-fda-project-library:docs-local/mb-1-fda-architecture-reference]]](C:/dev/dev-mb-1-fda/mb-1-fda-project-library/docs-local/mb-1-fda-architecture-reference.md) sections 4 and 5.

| Area | How often | Done by | What happens |
|---|---|---|---|
| Releases | Each approved release | App 5 | Test client first, then every client; a failed health check rolls the client back |

---

## 2. What the Developer Does by Hand

- Approve each release.
- Answer support emails within one working day; within four hours when a client cannot work at all.
- Act on reports to `abuse@mybizz.live`, using App 5's Suspend action.
- Keep the outreach going: the teardown routine in [[[data-mybizz-mgt:marketing/mybizz-live-marketing-plan]]](C:/data-mybizz-mgt/marketing/mybizz-live-marketing-plan.md) section 8.

---

## 3. Risks and Safeguards

The technical safeguards are in [[[mb-1-fda-project-library:docs-local/mb-1-fda-architecture-reference]]](C:/dev/dev-mb-1-fda/mb-1-fda-project-library/docs-local/mb-1-fda-architecture-reference.md) sections 4 and 5, and the product's risks and answers in [[[mb-1-fda-project-library:docs-local/mb-1-fda-concept]]](C:/dev/dev-mb-1-fda/mb-1-fda-project-library/docs-local/mb-1-fda-concept.md) section 15.

| Risk | Safeguard |
|---|---|
| A key leaks | Keys limited to one purpose; hardware security keys on every supplier account |

---

## 4. Launch Steps

### Mybizz FDA launch
1. **Servers:** set up the Ubicloud database service, the Hetzner application server, Caddy, monitoring and the provisioning runner; test a full backup and restore.
2. **Email:** set up Amazon SES for `in.fda.mybizz.live` and `reply.fda.mybizz.live`.
3. **Google:** submit Mybizz FDA's calendar access for Google verification.
4. **Abuse address:** set up `abuse@mybizz.live`.
5. **Paddle:** add the £45 Mybizz FDA price in Paddle, once the company steps in [[[data-mybizz-mgt:business/mybizz-live/mybizz-live-business-plan]]](C:/data-mybizz-mgt/business/mybizz-live/mybizz-live-business-plan.md) are done.
6. **Mybizz's own front desk:** run Mybizz's own Mybizz FDA copy on mybizz.live so prospects can test it.
7. **Final checks:** run a test enquiry on every launch channel; confirm STOP stops every automatic message; confirm approvals record who gave them.

The WhatsApp channel is switched on for every client once Mybizz-Live Ltd is registered and verified by Meta; the company steps are in [[[data-mybizz-mgt:business/mybizz-live/mybizz-live-business-plan]]](C:/data-mybizz-mgt/business/mybizz-live/mybizz-live-business-plan.md).
