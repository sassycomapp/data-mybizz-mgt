"""Narrate Mybizz film scripts with Kokoro, one voice file per scene.

Reads each script in marketing/scripts/, takes the text under "## Narration"
(without scene headings and "On screen" notes), and writes one file per scene to
marketing/brand-assets/done-audios/ as <video>-<lang>-sNN.wav.
A scene file that already exists is skipped, so a stopped run carries on where it stopped;
--force remakes scenes that already exist. --speed sets the pace: English runs at 0.85, the Mybizz
narration pace, 15% slower than the voice's own pace (1.0); French, German, Spanish and Italian run at
the voice's own pace (1.0), so the longer translated sentences fit the English scenes.

German is spoken by Piper. Piper's sound converter splits the "ch" of "ich" (sign ç) into "c" and a
separate cedilla, which the German voice does not know and drops; the tool joins every such split sign
back into the single sign the voice knows before speaking, and reports how many it joined.

--say speaks one text to one file instead of a script (shared clips), for example:
  ~/tools/kokoro/.venv/bin/python narrate.py --lang de --voice de_DE-kerstin-low --speed 0.85 --say "Hallo." --out sc-3-de.wav

Run from WSL with Kokoro's Python (task-spec-sheets/narration-voices.md):
  ~/tools/kokoro/.venv/bin/python narrate.py --lang en --voice bf_lily fda-1 fda-2
"""
import argparse
import glob
import os
import re
import sys
import unicodedata

import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
MARKETING = os.path.dirname(HERE)
SCRIPTS = os.path.join(MARKETING, "scripts")
OUT = os.path.join(MARKETING, "brand-assets", "done-audios")
LANG_CODES = {"en": "b", "fr": "f", "es": "e", "it": "i", "de": None}  # German is spoken by Piper
PIPER_VOICES = os.path.expanduser("~/tools/kokoro/piper-voices")


def scenes(path):
    text = open(path, encoding="utf-8").read()
    body = text.split("## Narration", 1)[1].split("## Outro", 1)[0]
    parts = re.split(r"^\*\*Scene (\d+) — .*?\*\*\s*$", body, flags=re.M)
    for i in range(1, len(parts), 2):
        num = int(parts[i])
        lines = [l.strip() for l in parts[i + 1].splitlines()]
        lines = [l for l in lines if l and not l.startswith("*On screen")]
        yield num, " ".join(lines)


class Speaker:
    """One voice: Kokoro for English, French, Spanish and Italian; Piper for German."""

    def __init__(self, lang, voice, speed):
        self.voice, self.speed = voice, speed
        if lang == "de":
            from piper import PiperVoice
            self.piper = PiperVoice.load(os.path.join(PIPER_VOICES, f"{voice}.onnx"))
            self.kokoro = None
        else:
            from kokoro import KPipeline
            self.kokoro = KPipeline(lang_code=LANG_CODES[lang], repo_id="hexgrad/Kokoro-82M")

    def speak(self, text, dest):
        if self.kokoro:
            audio = np.concatenate([np.asarray(x) for _, _, x in self.kokoro(text, voice=self.voice, speed=self.speed)])
            sf.write(dest, audio, 24000)
            return len(audio) / 24000, ""
        from piper import SynthesisConfig
        cfg = SynthesisConfig(length_scale=1 / self.speed)  # length scale is the inverse of speed
        known = self.piper.config.phoneme_id_map
        parts, joined, unknown = [], 0, set()
        for sentence in self.piper.phonemize(text):
            signs = []
            for sign in sentence:
                if signs and unicodedata.combining(sign):
                    whole = unicodedata.normalize("NFC", signs[-1] + sign)
                    if whole in known:
                        signs[-1] = whole
                        joined += 1
                        continue
                signs.append(sign)
            unknown |= {x for x in signs if x not in known}
            audio = np.asarray(self.piper.phoneme_ids_to_audio(self.piper.phonemes_to_ids(signs), cfg))
            if audio.dtype == np.int16:
                audio = audio.astype(np.float32) / 32768
            parts.append(audio.astype(np.float32).ravel())
        rate = self.piper.config.sample_rate
        audio = np.concatenate(parts)
        sf.write(dest, audio, rate)
        note = f", {joined} split sign(s) joined"
        if unknown:
            note += ", UNKNOWN SIGNS: " + " ".join(f"U+{ord(c[0]):04X}" for c in sorted(unknown))
        return len(audio) / rate, note


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="en", choices=sorted(LANG_CODES))
    ap.add_argument("--voice", default="bf_lily")
    ap.add_argument("--speed", type=float, default=None,
                    help="speaking pace; default 0.85 for English, 1.0 for the other languages")
    ap.add_argument("--force", action="store_true", help="remake scenes that already exist")
    ap.add_argument("--say", help="speak this text instead of a script")
    ap.add_argument("--out", help="with --say: the file name in done-audios, e.g. sc-3-de.wav")
    ap.add_argument("videos", nargs="*", help="video IDs, e.g. fda-1 cs-2")
    a = ap.parse_args()
    if a.speed is None:
        a.speed = 0.85 if a.lang == "en" else 1.0
    if bool(a.say) != bool(a.out) or bool(a.say) == bool(a.videos):
        sys.exit("Give either video IDs, or --say with --out.")
    speaker = Speaker(a.lang, a.voice, a.speed)
    if a.say:
        secs, note = speaker.speak(a.say, os.path.join(OUT, a.out))
        print("made", a.out, f"{secs:.0f} s{note}")
        return
    for vid in a.videos:
        suffix = "" if a.lang == "en" else f"-{a.lang}"
        found = glob.glob(os.path.join(SCRIPTS, f"{vid}-*{suffix}.md"))
        found = [f for f in found if a.lang != "en" or not re.search(r"-(fr|de|es|it)\.md$", f)]
        if len(found) != 1:
            sys.exit(f"Script for {vid} ({a.lang}) not found exactly once: {found}")
        for num, text in scenes(found[0]):
            name = f"{vid}-{a.lang}-s{num:02d}.wav"
            dest = os.path.join(OUT, name)
            if os.path.exists(dest) and not a.force:
                print("skip", name)
                continue
            secs, note = speaker.speak(text, dest)
            print("made", name, f"{secs:.0f} s{note}", flush=True)
    print("done")


if __name__ == "__main__":
    main()
