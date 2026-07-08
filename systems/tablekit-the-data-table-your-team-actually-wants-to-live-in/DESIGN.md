# Design System — Tablekit — The data table your team actually wants to live in

> Category: Dashboards  ·  Industry: SaaS
> Auto-scaffolded from prompt [`tablekit-the-data-table-your-team-actually-wants-to-live-in`](../../prompts/tablekit-the-data-table-your-team-actually-wants-to-live-in/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Light, dense SaaS-admin aesthetic. Cobalt accent on a near-white canvas, Inter throughout with tabular numerals and tight letter-spacing, soft layered shadows, generous rounding on the panel but tight rounding on controls. Status conveyed by semantic color (cobalt/amber/violet/slate/emerald/rose) on pale tinted badge fills.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#f8fafc`
- `#0f172a`
- `#eef4ff`
- `#dbe6ff`
- `#bdd1ff`
- `#93b4ff`
- `#608dff`
- `#3b6bff`
- `#2563eb`
- `#1d4ed8`
- `#1e40af`
- `#94a3b8`
- `#64748b`
- `#475569`
- `#7c899c`
- `#e2e8f0`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design system: light mode, page background #f8fafc, primary ink text #0f172a. Accent is a cobalt ramp: 50 #eef4ff, 100 #dbe6ff, 200 #bdd1ff, 300 #93b4ff, 400 #608dff, 500 #3b6bff, 600 #2563eb (primary buttons/brand), 700 #1d4ed8 (hover), 800 #1e40af (dark text on tint). Neutral text uses Tailwind slate (slate-400 #94a3b8, slate-500 #64748b, slate-600 #475569) plus a custom muted-uppercase slate-450 #7c899c for table headers. Borders are slate-200 (#e2e8f0). Semantic badge colors: amber (Bug), violet (Docs), slate (Chore), emerald (Done), rose (High priority / Delete). Typeface: Inter (weights 400/450/500/600/700/800), -webkit-font-smoothing antialiased, font-feature-settings 'cv05' 1,'ss01' 1,'tnum' 1; numeric/data cells use tabular-nums. Letter-spacing -0.012em on headings ('tightish'). Shadows: card = 0 1px 2px rgba(15,23,42,.04), 0 1px 3px rgba(15,23,42,.06); panel = 0 1px 3px rgba(15 …

## 5. Layout

Single-column, max-width 1240px centered. Vertical flow: sticky nav (56px) -> full-bleed hero with dotted grid + masked fade -> centered <main> holding a section heading row and one large rounded panel that stacks filter bar / bulk-action bar / scrollable sticky-header table / pagination footer -> a slim page footer. Table is horizontally min-width 760px and scrolls inside a max-height 560px scroll container so the header stays sticky.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

REVIEW —
- Accent is a cobalt ramp: 50 #eef4ff, 100 #dbe6ff, 200 #bdd1ff, 300 #93b4ff, 400 #608dff, 500 #3b6bff, 600 #2563eb (primary buttons/brand), 700 #1d4ed8 (hover), 800 #1e40af (dark text on tint)

## 8. Voice & Brand

Dense light-mode admin data table (Tablekit): blurred sticky nav, dotted-grid hero, a cobalt-on-white panel with a filter bar, bulk-action bar, sticky-header scroll table with colored status/priority/type badges and avatar chips, and a full pagination footer.

## 9. Anti-patterns

Keep it dense and tabular: numerals must be tabular-nums and type tight; this is an information surface, not a marketing page. The cobalt-600 #2563eb is the only saturated color used structurally (brand tile, primary buttons, selection, active states); every other color is a low-saturation semantic tint used only inside badges/icons. The sticky header must live on the scroll container (thead sticky top-0), not the page, so it stays put while body rows scroll under it. Use Inter with tabular-nums + 'tightish' (-0.012em) heading tracking, soft layered shadows, and a glowing cobalt 'pop' shadow reserved for primary CTAs. Mobile reflow: nav center links and the search/⌘K hide, badge facet chips and secondary labels hide, the table stays horizontally scrollable at min-width 760px.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
