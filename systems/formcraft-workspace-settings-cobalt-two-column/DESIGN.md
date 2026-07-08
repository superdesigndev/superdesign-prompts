# Design System — Formcraft — Workspace Settings (cobalt two-column)

> Category: Forms & Contact  ·  Industry: SaaS
> Auto-scaffolded from prompt [`formcraft-workspace-settings-cobalt-two-column`](../../prompts/formcraft-workspace-settings-cobalt-two-column/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Calm, modern product-settings aesthetic on a near-white (#f8fafc) canvas with a slate ink palette and one disciplined cobalt-blue accent (#2563eb). Inter typeface, soft rounded cards with hairline borders and a very light card shadow, generous padding, and translucent backdrop-blurred sticky chrome top and bottom.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#f8fafc`
- `#2563eb`
- `#ffffff`
- `#0f172a`
- `#64748b`
- `#94a3b8`
- `#334155`
- `#1e293b`
- `#1d4ed8`
- `#eff4ff`
- `#e2e8f0`
- `#f1f5f9`
- `#fff`
- `#fecdd3`
- `#be123c`
- `#e11d48`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a light, calm SaaS settings visual style. Page background slate-50 #f8fafc; cards and chrome white #ffffff (sticky bars at 85-90% opacity with backdrop-blur). Text in slate: headings/primary #0f172a (ink-900), body/secondary #64748b (ink-500), muted #94a3b8 (ink-400), strong-label #334155 (ink-700) and #1e293b (ink-800). Single accent color cobalt blue #2563eb (cobalt-600), hover #1d4ed8 (cobalt-700), light accent fill #eff4ff (cobalt-50), accent text #1d4ed8 (cobalt-700); focus ring rgba(37,99,235,0.12) at 4px. Borders #e2e8f0 (ink-200, often at 70-80% opacity) and #f1f5f9 (ink-100) for inner row dividers; input fill slate-50 at 60% (#f8fafc/60) turning white #fff on focus, input border #e2e8f0. Danger uses rose: border #fecdd3 (rose-200), text #be123c (rose-700)/#e11d48 (rose-600), hover fill rose-50; success uses emerald-500 #10b981; the unsaved-changes dot is amber-400 #fbbf24. T …

## 5. Layout

A max-w-6xl page with a sticky top app nav, a white breadcrumb + title header band, then a body that is a CSS grid of [208px sidebar | 1fr content] on large screens and a single stacked column on mobile. The left sidebar is a sticky in-page section nav; the right column is a vertical stack (gap-7) of rounded settings cards, each card a titled header strip plus rows. A fixed bottom save bar spans the viewport. The sidebar nav becomes a horizontal scrollable strip and every label/field row collapses to stacked on mobile.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

REVIEW —
- Single accent color cobalt blue #2563eb (cobalt-600), hover #1d4ed8 (cobalt-700), light accent fill #eff4ff (cobalt-50), accent text #1d4ed8 (cobalt-700); focus ring rgba(37,99,235,0
- Danger uses rose: border #fecdd3 (rose-200), text #be123c (rose-700)/#e11d48 (rose-600), hover fill rose-50; success uses emerald-500 #10b981; the unsaved-changes dot is amber-400 #fbbf24

## 8. Voice & Brand

A two-column SaaS workspace-settings screen: sticky app nav, left section nav, grouped settings cards with toggles, a segmented control, selectable delivery cards, and a fixed save bar, in Inter on slate with one cobalt accent.

## 9. Anti-patterns

Single accent discipline is the core idea: cobalt #2563eb is reserved for the active nav item, links, focus rings, the primary 'Save/Upload' buttons, the selected destination card, and the notification icon tiles; everything else is slate-on-white, with rose used only for the danger zone, emerald only for the synced status, and amber only for the unsaved-changes dot. The page is a two-column [208px sidebar | 1fr] grid on lg and a single stacked column on mobile; the left section nav is sticky on desktop and a horizontal overflow strip on mobile. Each label+field row is row-on-sm and stacked-on-mobile, with controls capped at max-w-md so long forms stay scannable. Inputs default to a slate-50/60 fill that turns white with a 4px cobalt focus ring. Toggles, segmented control, and selects are drawn in pure CSS (pseudo-elements + inlined SVG), not images. A fixed bottom save bar (pb-32 on main reserves space) keeps the primary action always reachable. Fonts via Google Fonts Inter (400-800); icons via Iconify lucide:* set; Tailwind via CDN with extended 'cobalt' (50 #eff4ff -> 900 #1e3a8a) and 'ink' (50 #f8fafc -> 900 #0f172a) color scales.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
