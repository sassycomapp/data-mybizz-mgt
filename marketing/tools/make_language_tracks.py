"""Make a finished film's language tracks for YouTube's multi-language audio.

A language track is one sound file, the same length as the English film, that plays
the presenter's intro, the narration and the outro in another language over the
English pictures. YouTube takes it as an extra audio track of the one English video.

Run from WSL:
    cd /mnt/c/data-mybizz-mgt/marketing/tools && python3 make_language_tracks.py fda-1 --langs fr de --preview

How the track is built:
    intro   the sound of done-videos/<video>-intro-<lang>.mp4, fitted to the English intro's length
    scenes  each scene's voice file done-audios/<video>-<lang>-sNN.wav, started at the moment the
            English scene's narration starts; a scene too long for its place is spoken slightly faster
    outro   the sound of done-videos/<outro>-<lang>.mp4, fitted to the English outro's length
Scene start times come from the film's video_explainer storyboard
(~/video_explainer/projects/<video>/storyboard/storyboard.json), using the same arithmetic as
the render. The narration is brought to the English narration's loudness.

Output:
    done-audios/<video>-track-<lang>.wav             the language track, uploaded to YouTube
    wip-videos/<video>-preview-<lang>.mp4 (--preview) the English film with the language track,
                                                     for watching before upload
"""
import argparse
import json
import math
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "brand-assets")
DONE = os.path.join(ASSETS, "done-videos")
WIP = os.path.join(ASSETS, "wip-videos")
AUDIO = os.path.join(ASSETS, "done-audios")
VE = os.path.expanduser("~/video_explainer")

FPS = 30
RATE = 48000
SAFETY = 0.3      # seconds kept clear before the next scene's narration starts
FAST_WARN = 1.15  # a scene spoken more than 15% faster is reported for a shorter translation


def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)


def seconds(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
               "-of", "default=nw=1:nk=1", path]).stdout
    return float(out.strip())


def mean_volume(paths):
    cmd = ["ffmpeg", "-hide_banner", "-nostats"]
    for p in paths:
        cmd += ["-i", p]
    inputs = "".join(f"[{i}:a]aresample={RATE},aformat=channel_layouts=mono[a{i}];" for i in range(len(paths)))
    joined = "".join(f"[a{i}]" for i in range(len(paths)))
    cmd += ["-filter_complex", f"{inputs}{joined}concat=n={len(paths)}:v=0:a=1,volumedetect",
            "-f", "null", "-"]
    err = subprocess.run(cmd, check=True, capture_output=True, text=True).stderr
    return float(re.search(r"mean_volume: (-?[\d.]+) dB", err).group(1))


def scene_slots(video, total):
    """Start time and room, in seconds, of each scene's narration in the rendered scenes."""
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


def fitted(label, idx, length, tempo=1.0, gain_db=0.0):
    """Filter text that turns input idx into exactly `length` seconds of 48 kHz stereo sound."""
    n = round(length * RATE)
    f = f"[{idx}:a]aresample={RATE},aformat=sample_fmts=fltp:channel_layouts=stereo"
    if tempo > 1.0:
        f += f",atempo={tempo:.4f}"
    if gain_db:
        f += f",volume={gain_db:.2f}dB"
    return f + f",apad=whole_len={n},atrim=end_sample={n},asetpts=N/SR/TB[{label}]"


def make_track(video, lang, outro, preview):
    intro_en = os.path.join(DONE, f"{video}-intro-en.mp4")
    scenes_en = os.path.join(WIP, f"{video}-scenes-en.mp4")
    outro_en = os.path.join(DONE, f"{outro}-en.mp4")
    film_en = os.path.join(DONE, f"{video}-en.mp4")
    intro_l = os.path.join(DONE, f"{video}-intro-{lang}.mp4")
    outro_l = os.path.join(DONE, f"{outro}-{lang}.mp4")
    needed = [intro_en, scenes_en, outro_en, film_en, intro_l, outro_l]

    scenes_len = seconds(scenes_en)
    slots, board_len = scene_slots(video, scenes_len)
    if abs(board_len - scenes_len) > 0.5:
        sys.exit(f"The storyboard ({board_len:.2f} s) does not match {os.path.basename(scenes_en)} "
                 f"({scenes_len:.2f} s); the scene times cannot be trusted.")
    voice_l = [os.path.join(AUDIO, f"{video}-{lang}-s{n:02d}.wav") for n, _, _ in slots]
    voice_en = [os.path.join(AUDIO, f"{video}-en-s{n:02d}.wav") for n, _, _ in slots]
    missing = [p for p in needed + voice_l + voice_en if not os.path.exists(p)]
    if missing:
        sys.exit("Missing: " + ", ".join(missing))

    gain = mean_volume(voice_en) - mean_volume(voice_l)
    intro_len, outro_len = seconds(intro_en), seconds(outro_en)

    inputs = [intro_l] + voice_l + [outro_l]
    parts = [fitted("p0", 0, intro_len)]
    report = []
    for k, ((n, start, room), path) in enumerate(zip(slots, voice_l), start=1):
        spoken = seconds(path)
        tempo = max(1.0, spoken / max(room - SAFETY, 0.5))
        if tempo > 1.0:
            report.append((n, tempo))
        parts.append(fitted(f"p{k}", k, room, tempo, gain))
    last = len(inputs) - 1
    parts.append(fitted(f"p{last}", last, outro_len))
    graph = ";".join(parts) + ";" + "".join(f"[p{i}]" for i in range(len(inputs))) + \
        f"concat=n={len(inputs)}:v=0:a=1[out]"

    out = os.path.join(AUDIO, f"{video}-track-{lang}.wav")
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
    for p in inputs:
        cmd += ["-i", p]
    cmd += ["-filter_complex", graph, "-map", "[out]", "-c:a", "pcm_s16le", out]
    subprocess.run(cmd, check=True)

    track_len, film_len = seconds(out), seconds(film_en)
    print(f"made {out}")
    print(f"  length {track_len:.2f} s; English film {film_len:.2f} s; difference {track_len - film_len:+.2f} s")
    print(f"  narration loudness changed by {gain:+.1f} dB to match the English narration")
    for n, tempo in report:
        flag = "  <- shorten this scene's translation" if tempo > FAST_WARN else ""
        print(f"  scene {n}: spoken {100 * (tempo - 1):.0f}% faster to fit{flag}")
    if not report:
        print("  every scene fits without speeding up")

    if preview:
        prev = os.path.join(WIP, f"{video}-preview-{lang}.mp4")
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", film_en, "-i", out,
                        "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                        "-shortest", "-movflags", "+faststart", prev], check=True)
        print(f"  preview {prev}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video", help="video ID, e.g. fda-1")
    ap.add_argument("--langs", nargs="+", default=["fr", "de", "es", "it"], choices=["fr", "de", "es", "it"])
    ap.add_argument("--outro", default="sc-1", help="sc-1 for marketing films, sc-2 for explainers")
    ap.add_argument("--preview", action="store_true", help="also make the English film with each track, to watch")
    a = ap.parse_args()
    for lang in a.langs:
        make_track(a.video, lang, a.outro, a.preview)


if __name__ == "__main__":
    main()
