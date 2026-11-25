---
title: "handover-task-list"
doc-id: "mb-4c7e19a2"
updated: "2026-11-25"
---
# Handover Task List — Currency, Clause Builder, Enterprise, Referral Credit, Documentation Homes

The checklist of the work agreed on 2026-11-25 from the handover of the same date. A finished item keeps its place and is prefixed with "Done". Claude does every item except group H. Before each group, Claude lists the group's exact files and changes for David's approval, then pushes the group.

---

## A. Currency: books at the day's exchange rate

1. `project-library-global`: rewrite the books rule in `adr-global/adr-system-currency-selection-and-immutability.md`, `policy-global/pol-common-aspects-for-mybizz-anvil-applications.md` (aspect 11), `specifications-global/spec-integration.md` and `test-suite/ts-catalogue.md`. Each sale is recorded in the customer's currency and in the system currency, converted at the European Central Bank's rate on the day of the sale; the rate used is stored on the record.
2. `mb-3-cs-project-library`: the same rule in `docs-local/GLOSSARY.md`, `mb-3-cs-concept.md`, `mb-3-cs-architecture-reference.md`, `design/app1/design-doc.md`, `design/app1/design-doc-first-concept.md`, `design/app1/test-plan.md`; `docs-standard-local/` BRD, PRD, SRS, `integration-architecture.md`, `scaffold-spec.md`; `legal-local/client-service-agreement.md`; `specifications-local/spec-test-specification.md`; ticket 22; the locked copies B12, B14, B15, B16 and C17.
3. Rewrite six screen requirements to the Local Currencies design: `ui/settings/SettingsForm/CurrencyTab/CurrencyTab-requirement.md` (becomes the Local Currencies tab), `SettingsForm`, `ServiceEditorForm` (local prices from `service_local_prices`), `ServiceViewerForm`, `ServicesPage`, `ServiceDetailPage`.
4. `docs-local/design/app1/access-matrix.yaml` line 360: `DisplayCurrency` becomes `LocalCurrencies` (Owner all, Manager all, every other role none).
5. `mb-4-ecom-project-library`: the same rule in `mb-4-ecom-commerce-schema.md` and `mb-4-ecom-commerce-lifecycles.md`.

## B. Data tables

6. mb-3-cs `authoritative-schema.md` and `schema-migration-log.md`: add `exchange_rate` to `payments`, `invoice` and `orders`; replace `privacy_policy`, `t_and_c` and `cookie_policy` with `policies`, `policy_clauses` and `clause_library`.
7. mb-4-ecom `mb-4-ecom-commerce-schema.md`: the same three policy tables, also replacing `returns_policy` and `delivery_policy`.
8. Apply every outstanding mb-3-cs schema change to `mb-3-cs-app1/anvil.yaml` through the `anvil-yaml` skill: the 2026-11-24 currency migration (`local_currencies`, `service_local_prices`, `package_local_prices`, `currency`, `system_amount`, `tax_amount_system`, removal of `services.display_currency`) and items 6 and 7. The C17 schema copy is regenerated from the result.

## C. Clause Builder

9. `specifications-global/spec-legal-documents-and-consent.md` and `adr-global/adr-legal-policy-responsibility-acknowledgement-and-clause-builder-architecture.md`: one display form for every policy; the client names any new policy; Mybizz's clauses are a read-only library of suggestions the client copies from; every clause in a client's policy can be edited or deleted; policies are optional.
10. Remove the rule that policies must be published before go-live; onboarding asks only for the responsibility acknowledgement switch. Files: the legal spec, `pol-common-aspects-for-mybizz-anvil-applications.md`, `test-suite/ts-conformance-checks.md`, ticket 40, `GLOSSARY.md`, both design docs and the locked copies B12, B14, B15, B16.
11. Screen requirements: `ClauseBuilder`, `PolicyEditorForm`; `PrivacyPolicyPage`, `TermsConditionsPage` and `CookiePolicyPage` become one `PolicyPage`; `FooterComponent` shows only published policies.
12. Align with the new tables: `custom-component-requirements-matrix.md`, `DESIGN.md`, the SRS, ticket 12, `mb-3-cs-architecture-reference.md`, `adr-local/adr-schema-scope-reduction.md`, the locked copies C17 and C20.

## D. Mybizz Enterprise (common to Mybizz CS and Mybizz Shop)

13. `specifications-global/spec-client-instance-hosting.md`: a section on the dedicated server — how App 5 sets it up, sizes it (8 GiB container), releases to it, backs it up, rebuilds it, and runs the private test copy.
14. `adr-global/adr-automatic-resizing.md`: an Enterprise container has a fixed 8 GiB, outside the 2 GiB automatic limit.
15. `adr-global/adr-tiers-model.md`: Mybizz Enterprise as a plan any Mybizz CS or Mybizz Shop client may move up to: £299 a month, £2,990 a year, the move charged at one month's price, once; prices in the other market currencies in the same proportion. Then `adr-fair-use-limits.md`, `adr-mybizz-management-visibility.md` and `spec-observability.md` refer to the plan.
16. `mb-4-ecom-concept.md` and `mb-4-ecom-architecture-report.md`: refer to the common plan instead of describing it.

## E. Referral credit

17. `adr-global/adr-tiers-model.md` and `specifications-global/spec-client-billing.md` section 4.1: the referral credit applies only to the standard annual plan; Mybizz Enterprise takes no part in it.
18. New ADR in `mb-1-fda-project-library` (`adr-local/`): Mybizz FDA has no annual plan and takes no part in the referral credit, because the margin on a Mybizz FDA client is too small. Mybizz FDA is a tool, a subset of the Mybizz CS and Mybizz Shop platforms, not a platform.

## F. Project library, marketing and business

19. Merge the Mybizz CS and Mybizz FDA brand profiles into one `data-mybizz-mgt/marketing/mybizz-brand-profile.md` with a section per product.
20. Move the design sections of the brand profiles (colour, typography, layout, interaction) into each app's `DESIGN.md`; create `DESIGN.md` for Mybizz FDA.
21. Move `mb-3-cs-project-library/docs-local/strategy/positioning-strategy.md` and `pricing-strategy.md` to `data-mybizz-mgt/business/mybizz-cs/`.
22. Check every concept document for business or marketing content and move any found.
23. G4.1 and G4.2: point the go-to-market link in `mb-3-cs-concept.md` to `marketing/mybizz-live-marketing-plan.md`; repair every link the moves break (the 11 files that link the brand profiles).
24. G4.3: the brand statement becomes "One platform. One price. Your customers. Your data." in the brand profile (former lines 23, 168 and 319).
25. Delete `data-mybizz-mgt/marketing/mybizz-cs-marketing-plan.md`.

## G. PDLF records

26. `pdlf/pdlf-library/docs-local/pdlf-todo.md`: close G4.1 to G4.4; add the master-template items (local currencies, the policy tables, Mybizz Enterprise).
27. PDLF Step 23 (design review) for mb-3-cs app1.

## H. David

28. Resolve in anvil.works after item 8.
29. In claude.ai, set each connector already in use to ask for approval before acting.
