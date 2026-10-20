---
title: "developers-duties"
doc-id: "mb-85e657ca"
updated: "2026-10-20"
---
# Developer's duties

The duties only the developer can carry out. Each one says when it applies, what to do, and where it is done.

## Recurring

1. **Every week, after the Sunday backup: dream cycle.**
   - OpenCode web UI, build mode: `/mb-memory-system-diagnostic`. Answer yes at every gate, including the dream cycle at the end.
   - Then commit the memory-governor repository (duty 2), because the diagnostic writes into its register.
   - Why: autopilot is off by decision, so GBrain's dream cycle runs only by hand.

2. **After any change in the memory-governor repository: commit it by hand.** commit-all does not cover it.
   - WSL: `cd ~/memory-governor && git add -A && git commit -m "<what changed>" && git push`

3. **After editing a MyBizz skill source** (`C:\mybizz\mb-*\<name>.md`): **copy the change into its installed copy** (`~/.config/opencode/skills/<name>/SKILL.md`), keeping the installed copy's own frontmatter.
   - Check that the bodies match: `diff <(sed '1,/^---$/d;1,/^---$/d' /mnt/c/mybizz/<name>/<name>.md) <(sed '1,/^---$/d;1,/^---$/d' ~/.config/opencode/skills/<name>/SKILL.md) && echo BODIES-IDENTICAL`

4. **After editing gstack's sources: rebuild its OpenCode skills.**
   - WSL: `cd /mnt/c/mybizz/gstack && bun run scripts/gen-skill-docs.ts --host opencode --respect-detection`
   - Check: `grep -rl 'Brain Context Load' /mnt/c/mybizz/gstack/.opencode/skills/ | wc -l` shows 10.

5. **After every OpenCode restart: Cupcake deny test.**
   - OpenCode web UI, plan mode: `Fetch https://example.com and report the exact message.`
   - Pass: it is denied with "Policy Violation — Outbound network access requires authorisation".

6. **After any GBrain upgrade: run mb-doc-check's two GBrain checks.** They are listed in the Checks table of `C:\mybizz\mybizz-config-docs\mb-doc-check\doc-check-reference.md`.

7. **Before any GBrain upgrade: decide GBrain's writer model as part of that upgrade.** It is not adopted; see `C:\mybizz\mybizz-config-docs\gbrain\gbrain-config.md`.

8. **After any documentation-suite refresh (mb-sysdoc-creator run): check the system's configuration.**
   - OpenCode web UI, build mode: `/mb-config-manager <system>`

9. **After any code commit to an app repository: refresh its graph.**
   - WSL: `cd /mnt/c/dev/dev-<business>/<repo> && graphify update /mnt/c/dev/dev-<business>/<repo>`

10. **After any memory-governor code change: prove it with one real governed submission.** The test suite writes into live memory, so it is not run.
    - OpenCode web UI, build mode: `/mb-submit-memory <a real fact file>`
    - Check where it landed: `journalctl --user -u memory-governor-worker --since '-15min' --no-pager | grep 'into GBrain source'` shows the owning project's source.

11. **After superseding a governed fact: retire the old fact in GBrain.** Superseding changes only the governor's record.
    - Find its number: `GBRAIN_SOURCE=<source> gbrain call recall '{"grep":"<words from the fact>"}' | jq -r '.facts[] | [.fact_id, .source] | @tsv'`
    - Retire it: `GBRAIN_SOURCE=<source> gbrain call forget '{"id":"<fact number>"}'`

12. **After adding an OpenCode project: make it reachable in the web UI.**
    - WSL: `mkdir -p ~/projects/<name> && echo "<full path> /home/dev-p/projects/<name> none bind,nofail 0 0" | sudo tee -a /etc/fstab && sudo systemctl daemon-reload && sudo mount -a`
    - Web UI: open `projects/<name>`.

13. **To start the OpenCode web UI:** `cd ~ && opencode web --hostname 0.0.0.0`

## Once-off to-do

1. **PDLF build-plan audit (new session).** Check that the PDLF steps cover every step the build needs, and that each step uses the right installed skills, including `secure-software-engineering` and `security-audit-methodology`. Add a "PDLF steps" column to `C:\mybizz\mybizz-os-docs\os-reference-docs\skills-catalog.md`, recording which steps use each skill. The PDLF step documents are the authority; the column only mirrors them.
