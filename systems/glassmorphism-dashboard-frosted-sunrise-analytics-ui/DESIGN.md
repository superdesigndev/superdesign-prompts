# Design System — Glassmorphism Dashboard: Frosted Sunrise Analytics UI

> Category: Dashboards  ·  Industry: SaaS
> Auto-scaffolded from prompt [`glassmorphism-dashboard-frosted-sunrise-analytics-ui`](../../prompts/glassmorphism-dashboard-frosted-sunrise-analytics-ui/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Warm, airy, high-contrast glassmorphism. The signature is frosted-WHITE glass (not dark glass) over a warm SUNRISE aurora, so it reads bright and premium instead of moody. Cards are semi-transparent white (linear-gradient from ~0.74 to ~0.56 alpha) with backdrop-blur ~22px and saturate(150%), a 1px near-white border, an inset top highlight, and a soft warm-brown shadow — they look like frosted glass panes lit from behind. The background is a multi-stop radial aurora: peach (#ffd9a8) top-left, coral (#ff9d7a) top-right, warm amber bottom-right, a soft rose (#ff8fa0) bottom-left, over a pale peach base — plus a faint blurred coral/amber bloom layer. Ink is near-black #1c1512 for headings and numbers, #5c5049 for secondary text, #8a7768 for muted labels; the ONE accent is a saturated coral #f2521b (with a deeper #d8410f and a warm amber #ef8f2a as supporting hues, and rose #fb7185 only for negative/decorative). Status uses emerald for positive, rose for negative. Type pairs a grotesk DISPLAY face (Space Grotesk) for headings with a clean sans (Inter) for body and a MONO (JetBrains Mono, tabular figures) for every number, which gives the data a precise, engineered feel. Generous rounding (rounded-3xl cards, rounded-2xl chips/buttons), soft shadows, and small coloured pills. ABSOLUTELY no indigo/violet/blue gradient — the warmth is the identity.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#ffd9a8`
- `#ff9d7a`
- `#ff8fa0`
- `#1c1512`
- `#5c5049`
- `#8a7768`
- `#f2521b`
- `#d8410f`
- `#ef8f2a`
- `#fb7185`
- `#fff2e6`
- `#ffd9c4`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a LIGHT, warm, high-contrast glassmorphism dashboard. Float frosted-WHITE glass cards over a warm SUNRISE aurora background — do NOT use a dark glass or any indigo/violet/blue gradient. Build the background from layered radial-gradients: peach #ffd9a8 top-left, coral #ff9d7a top-right, warm amber bottom-right, soft rose #ff8fa0 bottom-left, over a pale peach base (#fff2e6 to #ffd9c4), plus a faint blurred coral/amber bloom. Make every card semi-transparent white (linear-gradient rgba(255,255,255,0.74) to 0.56) with backdrop-filter blur(22px) saturate(150%), a 1px rgba(255,255,255,0.78) border, an inset top highlight, and a soft warm shadow (rgba(120,60,20,0.28)). Use near-black ink #1c1512 for headings/numbers, #5c5049 secondary, #8a7768 muted; ONE saturated accent coral #f2521b (deeper #d8410f, supporting amber #ef8f2a; rose #fb7185 only for negatives). Keep all functional text a …

## 5. Layout

A gap-separated glass layout on the aurora: a slim sticky LEFT ICON RAIL, and to its right a MAIN column of a sticky top bar, a 4-up KPI row, a 2/3 + 1/3 chart+donut row, and a 2/3 + 1/3 table+goal row. Desktop uses a 4-col KPI grid and 3-col content grid (chart/table span 2). At ~1024 the KPI grid drops to 2 columns and the content rows stack to full-width; at mobile the rail hides and everything is one column. Top bar and rail are sticky.

## 6. Components

- **Warm sunrise aurora background** — The signature backdrop — layered radial gradients in peach/coral/amber/rose, NOT the default blue.
- **Frosted-white glass card** — Light glass panes lit from behind — the light counterpart to dark glassmorphism.
- **KPI card with delta pill + sparkline** — A dense stat tile: icon chip, coloured trend pill, big mono number, mini sparkline.
- **Inline-SVG area chart with comparison line** — A real area chart, hand-drawn in SVG, with a dashed last-year line.
- **Segmented donut with legend** — Traffic-source ring using stroke-dasharray segments.
- **Radial goal + gradient progress bars** — A coral progress ring plus labelled coral-to-amber bars.
- **Status pill** — Small rounded-full state chips in the warm/status palette.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A light, warm, high-contrast glassmorphism SaaS analytics dashboard (desktop). Frosted white glass cards with backdrop-blur, a hairline white border and a soft shadow float over a warm *sunrise* aurora gradient (peach to coral to amber, with a soft rose corner). Text is near-black ink for strong contrast, and a single saturated coral is the only accent. Layout: a compact left icon rail, a top bar with search + date range + notifications + avatar, a row of four KPI stat cards (big mono numbers, trend-delta pills, tiny sparklines), a large inline-SVG area chart with a dashed last-year comparison line, a donut traffic-source card, a scannable transactions data table with status pills, and a monthly-goal radial with progress bars. Typography pairs Space Grotesk (display) with Inter (body) and JetBrains Mono (numerals). The airy, warm alternative to a dark glass dashboard.

Source: https://templatemo.com/tm-607-glass-admin

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
