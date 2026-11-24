"""Narrate Mybizz film scripts with Kokoro, one voice file per scene.

Reads each script in marketing/scripts/, takes the text under "## Narration"
(without scene headings and "On screen" notes), and writes one file per scene to
marketing/brand-assets/done-audios/ as <video>-<lang>-sNN.wav.
A scene file that already exists is skipped, so a stopped run carries on where it stopped;
--force remakes scenes that already exist. --speed sets the pace: 0.85, the Mybizz narration
pace, is 15% slower than Kokoro's own pace (1.0).

Run from WSL with Kokoro's Python (task-spec-sheets/narration-voices.md):
  ~/tools/kokoro/.venv/bin/python narrate.py --lang en --voice bf_lily fda-1 fda-2
"""
import argparse
import glob
import os
import re
import sys

import numpy as np
import soundfile as sf
import subprocess

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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="en", choices=sorted(LANG_CODES))
    ap.add_argument("--voice", default="bf_lily")
    ap.add_argument("--speed", type=float, default=0.85, help="speaking pace; 0.85 is the Mybizz pace")
    ap.add_argument("--force", action="store_true", help="remake scenes that already exist")
    ap.add_argument("videos", nargs="+", help="video IDs, e.g. fda-1 cs-2")
    a = ap.parse_args()
    if a.lang == "de":
        pipe = None
    else:
        from kokoro import KPipeline
        pipe = KPipeline(lang_code=LANG_CODES[a.lang], repo_id="hexgrad/Kokoro-82M")
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
            if pipe is None:
                # Piper: length scale is the inverse of speed (0.85 -> 1.18)
                subprocess.run([sys.executable, "-m", "piper", "-m", a.voice, "--data-dir", PIPER_VOICES,
                                "--length-scale", f"{1 / a.speed:.2f}", "-f", dest, "--", text], check=True)
                info = sf.info(dest)
                print("made", name, f"{info.duration:.0f} s", flush=True)
                continue
            audio = np.concatenate([np.asarray(x) for _, _, x in pipe(text, voice=a.voice, speed=a.speed)])
            sf.write(dest, audio, 24000)
            print("made", name, f"{len(audio) / 24000:.0f} s", flush=True)
    print("done")


if __name__ == "__main__":
    main()
