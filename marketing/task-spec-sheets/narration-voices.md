---
title: "narration-voices"
---
# Task Spec Sheet — Mybizz Narration Voices

**Task:** C2 in `marketing-plan.xlsx`
**Owner:** David
**Unblocks:** every narrated video in the marketing plan (explainer, help and teardown videos, the narration in long-form videos, and the teardown intro and outro)

---

## 1. Result

Mybizz makes all narration on David's own PC, in WSL, with two free, open-source voice tools. Neither needs an account, a key, a card or an internet connection once installed, and neither has a daily limit.

| Item | Value |
|---|---|
| English, French, Spanish, Italian | **Kokoro** (Kokoro-82M, Apache 2.0 licence), Python package `kokoro` |
| German | **Piper** (`piper-tts` 1.8.0), with Piper voice files |
| Installed in | WSL, `~/tools/kokoro` (Python environment `~/tools/kokoro/.venv`) |
| Piper voice files | `~/tools/kokoro/piper-voices` |
| Helper | `espeak-ng` (installed with `apt`), needed by Kokoro for French, Spanish and Italian |
| Finished voice files | `C:\data-mybizz-mgt\marketing\brand-assets\done-audios\`, on the PC only; voice files are never stored in GitHub |
| Sound format | WAV, 24,000 Hz, mono (Kokoro); WAV (Piper) |

---

## 2. How It Works

- **Why on the PC.** The PC has 8 GB of memory and no graphics card for AI work. Kokoro (82 million parameters) and Piper both run on the processor in well under 1 GB of memory, at about the speed of speech, so a full narration runs in the background while other work continues.
- **The voices.** Each presenter has one fixed voice per language, chosen by ear (section 5). The voices are ready-made: neither tool copies the presenter's Google Flow voice, so the narration voice is the closest match chosen by ear.
- **The accent.** Kokoro's British English voices speak British English by themselves (language code `b`); no accent instruction is sent.
- **One line per call for short clips, one scene per call for films.** Each script scene is narrated as one piece and saved as one file, so a fault is fixed by remaking one scene, not the whole film.
- **File names.** Every voice file is named after its video ID and language, in lower case: `sc-3-en.wav`, `sc-4-de.wav`. Film narration adds the scene number: `fda-1-en-s03.wav`.

---

## 3. Set-Up (WSL terminal, once)

1. Kokoro's engine (PyTorch for processors without a graphics card):

```
cd ~ && mkdir -p ~/tools/kokoro && cd ~/tools/kokoro && python3 -m venv .venv && .venv/bin/pip install --upgrade pip && .venv/bin/pip install torch --index-url https://download.pytorch.org/whl/cpu
```

2. Kokoro and its language helper:

```
cd ~/tools/kokoro && sudo apt-get update && sudo apt-get install -y espeak-ng && .venv/bin/pip install "kokoro>=0.9.4" soundfile
```

3. Piper and its voices:

```
cd ~/tools/kokoro && .venv/bin/pip install piper-tts && mkdir -p piper-voices && cd piper-voices && ../.venv/bin/python -m piper.download_voices de_DE-kerstin-low de_DE-thorsten-medium
```

Kokoro downloads each voice from Hugging Face (`hexgrad/Kokoro-82M`) the first time it is used and keeps it on the PC. The messages "unauthenticated requests to the HF Hub" and "Defaulting repo_id to hexgrad/Kokoro-82M" are expected and need no action.

**Check:** the test in section 4 writes a playable file.

---

## 4. Making Narration

### Kokoro (English, French, Spanish, Italian)

The language code and voice come from section 5. Each entry in `lines` is one file: language code, voice, file name, text.

```
cd ~/tools/kokoro && .venv/bin/python - <<'EOF'
from kokoro import KPipeline
import soundfile as sf, numpy as np
out = "/mnt/c/data-mybizz-mgt/marketing/brand-assets/done-audios/"
lines = [
 ("b","bf_lily","sc-3-en","Hello. I'm Sarah, an AI presenter, with a quick look at your website."),
]
pipes = {}
for lang, voice, name, text in lines:
    p = pipes.setdefault(lang, KPipeline(lang_code=lang))
    audio = np.concatenate([np.asarray(a) for _, _, a in p(text, voice=voice)])
    sf.write(out + name + ".wav", audio, 24000)
    print("made", name)
print("done")
EOF
```

### Film narration (Kokoro, all scenes of one or more scripts)

`marketing/tools/narrate.py` reads each script in `marketing/scripts/`, takes the narration of every scene (without the scene headings and "On screen" notes) and writes one file per scene, `<video>-<language>-sNN.wav`, to `done-audios`. A scene file that already exists is skipped, so a stopped run carries on where it stopped; a faulty scene is remade by deleting its file and running again.

```
cd /mnt/c/data-mybizz-mgt/marketing/tools && ~/tools/kokoro/.venv/bin/python narrate.py --lang en --voice bf_lily fda-1 fda-2 fda-3 fda-4 cs-1 cs-2 cs-3 cs-4
```

`--lang` is `en`, `fr`, `es` or `it`, and `--voice` is the presenter's voice for that language (section 5). Narration uses Kokoro's own speaking pace, which business viewers follow easily and which keeps their interest. Translated scripts are named like their English script with the language at the end, for example `fda-1-the-five-minute-rule-fr.md`.

### Piper (German)

```
cd ~/tools/kokoro/piper-voices && ../.venv/bin/python -m piper -m de_DE-kerstin-low --data-dir . -f /mnt/c/data-mybizz-mgt/marketing/brand-assets/done-audios/sc-3-de.wav -- "Hallo. Ich bin Sarah, eine KI-Moderatorin, mit einem kurzen Blick auf Ihre Website."
```

The warning "Missing phoneme from id map" means one rare sound mark is skipped; it needs no action unless the sentence sounds wrong.

### Listening check

Every file is played once before it is used: the words are complete, the pronunciation is natural, and the file ends cleanly with no noise.

---

## 5. The Presenter Voices

| Presenter | Language | Tool | Language code | Voice |
|---|---|---|---|---|
| Sarah | English (British) | Kokoro | `b` | `bf_lily` |
| Sarah | French | Kokoro | `f` | `ff_siwis` |
| Sarah | Spanish | Kokoro | `e` | `ef_dora` |
| Sarah | Italian | Kokoro | `i` | `if_sara` |
| Sarah | German | Piper | — | `de_DE-kerstin-low` |
| Brian | English (British) | Kokoro | `b` | `bm_daniel` |
| Brian | French | Piper | — | `fr_FR-tom-medium` |
| Brian | Spanish | Kokoro | `e` | `em_alex` |
| Brian | Italian | Kokoro | `i` | `im_nicola` |
| Brian | German | Piper | — | `de_DE-thorsten-medium` |

Sarah's voices are chosen by ear and used. Brian's French, Spanish, Italian and German voices are confirmed by ear before his first translated narration; Piper downloads `fr_FR-tom-medium` with `python -m piper.download_voices fr_FR-tom-medium` in `piper-voices`.

---

## 6. Accounts Kept but Not Used for Narration

| Account | Detail |
|---|---|
| Google AI Studio | `mybizzlive@gmail.com`; project **Mybizz** (`mybizz-515510`, number 81918688433); key **Gemini API Key**, free tier, kept in David's password manager only. Google's speech models run on the paid tier only. |
| Hugging Face | Free account on `mybizzlive@gmail.com`; password in David's password manager. Its free web pages have a small daily allowance. |
| Google payments profile | Individual, South Africa, legal name David Coleman, profile ID 5401-0178-4710; holds no card; no billing account exists. |
