#!/usr/bin/env python3
"""Factor each prompt into two reusable axes (Option B).

Every Superdesign prompt bundles a *style* (how it looks) and a *structure*
(what page it is). Point-solutions live at one cell of that matrix. This script
factors them apart so they recombine:

  style axis  ->  systems/<slug>/     (DESIGN.md + tokens.css + manifest.json)
  page axis   ->  page-types/<cat>/   (SKILL.md aggregating layout + components)

N styles x M page-types = N*M possible outputs from content we already own.

Auto-scaffolded drafts: token role assignment and prose are best-effort and
marked `REVIEW`. Run an LLM pass (or hand-edit) to promote a draft to canonical.

Run: python3 scripts/factor_prompts.py
"""
import json, re, pathlib, collections, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
SYS_DIR = ROOT / "systems"
PT_DIR = ROOT / "page-types"
HEX = re.compile(r"#[0-9a-fA-F]{3,8}\b")
FONT = re.compile(r"['\"]([A-Z][A-Za-z0-9 ]+(?:Mono|Sans|Serif|Display|Grotesk|Neue)?)['\"]")

# structural categories become page-type skills; the rest are style-led
PAGE_CATEGORIES = {
    "Landing Pages", "Pricing Pages", "Auth & Login", "Dashboards", "Onboarding",
    "Waitlist & Coming Soon", "Forms & Contact", "Blog & Editorial", "E-commerce",
    "Portfolios", "Mobile Apps", "Components",
}


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def parse_prompt(x):
    pr = x.get("prompt")
    if isinstance(pr, dict):
        return pr
    if isinstance(pr, str) and pr.strip().startswith("{"):
        try:
            return json.loads(pr)
        except json.JSONDecodeError:
            return None
    return None


def style_text(d, x):
    """Concatenate every stylistic prose field available."""
    parts = []
    st = d.get("style") if d else None
    if isinstance(st, dict):
        for k in ("description", "prompt", "prompt_typography"):
            if isinstance(st.get(k), str):
                parts.append(st[k])
        for k in ("fonts", "palette"):
            if st.get(k):
                parts.append(json.dumps(st[k], ensure_ascii=False))
    elif isinstance(st, str):
        parts.append(st)
    if not parts:  # plain-text prompt
        if isinstance(x.get("prompt"), str):
            parts.append(x["prompt"])
    parts.append(x.get("description", ""))
    return "\n".join(p for p in parts if p)


def harvest(text):
    colors, seen = [], set()
    for m in HEX.findall(text):
        c = m.lower()
        if c not in seen:
            seen.add(c)
            colors.append(m)
    fonts = []
    for f in FONT.findall(text):
        if f not in fonts and len(f) > 2:
            fonts.append(f)
    return colors[:16], fonts[:6]


def write_system(x, d):
    slug = x["slug"]
    # never clobber a hand-curated system
    mpath = SYS_DIR / slug / "manifest.json"
    if mpath.exists():
        try:
            if json.load(open(mpath)).get("status") == "curated":
                return "skipped-curated"
        except (json.JSONDecodeError, OSError):
            pass
    text = style_text(d, x)
    colors, fonts = harvest(text)
    st = d.get("style") if d else None
    st_desc = st.get("description") if isinstance(st, dict) else (st if isinstance(st, str) else "")
    st_prompt = st.get("prompt", "") if isinstance(st, dict) else ""
    components = d.get("special_ui_components", []) if d else []
    layout = d.get("layout_and_structure", {}) if d else {}
    layout_desc = layout.get("description", "") if isinstance(layout, dict) else ""
    notes = d.get("special_notes", "") if d else ""

    comp_lines = "\n".join(
        f"- **{c.get('component','')}** — {c.get('description','')}"
        for c in components if isinstance(c, dict)
    ) or "_REVIEW: no components captured._"

    design_md = f"""# Design System — {x['title']}

> Category: {x.get('category','')}  ·  Industry: {x.get('industry','')}
> Auto-scaffolded from prompt [`{slug}`](../../prompts/{slug}/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

{st_desc or x.get('description','') or '_REVIEW_'}

## 2. Color Palette & Roles

{_palette_prose(colors)}

## 3. Typography

{_font_prose(fonts)}

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

{_clip(st_prompt) or '_none captured_'}

## 5. Layout

{layout_desc or '_REVIEW_'}

## 6. Components

{comp_lines}

## 7. Motion

{_motion_prose(text)}

## 8. Voice & Brand

{x.get('description','') or '_REVIEW_'}

## 9. Anti-patterns

{notes or '_REVIEW: none captured._'}

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
"""

    manifest = {
        "schemaVersion": "sd-design-system/v1",
        "id": slug,
        "name": x["title"],
        "category": x.get("category", ""),
        "industry": x.get("industry", ""),
        "source": {"type": "prompt", "slug": slug},
        "status": "draft",
        "files": {"design": "DESIGN.md"},
        "extracted": {"colors": colors, "fonts": fonts},
    }
    out = SYS_DIR / slug
    out.mkdir(parents=True, exist_ok=True)
    (out / "DESIGN.md").write_text(design_md)
    # tokens.css dropped: role assignment was guessed by order and often wrong (fg/accent swapped).
    # The prompt README is the source of truth for exact roles.
    (out / "tokens.css").unlink(missing_ok=True)
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))


def _clip(s, n=900):
    s = (s or "").strip()
    return s if len(s) <= n else s[:n] + " …"


def _palette_prose(colors):
    if not colors:
        return "_No colors captured from the source prompt._"
    return "Colors used in this style (the prompt has their exact roles):\n\n" + "\n".join(
        f"- `{c}`" for c in colors
    )


def _font_prose(fonts):
    if not fonts:
        return "_REVIEW: no font families captured._"
    return "\n".join(f"- `{f}`" for f in fonts)


def _motion_prose(text):
    hits = [ln.strip() for ln in re.split(r"[.\n]", text)
            if re.search(r"\b(transition|animat|motion|ease|hover|duration|ms)\b", ln, re.I)]
    return ("REVIEW —\n" + "\n".join(f"- {h}" for h in hits[:5])) if hits else "_REVIEW: none captured._"


def write_page_type(cat, members):
    slug = slugify(cat)
    comp_counter = collections.Counter()
    parts_counter = collections.Counter()
    for x, d in members:
        for c in (d.get("special_ui_components", []) if d else []):
            if isinstance(c, dict) and c.get("component"):
                comp_counter[c["component"]] += 1
        lay = d.get("layout_and_structure", {}) if d else {}
        for pt in (lay.get("prompts", []) if isinstance(lay, dict) else []):
            if isinstance(pt, dict) and pt.get("part"):
                parts_counter[pt["part"]] += 1

    member_rows = "\n".join(
        f"- [{x['title']}](../../prompts/{x['slug']}/) · design {x.get('deslop_score',5)}/10 · {x.get('tryCount',0):,} runs"
        for x, _ in sorted(members, key=lambda m: (m[0].get("deslop_score", 5), m[0].get("tryCount") or 0), reverse=True)
    )
    common_parts = "\n".join(f"- {p}  _(in {n} prompts)_" for p, n in parts_counter.most_common(12)) or "_REVIEW_"
    common_comps = "\n".join(f"- {c}  _(in {n} prompts)_" for c, n in comp_counter.most_common(15)) or "_REVIEW_"

    skill = f"""# Page type — {cat}

> Structure axis. Style-agnostic: pair with any [system](../../systems/) to render.
> Aggregated from {len(members)} prompts in this repo.

## What this page type is

A reusable {cat} generator. Bring a design system (colors, type, motion) and this
skill supplies the structure — sections, layout, and the components users expect.

## Common sections

{common_parts}

## Common components

{common_comps}

## Example — render in a chosen style

```text
Build a {cat.rstrip('s')} using the "<system-id>" design system
(see systems/<system-id>/DESIGN.md). Include the common sections above.
```

## Reference prompts (best-designed first)

{member_rows}
"""
    out = PT_DIR / slug
    out.mkdir(parents=True, exist_ok=True)
    (out / "README.md").write_text(skill)  # renders as the folder page on github.com
    (out / "SKILL.md").write_text(skill)   # kept: referenced by the recombine workflow


def main():
    prompts = json.load(open(ROOT / "prompts.json"))
    by_cat = collections.defaultdict(list)
    n_sys = 0
    for x in prompts:
        d = parse_prompt(x)
        write_system(x, d)
        n_sys += 1
        by_cat[x.get("category", "Other")].append((x, d or {}))
    n_pt = 0
    for cat, members in by_cat.items():
        if cat in PAGE_CATEGORIES:
            write_page_type(cat, members)
            n_pt += 1

    # cleanup: remove orphan folders left by prompts/categories that dropped out
    keep = {x["slug"] for x in prompts}
    orphans = 0
    if SYS_DIR.exists():
        for p in SYS_DIR.iterdir():
            # a system with no matching prompt is dangling (broken back-link) — remove it
            if p.is_dir() and p.name not in keep:
                shutil.rmtree(p); orphans += 1
    pt_keep = {slugify(c) for c in by_cat if c in PAGE_CATEGORIES}
    if PT_DIR.exists():
        for p in PT_DIR.iterdir():
            if p.is_dir() and p.name not in pt_keep:
                shutil.rmtree(p)
    print(f"factored: {n_sys} systems -> systems/  ·  {n_pt} page-types -> page-types/  ·  cleaned {orphans} orphan systems")


if __name__ == "__main__":
    main()
