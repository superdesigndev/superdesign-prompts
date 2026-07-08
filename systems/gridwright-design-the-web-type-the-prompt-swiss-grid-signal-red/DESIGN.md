# Design System — Gridwright — Design the web, type the prompt (Swiss Grid / Signal Red)

> Category: Pricing Pages  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`gridwright-design-the-web-type-the-prompt-swiss-grid-signal-red`](../../prompts/gridwright-design-the-web-type-the-prompt-swiss-grid-signal-red/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

International Typographic Style (Swiss design) for a developer tool: pure white paper, near-black ink, and exactly one signal red used surgically for the accent word, primary CTAs, indicator dots, the Popular badge and the CTA band. The page is built as an explicit 12-column grid where every section sits inside drawn 1px hairlines, so the structure itself is the decoration. Inter does all the work across nine weights, set very tight on display type; tabular numbers for stats and prices; uppercase wide-tracked micro-labels and a mono register for metadata. No gradients, no shadows, no rounded corners. Black-on-white that flips to white-on-black on hover and in the Pro/workflow/CTA panels.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#0a0a0a`
- `#ffffff`
- `#ff3b30`
- `#fafafa`
- `#111`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Swiss / International Typographic Style, stark and grid-driven. Palette is three tokens only: ink #0a0a0a (near-black, all primary text + dark panels), paper #ffffff (page + inverted text), and signal #ff3b30 (the single accent: hero accent word 'prompt.', primary CTAs, the New chip, indicator dots, the Popular badge, stat unit marks, the full CTA band, and ::selection background with white text). Hairlines are the system: light hairline rgba(10,10,10,0.12) on white, dark hairline rgba(255,255,255,0.14) on the black panels, applied as top/bottom/left/right 1px borders to draw every cell. Secondary surface is #fafafa (artboard well) and #111 (mini variant tiles inside the dark split). Text uses graded ink opacity: body ink/70, muted ink/55-60, micro ink/35-45; on dark panels paper/55-80. Typography: Inter only (Google Fonts, weights 300-900), font-extrabold/900 for all display. Tracking c …

## 5. Layout

A max-w-[1240px] container with px-6, and a reusable 12-column grid (grid-template-columns: repeat(12,1fr)) that every section snaps to. Sections are separated and bounded by 1px hairlines (hair-t/b/l/r) so the page reads as one continuous ledger of cells. The hero, feature grid, dark split, stats, pricing and footer all reuse the same column math and hairline cells. Responsive: the 12-col layout collapses to col-span-12 stacks on mobile, feature grid goes 1->2->3 columns, footer link columns go 4-up to 2-up, hero CTAs and sub-copy reflow under the headline.

## 6. Components

- **Hairline 12-column grid system** — The defining device: a reusable .grid12 (12 equal columns) plus .hair-t/b/l/r and .hd-t/b/l/r utilities that draw 1px borders (rgba(10,10,10,0.12) on white, rgba(255,255,255,0.14) on black). Every section, card, stat, tier, logo and footer column is a bounded cell, so the structural grid itself is the visual style. Faint mark-grid (28px square line texture) sits behind the hero and inside the mock artboards.
- **Square logo mark** — A 24px solid ink square containing a centered 10px signal-red square, paired with the 'Gridwright' wordmark in extrabold tt-tight. Reused identically in the nav and the footer.
- **Embedded canvas / app mock** — An in-page recreation of the product canvas: a toolbar (file label, zoom %, square icon buttons, a 'Generating' status pill with a red dot), a left Prompt rail with a quoted prompt and an A/B/C variants list (active = red dot), and a right #fafafa artboard holding a hairline wireframe of a landing page (opacity bars + one red block + mark-grid texture).
- **Hover-invert feature cells** — Each of the 6 feature cells flips from black-on-white to white-on-black on hover (group hover:bg-ink hover:text-paper), with the red icon staying red and the muted body text easing to paper/60. Each carries a red lucide icon and a mono index number (01-06).
- **Variant mini-artboard grid** — On the dark split, a 6-tile grid of #111 aspect-[3/4] cards (A grid, B cards, C stack, D hero, E docs, F price) on a 1px paper/12 hairline gap-grid, each abstractly rendering a layout from paper-opacity bars, hairline mini-cells and signal-red highlight blocks/dots marking the selected option.
- **Inverted Pro pricing card** — The middle of three tier columns is the only inverted card: bg-ink text-paper with a red 'Popular' badge pinned to the top-right corner, a red 'Pro' eyebrow, red check bullets, and a solid red 'Start Pro' CTA that inverts to paper-on-ink on hover. The outer Solo/Team cards stay white with ink checks and hairline-outlined buttons.
- **Segmented Annual/Monthly toggle** — A hairline-bounded inline segmented control where the active segment ('Annual') is a solid ink fill with paper text and the inactive segment ('Monthly') is ink/50, no rounding, matching the square Swiss aesthetic.

## 7. Motion

REVIEW —
- Black-on-white that flips to white-on-black on hover and in the Pro/workflow/CTA panels
- A Swiss-grid SaaS marketing homepage: stark white paper, near-black ink, one signal-red accent, an oversized two-line hero, an embedded prompt-to-canvas product mock, a hover-invert feature grid, a dark variant-tile workflow split, a 3-tier pricing block with an inverted Pro card, and a hairline-celled mega footer

## 8. Voice & Brand

A Swiss-grid SaaS marketing homepage: stark white paper, near-black ink, one signal-red accent, an oversized two-line hero, an embedded prompt-to-canvas product mock, a hover-invert feature grid, a dark variant-tile workflow split, a 3-tier pricing block with an inverted Pro card, and a hairline-celled mega footer.

## 9. Anti-patterns

Strict three-token palette: ink #0a0a0a, paper #ffffff, signal #ff3b30 only. Light hairline rgba(10,10,10,0.12), dark-panel hairline rgba(255,255,255,0.14); secondary surfaces #fafafa and #111 inside the dark split. Inter (300-900) is the only typeface; tt-tight = -0.045em on giant display, tt-wide = 0.22em uppercase on micro-labels, mono register + tabular-nums for metadata/stats/prices. NO gradients, NO drop shadows, NO border-radius anywhere except the tiny rounded-full indicator dots. The visible 12-column hairline grid must remain the dominant visual idea (it is the brand). Restrict red to true accents (accent word, primary CTAs, dots, Popular badge, CTA band, ::selection); never let it become a second body color. Keep it fully responsive: 12-col stacks to col-span-12, feature grid 1->2->3, footer 4->2 columns, hero CTAs and sub-copy reflow. No em-dashes in any copy.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
