---
title: "system-adjustments-task-list"
doc-id: "mb-4c7e19a2"
updated: "2026-11-25"
---
# System Adjustments — Task List

The checklist of the system adjustments David approved on 2026-11-25: currency, data tables, the Clause Builder, Mybizz Enterprise, the referral credit, and the homes of project, marketing and business documents. Part 1 holds every decision and fact the work needs. Part 2 is the checklist.

**How the list is worked**

- Claude does every item except group H.
- Before each group, Claude lists every file of the group and the exact change in each, and waits for David's express approval. After approval Claude makes the changes, pushes them, and gives David the pull command.
- A finished item keeps its place and is prefixed with "Done". No item is ever removed.
- Claude reads the live repositories before changing anything and confirms each file's state with a read-only check first.
- Groups run in order: A, B, C, D, E, F, G. Claude never works in auto mode.

---

# Part 1 — Decisions and Facts

## 1. Mybizz and its projects

- One company: Mybizz-Live, called Mybizz. Three projects: `mb-3-cs` (Mybizz CS) in active development; `mb-1-fda` (Mybizz FDA) in advanced context planning; `mb-4-ecom` (Mybizz Shop) mostly scoped, context not worked out.
- Mybizz FDA launches first; Mybizz CS is developed first; Mybizz Shop waits until both are running.
- Mybizz CS and Mybizz Shop are platforms. Mybizz FDA is a tool, a subset of either platform; Mybizz CS has FDA built in and Mybizz Shop will likely have it too.
- Architecture, design principles, marketing plans and materials and business plans are kept as common as possible across all apps.
- A project library holds only what is canonical to building that application. Marketing lives in `C:\data-mybizz-mgt\marketing`; business planning and documentation in `C:\data-mybizz-mgt\business`; both cover every app and may hold a subfolder per app. Documents still in a project library that belong to marketing or business are moved to their homes as the work proceeds.
- `marketing/mybizz-live-marketing-plan.md` is the one marketing plan for every product. Product material is kept per product in `marketing-plan.xlsx` (Video Plan sheet) and `marketing/scripts/`.
- Division of work: Claude is lead engineer, designer and architect and does every document and schema change, including `anvil.yaml` through the `anvil-yaml` skill (OpenCode build mode or WSL). David does only the Resolve step in anvil.works and decides intent.
- Security: minimum permissions. A connector is added only when a need is agreed with David.

## 2. Currency (all Mybizz apps)

- **System currency:** one per client, set at onboarding, fixed once confirmed; the currency of the books, reports and tax returns.
- **Prices:** the client prices every product and service in the system currency.
- **Selling currencies:** in the Local Currencies tab of the dashboard's Settings page, the client links any currency to any set of countries (`local_currencies`: `currency`, `country_codes`, `rate`, `rounding`, `enabled`). Each country sees exactly one currency; a country with no row pays in the system currency. The client may type a price per item per currency (`{item}_local_prices`); where none is typed, the client's own `rate` and `rounding` produce it. This is the Shopify Markets model.
- **Charging:** the site shows the local price, and Stripe or PayPal charges it.
- **Books (one method, always):** every sale, invoice and payment stores the transaction amount in the customer's currency (`currency`) and the system-currency amount (`system_amount`), converted at the European Central Bank's published rate for the day of the transaction; the rate used is stored in `exchange_rate`. Books, reports, the dashboard and contact totals use `system_amount`. This is how Shopify (shop money and presentment money) and accounting software such as Xero (spot rate on the transaction date) record foreign-currency sales. The later difference between that amount and what reaches the bank is a realised exchange gain or loss for the client's accountant.
- **Payouts:** where the money lands does not affect the records. Stripe pays USD charges into a USD bank account without conversion when the client has added one, and converts other currencies to the default currency. PayPal holds a foreign balance by default, or converts automatically if the client sets that in Payment Receiving Preferences.
- **Refunds:** paid in the currency the customer paid in.
- Retired terms: "display currency", "dual currency". The term is "local currency".
- Mybizz is not a merchant of record and not a payment gateway.

## 3. Clause Builder (all Mybizz apps)

- Three tables: `policies` (one row per policy: name, version, published date, page address, active), `policy_clauses` (one row per clause of the client's policies: policy link, category, title, clause text, sort order, active, `feature_key` for cookie clauses tied to maps, video or payments), `clause_library` (Mybizz's suggested clauses, read-only to the client, updated by Mybizz releases).
- Every policy is shown in one display form (`PolicyPage`), one policy at a time.
- The client creates a policy by naming it, then picks suggested clauses (each pick is copied into the client's policy) or writes clauses of their own. Every clause in a client's policy can be edited, switched off, reordered or deleted.
- Mybizz suggests; the client decides. Policies are optional.
- Onboarding requires only the switch by which the client acknowledges responsibility for the business's policies. No policy has to be published before go-live. The footer and consent links show only published policies.
- Publishing raises the policy's version, keeps a copy at `legal/{policy}/v{version}.html` in R2, and consent records (kept 7 years) point to the version.
- `privacy_policy`, `t_and_c` and `cookie_policy` (Mybizz CS) and `returns_policy` and `delivery_policy` (Mybizz Shop) are replaced by these three tables. Mybizz Shop's returns and delivery policies are seeded suggestions.

## 4. Mybizz Enterprise (common to Mybizz CS and Mybizz Shop)

- A plan any Mybizz CS or Mybizz Shop client may move up to, at the client's discretion. Mybizz FDA does not offer it. It replaces the standard plan; it is not an add-on.
- Price: £299 a month; £2,990 a year (ten months, the standard annual rule); the move to Enterprise charged at one month's price, once (the assisted-setup rule). Prices in the other market currencies follow the same proportion as the standard plan.
- Hosting: a Hetzner `CCX33` server of the client's own (8 dedicated vCPU, 32 GB memory), with backups; an 8 GiB container (fixed size, outside the 2 GiB automatic limit of App 5); database connections sized to the client; a private test copy (catalogue and settings, no customer data) in a second container on the same server; the same release image and release day as every client. Database stays in Mybizz's Ubicloud service.
- Cost to Mybizz: about £139 a month (€166.69 / £139.02 in `spec-client-instance-hosting.md`), leaving about £160 a month margin (a standard client leaves about £113).
- Purpose: a client that is large all year. A short spike is met by App 5 raising a container to 2 GiB. No custom features, ever.

## 5. Referral credit

- Recorded in `adr-global/adr-tiers-model.md` ("Referral credit") and `specifications-global/spec-client-billing.md` section 4.1; App 5 keeps the `referrals` table and each client's `referral_code` and `referred_by`; the client instance shows them in `plan_summary`; tests BR-10 and RL-23.
- Only the standard annual plan takes part. An annual client earns one credit per referred client whose first annual payment completes; each credit takes one month's price off the referring client's next annual renewal, at most 5 per renewal. With the annual plan's two free months, the most a client can save is 7 months of 12 (58.3%).
- Mybizz Enterprise takes no part.
- Mybizz FDA has no annual plan (£45 a month, `mb-1-fda-concept.md` line 226–227) and takes no part, because the margin on a Mybizz FDA client is too small.

## 6. Verified state on 2026-11-25

- `mb-3-cs` app1: PDLF Steps 17 to 22 complete (C22 closed out, `mb-3-cs-project-library` commit `fd926a7`); Step 23 waits for groups A to G.
- Still carrying "display currency": the six `ui/` requirements of item 3; `access-matrix.yaml` line 360 (`DisplayCurrency`); `mb-3-cs-app1/anvil.yaml` line 3335 and `pdlf-outputs/c17/mb-3-cs-c17-app1-anvil-db-schema.yaml` line 3334 (`display_currency`). `GLOSSARY.md` names "display currency" only as a term to avoid, which is correct.
- The 2026-11-24 migration is in `docs-local/schema-migration-log.md` and `authoritative-schema.md` (74 tables), not yet in `anvil.yaml`.
- `pdlf-todo.md` section G4: items 1–3 (marketing-plan links, brand statement) open; item 4 wrongly gives line 303 and says every other file is done.
- Links to the old marketing plan: `mb-3-cs-concept.md` line 562 and `brand-profile.md` line 14.
- Brand statement: "One platform. One price. You own it." on `brand-profile.md` lines 23 and 319, a similar wording on line 168; the approved statement is "One platform. One price. Your customers. Your data." (`marketing/brand-assets/profile-texts.md`).
- The brand profiles (`mb-3-cs-project-library/docs-local/brand-profile.md`, `mb-1-fda-project-library/docs-local/brand-profile.md`) mix marketing sections with app design sections (sections 12–20 of the Mybizz CS profile: visual identity, colour, typography, layout, interaction, public website, content presentation, customer experience).
- The PRD template theming row is corrected to the m3-custom-theme law (`project-library-global` commit `43a061a`).
- The Anthropic API key is renewed and the old key removed, including from `~/.bashrc`.
- The `project-template` repository holds no currency or policy material.

---

# Part 2 — Checklist

## A. Currency: books at the day's exchange rate

1. `project-library-global`: rewrite the books rule (Part 1, section 2) in `adr-global/adr-system-currency-selection-and-immutability.md`, `policy-global/pol-common-aspects-for-mybizz-anvil-applications.md` (aspect 11), `specifications-global/spec-integration.md` and `test-suite/ts-catalogue.md`.
2. `mb-3-cs-project-library`: the same rule in `docs-local/GLOSSARY.md`, `mb-3-cs-concept.md`, `mb-3-cs-architecture-reference.md`, `design/app1/design-doc.md`, `design/app1/design-doc-first-concept.md`, `design/app1/test-plan.md`; `docs-standard-local/` BRD, PRD, SRS, `integration-architecture.md`, `scaffold-spec.md`; `legal-local/client-service-agreement.md`; `specifications-local/spec-test-specification.md`; ticket 22; the locked copies B12, B14, B15, B16 and C17.
3. Rewrite six screen requirements to the Local Currencies design: `ui/settings/SettingsForm/CurrencyTab/CurrencyTab-requirement.md` (becomes the Local Currencies tab), `SettingsForm` (line 28 and key `settings.tab.display_currency`), `ServiceEditorForm` (local prices from `service_local_prices`), `ServiceViewerForm`, `ServicesPage`, `ServiceDetailPage` (price in the customer's local currency where the client sells in it, else the system-currency price).
4. `docs-local/design/app1/access-matrix.yaml` line 360: `DisplayCurrency` becomes `LocalCurrencies` (Owner all, Manager all, every other role none).
5. `mb-4-ecom-project-library`: the same rule in `mb-4-ecom-commerce-schema.md` and `mb-4-ecom-commerce-lifecycles.md`.

## B. Data tables

6. mb-3-cs `authoritative-schema.md` and `schema-migration-log.md`: add `exchange_rate` to `payments`, `invoice` and `orders`; replace `privacy_policy`, `t_and_c` and `cookie_policy` with `policies`, `policy_clauses` and `clause_library`.
7. mb-4-ecom `mb-4-ecom-commerce-schema.md`: the same three policy tables, also replacing `returns_policy` and `delivery_policy`.
8. Apply every outstanding mb-3-cs schema change to `mb-3-cs-app1/anvil.yaml` through the `anvil-yaml` skill: the 2026-11-24 currency migration (`local_currencies`, `service_local_prices`, `package_local_prices`, `currency`, `system_amount`, `tax_amount_system`, removal of `services.display_currency`) and item 6. The C17 schema copy is regenerated from the result.

## C. Clause Builder

9. `specifications-global/spec-legal-documents-and-consent.md` and `adr-global/adr-legal-policy-responsibility-acknowledgement-and-clause-builder-architecture.md`: the design of Part 1, section 3.
10. Remove the rule that policies must be published before go-live; onboarding asks only for the responsibility acknowledgement switch. Files: the legal spec, `pol-common-aspects-for-mybizz-anvil-applications.md`, `test-suite/ts-conformance-checks.md`, ticket 40, `GLOSSARY.md`, both design docs and the locked copies B12, B14, B15, B16.
11. Screen requirements: `ClauseBuilder`, `PolicyEditorForm`; `PrivacyPolicyPage`, `TermsConditionsPage` and `CookiePolicyPage` become one `PolicyPage`; `FooterComponent` shows only published policies.
12. Align with the new tables: `custom-component-requirements-matrix.md`, `DESIGN.md`, the SRS, ticket 12, `mb-3-cs-architecture-reference.md`, `adr-local/adr-schema-scope-reduction.md`, the locked copies C17 and C20.

## D. Mybizz Enterprise (common to Mybizz CS and Mybizz Shop)

13. `specifications-global/spec-client-instance-hosting.md`: a section on the dedicated server (Part 1, section 4) — how App 5 sets it up, sizes it, releases to it, backs it up, rebuilds it, and runs the private test copy.
14. `adr-global/adr-automatic-resizing.md`: an Enterprise container has a fixed 8 GiB, outside the 2 GiB automatic limit.
15. `adr-global/adr-tiers-model.md`: Mybizz Enterprise as a plan (Part 1, section 4). Then `adr-fair-use-limits.md`, `adr-mybizz-management-visibility.md` and `spec-observability.md` refer to the plan.
16. `mb-4-ecom-concept.md` and `mb-4-ecom-architecture-report.md`: refer to the common plan instead of describing it.

## E. Referral credit

17. `adr-global/adr-tiers-model.md` and `specifications-global/spec-client-billing.md` section 4.1: the referral credit applies only to the standard annual plan; Mybizz Enterprise takes no part in it.
18. New ADR in `mb-1-fda-project-library/adr-local/`: Mybizz FDA has no annual plan and takes no part in the referral credit, because the margin on a Mybizz FDA client is too small; Mybizz FDA is a tool, a subset of the Mybizz CS and Mybizz Shop platforms.

## F. Project library, marketing and business

19. Merge the Mybizz CS and Mybizz FDA brand profiles into one `data-mybizz-mgt/marketing/mybizz-brand-profile.md` with a section per product.
20. Move the design sections of the brand profiles into each app's `DESIGN.md`; create `DESIGN.md` for Mybizz FDA.
21. Move `mb-3-cs-project-library/docs-local/strategy/positioning-strategy.md` and `pricing-strategy.md` to `data-mybizz-mgt/business/mybizz-cs/`.
22. Check every concept document (`mb-3-cs-concept.md`, `mb-1-fda-concept.md`, `mb-4-ecom-concept.md`) for business or marketing content and move any found.
23. G4.1 and G4.2: point the go-to-market link in `mb-3-cs-concept.md` to `marketing/mybizz-live-marketing-plan.md`; repair every link the moves break (the 11 files that link the brand profiles).
24. G4.3: the brand statement becomes "One platform. One price. Your customers. Your data." in the brand profile.
25. Delete `data-mybizz-mgt/marketing/mybizz-cs-marketing-plan.md`.

## G. PDLF records

26. `pdlf/pdlf-library/docs-local/pdlf-todo.md`: close G4.1 to G4.4; add the master-template items (local currencies, the policy tables, Mybizz Enterprise).
27. PDLF Step 23 (design review) for mb-3-cs app1.

## H. David

28. Resolve in anvil.works after item 8.
29. In claude.ai, set each connector already in use to ask for approval before acting.
