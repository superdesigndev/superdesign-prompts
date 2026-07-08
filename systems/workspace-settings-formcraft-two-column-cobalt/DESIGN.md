# Design System — Workspace Settings · Formcraft (two-column, cobalt)

> Category: Dashboards  ·  Industry: SaaS
> Auto-scaffolded from prompt [`workspace-settings-formcraft-two-column-cobalt`](../../prompts/workspace-settings-formcraft-two-column-cobalt/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Light, calm, professional product-settings aesthetic. Single cobalt-blue accent on a cool slate (ink) neutral scale; near-white app background, pure-white cards. Soft hairline borders and very subtle card shadows instead of heavy elevation. Inter font, tight tracking on headings, bold section titles with muted sub-descriptions. Rounded corners (lg on controls, 2xl on cards, full on pills/toggles/avatars). Lucide line icons sized 14-18px. Restrained color: green only for the success status pill, rose only for the danger zone, amber only for the unsaved-changes dot.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#2563eb`
- `#1d4ed8`
- `#eff4ff`
- `#dbe6fe`
- `#93b4fd`
- `#f8fafc`
- `#ffffff`
- `#e2e8f0`
- `#f1f5f9`
- `#64748b`
- `#0f172a`
- `#334155`
- `#475569`
- `#94a3b8`
- `#ecfdf5`
- `#047857`

## 3. Typography

- `Danger zone`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a light, modern SaaS settings page using Inter (weights 400/500/600/700/800), antialiased. Use a single cobalt-blue accent scale (primary #2563eb, hover #1d4ed8, light tint #eff4ff, mid #dbe6fe / #93b4fd) on a cool slate 'ink' neutral scale (page bg #f8fafc, white cards #ffffff, borders #e2e8f0 and hairlines #f1f5f9/#e2e8f0 at ~70-80% opacity, body text #64748b, headings #0f172a, strong labels #334155, secondary labels #475569, muted #94a3b8). Reserve color strictly: emerald (#ecfdf5 bg / #047857 text / #a7f3d0 border) only for a success status pill, rose (#fecdd3 border / #e11d48 + #be123c text) only for a destructive 'Danger zone', amber (#fbbf24) only for the pulsing unsaved-changes dot. Cards are rounded-2xl with a 1px ink-200/80 border and a very soft two-layer shadow (0 1px 2px rgba(15,23,42,.04), 0 1px 3px rgba(15,23,42,.06)); inputs/buttons rounded-lg, pills/avatars/toggle …

## 5. Layout

Top-to-bottom: (1) sticky translucent app-bar; (2) tinted page header with breadcrumb, title and a status pill; (3) a max-w-6xl two-column grid — a 208px sticky section nav on the left and a vertical stack of settings cards on the right; (4) a sticky bottom save bar. Inside cards, settings are labeled-left / control-right rows separated by hairline dividers (row-divide), reflowing to stacked label-over-control on mobile.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

REVIEW —
- Use a single cobalt-blue accent scale (primary #2563eb, hover #1d4ed8, light tint #eff4ff, mid #dbe6fe / #93b4fd) on a cool slate 'ink' neutral scale (page bg #f8fafc, white cards #ffffff, borders #e2e8f0 and hairlines #f1f5f9/#e2e8f0 at ~70-80% opacity, body text #64748b, headings #0f172a, strong labels #334155, secondary labels #475569, muted #94a3b8)

## 8. Voice & Brand

Light SaaS workspace-settings page (form builder): sticky app-bar, tinted header, sticky left section nav + stacked white settings cards, toggles, segmented control and a sticky save bar, on a single cobalt accent over a slate neutral system.

## 9. Anti-patterns

Color discipline is the heart of this design: cobalt is the only brand accent and everything else lives on the slate/ink neutral scale; emerald, rose, and amber appear exactly once each (success status, danger zone, unsaved dot) so they read as meaningful state, not decoration. Hierarchy comes from weight and spacing rather than dividers or boxes: bold tracking-tight section titles over 12.5-13px muted descriptions, hairline (#f1f5f9) row dividers, and rounded-xl ink-100 sub-groups that quietly cluster related fields. Elevation is deliberately low (1-3px soft shadows) so the page feels flat and trustworthy. Layout is fully responsive: the two-column body collapses to one column, the left section nav turns into a horizontal scroller, and every labeled form row reflows from label-left to label-over-control under the sm breakpoint. Both the top app-bar and the bottom save bar are sticky with backdrop-blur so navigation and the save action stay reachable while scrolling a long settings page. Icons are Lucide line icons; the type is Inter throughout.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
