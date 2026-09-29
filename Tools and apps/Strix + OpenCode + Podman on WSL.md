---
title: "Strix + OpenCode + Podman on WSL"
doc-id: "mb-54d88dcc"
---
https://github.com/usestrix/strix

# Strix + OpenCode + Podman on WSL

## AI‑powered penetration testing for Anvil.works apps

**Audience:** Independent developers running Windows 11 + WSL, using OpenCode and building Anvil.works applications, who want to add automated security testing with Strix using **Podman** instead of Docker.

---

## 1. What is Strix?

Strix is an open‑source, AI‑driven penetration testing tool that:

- Spawns autonomous LLM agents inside an isolated sandbox  
- Actively probes your **codebase, web app, or API** for exploitable vulnerabilities  
- Returns **validated findings with proof‑of‑concept (PoC) exploits**, not just static warnings  
- Can suggest **remediation steps or patches**  
- Integrates with CI/CD and coding agents (e.g. OpenCode, Claude Code, Cursor) via “skills” [100][105][106]

Key properties:

- License: Apache‑2.0 (open source) [100][107]  
- Default LLM support includes OpenRouter models such as `openrouter/z-ai/glm-5.3` [104]  
- Designed to run locally in a containerized sandbox (officially Docker; this guide adapts it to Podman on WSL) [104][106]

For Anvil.works projects, Strix can:

- Test the running Anvil app (via its URL) for OWASP Top 10‑style issues  
- Scan your local Anvil project code for insecure patterns  
- Generate actionable reports you can use to harden your app before deploying to production

---

## 2. Why use Strix with Anvil.works?

Anvil lets you build full‑stack Python web apps quickly. Strix adds:

- **Automated adversarial testing**: AI agents try to break your app like a real attacker would [111][114]  
- **Focus on exploitable bugs**: Instead of hundreds of low‑value static warnings, you get findings with working PoCs [109][114]  
- **Developer‑friendly workflow**: CLI + optional OpenCode integration; results stored locally in `strix_runs/` [104][106]  
- **Cost control**: You choose the LLM (e.g. GLM‑5.3 via OpenRouter) and scan depth, so you can balance thoroughness vs token cost [104]

Typical use cases for your Anvil apps:

- Pre‑release security check before pushing to production  
- Periodic scans of critical apps (auth, payments, admin panels)  
- CI‑style scans on major changes (via scripts or OpenCode tasks)

---

## 3. Architecture overview (with Podman on WSL)

High‑level flow:

1. **You** run the Strix CLI inside WSL (Ubuntu, for example).  
2. Strix uses **Podman** to start a sandbox container with:
   - A browser / HTTP proxy  
   - Python runtime and tooling  
   - Recon/exploitation utilities  
3. Strix’s LLM agents (via your configured provider, e.g. OpenRouter + GLM‑5.3) direct the agents inside the sandbox to:
   - Explore your Anvil app (by URL or local repo)  
   - Attempt attacks (SQLi, XSS, auth bypass, SSRF, etc.)  
   - Validate any vulnerability with a working PoC  
4. Findings + PoCs are written to `strix_runs/<run-name>` on your WSL filesystem.  
5. You review the report, fix issues in your Anvil project, and re‑run Strix as needed.

This guide replaces Docker with Podman while keeping the same logical model.

---

## 4. Prerequisites

You need:

1. **Windows 11 + WSL**  
   
   - A supported distro installed (e.g. Ubuntu 22.04/24.04)  
   - Comfortable working in a WSL terminal

2. **Podman installed in WSL**  
   
   - Podman must be functional inside your WSL distro  
   - You should be able to run:
     
     ```bash
     podman run --rm hello-world
     ```
     
     or a simple Alpine container successfully.

3. **OpenCode installed in WSL** (optional but recommended for integration)  
   
   - You already use OpenCode; ensure `opencode` works in your WSL terminal.

4. **An LLM API key**  
   
   - For this guide: an **OpenRouter** API key  
   - You’ll configure Strix to use `openrouter/z-ai/glm-5.3` (or another model you prefer) [104]

5. **An Anvil.works app to test**  
   
   - Either:
     - A deployed app URL (e.g. `https://your-app.anvil.app`), or  
     - A local Anvil project directory you can point Strix at.

> **Important:** Only run Strix against apps you own or have explicit permission to test. It performs active exploitation attempts.

---

## 5. Installing Strix in WSL

Inside your WSL terminal:

```bash
# 1. Install Strix CLI (official installer)
curl -sSL [https://strix.ai/install](https://strix.ai/install) | bash
```

This will:

- Download the Strix CLI binary  
- Add it to your PATH (follow any on‑screen instructions if needed)

Verify installation:

```bash
strix --version
```

If the installer assumes Docker, that’s fine for now; we’ll override the container runtime in the next section.

---

## 6. Configuring Strix to use Podman instead of Docker

Strix officially expects Docker, but you can make it use Podman by:

- Ensuring `docker` commands resolve to Podman’s compatibility shim, **or**  
- Using environment variables / config if Strix exposes a runtime override.

### Option A – Use Podman’s Docker shim (recommended)

On many WSL setups, installing Podman also provides a `docker` compatibility command. Check:

```bash
which docker
docker --version
```

If `docker` points to Podman’s shim (often via `podman-docker` package), Strix will automatically use Podman under the hood.

If `docker` is not found or is a real Docker CLI without a daemon, you can:

```bash
# Example for Ubuntu/Debian WSL (adjust if you already have Docker installed)
sudo apt update
sudo apt install -y podman-docker
```

This installs a `docker` binary that forwards to Podman. Confirm:

```bash
docker --version
# Should show Podman, not Docker CE
```

Now Strix’s internal `docker` calls will use Podman.

### Option B – Explicit runtime override (if supported)

If Strix adds an explicit runtime config (e.g. `STRIX_CONTAINER_RUNTIME=podman`), you would set:

```bash
export STRIX_CONTAINER_RUNTIME=podman
```

Check `strix --help` or the latest docs for any such flag. If not present, rely on Option A (Podman’s `docker` shim).

---

## 7. Configuring your LLM provider (OpenRouter + GLM‑5.3)

Strix uses environment variables to configure the LLM [104][106].

In your WSL shell (add these to `~/.bashrc` or `~/.zshrc` for persistence):

```bash
export STRIX_LLM="openrouter/z-ai/glm-5.3"
export LLM_API_KEY="YOUR_OPENROUTER_API_KEY"
```

Replace `YOUR_OPENROUTER_API_KEY` with your actual key.

Verify:

```bash
echo "$STRIX_LLM"
echo "$LLM_API_KEY"
```

You should see your configured model and non‑empty key.

---

## 8. Running your first Strix scan against an Anvil app

### 8.1. Scan a deployed Anvil app by URL

From your WSL terminal, in any directory:

```bash
strix --target [https://your-app.anvil.app](https://your-app.anvil.app)
```

Notes:

- First run will pull the Strix sandbox image via Podman (may take a few minutes).  
- Strix will explore the app, attempt attacks, and validate findings.  
- Results are saved under `strix_runs/<run-name>` in your current directory.

To run in **headless / non‑interactive** mode (useful for scripting or OpenCode tasks):

```bash
strix -n --target [https://your-app.anvil.app](https://your-app.anvil.app)
```

### 8.2. Scan a local Anvil project directory

If you have your Anvil project checked out locally in WSL (e.g. under `~/projects/my-anvil-app`):

```bash
cd ~/projects/my-anvil-app
strix --target ./
```

Strix will analyze the code and, if configured, also test the running app if you provide a URL as an additional target.

You can combine targets:

```bash
strix --target ./ --target [https://your-app.anvil.app](https://your-app.anvil.app)
```

---

## 9. Understanding the results

After a run completes, you’ll see output summarizing findings. Inspect the detailed report:

```bash
# List recent runs
ls strix_runs

# View a specific run (replace <run-name>)
strix view strix_runs/<run-name>
```

Each validated finding typically includes:

- **Vulnerability type** (e.g. SQL injection, XSS, auth bypass)  
- **Location** (URL, parameter, code file)  
- **Proof‑of‑concept** (steps or payload that successfully exploits it)  
- **Suggested remediation** (code changes, config fixes)

Use this to:

- Prioritize fixes (start with high‑severity, easy‑to‑fix issues)  
- Create tasks in your project tracker  
- Re‑run Strix after fixes to confirm resolution

---

## 10. Integrating Strix with OpenCode

You can use Strix as part of your OpenCode workflow for Anvil projects.

### 10.1. Manual OpenCode task

In an OpenCode session (inside WSL):

1. Ensure environment variables are set (`STRIX_LLM`, `LLM_API_KEY`).  
2. Ask OpenCode to:
   - Run a Strix scan against your Anvil app  
   - Summarize the top 3–5 findings  
   - Propose concrete code changes in your Anvil project to address them

Example prompt:

> Run `strix -n --target https://your-app.anvil.app` in the current directory.  
> Summarize the top 3 vulnerabilities with their PoCs.  
> For each, propose specific changes to my Anvil server code and client code to fix them.

OpenCode can then:

- Execute the command (if configured with shell access)  
- Parse the output  
- Suggest diffs or new files for your Anvil project

### 10.2. OpenCode “skill” for Strix (optional)

Strix provides a skill for coding agents (e.g. Claude Code, Codex) that defines a standard penetration‑testing workflow [105]. You can adapt this pattern for OpenCode by:

- Creating a local skill file (e.g. `skills/penetration-testing-with-strix.md`)  
- Describing:
  - How to invoke Strix  
  - How to interpret results  
  - How to generate fix proposals

Then, in OpenCode sessions, you can activate this skill to standardize how security scans are run and reported.

---

## 11. Using Strix in a lightweight CI‑style flow (WSL scripts)

Even without GitHub Actions, you can create simple scripts to run Strix before major deployments.

Example `scan-anvil.sh` in your project:

```bash
#!/usr/bin/env bash
set -euo pipefail

export STRIX_LLM="openrouter/z-ai/glm-5.3"
export LLM_API_KEY="$OPENROUTER_API_KEY"

APP_URL="[https://your-app.anvil.app](https://your-app.anvil.app)"

echo "Running Strix security scan against $APP_URL ..."
strix -n --target "$APP_URL" --scan-mode quick

echo "Scan complete. Check strix_runs/ for results."
```

Make it executable:

```bash
chmod +x scan-anvil.sh
```

Run before deploying:

```bash
./scan-anvil.sh
```

You can ask OpenCode to:

- Maintain this script  
- Adjust `--scan-mode` (e.g. `quick` vs deeper scans)  
- Summarize new findings compared to previous runs

---

## 12. Cost and performance considerations

- **LLM token usage:** Strix’s agents can be verbose; deeper scans cost more tokens.  
  - Start with `--scan-mode quick` for routine checks.  
  - Use deeper modes only for major releases or high‑risk apps.  
- **Podman overhead:** First run pulls the sandbox image; subsequent runs reuse it.  
- **Scan time:** Depends on app size/complexity and scan mode; expect minutes, not seconds.

To control costs:

- Limit scans to critical apps  
- Use targeted scans (specific URLs or sub‑trees)  
- Monitor your OpenRouter usage after initial runs

---

## 13. Security and ethical considerations

- Only test **apps you own or have explicit written permission** to test.  
- Do not run Strix against third‑party services without authorization.  
- Treat Strix like any other pentest tool: powerful, but potentially disruptive if misused.

---

## 14. Troubleshooting

### Podman / container issues

- Ensure Podman works independently:
  
  ```bash
  podman run --rm hello-world
  ```
- If Strix fails to start containers, verify:
  - `docker --version` points to Podman’s shim (if using Option A)  
  - No conflicting Docker daemon is running  
  - Your user has permission to run containers in WSL

### LLM / API issues

- Confirm environment variables:
  
  ```bash
  echo "$STRIX_LLM"
  echo "$LLM_API_KEY"
  ```
- Test your OpenRouter key with a simple API call outside Strix to ensure it’s valid.

### Anvil‑specific considerations

- If your Anvil app uses auth, consider:
  - Creating a dedicated test account for Strix to use  
  - Documenting login flows so agents can explore authenticated areas (if supported)  
- For apps behind custom domains or WAFs, ensure Strix’s sandbox can reach them from WSL.

---

## 15. Next steps

1. Install Strix in WSL and configure Podman as described.  
2. Run a first scan against a non‑critical Anvil app to learn the output format.  
3. Integrate Strix into your regular workflow:
   - Pre‑release scans  
   - Periodic checks for key apps  
   - OpenCode‑assisted triage and fixing of findings  

If you’d like, you can extend this setup later with:

- Scheduled scans via cron in WSL  
- Deeper CI integration if you move your Anvil projects into GitHub/GitLab  
- Custom OpenCode skills tailored to your Anvil architecture and threat model
