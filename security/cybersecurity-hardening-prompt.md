---
title: "cybersecurity-hardening-prompt"
doc-id: "mb-5da6987c"
updated: "2026-11-13"
---
# Cybersecurity Hardening – Defensive Security Due Diligence

Having addressed our legal and regulatory compliance obligations, I now want to take MyBizz's cybersecurity to the next level.

This is a voluntary security-hardening exercise, going beyond minimum legal compliance. Our objective is to make MyBizz as resistant as reasonably achievable to hacking, exploitation, unauthorised access, data theft, service disruption and other malicious activity. No system can be guaranteed hacker-proof, but we want to establish a robust, defence-in-depth security posture.

I want this investigation grounded in recognised industry best practices and, particularly, authoritative recommendations from the cybersecurity industry and respected security communities. These should include OWASP, NIST, CIS, CISA and other relevant authorities. Consider standards and resources such as OWASP ASVS, OWASP Top 10, API Security Top 10, OWASP Cheat Sheet Series, OWASP SAMM and NIST SSDF.

Please keep the investigation proportionate and practical. I do not want us disappearing down endless technical rabbit-holes, but neither should we overlook any essential vulnerability, attack surface or defensive measure relevant to a commercial SaaS application.

The investigation must consider MyBizz's actual architecture, technology stack, hosting environment, client- instance/ multi-tenant model, application functionality, integrations, development practices and operational responsibilities. Distinguish between security controls provided by our underlying platform and those we must implement ourselves.

The work should produce three deliverables:

1. **Cybersecurity Threat and Risk Assessment:** Identify the realistic threats, attack vectors, vulnerabilities and potential consequences relevant to MyBizz. Prioritise them according to likelihood, impact and exposure.

2. **Consolidated Security Requirements:** Establish a comprehensive but manageable set of defensive requirements, covering application security, authentication, authorisation, tenant isolation, APIs, databases, infrastructure, data protection, secrets, dependencies, development tools, deployment, monitoring, backups and incident response. Avoid duplication and establish appropriate security baselines.

3. **Technical Security Specification and Verification Plan:** Specify exactly how we should implement the required protections. Identify the necessary development practices, technical controls, tools, skills and testing methods. Define measurable security criteria, vulnerability thresholds, audit procedures and the evidence required to demonstrate that each requirement has been satisfied.

Particular attention must be given to preventing cross-tenant data exposure, privilege escalation, account compromise, injection attacks, insecure APIs, business-logic exploitation, supply-chain compromise and unauthorised access to sensitive information.

The cybersecurity assessment must account for MyBizz's distributed hosting architecture:

- **Anvil.works:** Hosts the central MyBizz management application and development environment.

- **DigitalOcean:** Hosts the deployed commercial client instances.

Assess both environments independently, as well as the security of the communication, deployment, management and integration mechanisms connecting them.

Clearly distinguish between security responsibilities provided by Anvil and DigitalOcean, those implemented by MyBizz, and those requiring shared responsibility.

Particular attention must be given to the security of the central management application, the deployment pipeline, privileged administrative access, client-instance provisioning, and the isolation of individual client environments.

Do not assume that securing one environment automatically secures the other. The overall assessment must address the complete MyBizz ecosystem and its associated attack surfaces.

Finally, establish a practical, prioritised implementation and verification roadmap. Every security requirement must have a corresponding method of implementation, a means of testing it, and an objectively verifiable acceptance criterion.

**The ultimate objective is to build security into MyBizz's architecture and development lifecycle rather than attempting to bolt it on afterwards.** We want a commercially credible, resilient SaaS platform with demonstrable defensive security, not simply an application that passes a superficial security checklist.
