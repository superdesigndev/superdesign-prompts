# Design System — Dashboard UI: Dark Linear-Style Developer Issue Tracker

> Category: Dashboards  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`dashboard-ui-dark-linear-style-developer-issue-tracker`](../../prompts/dashboard-ui-dark-linear-style-developer-issue-tracker/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Dark, dense, cool-indigo product-UI minimalism in the Linear register — a real working issue tracker, not a marketing page. Near-black canvases (#08090a app / #0c0d0f sidebar / #0b0c0e main) with ONE typeface (Inter) in cool near-white #f4f5f8, hierarchy from SIZE and WEIGHT (450-500 titles / 500 nav-and-headers / muted 12px ids and dates in #7d828c), never from color. Color is rationed to a SINGLE indigo/violet accent #5e6ad2 (the one filled 'New issue' button + the active-item tint), plus small semantic hues confined to status rings, priority glyphs, and label-pill dots. The shape language is FLAT and BORDER-ONLY: the sidebar and rows are separated by hairline rgba(255,255,255,0.07) dividers, never by drop shadows; radii are tight (5-8px). The register is quiet, keyboard-first, information-dense, and engineered — space and hairlines do the organizing, and the whole thing is unmistakably a dark product app.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#08090a`
- `#0c0d0f`
- `#0b0c0e`
- `#f4f5f8`
- `#7d828c`
- `#5e6ad2`

## 3. Typography

- `New issue`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a dark, cool-indigo 'Linear-style' developer issue tracker as a two-pane app shell. Use near-black canvases (app #08090a, sidebar #0c0d0f, main #0b0c0e) and ONE typeface only (Inter); build hierarchy from SIZE and WEIGHT, never from color: issue titles ~13.5px/weight 450-500 in cool near-white #f4f5f8, nav items and group headers 13px/weight 500, muted ids/dates/meta 12px in #7d828c. Ration color to a SINGLE indigo/violet accent #5e6ad2 — use it ONLY for the one filled 'New issue' button and the active-item tint — and confine all other hue to small semantic status rings, priority glyphs, and label-pill dots. Make everything FLAT and BORDER-ONLY: separate the sidebar and every row with 1px rgba(255,255,255,0.07) hairlines, NOT drop shadows; use tight radii (5-8px). Keep the type high-contrast on the dark canvas and never drop below 12px. Do NOT introduce a second typeface, drop sha …

## 5. Layout

A two-pane app shell: (1) a fixed ~240px left sidebar on #0c0d0f with a hairline right border — a workspace switcher (glyph + name + chevron), a ⌘K search field, primary nav (Inbox with a count badge, My Issues), a 'WORKSPACE' nav group (Initiatives / Views / Teams), a 'YOUR TEAMS' group with an expanded 'Engineering' team (Issues active, Cycles, Projects) and a collapsed 'Design' team, and a pinned user card; (2) a main column stacking a header bar ('Issues' breadcrumb + an All/Active/Backlog segmented control + ghost Filter/Display buttons + a single indigo 'New issue' button), a thin 'N issues · Grouped by status' strip, and a grouped issue list of three collapsible status groups (In Progress / Todo / Backlog) of dense issue rows. On a narrow viewport the sidebar collapses to an icon rail or drawer, the right-side label pills and dates hide first, and the list stays full-width and vertically scrollable with sticky group headers.

## 6. Components

- **Grouped app-shell sidebar with teams + user card** — A fixed ~240px dark sidebar: workspace switcher, ⌘K search, primary nav, labeled WORKSPACE + YOUR TEAMS groups with an expanded team and an active sub-item, and a pinned user card.
- **Dense grouped issue list** — Collapsible status groups (with a colored status icon + label + count) over dense ~40px issue rows separated by hairlines, each row a priority icon, mono id, status ring, title, label pills, date, and assignee avatar.
- **Priority + status icon system** — A compact set of inline-SVG glyphs — urgent red square-!, high/med/low bar-graph bars, no-priority dashes; status rings for In Progress / Todo / Backlog / Done / Canceled — all legible on a dark canvas.
- **Header bar with segmented view tabs + single indigo action** — A ~48px header with a breadcrumb, an All/Active/Backlog segmented control, ghost Filter/Display buttons, and exactly one filled indigo 'New issue' button.
- **Single-typeface dark type + flat border-only surfaces** — One Inter family in a cool near-white on near-black; every surface separated by hairlines, not shadows, with a single indigo accent.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A dark, cool-indigo "Linear-style" developer/product DASHBOARD built as a two-pane app shell around a grouped ISSUE TRACKER list. A fixed ~240px sidebar (workspace switcher, ⌘K search, Inbox/My Issues, WORKSPACE + YOUR TEAMS nav with an active team, a pinned user card) sits beside a main column: a header bar with an "All Issues/Active/Backlog" segmented control, ghost Filter/Display buttons, and a single solid indigo "+ New issue" button, then a dense grouped issue list (In Progress / Todo / Backlog) where each ~40px row shows a priority glyph, a muted mono ENG-### id, a status ring, the issue title, colored label pills, a due date, and a tinted assignee avatar. Near-black canvas, cool near-white text, ONE indigo accent, one Inter typeface, flat and border-only with hairline dividers. Reusable for any issue tracker, project/task app, internal tool, or dense dark B2B product UI.

Source: https://linear.app (dark product-UI visual language)

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
