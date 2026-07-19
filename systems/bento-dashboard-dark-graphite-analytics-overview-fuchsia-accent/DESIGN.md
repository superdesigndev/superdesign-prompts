# Design System — Bento Dashboard (Dark Graphite Analytics Overview, Fuchsia Accent)

> Category: Dashboards  ·  Industry: SaaS
> Auto-scaffolded from prompt [`bento-dashboard-dark-graphite-analytics-overview-fuchsia-accent`](../../prompts/bento-dashboard-dark-graphite-analytics-overview-fuchsia-accent/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Dark bento on a cool graphite ground - flat, precise, 'data console'. The mosaic is built from matte tiles that sit just proud of the ground: each tile is a rounded 22px surface (#16181f, the revenue hero #1b1e27) with a 1px hairline border (#262a35), a faint inset top highlight (inset 0 1px 0 rgba(255,255,255,0.05)) so it reads gently extruded, two soft dark shadows, and a springy translateY(-4px) hover-lift. Colour is disciplined: FUCHSIA #ec4899 (deep #db2777) is the ONE brand chroma - the logo tile, the active nav pill, the primary revenue line + gradient fill, the goal ring, and the primary button. Teal #2dd4bf, amber #f5b544, and violet #8b7cff appear ONLY as data-viz series and donut-segment colours (category-native, never as decoration or background wash). Text is bone #f2f3f7 for headings and cool grey #a6abb8 for body, with muted #6b7180 tracked-caps eyebrows and axis labels. No default indigo/violet gradient background, no gradient-as-decoration, no emoji. Typography pairs Manrope (500-800, tracking-tight bold) for headings and UI with IBM Plex Mono (400-500) for every numeral, tracked-caps label, axis figure, and table cell - the mono is the 'data console' signal and keeps the numbers tabular-aligned.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#16181f`
- `#1b1e27`
- `#262a35`
- `#ec4899`
- `#db2777`
- `#2dd4bf`
- `#f5b544`
- `#8b7cff`
- `#f2f3f7`
- `#a6abb8`
- `#6b7180`
- `#0e0f14`

## 3. Typography

- `Overview`
- `Last 30 days`
- `Top pages`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design the in-app 'Overview' screen of a product-analytics dashboard as a dark bento mosaic on a cool graphite ground #0e0f14. Build it from rounded 22px tiles in #16181f (the revenue hero tile #1b1e27), each with a 1px hairline border #262a35, a faint inset top highlight rgba(255,255,255,0.05), two soft dark shadows (0 12px 30px -14px rgba(0,0,0,.7) and 0 22px 50px -20px rgba(0,0,0,.8)), and a springy translateY(-4px) hover-lift on cubic-bezier(.34,1.4,.64,1). Use fuchsia #ec4899 (deep #db2777) as the ONLY brand accent - logo tile, active nav pill, revenue line + gradient fill, goal ring, primary button - and use teal #2dd4bf, amber #f5b544, violet #8b7cff ONLY as chart series and donut segments, never as a background wash. Text: bone #f2f3f7 headings, cool grey #a6abb8 body, muted #6b7180 tracked-caps eyebrows and axis. Type: Manrope for headings and UI, IBM Plex Mono for every number, …

## 5. Layout

A slim sticky top app bar over a page header row, then a 4-column bento grid (max-width ~1320px, centered, 18px gaps) with explicit mixed spans: a 2x2 revenue hero, two 1x1 KPI tiles, a 1x2 tall live-activity feed, a 1x2 tall traffic-sources donut, a 1x1 MRR goal gauge, and a 3x1 wide top-pages table. Responsive: 4 columns on desktop, 2 columns on tablet (the revenue hero spans full width), and one column on mobile where every tile stacks, the charts scale to 100% width, and the top-pages table scrolls horizontally inside its tile. The top-bar center nav links hide below md.

## 6. Components

- **Bento tile** — The core mixed-span surface used for every panel in the mosaic.
- **Anchored chart tooltip with connector** — A floating value callout tied to its data marker on the revenue chart.
- **Radial goal gauge** — The MRR-goal progress ring.
- **Delta pill** — The up/down change indicator on KPI tiles.
- **Micro data-viz (sparkline / micro-bars)** — The bottom-anchored mini charts inside the KPI and table tiles.
- **Live activity feed row** — One event line in the tall activity tile.
- **Horizontally scrollable data table** — Keeps the dense Top pages table usable on mobile.

## 7. Motion

REVIEW —
- 05)) so it reads gently extruded, two soft dark shadows, and a springy translateY(-4px) hover-lift
- 8)), and a springy translateY(-4px) hover-lift on cubic-bezier(

## 8. Voice & Brand

A dark bento analytics dashboard: the in-app "Overview" screen of a product, laid out as a mixed-span bento mosaic on a cool graphite ground with a single fuchsia accent. A slim top bar (logo, Overview / Audiences / Revenue / Reports nav, search, a "Last 30 days" date pill, a bell, an avatar) sits over a bento grid: a 2x2 revenue hero tile (big number, delta pill, a 12M/30D/7D toggle, and a fuchsia area chart with a tooltip anchored above its marker), two KPI stat tiles (active users with a teal sparkline, conversion rate with an amber micro bar chart), a tall live-activity feed, a tall traffic-sources donut with a legend, a fuchsia MRR-goal radial gauge, and a wide "Top pages" table with per-row trend sparklines. Manrope headings, IBM Plex Mono numerals, teal / amber / violet used only as data-viz colors. Fully responsive. Reusable for any SaaS product-analytics, admin, or metrics dashboard.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
