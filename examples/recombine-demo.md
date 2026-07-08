# Recombination demo — style × structure

The point of factoring prompts into [systems](../systems/) (style) and
[page-types](../page-types/) (structure) is that they **recombine**. One curated
style now renders many pages; one page type renders in many styles.

We use the curated **Stripe-Enterprise** system
([`systems/analytics-dashboard/`](../systems/analytics-dashboard/)) below.

---

## 1. The original (style × structure it came from)

**Stripe-Enterprise × Dashboards** → the analytics dashboard the prompt was born as.

```text
Build a Dashboard using the "analytics-dashboard" design system
(systems/analytics-dashboard/ — apply tokens.css, follow DESIGN.md).
Include the common sections from page-types/dashboards/SKILL.md:
sidebar nav, global header, metrics grid, analytics section, projects table.
```

## 2. Same style, NEW structure

**Stripe-Enterprise × Pricing Pages** → a pricing page that never existed as a prompt,
in exactly the dashboard's brand.

```text
Build a Pricing Page using the "analytics-dashboard" design system
(systems/analytics-dashboard/tokens.css + DESIGN.md).
Use the common sections from page-types/pricing-pages/SKILL.md:
plan tiers, feature comparison table, billing toggle, FAQ, CTA.
Keep --bg #F8F9FA, white cards, --accent #3B82F6, Inter + JetBrains Mono,
8px card radius, the --shadow-card elevation. No pill-shaped cards.
```

## 3. Same structure, NEW style

**Brutalist × Dashboards** → the same dashboard anatomy, a totally different look.

```text
Build a Dashboard using the "brutalist-e-commerce-page" design system
(systems/brutalist-e-commerce-page/).
Use the common sections from page-types/dashboards/SKILL.md.
```

---

### Why this beats a flat prompt list

| | Flat prompts | Factored (this repo) |
|---|---|---|
| "Analytics dashboard" | 1 dashboard, 1 look | reusable **Stripe-Enterprise** style |
| Want it as a pricing page? | write a new prompt | **swap the page type** |
| Want a brutalist dashboard? | write a new prompt | **swap the system** |
| Coverage | 150 cells | ~40 styles × 12 page types ≈ **480 combos** |
