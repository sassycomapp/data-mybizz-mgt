#!/usr/bin/env python3
"""List and translate the on-screen text of video_explainer scene files.

extract  <scenes_dir> <texts.json>          list every on-screen text, numbered
apply    <scenes_dir> <texts.json> <out_dir> write translated texts into copies

texts.json after extract:   [{"id": 1, "file": "X.tsx", "en": "Draft reply", "text": ""}, ...]
Claude fills "text" with the translation. Empty "text" keeps the English.
apply never changes <scenes_dir>; it writes changed copies of the .tsx files
(and copies every other file) into <out_dir>, then checks each .tsx parses.

Needs: node, and the typescript package (video_explainer/remotion/node_modules).
Set TS_DIR to the folder that contains node_modules/typescript if not found.
"""
import json, os, shutil, subprocess, sys
from pathlib import Path

JS = r"""
const path = require('path');
const fs = require('fs');
const ts = require(require.resolve('typescript', {paths: [process.env.TS_DIR]}));
const A = process.argv.slice(1);
const mode = A[0], file = A[1];
const src = fs.readFileSync(file, 'utf8');
const sf = ts.createSourceFile(file, src, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
const found = [];   // {start,end,kind,text}
const hasLetter = s => /\p{L}/u.test(s.replace(/\p{Extended_Pictographic}/gu, ''));
// string literals are on-screen text only when they sit in JSX text, or in a
// text-like property / array element; style values, keys, ids and colours are not.
const SKIP_PROPS = new Set(['key','id','icon','color','style','type','src','fill','stroke','d','points','transform','position','display','alignItems','justifyContent','flexDirection','textAlign','boxSizing','overflow','whiteSpace','verticalAlign','fontFamily','fontWeight','background','backgroundColor','border','boxShadow','opacity','cursor','alignSelf','patternUnits','viewBox','xmlns','className','extrapolateLeft','extrapolateRight','textTransform','letterSpacing','fontStyle','pointerEvents','mixBlendMode','filter','width','height','top','left','right','bottom','gap','padding','margin','content','lineHeight','borderRadius','fontSize','flex','maxWidth','minWidth','zIndex','boxSizing']);
const BRAND = new Set(['Mybizz','Mybizz FDA','Mybizz CS','FDA','CS','Mybizz Shop']);
function isCss(s){ return /^(#[0-9a-f]{3,8}|rgba?\(|hsla?\(|url\(|linear-gradient|none|line-through|underline|normal|italic|bold|pointer|auto|absolute|relative|flex|block|inline|center|nowrap|hidden|visible|\d+(\.\d+)?(px|%|em|rem)?)/i.test(s); }
function add(node, text, kind){
  const t = text;
  if (!hasLetter(t)) return;
  if ((t.match(/\p{L}/gu) || []).length < 2) return;        // single initials (avatars)
  if (/[¿¡]/.test(t)) return;                                 // Spanish demo text stays Spanish
  if (kind === 'tplpart' && !/\p{L}{3,}/u.test(t)) return;   // path / CSS fragments
  if (BRAND.has(t.trim())) return;
  if (isCss(t.trim())) return;
  found.push({start: node.getStart(sf), end: node.getEnd(), kind, text: t, node});
}
function inCodeContext(n){
  // string literal inside: import/export, comparison, call args like useCurrentFrame, index access, switch case
  const p = n.parent;
  if (!p) return true;
  if (ts.isImportDeclaration(p) || ts.isExportDeclaration(p)) return true;
  if (ts.isElementAccessExpression(p) && p.argumentExpression === n) return true;
  if (ts.isBinaryExpression(p) && [ts.SyntaxKind.EqualsEqualsEqualsToken, ts.SyntaxKind.ExclamationEqualsEqualsToken, ts.SyntaxKind.EqualsEqualsToken, ts.SyntaxKind.ExclamationEqualsToken].includes(p.operatorToken.kind)) return true;
  if (ts.isCaseClause(p)) return true;
  if (ts.isCallExpression(p) && !ts.isArrayLiteralExpression(p)) return true;
  if (ts.isAsExpression(p)) return true;
  if (ts.isJsxAttribute(p)) return true; // attributes (id, fill, ...) are not text
  if (ts.isPropertyAssignment(p) && p.initializer === n) {
    const name = p.name.getText(sf).replace(/['"]/g,'');
    return SKIP_PROPS.has(name);
  }
  return false;
}
function visit(n){
  if (ts.isJsxText(n)) {
    const raw = n.getText(sf);
    if (raw.trim()) add(n, raw, 'jsx');
  } else if (ts.isStringLiteral(n) || ts.isNoSubstitutionTemplateLiteral(n)) {
    // skip comments inside by construction (not nodes); skip code contexts
    if (!inCodeContext(n)) add(n, n.text, ts.isStringLiteral(n) ? 'str' : 'tpl');
  } else if (ts.isTemplateExpression(n)) {
    // template with ${...}: translate the fixed parts only if they hold letters
    if (!inCodeContext(n)) {
      const parts = [n.head, ...n.templateSpans.map(s => s.literal)];
      for (const p of parts) add(p, p.text, 'tplpart');
    }
  }
  ts.forEachChild(n, visit);
}
visit(sf);
// drop strings nested inside a found jsx/tpl node duplicates & overlapping
found.sort((a,b)=>a.start-b.start);
const out = [];
for (const f of found) { if (out.length && f.start < out[out.length-1].end) continue; out.push(f); }
if (mode === 'extract') {
  console.log(JSON.stringify(out.map(f => ({text: f.text, kind: f.kind}))));
} else {
  const map = JSON.parse(fs.readFileSync(A[2], 'utf8')); // [{en,text}] by position
  let res = src;
  for (let i = out.length - 1; i >= 0; i--) {
    const f = out[i];
    const tr = map[i];
    if (!tr || !tr.text || tr.text === f.text) continue;
    if (tr.en !== f.text.trim()) { console.error('MISMATCH at ' + i + ': ' + tr.en + ' != ' + f.text); process.exit(2); }
    let rep;
    const esc = s => s.replace(/\\/g,'\\\\');
    if (f.kind === 'jsx') {
      // keep leading/trailing whitespace of the original node; make JSX-safe
      const lead = f.text.match(/^\s*/)[0], trail = f.text.match(/\s*$/)[0];
      const body = tr.text.replace(/[{}<>]/g, c => '{' + JSON.stringify(c) + '}');
      rep = lead + body + trail;
    } else if (f.kind === 'str') {
      const q = src[f.start];
      rep = q + tr.text.replace(/\\/g,'\\\\').split(q).join('\\' + q) + q;
    } else if (f.kind === 'tpl') {
      rep = '`' + tr.text.replace(/\\/g,'\\\\').replace(/`/g,'\\`').replace(/\$\{/g,'\\${') + '`';
    } else { // tplpart: raw segment only
      rep = tr.text.replace(/\\/g,'\\\\').replace(/`/g,'\\`');
      const full = src.slice(f.start, f.end);
      const rawStart = f.start;
      // template head/middle/tail tokens include delimiters; keep them
      const open = full.startsWith('`') ? '`' : '}';
      const close = full.endsWith('`') ? '`' : '${';
      rep = open + rep + close;
    }
    res = res.slice(0, f.start) + rep + res.slice(f.end);
  }
  const sf2 = ts.createSourceFile(file, res, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
  const diags = sf2.parseDiagnostics || [];
  if (diags.length) { console.error('PARSE ERROR: ' + diags[0].messageText); process.exit(3); }
  fs.writeFileSync(A[3], res);
}
"""

def node(args, ts_dir):
    env = dict(os.environ, TS_DIR=str(ts_dir))
    r = subprocess.run(["node", "-e", JS, "--"] + args, capture_output=True, text=True, env=env)
    return r

def find_ts(explicit):
    for c in [explicit, os.environ.get("TS_DIR"), Path.home()/"video_explainer"/"remotion"]:
        if c and (Path(c)/"node_modules"/"typescript").exists():
            return Path(c)
    sys.exit("typescript not found. Set TS_DIR to the folder containing node_modules/typescript.")

def tsx_files(d):
    return sorted(p for p in Path(d).glob("*.tsx"))

def extract(scenes, out, ts_dir):
    rows = []
    for p in tsx_files(scenes):
        r = node(["extract", str(p)], ts_dir)
        if r.returncode: sys.exit(f"{p.name}: {r.stderr}")
        for it in json.loads(r.stdout):
            rows.append({"id": len(rows) + 1, "file": p.name, "en": it["text"].strip(), "kind": it["kind"], "text": ""})
    Path(out).write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(rows)} on-screen texts in {len(tsx_files(scenes))} scenes -> {out}")

def apply(scenes, texts, out, ts_dir):
    rows = json.loads(Path(texts).read_text(encoding="utf-8"))
    out = Path(out)
    if out.exists() and any(out.iterdir()):
        sys.exit(f"{out} already has files; choose an empty or new folder.")
    shutil.copytree(scenes, out, dirs_exist_ok=True)
    changed = 0
    for p in tsx_files(scenes):
        mine = [{"en": r["en"], "text": r["text"]} for r in rows if r["file"] == p.name]
        tmp = out / (p.name + ".map.json")
        tmp.write_text(json.dumps(mine, ensure_ascii=False), encoding="utf-8")
        r = node(["apply", str(p), str(tmp), str(out / p.name)], ts_dir)
        tmp.unlink()
        if r.returncode: sys.exit(f"{p.name}: {r.stderr}")
        changed += sum(1 for m in mine if m["text"] and m["text"] != m["en"])
    print(f"{changed} texts written into {out} (originals untouched); every scene parses.")

if __name__ == "__main__":
    a = sys.argv[1:]
    ts_dir = find_ts(None)
    if len(a) == 3 and a[0] == "extract": extract(a[1], a[2], ts_dir)
    elif len(a) == 4 and a[0] == "apply": apply(a[1], a[2], a[3], ts_dir)
    else: sys.exit(__doc__)
