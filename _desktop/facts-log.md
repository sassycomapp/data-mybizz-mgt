# Facts Log — Master Index

This file is the index of durable facts saved into GBrain. A fact is a
single short instruction or piece of knowledge that the AI must trust later
without re-checking it. The full fact itself lives inside GBrain, attached
to its subject; this file tells you what exists and how to find it.

## How to use this log

- Facts are stored in GBrain as numbered items, not as pages. The last
  column of the table holds that number (for example "fact-47"), which is
  the exact handle the AI uses to find, verify, or remove the fact.
- To remove an outdated fact, say which row. The AI expires the fact in
  GBrain (it leaves an audit trail, it is not silently erased) and removes
  the row from this table.
- Dates are written as YYYY/MM/DD.

## Facts

| No. | Date       | Subject        | Title                          | Fact                                                              | GBrain reference |
|-----|------------|----------------|--------------------------------|-------------------------------------------------------------------|------------------|
| 001 | 2026/09/13 | communications | Phrasing                       | Write in complete sentences; avoid jargon, avoid shorthand; ideas must flow in one unbroken thread | fact-47          |
| 002 | 2026/09/13 | personal-context | Designed-by-owner            | The developer personally designed every system on this machine and has amnesia; read explainer documents before assuming how anything works | fact-48          |
| 003 | 2026/09/13 | cupcake        | Network grant command          | Grant web access with net-grant --domain <host> --count N; revoke with net-revoke --domain <host>; never use in-policy time checks (they silently fail in the Cupcake engine) | fact-46          |
| 004 | 2026/09/14 | gbrain-dream-cycle | Never probe --phase bare  | A bare `gbrain dream --phase` starts a full live cycle (no parse-fail); only `--source` parse-fails safely; never pipe live dream output to a truncating consumer — capture to file, then read | fact-49          |
| 005 | 2026/09/14 | gbrain        | Upgrade policy + version       | Available upgrade is 0.50.0.0 (live banner 2026-09-14; older 0.48.x notes stale); never upgrade on newness — only on check failure | fact-50          |
| 006 | 2026/09/14 | graphify      | Rebuild provenance stamping    | `graphify extract` stamps built_at_commit from the invoking cwd's git repo, not the scanned path — rebuilds run from the target repo root; the provenance-confirmation step is mandatory (F-4, proven live 2026-09-14) | fact-52          |
| 007 | 2026/09/14 | dev-p         | Denial re-execution standard   | An honoured guard denial never substitutes for a formal execution — re-execute denied checks (clean single-purpose commands; mg-grant where required) or reclassify developer-run; never PASS on prior-session evidence | fact-53          |
| 008 | 2026/09/14 | dev-p         | Memory family                  | The memory family (developer-stated 2026-09-14): GBrain, gbrain-dream-cycle, memory-governor (+ its API, to be confirmed), Graphify, mb-submit-memory; Cupcake and PostgreSQL indirectly related — integration overview: memory-master-explainer.md and memory-functionality-audit.md in mybizz-os-docs | fact-54          |
