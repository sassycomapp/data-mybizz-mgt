---
title: "video-tools"
---
# Task Spec Sheet — Mybizz Video Tools

**Tasks:** C3 to C9 in `marketing-plan.xlsx`
**Owner:** David
**Depends on:** C2 (narration voices)
**Unblocks:** every video in the marketing plan

---

## 1. Result

| Task | Tool | Where | Version | Status |
|---|---|---|---|---|
| C3 | Claude Code | WSL | 2.1.330 | Installed, signed in |
| C4 | FFmpeg | WSL | 6.1.1 (Ubuntu package 7:6.1.1-3ubuntu5) | Installed |
| C5 | video_explainer | WSL, `~/video_explainer` | Remotion 4.0.242 | Installed, test render passed |
| C6 | OpenShot | Windows | 4.1.1 | Installed |
| C7 | OBS Studio | Windows | 33.0.3 | Installed, set up for recording |
| C9 | Playwright | WSL, `~/help-videos` | 1.65.1, with its Chromium browser | Installed |

**WSL system:** Ubuntu 24.04, Python 3.12.3, Node.js 24.15.0.

Every tool on this sheet is free. None needs a card, a billing account or an API key of its own.

---

## 2. C3 — Claude Code

- **What it is:** Anthropic's command-line coding assistant. video_explainer uses it to write scripts and build the animated scenes.
- **Install:** `cd ~ && curl -fsSL https://claude.ai/install.sh | bash`
- **Sign-in:** `claude`, then **Claude account with subscription**. Claude Code uses David's existing Claude plan, and its use counts towards that plan's allowance. The **Anthropic Console** option is never used, because it bills per request.
- **Folder trust:** Claude Code asks whether to trust the folder it starts in. It is started inside `~/video_explainer`, never in the home folder.
- **Check:** `cd ~ && claude --version` prints the version.

---

## 3. C4 — FFmpeg

- **What it is:** the standard tool that cuts, joins and converts audio and video. It builds the five language audio tracks and joins narration to video.
- **Install:** `cd ~ && sudo apt update && sudo apt install -y ffmpeg`
- **Check:** `cd ~ && ffmpeg -version | head -1` prints the version.

---

## 4. C5 — video_explainer

- **What it is:** an open-source pipeline (MIT licence) that turns a source document into an animated explainer video: script, narration, scenes, storyboard and render. Its scenes are drawn by Remotion, which renders each frame in a hidden browser. Source: `https://github.com/prajwal-y/video_explainer`.
- **Folder:** `~/video_explainer` in WSL. Each video is a project in `~/video_explainer/projects/<name>`.
- **Settings:** `config.yaml` sets `llm.provider: "claude-code"`, so video_explainer works through Claude Code on David's Claude plan. Narration is imported as Mybizz's own voiceover (the Gemini voices on the narration-voices sheet).

**Install (in this order):**

1. `cd ~ && git clone https://github.com/prajwal-y/video_explainer.git`
2. `cd ~/video_explainer && sudo apt install -y python3.12-venv && python3 -m venv .venv && .venv/bin/pip install -e .`
3. `cd ~/video_explainer/remotion && npm install`
4. The libraries Remotion's hidden browser needs on Ubuntu:
   `cd ~ && sudo apt install -y libnss3 libdbus-1-3 libatk1.0-0 libgbm-dev libasound2t64 libxrandr2 libxkbcommon-dev libxfixes3 libxcomposite1 libxdamage1 libatk-bridge2.0-0 libpango-1.0-0 libcairo2 libcups2`

**Rules:**

- **Commands run from `~/video_explainer` with its own Python:** `.venv/bin/python -m src.cli <command>`.
- **Every Remotion render names its project:** `PROJECT=<name>` before the render command. Without it, Remotion looks for an example project that is not included, and stops.
- **`npm audit fix` is never run.** npm lists warnings about packages used only on David's computer to build videos; nothing from them faces the internet, and the fix would upgrade packages and could break video_explainer.
- **Updates** to video_explainer, Remotion or any package happen only when David decides.

**Check (render test):** the test project `projects/render-test` holds an empty scene list. This renders one second of the built-in demo scene:

`cd ~/video_explainer/remotion && PROJECT=render-test npx remotion render src/index.ts ThreeDemo ~/render-test.mp4 --frames=0-29 --gl=swangle && ls -lh ~/render-test.mp4`

The test passes when `render-test.mp4` is listed with its size.

**Render speed:** the test rendered 30 frames in about 31 seconds, using two of the computer's processor cores at a time. A 10-minute video at 30 frames a second has 18,000 frames, so long videos render for several hours and are run overnight.

---

## 5. C6 — OpenShot (Windows)

- **What it is:** a free, open-source video editor. It joins each video's intro, main part and outro, and adds the intro and outro to teardowns.
- **Install:** the **Free EXE Installer** (64-bit) from `https://www.openshot.org/download/`, with the default settings. The Microsoft Store version is the same program, sold to support its developers.
- **Check:** OpenShot opens from the Start menu.

---

## 6. C7 — OBS Studio (Windows)

- **What it is:** a free, open-source screen recorder. It records the prospect's website while the teardown narration plays.
- **Install:** the Windows installer from `https://obsproject.com/download`, with the default settings.
- **Settings** (Auto-Configuration Wizard, **Optimize just for recording**):

  | Setting | Value |
  |---|---|
  | Recording encoder | Hardware (QSV, H.264): the computer's built-in video chip does the encoding, so recording does not slow the computer |
  | Recording quality | High quality, medium file size |
  | Base (canvas) resolution | 1366 × 768, the size of David's screen |
  | Output resolution | 1280 × 720 (720p) |
  | Frames per second | 30, the same as every other Mybizz video |

- **Check:** OBS opens, and **Start Recording** records the screen.

---

## 7. C9 — Playwright

- **What it is:** a free, open-source tool (Apache 2.0 licence) that controls a web browser from a script: it clicks, types and moves through an app exactly as written, and records what it does as a video. Mybizz uses it for help videos: Playwright performs one task in the real Mybizz app, once per language, and records it.
- **Folder:** `~/help-videos` in WSL.
- **Install:** `mkdir -p ~/help-videos && cd ~/help-videos && npm init -y && npm install -D @playwright/test && npx playwright install --with-deps chromium`
- **When recordings start:** each help video is recorded once its feature has passed its tests, because the video shows the real, working screen.
- **Check:** `cd ~/help-videos && npx playwright --version` prints the version.
