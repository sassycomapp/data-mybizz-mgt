---
title: "Budget"
doc-id: "mb-3afb1c99"
updated: "2026-11-11"
---
# Budget

All amounts are GBP per month unless stated otherwise. Supplier prices are converted to GBP at the planning rate set in the billing specification.

## 1. Mybizz Fixed Costs

| Cost | Per month |
|---|---|
| Anvil Business account (Apps 1, 2, 3, 5 and the demo apps) | £74.25 |
| Container registry, Basic plan (5 GiB; old images removed automatically) | £3.75 |
| Test client instance | £9.00 |
| `mybizz.live` domain at Cloudflare's renewal price (£18.90 a year) | £1.58 |
| Monitoring of App 5 (one DigitalOcean uptime check, inside the free allowance) | £0.00 |
| Email reputation alarms (two AWS CloudWatch alarms) | £0.15 |
| Image security scan (GitHub Actions on the public `{slug}-app4` repository) | £0.00 |
| Cyber Essentials certification, whole organisation, renewed yearly: £320 a year | £26.67 |
| Business insurance, one combined policy from one insurer, renewed yearly: technology professional indemnity £1m, cyber liability £500,000 and public liability £1m, £1,700 a year including Insurance Premium Tax (budget figure, replaced by the quoted premium when the policy is bought) | £141.67 |
| ICO data protection fee, tier 1, paid by direct debit: £47 a year | £3.92 |
| Companies House confirmation statement, filed online: £50 a year | £4.17 |
| FreeAgent accounting software, limited company plan: files the VAT returns, the annual accounts and the company tax return | £33.00 |
| UK address package: the registered office and the director's service address from one provider, with official mail scanned and emailed; about £60 a year (budget figure, replaced by the chosen provider's price) | £5.00 |
| **Total** | **£303.16** |

One-off costs: company registration at Companies House, £100; Wise Business account set-up, £50.

## 2. Client-Related Costs

**Scenario B: Advanced database with a standby.** A standby server takes over automatically when the main database server fails. Break-even is 9 clients.

| | Escalates with | 1 client | Break-even (9) | 50 clients | 60 clients | 100 clients |
|---|---|---|---|---|---|---|
| **Revenue** | Each client (£79) | **£79.00** | **£711.00** | **£3,950.00** | **£4,740.00** | **£7,900.00** |
| *Costs* | | | | | | |
| Client containers | Each client (£9.00) | £9.00 | £81.00 | £450.00 | £540.00 | £900.00 |
| Database main server | Steps up at client 60 | £97.50 | £97.50 | £97.50 | £195.00 | £195.00 |
| Database standby | Steps up with the main server | £97.50 | £97.50 | £97.50 | £195.00 | £195.00 |
| Email sending | Each client (£1.00) | £1.00 | £9.00 | £50.00 | £60.00 | £100.00 |
| AI writing and insight | Each client (£0.50) | £0.50 | £4.50 | £25.00 | £30.00 | £50.00 |
| Speech to text | Each client (£0.10) | £0.10 | £0.90 | £5.00 | £6.00 | £10.00 |
| Text to speech | Each client (£5.00) | £5.00 | £45.00 | £250.00 | £300.00 | £500.00 |
| Data transfer over the allowance | Each client (£1.00) | £1.00 | £9.00 | £50.00 | £60.00 | £100.00 |
| Paddle fee | Each client (£4.33) | £4.33 | £38.97 | £216.50 | £259.80 | £433.00 |
| **Total client-related costs** | | **£215.93** | **£383.37** | **£1,241.50** | **£1,645.80** | **£2,483.00** |
| **Gross profit** | | **−£136.93** | **£327.63** | **£2,708.50** | **£3,094.20** | **£5,417.00** |
| Mybizz fixed costs (section 1) | Fixed | £303.16 | £303.16 | £303.16 | £303.16 | £303.16 |
| **Net profit** | | **−£440.09** | **£24.47** | **£2,405.34** | **£2,791.04** | **£5,113.84** |

### Escalation points

| Trigger | Action by App 5 | Cost change |
|---|---|---|
| Client 60 | Raises the database cluster from 8 GiB to 16 GiB | Database from £195.00 to £390.00 |
| A client's container passes 80% memory use | Raises that client's container from 1 GiB to 2 GiB | That client's container from £9.00 to £18.75 |
| Cluster storage passes its plan's included storage | DigitalOcean's storage autoscaling adds storage | £0.09 per GiB per month added |
| A client adds staff | None | None: staff are unlimited within the £79 price |

### Highest cost of one client

With every fair-use limit of section 4 reached, one client costs at most £52.98 a month: container £18.75, email £3.75, AI and voice £16.80, data transfer £5.25, Paddle fee £4.33 and a database share of £3.90. Each client's revenue of £79 covers this.

## 3. Basis of the Figures

### VAT

- Mybizz-Live Ltd is registered for VAT from the day it is incorporated.
- Every supplier price in this budget excludes VAT. Overseas suppliers charge no VAT to a VAT-registered business, and VAT charged by UK suppliers is reclaimed on the quarterly VAT return.
- Paddle's payouts to Mybizz carry no VAT, because Paddle accounts for the VAT itself. Each client's £79 reaches Mybizz in full, less Paddle's fee.
- Insurance carries Insurance Premium Tax instead of VAT, which cannot be reclaimed and is included in the insurance line.

### Database

- Cluster: PostgreSQL Advanced Edition, version 18, one main server and one standby, London region.
- Connections: 3 per client. 100 clients use 300 connections.
- 8 GiB plan: 197 connections, 65 clients. 16 GiB plan: 397 connections, 132 clients.
- The edition is fixed when the cluster is created. The plan size can be raised at any time.
- 8 GiB price: £97.50 per server, £195.00 with the standby.
- 16 GiB price: £390.00 with the standby, an estimate until DigitalOcean's control panel shows the price.
- Storage autoscaling is on. Added storage costs £0.09 per GiB per month.

### Backups and uptime

- Daily backups and 7-day point-in-time recovery are included in the cluster price.
- Uptime commitment with a standby: 99.95%.
- Weekly maintenance window: Sunday 06:00 UK time (07:00 Europe, 01:00 New York, Saturday 22:00 Los Angeles).
- Mybizz's nightly copy of each client into the client's own storage continues as designed.

### Database connection

- Every connection uses TLS with full certificate verification. DigitalOcean's certificate is issued by a public authority, which the Anvil App Server trusts.
- Every client's database address carries `prepareThreshold=0`, so the App Server works through DigitalOcean's connection router in any pooling mode.
- Correct running on the cluster is proved by the pre-launch condition that the test client instance runs under realistic load before the first paying client.

### Revenue

- £79 per client per month. The fixed local prices in the other currencies are set close to £79.
- Paddle's fee is 5% of the price plus its fixed fee per payment: £4.33 per client.

### Usage

- Each client is budgeted at medium-to-heavy use: a team of about 6 using email, AI and voice every working day, £7.60 per client per month in total.
- Email: about 12,000 emails a month.
- AI writing and insight: about 600 requests a month.
- Speech to text: about 300 spoken requests a month.
- Text to speech: about 300,000 characters a month.
- Data transfer: each container includes 150 GB a month; £1.00 covers use above it.

## 4. Fair-Use Limits

Every shared resource carries a limit per client. Each limit is set well above the budgeted use, so normal and heavy use never reaches it. The limits are written into the client service agreement as fair-use terms.

| Resource | Budgeted use | Warning to the client | Hard limit | At the hard limit |
|---|---|---|---|---|
| Database connections | Up to 3 | None | 3 | Further requests wait for a free connection. |
| Database query time | Under 1 second | None | 60 seconds per query | The query is cancelled and logged. |
| Idle open transaction | None | None | 120 seconds | The database session is ended. |
| Database size | 100 MB a year | 1 GiB | 2 GiB | Bulk imports are switched off for that client, and David is notified. Each client container reports its database size to App 5 with its heartbeat. |
| Container memory | 1 GiB | At 80% use | 2 GiB container | No further raise; David is notified. |
| Marketing email | About 10,000 a month | 20,000 | 25,000 a month | Marketing sends pause until the next month. Booking, invoice and sign-in emails continue. |
| All email | About 12,000 a month | 40,000 | 50,000 a month | All sending except sign-in email pauses until the next month; David is notified. |
| Email reputation | Bounces under 2%, complaints under 0.05% | SES warns at its reputation policy's warning level | SES reputation policy pause level | SES pauses that client's sending alone. App 5 notifies the client and David. |
| AI and natural voice spend | £5.60 a month | £5.60 | £16.80 a month | AI and natural voice pause until the next month. The browser's built-in voice continues. |
| AI request rate | A few a minute | None | 20 a minute | Further requests wait. |
| Data transfer | Within 150 GB | 150 GB | 500 GB a month | The client and David are notified, and the fair-use terms apply. The cost to Mybizz at 500 GB is £5.25. |
| Client's own Cloudflare storage | Under 10 GB | 8 GB | None | Cloudflare bills the client directly above 10 GB. |

## 5. Maintenance and Automation

Each recurring maintenance point is carried out by App 5 or by a scheduled job. App 5 sends David one daily summary of routine actions and an immediate message for anything that needs his decision. The DigitalOcean, AWS, Groq and Anvil consoles are not watched by David.

| Maintenance point | Frequency | Carried out by | Automation |
|---|---|---|---|
| Client container size | On a memory alert | App 5 | A container above 80% memory use is raised to 2 GiB. |
| Database cluster size | At client 60 | App 5 | The cluster is raised from 8 GiB to 16 GiB when the client count reaches 60. |
| Database storage | Continuous | DigitalOcean | Storage autoscaling adds storage before the disk fills. |
| Fair-use limits | Continuous, and daily for sizes and totals | App 5 | Each limit in section 4 is measured and enforced. |
| New client | Each registration | App 5 | The **New client** action runs when the client completes registration and its Cloudflare set-up. |
| Non-payment | Each failed payment | App 5 | Suspension on day 7 and exit on day 37, driven by Paddle's notifications. |
| Release roll-out | Each release David approves | App 5 | Test client instance, then 10% of clients, then all clients. Each stage passes its health check before the next starts. A failed health check rolls the release back automatically. |
| Image security | Weekly, and at every image build | GitHub Actions | A vulnerability scan of the release image. A build containing end-of-life software fails. A finding is reported to App 5, and the patched image is rolled out as a release once David approves it. A high or critical finding (vendor-rated high or critical, or CVSS 7 or above) is released to every client within 14 days of the vendor's fix; App 5 messages David on days 7 and 10. |
| Registry storage | At every release | GitHub Actions | Images older than the last three releases are deleted, and the registry's storage is cleaned. |
| Received email files | Daily | AWS | Each received email file is deleted from S3 7 days after it is processed. |
| Backup check | Daily | App 5 | Each client's nightly copy is checked for arrival, date and size. |
| Restore drill | Monthly | Test client instance, scheduled by App 5 | One client's nightly copy is restored into a scratch database in the cluster, its row counts are compared with the source, the scratch database is deleted, and the result is reported to App 5. The drill runs inside DigitalOcean because the cluster accepts connections from DigitalOcean only. |
| Domain and certificate check | Daily | App 5 | Each client's domain is checked for resolution, certificate validity and registration expiry. The client is warned 30 days before expiry. |
| App 5 availability | Every minute | DigitalOcean Uptime | One check on App 5's status endpoint. The endpoint reports a fault when App 5 fails or when any active client's heartbeat is older than 30 minutes. Suspended and exited clients are excluded. |
| Access key rotation | Yearly | David, prompted by App 5 | App 5 sends the instructions 14 days before each key expires. The task takes about 10 minutes. |
| PostgreSQL major version | At end of support of version 18 | David, prompted by DigitalOcean and App 5 | One upgrade through DigitalOcean's control panel. |
| David's laptop and phone updates | Automatic | Windows Update, Microsoft Defender and the phone's own updates | Updates install automatically. High and critical fixes are installed within 14 days of release, as Cyber Essentials requires. |
| Business insurance renewal | Yearly | David, prompted by App 5 | App 5 sends the renewal reminder 30 days before the policy expires. The renewal proposal form is answered from the Cyber Essentials compliance document. |
| Cyber Essentials renewal | Yearly | David, prompted by App 5 | App 5 sends the renewal reminder 30 days before the certificate expires. |
| Statutory filings | Quarterly and yearly | FreeAgent, prompted by App 5 | App 5 reads every tax and accounts deadline from FreeAgent's tax timeline each day, through its own FreeAgent user, and sends a reminder 30 days before each one: the quarterly VAT return, the annual accounts (9 months after the year end; the first accounts 21 months after incorporation) and the company tax return with its payment (tax due 9 months and 1 day after the year end). App 5 holds the confirmation statement date itself, because that filing is made at Companies House. FreeAgent prepares and files each tax and accounts return. The ICO fee renews by direct debit. |
| Wise bank feed | Daily, and every 90 days | App 5, and David when prompted | App 5 checks daily through FreeAgent that Wise transactions are still arriving, and messages David when none has arrived for 7 days. App 5 reminds David to renew the bank feed consent 7 days before each 90-day consent ends. |

### Hands-on tasks remaining for David

| Task | Frequency |
|---|---|
| Approve each release, including security-patched images | Per release |
| Answer client support tickets | As they arrive |
| Act on an abuse report about a client's website or email, using App 5's **Suspend** action | When a report arrives at `abuse@mybizz.live` |
| Rotate the access keys | Yearly, about 10 minutes |
| Upgrade the PostgreSQL major version | Once, when version 18 reaches end of support |
| Keep a second payment card on DigitalOcean, Anvil, AWS, Groq and Cloudflare | Once, then when a card is replaced |
| Keep the two hardware security keys: one carried, one stored safely | Once |
| Ask DigitalOcean support to raise the app limit | Once, before client 10 |
| Restart the laptop and phone when updates ask | Weekly, a few minutes |
| Update the asset and software register when a device or cloud service is added or removed | When it happens |
| Renew Cyber Essentials | Yearly, about half a day |
| Renew the Wise bank feed consent in FreeAgent | Every 90 days, about two minutes |
| Approve and file each VAT return, confirmation statement, set of annual accounts and company tax return in FreeAgent | Quarterly and yearly, about one hour each |
| Renew the business insurance policy | Yearly, about one hour |
| Buy employers' liability insurance (at least £5m, as the law requires) before anyone other than David works for Mybizz, paid or unpaid | Once, when the first person is engaged |
| Report a security incident to the insurer's incident line, following the incident response runbook | When an incident happens |

## 6. Client Risks and Safeguards

| Risk to clients | Safeguard | Cost |
|---|---|---|
| One client's heavy database use slows every client on the cluster | Each client's database user has a connection limit of 3, a 60-second query limit and a 120-second idle-transaction limit. Each client's database size is capped at 2 GiB (section 4). | £0.00 |
| One client's bad email list gets Mybizz's whole email account paused by Amazon | Each client's SES tenant carries the standard reputation policy, which pauses that client's sending alone. Two CloudWatch alarms warn at a 4% bounce rate and a 0.08% complaint rate, below Amazon's review levels of 5% and 0.1%. Monthly email volume is capped per client (section 4). | £0.15 |
| One client's AI or voice use runs up costs or exhausts the shared Groq limit | AI and voice spend is capped at £16.80 per client per month and 20 requests a minute (section 4). A Groq organisation spend limit of £1,700 a month, with alerts at 50%, 75% and 90%, covers 100 clients at their cap. | £0.00 |
| One client's traffic runs up data transfer costs | Data transfer is measured per client, with notice at 500 GB and the fair-use terms (section 4). | £0.00 |
| One client's website is used for spam or phishing, and DigitalOcean acts against Mybizz's whole account | The client service agreement's acceptable-use terms, the `abuse@mybizz.live` address on every client website footer, and App 5's **Suspend** action, which stops one client's container. | £0.00 |
| A faulty release reaches every client | Staged roll-out with health checks and automatic rollback (section 5). | £0.00 |
| Backups fail without anyone knowing | Daily backup check and monthly restore drill (section 5). | £0.00 |
| App 5 stops, and with it the monitoring and automation | DigitalOcean Uptime checks App 5 every minute and emails David. Clients keep running while App 5 is down. | £0.00 |
| A London region failure stops every client | App 5's **Rebuild** action restores every client into a new Advanced cluster and new containers in another region, from DigitalOcean's backups or, when those are unreachable, from each client's nightly copy. At most 24 hours of data is lost when the nightly copy is used. | Only while rebuilt |
| A client's domain lapses or its records change, and its website and email stop | Daily domain and certificate check, with a warning to the client 30 days before expiry (section 5). | £0.00 |
| A leaked DigitalOcean access key is used to delete clients | Two keys with custom scopes. The automatic-tasks key can read and update apps and databases only. The provisioning key, which can create and delete, is used only by the **New client**, **Remove** and **Rebuild** actions. | £0.00 |
| A failed card payment suspends a supplier account and stops every client | A second payment card on every supplier account, and DigitalOcean billing alerts. | £0.00 |
| The registry fills and a release cannot be stored | Images older than the last three releases are deleted at every release (section 5). | £0.00 |
| A supplier account that controls clients is taken over with a stolen password | A hardware security key (FIDO2) is required for sign-in on DigitalOcean, Anvil, AWS, Cloudflare, Paddle, GitHub, Groq and every other cloud service Mybizz uses, including the business email account and the IASME portal. AWS's root user is used for nothing else. | £0.00 beyond two security keys, bought once |
| A leaked database password is used from outside | The cluster's trusted sources admit connections from the client containers and the test client instance only. Client database users and their limits are created by a provisioning job that runs inside DigitalOcean. | £0.00 |
| An intruder deletes or encrypts the backups | Each client's backup copies in its R2 bucket are locked for their whole retention period: daily copies for 7 days, weekly copies for 28 days. No key, Mybizz's included, can delete or overwrite a locked copy. | £0.00 |
| A client website is attacked by malicious requests, a flood of traffic or bots | Each client domain is proxied through the client's own Cloudflare account, with Cloudflare's free web application firewall, DDoS protection and bot blocking switched on. Cached pages also lower data transfer. | £0.00 |
| A client, buyer or insurer asks for proof of Mybizz's security | Cyber Essentials certification for the whole organisation, renewed yearly. It includes £25,000 cyber liability insurance with incident response, on top of Mybizz's own policy. | £26.67 |
| A client claims for a loss caused by a fault, an outage or lost data in the Mybizz service | Technology professional indemnity of £1m. The client service agreement caps Mybizz's liability within that cover. | Included in the insurance line of section 1 |
| A breach, ransomware or other cyber incident costs Mybizz money: incident response, data restoration, lost income, client notification, regulatory investigation and claims from affected people | Cyber liability of £500,000, with the insurer's 24-hour incident response line, under the same policy as the professional indemnity, so no claim falls between the two covers. The incident response runbook sets the order of actions. | Included in the insurance line of section 1 |
| A person is injured or property is damaged in connection with Mybizz's business, for example at a client meeting | Public liability of £1m. | Included in the insurance line of section 1 |
| A missed statutory filing or payment brings penalties, or Companies House strikes Mybizz-Live Ltd off the register and every client's service stops | App 5 reads each deadline from FreeAgent's tax timeline and reminds David 30 days before it; FreeAgent prepares and files each return; the ICO fee renews by direct debit (section 5). | Included in section 1 |
| Mybizz-Live Ltd's books fall behind because the Wise bank feed stops | App 5's daily check that Wise transactions are arriving, and its reminder before each 90-day consent ends (section 5). | £0.00 |
| The insurer refuses a claim because a policy condition was not met | Each condition of the policy (MFA on every service, tested and locked backups, timely patching, supported software) is met by a safeguard in this table and checked by a test. The insurance decision record lists each condition with its safeguard and test. | £0.00 |
| A known vulnerability in the release image stays open on client containers | High and critical fixes released within 14 days; end-of-life software fails the build (section 5). | £0.00 |
| A tampered or substituted image reaches clients | Each release image is signed when it is built. Each client container runs the image by its digest, never by a tag, and App 5 releases only an image whose signature verifies. | £0.00 |

## 7. Implementation Tasks

### Project Library Global (Claude)

| # | Task |
|---|---|
| 1 | Hosting specification, database section: Advanced Edition, a standby from the first paying client, PostgreSQL version 18, storage autoscaling, the capacity table, and every client's database address using TLS with full verification and `prepareThreshold=0`. |
| 2 | Hosting specification: the uptime section; the pre-launch conditions, with a test that the App Server reconnects by itself when its database connection is cut; the cost table on Scenario B; the Sunday 06:00 UK maintenance window. |
| 3 | Hosting specification: each client database user created with a connection limit of 3, a 60-second query limit and a 120-second idle-transaction limit. |
| 4 | Billing specification: the cash-flow section on Scenario B, with the £7.60 usage budget per client and the highest cost of one client. |
| 5 | New decision record, fair-use limits: every limit of section 4, how App 5 measures and enforces it, and the notifications to the client and David. |
| 6 | New decision record, automatic resizing: App 5 raises a client's container to 2 GiB and the cluster to 16 GiB, the trigger for each, the largest size App 5 may choose, and the notification to David. |
| 7 | Management visibility decision record and the App 5 design: App 5's connection to DigitalOcean, the scheduled checks, both resize actions, the fair-use enforcement, the **Suspend** and **Rebuild** actions, the audit record, the daily summary and the immediate messages. |
| 8 | Release decision record and hosting specification: the staged roll-out with health checks and automatic rollback, and the registry clean-up at every release. |
| 9 | Integration specification: the SES tenant reputation policy per client, the two CloudWatch alarms, the monthly email caps per client, and the 7-day deletion of received email files from S3. |
| 10 | AI decision record: per-client metering of AI and voice spend, the warning at £5.60, the stop at £16.80, the 20-a-minute rate limit, and the £1,700 Groq organisation spend limit. |
| 11 | Backup security document and hosting specification: the daily backup check and the monthly restore drill. |
| 12 | Observability decision record: App 5's status endpoint, the DigitalOcean Uptime check, the daily domain and certificate check, and the data transfer and client storage checks. |
| 13 | Security documents: the two DigitalOcean access keys and their custom scopes, the yearly rotation, and the `abuse@mybizz.live` address. |
| 14 | Client activation runbook: each client's database and database user created in the Advanced cluster with the settings of tasks 1 and 3. |
| 15 | Rebuild procedure: App 5's **Rebuild** action, restoring every client into a new Advanced cluster and new containers in another region. |
| 16 | Security documents: hardware security keys required on every cloud service Mybizz uses, as Cyber Essentials requires, and AWS's root user kept unused. |
| 17 | Hosting specification and client activation runbook: the cluster's trusted sources limited to DigitalOcean containers; the provisioning job inside DigitalOcean that creates each client's database user and its limits; each container's heartbeat carrying its database size. |
| 18 | Client R2 storage decision record: each client's backup copies locked for their whole retention period. |
| 19 | Client activation runbook and integration specification: each client domain proxied through Cloudflare, with the web application firewall, DDoS protection and bot blocking switched on. |
| 20 | Release decision record: images signed at build, run by digest, and released only when the signature verifies. |
| 21 | New security document, Cyber Essentials compliance: the whole-organisation scope (Mybizz-Live Ltd, David's laptop and phone, every cloud service, Apps 1 to 5 and the client hosting platform); how each of the five controls is met (firewalls, secure configuration, security update management, user access control, malware protection); the asset and software register; the 14-day rule for high and critical fixes; the yearly renewal. Written against the current NCSC requirements (version 3.3, Danzell question set). |
| 22 | Release decision record and App 5 design: high and critical image findings released within 14 days of the vendor's fix, with App 5's messages on days 7 and 10; base image and Java runtime kept on vendor-supported versions; a build containing end-of-life software fails; App 5 records the Cyber Essentials certificate dates and sends the renewal reminder 60 days before expiry. |
| 23 | New decision record, business insurance: the one combined policy (technology professional indemnity £1m, cyber liability £500,000, public liability £1m) and why each cover and limit; employers' liability bought before anyone other than David works for Mybizz; each policy condition listed with the safeguard that meets it and the test that checks it; yearly renewal answered from the Cyber Essentials compliance document. |
| 24 | New policy, incident response, with its runbook: how an incident is recognised, contained and recorded in App 5; the call to the insurer's incident line before any outside supplier is engaged; the report to the Information Commissioner's Office within 72 hours of a personal data breach; notice to affected clients without undue delay; evidence kept for the insurer. |
| 25 | Billing specification: every fixed cost of section 1, VAT registration from incorporation, Paddle payouts without VAT, and break-even at 9 clients. Security documents and the Cyber Essentials compliance document: cross-references to the insurance decision record and the incident response policy. |
| 26 | App 5 design: the insurance policy dates and the renewal reminder 30 days before expiry; the statutory deadline calendar read daily from FreeAgent's tax timeline, plus the confirmation statement date held in App 5, with a reminder 30 days before each deadline; the daily Wise bank feed check and the 90-day consent reminder; the incident record with its timeline (detected, contained, insurer called, Information Commissioner's Office reported, clients notified). |
| 27 | New decision record, company compliance: Mybizz-Live Ltd's statutory obligations and how each is met (VAT registration from incorporation and the quarterly VAT return, the confirmation statement, the annual accounts and the company tax return filed from FreeAgent, the ICO fee by direct debit, the UK registered office), each deadline, and the App 5 reminder for each. |
| 28 | New decision record, FreeAgent integration: App 5 connects to FreeAgent's API through its own FreeAgent user at the lowest access level that reads the tax timeline, and only ever reads; what App 5 reads (the tax timeline, Corporation Tax returns, bank transactions for the bank feed check, monthly income and costs for the daily summary); the stored credentials in App 5's Vault; what happens when the connection fails (App 5 messages David). |

### mb-3-cs Project Library (Claude)

| # | Task |
|---|---|
| 29 | Concept document: the cost and profit figures on Scenario B. |
| 30 | Architecture reference and explainer: App 5's automatic resizing, fair-use enforcement and notifications. |
| 31 | Business, product and software requirements documents and the test specification: the resize, fair-use and notification requirements, each with its test. |
| 32 | Client service agreement, in mb-3-cs and in the project template: the fair-use limits of section 4 and the acceptable-use terms. |
| 33 | Public website footer design: the `abuse@mybizz.live` address on every client website. |
| 34 | Marketing website and client service agreement: the Cyber Essentials statement and badge, added once the certificate is issued. |
| 35 | Client service agreement, in mb-3-cs and in the project template: the limitation of liability, with Mybizz's total liability capped at the fees the client paid in the 12 months before the claim, which sits inside the £1m professional indemnity; the clause on notifying the client of a personal data breach without undue delay. |
| 36 | New document, `saas-tos-iro-paddle.md`, in mb-3-cs and in the project template: the Mybizz terms of service in respect of Paddle, covering Paddle as reseller and merchant of record, invoices and receipts issued by Paddle, refunds paid by Paddle on Mybizz's decision, price changes with advance notice, and agreement to Paddle's buyer terms at checkout. The client service agreement includes this document. |
| 37 | Business, product and software requirements documents and the test specification: the incident record, the breach notice to clients and the insurance renewal reminder, each with its test. |

### PDLF (Claude)

| # | Task |
|---|---|
| 38 | Step 11, App 3 run: the DigitalOcean project, the Advanced cluster with its standby, storage autoscaling and trusted sources, the provisioning job, the registry and the test instance, each one checked. |
| 39 | Step 11, App 5 run: the two DigitalOcean access keys stored in App 5's Vault and checked; the DigitalOcean Uptime check on App 5's status endpoint; the two CloudWatch alarms; the Groq spend limit. |
| 40 | Test suite: the resize decisions and every fair-use limit tested against simulated suppliers; the App Server's reconnection tested after its database connection is cut; a check that the cluster is Advanced with a standby; a check that each client database user carries its three limits; a check that the cluster refuses connections from outside DigitalOcean; a check that a locked backup cannot be deleted; a check that an unsigned image is refused. |
| 41 | `{slug}-app4` repository: the GitHub Actions workflows that scan the release image weekly and at every build, sign each image, report to App 5, and clean the registry at every release. |
| 42 | Step 11, App 3 run: the test client instance's domain proxied through Cloudflare and its nightly-copy bucket locked, each one checked, exactly as every client is set up. |
| 43 | `{slug}-app4` workflows and App 5: the 14-day countdown on high and critical findings, the end-of-life check that fails a build, and the Cyber Essentials renewal reminder, each tested. |
| 44 | Test suite: a check that App 5 holds current insurance, Cyber Essentials and statutory deadline dates and sends each reminder; App 5's FreeAgent connection tested against a FreeAgent sandbox company (tax timeline read, bank feed check, monthly figures, and no write made); an incident drill, run on the test client instance, that walks the incident response runbook and checks each step is recorded in App 5's incident record. |

### David

| # | Task |
|---|---|
| 45 | Before incorporation: buy the UK address package (registered office and director's service address), and verify your identity through GOV.UK One Login. |
| 46 | Register Mybizz-Live Ltd at Companies House (£100), with the address package of task 45 and the identity verification code. |
| 47 | On incorporation: open the Wise Business account (£50), register for VAT and Corporation Tax with HMRC, pay the ICO data protection fee by direct debit, and subscribe to FreeAgent with the Wise bank feed connected. Enter the VAT number on every supplier account. Create App 5's own FreeAgent user at the lowest access level that reads the tax timeline, approve App 5's connection, and enter the confirmation statement date in App 5. The order and detail are in `mybizz-live-business-setup.md`. |
| 48 | Ask DigitalOcean support to raise the account's app limit before client 10. |
| 49 | Create the two DigitalOcean access keys when App 5 is built, as Step 11 instructs. |
| 50 | Add a second payment card to DigitalOcean, Anvil, AWS, Groq and Cloudflare, and switch on DigitalOcean's billing alerts. |
| 51 | Create the `abuse@mybizz.live` address, forwarded to David's email. |
| 52 | Buy two hardware security keys and register both on DigitalOcean, Anvil, AWS, Cloudflare, Paddle, GitHub, Groq and every other cloud service Mybizz uses, including the business email account and the IASME portal. |
| 53 | Set up the laptop and phone for Cyber Essentials: supported operating systems, automatic updates on, Microsoft Defender antivirus and firewall on, screen lock on, unsupported software removed, and a standard Windows account for daily work with a separate administrator account used for administration only. |
| 54 | Fill in the asset and software register of task 21, and run the NCSC's free Cyber Essentials Readiness Tool against it. Fix every gap it reports. |
| 55 | After Mybizz-Live Ltd is incorporated and before the first paying client: choose an IASME certification body, apply for Cyber Essentials for the whole organisation, opt in to the cyber liability insurance, and sign the director's declaration. |
| 56 | Renew Cyber Essentials each year when App 5's reminder arrives. |
| 57 | Before the first paying client: buy the combined policy (technology professional indemnity £1m, cyber liability £500,000, public liability £1m) from one insurer, answering the proposal form from the Cyber Essentials compliance document. Enter the policy dates and the insurer's incident line in App 5 and in the incident response runbook. |
| 58 | Renew the insurance policy each year when App 5's reminder arrives. |
