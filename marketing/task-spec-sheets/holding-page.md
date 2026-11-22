---
title: "holding-page"
doc-id: "mb-14ab4c75"
updated: "2026-11-20"
---
# Task Spec Sheet — Holding Page on mybizz.live

**Task:** A10 in `marketing-project-plan.xlsx`
**Owner:** David
**Depends on:** A5 (approved logo)
**Unblocks:** B1 to B5, because every Mybizz account links to mybizz.live

---

## 1. Result

`mybizz.live` and `www.mybizz.live` show one Mybizz page: the white Mybizz logo (smiling M mark and wordmark) on Professional Blue, the line "Online business software for consultants and service businesses – One platform. One price. Your customers. Your data.", "Launching soon", a sign-up form, and a link to `hello@mybizz.live`.

The sign-up form is EmailOctopus's, loaded from EmailOctopus; its settings are on [[[data-mybizz-mgt:marketing/task-spec-sheets/emailoctopus]]](C:/data-mybizz-mgt/marketing/task-spec-sheets/emailoctopus.md). Below the form, the page carries Google's reCAPTCHA notice. The page layout grows with its content, so it scrolls on a phone.

---

## 2. How the Design Works

| Part | Service | What it does | Cost |
|---|---|---|---|
| The page | `marketing/holding-page/` in `data-mybizz-mgt` | Holds the page (`index.html`) and its icons (`favicon.ico`, `mybizz-smile-mark-disc-800.png`) | Free |
| Hosting | Cloudflare Pages | Serves the page at `mybizz.live` and `www.mybizz.live` | Free |

- **Only two addresses change:** `mybizz.live` and `www.mybizz.live`. The app addresses (`mb-3-cs-app1`, `mb-3-cs-app5`, `mb-4-ecom-app1`, `mb-4-ecom-app5`) and every email record stay as they are.
- **When the Mybizz website is live:** the two custom domains are removed from the Cloudflare Pages project, and the two A records pointing to `52.56.203.177` (Proxied) are added back.

---

## 3. Steps

### Part A — Remove the two A records (Cloudflare)

In Cloudflare, open **mybizz.live → DNS → Records** and delete these two records, each by **Edit → Delete**:

| Type | Name | Content |
|---|---|---|
| A | `mybizz.live` | `52.56.203.177` |
| A | `www` | `52.56.203.177` |

Every other record stays.

### Part B — Publish the page (Cloudflare Pages)

1. In Cloudflare, open **Workers & Pages → Create → Pages → Upload assets** (Direct Upload).
2. **Project name:** `mybizz-holding`. Click **Create project**.
3. Upload the folder `C:\data-mybizz-mgt\marketing\holding-page`, then click **Deploy site**.
4. The page opens at `mybizz-holding.pages.dev`. It shows the Mybizz page.

### Part C — Connect the two addresses

1. In the `mybizz-holding` project, open **Custom domains → Set up a custom domain**.
2. Enter `mybizz.live` and click **Continue → Activate domain**. Cloudflare adds the record itself.
3. Repeat with `www.mybizz.live`.
4. Each domain shows **Active** within a few minutes.

---

## 4. Checks

| # | Check | Success |
|---|---|---|
| 1 | Open `https://mybizz.live` in a browser | The Mybizz page shows, with the padlock (secure connection) |
| 2 | Open `https://www.mybizz.live` | The same page shows |
| 3 | Open the page on a phone | The page fits the screen, and the text is readable |
| 4 | Click `hello@mybizz.live` on the page | A new email to `hello@mybizz.live` opens |
| 5 | Send a test email to `hello@mybizz.live` | The email arrives in the hello folder in Thunderbird |

---

## 5. Records

1. **Accounts** sheet of `marketing-project-plan.xlsx`: Cloudflare Pages, project `mybizz-holding`.
2. **Plan** sheet: task A10 set to **Done**, with the date.
