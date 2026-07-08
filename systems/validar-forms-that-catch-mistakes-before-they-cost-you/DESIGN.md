# Design System — Validar — Forms that catch mistakes before they cost you

> Category: Forms & Contact  ·  Industry: SaaS
> Auto-scaffolded from prompt [`validar-forms-that-catch-mistakes-before-they-cost-you`](../../prompts/validar-forms-that-catch-mistakes-before-they-cost-you/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Modern SaaS product-marketing aesthetic in a single teal accent over a near-white paper canvas, dark slate ink for text. Generous whitespace, large extrabold tracking-tight display headings (Inter), rounded-2xl/3xl cards with soft multi-layer shadows, a faint teal dot-grid grain texture, blurred teal radial glows behind cards, and semantic validation colors (green = valid, red = error) used consistently in fills, borders, icons and helper text. Friendly, precise, trustworthy.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#f8fafc`
- `#0f1729`
- `#475569`
- `#f0fdfa`
- `#ccfbf1`
- `#99f6e4`
- `#5eead4`
- `#2dd4bf`
- `#14b8a6`
- `#0d9488`
- `#0f766e`
- `#115e59`
- `#134e4a`
- `#15803d`
- `#f0fdf4`
- `#86efac`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a modern SaaS product-marketing page using a single teal accent system on a near-white paper background. Typeface: Inter (weights 400/500/600/700/800/900), antialiased, tracking-tight on headings. Palette — paper background #f8fafc; ink (primary text) #0f1729; slatey (secondary text) #475569; teal scale: teal-50 #f0fdfa, teal-100 #ccfbf1, teal-200 #99f6e4, teal-300 #5eead4, teal-400 #2dd4bf, teal-500 #14b8a6, teal-600 #0d9488, teal-700 #0f766e (primary brand), teal-800 #115e59 (hover), teal-900 #134e4a (dark band). Semantic states — valid: text/icon #15803d (good), fill #f0fdf4 (goodbg), border #86efac (goodln); error: text/icon #dc2626 (bad), fill #fef2f2 (badbg), border #fca5a5 (badln); neutral slate-100/slate-200 for idle bars. Use rounded geometry (rounded-full pills, rounded-xl inputs, rounded-2xl/1.75rem cards). Shadows: layered soft card shadow '0 1px 2px rgba(15,23,41,0.04 …

## 5. Layout

Single-column scrolling page, content centered in a max-w-6xl container with px-6 gutters. Order: sticky nav, split hero (copy + live form card), four-up state-model band, full-bleed dark-teal demo section with completed card, why-it-matters two-column benefit grid, slim footer. Hero and demo use a two-column (lg) grid that stacks on mobile; the state cards reflow 1→2→4 columns.

## 6. Components

- **** — 
- **** — 
- **** — 
- **** — 
- **** — 

## 7. Motion

REVIEW —
- Palette — paper background #f8fafc; ink (primary text) #0f1729; slatey (secondary text) #475569; teal scale: teal-50 #f0fdfa, teal-100 #ccfbf1, teal-200 #99f6e4, teal-300 #5eead4, teal-400 #2dd4bf, teal-500 #14b8a6, teal-600 #0d9488, teal-700 #0f766e (primary brand), teal-800 #115e59 (hover), teal-900 #134e4a (dark band)

## 8. Voice & Brand

A teal-on-paper SaaS landing page for an inline form-validation tool: a sticky glass nav, a split hero with a live account-creation card showing all four field states (idle, active, valid, error) at once, a four-up state-model band, a dark-teal 'submit unlocks itself' section, a benefit grid, and a footer. Color + icon + plain-words validation, Inter, soft layered shadows.

## 9. Anti-patterns

Accessibility is the design thesis: state is never carried by color alone — every state pairs a hue with a matching ph: icon and a plain-language word/helper, and the submit button states are spelled out ('Fix 1 field to continue' vs 'Create account'). Keep the palette monochromatic-teal + neutral, and reserve green/red strictly for valid/error semantics. Reuse the four-state input as the single source of truth; the page narrative (hero card → state cards → demo card) is just that one component shown at different points in its lifecycle. Icons are Phosphor bold (ph:*); body/display font is Inter throughout.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
