---

title: "developers-duties"
doc-id: "mb-85e657ca"
updated: "2026-11-11"

---

# Developer's duties

The duties only the developer can carry out. Each one says when it applies, what to do, and where it is done.

## Recurring

1. **When the Morning Tasks pop-up says the dream cycle is due: run it.**
   
   - OpenCode web UI, build mode: `/mb-memory-system-diagnostic`. Answer yes at every gate, including the dream cycle at the end.
   - Then commit the memory-governor repository (duty 2), because the diagnostic writes into its register.
   - Why: autopilot is off by decision, so GBrain's dream cycle runs only by hand. How Morning Tasks works: [[[mybizz-os-docs:operating-procedures/morning-tasks-explainer]]](C:/mybizz/mybizz-os-docs/operating-procedures/morning-tasks-explainer.md).

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

14. **Whenever the Anvil editor shows an app out of sync with GitHub: choose Merge changes.**
    
    - Anvil editor: in the out-of-sync pop-up, click **Merge changes**. Never click **Discard the remote changes**.
    - Why: Discard the remote changes overwrites GitHub with the editor's copy, and every commit made from the PC since is lost from GitHub. Merge changes keeps both.
15. **Update Brand Profile**
    “When a canonical document named in the brand profile changes, update the brand profile.”

## Once-off to-do

1. **Clean up PostgreSQL.** Windows has a duplicate `PostgreSQL` service, a `pgvector_user` role and leftover test databases in the `postgres` database; the WSL PostgreSQL databases have never been listed in full. The ledger (`pdlf`, Windows, port 5433) and GBrain (`gbrain`, WSL, port 5432) are the only databases in use.
   - Ask Claude for the commands: first a read-only census of both servers, then the removals you approve.

2. **When the Cyber Essentials certificate is issued (before 1 April 2027): add the Cyber Essentials statement and badge.**
   - Ask Claude to add the statement and the badge to the Mybizz marketing website and to the client service agreement of each business (`C:\dev\dev-mb-3-cs\mb-3-cs-project-library\legal-local\client-service-agreement.md` and the project template's copy), with the certificate number and its expiry date.
   - Why: the badge may only be shown once the certificate exists; this is Budget.md task 34 (`C:\data-mybizz-mgt\business\Budget.md`).
