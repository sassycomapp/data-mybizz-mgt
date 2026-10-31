---
title: "video-creation-suite"
doc-id: "mb-6c4f6600"
updated: "2026-10-31"
---
# Video creation suite

## What it is

The video creation suite is how MyBizz turns its own documentation and diagrams into explainer videos and marketing material for clients. It has two parts:

| Part | Job |
|---|---|
| **Archify** | Draws the approved diagrams: system architecture, user and service flows, and feature walkthroughs. It is already installed. |
| **video_explainer** | Turns documents into narrated, animated videos, plus short vertical clips for social media. Source: `github.com/prajwal-y/video_explainer`, MIT licence. |

video_explainer is installed when the first app has a finished feature to show. Until then, this document is the plan it is installed from.

## How it works

video_explainer reads source documents (Markdown, PDF or a web page) and builds a video in fixed steps:

1. **Plan:** it proposes the video's outline. The developer reviews it and approves it.
2. **Script:** it writes the narration script from the source documents.
3. **Narration:** it shapes the script into spoken narration.
4. **Scenes:** it writes each scene as animated code for Remotion, a video engine that draws video from code.
5. **Voiceover:** it records the narration with a computer voice and times every word.
6. **Storyboard:** it lines up the scenes with the voice.
7. **Render:** it produces the finished video.

Around these steps it can also:

- check the script's facts against the source documents (`factcheck`);
- refine single scenes from written feedback (`refine` and `feedback`);
- add sound effects and background music (`sound` and `music`);
- produce vertical shorts for social media (`short` and `render --short`).

An AI model writes the plan, the script and the scenes. The developer approves the plan before anything else is built.

## Why it works this way

- **The documentation is the source of truth.** A video only explains what an approved document already states. The video is a release, never a source.
- **Archify's diagrams are the approved picture.** video_explainer draws its own animated scenes, so every scene is checked against the approved Archify diagram before release. A video never shows a relationship the diagram does not.
- **One tool, one job.** video_explainer covers every kind of video MyBizz needs: short marketing clips, longer explainers and vertical shorts. No second video tool is installed.
- **It is run by the developer, from the WSL terminal.** It is a program, not an agent skill, so it adds no load to OpenCode sessions, and it sits outside every app.
- **The cost stays low.** The tool is free. Remotion is free for an individual and for a company of up to 3 employees. The Microsoft Edge voices are free. The one running cost is the AI model that writes each video, charged per use by Anthropic or OpenAI.

## Where it lives

| Item | Location |
|---|---|
| The tool | `~/video-explainer` in WSL, pinned to one tested commit |
| Each video | `~/video-explainer/projects/<video-name>/` |
| Source documents for a video | `~/video-explainer/projects/<video-name>/input/` |
| Finished videos | `~/video-explainer/projects/<video-name>/output/` |
| The AI provider key | A file only the developer can read, `~/.config/video-explainer/keys.env`; never in a document, never in `~/.bashrc` |

## What it needs

| Requirement | On this PC |
|---|---|
| Python 3.10 or newer | Python 3.12.3 is installed in WSL |
| Node.js 20 or newer | Node.js 24.15.0 is installed in WSL |
| FFmpeg | Installed in WSL with `sudo apt install ffmpeg` |
| An AI provider key | Anthropic (`ANTHROPIC_API_KEY`) or OpenAI (`OPENAI_API_KEY`) |
| A voice | Microsoft Edge voices, free (`--voice-provider edge`). ElevenLabs is an optional paid voice and needs `ELEVENLABS_API_KEY` |

The AI provider is set in the tool's `config.yaml`, under `llm`: `provider` is `anthropic`, `openai`, `claude-code` or `mock`, and `model` names the model.

The install downloads PyTorch, a large AI library. Background music uses it. Music is optional, and a video works without it.

## How to install it

Once, in the WSL terminal:

1. `sudo apt install ffmpeg`
2. `git clone https://github.com/prajwal-y/video_explainer.git ~/video-explainer`
3. `cd ~/video-explainer`, then `git checkout <tested-commit>` to pin the tool, and record that commit in this document.
4. `python3 -m venv .venv`, then `source .venv/bin/activate`, then `pip install -e .`
5. `cd remotion && npm install && cd ..`
6. Create the key file: `mkdir -p ~/.config/video-explainer`, put the line `ANTHROPIC_API_KEY=<key>` in `~/.config/video-explainer/keys.env`, then `chmod 600 ~/.config/video-explainer/keys.env`.
7. Set `llm.provider` to `anthropic` in `config.yaml`.
8. Prove the install with the free test run: `python -m src.cli create test-video`, then `python -m src.cli generate test-video --mock`.

## How to make a video

Every command runs in the WSL terminal, from inside `~/video-explainer`, with the tool's Python environment active (`source .venv/bin/activate`) and the key file loaded (`set -a; . ~/.config/video-explainer/keys.env; set +a`).

1. **Create the video's project.**
   ```bash
   python -m src.cli create client-onboarding --title "Client onboarding in two minutes"
   ```
2. **Add the source.** Copy the approved document into `projects/client-onboarding/input/`. The source is a Markdown document or a PDF of the approved document, with the Archify diagram in it.
3. **Plan, then approve the plan.**
   ```bash
   python -m src.cli plan create client-onboarding
   python -m src.cli plan approve client-onboarding
   ```
4. **Generate everything up to the voiceover, with the free voice.**
   ```bash
   python -m src.cli generate client-onboarding --to voiceover --voice-provider edge
   ```
5. **Check the facts against the source.**
   ```bash
   python -m src.cli factcheck client-onboarding
   ```
6. **Finish the pipeline.**
   ```bash
   python -m src.cli generate client-onboarding --from storyboard
   ```
7. **Preview at low quality first.**
   ```bash
   python -m src.cli render client-onboarding --preview
   ```
8. **Fix any scene from written feedback.**
   ```bash
   python -m src.cli feedback client-onboarding add "Scene 3: show the sign-up step before the payment step"
   ```
9. **Render the final video.**
   ```bash
   python -m src.cli render client-onboarding -r 1080p
   ```
10. **Make the vertical short for social media.**
    ```bash
    python -m src.cli short generate client-onboarding
    python -m src.cli render client-onboarding --short
    ```

To see the video while it is being built, run `cd remotion && npm run dev` and open the address it prints in a browser.

`python -m src.cli generate <video-name> --mock` runs the whole pipeline with no AI and no voice. It costs nothing.

## What has to happen

- The source for every video is an approved document. The video says nothing the document does not.
- Every scene is checked against the approved Archify diagram before release.
- `factcheck` runs on every video before its final render.
- The developer approves the plan of every video before it is built.
- The AI provider key lives only in `~/.config/video-explainer/keys.env`, readable by the developer alone.
- The tool stays pinned to its tested commit. An update is the developer's decision.
- Remotion's free licence holds while MyBizz has no more than 3 employees. Beyond that, Remotion requires a company licence.
- A finished video is checked by the developer before it reaches a client.
