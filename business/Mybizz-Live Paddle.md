---
title: "Mybizz-Live Paddle"
doc-id: "mb-930d5107"
updated: "2026-11-10"
---
# Mybizz-Live Paddle

1. **Paddle is NOT an App Store or Marketplace:** There is no "Paddle App Marketplace" where customers go to browse or download software (like Apple’s App Store, Google Play, or Shopify App Store). Paddle does not host, list, or market your software. Your app stays 100% on your domain, on your servers, built your way.

2. **Paddle is NOT a standard Payment Gateway:** A gateway (like Stripe, PayPal, or Payfast) simply moves money from point A to point B under *your* business name. Paddle operates under a completely different legal model called a **Merchant of Record (MoR)**.

### Why the "Merchant of Record" (MoR) Model Conflicts With Your Goals

You mentioned: *"I don't want transactions with my company to be under the banner of Paddle... I want my customers to be dealing with my company."*

This requirement touches the exact point of how an MoR works. **Under legal and financial regulations, it is impossible for Paddle to act as an MoR without their legal name appearing on the transaction.**

#### How the Law Works when using an MoR:

- **The Legal Reseller Chain:** Legally, when a customer buys your subscription, **your UK Ltd sells the software to Paddle, and Paddle instantly resells it to your end customer**.

- **Why the 5% + $0.50 Fee Exists:** The only reason Paddle is legally allowed to take care of 100% of your global VAT, EU OSS, Canadian GST, and US Sales Tax filings is **because THEY are the legal seller of record**. Governments demand tax from whoever's name is on the receipt.

- **What the Customer Sees:**
  
  - **On the Checkout Screen:** The overlay will display branding like *"Powered by Paddle"* or *"PADDLE.NET * YOURAPPNAME"*.
  
  - **On Credit Card Statements:** The transaction charge will read `PADDLE.NET * [YOURAPP]`.
  
  - **On the Invoices/Receipts:** The official tax invoice sent to your user will state *"Paddle.com Market Ltd"* as the vendor of record.

### What You CAN and CANNOT Customize with Paddle

If you use Paddle, your core SaaS product, code, database, and business structure remain 100% yours. You do not structure your business according to Paddle. However, at the checkout layer, the relationship works like this:

| Feature                                                | Can You Do It with Paddle? | How It Works                                                                        |
| ------------------------------------------------------ | -------------------------- | ----------------------------------------------------------------------------------- |
| **Keep your app on your own domain**                   | **YES**                    | You embed Paddle's overlay checkout (`paddle.js`) seamlessly inside your website.   |
| **Brand the checkout window**                          | **YES (Partial)**          | You put your logo, app colors, and pricing tiers inside the overlay window.         |
| **Hide Paddle's name on credit card bills**            | **NO**                     | The bank descriptor legally must show Paddle's name (e.g., `PADDLE.NET * YOURAPP`). |
| **Issue official VAT invoices under your UK Ltd name** | **NO**                     | Tax invoices are legally issued by Paddle.com Market Ltd.                           |
| **Handle standard customer service yourself**          | **YES**                    | You handle 100% of product support, onboarding, and app features.                   |

### Summary & Decision Point

If your absolute primary requirement is that **your UK Ltd's name must appear on the credit card statement, bank descriptor, and official customer tax invoice**, **Paddle is legally unsuitable for your business**.

- **If you choose Paddle:** You trade away brand exclusivity on the bank statement/invoice in exchange for Paddle taking 100% of global tax liability, registration, and remittance off your hands.

- **If you insist on your UK Ltd being the direct merchant:** You cannot use an MoR. You must use a standard payment gateway (like Stripe or Adyen), where your company name is front-and-center everywhere, but your UK Ltd must take on direct tax registration and compliance obligations.



Paddle issues and sends the invoice to your customer directly.

You do **not** generate the invoice, write it up, or send it out yourself.

### How the Invoicing Process Works in Practice

1. **Automatic Delivery:** Whenever a customer buys a subscription or automated renewal payment occurs, **Paddle generates the PDF invoice and emails it straight to your customer’s inbox** on your behalf.

2. **What the Invoice Looks Like:**
   
   - **Seller Name:** It explicitly states **Paddle.com Market Ltd** (or *Paddle Payments*) as the vendor of record.
   
   - **Product Name:** It displays your product name (e.g., *"Subscription to [Your App Name]"*).
   
   - **Tax Registration:** It includes **Paddle’s tax numbers** (their UK VAT ID, EU OSS ID, etc.).
   
   - **Your Logo:** Paddle allows you to add your brand logo to the header of their receipt templates so it looks familiar to your user.

### What This Means for Your Workflow

- **You do zero invoicing work:** You don't need accounting software (like Xero or QuickBooks) to create individual customer tax invoices. Paddle creates, stamps, sends, and archives them legally.

- **Customer Support for Invoices:** If a customer contacts you asking, *"Can I get a copy of my tax invoice for my accountant?"*, you can either direct them to click the link inside their email from Paddle or send them a link to Paddle's self-serve buyer portal, where Paddle retrieves it for them.

- **B2B Tax Adjustments:** If an enterprise client needs to add their VAT/Tax number to an invoice after purchasing, they click a link directly on Paddle's invoice email to enter their tax ID, and **Paddle automatically reissues the corrected tax receipt**.



From your customers' perspective, dealing with a SaaS app that uses **Paddle** as the Merchant of Record feels **completely standard, professional, and familiar**.

In the modern B2B and consumer software industry, thousands of well-known applications (such as Framer, MacPaw, Raycast, and Setapp) use Merchant of Record models. Most buyers won't even realize a third-party reseller is involved—they will simply view it as your app's secure checkout process.

### How Customers Will Perceive Each Touchpoint

```
[ Your Website / App ] ──> [ Paddle Overlay Checkout ] ──> [ Bank Statement / Email Invoice ]
    (100% Your Brand)         (Your Logo + Secure Badge)        ("PADDLE.NET * YOURAPP")
```

#### 1. The On-Site Checkout Experience

- **Perception:** Seamless and trustworthy.

- **What they see:** When a customer clicks *"Upgrade"* or *"Subscribe"* inside your app, a clean modal window pops up. It features your app's logo, colors, and subscription details. At the bottom, a small tag reads *"Secured by Paddle"* or *"Merchant of Record: Paddle"*.

- **Customer mindset:** Buyers are accustomed to seeing payment security badges (like *"Powered by Stripe"* or *"Secured by Paddle"*). It reassures them that their credit card details are being handled by a certified, PCI-compliant payment infrastructure rather than stored directly on a small company's server.

#### 2. Credit Card & Bank Statements

- **Perception:** Identifiable, though slightly formal.

- **What they see:** The line item on their online banking app or credit card statement usually reads:`PADDLE.NET * YOURAPPNAME` or `PADDLE.COM * YOURAPP`

- **Customer mindset:** Because your app's name is right there in the descriptor, customers instantly recognize the charge. It prevents "unrecognized transaction" confusion or accidental chargebacks.

#### 3. PDF Receipts and Tax Invoices

- **Perception:** Highly professional and compliance-ready (especially for B2B buyers).

- **What they see:** The automated email receipt arrives with your logo in the header. The legal seller fine print lists *Paddle.com Market Ltd* alongside an official UK VAT registration number, complete line-item breakdown, and localized tax calculations.

- **Customer mindset:**
  
  - **For Individual / Consumer Buyers:** They simply treat it as an ordinary digital receipt and save it to their records.
  
  - **For Business / B2B Buyers:** This is actually a **major advantage**. Business clients (especially in Europe, the UK, or North America) require valid VAT/Tax invoices to claim software as a business expense. Paddle’s invoices are 100% tax-compliant globally out of the box, allowing business accounting departments to process them without hassle.

### Potential Friction Points (and How to Handle Them)

While customer perception is overwhelmingly positive, there are two minor scenarios to be aware of:

| **Potential Scenario**         | **Customer Reaction**                                                                                               | **How It's Easily Handled**                                                                                                                                                                                                               |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enterprise B2B Procurement** | A corporate client's finance team asks, *"Why does the invoice say Paddle.com instead of [Your Company Name] Ltd?"* | You simply explain: *"Paddle is our authorized global reseller and Merchant of Record. They handle our international billing and tax compliance."* Corporate accounting teams handle MoR invoices daily and understand this instantly.    |
| **Self-Serve Tax ID Edits**    | A business customer forgot to enter their company VAT number at checkout and needs it added to their invoice.       | Paddle provides a self-serve button directly on the invoice email (*"Add VAT / Tax ID"*). The customer clicks it, enters their number, and Paddle immediately reissues an updated B2B invoice without requiring your manual intervention. |

### The Verdict

Using Paddle does **not** make your business look smaller or third-party dependent. On the contrary, it gives a solo founder or lean startup the instant appearance of a **globally compliant, enterprise-ready software company** that effortlessly accepts local payment methods, issues valid tax invoices in dozens of currencies, and secures customer payment data.



From a User Experience (UX) perspective, comparing **Paddle Checkout** and **Stripe Elements** comes down to **managed drop-in convenience versus total custom control**.

While both support localized pricing, smooth mobile interactions, and standard payment methods, their architectural approach creates distinct differences in flow, visual customization, and customer friction.

### UX Breakdown: Paddle Checkout vs. Stripe Elements

| **UX Attribute**             | **Paddle Checkout**                                                                                 | **Stripe Elements**                                                        |
| ---------------------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **UX Model**                 | **Hosted Modal / Overlay (Turnkey)**                                                                | **Embedded UI Component (API-Native)**                                     |
| **Visual Customization**     | Moderate (Logo, primary color, button styling, dark/light theme).                                   | **Absolute** (Custom CSS/JS, fonts, border-radius, micro-animations).      |
| **Domain & Context**         | Renders as an overlay frame atop your page or redirects to a Paddle URL.                            | Embedded directly into your HTML form; customer **never leaves your DOM**. |
| **Address & Tax Collection** | **Mandatory upfront collection** (Postal code & country strictly enforced for VAT/Tax calculation). | **Flexible** (Collect only what you require; optional tax engine hooks).   |
| **Payment Methods**          | Auto-detects local methods (Cards, PayPal, Apple Pay, Google Pay, iDEAL).                           | Auto-detects 40+ methods (Cards, Apple Pay, Klarna, ACH, SEPA, Link).      |
| **Receipt & Invoicing Flow** | Automated system email sent by Paddle.com with instant B2B tax edit links.                          | Customizable native email receipts or webhook-triggered custom PDFs.       |

### 1. The Checkout Flow & Layout

#### Paddle (Overlay / Hosted Model)

- **How it Feels:** When a user clicks *"Subscribe"*, a lightbox overlay pops up over your screen (or opens as a dedicated hosted page).

- **The UX Benefit:** It creates a focused, distraction-free "checkout zone" without taking the user away from your app entirely.

- **The UX Friction:** Because Paddle is the Merchant of Record, it **must collect the buyer's billing country and postal code before displaying the final price** so it can calculate precise localized VAT/sales tax. This adds 1 extra step/field upfront compared to simple card-only checkouts.

#### Stripe Elements (Native Embedded Model)

- **How it Feels:** Card inputs, Apple Pay buttons, and address fields are rendered as native inputs right inside your page's existing form layout.

- **The UX Benefit:** Zero contextual break. The user feels like they are interacting strictly with your single application window, resulting in slightly higher baseline conversion rates for minimalist checkouts.

- **The UX Friction:** You must build and design the surrounding layout yourself (handling field focus, error states, and responsive resizing).

### 2. Localization & Payment Methods

Both platforms excel at international checkout UX, but handle defaults differently:

- **Currency & Language:** Both automatically detect the buyer's browser locale to present local currency pricing and translated text labels.

- **Digital Wallets (Apple Pay / Google Pay):**
  
  - **Stripe Elements** renders Express Checkout buttons dynamically at the very top of your checkout form if the browser supports them.
  
  - **Paddle** offers one-click Express Checkout buttons inside its overlay, but also natively integrates **PayPal**, which is a high-converting option in markets like Germany and parts of Europe where credit card usage is lower.

### 3. B2B & Tax UX (Crucial for Business Apps)

If your app sells to businesses (B2B), tax validation UX is a major factor:

```
[Paddle B2B UX]   ──> Customer enters EU VAT ID ──> Validates & removes VAT instantly on receipt.
[Stripe B2B UX]   ──> Requires custom UI field   ──> Passes ID to Stripe Tax API ──> Recalculates total.
```

- **Paddle's Native B2B Flow:** Paddle’s overlay includes a built-in *"Entering business details?"* toggle. When clicked, it asks for the company name and Tax/VAT ID, validates it in real time, applies the 0% Reverse Charge, and formats the invoice automatically.

- **Stripe Elements B2B Flow:** Stripe Elements handles standard credit card fields out of the box, but collecting and validating B2B VAT IDs requires you to code custom input fields, listen to change events, and query Stripe's Tax APIs to recalculate totals dynamically.

### Summary: Which UX Wins for Your App?

- **Choose Paddle’s UX if:** You want a clean, zero-maintenance checkout out of the box that handles localized taxes, PayPal, and B2B invoice requests automatically without needing custom frontend engineering.

- **Choose Stripe Elements’ UX if:** Your primary priority is brand control, seamless on-page integration where the user never sees an overlay, and complete freedom over how payment fields look and behave.
