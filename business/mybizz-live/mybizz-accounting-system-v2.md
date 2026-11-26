---
title: "mybizz-accounting-system-v2"
updated: "2026-11-26"
---
# Mybizz Accounting System — Concept and Technical Plan

This document defines the accounting system that every Mybizz client instance runs: the parties, the operating environment, the currencies, the exchange rates, the rules for every kind of record, and the technical design that carries those rules. The master template holds the system once; every client instance inherits it as a dependency.

## 1. Parties and terms

- **Mybizz:** the company. Mybizz has clients, never customers.
- **Client:** a subscriber to Mybizz. Each client runs its own online business in its own client instance.
- **Client instance:** the client's copy of the Mybizz master template.
- **Customer:** a person who buys products or services from a client in the client's instance. Clients and client instances have customers, never clients.
- **Pronouns:** the document never uses "we", "us", "they" or "them". Every sentence names the party it means.
- **System currency:** the one currency a client instance keeps its books in.
- **Foreign currency:** any currency other than the system currency.
- **Document rate:** the official daily exchange rate stamped on a document (invoice, quote, order, booking, package, expense) on its date.
- **Settled amount:** the system-currency amount that actually reached the client's gateway balance or bank account.
- **Realised exchange gain or loss:** the difference between a payment's settled amount and the amount the invoice recorded for the same money.

## 2. Operating environment

### 2.1 Business

1. The accounting system covers only transactions between clients and their customers. Transactions between Mybizz and its clients are outside it.
2. There are two payment gateways: Stripe and PayPal.
3. Clients may also accept offline payments, such as bank wires or cheques, alongside Stripe and PayPal.
4. Clients may give customers payment terms, such as 30 days on invoice.
5. Refunds and chargebacks are standard business operations. The accounting system handles both.

### 2.2 Gateways

1. The rules, regulations and standard methods of operation of Stripe and PayPal apply to every transaction that runs through them, and are not negotiable.
2. Refunds and chargebacks follow each gateway's own rules.

### 2.3 System currency

1. Each client sets one system currency at onboarding.
2. Once confirmed, the system currency never changes.
3. The system currency is normally the currency of the client's home country, the currency the client's business pays tax in.

### 2.4 Standard

1. One foreign-exchange standard applies to every client instance. The master template encodes it, so every client instance runs it identically.
2. The standard must be acceptable to banks, financiers, accountants, tax authorities and businesses worldwide.
3. Credo: simple, secure, robust, fit for purpose.
4. One best-fit solution, not options.

## 3. Currencies

### 3.1 How a client may sell

A client may:

1. sell only in the system currency;
2. sell to a chosen region in that region's currency (for example, a UK client prices goods and services in USD for the US market);
3. sell to every market in each market's own currency;
4. sell to every market in one chosen currency (for example, a UK client prices everything in USD).

### 3.2 Currency codes

ISO 4217 governs every currency code (USD, GBP, EUR, CAD …) and every currency's minor unit (2 decimals for USD, GBP and EUR; 0 for JPY; 3 for KWD). ISO 4217 is the one currency identification standard shared by every bank, tax authority, payment gateway and accounting package.

### 3.3 Currencies a client may use

The currencies a client may use, as system currency or as a selling currency, are those that both the ECB and Stripe cover. The regular list has 30 currencies:

AUD, BRL, CAD, CHF, CNY, CZK, DKK, EUR, GBP, HKD, HUF, IDR, ILS, INR, ISK, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PLN, RON, SEK, SGD, THB, TRY, USD, ZAR.

Stripe covers all 30. PayPal covers fewer. The sublist below holds the currencies in which a customer cannot pay by PayPal:

| Currency | PayPal position |
|---|---|
| IDR, INR, ISK, KRW, RON, TRY, ZAR | Not supported by PayPal |
| BRL, CNY, MYR | Supported by PayPal only for PayPal accounts registered in Brazil, China and Malaysia |

In these currencies, the client instance offers card payment (Stripe) and offline payment only, unless the client's PayPal account is registered in the matching country.

## 4. Accounting standard

### 4.1 One method for every country

Every major accounting framework (IFRS IAS 21, US GAAP ASC 830, UK FRS 102 section 30, Canadian ASPE) measures a foreign-currency transaction the same way:

1. The transaction is recorded in the functional (system) currency at the exchange rate on the transaction date.
2. The cash, when it settles, is recorded at what was actually received on the settlement date.
3. The difference between the two is a realised exchange gain or loss in profit and loss.

A client that keeps cash-basis books uses only the settled payment amount and ignores the gain or loss. The same records therefore serve accrual and cash-basis clients in every country.

### 4.2 Records the client instance keeps

| Group | Records |
|---|---|
| Sales | Quotes and their lines; orders for delivered work; packages customers have bought; bookings and their prices |
| Invoices | Every invoice and every invoice line |
| Money received and refunded | Every payment and every refund: card, PayPal, or recorded by hand |
| Money spent | Every expense of the business, sorted into categories the client can edit |
| Time worked | Hours a team member worked that can be billed on an invoice |

### 4.3 Reports the client instance produces

1. Profit and loss, month by month, with realised exchange gains and losses on their own line.
2. Outstanding invoices.
3. Tax collected and tax paid.
4. Customer statements.
5. One-click export of a period's full books to Wave, Xero or QuickBooks. The export carries each invoice with its document rate and each payment with its settled amount and actual rate, so the accounting package shows the same exchange gain or loss as the client instance.

## 5. Exchange rates

### 5.1 Two kinds of amount

1. **Documents** (invoices, quotes, orders, bookings, packages, unpaid expenses) carry no cash yet. A document is converted to the system currency at the document rate on its date.
2. **Cash** (payments, refunds, chargebacks) is recorded at the settled amount: what actually reached or left the client's gateway balance or bank account. The client instance never converts cash with a calculated rate when a settled amount exists.

### 5.2 Which official rate

Tax authorities differ on which rate is acceptable for the tax figure on a foreign-currency invoice:

| Authority | Acceptable rates |
|---|---|
| UK, HMRC (VAT) | The UK market selling rate at the time of supply (default); the HMRC period rate (published monthly); any other rate only with HMRC's written approval |
| EU member states (VAT Directive, Article 91) | The latest selling rate on the member state's most representative exchange market; every member state must also accept the latest ECB rate |
| US, IRS | No official rate; any posted rate used consistently |

No single commercial feed is accepted by every one of these authorities. The rule is therefore:

**Each client instance uses the official rate of its own tax authority, set automatically from the system currency at onboarding and never changed:**

| System currency | Rate source |
|---|---|
| GBP | HMRC period rate for the month of the document date |
| Every other currency on the regular list | ECB reference rate for the document date; where the ECB has published no rate for that date (weekends, holidays, before about 16:00 CET), the last rate published before it |

Rates between two non-euro currencies are worked out through the euro, as Article 91 prescribes. An EU member state may require a business to notify it that the business uses the ECB rate; the client's onboarding tells the client to do so where the client's country requires it. The rate source of a client instance is one fixed setting, like the system currency: every document in that instance uses it, with no exceptions.

### 5.3 Rate storage

1. The client instance fetches each rate source once per day (ECB) or once per month (HMRC), keeps it, and reuses it for every document of that date.
2. The rate used is stamped on the document as `exchange_rate` and is never recalculated.
3. The client may still set any commercial selling price. A product priced at USD 99.00 is invoiced at USD 99.00; the invoice is converted to the system currency at the document rate, whatever the client's pricing rate was.

## 6. Rules

### Rule 1 — Documents and the tax point

- **Trigger:** a client issues an invoice, or records a quote, order, booking, customer package or expense.
- **Action:** the client instance takes the document rate (foreign currency → system currency) for the document's date and saves it permanently as `exchange_rate`.
- **Fixed amounts:**
  - `invoice.system_amount` = `invoice.total_amount` × `invoice.exchange_rate`
  - `invoice.tax_amount_system` = `invoice.tax_amount` × `invoice.exchange_rate`
- **Tax point:** tax authorities require the tax on a foreign-currency invoice to be fixed in the system currency on the invoice date (the tax point) at an official rate, whenever the customer pays. `tax_amount_system` is printed on the invoice and never changes. The invoice carries one tax rate, so the tax total sits on the invoice, not on each line.
- **Quotes, orders, packages, bookings:** converted at the document rate on their creation date. The conversion is indicative only; no cash moves and no gain or loss arises.

### Rule 2 — Cash is recorded at the settled amount

Every payment follows one rule: cash is recorded at the actual system-currency amount received.

| Payment route | Trigger | Recording rule |
|---|---|---|
| Stripe | `payment_intent.succeeded` / `charge.succeeded` → read the Balance Transaction | Record `balance_transaction.amount` (converted from minor units) as the settled amount |
| PayPal, converted to the system currency | `PAYMENT.CAPTURE.COMPLETED` → read `seller_receivable_breakdown` | Record `receivable_amount.value` as the settled amount |
| PayPal, held in a foreign balance | `PAYMENT.CAPTURE.COMPLETED` where `receivable_amount.currency_code` is not the system currency | Mark the payment "awaiting conversion". Once the client converts the balance in PayPal, the client enters the actual system-currency amount received, exactly as for a bank wire |
| Offline (bank wire, cheque) | Entered by hand | The client enters: (1) the foreign amount the customer paid; (2) the system-currency amount credited, exactly as the bank statement shows it; (3) the settlement date; (4) any bank charge on the statement. The client instance works out the actual rate: settled amount ÷ foreign amount |

Why: the bank statement and the gateway report are the real cash, and the books must match the bank to the cent. A rate calculated by the client instance never matches the bank exactly.

### Rule 3 — Realised exchange gain or loss

- **Trigger:** a payment settles against an invoice, and the payment is not "awaiting conversion".
- **Formula** (proportional, so part payments and instalments work the same way as full payments):

  Realised gain or loss = settled amount − (invoice system amount × foreign amount paid ÷ invoice foreign total)

- **Example:** an invoice for USD 1,000 is issued on Day 1 at a document rate of 0.80, so `invoice.system_amount` is GBP 800.00. The customer pays USD 1,000 on Day 30 and GBP 790.00 reaches the bank. Realised loss = 790.00 − (800.00 × 1,000 ÷ 1,000) = GBP −10.00.
- **Storage:** on the payment record, as `realised_fx_gain_loss`.
- **Reporting:** a line of its own in the monthly profit and loss; exported with both the invoice's document rate and the payment's actual rate.

### Rule 4 — Refunds and chargebacks

- **Trigger:** Stripe `charge.refunded` or `charge.dispute.closed`; PayPal `PAYMENT.CAPTURE.REFUNDED` or `CUSTOMER.DISPUTE.RESOLVED`.
- **Refund currency:** the customer is refunded in the currency the customer paid in.
- **Action:** the gateways process refunds and chargebacks at the exchange rate on the refund or dispute date, not the original sale date. The client instance records the exact system-currency amount taken from the client's gateway balance (Stripe Balance Transaction, PayPal refund breakdown).
- **Gain or loss:** the difference between the original payment's settled amount (in proportion to the part refunded) and the refund's settled amount is recorded as a realised exchange gain or loss on the refund record, so the books match the bank to the cent.

### Rule 5 — Expenses

- An expense paid at once by card or bank is recorded at the system-currency amount the card or bank actually charged.
- An expense recorded as an unpaid bill is converted at the document rate on its receipt date. When the bill is paid, the payment is recorded at the settled amount, and the difference is a realised exchange gain or loss, exactly as Rule 3.

## 7. Record matrix

| Record or event | Amount in the system currency | Realised gain or loss |
|---|---|---|
| Quotes, orders, packages, bookings | Document rate on the creation date (indicative) | No; no cash moved |
| Customer invoice (Day 1) | Document rate on the invoice date; tax fixed at the same rate | No; sets the baseline |
| Expense paid at once | Amount the card or bank actually charged | No |
| Expense as an unpaid bill | Document rate on the receipt date | Yes, when paid at a different rate |
| Stripe payment | Settled amount from the Balance Transaction | Yes: settled amount − invoice share |
| PayPal payment, converted | Settled amount from `seller_receivable_breakdown` | Yes: settled amount − invoice share |
| PayPal payment, held in a foreign balance | "Awaiting conversion" until the client enters the settled amount | Yes, once entered |
| Offline payment | Settled amount from the bank statement, entered by the client | Yes: settled amount − invoice share |
| Refund or chargeback | Settled amount the gateway deducted | Yes: settled amount − original payment share |

## 8. Gateway settlement

### 8.1 Stripe

1. When a customer pays in a currency other than the client's settlement currency, Stripe converts the charge into the settlement currency and records the converted amount and the rate on the Balance Transaction.
2. In certain countries, Stripe lets a business settle in additional currencies into matching bank accounts. A client that sets this up receives foreign-currency settlements; those payments follow the "held in a foreign balance" route of Rule 2.
3. Onboarding instruction: the client's Stripe settlement currency is the system currency, with no additional settlement currencies.

### 8.2 PayPal

1. Unless set otherwise, PayPal does not convert a payment in a currency the client does not hold: PayPal prompts the client to open a balance in that currency, convert the payment to the primary currency, or deny the payment, and the payment stays pending until the client acts.
2. PayPal's Payment Receiving Preferences let a business account convert every such payment automatically to the primary currency.
3. Onboarding instruction (PayPal's own feature, within PayPal's rules):
   - the client's PayPal primary currency is the system currency;
   - Payment Receiving Preferences are set to "Yes, accept and convert them to [system currency]";
   - the client holds no other currency balance in PayPal, because automatic conversion applies only to currencies the client does not hold.
4. With this setting, PayPal behaves like Stripe: every payment arrives in the system currency with its settled amount and rate in the capture webhook.
5. A payment that still arrives in a foreign currency follows the "held in a foreign balance" route of Rule 2.

## 9. Technical design

1. **Currency codes:** ISO 4217 three-letter codes only, validated against the regular list (section 3.3).
2. **Amounts:** exact decimal storage, never floating point: money as DECIMAL(19,4), exchange rates as DECIMAL(18,8). Display and gateway amounts follow each currency's ISO 4217 minor unit.
3. **Document fields:** every document carries `currency`, the foreign amounts, `exchange_rate` and `system_amount`; an invoice also carries `tax_amount_system`. All are fixed on the document date.
4. **Payment fields:** `currency`, foreign amount, settled `system_amount`, actual rate (settled amount ÷ foreign amount), gateway fee or bank charge, status (including "awaiting conversion"), `realised_fx_gain_loss`.
5. **Refund fields:** as payment fields, with the link to the original payment and its own `realised_fx_gain_loss`.
6. **Rate source:** one fixed setting per client instance, from the system currency (section 5.2). Rates are fetched once per publication (daily for ECB, monthly for HMRC), kept, and reused, so every lookup is fast and gives the same answer.
7. **Gateway integration:** always read the settled Stripe Balance Transaction and the PayPal `seller_receivable_breakdown`, never the customer's checkout charge, so the gateway's conversion spread is captured exactly.
8. **Immutability:** `exchange_rate`, `system_amount`, `tax_amount_system` and `realised_fx_gain_loss` are written once and never recalculated.

## 10. Research record

The research behind this plan raised the claims below. Each claim was checked at its source on 2026-11-26.

| Claim in the research | Finding |
|---|---|
| The ECB publishes rates for 29 currencies against the euro | Correct: 29 currencies; the ECB has suspended the rouble |
| The ECB omits trading currencies such as AED, SAR, NGN and CLP | Correct |
| Stripe charges in over 135 currencies and converts at capture into the settlement currency | Correct |
| Only enterprise Stripe clients can settle in additional currencies | Incorrect: settlement in additional currencies is available in certain countries, not only to enterprise accounts |
| PayPal by default holds a foreign payment in a foreign-currency balance | Incorrect in detail: PayPal prompts the client to open a balance, convert or deny, and the payment stays pending until the client acts |
| PayPal lists 25 currencies; BRL, CNY and MYR are in-country only | Correct |
| HMRC publishes monthly and weekly rates, not daily rates | Partly correct: HMRC publishes monthly period rates and checks them weekly; HMRC VAT also accepts the UK market selling rate at the time of supply, which is a daily rate |
| The IRS requires daily spot rates | Incorrect in detail: the IRS has no official rate and accepts any posted rate used consistently, generally the spot rate when the item is received, paid or accrued |
| Open Exchange Rates is the feed used by Xero, QuickBooks and Wave | Incorrect: Xero uses XE.com; QuickBooks uses Wall Street On Demand; Wave's source was not confirmed |
| The IRS, HMRC, CRA and EU VAT authorities all accept commercial feeds such as XE, OANDA or Open Exchange Rates | Incorrect for HMRC and the EU: HMRC accepts the UK market selling rate, the HMRC period rate, or a rate approved in writing; EU member states must accept the national market selling rate or the ECB rate. Correct for the IRS. The CRA position was not confirmed |
| IFRS records a transaction at the transaction-date rate and the settlement at the settlement-date rate, with the difference in profit and loss | Correct (IAS 21); US GAAP ASC 830 follows the same principle |
| Xero, QuickBooks and Wave calculate the realised gain or loss from the invoice rate and the payment rate | Correct |

### 10.1 Earlier positions the research went through

1. **Books at the gateway pay-in amount:** each sale was recorded at the system-currency amount Stripe or PayPal paid in. This rule now applies to cash (Rule 2); documents use the document rate (Rule 1).
2. **Books at the ECB rate of the day for everything:** every sale, invoice and payment was converted at the ECB rate, including payments entered by hand. Payments now use the settled amount (Rule 2).
3. **PayPal foreign balance at the daily rate:** a PayPal payment held in a foreign balance was converted at the payment date's reference rate, with the PayPal wallet treated as a foreign-currency bank account. The settled amount entered by the client now applies (Rule 2), so the books match the bank.
4. **Open Exchange Rates (or XE, or Fixer) as the one rate source for every instance:** proposed because of its 170+ currencies and native support for any base currency. Not adopted, because HMRC and EU VAT law do not accept a commercial feed by default (section 10).
5. **Tax at the client's own pricing rate:** the tax figure on a foreign-currency invoice used the rate the client set for local prices. The official rate now applies (Rule 1).
