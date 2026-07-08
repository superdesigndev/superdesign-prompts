# Design System — Midnight Navy Fintech Pricing

> Category: Pricing Pages  ·  Industry: Finance & Crypto
> Auto-scaffolded from prompt [`midnight-navy-fintech-pricing-656a6d`](../../prompts/midnight-navy-fintech-pricing-656a6d/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Deep midnight-navy fintech dark theme with a single cool teal/mint accent, a soft faint dot/line grid plus radial teal glows in the background, fully rounded controls, and crisp two-weight typography (geometric Sora display + Inter body). High polish, low chroma: almost everything is navy/white/muted-slate, and teal is reserved for the one thing that matters (the highlighted tier, checks, and CTAs).

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#06152b`
- `#0b1f3a`
- `#0f2747`
- `#143055`
- `#1c3f6b`
- `#27507f`
- `#5eead4`
- `#2dd4bf`
- `#14b8a6`
- `#0d9488`
- `#eaf1f8`
- `#9fb2c9`
- `#ffffff`
- `#cfe6ff`

## 3. Typography

- `Most popular`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Build a dark fintech aesthetic on a near-black navy page background (#06152b). Define a navy ramp: navy-950 #06152b, navy-900 #0b1f3a, navy-850 #0f2747, navy-800 #143055, navy-700 #1c3f6b, navy-600 #27507f. Single accent is teal/mint: teal-300 #5eead4, teal-400 #2dd4bf, teal-500 #14b8a6, teal-600 #0d9488. Neutral text colors: 'mist' #eaf1f8 for primary body text, 'slate2' #9fb2c9 for muted/secondary text, pure white #ffffff for headings. Typography: load Google Fonts Sora (weights 400-800) as the display family for headings, prices, logo, and section labels, and Inter (weights 400/450/500/600) as the body/UI sans; enable antialiasing and tracking-tight on big headings. Use a hero headline gradient text effect (linear-gradient 92deg from #ffffff to #cfe6ff to #5eead4, clipped to text). Background texture for the hero/pricing region: a 'grid-bg' built from two radial glows (a large teal ra …

## 5. Layout

A single-column, frameless responsive web page that scrolls vertically: sticky translucent nav, centered hero with billing toggle, a responsive 3-card pricing grid (the key section) that reflows 3->2->1 column with the highlighted tier always emphasized, a 4-up trust strip, an accordion FAQ, and a tall footer. Everything is centered in a max-w-7xl container (FAQ narrows to max-w-3xl) with consistent horizontal padding (px-5 on mobile, sm:px-8).

## 6. Components

- **Monthly/Annual billing toggle** — A pill switch in the hero that flips all tier prices between monthly and annual, with a 'Save 18%' badge.
- **Highlighted 'Most popular' tier card** — The middle pricing tier rendered as a glowing, elevated, primary-CTA card to anchor the choice.
- **Feature checklist rows** — Consistent included-feature lists inside each tier card.
- **Background grid + glow texture** — The signature ambient backdrop behind the hero and pricing region.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A deep-navy, teal-accented SaaS/fintech pricing page with a sticky blurred nav, monthly/annual toggle, and a glowing 'Most popular' middle tier across three cards.

## 9. Anti-patterns

This is a FRAMELESS, fully responsive web page (no browser chrome / device frame): a single vertical scroll inside a max-w-7xl centered container (FAQ at max-w-3xl). The pricing grid is the centerpiece and must reflow 3->2->1 column (lg->md->mobile), the nav is sticky + blurred, and the billing toggle must actually rewrite prices via data-monthly/data-annual attributes. Pure HTML + Tailwind (CDN config extends the navy/teal palette and Sora/Inter fonts) + a small vanilla-JS toggle; icons via Iconify Phosphor set. No em-dashes in copy; use the navy+teal palette and reserve teal strictly for emphasis. Built with placeholder fintech-banking brand 'Vaultline' . swap brand, copy, and the 3 tier names/prices to repurpose.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
