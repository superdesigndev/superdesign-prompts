# Design System — Fintech Mobile App: Midnight Mint Navy Wallet Home

> Category: Mobile Apps  ·  Industry: General
> Auto-scaffolded from prompt [`fintech-mobile-app-midnight-mint-navy-wallet-home`](../../prompts/fintech-mobile-app-midnight-mint-navy-wallet-home/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Modern premium fintech, flat and data-forward: a deep ink-navy ground with soft elevated navy cards, a fresh mint + lime accent used sparingly, crisp near-white text, and Space Grotesk numerals for a confident financial voice. Not neon, not glassmorphism, not skeuomorphic.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#0e1626`
- `#0a1120`
- `#17233c`
- `#1d2c49`
- `#c3f24d`
- `#57e0a8`
- `#f2f6ff`
- `#8fa0bf`
- `#ff7a7a`
- `#1c3a2f`
- `#16324a`
- `#14213b`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Deep ink-navy ground (#0e1626, page backdrop #0a1120) with soft elevated cards (#17233c and #1d2c49) and hairline borders (white at ~6%). One fresh accent pair used sparingly: lime #c3f24d for the primary action, the active tab, and the single peak chart bar; mint #57e0a8 for positive numerals, secondary icons, and links. Near-white ink #f2f6ff, muted #8fa0bf for labels and dates, soft red #ff7a7a for expenses. The balance hero is a green-navy gradient (from #1c3a2f via #16324a to #14213b) lit by two large blurred mint/lime radial glows for depth, NOT a frosted-glass blur. Space Grotesk (500-700) for display, headings and every tabular numeral; Inter (400-600) for body and labels. Keep it flat and premium: generous radii (hero ~26px, cards ~24px, rows ~16px), no glassmorphism, no neon wash, no skeuomorphic texture. Set figures in tabular-nums so columns align.

## 5. Layout

A single mobile home screen between two sticky chrome bars: a sticky top bar, a scrolling content column (balance hero, quick actions, spend chart, recent activity), and a sticky bottom tab bar with a raised center FAB. Frameless, max-width 440px centered on large screens, reflows cleanly from 360px to tablet width.

## 6. Components

- **Gradient balance hero with glow depth** — A dark card that earns depth from light, not from glass.
- **Seven-bar weekly spend chart** — A pure-HTML bar chart with one highlighted day, no SVG.
- **Category-tinted transaction row** — A scannable activity row colour-coded by category.
- **Raised center-FAB tab bar** — A five-slot tab bar with a lifted primary action.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A dark premium fintech mobile app home screen (a neobank banking wallet dashboard) in deep ink-navy with a fresh mint and lime accent. A gradient balance hero card shows the total balance, a change pill, a masked card number and a VISA mark; a four-up quick-action row (Send, Request, Top up, More) sits above a Spending this week card with a seven-bar weekly chart, then a Recent activity transaction list with category-tinted icons and signed amounts. A sticky bottom tab bar with a raised center plus FAB anchors the screen. Flat and data-forward, not neon and not glassmorphism, set in Space Grotesk and Inter. Reusable for any banking, wallet, payments, budgeting or finance app home screen.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
