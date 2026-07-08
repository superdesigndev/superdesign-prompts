# Design System — Slate ROI-Calculator Pricing

> Category: Pricing Pages  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`slate-roi-calculator-pricing`](../../prompts/slate-roi-calculator-pricing/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Electric-mint-on-inky-slate dev-tool aesthetic: a deep near-black background system with a single saturated mint-green accent used for emphasis, CTAs, and data highlights. Geometric display type for headlines, a clean grotesque for body, and a monospace for labels/numbers. Subtle faint-green grid texture and a soft radial glow behind hero/CTA sections give it a 'terminal lit from above' feel. Glows and 1px tinted borders stand in for heavy shadows.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#0a0f14`
- `#0c1219`
- `#0e151d`
- `#121b25`
- `#16202c`
- `#1b2734`
- `#22313f`
- `#33485b`
- `#5a7287`
- `#7c93a6`
- `#a3b5c4`
- `#34e89e`
- `#4dffb0`
- `#1faf78`
- `#0d3a2c`
- `#ffffff`

## 3. Typography

- `Space Grotesk`
- `Inter`
- `JetBrains Mono`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Build a dark, high-contrast developer-tool style. Background palette is a custom near-black 'slate' ramp: slate-950 #0a0f14 (page bg / nav), slate-925 #0c1219, slate-900 #0e151d (cards / surfaces), slate-850 #121b25 (highlighted card), slate-800 #16202c, slate-750 #1b2734, slate-700 #22313f (slider tracks / borders), slate-600 #33485b, slate-500 #5a7287, slate-400 #7c93a6 (muted text), slate-300 #a3b5c4 (body text). The single accent is 'signal' mint-green: DEFAULT #34e89e, bright #4dffb0 (hover), dim #1faf78, deep #0d3a2c. Pure white #ffffff for primary headings; white/5–white/12 translucent overlays for hairline borders and subtle hover fills. Typography: display font 'Space Grotesk' (weights 400–700) for headlines and prices; body font 'Inter' (400/450/500/600/700); monospace 'JetBrains Mono' (400–600) for eyebrow labels, numbers (with tabular-nums), and badges. Texture: a faint mint  …

## 5. Layout

Frameless responsive single-column page, max content width ~1180px centered with px-6 gutters. Reading order top to bottom: announcement bar, sticky translucent nav, hero headline + ROI calculator, billing toggle + 4 plan cards, comparison table, FAQ accordion, glowing CTA band, multi-column footer. The pricing system itself spans three coordinated pieces: an interactive ROI calculator, the tiered plan grid with a billing toggle, and a feature comparison table. Cards reflow 4-col -> 2-col -> 1-col; nav is sticky with backdrop blur.

## 6. Components

- **Interactive ROI / savings calculator** — The page's hero centerpiece: three range sliders whose live values drive a big animated monthly-savings figure, an hours-reclaimed stat, a 3-line cost ledger, and a Net ROI multiplier pill.
- **Monthly / Annual billing toggle** — A segmented rounded-full pill switch that swaps every plan price between monthly and annual values, with the active segment filled mint and Annual showing a '-20%' savings tag.
- **Highlighted 'Most Popular' Pro card** — The recommended tier, lifted out of the row with a solid fill, mint accents, a mint glow shadow, and a notched badge.
- **Custom mint range slider** — Reusable dark slider styling: thin rounded track that fills mint up to the current value, with a glowing mint thumb.
- **Feature comparison table with Pro column highlight** — Horizontally scrollable plan-vs-feature matrix using mint checks, muted minus marks, an infinity glyph, and a tinted Pro column.

## 7. Motion

REVIEW —
- The single accent is 'signal' mint-green: DEFAULT #34e89e, bright #4dffb0 (hover), dim #1faf78, deep #0d3a2c
- Pure white #ffffff for primary headings; white/5–white/12 translucent overlays for hairline borders and subtle hover fills

## 8. Voice & Brand

A frameless dark SaaS pricing page in inky slate with one electric mint accent: an interactive ROI savings calculator, a 4-tier plan grid with a highlighted Pro card and monthly/annual toggle, a comparison table, and an accordion FAQ.

## 9. Anti-patterns

Frameless, fully responsive single page (no app chrome / window frame): content is centered in a ~1180px max-width container; the plan grid reflows 4 -> 2 -> 1 column, the calculator's two panes stack and flip their divider, the comparison table switches to horizontal scroll, and nav/buttons collapse on mobile. The nav is sticky with backdrop blur. Three Google fonts (Space Grotesk, Inter, JetBrains Mono) and Iconify lucide icons. Two small bits of vanilla JS power the experience: the live ROI calculator and the billing toggle (no framework). The mint 'signal' green is the only accent; everything else is the inky slate ramp, so it should stay restrained and used for emphasis only.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
