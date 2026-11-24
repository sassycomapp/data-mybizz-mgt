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

5. **Animations that tolerate equal timing points.** Remotion's `interpolate` stops the whole render when two timing points are equal (for example a fade-out that starts where the scene ends: `[896, 916, 1268, 1268]`). The installed Remotion 4.0.242 is changed so that `interpolate` moves an equal point forward by a millionth of a frame, which is invisible, in its three copies under `remotion/node_modules/remotion/dist`. After any change to Remotion's files, Remotion's build cache is cleared, or the render keeps using the old code.

```
cd ~/video_explainer/remotion && L='  inputRange = (function (r) { r = Array.from(r); for (let i = 1; i < r.length; i++) { if (!(r[i] > r[i - 1])) r[i] = r[i - 1] + 1e-6; } return r; })(inputRange); \/\/ Mybizz: strictly increasing ranges' && for f in $(grep -rl "^function interpolate(input, inputRange, outputRange, options) {$" node_modules/remotion/dist); do grep -q "Mybizz: strictly increasing" $f || sed -i "s/^function interpolate(input, inputRange, outputRange, options) {$/&\n$L/" $f; done && rm -rf node_modules/.cache
```

**Check:** `grep -rl "Mybizz: strictly increasing" ~/video_explainer/remotion/node_modules/remotion/dist | wc -l` prints `3`. Reinstalling Remotion (`npm install`) removes this change, so the command runs again after any reinstall.

6. **A correct Reference component.** Every scenes step writes `scenes/components/Reference.tsx` from a template in `src/scenes/generator.py`. The template holds each brace twice (`{{`), as Python text templates do, so the file is written through `.format()`, which turns each pair into the single brace the TypeScript compiler expects.

```
cd ~/video_explainer && sed -i 's/f.write(REFERENCE_TEMPLATE)$/f.write(REFERENCE_TEMPLATE.format())  # Mybizz: single braces/' src/scenes/generator.py
```

**Check:** `grep -c "Mybizz: single braces" ~/video_explainer/src/scenes/generator.py` prints `1`.

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

6. **Render, in one-minute pieces (1,800 frames each, about 35 minutes each):** the first piece is also the look check, watched before the rest are rendered. A piece that stops is run again.

```
cd ~/video_explainer && env -u ANTHROPIC_API_KEY .venv/bin/python -m src.cli render fda-1 --gl swangle --frames 0-1799
```

   The film's length in frames is the "Duration: … frames" line that this first render prints, because the renderer adds short pauses between scenes; the storyboard's length in seconds is shorter and is not used. The remaining pieces run from `1800-3599` upwards in steps of 1,800, and the last piece ends one frame below that duration (for a duration of 10356 frames, the last piece is `9000-10355`). They run one after another in one command:

```
cd ~/video_explainer && for r in 1800-3599 3600-5399 5400-7199 7200-8999 9000-10355; do env -u ANTHROPIC_API_KEY .venv/bin/python -m src.cli render fda-1 --gl swangle --frames $r || break; done
```

   The pieces are written to `projects/fda-1/output/` as `final-frames-<range>.mp4`; `cd ~/video_explainer/projects/fda-1/output && explorer.exe .` opens that folder in Windows.

7. **Join the pieces** once all are rendered:

```
cd ~/video_explainer && env -u ANTHROPIC_API_KEY .venv/bin/python -m src.cli render fda-1 --merge-chunks
```

8. **Save the rendered scenes for assembly** in `C:\data-mybizz-mgt\marketing\brand-assets\wip-videos\` as `<video>-scenes-en.mp4`. Work in progress goes in `wip-videos`; `done-videos` holds only finished videos and clips.

**Check:** `projects/fda-1/output/final.mp4` plays, the pictures match the narration, and no app screens, foreign logos or misspelt words appear. A faulty scene is redrawn with `env -u ANTHROPIC_API_KEY .venv/bin/python -m src.cli scenes fda-1 --scene <number>`, then steps 4 to 8 run again.

---

## Progress

| Film | State | Next step |
|---|---|---|
| FDA-1 (EN) | Pieces `0-1799` to `9000-9995` rendering since 2026-11-24 (render duration 10356 frames) | When that command ends, render the missing last piece, join all pieces and save the film: `cd ~/video_explainer && env -u ANTHROPIC_API_KEY .venv/bin/python -m src.cli render fda-1 --gl swangle --frames 9996-10355 && env -u ANTHROPIC_API_KEY .venv/bin/python -m src.cli render fda-1 --merge-chunks && cp projects/fda-1/output/final.mp4 /mnt/c/data-mybizz-mgt/marketing/brand-assets/wip-videos/fda-1-scenes-en.mp4` |
