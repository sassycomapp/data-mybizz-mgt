"""Build films ahead of rendering: narration import, word timing, scenes, check, colours, storyboard.

Run from WSL (terminal 2, beside the renders in terminal 1):
    cd ~/video_explainer && .venv/bin/python /mnt/c/data-mybizz-mgt/marketing/tools/build_films.py fda-3 fda-4 cs-1 cs-2 cs-3 cs-4
Show where every film stands, without changing anything:
    cd ~/video_explainer && .venv/bin/python /mnt/c/data-mybizz-mgt/marketing/tools/build_films.py --status fda-3 fda-4 cs-1 cs-2 cs-3 cs-4

Each step that already has its result is skipped, so a stopped run is started again with the
same command and carries on where it stopped. When a scene drawing stops short (Claude's usage
limit), the tool waits 30 minutes and draws that film's scenes again, up to 12 times, so a run
carries on by itself after the limit resets. When every scene is drawn but the check finds a
fault, the film's scenes are drawn once more; a second fault stops the run. A film whose storyboard exists is built.
Every video_explainer command runs without ANTHROPIC_API_KEY, so the API key is never used.
Each finished step is also written to projects/mybizz-build-log.txt with the date and time.
"""
import argparse
import datetime
import glob
import json
import os
import subprocess
import sys
import time

VE = os.path.expanduser("~/video_explainer")
PROJECTS = os.path.join(VE, "projects")
PY = os.path.join(VE, ".venv", "bin", "python")
PREPARE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prepare_film.py")
LOG = os.path.join(PROJECTS, "mybizz-build-log.txt")
WAIT_MINUTES = 30   # pause after a scene drawing that stopped short (Claude usage limit)
MAX_WAITS = 12      # 12 pauses of 30 minutes cover more than one 5-hour usage window
ENV = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}


def log(vid, text):
    line = f"{datetime.datetime.now():%Y-%m-%d %H:%M} {vid}: {text}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def run(args):
    return subprocess.run(args, cwd=VE, env=ENV).returncode == 0


def cli(*args):
    return run([PY, "-m", "src.cli", *args])


def scenes_complete(vid):
    """True when every scene of the script has its scene file; the syntax check runs separately."""
    p = os.path.join(PROJECTS, vid)
    try:
        wanted = len(json.load(open(os.path.join(p, "narration", "narrations.json")))["scenes"])
    except (OSError, ValueError, KeyError):
        return False
    return len(glob.glob(os.path.join(p, "scenes", "*.tsx"))) == wanted


def state(vid):
    p = os.path.join(PROJECTS, vid)
    if os.path.exists(os.path.join(p, "storyboard", "storyboard.json")):
        return "built (storyboard ready; render next)"
    if os.path.exists(os.path.join(p, "scenes", "styles.ts")) and scenes_complete(vid):
        return "scenes drawn; check, colours and storyboard to do"
    if os.path.exists(os.path.join(p, "scenes", "styles.ts")):
        return "scenes partly drawn; all scenes are drawn again on the next run"
    if os.path.exists(os.path.join(p, "voiceover", "manifest.json")):
        return "words timed; scenes to draw"
    if os.path.isdir(p):
        return "imported; words to time"
    return "not started"


def build(vid):
    p = os.path.join(PROJECTS, vid)
    if os.path.exists(os.path.join(p, "storyboard", "storyboard.json")):
        log(vid, "already built, skipped")
        return True
    if not os.path.isdir(p):
        if not run([PY, PREPARE, "prepare", vid]):
            return False
        log(vid, "imported")
    if not os.path.exists(os.path.join(p, "voiceover", "manifest.json")):
        if not cli("voiceover", vid, "--provider", "manual", "--audio-dir", f"projects/{vid}/recordings"):
            return False
        log(vid, "words timed")
    scenes_ok = scenes_complete(vid) and cli("scenes", vid, "--verify", "--no-auto-fix")
    waits = 0
    redraws = 0
    while not scenes_ok:
        cli("scenes", vid, "--force")
        if not scenes_complete(vid):
            # Scenes missing: Claude stopped answering, usually the usage limit. Wait, then draw again.
            waits += 1
            if waits > MAX_WAITS:
                return False
            log(vid, f"scenes stopped short; waiting {WAIT_MINUTES} minutes before drawing again ({waits} of {MAX_WAITS})")
            time.sleep(WAIT_MINUTES * 60)
            continue
        scenes_ok = cli("scenes", vid, "--verify", "--no-auto-fix")
        if not scenes_ok:
            # Every scene drawn but the check found a fault: draw the film once more, then stop.
            redraws += 1
            if redraws > 1:
                return False
            log(vid, "scene check found a fault; drawing the scenes once more")
    log(vid, "scenes drawn and checked")
    if not run([PY, PREPARE, "brand", vid]):
        return False
    if not cli("storyboard", vid):
        return False
    log(vid, "built (storyboard ready; render next)")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", action="store_true", help="only show where each film stands")
    ap.add_argument("videos", nargs="+")
    a = ap.parse_args()
    if a.status:
        for vid in a.videos:
            print(f"{vid}: {state(vid)}")
        return
    for vid in a.videos:
        if not build(vid):
            log(vid, f"stopped at: {state(vid)}; run the same command again to carry on")
            sys.exit(1)
    print("All films built.")


if __name__ == "__main__":
    main()
