# Design Systems — the *style* axis

> ⚠️ **Experimental / draft.** These systems are **auto-scaffolded** from the prompts by
> `scripts/factor_prompts.py`. Only `analytics-dashboard/` is hand-curated; the rest are
> best-effort extractions — the `tokens.css` role assignments (`--fg`, `--accent`, `--border`…)
> are *guesses* and some are wrong (e.g. text/accent swapped), and some prose is truncated.
> **Treat the prompt README (`prompts/<slug>/`) as the source of truth**, not these tokens, until
> a system is marked curated.

Every prompt in this repo bundles two separable things:

- a **style** — colors, type, spacing, motion, voice ("how it looks")
- a **structure** — sections, layout, components ("what page it is")

A raw prompt fuses them into one point-solution. This folder factors the **style**
out into a reusable **design system** — a brand contract you can pair with *any*
[page type](../page-types/) to render a new artifact.

```
 systems/ (style)   ×   page-types/ (structure)   =   N × M artifacts
 stripe-enterprise  ×   pricing-page              →   a Stripe-style pricing page
 stripe-enterprise  ×   dashboard                 →   the original analytics dashboard
 brutalist          ×   pricing-page              →   a brutalist pricing page
```

That's the same move Open Design and Figma themes make: a small authored set that
**recombines** into a huge surface, instead of a flat list of one-offs.

## What's in each system

| File | Purpose |
|---|---|
| `DESIGN.md` | 9-section prose spec (theme · color · type · effects · layout · components · motion · voice · anti-patterns). |
| `tokens.css` | Machine-readable CSS variables — drop into any project. |
| `manifest.json` | Metadata + `status` (`draft` \| `curated`) + extracted colors/fonts. |

## Draft → curated

All 150 systems here were **auto-scaffolded** from the prompts by
[`scripts/factor_prompts.py`](../scripts/factor_prompts.py). Auto-extracted token
roles and prose are best-effort and marked `REVIEW`. Promoting a draft to
`curated` means: assign token roles correctly, tighten the prose, confirm against
the preview. See [`analytics-dashboard`](analytics-dashboard/) for a curated
example (the "Stripe-Enterprise" system) vs. any other folder for a raw draft.

Regenerate all drafts (non-destructive to curated edits you protect):

```bash
python3 scripts/factor_prompts.py
```

## Use a system

```text
Build a <page type> using the "<system-id>" design system in
systems/<system-id>/ — apply tokens.css and follow DESIGN.md.
```

See [`../examples/recombine-demo.md`](../examples/recombine-demo.md) for a worked
style × structure recombination.
