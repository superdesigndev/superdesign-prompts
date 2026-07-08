# Design System — Ledgerline — Deep-Teal + Mint Fintech Startup (Dashboard Hero)

> Category: Dashboards  ·  Industry: Finance & Crypto
> Auto-scaffolded from prompt [`ledgerline-deep-teal-mint-fintech-startup-dashboard-hero`](../../prompts/ledgerline-deep-teal-mint-fintech-startup-dashboard-hero/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Calm, premium fintech aesthetic built on deep teal surfaces, a single mint accent, and warm cream text. The whole page lives on teal-900 #0f3d3e with darker teal-950 #0a2a2b panels and lighter teal-800 #134847 / teal-700 #1b5a58 card fills; the one accent is mint #4fd1c5 (used for the logo mark, primary buttons, the chart line, positive numbers, check marks, eyebrows and tinted icon tiles), and all text is cream #eef5f0 at varying opacities. Surfaces read as soft frosted glass via thin inset cream hairline 'rings' (inset 0 0 0 1px rgba(238,245,240,0.08)) and deep ambient drop shadows rather than hard borders. A reusable mint 'grain' backdrop (layered radial mint glows + a subtle top vertical wash) sits behind the hero, traction band and CTA. Trust, calm, and clarity over flash: lots of breathing room, tabular-numeric figures for money, gentle hover tints, no harsh contrast.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#0f3d3e`
- `#0a2a2b`
- `#134847`
- `#1b5a58`
- `#4fd1c5`
- `#eef5f0`

## 3. Typography

- `Live`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Build a calm, trustworthy fintech look. Background is teal-900 #0f3d3e; panels and the darkest surfaces use teal-950 #0a2a2b, card fills use teal-800 #134847 and the floating card chip uses a teal-700 #1b5a58 -> teal-800 gradient. The single accent is mint #4fd1c5: use it for the logo mark, primary pill buttons (mint fill, teal-950 #0a2a2b text), the area-chart stroke and gradient, positive/credit amounts, check marks, eyebrow labels, tinted icon tiles (mint at ~12-15% opacity behind a mint glyph) and 'Live' status dots. All text is cream #eef5f0: headings at full strength, body at ~65-70% (cream/65-70), muted meta at ~60%. Treat every surface as soft frosted glass: instead of hard borders use a 1px inset cream hairline ring `box-shadow: inset 0 0 0 1px rgba(238,245,240,0.08)` plus deep ambient shadows (cards: 0 24px 60px -28px rgba(0,0,0,0.7); the dashboard mock: 0 40px 90px -40px rgba( …

## 5. Layout

A single frameless, fully responsive web page (not a fixed-size mockup), centered in a max-w-7xl container with px-6/lg:px-8 gutters. Vertical flow: sticky blurred nav -> split hero (copy left, dashboard mock right) -> centered 'trusted by' compliance strip -> a bento feature grid (wide + tall cards with inline mocks) -> a stats/traction band (4 figures + pull-quote) -> a security & compliance section (copy + certifications badge grid) -> a glowing centered CTA -> a 4-column footer. The hero is the centerpiece: a two-column grid (lg:[1.04fr_1fr]) that stacks on mobile, with the product dashboard mock and a tilted floating virtual-card chip on the right. The nav stays pinned and frosted while the mint grain sections scroll beneath. Responsive: the hero, feature bento and traction grids collapse to one column, the cert grid goes 2->1, the floating card chip and some trust items hide on small screens, and headline sizes clamp down.

## 6. Components

- **Product dashboard mock** — The hero's right-side product proof: a glassy operating-account dashboard with a balance, a mint area chart and auto-categorized transactions, sitting on a soft mint halo.
- **Floating virtual-card chip** — A tilted mini credit-card that floats off the dashboard mock's bottom-left corner to sell the 'cards' product.
- **Frosted teal glass surface** — The repeating card/pill/row treatment — frosted teal with a thin cream inset hairline ring instead of a hard border.
- **Mint grain backdrop** — The soft multi-bloom mint glow field reused behind the hero, traction band and CTA.
- **Mint pill button + glow** — The signature primary CTA reused in the nav, hero, traction and CTA sections.

## 7. Motion

REVIEW —
- Trust, calm, and clarity over flash: lots of breathing room, tabular-numeric figures for money, gentle hover tints, no harsh contrast

## 8. Voice & Brand

A trustworthy deep-teal fintech-startup landing page with a mint accent and cream text: a split hero with a product dashboard mock and a floating virtual card, a bento feature grid, a stats traction band, a security certifications grid, and a glowing CTA.

## 9. Anti-patterns

Frameless, fully responsive web page (not a fixed-size artboard); dark/teal color-scheme only. Built with Tailwind (CDN) + a small custom-CSS layer for the grain backdrop, the inset-ring 'ringline'/'softcard'/'dash-shadow' shadows, the mint glow and tabular-nums; typography is Inter only (optical-sizing 14..32, ss01/cv11, weights 400-800) from Google Fonts, with Iconify Phosphor icons. There is no JS — every 'interactive' element (status pills, progress bar, togg'd states) is static. Key responsive behavior: the hero and traction grids collapse to one column, the feature bento wide cards drop their col-span, the certifications grid goes 2->1, the floating virtual card and the third hero trust item hide on small screens, and the nav center links collapse on mobile while the bar stays sticky/frosted. To rebrand, keep the frosted-teal-glass + single-mint-accent system and the grain backdrop, and swap the deep-teal surface ramp (#0a2a2b/#0f3d3e/#134847/#1b5a58) and the mint accent #4fd1c5.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
