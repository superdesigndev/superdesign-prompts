#!/usr/bin/env python3
"""build_data.py — the DATA layer of the pipeline (was export_v4 in scratchpad).

Pulls the live library, filters to team-authored, category-balances to 150, and writes the
DATA artifacts: prompts.json, prompts.csv, PROMPTS.md, per-prompt prompts/<slug>/README.md,
and downloads preview images. Team-only, PII-safe.

It does NOT write the top-level README.md or repo-maintained files — that boundary is
deliberate (README is owned by scripts/gen_readme.py). Pipeline: build_data → factor_prompts
→ gen_readme. See scripts/README.md."""
import json, os, csv, glob, pathlib, collections, shutil, urllib.request, mimetypes, re

ROOT = pathlib.Path(os.path.expanduser("~/Workspace/superdesign/superdesign-prompts-mirror"))
LIB = "https://superdesign.dev/library"
UTM = "utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
SKILL = "https://github.com/superdesigndev/superdesign-skill"
BLOG = "https://superdesign.dev/blog/how-to-make-claude-code-ui-look-good"
PER_CAT, HERO, CAP = 12, 30, 150
ALLOWED = {"shirley lou", "zhou jason", "jason zhou", "superdesign"}

def score(it): return (it.get("copyCount") or 0) * 2 + (it.get("tryCount") or 0)
def cname(x): return ((x.get("creator") or {}).get("name") or "").strip()
def try_url(s): return f"{LIB}/{s}?{UTM}"

# ---- page-type taxonomy (primary category, most-specific first) ----
CATS = ["Landing Pages", "Pricing Pages", "Auth & Login", "Dashboards", "AI Chat", "Onboarding",
        "Waitlist & Coming Soon", "Forms & Contact", "Blog & Editorial", "E-commerce",
        "Portfolios", "Mobile Apps", "Components", "Animations & Backgrounds",
        "Design Systems & Styles", "Other"]
STYLE_KW = ["style", "brutalis", "glassmorph", "neumorph", "monochrome", "minimalist",
            "cinematic", "noir", "luxury", "bauhaus", "win98", "sketch", "clay", "kinetic",
            "aurora", "liquid", "cyber", "retro", "vintage", "material", "flat design",
            "playful", "industrial", "avant-garde", "newsprint", "grunge", "editorial style"]

def has(t, *w): return any(x in t for x in w)

def page_category(it):
    tags = " ".join((it.get("tags") or [])).lower()
    txt = f"{it.get('title') or ''} {it.get('slug','')}".lower()
    T = tags + " " + txt
    tl = [t.strip().lower() for t in (it.get("tags") or [])]  # exact tag list (avoids "form" in "platform")
    if has(tags, "pricing", "billing-toggle", "three-tier", "comparison-table") or "pricing" in txt:
        return "Pricing Pages"
    if has(tags, "auth", "signup", "signin", "login") or has(txt, "login", "sign in", "sign-in", "signup", "sign up"):
        return "Auth & Login"
    # AI chat / chatbot / conversational UIs (before Dashboards/Components, which a chat
    # sidebar+composer layout would otherwise match on the 'sidebar'/'card' substrings)
    if has(tags, "ai-chat", "chatbot", "chat-interface", "chat-ui", "conversational", "llm-chat",
           "messaging-ui", "chat-app", "ai-assistant") \
            or has(txt, "chat interface", "chatbot", "ai chat", "ai-chat", "conversational"):
        return "AI Chat"
    # a landing page that merely *shows* a dashboard (tagged 'dashboard' + 'landing') is not a dashboard
    if "dashboard" in txt or has(txt, "admin panel", "admin dashboard", "console") \
            or (any("dashboard" in t for t in tl) and not any("landing" in t for t in tl)):
        return "Dashboards"
    if "onboarding" in T: return "Onboarding"
    if has(tags, "waitlist", "coming-soon") or has(txt, "waitlist", "coming soon", "coming-soon"):
        return "Waitlist & Coming Soon"
    if any(t in ("form", "forms", "contact", "contact-form", "contact form", "newsletter", "newsletter-signup") for t in tl) or has(txt, "contact form", "contact-form"):
        return "Forms & Contact"
    if has(tags, "blog", "article", "news", "magazine") or has(txt, "blog", "article", "magazine"):
        return "Blog & Editorial"
    if has(tags, "ecommerce", "e-commerce", "shopify", "apparel", "store", "cart", "checkout") \
            or has(txt, "shop", "store", "cart", "checkout", "ecommerce", "commerce"):
        return "E-commerce"
    if "portfolio" in T: return "Portfolios"
    if has(tags, "mobile app", "mobile") or "mobile" in txt: return "Mobile Apps"
    if has(tags, "ui component", "button", "modal", "dialog", "navbar", "table", "data-table",
            "tabs", "accordion", "tooltip", "dropdown", "sidebar", "card") or \
            has(txt, "button", "cursor", "counter", "card-", "pill-nav", "drawer", "toggle",
                "carousel", "coverflow", "loading", "-list", "folder", "shiny-text", "rolodex",
                "typing", "menu", "modal", "dialog", "navbar", "table"):
        return "Components"
    if has(tags, "animation", "background", "scroll animation", "text animation") or \
            has(txt, "background", "animation", "scroll"):
        return "Animations & Backgrounds"
    if any(k in txt for k in STYLE_KW) or (("style" in tags) and not has(tags, "landing page", "saas landing")):
        return "Design Systems & Styles"
    if has(tags, "landing page", "saas landing", "sass landing", "page", "high conversion page",
            "product launch") or has(txt, "landing", "one pager", "one-pager"):
        return "Landing Pages"
    return "Other"

# ---- industry axis (secondary, most-specific first) ----
INDUSTRIES = ["SaaS", "AI & Tech", "Dev Tools", "Agency & Studio", "Health & Wellness",
              "Fashion & Beauty", "Real Estate", "Finance & Crypto", "Food & Drink",
              "E-commerce & Retail", "Personal & Portfolio", "General"]

def industry(it):
    tags = " ".join((it.get("tags") or [])).lower()
    txt = f"{it.get('title') or ''} {it.get('slug','')}".lower()
    T = tags + " " + txt
    if has(T, "developer-tool", "dev-tool", "developer tool", "api", "sdk", "cli"): return "Dev Tools"
    if has(T, "ai first product", "ai-first", " ai ", "gpt", "agent", "machine learning", "ml ") or txt.startswith("ai"):
        return "AI & Tech"
    if has(T, "wellness", "health", "fitness", "meditation", "medical", "care", "therapy"): return "Health & Wellness"
    if has(T, "fashion", "apparel", "beauty", "cosmetic", "clothing", "jewelry"): return "Fashion & Beauty"
    if has(T, "real estate", "property", "realty"): return "Real Estate"
    if has(T, "fintech", "crypto", "finance", "web3", "bank", "payment", "trading"): return "Finance & Crypto"
    if has(T, "food", "restaurant", "cafe", "coffee", "menu", "drink"): return "Food & Drink"
    if has(T, "agency", "studio", "creative studio"): return "Agency & Studio"
    if has(T, "ecommerce", "e-commerce", "shopify", "store", "retail", "shop"): return "E-commerce & Retail"
    if has(T, "saas", "platform", "b2b"): return "SaaS"
    if has(T, "portfolio", "personal"): return "Personal & Portfolio"
    return "General"

def thumb_url(it):
    t = it.get("thumbnail")
    if isinstance(t, dict): return t.get("url")
    return t if isinstance(t, str) and t.startswith("http") else None

def download(url, dest):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "sd/3"})
        with urllib.request.urlopen(req, timeout=60) as r:
            ext = mimetypes.guess_extension((r.headers.get("Content-Type", "")).split(";")[0].strip()) or ".png"
            if ext == ".jpe": ext = ".jpg"
            dest.with_suffix(ext).write_bytes(r.read())
        return True
    except Exception as e:
        print(f"    ! img fail {url[:45]}: {e}"); return False

def img_rel(slug):
    # Prefer a still image (renders in <img> everywhere); fall back to whatever exists.
    d = ROOT / "prompts" / slug
    for ext in ("png", "jpg", "jpeg", "webp", "gif"):
        if (d / f"preview.{ext}").exists():
            return f"prompts/{slug}/preview.{ext}"
    h = glob.glob(str(d / "preview.*"))
    return f"prompts/{slug}/{pathlib.Path(h[0]).name}" if h else None

def video_rel(slug):
    p = ROOT / "prompts" / slug / "preview.mp4"
    return f"prompts/{slug}/preview.mp4" if p.exists() else None

def slugify(s): return s.lower().replace(" & ", "--").replace(" ", "-")

# Prompts where OUR brand leaks into the template content (footer wordmarks, mailto, summary).
BRAND_STRIP = {
    "red-noir-style", "deep-red-style-5b01cb", "glassmorphism-style",
    "luxury-focused-design-system", "bold-editorial-style", "high-energy-onboarding",
    "midnight-editorial-style-5f0a22",
}

def apply_patches(it):
    """Deterministic content fixes applied post-load (survive re-syncs). Patches the prompt/tags in place."""
    slug = it.get("slug"); pr = it.get("prompt") or ""
    # brand-neutralize globally: our brand must never ship inside a reusable template.
    # (try_url is a separate field, so the live-library backlinks stay intact.)
    pr = pr.replace("superdesign.dev", "example.com")
    pr = pr.replace("SUPERDESIGN", "ACME").replace("Superdesign", "Acme")
    if slug in BRAND_STRIP:
        pr = re.sub(r"\bSUPER\b(?!\s*[-#.:])", "ACME", pr)  # bare SUPER wordmark, not CSS/props
    # vendor fragile third-party assets -> stable equivalents (avoid rot in shipped templates)
    pr = re.sub(r"https://framerusercontent\.com/images/\S*?width=(\d+)&height=(\d+)",
                r"https://placehold.co/\1x\2", pr)  # someone's Framer project assets
    pr = pr.replace(
        "https://grainy-gradients.vercel.app/noise.svg",
        "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E"
        "%3CfeTurbulence type='fractalNoise' baseFrequency='0.85'/%3E%3C/filter%3E"
        "%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.35'/%3E%3C/svg%3E")
    if slug == "developer-tool-dashboardonboarding":
        pr = pr.replace("#33333 ", "#333333 ").replace("#33333;", "#333333;")
        it["tags"] = ["saas" if t == "sass" else t for t in (it.get("tags") or [])]
    it["prompt"] = pr
    return it

def main():
    items = json.load(open(ROOT / "data" / "all-prompts.json"))
    total = len(items)
    dspath = ROOT / "data" / "deslop-scores.json"
    DS = json.load(open(dspath)) if dspath.exists() else {}  # de-slop quality scores (spec-text pass)
    vspath = ROOT / "data" / "visual-scores.json"
    VS = json.load(open(vspath)) if vspath.exists() else {}  # rendered-PREVIEW visual quality (vision pass, 2026-07-09)
    VISUAL_FLOOR = 5  # drop prompts whose preview renders sparse/generic/janky (visual_score <= 4). Dial here.
    dfbpath = ROOT / "data" / "detail-fallback.json"
    DFB = json.load(open(dfbpath)) if dfbpath.exists() else {}  # STOPGAP (2026-07-09): the live /library/<slug>
    # detail page crashes for 21 legacy prompts whose `special_ui_components` are plain strings, not
    # {prompt} objects — StructuredPromptView does `comp.prompt.slice(...)` → throws (platform PR #1110).
    # For those, point "Try live" at the standalone previewUrl render instead of the crashing page.
    # REMOVE this + data/detail-fallback.json once platform PR #1110 (the normalize fix) deploys.
    team = [x for x in items if cname(x).lower() in ALLOWED]
    # Curation exclusions (2026-07-09, from the de-slop pass — docs/PROMPT-MIRROR-CURATION-ISSUES):
    EXCLUDE = {
        # non-design SOPs / cheatsheets (not design prompts at all)
        "email-template", "slide-deck", "product-feature", "web-app-onboarding",
        "animation-threejs-animation", "mobile-app-app-store-preview", "one-pager",
        # indigo/blue "slop" — the exact thing we mock (Inter + indigo/blue + card grid)
        "analytics-dashboard", "luminous-ethereal-glassmorphism-onboarding",
        "linear-inspired-developer-tool-dashboard", "futuristic-sass-landing-page", "clean-fluid",
        # broken AND thin (score <=3): compile error / trademarked copy / debug cruft / no spec
        "radiant-prompt-input", "jelly-squish-button", "side-drawer-navigation",
        "gsap-horizontal-scroll", "dynamic-data-display",
        # non-design mislabels surfaced scoring the backfills (image-gen / SEO skill / ops-YAML)
        "interactive-virtual-character", "landing-page-seo-keyword-page", "social-media-post",
    }
    team = [x for x in team if x["slug"] not in EXCLUDE]
    for x in team: x["_cat"], x["_ind"], x["_s"] = page_category(x), industry(x), score(x)
    team.sort(key=lambda x: x["_s"], reverse=True)

    # ---- category-balanced selection: top PER_CAT per category + global HERO ----
    chosen, seen = [], set()
    def add(x):
        if x["slug"] not in seen: seen.add(x["slug"]); chosen.append(x)
    for x in team[:HERO]: add(x)                      # hero: never drop the most-copied
    bycat = collections.defaultdict(list)
    for x in team: bycat[x["_cat"]].append(x)
    for c in CATS:
        for x in bycat.get(c, [])[:PER_CAT]: add(x)
    chosen.sort(key=lambda x: x["_s"], reverse=True)
    chosen = chosen[:CAP]
    # visual-quality floor: the vision pass judged how the RENDERED preview looks. That "is it
    # premium/filled" bar is valid for PAGES & STYLES, but NOT for components & effects — those are
    # MEANT to be a single focused element on a minimal canvas (a button, a cursor glow, a text
    # animation, a loading state). Judge those by FUNCTION (usage + spec), never by fill, or the
    # floor wrongly nukes good components as "sparse". (Jason, 2026-07-09.) No backfill on the pages.
    FUNCTION_JUDGED = {"Components", "Animations & Backgrounds"}
    before = len(chosen)
    chosen = [x for x in chosen
              if x["_cat"] in FUNCTION_JUDGED or VS.get(x["slug"], {}).get("visual_score", 5) >= VISUAL_FLOOR]
    print(f"visual floor >={VISUAL_FLOOR} (pages/styles only): dropped {before - len(chosen)}, kept {len(chosen)}")
    keep = {x["slug"] for x in chosen}

    # cleanup stale folders + ensure images
    pdir = ROOT / "prompts"; pdir.mkdir(exist_ok=True)
    for p in pdir.iterdir():
        if p.is_dir() and p.name not in keep: shutil.rmtree(p)
    dl = 0
    for x in chosen:
        d = pdir / x["slug"]; d.mkdir(parents=True, exist_ok=True)
        if not glob.glob(str(d / "preview.*")):
            u = thumb_url(x)
            if u and download(u, d / "preview"): dl += 1
    print(f"downloaded {dl} new images")

    recs = []
    for i, it in enumerate(chosen, 1):
        apply_patches(it)  # brand-strip + content fixes before serializing
        raw = cname(it)
        author = "Jason Zhou" if raw.lower() in ("zhou jason", "jason zhou") else (raw or "Superdesign")
        recs.append({"rank": i, "slug": it["slug"], "title": (it.get("title") or it["slug"]).strip(),
                     "category": it["_cat"], "industry": it["_ind"], "tags": it.get("tags") or [],
                     "description": (it.get("description") or "").strip(), "prompt": (it.get("prompt") or "").strip(),
                     "copyCount": it.get("copyCount") or 0, "tryCount": it.get("tryCount") or 0,
                     "try_url": DFB.get(it["slug"]) or try_url(it["slug"]), "preview": img_rel(it["slug"]),
                     "video": video_rel(it["slug"]), "author": author,
                     "deslop_score": DS.get(it["slug"], {}).get("deslop_score", 5),
                     "deslop_flags": DS.get(it["slug"], {}).get("flags", []),
                     "visual_score": VS.get(it["slug"], {}).get("visual_score", 5),
                     "visual_flag": VS.get(it["slug"], {}).get("flag", "")})

    # ---- per-prompt README ----
    for r in recs:
        d = pdir / r["slug"]
        fm = {k: r[k] for k in ("title", "slug", "category", "industry", "tags", "copyCount", "tryCount", "author")}
        fm["try_url"] = r["try_url"]
        b = ["---", *[f"{k}: {json.dumps(v)}" for k, v in fm.items()], "---", "", f"# {r['title']}", ""]
        if r["description"]: b += [r["description"], ""]
        if r["preview"]: b += [f'<img src="{pathlib.Path(r["preview"]).name}" alt="{r["title"]}" width="640">', ""]
        if r.get("video"): b += [f'▶ **[Watch the animated preview]({pathlib.Path(r["video"]).name})** (MP4)', ""]
        b += ["## Prompt", "", "```text", r["prompt"], "```", "",
              f"**▶ [Try it live →]({r['try_url']})**", "",
              f"**Use it in your coding agent:** install the [Superdesign skill]({SKILL}), then:", "",
              "```bash", f'superdesign get-prompts --slugs "{r["slug"]}" --json', "```", "",
              f"*{r['copyCount']:,} copies · {r['tryCount']:,} tries · {r['category']} · {r['industry']} · "
              f"{', '.join(r['tags'][:4])}*", ""]
        (d / "README.md").write_text("\n".join(b))

    # ---- machine-readable exports ----
    slim = [{k: r[k] for k in ("rank", "slug", "title", "category", "industry", "tags", "description",
             "copyCount", "tryCount", "deslop_score", "visual_score", "try_url", "preview", "video", "author", "prompt")} for r in recs]
    (ROOT / "prompts.json").write_text(json.dumps(slim, indent=2))
    with open(ROOT / "prompts.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["rank", "slug", "title", "category", "industry", "tags",
                                       "copyCount", "tryCount", "try_url", "author", "prompt"])
        for r in recs:
            w.writerow([r["rank"], r["slug"], r["title"], r["category"], r["industry"], "|".join(r["tags"]),
                        r["copyCount"], r["tryCount"], r["try_url"], r["author"], r["prompt"]])
    pm = [f"# All prompts (full text mirror)\n\nTop {len(recs)} team-authored prompts from the "
          f"[Superdesign prompt library]({LIB}), category-balanced. Generated from `prompts.json`.\n"]
    for r in recs:
        pm += [f"## {r['rank']}. {r['title']}", f"`{r['category']}` · `{r['industry']}` · "
               f"{r['copyCount']:,} copies · [try live]({r['try_url']})", ""]
        if r["description"]: pm += [r["description"], ""]
        pm += ["```text", r["prompt"], "```", "", "---", ""]
    (ROOT / "PROMPTS.md").write_text("\n".join(pm))

    # ---- README (dual axis: page type + industry) ----
    bycat = collections.OrderedDict((c, []) for c in CATS)
    byind = collections.OrderedDict((c, []) for c in INDUSTRIES)
    for r in recs: bycat[r["category"]].append(r); byind[r["industry"]].append(r)
    ccount = {c: len(v) for c, v in bycat.items() if v}
    icount = {c: len(v) for c, v in byind.items() if v}

    R = ["# Stop shipping AI-slop UI", "",
         "> Coding agents write great code and generic interfaces: default shadcn, same fonts, no "
         "taste. This is a library of **usage-ranked design prompts, each with a live preview**, that "
         "give your agent design direction so the UI it ships actually looks designed. "
         f"Powered by [Superdesign]({LIB}?{UTM}).", "",
         "<!-- badges: fill OWNER/REPO on publish -->",
         f"![prompts](https://img.shields.io/badge/prompts-{len(recs)}-blue) "
         "![ranked](https://img.shields.io/badge/ranked%20by-real%20usage-brightgreen) "
         "![for](https://img.shields.io/badge/for-Claude%20Code%20%2B%20Cursor-black) "
         "![license](https://img.shields.io/badge/code-MIT-informational)", "",
         f"**Curated from a live library with 1.7M+ real prompt runs.** These are the top {len(recs)} "
         "team-authored prompts, balanced across every page type and ranked by how many builders "
         "actually used them.", "",
         "## Why your AI UI looks generic (and how to fix it)", "",
         "AI-generated UI all looks the same because the agent has **no taste to anchor to** — so it "
         "reaches for the same fonts, the same card grid, the same indigo-500. Every prompt here is a "
         "**full design spec** (exact colors, type, spacing, motion, layout), ranked by how many real "
         "builders actually used it. Hand one to your agent and it builds to a real spec instead of a "
         "default.", "",
         "## How to use these — 3 ways to de-slop", "",
         "**1. Copy → paste into your agent** (zero setup, works everywhere)  ",
         "Find a look below, open it, copy the prompt, then tell Claude Code / Cursor:  ",
         "> *\"Redesign my dashboard using this design spec: [paste]\"*", "",
         "**2. Install the skill** (best — your agent picks and applies it for you)  ",
         "```bash",
         "npx skills add superdesigndev/superdesign-skill",
         "```",
         "Then just ask: *\"/superdesign make my pricing page not look like AI slop\"*. The agent "
         f"searches this library, pulls the right prompt, and applies it to your code. [Skill repo]({SKILL}).", "",
         "**3. Try it live** (see it first, then take the code)  ",
         "Hit **▶ Try live** on any prompt to generate and iterate it on the Superdesign canvas, then "
         "copy the result into your project.", "",
         f"> New to this? Start with [how to make Claude Code UI look good]({BLOG}).", "",
         "## Why this library is different", "",
         "| | Most prompt lists / DESIGN.md repos | This one |", "|---|---|---|",
         "| Ranking | Curated by opinion | **Ranked by real usage** (copies + tries) |",
         "| Format | Static text / markdown, no preview | **Live preview + one-click run** |",
         "| Freshness | Manual, goes stale | **Auto-synced** from a live product |",
         "| Coverage | A few categories | **Every page type + industry**, Webflow-style |", "",
         "## How this fits with the Superdesign skill", "",
         f"This repo is the **registry**; the [Superdesign skill]({SKILL}) is the **runtime** — like an "
         "npm registry and the npm CLI. They stack, they don't compete:", "",
         "| | This library (registry) | Superdesign skill (runtime) |",
         "|---|---|---|",
         "| Role | Prompts, previews, usage rankings, metadata | Reads the registry, applies a prompt to *your* code |",
         "| You | Browse, discover, copy, cite | Install once, then invoke |",
         "| Analogy | npm registry / Homebrew formulae | npm / brew (the client) |",
         "| Optimized for | Discovery + credibility | In-agent generating & iterating |", "",
         f"`superdesign get-prompts` pulls straight from this library's data. **Browse here, run it there.**", "",
         "## Browse by page type", ""]
    for c in CATS:
        if ccount.get(c): R.append(f"- [{c}](#{slugify(c)}) ({ccount[c]})")
    R += ["", "## Browse by industry", ""]
    for c in INDUSTRIES:
        if icount.get(c): R.append(f"- [{c}](#by-industry) ({icount[c]})")
    R += ["", "[Comparison](#superdesign-vs-other-ai-design-tools) · [FAQ](#faq) · [Contributing](#contributing)", ""]

    for c in CATS:
        rows = bycat[c]
        if not rows: continue
        R += [f"## {c}", "", "| Preview | Prompt | Industry | Copies | |", "|---|---|---|---|---|"]
        for r in sorted(rows, key=lambda x: -x["copyCount"]):
            prev = f'<img src="{r["preview"]}" width="200">' if r["preview"] else "—"
            R.append(f'| {prev} | **[{r["title"]}](prompts/{r["slug"]}/)**<br><sub>{", ".join(r["tags"][:3])}</sub> '
                     f'| {r["industry"]} | {r["copyCount"]:,} | [▶ Try live]({r["try_url"]}) |')
        R.append("")

    R += ['<a id="by-industry"></a>', "## By industry", ""]
    for c in INDUSTRIES:
        rows = byind.get(c)
        if not rows: continue
        R.append(f"**{c}** ({len(rows)}): " + " · ".join(
            f"[{r['title']}](prompts/{r['slug']}/)" for r in sorted(rows, key=lambda x: -x["copyCount"])[:15]))
        R.append("")

    R += ["## Superdesign vs other AI design tools", "",
          "<!-- DRAFT: verify each cell before publishing. Keep it factual. -->",
          "| | Superdesign | v0 | Lovable | Bolt | Google Stitch | Uizard |",
          "|---|---|---|---|---|---|---|",
          "| Runs inside your coding agent (Claude Code/Cursor) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |",
          "| Infinite design canvas | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |",
          "| Usage-ranked prompt library | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |",
          "| Designs into your existing design system | ✅ | ⚠️ | ⚠️ | ⚠️ | ❌ | ❌ |",
          "| Outputs real code | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ |", "",
          "## FAQ", "",
          "**Why does my AI-generated UI look generic / like AI slop?** Because the agent has no design "
          "direction, so it defaults to the same fonts, card grids, and colors every time. Give it a full "
          "design spec (like the prompts here) and it builds to that spec instead. See "
          f"[how to make Claude Code UI look good]({BLOG}).", "",
          "**How do I use these prompts?** Three ways: copy a prompt and paste it into Claude Code / Cursor; "
          f"install the [Superdesign skill]({SKILL}) and let your agent search + apply them; or click "
          "**Try it live** to generate on the Superdesign canvas. (See \"How to use\" above.)", "",
          f"**Do these work with Claude Code and Cursor?** Yes. Install the [Superdesign skill]({SKILL}) and "
          "your agent can search, pull, and apply any prompt here to your codebase.", "",
          "**What is the best AI design prompt?** Ranked by real usage, the most-copied are "
          f"[High Contrast Landing Page]({LIB}/high-contrast-landing-page?{UTM}), "
          f"[Glassmorphism]({LIB}/glassmorphism-style?{UTM}), and "
          f"[Lumina SaaS Landing Page]({LIB}/lumina-saas-landing-page?{UTM}).", "",
          "**What is Superdesign?** An AI product design agent that turns prompts into UI mockups, "
          f"components, and full designs on an infinite canvas. See [superdesign.dev]({LIB.replace('/library','')}?{UTM}).", "",
          "**Are the prompts free to use?** The prompt text is free to use. *(Data license TBD — see LICENSE.)*", "",
          "## Contributing", "",
          f"Read-only mirror of the live [Superdesign prompt library]({LIB}). Add prompts by creating them "
          "in the app (top prompts sync here, ranked by usage). Fixes: open a PR. See `CONTRIBUTING.md`.", "",
          "## License", "", "Repo code/structure: MIT (`LICENSE`). Prompt data: **TBD** (CC0 recommended).", ""]
    # NOTE (2026-07-08): README.md, TOPICS.md, LICENSE, CONTRIBUTING.md, .gitignore are
    # REPO-MAINTAINED, not regenerated here. The top-level README is owned by
    # scripts/gen_readme.py (surgical marker regions). This data builder must NOT write
    # README.md — doing so clobbers the hand-written positioning + gen_readme's markers.
    # The unused `R` block above is kept only for reference; its write is intentionally removed.
    _ = R  # retained for reference; not written

    print("v4 DONE. total:", len(recs))
    print("  page-type:", ccount)
    print("  industry :", icount)

if __name__ == "__main__":
    main()
