# Design System — Emerald 4-Tier SaaS Pricing Table

> Category: Pricing Pages  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`emerald-4-tier-saas-pricing-table`](../../prompts/emerald-4-tier-saas-pricing-table/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Premium light SaaS aesthetic: near-white paper background (#fbfdfb) with a faint emerald dot/grid hero wash, emerald-600 (#059669) as the single accent across logo, primary buttons, highlighted plan ring, badges and the CTA gradient. Ink-toned neutral text scale (almost-black headings #0c1410 down to muted #7d8d85). Sora for display/headings (geometric, tight tracking), Inter for body/UI. Generous whitespace, rounded-2xl cards, two layered soft green-tinted shadows, hairline #e7efe9 dividers, tabular-nums on prices.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#fbfdfb`
- `#059669`
- `#0c1410`
- `#7d8d85`
- `#e7efe9`
- `#ecfdf5`
- `#d1fae5`
- `#a7f3d0`
- `#6ee7b7`
- `#34d399`
- `#10b981`
- `#047857`
- `#065f46`
- `#064e3b`
- `#1f2a24`
- `#566a60`

## 3. Typography

- `Sora`
- `Inter`
- `Most popular`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Light-mode SaaS visual system. Background paper #fbfdfb. Single accent = emerald family: emerald-50 #ecfdf5, 100 #d1fae5, 200 #a7f3d0, 300 #6ee7b7, 400 #34d399, 500 #10b981, 600 #059669 (primary), 700 #047857, 800 #065f46, 900 #064e3b. Neutral 'ink' text scale: ink-900 #0c1410 (headings), ink-700 #1f2a24 (body/strong), ink-500 #566a60 (secondary), ink-400 #7d8d85 (muted/captions). Hairline divider/border = 'line' #e7efe9. Typography: display font 'Sora' (weights 500/600/700, tight -tracking, used for logo, h1/h2, prices, plan names) and body font 'Inter' (weights 400/500/600) for everything else; antialiased. Shapes: rounded-2xl cards, rounded-lg buttons/badges, rounded-full pills and toggle. Shadows: two custom soft greens — card-pop = '0 1px 2px rgba(6,78,59,0.04), 0 8px 24px -12px rgba(6,78,59,0.12)' and a stronger card-pop-hi = '0 4px 12px rgba(6,78,59,0.08), 0 24px 48px -18px rgba(5 …

## 5. Layout

Frameless, fully responsive single-column web page (not a fixed-frame mockup): centered max-w-6xl content, sticky translucent nav, centered hero with billing toggle, then the 4-tier pricing block, a centered FAQ accordion, and a gradient CTA + footer. The pricing tiers reflow from a fused 4-column bordered table on desktop -> 2 columns on tablet -> 1 stacked column on mobile.

## 6. Components

- **Monthly/Annual billing toggle (CSS-only)** — A pill switch between 'Monthly' and 'Annual' labels with a 'Save 20%' pill; flipping it swaps every plan's displayed price and the active-side label color, with no JavaScript.
- **Highlighted 'Most popular' plan column** — The Pro column is visually promoted out of the fused table: thicker emerald ring, deeper green shadow, lifted/scaled, raised z-index, and a badge straddling its top border.
- **Fused-table pricing grid with aligned rows** — Four plan columns that merge into a single bordered card on desktop using internal hairline dividers, with fixed-height head blocks so price rows, dividers, and checklists line up across columns.
- **Feature checklist rows** — Per-plan 'Includes / Everything in X, plus' lists of emerald-check + label rows.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A light-mode emerald-accented SaaS pricing page with a Monthly/Annual toggle and four tiers fused into one bordered table, the Pro column lifted and ring-highlighted as 'Most popular'.

## 9. Anti-patterns

This is a FRAMELESS, fully responsive real web page, not a fixed-canvas mockup: content is centered in a max-w-6xl container, the nav is sticky and translucent (backdrop-blur), and the pricing tiers reflow 4-col fused table -> 2-col -> 1-col across breakpoints. Reproduce the EXACT palette (paper #fbfdfb, emerald-600 #059669 accent, ink text scale #0c1410/#1f2a24/#566a60/#7d8d85, hairline #e7efe9) and fonts (Sora display, Inter body). Built with Tailwind (CDN) + iconify (Phosphor 'ph:' icons) and two custom green box-shadows; the billing toggle and FAQ accordion are pure CSS (no JS). The whole layout reads as one accent color on near-white with lots of whitespace — keep it restrained, do not add a second accent hue.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
