---
title: "mybizz-live-business-setup"
doc-id: "mb-2119df24"
updated: "2026-11-12"
---
# Mybizz-Live Business Setup

This document sets out the legal company behind Mybizz, how that company is formed, and what it must do to stay legally compliant. All amounts are GBP. The costs match the fixed costs in `Budget.md`.

## 1. The Company

| Item | Setting |
|---|---|
| Name | Mybizz-Live Ltd |
| Legal form | Private company limited by shares, registered in England and Wales |
| Rules | The standard Model Articles of Association, adopted when the company is registered online |
| Director | David, the only director |
| Shares | 100 ordinary shares of £1 each, all owned by David |
| Person with significant control | David, holding 100% of the shares and votes |
| Business activity (SIC code) | 62012, business and domestic software development, as the only code |
| Registered office | The UK address package (section 2) |
| Tax | UK Corporation Tax; registered for VAT from incorporation |
| Bank | Wise Business, GBP account |
| Accounting | FreeAgent, limited company plan |
| Sales | Paddle, as merchant of record: Paddle sells to each client and handles all sales taxes |

A limited company is a legal person in its own right. The company owns the software, the domain and the client contracts, and David's personal assets are separate from the company's debts.

David owns more than half the shares and the company has no employees, so the law does not require employers' liability insurance. That insurance is bought before anyone other than David works for Mybizz, paid or unpaid.

## 2. Addresses

David lives outside the UK, so the company buys one address package from a UK provider that covers both public addresses.

| Address | Purpose | Setting | Public |
|---|---|---|---|
| Registered office | The company's legal address, where HMRC and Companies House send official mail | The provider's physical UK address, with official mail scanned and emailed. A PO Box is not allowed | Yes |
| Director's service address | The contact address for David on the public register | The same provider address | Yes |
| Director's residential address | David's real home address | Given to Companies House only | No |

The package costs about £60 a year. It keeps David's home address off the public register.

## 3. Timeline

| Date | Milestone |
|---|---|
| January 2027 | Steps 1 to 3 of section 4: name check, address package, identity verification |
| 1 February 2027 | Step 4: the company is registered |
| February 2027 | Steps 5 to 12: bank, tax registrations, ICO fee, FreeAgent, Paddle |
| Before 1 April 2027 | Cyber Essentials and the business insurance, as `Budget.md` sets out |
| 1 April 2027 | Mybizz goes live and takes its first paying client |

The company is registered two months before go-live because Paddle's seller checks need the company and its bank account. Registering any earlier would only start the fixed costs earlier.

## 4. Setup Checklist

Every step is David's. The steps run in this order.

| # | Step | How | Cost |
|---|---|---|---|
| 1 | Check the name | Search "Mybizz-Live Ltd" on the Companies House register to confirm it is available. | Free |
| 2 | Buy the address package | Buy the registered office and director's service address package of section 2. | About £60 a year |
| 3 | Verify identity | Verify David's identity through GOV.UK One Login and note the personal code it gives. Identity verification is compulsory for every director and person with significant control. If One Login cannot verify the passport, verify through an Authorised Corporate Service Provider; most address providers offer this. | Free through One Login |
| 4 | Register the company | Register online at Companies House with the settings of section 1, the addresses of section 2 and the personal code of step 3. Approval usually takes 24 hours. The Certificate of Incorporation gives the company number. | £100, once |
| 5 | Open the bank account | Open a Wise Business account for Mybizz-Live Ltd with the Certificate of Incorporation, David's passport and proof of his home address. Activate the GBP balance. | £50, once; no monthly fee |
| 6 | Register for VAT | Register online with HMRC for VAT voluntarily, with quarterly returns. The registration states that the company makes taxable supplies of software services through Paddle. | Free |
| 7 | Register for Corporation Tax | HMRC posts the company's Unique Taxpayer Reference to the registered office after incorporation. Register for Corporation Tax online with that reference, within 3 months of the company starting business. | Free |
| 8 | Pay the ICO fee | Register with the Information Commissioner's Office as a tier 1 organisation and pay by direct debit. The law requires this fee from every company that holds personal data. | £47 a year |
| 9 | Set up FreeAgent | Subscribe to FreeAgent's limited company plan. Enter the company number, VAT number, Corporation Tax reference and year end. Connect the Wise GBP balance as a bank feed. | £33 a month |
| 10 | Enter the VAT number on every supplier account | Add the VAT number to DigitalOcean, Anvil, AWS, Cloudflare, Groq, Paddle and every other supplier, so no supplier charges VAT. | Free |
| 11 | Become a Paddle seller | Set up Paddle as section 5 describes. | Paddle's fee per payment only |
| 12 | Connect FreeAgent to App 5 | In FreeAgent, create a separate user for App 5 at the lowest access level that reads the tax timeline. Approve App 5's connection to FreeAgent through that user. Enter the confirmation statement date in App 5. App 5 only reads from FreeAgent and never changes anything there. | Free |

## 5. Paddle

### What Paddle is

Paddle is Mybizz-Live Ltd's merchant of record: the legal reseller of every Mybizz subscription. Mybizz-Live Ltd sells each subscription to Paddle, and Paddle sells it on to the client. Paddle is not a marketplace: Mybizz stays on its own domain, and clients never browse or find Mybizz through Paddle.

Paddle carries the work and the legal liability for sales taxes in every country. Mybizz-Live Ltd holds no tax registrations outside the UK.

| Paddle does | Mybizz-Live Ltd does |
|---|---|
| Runs the checkout, takes payment, and renews each subscription every month | Provides the Mybizz service, onboarding and all product support |
| Charges each client the sales tax of the client's country, and files and pays that tax | Answers support requests and points billing questions to Paddle's buyer portal |
| Accepts a client's business tax number at checkout, or later from the receipt email, and reissues the receipt | Sets prices and decides refunds |
| Issues and emails every invoice and receipt, under Paddle's name with the Mybizz logo | Acts on Paddle's notifications through App 5 |
| Handles fraud checks, chargebacks and failed payment retries | |
| Pays Mybizz-Live Ltd each month, less Paddle's fee | |

Paddle's fee is 5% of each payment plus a fixed amount per payment: £6.33 on each £119 monthly payment and £59.88 on each £1,190 annual payment.

### What the client sees

- The checkout opens over the Mybizz page, with the Mybizz logo and colours, and a note that Paddle is the merchant of record.
- The card statement shows Paddle's name followed by MYBIZZ, so the client recognises the charge.
- The invoice names Paddle.com Market Ltd as the seller, with Paddle's tax numbers and the Mybizz logo. A business client can claim the invoice as a business expense.

### Setup

These steps make up step 11 of section 4.

| # | Step |
|---|---|
| 1 | Publish the Mybizz terms of service, privacy policy and refund policy on `mybizz.live`, with the prices shown. Paddle reviews the website before approving a seller. The terms of service include Paddle's reseller clause from `saas-tos-iro-paddle.md`. |
| 2 | Create the Paddle seller account for Mybizz-Live Ltd with the company number, registered office, VAT number and David's identity. |
| 3 | Add and verify `mybizz.live` as the domain allowed to open the checkout. |
| 4 | Set the payout account to the Wise GBP account, with payouts in GBP. |
| 5 | Create the Mybizz subscription with two prices, £119 a month and £1,190 a year, and assisted setup as a one-off price of £119, each with the fixed local prices in the other currencies of the billing specification. |
| 6 | Brand the checkout and the receipts with the Mybizz logo and colours. |
| 7 | Point Paddle's notifications (webhooks) at App 5, which acts on each new subscription, renewal, failed payment and cancellation, including suspension on day 7 and exit on day 37 after a failed payment, and applies each referral credit as a discount on the referring client's next annual renewal. |
| 8 | Make one test purchase in Paddle's test environment, and check that App 5 records it and that the receipt arrives. |

## 6. Recurring Obligations

| Obligation | When | How | Cost |
|---|---|---|---|
| VAT return | Every quarter, due 1 month and 7 days after the quarter ends | FreeAgent prepares and files the return; David approves it | Included in FreeAgent |
| Confirmation statement | Every year, within 14 days of the company's review date | Filed online at Companies House; confirms the company's details | £50 a year |
| Annual accounts | 9 months after the year end; the first accounts 21 months after incorporation | FreeAgent prepares micro-entity accounts and files them with Companies House | Included in FreeAgent |
| Company tax return | 12 months after the year end | FreeAgent prepares and files the return with HMRC | Included in FreeAgent |
| Corporation Tax payment | 9 months and 1 day after the year end | Paid from the Wise account | The tax due |
| ICO fee | Every year | Direct debit | £47 a year |
| Address package | Every year | Provider renewal of the registered office and director's service address | About £60 a year |
| Wise bank feed consent | Every 90 days | David renews the consent in FreeAgent when App 5's reminder arrives, so Wise transactions keep arriving | Free |

App 5 reads every tax and accounts deadline from FreeAgent's tax timeline each day and reminds David 30 days before each one. App 5 holds the confirmation statement date itself, because that filing is made at Companies House. App 5 also checks daily that Wise transactions are still arriving in FreeAgent, and messages David when none has arrived for 7 days.

The year end is the last day of the month in which the company was registered, so a company registered in February 2027 has its year end on the last day of February each year.

## 7. How Money Flows

1. A client pays £119 a month, or £1,190 a year, to Paddle. Paddle charges the client any sales tax due.
2. Paddle pays out to the Wise GBP account, less Paddle's fee. The payout carries no VAT, because Paddle accounts for the VAT itself.
3. Wise sends each transaction to FreeAgent through the bank feed.
4. Suppliers are paid from the Wise account. With the VAT number on each supplier account, overseas suppliers charge no VAT, and VAT charged by UK suppliers is reclaimed on the quarterly VAT return.
