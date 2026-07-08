# Design System — Editorial Violet SaaS Pricing Matrix

> Category: Pricing Pages  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`editorial-violet-saas-pricing-matrix`](../../prompts/editorial-violet-saas-pricing-matrix/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Clean, premium, editorial light theme. Off-white 'paper' page (#fbfbfa) with a very subtle dot-grain texture in the hero, hairline warm-grey borders (#eceae5) everywhere to draw the grid, near-black 'ink' text, and ONE saturated accent: electric violet (#5b4af0). The Pro/featured column is washed in a pale violet tint (violet-soft #efedfd). The logo mark is the one high-contrast pop: a black rounded square with a LIME (#c9f24a) sparkle glyph. Numbers use tabular-nums. Generous whitespace, restrained shadows (one soft violet-tinted glow on the featured card/matrix).

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#fbfbfa`
- `#eceae5`
- `#5b4af0`
- `#efedfd`
- `#c9f24a`
- `#0f1115`
- `#2b3038`
- `#4a525f`
- `#6b7480`
- `#9aa2ad`
- `#ffffff`
- `#4536c4`

## 3. Typography

- `Space Grotesk`
- `Inter`
- `JetBrains Mono`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Build a light, editorial pricing page. Palette: page background paper off-white #fbfbfa; primary text ink-900 #0f1115; secondary inks #2b3038 (ink-700), #4a525f (ink-600), #6b7480 (ink-500), #9aa2ad (ink-400); hairline borders/dividers line #eceae5; cards/surfaces pure white #ffffff. Single accent = electric violet #5b4af0 (DEFAULT), with #efedfd (violet-soft) as a pale tint fill and #4536c4 (violet-deep) for hover/emphasis text. Reserve lime #c9f24a only for the sparkle glyph inside the black logo square. Typography: display/headlines in 'Space Grotesk' 700 with tight tracking (-0.02em), body/UI in 'Inter' (weights 400-700, note the unusual 450 and 500 micro-weights), and all data/section-eyebrows in 'JetBrains Mono' (uppercase, letter-spacing ~0.14em for section labels). Use tabular-nums on every price and quantity. Apply antialiasing and optimizeLegibility. Keep shadows almost invisib …

## 5. Layout

Frameless, fully responsive web page on an off-white canvas, max content width ~1180px, generous horizontal padding. Vertical flow: sticky top nav -> hero (eyebrow pill, two-line headline, sub, billing toggle) -> the comparison matrix (the hero of the page) -> two-column FAQ -> slim footer. The matrix is the defining element: on md+ it is ONE bordered white card laid out as a CSS grid with a 1.35fr label column + three equal plan columns, a header row that sticks under the nav, and feature rows split into mono-labeled groups; below md it REFLOWS into three stacked plan cards (each plan's features become a bulleted check-list). Cards/columns reflow 3 -> 2 -> 1 across breakpoints; nav stays sticky.

## 6. Components

- **Full-width grouped comparison matrix** — The page's centerpiece: instead of three floating price cards, one bordered white card holds a sticky plan header + feature rows arranged as a CSS grid, with features bucketed into labeled groups and the featured (Pro) column tinted down its full height.
- **Highlighted 'Popular' plan treatment** — The Pro plan is visually elevated wherever it appears — a violet-soft tint, a 3px violet top bar (matrix) or 2px violet border (mobile card), an uppercase 'Popular' badge, violet plan name and violet check icons, and a solid violet CTA.
- **Live monthly/annual price toggle** — A segmented pill toggle (active = solid black) plus a 'Save 20%' tag that, on click, rewrites every Pro and Team price element on the page in real time.
- **Lime-on-black sparkle logo mark** — Brand lockup: a small black rounded-square holding a lime sparkle icon, next to the 'Promptbook' wordmark in Space Grotesk. It is the only place the lime accent appears.

## 7. Motion

REVIEW —
- Single accent = electric violet #5b4af0 (DEFAULT), with #efedfd (violet-soft) as a pale tint fill and #4536c4 (violet-deep) for hover/emphasis text

## 8. Voice & Brand

A light, editorial SaaS pricing page led by a full-width grouped comparison matrix with a sticky 3-plan header, electric-violet accent, and a monthly/annual toggle.

## 9. Anti-patterns

FRAMELESS, fully responsive web page (not a fixed-size artboard): content centers in a ~1180px max-width column and everything reflows — the comparison matrix is a CSS grid (1.35fr + three equal plan columns) on md+ that collapses into stacked per-plan cards (3 -> 2 -> 1 column) below md, and the top nav stays sticky on scroll. Two sticky layers (nav at top:0, matrix plan-header at top:16) coexist. The whole page is one accent system: near-black ink on off-white paper, electric violet #5b4af0 as the sole UI accent (with the featured column tinted violet-soft), and lime reserved exclusively for the logo sparkle. Keep hairline #eceae5 borders on every cell/divider — the visible grid is core to the look. Fonts: Space Grotesk (display), Inter (UI/body, includes 450/500 micro-weights), JetBrains Mono (prices use tabular-nums and section eyebrows use uppercase mono with wide tracking). Replace the placeholder brand/prices/copy with your own; the transferable value is the matrix-led layout + this restrained editorial palette and type pairing.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
