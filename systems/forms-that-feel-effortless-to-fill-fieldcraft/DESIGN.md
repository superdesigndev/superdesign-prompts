# Design System — Forms that feel effortless to fill — Fieldcraft

> Category: Forms & Contact  ·  Industry: SaaS
> Auto-scaffolded from prompt [`forms-that-feel-effortless-to-fill-fieldcraft`](../../prompts/forms-that-feel-effortless-to-fill-fieldcraft/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Calm, editorial SaaS aesthetic on a white canvas with a slate-900 ink palette and one disciplined emerald accent (#10b981). Inter typeface, generous whitespace, soft rounded corners, faint dotted grain texture, and large blurred emerald glow blobs behind the hero and dark CTA.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#10b981`
- `#ffffff`
- `#0f172a`
- `#64748b`
- `#94a3b8`
- `#059669`
- `#047857`
- `#065f46`
- `#e2e8f0`
- `#cbd5e1`
- `#f8fafc`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a light, calm SaaS visual style. Background white (#ffffff); body text and headings in slate (#0f172a text-slate-900, secondary text #64748b text-slate-500, muted #94a3b8 text-slate-400). Single accent color emerald #10b981 (hover #059669, focus ring rgba(16,185,129,0.12), darker text #047857/#065f46). Borders #e2e8f0 (slate-200) and inputs #cbd5e1 (slate-300); field fill #f8fafc / slate-50. Typeface Inter (weights 400/500/600/700/800), system-ui fallback, antialiased, -webkit-font-smoothing. Headings extrabold with tight tracking and 1.05 line-height; eyebrow labels uppercase, bold, letter-spacing 0.18em, emerald-600. Rounded corners: lg (8px) on inputs/buttons, xl (12px) on icon tiles, 2xl (16px) on the form card and anatomy cards. Soft elevation: shadow-sm on chips/buttons, shadow-xl with a 5% slate tint on the form card, colored shadow-emerald-500/25 under primary buttons. Add a  …

## 5. Layout

Single-column, centered max-w-6xl page. Sticky translucent nav, gradient hero with centered headline, a slate-50 showcase band holding the form on a max-w-3xl white card, a 3-up anatomy grid on white, a dark emerald-glow prompt CTA with a code block, then a footer. The form itself is divided into stacked sections separated by hairline dividers, each section using a vertical stack or a 6-column responsive grid that collapses to one column on mobile.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

REVIEW —
- Single accent color emerald #10b981 (hover #059669, focus ring rgba(16,185,129,0

## 8. Voice & Brand

A stacked, multi-section account-settings form on a white card: top-aligned labels, helper text, a 6-column responsive grid, custom checkboxes and radios, and one disciplined emerald accent for focus and the primary action.

## 9. Anti-patterns

Single accent discipline is the core idea: emerald (#10b981) is used ONLY on focus rings, the primary button, and selected checkbox/radio states; everything else is slate/white. Labels are always top-aligned and semibold (text-slate-700) so the eye scans straight down. The 6-column grid is the responsive backbone: paired/tripled fields collapse to one column on mobile with no rework. Inputs default to a slate-50 fill that turns white on focus. Custom checkbox/radio marks are drawn in pure CSS (::after pseudo-elements), not images, and carry visible focus rings for WCAG. Fonts via Google Fonts Inter; icons via Iconify (lucide:* set). Tailwind via CDN with an extended emerald scale (50 #ecfdf5 -> 900 #064e3b).

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
