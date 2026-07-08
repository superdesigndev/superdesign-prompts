# Design System — Sign in to Verdant — Classic Split (Emerald)

> Category: Auth & Login  ·  Industry: SaaS
> Auto-scaffolded from prompt [`sign-in-to-verdant-classic-split-emerald`](../../prompts/sign-in-to-verdant-classic-split-emerald/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Crisp, modern SaaS auth aesthetic. White form side, deep slate brand side, a single emerald accent for the logo, primary button, links and focus rings. Inter typeface throughout, rounded-xl controls, soft inset fields, and a glowing gradient CTA. The dark panel adds depth with blurred emerald radial glows, a subtle dot + line grid masked by a radial fade, and a frosted-glass floating card.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#ffffff`
- `#0f172a`
- `#64748b`
- `#94a3b8`
- `#334155`
- `#059669`
- `#047857`
- `#065f46`
- `#10b981`
- `#6ee7b7`
- `#34d399`
- `#ecfdf5`
- `#d1fae5`
- `#f8fafc`
- `#f1f5f9`
- `#e2e8f0`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a clean modern SaaS authentication aesthetic with a light/dark split. Page background is white (#ffffff); body ink is slate-900 (#0f172a), secondary text slate-500 (#64748b) and slate-400 (#94a3b8), labels slate-700 (#334155). Single accent is emerald: primary emerald-600 (#059669), emerald-700 (#047857) and emerald-800 (#065f46) for the CTA gradient, emerald-500 (#10b981) for the focus ring and logo gradient top, emerald-300 (#6ee7b7) and emerald-400 (#34d399) as light accents on the dark panel; soft tints emerald-50 (#ecfdf5)/100 (#d1fae5). Neutrals are the full slate scale (50 #f8fafc, 100 #f1f5f9, 200 #e2e8f0, 300 #cbd5e1, 600 #475569, 700 #334155, 800 #1e293b, 900 #0f172a, 950 #020617). Typeface Inter (weights 400-900), antialiased; headings extrabold with tight tracking. Form controls are rounded-xl (12px) with 1px slate-200 borders on a slate-50/70 fill; on focus-within the bo …

## 5. Layout

A sticky full-bleed top nav above a two-column main grid (lg:grid-cols-[1.05fr_1fr], min-height = viewport minus nav). Left column: a centered max-w-[400px] auth form. Right column (hidden below lg): a dark slate brand panel laid out top/middle/bottom (eyebrow badge, quote + floating card, trust row). On mobile the right panel is hidden and only the form column shows, full width.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A full-bleed classic split sign-in page: white emerald-accented auth form on the left (social + email login, gradient Sign in CTA), a dark slate brand panel with ambient glows and a floating showcase card on the right, and a sticky nav above both.

## 9. Anti-patterns

Single emerald accent on slate/white neutrals only; do not introduce other hues. The layout is a true full-bleed split (no centered card) with the form on the left and the dark brand panel on the right, and a sticky nav above both. Below the lg breakpoint the right panel is hidden and the form column goes full width. Keep the exact field focus treatment (emerald-500 border + 4px emerald ring) and the CTA gradient + glow shadow. Inter throughout, rounded-xl controls. No em-dashes in copy.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
