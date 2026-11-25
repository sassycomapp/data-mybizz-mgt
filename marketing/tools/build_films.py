"""Build films ahead of rendering: narration import, word timing, scenes, check, colours, storyboard.

Run from WSL (terminal 2, beside the renders in terminal 1):
    cd ~/video_explainer && .venv/bin/python /mnt/c/data-mybizz-mgt/marketing/tools/build_films.py fda-3 fda-4 cs-1 cs-2 cs-3 cs-4
Show where every film stands, without changing anything:
    cd ~/video_explainer && .venv/bin/python /mnt/c/data-mybizz-mgt/marketing/tools/build_films.py --status fda-3 fda-4 cs-1 cs-2 cs-3 cs-4

Each step that already has its result is skipped, so a stopped run is started again with the
same command and carries on where it stopped. When a scene drawing stops short (Claude's usage
limit), the tool waits 30 minutes and draws that film's scenes again, up to 12 times, so a run
carries on by itself after the limit resets. When every scene is drawn but the check finds a
fault, only the faulty scene is drawn again, at most twice; a fault that remains stops the run and
names the file. A film whose storyboard exists is built.
Every video_explainer command runs without ANTHROPIC_API_KEY, so the API key is never used.
Each finished step is also written to projects/mybizz-build-log.txt with the date and time.
"""
import argparse
import datetime
import glob
import json
import os
import re
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


def check(vid):
    """Run the scene check; return the faulty scene files (empty list when every scene passes)."""
    r = subprocess.run([PY, "-m", "src.cli", "scenes", vid, "--verify", "--no-auto-fix"],
                       cwd=VE, env=ENV, capture_output=True, text=True)
    print(r.stdout, r.stderr, sep="", end="", flush=True)
    if r.returncode == 0:
        return []
    m = re.search(r"Files with remaining errors:\s*(.+)", r.stdout)
    return [f.strip() for f in m.group(1).split(",")] if m else ["(unknown file)"]


def scene_number(vid, filename):
    """Scene number of a scene file, from the script titles (the generator names files after them)."""
    script = json.load(open(os.path.join(PROJECTS, vid, "script", "script.json")))
    for i, s in enumerate(script["scenes"], 1):
        words = re.sub(r"[^a-zA-Z0-9\s]", "", s.get("title", "")).split()
        if "".join(w.capitalize() for w in words) + "Scene.tsx" == filename:
            return i
    return None


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
    faulty = check(vid) if scenes_complete(vid) else None
    waits = 0
    while faulty is None:
        cli("scenes", vid, "--force")
        if not scenes_complete(vid):
            # Scenes missing: Claude stopped answering, usually the usage limit. Wait, then draw again.
            waits += 1
            if waits > MAX_WAITS:
                return False
            log(vid, f"scenes stopped short; waiting {WAIT_MINUTES} minutes before drawing again ({waits} of {MAX_WAITS})")
            time.sleep(WAIT_MINUTES * 60)
            continue
        faulty = check(vid)
    redraws = 0
    while faulty:
        # Every scene drawn but the check found a fault: redraw only the faulty scenes, at most twice.
        redraws += 1
        nums = [scene_number(vid, f) for f in faulty]
        if redraws > 2 or None in nums:
            log(vid, "scene check still finds a fault in " + ", ".join(faulty) + "; ask Claude for the fix")
            return False
        for f, n in zip(faulty, nums):
            log(vid, f"scene check found a fault in {f}; redrawing scene {n} only")
            cli("scenes", vid, "--scene", str(n))
        faulty = check(vid)
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
