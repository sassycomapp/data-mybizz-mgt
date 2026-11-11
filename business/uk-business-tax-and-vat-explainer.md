---
title: "uk-business-tax-and-vat-explainer"
doc-id: "mb-6450d886"
updated: "2026-11-11"
---
# UK Business Tax and VAT Explainer

This document explains the taxes Mybizz-Live Ltd pays and files as a UK company, and how sales taxes work on Mybizz subscriptions sold through Paddle. The setup steps and deadlines are in `mybizz-live-business-setup.md`. The costs are in `Budget.md`.

## 1. Corporation Tax

### What it is

Corporation Tax is the UK tax on a company's profit. Profit is income less the costs of running the business. Mybizz-Live Ltd is incorporated in the UK, so it is UK tax resident and pays Corporation Tax to HMRC on all its profit.

### Rates

| Yearly profit | Rate |
|---|---|
| Up to £50,000 | 19% (small profits rate) |
| £50,000 to £250,000 | Between 19% and 25%, through marginal relief, a sliding scale HMRC applies automatically |
| Over £250,000 | 25% (main rate) |

The £50,000 and £250,000 limits are reduced for an accounting period shorter than 12 months. They are also divided between companies under common control, so they apply in full while Mybizz-Live Ltd is David's only company.

### Filing and payment

| Item | Deadline | How |
|---|---|---|
| Annual accounts | 9 months after the year end; the first accounts 21 months after incorporation | Filed with Companies House from FreeAgent as micro-entity accounts |
| Company tax return (CT600) | 12 months after the year end | Filed with HMRC from FreeAgent, with the accounts in the format HMRC requires (iXBRL) |
| Corporation Tax payment | 9 months and 1 day after the year end | Paid from the Wise account |

The payment falls due before the return. FreeAgent works out the tax during the year, so the amount is known in time.

### Taking money out of the company

The company's money belongs to the company, not to David. Money reaches David in one of two ways:

- **Salary:** a cost to the company, which lowers its profit and its Corporation Tax. Salary is run through payroll.
- **Dividends:** paid from profit after Corporation Tax. The UK takes no tax from dividends paid to a shareholder living outside the UK.

David's personal tax on salary and dividends is decided by the country he lives in, and is outside this document.

## 2. VAT

### What it is

VAT (Value Added Tax) is a tax on sales of goods and services. A VAT-registered business adds VAT to its sales and pays that VAT to HMRC. It reclaims the VAT it pays on its own costs. The standard UK rate is 20%.

### Mybizz-Live Ltd's registration

Registration is compulsory once a business's UK taxable sales pass £90,000 in 12 months. Mybizz-Live Ltd registers voluntarily from the day it is incorporated, because registration removes VAT from its costs and adds no VAT to its sales:

- **Sales:** Mybizz-Live Ltd sells every subscription to Paddle. Paddle confirms that sellers charge Paddle no VAT on payouts, because Paddle accounts for that VAT itself. Each client's £79 reaches Mybizz-Live Ltd in full, less Paddle's fee.
- **Overseas suppliers:** DigitalOcean, Anvil, AWS, Cloudflare and Groq charge no VAT to a business that gives them a UK VAT number. Mybizz-Live Ltd records the VAT on these services itself under the reverse charge: the VAT is entered as both owed and reclaimed on the same return, so the net amount is nil.
- **UK suppliers:** VAT charged by UK suppliers, such as FreeAgent, is reclaimed on the VAT return.
- **Insurance:** insurance carries Insurance Premium Tax instead of VAT. It cannot be reclaimed.

### VAT returns

| Item | Deadline | How |
|---|---|---|
| VAT return | Every quarter, due 1 month and 7 days after the quarter ends | Filed from FreeAgent under Making Tax Digital, HMRC's rule that VAT returns are filed from approved software |
| VAT payment or repayment | Same deadline | Mybizz-Live Ltd's returns usually show VAT to reclaim, which HMRC repays to the Wise account |

## 3. Sales Taxes on Mybizz Subscriptions

### Who handles them

Paddle is Mybizz's merchant of record: the legal seller of every subscription to every client. Paddle therefore charges, files and pays the sales tax on every subscription, in every country:

| Client's location | Tax Paddle handles |
|---|---|
| United Kingdom | UK VAT at 20% |
| European Union | The VAT of the client's country |
| United States | State sales tax, where the client's state taxes software subscriptions |
| Canada | GST, HST or provincial tax |
| Other countries | The local tax on digital services |

Mybizz-Live Ltd holds no tax registration outside the UK, files no foreign tax return, and carries no liability for any foreign tax audit.

### Business and consumer clients

Tax law treats a buyer as a business only when the buyer gives a valid business tax number. A client who gives none is treated as a consumer, even if the client uses Mybizz only for business.

Paddle's checkout asks each client for a business name and tax number, and checks the number at once:

- **Valid number:** for a client outside the UK, Paddle charges no tax (the reverse charge) and the client accounts for the tax itself. A UK business client pays UK VAT and reclaims it.
- **No number:** Paddle charges the tax of the client's country.

A client who forgets the number at checkout adds it from the receipt email, and Paddle reissues the receipt. Mybizz-Live Ltd takes no part in this.

### What Mybizz-Live Ltd records

Mybizz-Live Ltd records one sale per Paddle payout, less Paddle's fee, with no VAT. FreeAgent receives each payout through the Wise bank feed.
