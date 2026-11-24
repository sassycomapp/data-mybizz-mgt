---
title: "film-production"
---
# Task Spec Sheet — Mybizz Film Production

**Tasks:** every "Scenes and render" task in `marketing-plan.xlsx` (Video Plan sheet), starting with task 42 (FDA-1)
**Owner:** David runs the commands; Claude writes and checks them
**Depends on:** the film's English script (`marketing/scripts/`) and its English narration (`done-audios`, one file per scene)
**Tools:** video_explainer and Claude Code (`video-tools.md`), Kokoro (`narration-voices.md`)

---

## 1. Result

Each long-form film's animated picture track is made by video_explainer on David's PC, timed to Sarah's narration, in the Mybizz colours. The picture track is then assembled with the intro and outro clips in OpenShot.

| Item | Value |
|---|---|
| Project folder (WSL) | `~/video_explainer/projects/<video>`, for example `projects/fda-1` |
| Script used | the film's English script, word for word |
| Picture instructions | each scene's "On screen" note |
| Narration used | `done-audios/<video>-en-sNN.wav`, one file per scene |
| Colours | Professional Blue `#0200BD` and `#004FDA` on white |
| Rendered film | `projects/<video>/output/final.mp4` |
| Import tool | `marketing/tools/prepare_film.py` |

---

## 2. How It Works

- **The script is not rewritten.** `prepare_film.py` writes the finished script into the project's script and narration files, so video_explainer's own script-writing steps are never run.
- **The pictures follow the "On screen" notes.** Claude Code draws each scene as moving graphics (shapes, icons, short words, arrows and counters) from its "On screen" note and narration. The films in this sheet show no app screens.
- **The pictures follow the voice.** Whisper, a free speech-recognition tool (`faster-whisper`), listens to each scene's voice file and records when each word is spoken, so each picture appears on its words.
- **The colours are Mybizz's.** video_explainer writes a colour file (`scenes/styles.ts`) with its own blue; `prepare_film.py brand` replaces it with the Mybizz blues before the render.
- **Claude Code usage.** The scenes step runs Claude Code on David's Claude plan: about one Claude Code session per film.
- **Render time.** The PC renders about one frame a second; a 6-to-7-minute film (about 12,000 frames) takes about 3 to 4 hours. The PC cannot stay on overnight, so renders run during the day.

---

## 3. Set-Up (WSL terminal, once)

1. **Whisper, with PyAV 16.1.** Whisper reads sound files through PyAV; PyAV 19 dropped an option Whisper uses, and PyAV 16.1 is the newest version that both works with Whisper and installs ready-made on this PC.

```
cd ~/video_explainer && .venv/bin/pip install faster-whisper && .venv/bin/pip install "av==16.1.0" --only-binary=:all:
```

2. **A current Claude model.** video_explainer names the retired model `claude-sonnet-4-20250514` in `config.yaml` and in its program code; every mention is replaced by `sonnet`, which Claude Code maps to the current Sonnet model.

```
cd ~/video_explainer && sed -i 's/model: "claude-sonnet-4-20250514"/model: "sonnet"/' config.yaml && grep -rl "claude-sonnet-4-20250514" src | xargs -r sed -i 's/claude-sonnet-4-20250514/sonnet/g'
```

3. **Claude subscription, never the API key.** `~/.bashrc` sets an `ANTHROPIC_API_KEY`, which Claude Code would use, and bill, before David's Claude subscription. Every video_explainer command therefore starts with `env -u ANTHROPIC_API_KEY`, which hides the key for that command only.

**Check:** `cd ~/video_explainer && env -u ANTHROPIC_API_KEY claude auth status` shows `"authMethod": "claude.ai"`.

4. **Scene checks by the TypeScript compiler only.** video_explainer's quick brace check reads every apostrophe in on-screen text or comments (for example "YOU'RE", "customer's") as the start of a quotation, reports false errors, and its automatic repair then damages correct files. The automatic repair and the quick check are switched off; the TypeScript compiler, which builds the video, stays as the check.

```
cd ~/video_explainer && sed -i 's/return verifier.verify_scenes(scenes_dir, auto_fix=True)/return verifier.verify_scenes(scenes_dir, auto_fix=False)/' src/scenes/generator.py && sed -i 's/basic_errors = self._run_basic_syntax_check(scenes_dir)/basic_errors = []  # Mybizz: TypeScript compiler only; the basic check misreads apostrophes/' src/scenes/syntax_verifier.py
```

The message "FutureWarning: The `fitz` API is deprecated" appears at the start of every video_explainer command; it comes from a document-reading library video_explainer does not use for Mybizz films, and needs no action.

---

## 4. Making One Film (WSL terminal, one step at a time)

`fda-1` stands for the film's video ID.

1. **Import the script and narration:**

```
cd ~/video_explainer && .venv/bin/python /mnt/c/data-mybizz-mgt/marketing/tools/prepare_film.py prepare fda-1
```

2. **Time the words (voiceover import):**

```
cd ~/video_explainer && env -u ANTHROPIC_API_KEY .venv/bin/python -m src.cli voiceover fda-1 --provider manual --audio-dir projects/fda-1/recordings
```

3. **Draw the scenes (Claude Code, about 30 to 60 minutes; `--force` redraws scenes that already exist):**

```
cd ~/video_explainer && env -u ANTHROPIC_API_KEY .venv/bin/python -m src.cli scenes fda-1 --force
```

   Then check the scenes with the TypeScript compiler; the check passes with "All scenes pass syntax verification":

```
cd ~/video_explainer && env -u ANTHROPIC_API_KEY .venv/bin/python -m src.cli scenes fda-1 --verify --no-auto-fix
```

4. **Set the Mybizz colours:**

```
cd ~/video_explainer && .venv/bin/python /mnt/c/data-mybizz-mgt/marketing/tools/prepare_film.py brand fda-1
```

5. **Build the storyboard:**

```
cd ~/video_explainer && env -u ANTHROPIC_API_KEY .venv/bin/python -m src.cli storyboard fda-1
```

6. **Render:**

```
cd ~/video_explainer && env -u ANTHROPIC_API_KEY .venv/bin/python -m src.cli render fda-1 --gl swangle
```

**Check:** `projects/fda-1/output/final.mp4` plays, the pictures match the narration, and no app screens, foreign logos or misspelt words appear. A faulty scene is redrawn with `env -u ANTHROPIC_API_KEY .venv/bin/python -m src.cli scenes fda-1 --scene <number>`, then steps 4 to 6 run again.
