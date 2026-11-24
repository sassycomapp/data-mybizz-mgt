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

```
cd ~/video_explainer && .venv/bin/pip install faster-whisper
```

---

## 4. Making One Film (WSL terminal, one step at a time)

`fda-1` stands for the film's video ID.

1. **Import the script and narration:**

```
cd ~/video_explainer && .venv/bin/python /mnt/c/data-mybizz-mgt/marketing/tools/prepare_film.py prepare fda-1
```

2. **Time the words (voiceover import):**

```
cd ~/video_explainer && .venv/bin/python -m src.cli voiceover fda-1 --provider manual --audio-dir projects/fda-1/recordings
```

3. **Draw the scenes (Claude Code):**

```
cd ~/video_explainer && .venv/bin/python -m src.cli scenes fda-1
```

4. **Set the Mybizz colours:**

```
cd ~/video_explainer && .venv/bin/python /mnt/c/data-mybizz-mgt/marketing/tools/prepare_film.py brand fda-1
```

5. **Build the storyboard:**

```
cd ~/video_explainer && .venv/bin/python -m src.cli storyboard fda-1
```

6. **Render:**

```
cd ~/video_explainer && .venv/bin/python -m src.cli render fda-1 --gl swangle
```

**Check:** `projects/fda-1/output/final.mp4` plays, the pictures match the narration, and no app screens, foreign logos or misspelt words appear. A faulty scene is redrawn with `.venv/bin/python -m src.cli scenes fda-1 --scene <number>`, then steps 4 to 6 run again.
