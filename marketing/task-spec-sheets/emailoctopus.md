---
title: "emailoctopus"
---
# Task Spec Sheet — Mybizz Newsletter (EmailOctopus)

**Task:** C8 in `marketing-project-plan.xlsx`
**Owner:** David
**Depends on:** A1 (Mybizz email addresses)
**Unblocks:** the Mybizz newsletter and every email sent to subscribers

---

## 1. Result

| Item | Value |
|---|---|
| Service | EmailOctopus, free plan |
| Address | `https://emailoctopus.com` |
| Signs in with | `hello@mybizz.live` and its password (password manager) |
| Card or billing | None |
| Postal address in emails | Kept out |
| 2-step verification | On, by authentication app |
| Google sign-in | Not linked: one sign-in method only |

---

## 2. Brand Kit

| Item | Value |
|---|---|
| Logo | `mybizz-smile-mark-disc-800.png` |
| Primary colour | Professional Blue `#0200BD` |
| Secondary colour | `#004FDA`, the secondary colour of the Professional Blue palette in `m3-custom-theme` |
| Heading | Roboto, 24 px, bold |
| Body text | Roboto, 16 px, regular |

**Social links:**

| Platform | Link |
|---|---|
| YouTube | `https://www.youtube.com/@mybizzlive` |
| Facebook | `https://www.facebook.com/mybizzlive` |
| Instagram | `https://www.instagram.com/mybizzlive` |
| TikTok | `https://www.tiktok.com/@mybizzlive` |

LinkedIn is added once the Mybizz-Live company page exists.

- **Why these colours and fonts:** emails then match the Mybizz app, the logo and every channel.
- **Why 16 px body text:** smaller text is hard to read on a phone, where most emails are opened.

---

## 3. Before the First Newsletter

1. **Business postal address.** Email marketing rules, notably in the United States, expect a business postal address in every marketing email. Once Mybizz-Live Ltd is registered, its UK registered office address is added in EmailOctopus and switched on for emails. David's home address never appears in an email.
2. **Sending domain.** EmailOctopus is set up to send as `hello@mybizz.live`, with the DNS records EmailOctopus gives added in Cloudflare (recorded on [[[data-mybizz-mgt:marketing/task-spec-sheets/cloudflare]]](C:/data-mybizz-mgt/marketing/task-spec-sheets/cloudflare.md)), so the newsletter passes SPF, DKIM and DMARC checks.

**Check:** a test campaign sent to `hello@mybizz.live` arrives in the **hello** folder, shows the logo, colours and social links, and its footer shows the Mybizz-Live Ltd address.
