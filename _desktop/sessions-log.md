# Sessions Log — Master Index

This file is the index of past AI sessions. Every time a session is closed
out, the AI adds one row to the table below: a number, the date, the project
or area the session belonged to (Topic), the narrower piece of work within it
(Subject), the full human-readable title, and the exact name of the session
page inside GBrain. The full session summary itself lives in GBrain, not in
this file. This file only tells you what exists and what it is called.

## How to use this log

- To revisit a session, open any AI session and say: "open session 001" (or
  whichever number you want). The AI reads this log, finds the GBrain page
  name, and loads that page.
- To clean up old sessions, say which number or date range you no longer
  need. The AI deletes the GBrain page by its exact name and removes the row
  from this table. Pages can be restored for three days after deletion.
- Rows are numbered in the order sessions are closed out. Numbers are never
  reused.
- Dates are written as YYYY/MM/DD.

## How the GBrain page name is formed

The AI chooses the page name when it writes the page. The convention is:
`sessions/YYYY-MM-DD-NNN-<short-hint>`, where the short hint comes from the
Topic and Subject in plain hyphenated words (for example
`sessions/2026-09-13-002-makepdlf-step-11`). The full Title is for humans
and lives only in this table. The page name only needs to be unique and
stable; this log is the authoritative record of which name belongs to which
number.

## Sessions

| No. | Date       | Topic          | Subject                        | Title                                                                       | GBrain page name                                        |
|-----|------------|----------------|--------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------|
| 001 | 2026/09/13 | cupcake, gbrain | network grants; close-out design | Session 001 — the network grant system, the session close-out design, and the communication rules | sessions/2026-09-13-001-network-grants-and-session-memory |
| 002 | 2026/09/14 | config-management | gbrain-dream-cycle suite | Session 002 — the dream-cycle configuration-management suite built and verified healthy (run #1 formal plus the developer-unlocked full live cycle), the standing setup prompt created, and the backup second lane established | sessions/2026-09-14-001-dream-cycle-config-mgmt |
| 003 | 2026/09/14 | config-management | graphify suite | Session 003 — the graphify configuration-management suite built and finalized: run #1 HEALTHY with all tiers 0–3 in full including the complete documented rebuild, the F-4 cwd-provenance tool defect found and fixed in-run, the denial-re-execution standard applied, and the memory family recorded | sessions/2026-09-14-002-graphify-config-mgmt |
| 004 | 2026/09/15 | data-mybizz-mgt registration | underscore dropped from folder; repo, GBrain source, opencode allow registered | data-mybizz-mgt repo + GBrain + opencode registration | sessions/2026-09-15-001-data-mybizz-mgt-repo-registration |
