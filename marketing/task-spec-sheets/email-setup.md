---
title: "email-setup"
doc-id: "mb-ece401ac"
updated: "2026-11-19"
---
# Task Spec Sheet — Email Setup

**Task:** A1 in `marketing-project-management-plan.xlsx`
**Owner:** David
**Depends on:** nothing
**Unblocks:** A2 (the Mybizz Google account), C8 (EmailOctopus) and every Mybizz account created after them

---

## 1. Result

Mybizz has three working mybizz.live email addresses at no cost. Mail sent to any of them arrives in Thunderbird, and David sends mail from them in Thunderbird.

| Address | Use |
|---|---|
| `hello@mybizz.live` | Every Mybizz account, marketing and teardown messages |
| `support@mybizz.live` | Client support, as named in the Mybizz FDA legal policies |
| `abuse@mybizz.live` | Abuse reports, as named in the Mybizz FDA operations plan |

---

## 2. How the Design Works

| Part | Service | What it does | Cost |
|---|---|---|---|
| Receiving | Cloudflare Email Routing | Takes mail sent to the three addresses and passes it to David's Gmail inbox, the inbox Thunderbird already reads | Free |
| Sending | Brevo, free plan | Sends David's outgoing mail from the three addresses, signed for mybizz.live so receiving mail systems trust it | Free up to 300 emails a day |
| Reading and writing | Thunderbird | Shows the incoming mail and sends replies through Brevo | Free |

- **Why Cloudflare:** the mybizz.live DNS records are managed in Cloudflare, so the routing is set up in the same dashboard.
- **Why Brevo for sending:** mail sent through Brevo carries a signature for mybizz.live, so it passes the receiving systems' checks (SPF, DKIM and DMARC: the three tests that prove a message really comes from mybizz.live) and lands in the inbox, not in spam.
- **Brevo's role:** Brevo carries David's own business mail only. Brevo is not part of any Mybizz product.
- **The Gmail address stays private:** senders and recipients only ever see the mybizz.live addresses.

---

## 3. Before Starting

1. A Cloudflare login with access to the `mybizz.live` zone.
2. A Namecheap login for the account that holds the `mybizz.live` domain.
3. Thunderbird open, with David's Gmail account working.

---

## 4. Steps

### Part A — Check the old forwarding (Namecheap)

The `mybizz.live` DNS records hold five MX records pointing at `eforward1` to `eforward5.registrar-servers.com`. These are Namecheap's email forwarding servers. Part B replaces them.

1. In Namecheap, open **Domain List → mybizz.live → Manage → Redirect Email**.
2. Note any forwarding rule listed there. Every address that matters is recreated in Part B, step 6.

### Part B — Receiving (Cloudflare Email Routing)

1. In Cloudflare, open **mybizz.live → Email → Email Routing**.
2. Click **Get started** (or **Enable Email Routing**).
3. Cloudflare lists the records that clash with Email Routing: the five `eforward` MX records and the `v=spf1 include:spf.efwd.registrar-servers.com` TXT record. Approve their removal. Cloudflare then adds its own MX records (`route1`, `route2` and `route3.mx.cloudflare.net`) and its own SPF record.
4. Open **Destination addresses → Add destination address** and enter David's Gmail address.
5. Open the verification email in Thunderbird and click the link. The destination shows **Verified**.
6. Open **Routing rules → Create address** three times, for `hello`, `support` and `abuse`, each with the action **Send to an email** and the verified Gmail address as destination.
7. Leave **Catch-all** switched off, so mail to unknown addresses is refused instead of filling the inbox with spam.

### Part C — Sending (Brevo)

1. Sign up for Brevo's free plan at brevo.com with `hello@mybizz.live`. The confirmation email arrives in Thunderbird through Part B.
2. In Brevo, open **Senders, Domains & Dedicated IPs → Domains → Add a domain** and enter `mybizz.live`.
3. Brevo offers to set up the records in Cloudflare automatically. Accept the automatic set-up. If Brevo shows the records instead, add each one in Cloudflare under **DNS → Records** as **DNS only** (grey cloud): the `brevo-code` TXT record, the DKIM records and the DMARC record.
4. In Cloudflare **DNS → Records**, open the one TXT record that starts `v=spf1` and set its content to exactly:
   `v=spf1 include:_spf.mx.cloudflare.net include:spf.brevo.com ~all`
   The domain holds exactly one SPF record. Two SPF records break both.
5. If the DNS records hold no `_dmarc` TXT record after step 3, add one: name `_dmarc`, content `v=DMARC1; p=none; rua=mailto:hello@mybizz.live`.
6. Back in Brevo, click **Authenticate** for `mybizz.live`. Every check shows green.
7. In Brevo, open **Senders → Add a sender** twice: `hello@mybizz.live` with the name **Mybizz**, and `support@mybizz.live` with the name **Mybizz Support**.
8. In Brevo, open **SMTP & API → SMTP → Generate a new SMTP key**, name it `thunderbird`, and copy the key. Brevo shows the key once. Keep it in the password manager.
9. Note the **SMTP login** shown on the same page.

### Part D — Thunderbird

1. Open **Account Settings → Outgoing Server (SMTP) → Add**:

   | Setting | Value |
   |---|---|
   | Description | Brevo |
   | Server name | `smtp-relay.brevo.com` |
   | Port | `587` |
   | Connection security | STARTTLS |
   | Authentication method | Normal password |
   | User name | The Brevo SMTP login from Part C, step 9 |

2. Open the Gmail account's **Account Settings → Manage Identities → Add**:
   - Your Name: `Mybizz`
   - Email Address: `hello@mybizz.live`
   - Outgoing Server: **Brevo**
3. Add a second identity the same way: `Mybizz Support`, `support@mybizz.live`, outgoing server **Brevo**.
4. Send the first message from the `hello@mybizz.live` identity. Thunderbird asks for the Brevo password: paste the SMTP key from Part C, step 8, and tick **Use Password Manager to remember this password**.

---

## 5. Checks

| # | Check | Success |
|---|---|---|
| 1 | From any other email account, send a message to `hello@mybizz.live`, `support@mybizz.live` and `abuse@mybizz.live` | All three arrive in Thunderbird |
| 2 | Reply to the `hello@` test message from the `hello@mybizz.live` identity | The other account receives the reply from `hello@mybizz.live`, in its inbox, not in spam |
| 3 | In that other account (a Gmail account), open the reply and choose **Show original** | SPF, DKIM and DMARC each show **PASS** |
| 4 | Send a message to `nobody@mybizz.live` | The message is refused |

---

## 6. Records

1. Add Cloudflare Email Routing and Brevo to the **Accounts** sheet of `marketing-project-management-plan.xlsx`, with login email and 2-step verification status.
2. Switch on 2-step verification in Brevo.
3. Set task A1 to **Done** on the **Plan** sheet, with the date.
