---
title: "Mybizz-Live Intl. VAT Handling"
doc-id: "mb-5522c081"
updated: "2026-11-10"
---
# Mybizz-Live Intl. VAT Handling

## B2B, B2C ?

Strictly speaking, **the product intent is B2B (Business-to-Business)**, but **tax authorities do not classify transactions based on what your software does—they classify them based on *who* buys it and whether they provide a verified business tax identity.**

In tax law (UK HMRC, EU VAT, and international tax frameworks), the line between B2B and B2C depends on the customer's **legal tax status at checkout**, not their usage intent.

### 1. The Legal & Tax Reality: "B2B vs B2C"

If an individual buys your app to run a business, they could fall into one of two tax categories:

#### Scenario A: Sole Trader / Self-Employed *With* a Tax/VAT ID

- **Classification:** **B2B**

- **Why:** In most jurisdictions (such as the UK, EU, South Africa, or Australia), a self-employed individual or sole proprietor who has registered their business with their tax authority holds an official Tax Identification Number (TIN) or VAT number.

- **Tax Handling:** Once they enter and validate their Tax ID at checkout, tax systems (like Stripe Tax, Paddle, or Quaderno) recognize them as a business entity. Cross-border EU/UK sales can then apply the **Reverse Charge mechanism** (0% tax on the invoice).

#### Scenario B: Individual / Freelancer *Without* a Registered Tax ID

- **Classification:** **B2C (Consumer)** for tax purposes

- **Why:** Tax authorities assume that if a buyer cannot (or does not) provide a verified corporate/business Tax ID, they are acting as an individual consumer.

- **Tax Handling:** Even if they use your software 100% for business tasks, tax law legally requires you to treat them as a consumer, charge local consumer VAT/sales tax at checkout, and remit it to their home country's tax authority.

### 2. How Your App Architecture Should Handle This

Because you are selling business management software, your target audience is entirely business-minded, but their legal entity status will vary.

To protect your business from tax compliance errors, structure your billing and checkout flow around these best practices:

1. **Always Request a Tax/VAT ID at Checkout:** Add an optional field for *"Company Name & Tax/VAT ID"* during user onboarding or payment checkout.

2. **Use Real-Time Tax ID Validation:**If you use payment platforms like Stripe Tax or Paddle, they automatically query verification databases (like the EU VIES database) when a customer enters a tax ID.
   
   - **If Validated:** The order is processed as **B2B** (triggering Reverse Charge / tax exemption).
   
   - **If Blank or Invalid:** The order is treated as **B2C** and local sales tax/VAT is collected.

3. **Receipting & Expense Invoices:** Even if a sole trader is treated as B2C for tax collection purposes, generate a detailed tax invoice containing their personal name or business trading name so they can still write off your SaaS subscription as a legitimate business expense on their personal income tax return.

### Summary Checklist

| **Customer Profile**                    | **Provided Valid Tax/VAT ID?** | **Tax Status** | **Invoice Treatment**                   |
| --------------------------------------- | ------------------------------ | -------------- | --------------------------------------- |
| **Incorporated Company** (Ltd, LLC)     | Yes                            | **B2B**        | 0% Tax (Reverse Charge / Exempt)        |
| **Registered Sole Trader / Freelancer** | Yes                            | **B2B**        | 0% Tax (Reverse Charge / Exempt)        |
| **Unregistered Individual / Start-up**  | No                             | **B2C**        | Charge Customer's Local VAT / Sales Tax |

Handling Value-Added Tax (VAT), Goods and Services Tax (GST), and Sales Tax across global software sales requires navigating the distinction between **B2B (Business-to-Business)** and **B2C (Business-to-Consumer)** transactions.

When selling a SaaS product cross-border:

- **B2C Sales:** The seller (your company) is almost always responsible for charging, collecting, and remitting local consumption tax at the rate of the *buyer's* country.

- **B2B Sales:** The responsibility usually shifts to the purchasing business under a mechanism called the **Reverse Charge**, allowing you to charge 0% VAT provided you collect and validate their local tax ID.

### Regional Tax Breakdown

```
                  ┌─────────────────────────────────────────┐
                  │          GLOBAL TAX RULES MATRIX        │
                  └────────────────────┬────────────────────┘
                                       │
        ┌──────────────────┬───────────┴───────┬──────────────────┐
        ▼                  ▼                   ▼                  ▼
   [United Kingdom]   [European Union]   [United States]      [Canada]
 ───────┬────────   ───────┬───────   ───────┬───────   ───────┬───────
  • Non-resident threshold:    • Non-resident threshold:    • Economic nexus rules    • Simplified GST/HST
    £0 for B2C SaaS            €0 for B2C (OSS)             vary by state ($100k)       threshold: CAD $30k
  • Standard Rate: 20%       • Member rates (17-27%)    • No federal VAT; state    • Federal + Provincial
  • B2B: Reverse Charge      • B2B: Reverse Charge          sales tax rules apply       blended rates (5-15%)
```

#### 1. United Kingdom (UK)

As a UK Limited Company, the UK is your home corporate jurisdiction.

- **B2C Sales (UK Private Consumers):** You must charge UK VAT (standard rate **20%**). Note that while resident UK businesses have a domestic registration threshold (£90,000), non-resident-owned businesses making digital supplies directly must monitor registration requirements closely.

- **B2B Sales (UK Businesses):** You charge 20% UK VAT on the invoice. The UK buyer reclaims this on their domestic VAT return.

#### 2. European Union (EU)

The EU has strict rules governing cross-border digital services.

- **Non-Resident Threshold:** **€0**. The moment you sell a single subscription to an EU consumer, tax is owed in their country.

- **B2C Sales:** You must charge VAT at the local rate of the *buyer's country* (ranging from 17% in Luxembourg to 27% in Hungary).

- **Do you need 27 separate registrations?** No. You can register for the **EU Non-Union One-Stop Shop (OSS)** portal in a single EU country (e.g., Ireland or the Netherlands). The OSS allows you to file one quarterly return and make one consolidated payment, which the host country redistributes across the EU.

- **B2B Sales:** **0% VAT (Reverse Charge)**. If the EU business provides a valid EU VAT number (verifiable via the EU VIES system), you do not charge VAT. Note their VAT ID on the invoice and state that the *reverse charge mechanism applies*.

#### 3. United States (US)

The US does not have a federal VAT. Instead, sales tax is governed independently by **50 individual states and local municipalities**.

- **Economic Nexus Thresholds:** You are only required to register and collect sales tax in a state once you cross its **economic nexus threshold** (typically **$100,000 in annual revenue** or **200 separate transactions** into that specific state).

- **Taxability of SaaS:** SaaS is not taxed uniformly. Some states (like California) generally do not tax pure cloud SaaS, while others (like New York, Texas, and Pennsylvania) treat SaaS as fully taxable.

- **B2B vs B2C:** Many states tax B2B software transactions unless the purchasing company provides a valid state-specific **Resale or Exemption Certificate**.

#### 4. Canada

Canada levies a combination of federal **GST (Goods and Services Tax)** and provincial taxes (**PST/RST/HST**).

- **Registration Threshold:** Foreign digital sellers must register under Canada's **Simplified GST/HST regime** once worldwide sales of digital products to Canadian consumers exceed **CAD $30,000** over a 12-month period.

- **Rates:** You collect tax based on the customer's province, ranging from **5% GST** (e.g., Alberta) up to **15% HST** (e.g., Nova Scotia) or combined GST+QST (**14.975%** in Quebec).

- **B2B Sales:** Under the simplified scheme, if a Canadian customer provides a valid GST/HST registration number, you do not charge tax.

### Comparison of Global Obligations

| **Region** | **Registration Threshold**                      | **B2C Tax Responsibility**                           | **B2B Tax Handling**                                | **Simplified Registration System**      |
| ---------- | ----------------------------------------------- | ---------------------------------------------------- | --------------------------------------------------- | --------------------------------------- |
| **UK**     | £0 (Non-resident B2C) / £90k domestic threshold | Charge **20% UK VAT**                                | Charge 20% (buyer reclaims)                         | Direct HMRC Registration                |
| **EU**     | **€0** for non-EU/UK sellers                    | Charge buyer's country rate (17–27%)                 | **0% VAT** (Reverse Charge with valid VAT ID)       | **EU One-Stop Shop (OSS)**              |
| **USA**    | **$100,000 / 200 sales** per state              | Charge state/local sales tax (where SaaS is taxable) | Taxable unless buyer provides exemption certificate | State-by-State (or SST Governing Board) |
| **Canada** | **CAD $30,000** rolling 12-month sales          | Charge GST/HST/QST by province (5–15%)               | **0% Tax** if buyer provides GST/HST number         | Simplified CRA GST/HST Registration     |

### Practical Implementation Strategies

Managing cross-border tax compliance manually across hundreds of state and national jurisdictions is technically complex. SaaS companies typically use one of two integration models:

1. **Merchant of Record (MoR) Model (e.g., Paddle, Lemon Squeezy):**
   
   - The MoR acts as the legal reseller of your software.
   
   - They handle 100% of global tax calculation, registration, remittance, and audit compliance across all countries. You receive a net payout.

2. **Automated Tax Engines (e.g., Stripe Tax, TaxJar, Anvil/Custom API Integrations):**
   
   - Your business remains the direct merchant.
   
   - The tax engine dynamically calculates the exact tax rate at checkout based on buyer IP/billing address, collects tax numbers for B2B validation, tracks your proximity to state/national thresholds, and outputs formatted filing reports.



## Stripe Tax

Using **Stripe Tax** to handle VAT, GST, and US Sales Tax for your UK-based SaaS company is one of the cleanest ways to automate compliance. However, there is a fundamental distinction between how Stripe Tax operates versus a **Merchant of Record (MoR)** (like Paddle or Lemon Squeezy).

### 1. Does Stripe Tax Pay the Tax Over for You? (Crucial Distinction)

Your intuition that VAT is a "straight-through" tax (collected from the customer and passed to the government) is correct in spirit. **However, Stripe Tax does NOT automatically remit (pay over) the money to tax authorities on your behalf.**

- **What Stripe Tax DOES:**
  
  - It detects where your customer is located (via IP, billing address, or card issuer).
  
  - It validates B2B VAT IDs in real-time (applying 0% Reverse Charge when valid).
  
  - It applies the exact tax rate to the checkout total (e.g., 20% in the UK, 21% in Spain, GST in Canada).
  
  - It tracks your revenue against registration thresholds in all 50 US states, Canada, the EU, and the UK, alerting you when you need to register.
  
  - It generates line-by-line tax reports formatted for filing.

- **What YOU (or an Agent) MUST DO:**
  
  - You must submit the tax registrations in the respective regions (or use a service to register you).
  
  - You must take the aggregated tax collected in your Stripe balance and **file/pay it over** to HMRC (UK), the EU One-Stop Shop (OSS), the Canadian Revenue Agency (CRA), and individual US states.
  
  - *(Note: Stripe offers partner integrations with tax filing services like Taxually or Marosa directly in your dashboard if you want automated filing for an extra fee).*

### 2. Stripe Tax Pricing & Operational Costs

Stripe Tax has a separate usage fee on top of standard payment processing fees.

#### A. Stripe Tax Specific Fees

- **0.5% per transaction** where tax is collected.

- *Alternative Threshold pricing:* 0.4% per transaction if you commit to high volume, or pay-as-you-go.

- *Note:* You are only charged the 0.5% fee on transactions where you have added an active tax registration location in your Stripe dashboard.

#### B. The Complete Transaction Fee Breakdown (Example for a $100 SaaS Sale)

Because your company is incorporated in the UK, your standard Stripe processing stack for an international card (e.g., a US buyer paying $100) will look like this:

| **Fee Component**                      | **Estimated Rate**                        | **Cost on a $100 USD Sale** |
| -------------------------------------- | ----------------------------------------- | --------------------------- |
| **Base UK Processing Fee**             | ~1.5% + £0.20                             | $1.70                       |
| **International Card Fee**             | +1.5%                                     | $1.50                       |
| **Stripe Tax Fee**                     | **+0.5%**                                 | **$0.50**                   |
| **FX Conversion (if settling in GBP)** | +1.0% *(0% if paid directly to Wise USD)* | $1.00 *(or $0.00)*          |
| **Total Stripe Overhead**              | **~3.5% – 4.5%**                          | **$3.70 – $4.70**           |

*(Compare this to a Merchant of Record like Paddle, which charges a flat ~5% + $0.50, but handles 100% of the filing and remittance for you).*

### 3. How Stripe Tax Handles Your Key Regions

```
               ┌─────────────────────────────────────────────────────────┐
               │                  STRIPE TAX AUTOMATION                  │
               └────────────────────────────┬────────────────────────────┘
                                            │
        ┌───────────────────┬───────────────┴───────┬──────────────────┐
        ▼                   ▼                       ▼                  ▼
   [United Kingdom]    [European Union]       [United States]      [Canada]
 ───────┬────────   ────────┬───────       ───────┬───────   ───────┬───────
  • Rates: 20%        • Rates: 17–27%        • Rates: 0–10%     • Rates: 5–15%
  • Home country      • Uses EU OSS          • Tracks state     • Simplified GST
  • Collect & remit     (1 registration)       economic nexus     scheme (CAD $30k)
```

1. **United Kingdom (Home Base):**
   
   - **Setup:** Add your UK VAT registration details to Stripe Tax.
   
   - **Handling:** Stripe charges 20% VAT on all UK B2C and non-exempt B2B sales. You download the quarterly summary from Stripe and file it on your HMRC portal.

2. **European Union (EU):**
   
   - **Setup:** Register for the **EU Non-Union One-Stop Shop (OSS)** scheme in one EU country (e.g., Ireland). Input your OSS number into Stripe Tax.
   
   - **B2C Handling:** Stripe automatically applies the customer's local rate (e.g., 19% in Germany, 21% in Spain) based on their IP/address at checkout.
   
   - **B2B Handling:** When an EU business inputs a valid VAT ID, Stripe validates it live via VIES and applies a **0% Reverse Charge**. You collect €0 tax, but the transaction is recorded properly.

3. **United States:**
   
   - **Setup:** You do **not** collect tax immediately in every state.
   
   - **Handling:** Stripe Tax runs a **Threshold Monitor** in the background. It tracks your gross sales into each state. When you hit a state's economic nexus limit (typically $100,000 or 200 transactions), Stripe sends an alert telling you it is time to register and turn on collection in that state.

4. **Canada:**
   
   - **Setup:** Stripe monitors the CAD $30,000 digital threshold.
   
   - **Handling:** Once crossed, you register under the Simplified CRA GST/HST scheme and enter the ID into Stripe. Stripe then charges between 5% and 15% depending on whether the customer is in Alberta (5%), Ontario (13%), etc.

### Summary Checklist for Getting Started

1. Go to **Stripe Dashboard $\rightarrow$ Tax $\rightarrow$ Registrations**.

2. Add your **UK VAT ID** (or turn on monitoring if you haven't hit registration limits).

3. Set your **Default Product Tax Code** in Stripe to **`txcd_10000000` (Digital Goods - Software as a Service)** so Stripe knows your product is intangible software.

4. Enable **Stripe Tax on Checkout / Invoices**.

5. Set a calendar reminder at the end of each quarter to export the **Stripe Tax Location Reports** to hand to your accountant or submit via government portals.
   
   

## Stripe Tax with Taxually or Marosa

While **Stripe Tax** handles calculating and collecting sales tax, VAT, and GST at checkout, **it does not automatically file or remit your taxes in most international jurisdictions**.

To bridge this gap, Stripe integrates with specialized third-party tax filing software partners—primarily **Taxually** and **Marosa**—via the **Stripe App Marketplace**. These apps pull transaction data directly from your Stripe account to handle multi-jurisdictional registrations, return preparation, and government submissions.

### How the Ecosystem Works

```
┌────────────────────────────────┐
│          STRIPE TAX            │  Calculates, collects & tracks thresholds
└───────────────┬────────────────┘  (UK, EU, US, Canada, etc.)
                │
                │  Auto-syncs transactional tax data
                ▼
┌────────────────────────────────┐
│  Taxually  or  Marosa App      │  Fires up registrations & prepares returns
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│   Tax Authorities (HMRC,       │  Automated submission & payment routing
│   EU OSS, CRA, US States)      │
└────────────────────────────────┘
```

### 1. Taxually (Official Stripe Partner)

Taxually is Stripe’s primary native integration partner for global tax registrations and filings. When you request non-US tax registrations directly from the Stripe Dashboard ("Register for me"), Stripe routes the request behind the scenes to Taxually.

- **How it integrates:** You install the **Taxually for Stripe** app. It automatically ingests sales totals, tax collected, customer locations, and exemption IDs from your Stripe Tax reports.

- **Key Capabilities:**
  
  - **EU Non-Union OSS:** Registers your UK Ltd for the EU One-Stop Shop portal, prepares the quarterly return, and submits it to the selected EU member state.
  
  - **UK HMRC & Canada CRA:** Prepares and files statutory VAT/GST returns in the UK, Canada, Australia, and other global regions.
  
  - **Automated Returns:** Generates pre-populated tax return forms so you can review and submit with one click.

- **Best Suited For:** Growing digital SaaS startups looking for a streamlined, self-serve interface that plugs into Stripe with minimal setup.

### 2. Marosa

Marosa is an established European indirect tax software provider with a dedicated app in the Stripe App Marketplace. It is geared toward companies operating across Europe and non-EU jurisdictions that require end-to-end VAT management alongside human tax advisory.

- **How it integrates:** Installs directly inside your Stripe Dashboard. It embeds dedicated compliance dashboards where you can view pending returns, approve filings, and track tax liabilities by country without leaving Stripe.

- **Key Capabilities:**
  
  - **Dashboard Integration:** Allows you to review, approve, and monitor filing status directly within the Stripe UI.
  
  - **Intrastat & SAF-T Reporting:** Beyond standard VAT returns, Marosa handles complex European reporting requirements (such as SAF-T files and EC Sales lists).
  
  - **Dedicated Human Support:** Bundles access to dedicated tax specialists who review returns and handle local tax authority correspondence.

- **Pricing Model:** Uses structured monthly/annual compliance plans based on monthly transaction volume and filing locations (e.g., plans starting around €350–€400/month for up to 6 registrations and 1,200 monthly transactions).

- **Best Suited For:** Companies with higher transaction volumes, multiple local VAT registrations across individual EU states, or complex reporting requirements that require dedicated tax advisor backing.

### 3. Comparison: Taxually vs. Marosa

| **Feature / Aspect**        | **Taxually**                                                       | **Marosa**                                                                  |
| --------------------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| **Stripe Ecosystem Status** | Primary default registration partner within Stripe.                | Marketplace App partner.                                                    |
| **UI Integration**          | Standalone web app connected via Stripe API.                       | Embedded dashboard view directly inside the Stripe app UI.                  |
| **Target Audience**         | Early-to-mid stage SaaS & digital sellers needing global coverage. | Mid-to-enterprise businesses needing EU VAT reporting and dedicated advice. |
| **Human Tax Advisory**      | Primarily self-serve automated filings with platform support.      | Full human tax advisor access bundled into compliance plans.                |
| **Key Regions Covered**     | Global (EU OSS, UK, Canada, Australia, US).                        | Strong emphasis on EU-27, UK, and European non-EU states.                   |

### What You Can Expect to Pay (Total Cost Breakdown)

Using this stack for your UK Ltd selling globally involves three cost components:

1. **Stripe Tax Collection Fee:** **0.5% per transaction** where tax is calculated/collected.

2. **Filing Software Subscription (Taxually or Marosa):**
   
   - **Taxually:** Typically charges a fee per return filed (or a monthly plan based on active regions, starting around £40–£100/month depending on number of countries).
   
   - **Marosa:** Subscription plans start at ~€350/month for multi-country registrations and returns.

3. **The Actual Tax Collected (Pass-Through):** Collected from the customer at checkout and remitted via the platform to the tax authority.



## Stripe & Taxually vs. Paddle

Choosing between **Paddle (Merchant of Record)** and **Stripe Tax + Taxually (DIY Direct Merchant)** comes down to a trade-off between **financial cost vs. operational labor and legal liability**.

### 1. The Core Architectural Difference

- **Paddle (Merchant of Record):** Paddle acts as the legal reseller of your software. Your customer buys from Paddle; Paddle collects the money, assumes 100% of the indirect tax liability, files returns globally, and pays out your net earnings.

- **Stripe Tax + Taxually (Direct Merchant):** Your UK Ltd is the legal seller. Stripe Tax calculates and collects the correct tax at checkout. Taxually pulls that data to prepare filings. **You (or Taxually on your behalf) must hold the tax registrations and pay the money over to government tax portals**.

### 2. Comprehensive Cost Breakdown

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ESTIMATED ALL-IN COST MATRICES                  │
├───────────────────────┬────────────────────────────────────────────────┤
│ Stack                 │ Total Estimated Overhead Rate                  │
├───────────────────────┼────────────────────────────────────────────────┤
│ Paddle (All-In)       │ 5% + $0.50 flat per transaction (FX fees extra)│
├───────────────────────┼────────────────────────────────────────────────┤
│ Stripe Tax + Taxually │ ~4.1% – 5.5% per sale + £40–£120/mo fixed software│
└───────────────────────┴────────────────────────────────────────────────┘
```

#### Option A: Paddle Pricing Model

- **Transaction Fee:** A flat **5% + $0.50** per successful checkout transaction.

- **Included Services:** Payments processing, subscription engine (Paddle Billing), fraud prevention, chargeback defense, VAT/GST tax calculation, global tax registrations, and end-to-end tax filings.

- **FX / Currency Markup:** ~2% on foreign currency conversion payouts.

- **Fixed Monthly Overhead:** **$0** (No base subscription fees).

#### Option B: Stripe Tax + Taxually Pricing Model

Stripe’s stack uses modular add-on pricing:

1. **Stripe Payments Base Fee:** ~1.5% + £0.20 (UK/EU cards) or ~2.9% + £0.20 (International cards).

2. **Stripe Billing Add-on:** **+0.7%** of billing volume (for managing subscription renewals and proration).

3. **Stripe Tax Add-on:** **+0.5%** per transaction where tax is calculated.

4. **Taxually Subscription (Filings):** Fixed monthly fee depending on regions active (e.g., ~£40–£120/month for UK VAT, EU OSS, and Canada CRA returns).

5. **Effective Variable Cost per Sale:** **~3.5% to 4.5%** per transaction + the fixed monthly Taxually fee.

### 3. Effort & Operational Load Comparison

| **Operational Area**       | **Paddle (Merchant of Record)**                                                                            | **Stripe Tax + Taxually**                                                                                                                 |
| -------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Tax Registration Setup** | **Zero Effort:** You register zero tax entities. Paddle operates using its own global tax registrations.   | **Moderate Effort:** You must apply for a UK VAT ID, EU Non-Union OSS ID, and Canadian CRA ID in your company's name.                     |
| **Filing & Remittance**    | **Zero Effort:** Paddle handles all quarterly/annual filings and remits money directly to tax authorities. | **Low-to-Medium Effort:** Taxually auto-generates returns, but you must review, approve, and authorize payments out of your bank account. |
| **Tax Audit Liability**    | **Assumed by Paddle:** If an EU state audits a transaction, Paddle defends it legally.                     | **Assumed by You:** Your UK company carries ultimate audit liability for tax accuracy.                                                    |
| **Checkout & DX Polish**   | **Good:** Standard hosted or inline pop-up checkout experience.                                            | **Industry Standard:** Full control over Stripe Elements, APIs, native custom UI, and deep developer documentation.                       |
| **Customer Invoicing**     | Paddle issues invoices under its name ("Paddle.com Market Ltd").                                           | Invoices are issued directly under your UK Ltd name.                                                                                      |

### 4. Which Stack Should You Choose?

#### Choose **Paddle** if:

- **You want zero tax admin:** You operate as a solo founder or lean team and do not want to manage individual foreign tax registrations, tax portal logins, or multi-currency filings.

- **You have a lower transaction count at higher ACV:** On a $50/month or $100/month SaaS tier, Paddle's flat 5% + $0.50 is predictable, eliminating fixed monthly accounting overhead.

#### Choose **Stripe Tax + Taxually** if:

- **You want direct control & native branding:** You want invoices issued strictly under your company's legal name, or you rely on Stripe's developer SDKs and API capabilities.

- **You want lower transaction fees at higher scale:** Once your monthly revenue crosses $15k–$20k MRR, the lower variable fees of Stripe (~3.5%–4% vs Paddle's 5%) more than offset Taxually's fixed monthly software subscription.
