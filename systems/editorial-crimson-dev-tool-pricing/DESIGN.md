# Design System — Editorial Crimson Dev-Tool Pricing

> Category: Pricing Pages  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`editorial-crimson-dev-tool-pricing`](../../prompts/editorial-crimson-dev-tool-pricing/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Warm editorial-tech aesthetic: near-white background, a single saturated crimson accent used for the logo mark, featured tier, pills, check icons and links, and a near-black 'ink' for text and the dark CTA band. Serif display headings (Fraunces) over a clean Inter body create a confident, designerly-but-technical feel. Generous whitespace, 1px hairline ink borders, rounded-2xl cards, soft layered shadows, subtle dotted grain texture, and blurred crimson glow blobs behind the hero. Uppercase, wide-tracked micro-labels.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#ffffff`
- `#f7f7f8`
- `#0e0f12`
- `#5a5d66`
- `#71747e`
- `#90939c`
- `#fff1f2`
- `#ffe1e3`
- `#ffc8cd`
- `#f23a4d`
- `#dc1d34`
- `#b8132a`
- `#991327`
- `#7e1526`
- `#eeeef0`
- `#d9dadd`

## 3. Typography

- `Fraunces`
- `Inter`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a light editorial dev-tool style. Background pure white #ffffff; section bands alternate with a faint tint of ink-50 #f7f7f8 (e.g. bg-ink-50/60). Text in near-black ink-900 #0e0f12 for headings, ink-600 #5a5d66 for body, ink-500 #71747e / ink-400 #90939c for muted captions. Single accent is crimson, scaled as: crimson-50 #fff1f2, crimson-100 #ffe1e3, crimson-200 #ffc8cd, crimson-500 #f23a4d, crimson-600 #dc1d34 (primary), crimson-700 #b8132a, crimson-800 #991327, crimson-900 #7e1526. Borders are 1px ink-100 #eeeef0 / ink-200 #d9dadd hairlines. Typography: display serif 'Fraunces' (opsz, weights 400-900) for the logo, h1/h2/h3 and the big price numerals (tight tracking ~ -0.02em, line-height ~1.04-1.1); body + UI in 'Inter' (weights 400-800). Micro-labels are 11-12px, font-700, uppercase, letter-spacing ~0.16em, in ink-500. Rounded corners: lg/xl on buttons and pills, 2xl (rounded-2xl …

## 5. Layout

A frameless, responsive single-column web page (max content width 1240px, generous side padding) stacked as: sticky translucent nav, a serif hero with eyebrow pill and trust row, a controls band holding the audience segmented tabs + billing toggle, the 4-up pricing grid with a raised featured tier, a 4-column 'all plans include' feature band, a two-column FAQ accordion, a dark CTA band, and a slim footer. The whole thing is fluid: the pricing cards reflow 4 -> 2 -> 1 columns, the controls row stacks vertically on mobile, and the nav collapses its link list on small screens. Not a fixed-size frame, a full responsive page.

## 6. Components

- **Audience segmented-tab switcher** — A 3-way pill switcher (Personal / Teams / Enterprise) that doesn't just style itself, it swaps the entire pricing data set and the context sentence below the controls. The active segment fills crimson-600 with white text.
- **Monthly / Annual billing toggle with Save pill** — A two-button billing toggle plus a 'Save 20%' badge that recomputes every visible price between monthly and annual amounts and dims the badge when monthly is active.
- **Featured (most-popular) pricing tier** — One tier visually elevated above the rest: a solid crimson gradient card with white text, a notched 'Popular' corner ribbon, the crimson glow shadow, and a slight vertical lift over its neighbours on wide screens.
- **Plus-to-x FAQ accordion** — Native disclosure rows where a crimson plus icon rotates into an x when the item opens.

## 7. Motion

REVIEW —
- Buttons: primary = solid crimson-600 white text rounded-lg; ghost = white with a 1px ink-200 ring that turns crimson on hover; dark = ink-900

## 8. Voice & Brand

A light, serif-accented SaaS pricing page on white with a single crimson accent, audience segmented tabs, a monthly/annual toggle, and a 4-tier grid with one elevated 'most popular' card.

## 9. Anti-patterns

Frameless, fully responsive web page, not a fixed canvas: content is capped at max-w-1240px with fluid side padding, the pricing cards reflow 4 -> 2 -> 1 columns, the controls row stacks on mobile, and the nav link list hides on small screens. The two controls (audience tabs + billing toggle) are the heart of the pattern: copying this design means copying the interaction where one switcher swaps the whole plan set and the other recomputes all prices. Built with Tailwind (CDN) config extending custom 'crimson' and 'ink' palettes plus 'card'/'pop'/'navy' shadows, Fraunces + Inter from Google Fonts, and Phosphor icons via Iconify; tiers are rendered from a JS data object so add/remove/reorder tiers by editing data, not markup. Keep the single-accent discipline (everything that isn't ink is crimson) and the serif-display / sans-body pairing, that contrast is what gives this page its character.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
