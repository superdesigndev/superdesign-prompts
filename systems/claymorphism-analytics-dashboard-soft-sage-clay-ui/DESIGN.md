# Design System — Claymorphism Analytics Dashboard (Soft Sage Clay UI)

> Category: Dashboards  ·  Industry: SaaS
> Auto-scaffolded from prompt [`claymorphism-analytics-dashboard-soft-sage-clay-ui`](../../prompts/claymorphism-analytics-dashboard-soft-sage-clay-ui/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Claymorphism (soft, puffy, pressed clay) on a genuinely MID-TONE dusty-sage ground, deliberately NOT pastel and NOT candy-bright (both already occupied). The whole UI is one soft-clay material: raised surfaces (cards, KPI tiles, buttons, the account chip) use a dual soft shadow - a dark bottom-right shadow plus a light top-left highlight - to read as gently extruded; inset 'sunken' shadows on the search field, credit meter, segmented toggle, and table header make those read as pressed IN. Corners are generously rounded (24-28px on cards, full-round on pills and meters). Colour is restrained: a desaturated sage ground and surfaces carry the design, dark forest-green ink for text, muted sage-grey for secondary text, and four small JEWEL accents used only for meaning - teal (primary / positive), rust (alert / a donut slice), brass (warning / referral), navy (social). No default indigo/violet, no gradients-as-decoration, no emoji. Typography pairs a rounded friendly display (Baloo 2) for headings and numbers with a clean humanist sans (Figtree) for body and labels - the rounded display echoes the puffy clay geometry.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#c5d0be`
- `#dbe2d5`
- `#e2e8dc`
- `#26301f`
- `#6b7663`
- `#14776b`
- `#c4643f`
- `#cf9b34`
- `#22304a`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design an analytics dashboard entirely in a soft claymorphism material on a mid-tone dusty-sage ground (#c5d0be), with clay surfaces #dbe2d5 and #e2e8dc, dark forest ink #26301f, and muted sage-grey #6b7663 for secondary text. Give every raised element (cards, KPI tiles, buttons, avatar, logo tile) a dual soft shadow: a dark bottom-right shadow rgba(88,104,84,.5) at 12px 14px 30px plus a light top-left highlight rgba(255,255,255,.95) at -8px -10px 22px. Give pressed elements (search field, progress meters, the 30D toggle, the table header strip) inset shadows so they read as sunken. Round card corners 24-28px, make pills and meters fully round. Use only four small jewel accents for meaning - teal #14776b (primary/positive), rust #c4643f, brass #cf9b34, navy #22304a - never as background wash. Type: Baloo 2 for headings and big numbers, Figtree for body and labels. No indigo/violet, no de …

## 5. Layout

A two-pane app shell inside a max-width container: a fixed ~260px left sidebar beside a flexible main column. Main = topbar, then a stacked content region: a four-up KPI stat grid, an 8/4 grid pairing the revenue area chart with the traffic donut, and a full-width campaigns table. Responsive: below the md breakpoint the sidebar drops to a full-width block on top, the KPI grid becomes 2-up, the chart and donut stack to one column, and the campaigns table scrolls horizontally within its clay card.

## 6. Components

- **Raised clay card / KPI tile** — The core puffy surface used for every panel and stat tile.
- **Sunken (pressed-in) clay control** — Search field, progress meter, segmented toggle, table header - the 'pressed IN' counterpart.
- **Delta pill** — The up/down change indicator on each KPI tile.
- **Anchored chart tooltip with connector** — A floating value callout tied to its data marker.
- **Segmented range toggle** — The 12M / 30D / 7D chart range switch.
- **Status + channel pills** — The campaigns table's categorical tags.
- **Horizontally scrollable data table** — Keeps a dense 6-column table usable on mobile.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A claymorphism analytics dashboard in mid-tone dusty sage: a puffy sidebar, a four-up KPI stat row with delta pills, a revenue area chart with an anchored tooltip, a traffic-sources donut, and a scrollable campaigns table. Soft pressed-clay surfaces (raised cards, sunken controls), Baloo 2 + Figtree, jewel accents. Fully responsive.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
