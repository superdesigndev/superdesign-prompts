# Design System — Developer Dashboard (E-Ink Paper CI/CD Deployments Console)

> Category: Dashboards  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`developer-dashboard-e-ink-paper-cicd-deployments-console`](../../prompts/developer-dashboard-e-ink-paper-cicd-deployments-console/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

E-ink print-console minimalism: the whole dashboard rendered as near-black ink on warm paper, like a monochrome e-reader or a printed spec sheet. Flat and border-only: 1px hairline dividers at ~14% ink opacity do ALL the separating, with zero drop shadows and zero gradients; the only texture is a faint radial dot-grain on the hero card. Data density IS the aesthetic: IBM Plex Mono tabular figures everywhere numbers appear, uppercase letter-spaced micro-labels, tight 5-8px radii. Semantic states are part of the ink language (filled/half/empty/dashed circles) so the page stays monochrome, and exactly one signal red is rationed to the failed state, which makes failures impossible to miss precisely because nothing else has color.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#f4f1ea`
- `#faf8f3`
- `#141310`
- `#c8321e`

## 3. Typography

- `IBM Plex Sans`
- `IBM Plex Mono`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a strict e-ink paper palette: app canvas #f4f1ea (warm paper), raised cards and sidebar #faf8f3, primary ink #141310, secondary text rgba(20,19,16,0.62), muted meta rgba(20,19,16,0.42), hairline borders rgba(20,19,16,0.14) at 1px. The ONLY accent is signal red #c8321e, used exclusively for the failed deployment row (glyph, id, error text, Redeploy link) and the error lines of the build log. NO drop shadows anywhere, NO gradients, NO blue/green/amber/violet: success is a FILLED INK dot, never green. Texture: a faint dot-grain via radial-gradient(rgba(20,19,16,0.05) 0.5px, transparent 0.5px) on a 4px grid, applied to the hero card only. Fonts: 'IBM Plex Sans' (400/500/600) for UI labels, nav, and headings; 'IBM Plex Mono' (400/500/600) with font-variant-numeric: tabular-nums for every piece of data: deploy ids, commit hashes, branches, durations, ages, timestamps, URLs, log lines, and  …

## 5. Layout

A two-pane app shell at natural page height. LEFT: a fixed ~240px sidebar on raised paper with a hairline right border: workspace switcher, Cmd-K search field, main nav (Overview, Deployments ACTIVE with a 3px solid-ink left rule + semibold, Logs, Analytics, Storage, Settings), an uppercase ENVIRONMENTS group whose items carry ink status glyphs (Production = filled dot, Preview = half ring, dev = empty ring), and a pinned bottom block: a Build-minutes usage card (412/600 with a thin solid-ink progress bar) and a user row. RIGHT main column: (1) a ~52px header bar with breadcrumb 'canvas-app / Deployments', a joined-pill segmented control All/Production/Preview (active = solid ink fill, paper text), a ghost Filter button and ONE solid-ink Deploy button; (2) a CURRENT PRODUCTION hero card (raised paper, hairline, dot-grain) with status line, mono deploy id, underlined mono domain link, a commit chip, a muted meta line, and on the right a 4-stage PIPELINE STRIP; (3) a dense DEPLOYMENTS TABLE in a hairline container: columns Status / Deployment / Branch-Commit / Environment / Duration / Age / Author, ~44px rows in reverse-chronological order; (4) a bottom split row with a LAST FAILED BUILD log card and a DEPLOYS LAST 14 DAYS bar-chart card. Responsive: sidebar stacks above the main column under lg, the table wraps in an overflow-x-auto container so it scrolls horizontally on mobile, the hero card stacks its two blocks, and the bottom split collapses to one column.

## 6. Components

- **Ink status-glyph system** — A monochrome deployment-state vocabulary drawn purely in ink: filled circle = Ready, half-filled ring = Building, empty ring = Queued, dashed ring = Canceled, and a red circle-x reserved as the page's only chroma for Failed.
- **Pipeline stage strip** — A horizontal 4-stage CI pipeline (Build, Test, Bundle, Deploy) drawn as filled ink dots on a hairline rail with per-stage mono durations that sum exactly to the deploy total.
- **Mono build-log excerpt with red error tail** — A paper-ground terminal-style log block: bracketed mono timestamps, info lines in graded ink opacities, and the final error lines in the page's single signal red.
- **Solid-ink usage meter** — A quiet quota card (Build minutes 412/600) with a thin solid-ink progress bar on a hairline track, no color coding.
- **Stepped ink bar chart** — A 14-day deploy-frequency chart of thin solid-ink bars on a hairline baseline with mono axis labels and a mono stat line, no gridlines and no color.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A light "e-ink paper" developer dashboard: a CI/CD deployments console drawn entirely in near-black ink on warm paper with hairline borders, IBM Plex Mono data, ink status glyphs (filled dot ready, half ring building, empty ring queued, dashed canceled), and one signal-red failed deployment with its build log. Two-pane app shell: sidebar with environments + build-minutes meter, current-production hero card with a 4-stage pipeline strip, a dense deployments table, a failed-build log excerpt, and a 14-day deploy-frequency bar chart.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
