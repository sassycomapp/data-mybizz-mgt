---
title: "email-setup"
doc-id: "mb-ece401ac"
updated: "2026-11-20"
---
# Task Spec Sheet — Email Setup

**Task:** A1 in `marketing-project-plan.xlsx`
**Owner:** David
**Depends on:** nothing
**Unblocks:** A2 (the Mybizz Google account), C8 (EmailOctopus) and every Mybizz account created after them

---

## 1. Result

Mybizz has three working mybizz.live email addresses at no cost. Each address has its own folder in Thunderbird, holding the mail it receives and the mail sent from it.

| Address | Use | Sends mail |
|---|---|---|
| `hello@mybizz.live` | The main business address: every Mybizz account, marketing, teardowns and general enquiries | Yes; the default sender |
| `support@mybizz.live` | Client support, as named in the Mybizz FDA legal policies | Yes |
| `abuse@mybizz.live` | Abuse reports, as named in the Mybizz FDA operations plan | No; receives only |

Mail sent to any other mybizz.live address is refused.

---

## 2. How the Design Works

| Part | Service | What it does | Cost |
|---|---|---|---|
| Receiving | Cloudflare Email Routing | Takes mail sent to the three addresses and passes it to the Mybizz mailbox, `mybizzlive@gmail.com` | Free |
| Mailbox | Gmail, `mybizzlive@gmail.com` | Stores the mail and sorts each address's mail into its own label: `hello`, `support`, `abuse` | Free |
| Sending | Brevo, free plan | Sends the outgoing mail of `hello@` and `support@`, signed for mybizz.live so it passes SPF, DKIM and DMARC (the three tests that prove a message really comes from mybizz.live) | Free up to 300 emails a day |
| Reading and writing | Thunderbird | Shows each label as a folder, sends through Brevo, and files each sent message in the folder of the address it was sent from | Free |

- **Why Cloudflare:** the mybizz.live DNS records are managed in Cloudflare, so the routing is set up in the same dashboard.
- **Why a dedicated Gmail mailbox:** Mybizz mail stays apart from all other mail and can be handed to a helper on its own.
- **Why Brevo for sending:** Brevo signs each message for mybizz.live, so messages land in the inbox, not in spam.
- **Brevo's role:** Brevo carries Mybizz's own business mail only. Brevo is not part of any Mybizz product.
- **The Gmail address stays private:** senders and recipients only ever see the mybizz.live addresses.

---

## 3. Before Starting

1. A Cloudflare login with access to the `mybizz.live` zone.
2. A Namecheap login for the account that holds the `mybizz.live` domain.
3. Thunderbird installed.

---

## 4. Steps

### Part A — Check the old forwarding (Namecheap)

1. In Namecheap, open **Account → Domain List → mybizz.live → Manage → Advanced DNS → Mail Settings**.
2. Note any forwarding rule listed. Every address that matters is recreated in Part D.

### Part B — The Mybizz mailbox (Gmail and Thunderbird)

1. In a private browser window, create the Gmail account `mybizzlive@gmail.com` at accounts.google.com/signup.
2. Switch on 2-step verification: **myaccount.google.com → Security → 2-Step Verification**.
3. Add `mybizzlive@gmail.com` to Thunderbird.

### Part C — Clear the old mail records (Cloudflare)

In Cloudflare, open **mybizz.live → DNS → Records** and delete these six records, each by **Edit → Delete**:

| Type | Name | Content |
|---|---|---|
| MX | mybizz.live | `eforward1.registrar-servers.com` |
| MX | mybizz.live | `eforward2.registrar-servers.com` |
| MX | mybizz.live | `eforward3.registrar-servers.com` |
| MX | mybizz.live | `eforward4.registrar-servers.com` |
| MX | mybizz.live | `eforward5.registrar-servers.com` |
| TXT | mybizz.live | `v=spf1 include:spf.efwd.registrar-servers.com …` |

Every A record stays as it is.

### Part D — Receiving (Cloudflare Email Routing)

1. Open **Email → Email Routing → Onboard Domain**, choose **mybizz.live**, and click **Activate**. Cloudflare adds and locks five records: three MX records (`route1`, `route2` and `route3.mx.cloudflare.net`), a DKIM record (`cf2024-1._domainkey`) and the SPF record `v=spf1 include:_spf.mx.cloudflare.net ~all`. The status changes from **Syncing** to **Enabled**.
2. Open **Destination addresses**, add `mybizzlive@gmail.com`, and click **Verify email address** in Cloudflare's email. The status changes to **Verified**.
3. Open **mybizz.live → Routing rules → Create routing rule** three times:

   | Email pattern | Action | Destination |
   |---|---|---|
   | `hello` @ mybizz.live | Send to an email | `mybizzlive@gmail.com` |
   | `support` @ mybizz.live | Send to an email | `mybizzlive@gmail.com` |
   | `abuse` @ mybizz.live | Send to an email | `mybizzlive@gmail.com` |

4. **Catch-all** stays **Disabled**.

### Part E — Sorting (Gmail filters)

In Gmail (mail.google.com, signed in as `mybizzlive@gmail.com`), create one filter for each address: **Show search options → To → Create filter**, with these settings:

| To | Skip the Inbox (Archive it) | Apply the label | Also apply filter to matching conversations |
|---|---|---|---|
| `hello@mybizz.live` | Ticked | `hello` | Ticked |
| `support@mybizz.live` | Ticked | `support` | Ticked |
| `abuse@mybizz.live` | Ticked | `abuse` | Ticked |

### Part F — Sending (Brevo)

1. Sign up for Brevo's free plan at brevo.com with `hello@mybizz.live`, and confirm through the link in Brevo's email. Brevo creates `hello@mybizz.live` as a sender automatically.
2. Open **Senders, Domains & Dedicated IPs → Domains → Add a domain**, enter `mybizz.live`, leave **Branded subdomain** empty, and choose the **Manual** setup method.
3. In Cloudflare **DNS → Records → Add record**, add the four records Brevo lists, copying each value with Brevo's **Copy** button:

   | Type | Name | Content / Target | Proxy status |
   |---|---|---|---|
   | TXT | `@` | Brevo's value starting `brevo-code:` | — |
   | CNAME | `brevo1._domainkey` | `b1.mybizz-live.dkim.brevo.com` | DNS only |
   | CNAME | `brevo2._domainkey` | `b2.mybizz-live.dkim.brevo.com` | DNS only |
   | TXT | `_dmarc` | Brevo's value starting `v=DMARC1; p=none; rua=mailto:rua@dmarc.brevo.com` | — |

   Each CNAME record is set to **DNS only** (grey cloud) before it is saved.
4. In Brevo, click **Verify records**, then **Authenticate domain**. The **Domains** tab shows `mybizz.live` as authenticated. The branding notice is skipped.
5. Open **Senders → Add sender**: **From name** `Mybizz Support`, **From email** `support@mybizz.live`. `hello@mybizz.live` carries the name `Mybizz`.
6. Open **SMTP & API → SMTP → Generate a new SMTP key**, name it `thunderbird`, and save the key in the password manager. Brevo shows the key once. Note the **Login** on the same page.
7. Switch on two-factor authentication in Brevo's security settings.

### Part G — Thunderbird

1. **Account Settings → Outgoing Server (SMTP) → Add:**

   | Setting | Value |
   |---|---|
   | Description | Brevo |
   | Server Name | `smtp-relay.brevo.com` |
   | Port | `587` |
   | Connection security | STARTTLS |
   | Authentication method | Normal password |
   | User Name | The Brevo SMTP login from Part F, step 6 |

2. **Account Settings → mybizzlive@gmail.com → Manage Identities → Add**, twice:

   | Your Name | Email Address | Outgoing Server | Copies & Folders: Place a copy in |
   |---|---|---|---|
   | `Mybizz` | `hello@mybizz.live` | Brevo - smtp-relay.brevo.com | Other: **hello** on mybizzlive@gmail.com |
   | `Mybizz Support` | `support@mybizz.live` | Brevo - smtp-relay.brevo.com | Other: **support** on mybizzlive@gmail.com |

3. Select **Mybizz <hello@mybizz.live>** and click **Set Default**.
4. Check that the folders **hello**, **support** and **abuse** show under `mybizzlive@gmail.com`. If any folder is missing, right-click the account, choose **Subscribe…**, and tick it.
5. On the first message sent through Brevo, Thunderbird asks for the password: paste the SMTP key and tick **Use Password Manager to remember this password**.
6. **Signatures.** **Account Settings → mybizzlive@gmail.com → Manage Identities**, select an identity, **Edit**. On the **Settings** tab, tick **Attach the signature from a file instead (text, HTML or image)**, click **Choose…**, pick that identity's signature file, and click **OK**. Do this for both identities.

   | Identity | Signature file (in `C:\data-mybizz-mgt\marketing\brand-assets\`) | Signer |
   |---|---|---|
   | Mybizz <hello@mybizz.live> | `signature-hello.html` | David |
   | Mybizz Support <support@mybizz.live> | `signature-support.html` | Mybizz Support |

   Each signature has four lines: the signer's name in bold, a link to mybizz.live, the brand statement in Professional Blue at 16 pixels (two pixels larger than the rest), and the smiling M tile at 48 pixels. The sender's address is left out, because every email already shows it. Thunderbird places its standard `-- ` separator line above every signature. The tile comes from `mybizz-smile-mark-96.png` in the same folder; Thunderbird embeds it in each email, so it shows in every mail program without the reader allowing images from the internet. The signature carries a first name only: no surname, phone number or postal address. Teardowns and EmailOctopus emails do not use these signatures; teardowns are signed "Mybizz", and EmailOctopus adds its own footer.

---

## 5. Checks

| # | Check | Success |
|---|---|---|
| 1 | From another email account, send a message to each of `hello@`, `support@` and `abuse@mybizz.live` | Each message arrives in its own folder in Thunderbird |
| 2 | Send a message from `hello@mybizz.live` and from `support@mybizz.live` to another account, and reply to each from that account | Each message arrives from the right mybizz.live address, in the inbox, not in spam; each sent message and its reply sit in the matching folder |
| 3 | In the other account (Gmail), open each message received from mybizz.live and choose **⋮ → Show original** | SPF, DKIM and DMARC each show **PASS** |
| 4 | Send a message to `nobody@mybizz.live` | The message is refused and bounces back |
| 5 | From each identity, send a message to another account | The identity's signature appears at the bottom, and the received message shows the name, the mybizz.live link, the brand statement and the Mybizz tile |

---

## 6. Records

1. **Accounts** sheet of `marketing-project-plan.xlsx`: the Gmail mailbox, Cloudflare Email Routing and Brevo, each with login email and 2-step verification status.
2. **Plan** sheet: task A1 set to **Done**, with the date.
