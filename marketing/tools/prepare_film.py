"""Put a finished Mybizz film script and its narration into a video_explainer project.

Run in WSL from ~/video_explainer, with video_explainer's own Python:

  prepare  creates projects/<video>/ from marketing/scripts/<video>-*.md and the scene
           voice files in done-audios (<video>-en-sNN.wav): the script word for word,
           each scene's "On screen" note as its picture instruction, the Mybizz colours,
           and the voice files named by scene for the voiceover import.
  brand    sets the Mybizz colours in the project's generated scenes/styles.ts.
           Run after the scenes step, before the storyboard and the render.

  cd ~/video_explainer && .venv/bin/python /mnt/c/data-mybizz-mgt/marketing/tools/prepare_film.py prepare fda-1
  cd ~/video_explainer && .venv/bin/python /mnt/c/data-mybizz-mgt/marketing/tools/prepare_film.py brand fda-1
"""
import argparse
import glob
import json
import os
import re
import shutil
import sys
import wave

HERE = os.path.dirname(os.path.abspath(__file__))
MARKETING = os.path.dirname(HERE)
SCRIPTS = os.path.join(MARKETING, "scripts")
AUDIO = os.path.join(MARKETING, "brand-assets", "done-audios")
VE = os.getcwd()
PROJECTS = os.path.join(VE, "projects")

BLUE = "#0200BD"        # Mybizz Professional Blue
BLUE_2 = "#004FDA"      # Mybizz secondary blue
STYLE = {"background_color": "#FFFFFF", "primary_color": BLUE,
         "secondary_color": BLUE_2, "font_family": "Roboto"}


def read_script(vid):
    found = [f for f in glob.glob(os.path.join(SCRIPTS, f"{vid}-*.md"))
             if not re.search(r"-(fr|de|es|it)\.md$", f)]
    if len(found) != 1:
        sys.exit(f"English script for {vid} not found exactly once: {found}")
    text = open(found[0], encoding="utf-8").read()
    title = re.search(r"^# Script — \S+ (.+)$", text, flags=re.M).group(1).strip()
    body = text.split("## Narration", 1)[1].split("## Outro", 1)[0]
    parts = re.split(r"^\*\*Scene (\d+) — (.*?)\*\*\s*$", body, flags=re.M)
    scenes = []
    for i in range(1, len(parts), 3):
        num, stitle, chunk = int(parts[i]), parts[i + 1].strip(), parts[i + 2]
        lines = [l.strip() for l in chunk.splitlines() if l.strip()]
        cue = next((l for l in lines if l.startswith("*On screen")), "")
        cue = re.sub(r"^\*On screen:\s*|\*$", "", cue).strip()
        narration = " ".join(l for l in lines if not l.startswith("*On screen"))
        scenes.append((num, stitle, cue, narration))
    return found[0], title, scenes


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return s[:40].rstrip("_")


def wav_seconds(path):
    with wave.open(path) as w:
        return w.getnframes() / w.getframerate()


def prepare(vid):
    sys.path.insert(0, VE)
    from src.project.loader import create_project

    src, title, scenes = read_script(vid)
    if os.path.exists(os.path.join(PROJECTS, vid)):
        sys.exit(f"Project projects/{vid} already exists; nothing was changed.")
    audio = {n: os.path.join(AUDIO, f"{vid}-en-s{n:02d}.wav") for n, *_ in scenes}
    missing = [os.path.basename(p) for p in audio.values() if not os.path.exists(p)]
    if missing:
        sys.exit(f"Missing voice files in done-audios: {missing}")

    project = create_project(project_id=vid, title=title, projects_dir=PROJECTS)
    root = str(project.root_dir)
    for d in ("input", "script", "narration", "recordings"):
        os.makedirs(os.path.join(root, d), exist_ok=True)
    shutil.copy2(src, os.path.join(root, "input", "source.md"))

    script_scenes, narr_scenes, total = [], [], 0.0
    for k, (num, stitle, cue, narration) in enumerate(scenes):
        sid = f"s{num:02d}_{slug(stitle)}"
        secs = wav_seconds(audio[num])
        total += secs
        shutil.copy2(audio[num], os.path.join(root, "recordings", f"{sid}.wav"))
        stype = "hook" if k == 0 else ("conclusion" if k == len(scenes) - 1 else "explanation")
        script_scenes.append({
            "scene_id": sid, "scene_type": stype, "title": stitle, "voiceover": narration,
            "visual_cue": {"description": cue, "visual_type": "animation", "elements": [],
                           "duration_seconds": round(secs, 2)},
            "duration_seconds": round(secs, 2),
            "notes": "Mybizz brand: Professional Blue #0200BD and #004FDA on white; no app screens; "
                     "show only what the On screen note and the narration describe.",
        })
        narr_scenes.append({"scene_id": sid, "title": stitle,
                            "duration_seconds": int(round(secs)), "narration": narration})

    json.dump({"title": title, "total_duration_seconds": round(total, 2),
               "scenes": script_scenes, "source_document": "input/source.md"},
              open(os.path.join(root, "script", "script.json"), "w"), indent=2)
    json.dump({"scenes": narr_scenes},
              open(os.path.join(root, "narration", "narrations.json"), "w"), indent=2)

    cfg_path = os.path.join(root, "config.json")
    cfg = json.load(open(cfg_path))
    cfg["video"]["target_duration_seconds"] = int(round(total))
    cfg["tts"] = {"provider": "manual", "voice_id": ""}
    cfg["style"] = STYLE
    json.dump(cfg, open(cfg_path, "w"), indent=2)
    print(f"Prepared projects/{vid}: {len(scenes)} scenes, {total / 60:.1f} minutes of narration")


def brand(vid):
    path = os.path.join(PROJECTS, vid, "scenes", "styles.ts")
    if not os.path.exists(path):
        sys.exit(f"{path} not found: run the scenes step first.")
    s = open(path, encoding="utf-8").read()
    for old, new in (('"#0066FF"', f'"{BLUE}"'), ('"#0088FF"', f'"{BLUE_2}"'),
                     ("rgba(0, 102, 255,", "rgba(2, 0, 189,")):
        s = s.replace(old, new)
    open(path, "w", encoding="utf-8").write(s)
    print(f"Mybizz colours set in projects/{vid}/scenes/styles.ts")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("step", choices=["prepare", "brand"])
    ap.add_argument("video", help="video ID, e.g. fda-1")
    a = ap.parse_args()
    if not os.path.isdir(os.path.join(VE, "src")):
        sys.exit("Run this from ~/video_explainer.")
    prepare(a.video) if a.step == "prepare" else brand(a.video)


if __name__ == "__main__":
    main()
