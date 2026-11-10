---
title: "Mybizz-Live Banking (UK)"
doc-id: "mb-e56ee453"
updated: "2026-11-10"
---
Mybizz-Live Money (UK)

## Banking Options for Non-Resident Founders

As a non-resident running a digital SaaS business, your best options are **Electronic Money Institutions (EMIs)** or digital banking providers that issue local UK Sort Codes and Account Numbers:

### Top Digital Banking Options

1. **Wise Business (Formerly TransferWise)**
   
   - **Best For:** International SaaS revenue, multi-currency hold/exchange (GBP, USD, EUR), and low FX fees.
   
   - **Setup:** Done 100% online. One-time setup fee (~£45) with no ongoing monthly maintenance fees.
   
   - **Requirements:** Certificate of Incorporation, passport, non-UK proof of address (utility bill/bank statement under 3 months old), and description of your SaaS model.

### Top Digital Banking Options

1. **Wise Business (Formerly TransferWise)**
   
   - **Best For:** International SaaS revenue, multi-currency hold/exchange (GBP, USD, EUR), and low FX fees.
   
   - **Setup:** Done 100% online. One-time setup fee (~£45) with no ongoing monthly maintenance fees.
   
   - **Requirements:** Certificate of Incorporation, passport, non-UK proof of address (utility bill/bank statement under 3 months old), and description of your SaaS model.

2. **Revolut Business (UK)**
   
   - **Best For:** Fast account setup, automated accounting integrations (Xero/QuickBooks), and team corporate cards.
   
   - **Setup:** Online application; approves eligible non-resident applications quickly (often within 24–48 hours). Monthly plans range from free to paid tiers.
   
   - **Requirements:** UK Ltd registration documents, director identity verification, and proof of non-UK residency.

3. **Airwallex / Payoneer**
   
   - **Best For:** Global payout routing and integrating directly with merchant processors like Stripe/PayPal for SaaS subscriptions.



For a UK-incorporated SaaS business using **Stripe** to bill international subscribers, both **Wise Business** and **Revolut Business** work well, but they serve different operational priorities.

The key distinction lies in **FX fee mechanics, Stripe payout architecture, and team expense scaling**.

## 1. Summary Verdict

| **Metric / Priority**          | **Wise Business**                                                    | **Revolut Business**                                                  | **Winner**                   |
| ------------------------------ | -------------------------------------------------------------------- | --------------------------------------------------------------------- | ---------------------------- |
| **Pricing Model**              | Single £45 setup fee; **no monthly subscription**.                   | Monthly plan tiers (Basic £10/mo, Grow £30/mo, Scale £90/mo).         | **Wise** (for low overhead)  |
| **Stripe FX Avoidance**        | Direct local sort codes in USD, EUR, GBP, AUD, CAD, SGD.             | Multi-currency local details in GBP, EUR, USD, and 25+ currencies.    | **Tie**                      |
| **Foreign Exchange (FX)**      | True mid-market rate + 0.33%–0.5% variable fee. 24/7 static pricing. | Interbank rate within plan monthly allowances. **1% weekend markup**. | **Wise** (predictability)    |
| **API & Automation**           | **Free open API access** on all accounts.                            | API access restricted to paid tiers (Grow and higher).                | **Wise** (for tech/SaaS)     |
| **Corporate Cards & Controls** | Basic virtual/physical cards; simple spend limits.                   | Advanced controls, virtual cards per service, receipt auto-matching.  | **Revolut** (for team scale) |

## 2. Stripe Integration & FX Avoidance

When selling SaaS globally through Stripe, **Stripe charges a steep 2% FX conversion fee** if it converts customer currencies into your UK GBP bank account before payout.

To eliminate Stripe’s conversion fee:

1. Open a USD bank account inside Wise or Revolut.

2. Add those local routing/account numbers into your **Stripe Payout Settings** under *Manage Payout Currencies*.

3. Pay out USD customer subscriptions directly into your USD balance, EUR into EUR, and GBP into GBP.

### How They Compare on Stripe Payouts:

- **Wise Business:** Provides true domestic US routing and account numbers (ACH), SEPA IBANs for EUR, and local UK Sort Codes. Stripe recognizes Wise accounts as native local accounts, allowing **0% FX payout fees** from Stripe.

- **Revolut Business:** Provides local UK Sort Codes and SEPA IBANs. US routing details are available, but depend on Revolut’s US partner bank setup.

## 3. Deep Dive: Wise vs. Revolut

### Choose **Wise Business** if:

- **You want zero recurring subscription costs:** Pay a one-time ~£45 setup fee and pay only when you transfer or exchange funds.

- **You want predictable FX fees:** Wise uses the mid-market exchange rate 24/7 without weekend markups.

- **You need custom developer API access:** Wise provides full access to its webhooks and payout APIs on every account at no extra charge—ideal for automating SaaS vendor payouts or partner affiliate payouts directly from your application code.

- **You have a lean or solo team:** You don't need complex internal spend approvals, purchase order matching, or multi-user card issuing.

### Choose **Revolut Business** if:

- **You operate a distributed team with software expenses:** Revolut allows you to issue virtual debit cards instantly to employees or set up dedicated single-use cards for SaaS vendor subscriptions (AWS, GitHub, Google Cloud) with hard spend limits.

- **You want automated expense & receipt matching:** Team members take photos of receipts in the mobile app, and Revolut automatically matches them to card transactions and syncs with Xero or QuickBooks.

- **You process large monthly FX volumes:** If you subscribe to higher plans (e.g., Grow or Scale), your plan includes fee-free interbank exchange allowances during market hours.



By default, if your UK entity accepts non-GBP payments (such as USD or EUR), Stripe automatically converts those funds into GBP at its standard foreign exchange (FX) fee (typically 2%) before paying out to your main UK bank account.

To avoid this, you can configure **Multi-Currency Payouts** in Stripe using your Wise Business multi-currency account details. This allows USD to settle natively into a USD balance, EUR into EUR, and GBP into GBP—completely bypassing Stripe's auto-conversion.

## Step 1: Obtain Currency Account Details from Wise

Log into your **Wise Business** dashboard:

1. Under your balances, open or activate the specific currency account balances you need (e.g., **USD**, **EUR**, **GBP**).

2. Click on each currency balance to view its dedicated domestic routing details:
   
   - **USD:** Wire / ACH Routing Number and Account Number (issued via Wise's US banking partner).
   
   - **EUR:** Eurozone IBAN (starting with `BE` or `LU`).
   
   - **GBP:** UK Sort Code and 8-digit Account Number.

## Step 2: Add Wise Bank Accounts to Stripe

Log into your **Stripe Dashboard**:

1. Go to **Settings** (gear icon) $\rightarrow$ **Business Settings** $\rightarrow$ **Bank accounts and currencies** (or **Payout Settings**).

2. Under the *Bank Accounts* section, click **+ Add bank account**.

3. Add each currency account separately:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ADDING CURRENCY ACCOUNTS                        │
├──────────────┬───────────────────┬─────────────────────────────────────┤
│ Currency     │ Select Country    │ Enter Details from Wise             │
├──────────────┼───────────────────┼─────────────────────────────────────┤
│ USD Payouts  │ United States     │ USD ACH Routing & Account Number    │
│ EUR Payouts  │ Belgium / Single  │ Eurozone IBAN (BE...)               │
│              │ Euro Area (SEPA)  │                                     │
│ GBP Payouts  │ United Kingdom    │ UK Sort Code & Account Number       │
└──────────────┴───────────────────┴─────────────────────────────────────┘
```

> **Important for USD Setup:** When adding the USD bank account on a UK Stripe account, set the bank location country to **United States** so Stripe accepts the domestic ACH routing number provided by Wise.

## Step 3: Configure Multi-Currency Payout Rules

Once the bank accounts are linked to Stripe:

1. In **Settings** $\rightarrow$ **Bank accounts and currencies**, ensure **Multi-currency settlement** is enabled.

2. Set each corresponding account as the default payout target for that specific currency:
   
   - USD Stripe Balance $\rightarrow$ Wise USD Account
   
   - EUR Stripe Balance $\rightarrow$ Wise EUR Account
   
   - GBP Stripe Balance $\rightarrow$ Wise GBP Account

## How Money Flows & How to Save

```
[Customer Pays USD] ──> [Stripe USD Balance] ──> [Wise USD Account (0% Stripe FX)] ──> [Wise Mid-Market Conversion to GBP (0.33%-0.5%)]
```

1. **Stripe collects $100 USD:** Funds flow straight to your USD balance on Stripe.

2. **Payout to Wise:** Stripe transfers $100 directly to your Wise USD account without converting it.

3. **Wise Currency Exchange:** You can hold the USD in Wise to pay software vendors in USD (AWS, GitHub, Google) with zero FX fees, or convert USD to GBP inside Wise at the true mid-market rate (~0.33%–0.5% fee vs. Stripe’s 2%).
