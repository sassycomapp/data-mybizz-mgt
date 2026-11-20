---
title: "cloudflare"
doc-id: "mb-4b18c001"
updated: "2026-11-20"
---
# Task Spec Sheet — Cloudflare

The single reference for everything Mybizz has in Cloudflare: the account, the mybizz.live domain, every DNS record, and every Cloudflare service in use. Any change made in Cloudflare is recorded here.

---

## 1. Account and Domain

| Item | Value |
|---|---|
| Cloudflare account owner (login) | `sassycomapp@gmail.com` |
| Domain in the account | `mybizz.live` (the only domain) |
| Domain registrar | Namecheap. Namecheap holds the registration; Cloudflare manages the DNS records. |
| Workers | None |

---

## 2. DNS Records of mybizz.live

A DNS record is one line of the domain's address book: it tells the internet where a name such as `www.mybizz.live` or the mail for `mybizz.live` goes.

| # | Type | Name | Content | Proxy status | Purpose | Set by | Change rule |
|---|---|---|---|---|---|---|---|
| 1 | A | `mb-3-cs-app1` | `52.56.203.177` | Proxied | Mybizz CS App 1 on Anvil | PDLF build | Never change from marketing work |
| 2 | A | `mb-3-cs-app5` | `52.56.203.177` | Proxied | Mybizz CS App 5 on Anvil | PDLF build | Never change from marketing work |
| 3 | A | `mb-4-ecom-app1` | `52.56.203.177` | Proxied | mb-4-ecom App 1 on Anvil | PDLF build | Never change from marketing work |
| 4 | A | `mb-4-ecom-app5` | `52.56.203.177` | Proxied | mb-4-ecom App 5 on Anvil | PDLF build | Never change from marketing work |
| 5 | CNAME | `mybizz.live` | `mybizz-holding.pages.dev` | Proxied | Holding page | Cloudflare Pages (custom domain) | Changed only by the steps in section 5 |
| 6 | CNAME | `www` | `mybizz-holding.pages.dev` | Proxied | Holding page | Cloudflare Pages (custom domain) | Changed only by the steps in section 5 |
| 7 | MX | `mybizz.live` | `route1.mx.cloudflare.net` (priority 42) | DNS only, locked | Receives mybizz.live mail | Email Routing | Locked by Cloudflare |
| 8 | MX | `mybizz.live` | `route2.mx.cloudflare.net` (priority 28) | DNS only, locked | Receives mybizz.live mail | Email Routing | Locked by Cloudflare |
| 9 | MX | `mybizz.live` | `route3.mx.cloudflare.net` (priority 25) | DNS only, locked | Receives mybizz.live mail | Email Routing | Locked by Cloudflare |
| 10 | TXT | `cf2024-1._domainkey` | `v=DKIM1; h=sha256; k=rsa; p=…` | DNS only, locked | Cloudflare's mail signature | Email Routing | Locked by Cloudflare |
| 11 | TXT | `mybizz.live` | `v=spf1 include:_spf.mx.cloudflare.net ~all` | DNS only | SPF: the servers allowed to handle mybizz.live mail | Email Routing | Exactly one SPF record exists for mybizz.live |
| 12 | TXT | `mybizz.live` | `brevo-code:24c7a7846433b9af4cf47…` | DNS only | Proves to Brevo that Mybizz owns mybizz.live | Brevo set-up | Keep while Brevo sends Mybizz mail |
| 13 | CNAME | `brevo1._domainkey` | `b1.mybizz-live.dkim.brevo.com` | DNS only | Brevo's mail signature (DKIM) | Brevo set-up | Must stay DNS only |
| 14 | CNAME | `brevo2._domainkey` | `b2.mybizz-live.dkim.brevo.com` | DNS only | Brevo's mail signature (DKIM) | Brevo set-up | Must stay DNS only |
| 15 | TXT | `_dmarc` | `v=DMARC1; p=none; rua=mailto:rua@dmarc.brevo.com` | DNS only | DMARC: tells receiving servers how to treat mail that fails the checks | Brevo set-up | Keep while Brevo sends Mybizz mail |

---

## 3. Cloudflare Services in Use

### 3.1 Email Routing (receiving)

| Setting | Value |
|---|---|
| Status | Enabled |
| Destination address | `mybizzlive@gmail.com` (Verified) |
| Routing rule | `hello@mybizz.live` → Send to an email → `mybizzlive@gmail.com` (Active) |
| Routing rule | `support@mybizz.live` → Send to an email → `mybizzlive@gmail.com` (Active) |
| Routing rule | `abuse@mybizz.live` → Send to an email → `mybizzlive@gmail.com` (Active) |
| Catch-all | Disabled: mail to any other address is refused |

The full email set-up, including sending through Brevo and the Thunderbird folders, is in [[[data-mybizz-mgt:marketing/task-spec-sheets/email-setup]]](C:/data-mybizz-mgt/marketing/task-spec-sheets/email-setup.md).

### 3.2 Pages (the holding page)

| Setting | Value |
|---|---|
| Project | `mybizz-holding` (Direct Upload) |
| Address on Cloudflare | `https://mybizz-holding.pages.dev` |
| Custom domains | `mybizz.live` and `www.mybizz.live`, both Active |
| Content | The folder `C:\data-mybizz-mgt\marketing\holding-page` (`index.html`, `mybizz-mark-800.png`) |

To change the page: edit the files in `marketing/holding-page`, then open the `mybizz-holding` project, choose **Create deployment**, and upload the folder again.

The holding page's own set-up is in [[[data-mybizz-mgt:marketing/task-spec-sheets/holding-page]]](C:/data-mybizz-mgt/marketing/task-spec-sheets/holding-page.md).

### 3.3 Email Address Obfuscation

Cloudflare hides email addresses on Mybizz web pages from robots that collect addresses. Visitors see and click the addresses as normal.

---

## 4. Cloudflare Services Not in Use

| Service | Status |
|---|---|
| Email Sending | Not used. Mybizz sends its own mail through Brevo. Email Sending is a paid Cloudflare service and stays unpurchased. |
| Workers | None created |
| R2 storage | No bucket in the account. R2's role in the Mybizz products is set out in [[[project-library-global:specifications-global/spec-client-instance-hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md). |

---

## 5. Pointing mybizz.live to the Mybizz Website

When the Mybizz website is live on Anvil, `mybizz.live` and `www.mybizz.live` move from the holding page to the website:

1. In **Workers & Pages → mybizz-holding → Custom domains**, remove `mybizz.live` and `www.mybizz.live`. Cloudflare removes records 5 and 6.
2. In **mybizz.live → DNS → Records**, add two A records, both **Proxied**:

   | Type | Name | Content |
   |---|---|---|
   | A | `mybizz.live` | `52.56.203.177` |
   | A | `www` | `52.56.203.177` |

3. Open `https://mybizz.live` and `https://www.mybizz.live`. Both show the Mybizz website.
4. Record the change in this sheet.
