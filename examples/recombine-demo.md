# Recombination demo — style × structure

Every prompt is factored into a [system](../systems/) (style) and a [page-type](../page-types/)
(structure), so they **recombine**: one style renders many pages, one page type renders in many styles.

We use the **AI System Configuration Console** style
([`systems/ai-system-configuration-console/`](../systems/ai-system-configuration-console/)) below — a
dark-slate + acid-green brutalist console look.

> `systems/` holds a `DESIGN.md` summary per style. For the **exact** colors, fonts, and tokens, the
> [prompt README](../prompts/) is the source of truth.

---

## 1. The original (style × structure it came from)

**AI Console × Dashboards** → the console dashboard the prompt was born as.

```text
Build a Dashboard in the "ai-system-configuration-console" style
(see systems/ai-system-configuration-console/DESIGN.md; exact tokens in
prompts/ai-system-configuration-console/).
Include the common sections from page-types/dashboards/README.md.
```

## 2. Same style, NEW structure

**AI Console × Pricing Pages** → a pricing page that never existed as a prompt, in the console's look.

```text
Build a Pricing Page in the "ai-system-configuration-console" style
(systems/ai-system-configuration-console/DESIGN.md + the prompt for exact tokens).
Use the common sections from page-types/pricing-pages/README.md:
plan tiers, comparison table, billing toggle, FAQ, CTA.
```

## 3. Same structure, NEW style

**Glassmorphism × Dashboards** → the same dashboard anatomy, a totally different look.

```text
Build a Dashboard in the "glassmorphism-style" style
(systems/glassmorphism-style/DESIGN.md).
Use the common sections from page-types/dashboards/README.md.
```

---

### Why this beats a flat prompt list

| | Flat prompts | Factored (this repo) |
|---|---|---|
| A dashboard | 1 dashboard, 1 look | a reusable **style** you can re-apply |
| Want it as a pricing page? | write a new prompt | **swap the page type** |
| Want a different look? | write a new prompt | **swap the style** |
| Coverage | 150 point solutions | styles × page types = **many more combinations** |
