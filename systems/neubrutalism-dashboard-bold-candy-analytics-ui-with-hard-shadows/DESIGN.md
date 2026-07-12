# Design System — Neubrutalism Dashboard: Bold Candy Analytics UI with Hard Shadows

> Category: Dashboards  ·  Industry: SaaS
> Auto-scaffolded from prompt [`neubrutalism-dashboard-bold-candy-analytics-ui-with-hard-shadows`](../../prompts/neubrutalism-dashboard-bold-candy-analytics-ui-with-hard-shadows/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Bold 'candy' neubrutalism: an off-white paper canvas, chunky 2px ink-black borders on absolutely everything, hard (non-blurred) offset drop shadows, generously rounded corners, and a bright accent palette led by hot magenta-pink with canary yellow, mint green and soft lilac supports. Black text always sits on the bright fills (never white on yellow) so contrast stays high. Confident and tactile — cards feel like physical stickers pressed onto the page — but organized and scannable, never cluttered. The dominant color is hot-pink; yellow/mint/lilac are accents for variety across KPI tiles, status pills, and chart series.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#fdf9f0`
- `#ffffff`
- `#111111`
- `#111`
- `#ff3d81`
- `#ffd23f`
- `#3ddc97`
- `#c8a2ff`
- `#ff6b5e`

## 3. Typography

- `Archivo Black`
- `Space Grotesk`
- `Space Mono`
- `Overview`
- `Export report`
- `Revenue over time`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Build a bold candy neubrutalism visual style for a data dashboard. Canvas is off-white paper #fdf9f0 overlaid with a faint 24px square grid (lines rgba(17,17,17,0.05)). Surfaces are white #ffffff cards. Ink #111111 is used for ALL text and the 2px solid borders that outline every card, button, badge, icon tile, nav item, chart bar and input. Signature shadows are HARD and un-blurred, offset toward bottom-right in ink: small 4px 4px 0 #111, medium 6px 6px 0 #111, large 9px 9px 0 #111 (use large on the hero chart card, medium on KPI/table cards, small on buttons/badges/tiles). Corners: cards rounded ~18px, buttons/tiles smaller radius, badges/pills fully pill. Accent palette: HERO hot-pink #ff3d81 (active nav pill, primary button, dominant chart series, one KPI icon tile), canary yellow #ffd23f, mint green #3ddc97, soft lilac #c8a2ff — rotate these across the four KPI icon tiles and use th …

## 5. Layout

A full-bleed desktop web-app shell at ~1440px wide: a fixed 240px white left sidebar with a 2px black right border, then a fluid main column holding a top bar, a 4-up KPI stat row, a 2-column region (a ~2/3 hero chart card next to a ~1/3 right column of two stacked cards), and a full-width activity table at the bottom. Everything is bordered and hard-shadowed; the layout is a clean grid, generous gutters, nothing clipped.

## 6. Components

- **Hard-shadow sticker surfaces** — Every card, button, badge, tile, nav item and chart bar uses a 2px ink border plus a hard, un-blurred offset shadow so it reads like a physical sticker pressed onto the page.
- **Rotating-accent KPI stat cards** — Four bordered stat cards, each with a differently-colored bordered icon tile, a big Archivo Black number, a label, and a mint/coral delta chip with a mono comparison note.
- **Inline-SVG grouped bar chart** — A dependency-free 12-month grouped bar chart where each month pairs a hot-pink 'this year' bar with a thinner lilac 'last year' bar, all outlined in black, over a real labelled y-axis.
- **Bordered donut with legend** — A ring chart for traffic sources with a centered session count and an accent-coded legend, drawn cleanly so a still frame renders it correctly.
- **Bold status pills** — Data-table status labels rendered as bold bordered pills in the accent palette with black text, so state is scannable at a glance.
- **Filled active nav pill** — The current sidebar route is a solid hot-pink hard-shadowed pill while the rest are plain icon rows, making the active location unmistakable.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A bold neubrutalism (neo-brutalist) SaaS analytics dashboard on an off-white canvas where every card, button, badge and chart bar carries a 2px black border and a hard, un-blurred offset drop shadow. A 240px sidebar (bolt logo, a hot-pink filled "Overview" nav pill, icon nav rows, a workspace card) sits beside a top bar with a bordered search field, a date-range pill, and a filled hot-pink "Export report" button. The body stacks a 4-card KPI row (Revenue $48.2k, Active users, Conversion, New signups, each with a colored icon tile and a mint/coral delta chip), a hero "Revenue over time" card holding a 12-month grouped inline-SVG bar chart (hot-pink "this year" + lilac "last year" bars with a real y-axis), a right column with a "Traffic sources" donut and a "Top content" list of ranked progress bars, and a full-width "Recent activity" table with monogram avatars, colored status pills, mono amounts and timestamps. Bold candy palette: off-white #fdf9f0, ink #111111, hot-pink #ff3d81, canary #ffd23f, mint #3ddc97, lilac #c8a2ff. Fonts: Archivo Black, Space Grotesk, Space Mono. Reusable for any SaaS, creator, or product analytics dashboard.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
