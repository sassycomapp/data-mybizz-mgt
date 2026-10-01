---
title: "initial"
doc-id: "mb-08d4cd73"
---
Project Development Lifecycle Framework (PDLF)
1. Ideation
Generate many possible ideas and opportunities.
Output: Idea pool
Resources: Creative brainstorming, AI ideation, domain knowledge, competitive analysis, research, imagination, intuition


2. Concept Synthesis
Combine, select, and consolidate ideas into one candidate concept.
Output: Concept statement
Resources: AI synthesis, concept clustering, prioritization frameworks, decision matrices, structured thinking


3. Concept Expansion
Explore the concept’s boundaries using imagination, intuition, constraints, and known best practices.
Output: Expanded concept model
Resources: AI exploration, domain expertise, best practices, systems thinking, scenario design


4. Concept Definition
Identify the essential working principle — what the concept actually is.
Output: Core concept definition
Resources: First-principles thinking, abstraction, concept modeling, requirements reasoning


5. Concept Distillation
Remove fluff, assumptions, duplication, and non-essential details. Keep only truth, constraints, and relevance.
Output: Distilled concept document
Resources: AI refinement, simplification methods, requirements filtering, relevance testing


6. Project Framing
Convert concept into operational form: goals, user flows, workflows, scope, outcomes.
Output: Project Concept Document (PCD)
Resources: User flow design, operational workflow design, use cases, journey mapping, planning methods


7. Platform & Framework Selection
Define execution environment and foundational stack.
Output: Technology & Delivery Stack
Resources:
	• Daniel Miessler LifeOS principles
	• OpenCode
	• G Stack skills
	• Matt Pocock practices
	• Anvil.works
	• Anvil AI
	• GitHub
	• Material Design 3 principles
	• MUI design principles
	• CSS Overlay approach


8. Architecture & Standards
Define architecture, design rules, constraints, conventions, and quality principles.
Output: Architecture Specification
Resources:
	• Architecture patterns
	• Security-first design
	• Simplicity principles
	• Robustness standards
	• Fit-for-purpose evaluation
	• Coding standards
	• UI standards
	• Component standards
	• System constraints


9. Product Planning
Develop PRD and supporting planning documents.
Output: Locked planning package
Resources:
	• PRD
	• Functional specifications
	• User stories
	• Acceptance criteria
	• Requirement traceability
	• AI-assisted documentation


10. Data Design
Design database/schema.
Output: Data Model
Resources:
	• Anvil Data Tables
	• Table structures
	• Column definitions
	• Data types
	• Relationships
	• Validation rules
	• Naming conventions
	• Security model


11. Design Sanity Audit
Validate consistency, feasibility, simplicity, and fit-for-purpose.
Output: Audit findings
Resources:
	• Architecture review
	• UX review
	• Risk assessment
	• Complexity analysis
	• Constraint validation
	• Technical feasibility checks


12. Design Lockdown
Finalize PRD and architecture.
Output: Baseline v1
Resources:
	• Change control
	• Versioned documents
	• Approval checkpoints
	• Scope freeze


13. UX/UI Design
Create wireframes and screens.
Output: UI package
Resources:
	• Wireframes
	• Screen flows
	• Material 3
	• MUI principles
	• UX standards
	• Component hierarchy
	• Design consistency checks


14. Frontend Assembly (Anvil)
Build interfaces and connect components.
Output: Functional UI
Resources:
	• Anvil.works
	• Anvil Designer
	• Anvil AI
	• Material 3 theme
	• CSS Overlay
	• Component wiring
	• Event design


15. Feature Development (OpenCode + TDD)
Build feature-by-feature with tests first.
Output: Working application
Resources:
	• OpenCode
	• TDD
	• AI coding
	• G Stack skills
	• Matt Pocock practices
	• GitHub version control
	• Unit testing
	• Feature branching
	• Refactoring


16. Integration & Refinement (Anvil + AI)
Push, integrate, refine, stabilize.
Output: Release candidate
Resources:
	• Anvil deployment
	• GitHub synchronization
	• AI-assisted refinement
	• Integration testing
	• Bug fixing
	• Performance tuning


17. Validation & Release
Acceptance testing, deployment, lessons learned.
Output: Production release
Resources:
	• UAT
	• Production validation
	• Release checklist
	• Deployment process
	• Monitoring
	• Retrospective
	• Documentation updates


Workflow:

progressive with controlled iteration.
You generally move 1 → 17, but with intentional feedback loops.
A simple model:

Phase A — Discover
1 → 5
(Ideation → Distillation)
↓ (concept validated)

Phase B — Define
6 → 12
(Project framing → Design lockdown)
↺ Architecture, planning, data, and audit may cycle several times.
↓ (baseline approved)

Phase C — Design
13 → 14
(UI design → Frontend assembly)
↺ UI frequently feeds back into architecture and PRD.
↓ (UI stable)

Phase D — Build
15 → 16
(Feature development → Integration)
↺ Continuous TDD and refinement loops.
↓ (candidate accepted)

Phase E — Validate & Release
17
↺ Findings can reopen:
	• UI → back to 13 
	• Architecture → back to 8 
	• Planning → back to 9 
	• Data → back to 10 

A useful rule:
	• Move forward by default 
	• Loop backward only when new information invalidates earlier decisions 
	• Never redesign completed phases without a documented reason 
So the structure is stage-gated, not waterfall. The numbered order remains valuable, but iteration is expected.


## Skill Workflow Table (Authoritative)

The 17 stages above are the conceptual framework. The actual execution order is defined by the 24-step skill workflow table at:
`C:\pdlf\docs\skill-workflow-table.md`

The PDLF orchestrator (`/pdlf`) uses the 24-step table as its execution model. The phases A-E map to the 24 steps as follows:

**Phase A — Discover & Define (steps 1–5):**
1. `/office-hours` → 2. `to-prd` → 3. `/plan-ceo-review` → 4. `/plan-eng-review` → 5. `domain-modeling`

**Phase B — Design & Plan (steps 6–13):**
6. Manual: Anvil data tables → 7. `to-issues` → 8. `/design-consultation` → 9. `wireframe` (Phase 1) → 10. `/plan-design-review` → 11. `/plan-devex-review` → 12. `prototype` (optional) → 13. `wireframe` (Phase 2)

**Phase C — Scaffold & Assemble (steps 14–15):**
14. Manual: Anvil UI forms → 15. Manual: client/server scaffolding

**Phase D — Build & Verify (steps 16–21):**
16. `/build` (OpenCode agent) → 17. `/design-review` → 18. `/review` → 19. `/qa` → 20. `triage` → 21. `improve-codebase-architecture` (optional)

**Phase E — Ship & Monitor (steps 22–24):**
22. `/ship` → 23. `/land-and-deploy` → 24. `/canary` (initial check)

**Post-E — LEARN (step 25):**
Retro + learnings + context-save + ISA update + GBrain embed

The skill workflow table defines the authoritative order. The PDLF orchestrator enforces sequential execution — each step is a hard gate.
