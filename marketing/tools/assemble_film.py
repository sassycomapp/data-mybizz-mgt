"""Join a film's intro clip, rendered scenes and outro clip into the finished film, in one language.

Run from WSL:
    cd /mnt/c/data-mybizz-mgt/marketing/tools && python3 assemble_film.py fda-1
    cd /mnt/c/data-mybizz-mgt/marketing/tools && python3 assemble_film.py fda-1 --lang de

Inputs (all in marketing/brand-assets):
    done-videos/<video>-intro-<lang>.mp4   presenter intro clip (Google Flow), used as made
    wip-videos/<video>-scenes-en.mp4       rendered scenes with English narration (video_explainer)
    done-audios/<video>-<lang>-sNN.wav     scene narration in French, German, Spanish or Italian
    done-videos/<outro>-<lang>.mp4         shared outro clip (sc-1 marketing, sc-2 explainer), used as made
Output:
    done-videos/<video>-<lang>.mp4

English: the rendered scenes keep their own narration.
Other languages: the tool first makes wip-videos/<video>-scenes-<lang>.mp4, the English scene pictures
with that language's narration. Each scene's narration starts where the English scene's narration
starts (times from ~/video_explainer/projects/<video>/storyboard/storyboard.json, by the same arithmetic
as the render), at its recorded level, copied to both stereo channels. A scene too long for its place
is sped up just enough to fit, without changing pitch. Every scene's final pace, in syllables a second,
is checked against the average pace of native speakers reading aloud (Pellegrino, Coupe and Marsico,
2011): a scene faster than that average is marked "too fast" and the film is not made.

Every part is brought to 1920x1080 at 30 frames a second, with 48 kHz stereo sound,
so clips of different sizes and sound formats join cleanly.
"""
import argparse
import json
import math
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MARKETING = os.path.dirname(HERE)
ASSETS = os.path.join(MARKETING, "brand-assets")
DONE = os.path.join(ASSETS, "done-videos")
WIP = os.path.join(ASSETS, "wip-videos")
AUDIO = os.path.join(ASSETS, "done-audios")
SCRIPTS = os.path.join(MARKETING, "scripts")
VE = os.path.expanduser("~/video_explainer")

FPS = 30
RATE = 48000
SAFETY = 0.3  # seconds kept clear before the next scene's narration starts
# Average syllables per second of native speakers reading aloud (Pellegrino et al. 2011, table 2)
NATURAL = {"fr": 7.18, "de": 5.97, "it": 6.99, "es": 7.82}
VOWELS = {"fr": "aeiouyàâéèêëîïôûùüœæ", "de": "aeiouyäöü", "es": "aeiouáéíóúü", "it": "aeiouàèéìíòóùú"}


def seconds(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=nw=1:nk=1", path], check=True, capture_output=True, text=True).stdout
    return float(out.strip())


def scene_texts(video, lang):
    found = [f for f in os.listdir(SCRIPTS) if f.startswith(f"{video}-") and f.endswith(f"-{lang}.md")]
    if len(found) != 1:
        sys.exit(f"Script for {video} ({lang}) not found exactly once: {found}")
    text = open(os.path.join(SCRIPTS, found[0]), encoding="utf-8").read()
    body = text.split("## Narration", 1)[1].split("## Outro", 1)[0]
    parts = re.split(r"^\*\*Scene (\d+) — .*?\*\*\s*$", body, flags=re.M)
    out = {}
    for i in range(1, len(parts), 2):
        lines = [l.strip() for l in parts[i + 1].splitlines()]
        out[int(parts[i])] = " ".join(l for l in lines if l and not l.startswith("*On screen"))
    return out


def syllables(text, lang):
    """Spoken syllables: each group of vowels in a word is one syllable; in French a word-final
    silent e (e, es, ent after a consonant) is not spoken. Accurate to within a few percent."""
    count = 0
    for word in re.findall(r"[^\W\d_]+", text.lower()):
        if lang == "fr" and len(word) > 2:
            word = re.sub(r"(?<=[^aeiouyàâéèêëîïôûùüœæ])(e|es|ent)$", "", word)
        count += len(re.findall(f"[{VOWELS[lang]}]+", word))  # elided l', d', qu' count 0
    return count


def scene_slots(video, total):
    """Scene number, start time and room, in seconds, of each scene's narration in the rendered scenes."""
    path = os.path.join(VE, "projects", video, "storyboard", "storyboard.json")
    if not os.path.exists(path):
        sys.exit(f"Storyboard not found: {path}")
    board = json.load(open(path))
    buffer = (board.get("audio") or {}).get("buffer_between_scenes_seconds", 1.0)
    starts, frame = [], 0
    for s in board["scenes"]:
        starts.append(frame / FPS)
        frame += math.ceil((s["audio_duration_seconds"] + buffer + s.get("visual_padding_seconds", 0)) * FPS)
    ends = starts[1:] + [total]
    nums = [int(re.match(r"s(\d+)", s["id"]).group(1)) for s in board["scenes"]]
    return [(n, a, b - a) for n, a, b in zip(nums, starts, ends)], frame / FPS


def language_scenes(video, lang):
    """Make wip-videos/<video>-scenes-<lang>.mp4: English scene pictures with the language's narration."""
    scenes_en = os.path.join(WIP, f"{video}-scenes-en.mp4")
    if not os.path.exists(scenes_en):
        sys.exit(f"Missing: {scenes_en}")
    total = seconds(scenes_en)
    slots, board_len = scene_slots(video, total)
    if abs(board_len - total) > 0.5:
        sys.exit(f"The storyboard ({board_len:.2f} s) does not match {os.path.basename(scenes_en)} "
                 f"({total:.2f} s); the scene times cannot be trusted.")
    voices = [os.path.join(AUDIO, f"{video}-{lang}-s{n:02d}.wav") for n, _, _ in slots]
    missing = [p for p in voices if not os.path.exists(p)]
    if missing:
        sys.exit("Missing: " + ", ".join(missing))
    texts = scene_texts(video, lang)

    print(f"pace limit for {lang}: {NATURAL[lang]:.2f} syllables a second")
    parts, fast = [], 0
    for k, ((n, start, room), path) in enumerate(zip(slots, voices)):
        spoken = seconds(path)
        tempo = max(1.0, spoken / max(room - SAFETY, 0.5))
        rate = syllables(texts[n], lang) / (spoken / tempo)
        flag = ""
        if rate > NATURAL[lang]:
            flag, fast = "  <- too fast: shorten this scene's translation", fast + 1
        print(f"  scene {n}: {rate:.2f} syllables a second, sped up {100 * (tempo - 1):.0f}%{flag}")
        samples = round(room * RATE)
        f = f"[{k + 1}:a]aresample={RATE},aformat=sample_fmts=fltp:channel_layouts=mono"
        if tempo > 1.0:
            f += f",atempo={tempo:.4f}"
        # one channel copied unchanged into both stereo channels: no level change
        f += f",pan=stereo|c0=c0|c1=c0,apad=whole_len={samples},atrim=end_sample={samples},asetpts=N/SR/TB[p{k}]"
        parts.append(f)
    if fast:
        sys.exit(f"{fast} scene(s) too fast; the film is not made.")

    out = os.path.join(WIP, f"{video}-scenes-{lang}.mp4")
    graph = ";".join(parts) + ";" + "".join(f"[p{k}]" for k in range(len(parts))) + \
        f"concat=n={len(parts)}:v=0:a=1[a]"
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", scenes_en]
    for p in voices:
        cmd += ["-i", p]
    cmd += ["-filter_complex", graph, "-map", "0:v", "-map", "[a]", "-c:v", "copy",
            "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.3f}", out]
    subprocess.run(cmd, check=True)
    print("made", out)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video", help="video ID, e.g. fda-1")
    ap.add_argument("--lang", default="en", choices=["en", "fr", "de", "es", "it"])
    ap.add_argument("--outro", default="sc-1", help="sc-1 for marketing films, sc-2 for explainers")
    ap.add_argument("--force", action="store_true", help="replace a finished film that already exists")
    a = ap.parse_args()

    out = os.path.join(DONE, f"{a.video}-{a.lang}.mp4")
    if os.path.exists(out) and not a.force:
        sys.exit(f"{out} already exists; add --force to replace it")
    intro = os.path.join(DONE, f"{a.video}-intro-{a.lang}.mp4")
    outro = os.path.join(DONE, f"{a.outro}-{a.lang}.mp4")
    missing = [p for p in (intro, outro) if not os.path.exists(p)]
    if missing:
        sys.exit("Missing: " + ", ".join(missing))
    scenes = os.path.join(WIP, f"{a.video}-scenes-en.mp4") if a.lang == "en" else language_scenes(a.video, a.lang)
    parts = [intro, scenes, outro]
    if not os.path.exists(scenes):
        sys.exit(f"Missing: {scenes}")

    norm = []
    for i in range(3):
        norm.append(
            f"[{i}:v]scale=1920:1080:force_original_aspect_ratio=decrease,"
            f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=white,fps=30,setsar=1,format=yuv420p[v{i}];"
            f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo[a{i}]"
        )
    graph = ";".join(norm) + ";[v0][a0][v1][a1][v2][a2]concat=n=3:v=1:a=1[v][a]"
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-stats", "-y"]
    for p in parts:
        cmd += ["-i", p]
    cmd += ["-filter_complex", graph, "-map", "[v]", "-map", "[a]",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
            "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True)
    print("made", out)


if __name__ == "__main__":
    main()
