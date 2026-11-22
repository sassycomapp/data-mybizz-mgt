---
title: "emailoctopus"
---
# Task Spec Sheet — Mybizz Newsletter (EmailOctopus)

**Task:** C8 in `marketing-project-plan.xlsx`
**Owner:** David
**Depends on:** A1 (Mybizz email addresses)
**Unblocks:** the Mybizz newsletter, every email sent to subscribers, and D10 (the sign-up form)

---

## 1. Result

| Item | Value |
|---|---|
| Service | EmailOctopus, free plan |
| Address | `https://emailoctopus.com` |
| Signs in with | `hello@mybizz.live` and its password (password manager) |
| Card or billing | None |
| List | Mybizz |
| Sending domain | `mybizz.live`, verified (DNS records 16 to 19 on the Cloudflare sheet) |
| Sender address | `hello@mybizz.live`, verified |
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

## 3. Sign-Up Form and Double Opt-In

The holding page at mybizz.live carries an EmailOctopus sign-up form that adds subscribers to the **Mybizz** list.

| Item | Value |
|---|---|
| Form type | Inline, template **Marie** |
| Form ID | `059a6656-e679-11f1-80ee-21200a5a1eff` |
| Heading | Be the first to know when Mybizz launches |
| Text | Get an email the day Mybizz opens, then occasional news. Unsubscribe any time. |
| Button | Notify me, Professional Blue `#0200BD`; form padding 6 px top, left and right |
| Consent checkbox | On: "I agree to receive emails from Mybizz about its launch, news and offers. I can unsubscribe at any time." |
| Bot protection | Google reCAPTCHA, on; the holding page carries Google's required notice |
| Success message | Thanks. Please check your inbox to confirm. |

**Double opt-in** (list settings → Consent & customisation → Double opt-in): on. Every sign-up gets a confirmation email and joins the list only after clicking its button.

| Confirmation email | Value |
|---|---|
| Sending from (name) | Mybizz |
| Sending from (address) | `hello@mybizz.live` |
| Subject | Please confirm your email for Mybizz |
| Title | Confirm your email |
| Button | Yes, keep me updated |
| Colours | Background `#F7F7F7`; title and button `#0200BD` |

- **Why double opt-in:** it keeps mistyped and fake addresses off the list and records each subscriber's consent, as UK and EU rules expect.
- **Changes to the form** are made in EmailOctopus and saved there; the holding page loads the form from EmailOctopus, so no redeploy is needed.

**Check:** a sign-up on mybizz.live from the phone shows the success message, the confirmation email arrives, and the confirmed address appears in the Mybizz list.

---

## 4. Before the First Newsletter

**Business postal address.** Email marketing rules, notably in the United States, expect a business postal address in every marketing email. Once Mybizz-Live Ltd is registered, its UK registered office address is added in EmailOctopus and switched on for emails. David's home address never appears in an email.

**Check:** a test campaign sent to `hello@mybizz.live` arrives in the **hello** folder, shows the logo, colours and social links, and its footer shows the Mybizz-Live Ltd address.
