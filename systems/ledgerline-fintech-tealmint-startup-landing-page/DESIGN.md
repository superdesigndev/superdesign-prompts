# Design System — Ledgerline — fintech teal/mint startup landing page

> Category: Dashboards  ·  Industry: Finance & Crypto
> Auto-scaffolded from prompt [`ledgerline-fintech-tealmint-startup-landing-page`](../../prompts/ledgerline-fintech-tealmint-startup-landing-page/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Dark, premium, trustworthy fintech editorial. Deep teal canvas with a single mint accent and warm cream text reads as financial software (Brex/Mercury/Ramp lineage), calm and high-contrast, never neon or busy. Inter for everything (400-800) with very tight tracking on display headings (-0.045em) and extra-bold weights; tabular-nums on all money/figures. Depth comes from layered soft shadows, inset cream hairline 'rings', mint glow on primary buttons, and faint mint radial gradients ('grain') washed over hero/CTA/stats. Fully rounded pill buttons; small uppercase wide-tracked eyebrow/label text; mint used sparingly as the only saturated color so it always reads as the call to action.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#0f3d3e`
- `#0a2a2b`
- `#134847`
- `#1b5a58`
- `#256a67`
- `#4fd1c5`
- `#eef5f0`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design in a dark, premium fintech / neobank style. Palette: deep teal canvas teal-900 #0f3d3e as the page background, with teal-950 #0a2a2b (darkest, for dashboard/inputs/CTA), teal-800 #134847 (feature cards), teal-700 #1b5a58 and teal-600 #256a67 (card gradients); one mint accent #4fd1c5 for the logo mark, primary buttons, links, icons, chart stroke, stat numbers and the brand period; cream #eef5f0 for text. Text opacity ladder: cream for primary, cream/70-/75 for body, cream/60-/65 for muted captions and uppercase labels. Use Inter (weights 400/500/600/700/800) for everything; display headings are font-extrabold with very tight letter-spacing -0.045em ('tightest') and leading ~1.04-1.07; apply tabular-nums (font-variant-numeric) to every dollar amount, percentage and figure. Surfaces: cards use an inset cream hairline ring (box-shadow inset 0 0 0 1px rgba(238,245,240,0.08)) plus a sof …

## 5. Layout

Single-column long-form landing page, centered max-w-7xl (80rem) container with px-6 / lg:px-8 gutters, on a uniform deep-teal body. Top-down order: sticky blurred header nav; hero (asymmetric 2-col grid ~1.04fr / 1fr: copy left, product dashboard mock right with a tilted floating card chip); a centered trust/logo strip on a darker band; a bento feature section (2-wide + 1 + 1 + 2-wide cards, several with inline product mocks); a stats/traction band (2-col intro + a 2x2 hairline-divided stat grid) followed by a large pull-quote with avatar; a security & compliance section (copy + bulleted assurances on the left, a certifications badge grid card on the right); a glowing centered CTA section; and a 4-column footer with a bottom legal bar. Bands alternate teal-900 / teal-950 tints with hairline cream/10 borders for rhythm. Responsive: the hero and all multi-col grids collapse to one column, nav links and some trust logos / hero meta items hide below their breakpoints, and the floating card chip hides on mobile.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

Dark premium fintech / neobank startup landing page: deep teal canvas with a single mint accent and cream text (Inter), sticky blurred nav, a hero with a live account-dashboard mock (balance, area chart, transactions) and a tilted virtual-card chip, a bento feature grid, a hairline stat band with a pull-quote, a security & compliance badge grid, and a glowing centered CTA.

## 9. Anti-patterns

Single Google font: Inter (opsz 14..32, weights 400-800), set as the sans family; no serif. Styled with Tailwind via CDN using a custom theme: teal scale (950 #0a2a2b, 900 #0f3d3e, 800 #134847, 700 #1b5a58, 600 #256a67), mint #4fd1c5, cream #eef5f0, and a custom letterSpacing 'tightest' -0.045em. Body is bg-teal-900 text-cream with -webkit-font-smoothing:antialiased and font-feature-settings 'ss01','cv11'; all monetary figures use tabular-nums. Custom CSS utilities: .grain (layered mint radial + teal linear wash), .ringline (inset cream hairline), .softcard / .dash-shadow (soft deep drop shadows + ring), .mint-glow (mint button glow), .num-mono (tabular-nums), and a mint ::selection. Icons via Iconify iconify-icon web component (Phosphor 'ph:' set). All product data (balances, transactions, certifications, logos, the customer quote) is fabricated placeholder content. Keep mint as the only saturated accent so it always reads as the CTA; the mood must stay calm, premium, secure and high-contrast, never neon, playful or cluttered. Sticky nav, the floating card chip, multi-column grids and hero meta reflow responsibly down to mobile (single column).

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
