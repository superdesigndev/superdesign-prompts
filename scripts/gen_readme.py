#!/usr/bin/env python3
"""Regenerate the auto-managed regions of README.md from prompts.json.

Updates, in place, between HTML-comment markers:
  - the `last synced` badge date
  - the top-prompts gallery  (GALLERY:START / GALLERY:END)
  - the leaderboard table     (LEADERBOARD:START / LEADERBOARD:END)
  - the aggregate stats line   (STATS:START / STATS:END)

Ranking is by copyCount (the most differentiated real-usage signal).
Run: python3 scripts/gen_readme.py [--date YYYY-MM-DD]
"""
import json, re, sys, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
UTM = "utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
IMG_EXT = ("png", "jpg", "jpeg", "gif", "webp")


def num(x, k):
    try:
        return int(x.get(k) or 0)
    except (TypeError, ValueError):
        return 0


def try_url(slug):
    return f"https://superdesign.dev/library/{slug}?{UTM}"


def human(n):
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M".replace(".0M", "M")
    if n >= 1_000:
        return f"{round(n/1000)}K"
    return str(n)


def build_gallery(prompts, cols=4, rows=3):
    # showcase = best-LOOKING (vision pass on the rendered preview, gated to Jason's bar of >=7),
    # not merely most-copied or best-on-paper. visual_score is the truth; deslop is the tiebreak.
    imgs = [p for p in prompts
            if p.get("preview", "").lower().rsplit(".", 1)[-1] in IMG_EXT and num(p, "visual_score") >= 7]
    top = sorted(imgs, key=lambda z: (num(z, "visual_score"), num(z, "deslop_score"), num(z, "tryCount")),
                 reverse=True)[: cols * rows]
    out = ["<table>"]
    for i in range(0, len(top), cols):
        out.append("<tr>")
        for x in top[i : i + cols]:
            out.append(
                f'<td width="{100//cols}%" align="center" valign="top">'
                f'<a href="{try_url(x["slug"])}"><img src="{x["preview"]}" width="200" alt="{x["title"]}"></a><br>'
                f'<sub><b><a href="prompts/{x["slug"]}/">{x["title"]}</a></b><br>{num(x,"tryCount"):,} runs</sub></td>'
            )
        out.append("</tr>")
    out.append("</table>")
    return "\n".join(out)


def build_leaderboard(prompts, n=10):
    # Ranked by DESIGN quality = the vision score on the rendered preview (how it actually looks),
    # deslop then runs as tiebreaks. Runs are near-uniform so they can't discriminate.
    top = sorted(prompts, key=lambda z: (num(z, "visual_score"), num(z, "deslop_score"), num(z, "tryCount")),
                 reverse=True)[:n]
    rows = ["| # | Prompt | Category | Design | Runs | |", "|---|---|---|---|---|---|"]
    for i, x in enumerate(top, 1):
        rows.append(
            f'| {i} | **[{x["title"]}](prompts/{x["slug"]}/)** | {x.get("category","")} | '
            f'{num(x,"visual_score")}/10 | {num(x,"tryCount"):,} | [▶ Try live]({try_url(x["slug"])}) |'
        )
    return "\n".join(rows)


def build_stats(prompts, all_prompts):
    tc = sum(num(x, "tryCount") for x in prompts)
    cc = sum(num(x, "copyCount") for x in prompts)
    tc_all = sum(num(x, "tryCount") for x in all_prompts) if all_prompts else tc
    return (
        f"  <b>{len(prompts)} top prompts</b> · <b>{human(tc)} tries</b> · <b>{human(cc)} copies</b> — "
        f"hand-picked and category-balanced from a <b>{len(all_prompts or prompts)}-prompt live library</b> "
        f"with <b>{human(tc_all)}+ tries</b>.<br>\n"
        f'  Browse all and run any live at <b><a href="https://superdesign.dev/library?{UTM}">superdesign.dev/library</a></b>.'
    )


def replace_region(text, name, body):
    pat = re.compile(
        rf"(<!-- {name}:START[^>]*-->\n).*?(\n<!-- {name}:END -->)", re.DOTALL
    )
    if not pat.search(text):
        raise SystemExit(f"marker {name} not found in README")
    return pat.sub(lambda m: m.group(1) + body + m.group(2), text)


def main():
    date = None
    if "--date" in sys.argv:
        date = sys.argv[sys.argv.index("--date") + 1]
    date = date or datetime.date.today().isoformat()

    prompts = json.load(open(ROOT / "prompts.json"))
    all_path = ROOT / "data" / "all-prompts.json"
    all_prompts = json.load(open(all_path)) if all_path.exists() else None

    readme = (ROOT / "README.md").read_text()
    readme = replace_region(readme, "GALLERY", build_gallery(prompts))
    readme = replace_region(readme, "LEADERBOARD", build_leaderboard(prompts))
    readme = replace_region(readme, "STATS", build_stats(prompts, all_prompts))
    # last-synced badge
    readme = re.sub(
        r"(last%20synced-)[0-9]{4}--[0-9]{2}--[0-9]{2}",
        r"\g<1>" + date.replace("-", "--"),
        readme,
    )
    # prompt-count badge (keeps it honest as the visual floor changes the count)
    readme = re.sub(r"(badge/prompts-)\d+(-blue)", rf"\g<1>{len(prompts)}\g<2>", readme)
    (ROOT / "README.md").write_text(readme)
    print(f"README regenerated · {len(prompts)} prompts · synced {date}")


if __name__ == "__main__":
    main()
