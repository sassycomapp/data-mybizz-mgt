"""Join a film's intro clip, rendered scenes and outro clip into the finished film.

Run from WSL:
    cd /mnt/c/data-mybizz-mgt/marketing/tools && python3 assemble_film.py fda-1

Inputs (all in marketing/brand-assets):
    done-videos/<video>-intro-<lang>.mp4   presenter intro clip (Google Flow)
    wip-videos/<video>-scenes-<lang>.mp4   rendered scenes with narration (video_explainer)
    done-videos/<outro>-<lang>.mp4         shared outro clip (sc-1 marketing, sc-2 explainer)
Output:
    done-videos/<video>-<lang>.mp4

Every part is brought to 1920x1080 at 30 frames a second, with 48 kHz stereo sound,
so clips of different sizes and sound formats join cleanly.
"""
import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "brand-assets")
DONE = os.path.join(ASSETS, "done-videos")
WIP = os.path.join(ASSETS, "wip-videos")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video", help="video ID, e.g. fda-1")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--outro", default="sc-1", help="sc-1 for marketing films, sc-2 for explainers")
    ap.add_argument("--force", action="store_true", help="replace a finished film that already exists")
    a = ap.parse_args()

    parts = [
        os.path.join(DONE, f"{a.video}-intro-{a.lang}.mp4"),
        os.path.join(WIP, f"{a.video}-scenes-{a.lang}.mp4"),
        os.path.join(DONE, f"{a.outro}-{a.lang}.mp4"),
    ]
    missing = [p for p in parts if not os.path.exists(p)]
    if missing:
        sys.exit("Missing: " + ", ".join(missing))
    out = os.path.join(DONE, f"{a.video}-{a.lang}.mp4")
    if os.path.exists(out) and not a.force:
        sys.exit(f"{out} already exists; add --force to replace it")

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
