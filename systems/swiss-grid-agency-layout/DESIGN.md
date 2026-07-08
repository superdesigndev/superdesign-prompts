# Design System — Swiss Grid Agency Layout

> Category: Portfolios  ·  Industry: Agency & Studio
> Auto-scaffolded from prompt [`swiss-grid-agency-layout`](../../prompts/swiss-grid-agency-layout/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

High-contrast Swiss / International Typographic Style: a pure paper-white page (#ffffff) with pure-black ink (#0a0a0a) and a single electric cobalt accent (#1f4fff), and nothing else. There is no decoration that has not earned its place: structure comes entirely from a strict 12-column grid, hairline rules, and the type itself. Two typefaces only: Inter (300-900) does all the display and body work with negative letter-spacing and tight leading (the giant headline runs leading-[0.84]); JetBrains Mono is reserved exclusively for the uppercase, 0.14em-tracked micro-labels (the 'label' class: 11px, uppercase) that index every section ('No. 01 / 06', column headers, eyebrows, nav items). Section breaks are 1px ink hairlines for quiet divisions and a 2px cobalt rule (.hairline-cobalt) for the primary ones. Cobalt is dosed sparingly: the headline's terminal period, the marquee's alternating labels, the work-row hover state, the inverted 4th service card, the contact-line hover, and the brand mark's square + dot. ::selection is cobalt-on-white. The whole thing reads like a printed editorial spread: disciplined, legible, engineered, zero gradients/shadows/rounded corners.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#ffffff`
- `#0a0a0a`
- `#1f4fff`
- `#fff`

## 3. Typography

- `JetBrains Mono`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Swiss / International-Typographic-Style agency site, pure monochrome + one electric cobalt. Exact palette via tailwind.config custom colors: ink #0a0a0a (text + hairlines), paper #ffffff (page bg), cobalt #1f4fff (the single accent). Body is bg-paper text-ink font-sans antialiased with -webkit-font-smoothing:antialiased and text-rendering:optimizeLegibility. The ONLY accent is cobalt #1f4fff: never introduce any other hue. Define a .label utility = font-family 'JetBrains Mono', monospace; font-size 11px; letter-spacing 0.14em; text-transform uppercase (used on every micro-label/eyebrow/nav item/column header). Hairlines: .hairline { border-color:#0a0a0a } for ink rules and .hairline-cobalt { border-color:#1f4fff } used as a border-t-2 for primary section breaks. Display type uses .display { font-feature-settings:'ss01' 1; letter-spacing:-0.04em; line-height:0.86 }. A strict grid utility  …

## 5. Layout

A single-column, vertically stacked, frameless responsive editorial agency page where every content section centers inside mx-auto max-w-[1320px] with px-6 -> md:px-10 padding and snaps to a strict 12-column grid (.grid-12 gap-4). Order top to bottom: a sticky paper nav with a bottom ink hairline; a hero (an 'index' meta row over a 2px cobalt rule + a discipline line, then a giant .display headline, then a sub-grid splitting a thesis statement from a 2x2 stat block); a full-bleed inverted (black bg / paper text) auto-scrolling marquee strip bordered top + bottom in ink; a numbered Selected-Work index list (a header row of mono column labels, then 06 hairline-divided rows on the 12-col grid); a 4-up services grid built from gap-px hairlines (the 4th card inverted to solid cobalt); a large studio statement section under a cobalt/ink rule; a contact section (a giant mailto .display line + a right-aligned Berlin address + social labels) opened by a 2px cobalt rule; and a 3-up hairline footer. Reflow: the nav is a 12-col grid (brand col-span-6 -> md:col-span-3, center links col-span-6 hidden below md, CTA col-span-6 -> md:col-span-3); hero meta rows reserve a md-only middle column; the headline scales by viewport (19vw -> 15.5vw -> 200px); the stat block is a 2-col grid; the work list hides its № index, year column, and discipline-inline layout below md (discipline drops under the title); the services grid goes grid-cols-1 -> md:grid-cols-2 -> lg:grid-cols-4; the contact + footer 12-col rows go right-aligned on md and stack/left-align on mobile. Everything collapses to one column on mobile and the center nav links hide below md.

## 6. Components

- **Strict 12-column grid system (.grid-12)** — The backbone of the whole page: a literal 12-column CSS grid that every section, every row, the nav, the work list, and the footer snap to, which is what makes it read as Swiss / International Typographic Style rather than a generic stacked landing page.
- **Mono micro-label index system (.label)** — Every section is indexed and captioned with uppercase JetBrains Mono micro-labels (No. 01 / 06, column headers, eyebrows, nav items, captions) that give the page its editorial, printed-spec-sheet character and carry almost all of the cobalt accenting.
- **Hairline + 2px-cobalt rule system** — Sections are divided not by colored blocks but by 1px ink hairlines for quiet breaks and a 2px cobalt rule for the primary ones, plus the services grid is literally constructed from gap-px hairlines, giving the page its quiet, engineered restraint.
- **Inverted auto-scroll marquee strip** — A full-bleed black band that inverts the page (paper text on ink) and continuously scrolls the studio's disciplines, breaking the white spread with a single dark rhythm element and a second dose of cobalt.
- **Indexed work list with hover-cobalt + nudging arrow** — The portfolio is a numbered, grid-aligned index list (not cards): each row spans the 12-col grid with a mono index, a large client title, discipline, and year, and on hover the title turns cobalt while a cobalt out-arrow slides right and fades in.
- **Inverted cobalt service card** — Within the otherwise paper-white 4-up services grid, the final card flips to solid cobalt with paper text, providing a single punch of color and a focal endpoint to the capability row.

## 7. Motion

REVIEW —
- Cobalt is dosed sparingly: the headline's terminal period, the marquee's alternating labels, the work-row hover state, the inverted 4th service card, the contact-line hover, and the brand mark's square + dot
- Work-row hover:
- work-row:hover
- work-row:hover
- ' display headline (Inter) with a 2x2 stat block, an inverted black auto-scroll marquee of disciplines, a numbered Selected-Work index list with hover-cobalt titles and a nudging out-arrow, a 4-up hairline services grid (4th card inverted to solid cobalt), a large studio statement, a giant mailto contact line, and a 3-up hairline footer

## 8. Voice & Brand

A Swiss / International-Typographic-Style agency homepage on a strict 12-column grid: pure black ink #0a0a0a on paper white #ffffff with one electric cobalt #1f4fff accent, a sticky paper nav with an ink hairline, an editorial index row over a 2px cobalt rule, a giant disciplined 'AGENCY SITES.' display headline (Inter) with a 2x2 stat block, an inverted black auto-scroll marquee of disciplines, a numbered Selected-Work index list with hover-cobalt titles and a nudging out-arrow, a 4-up hairline services grid (4th card inverted to solid cobalt), a large studio statement, a giant mailto contact line, and a 3-up hairline footer. JetBrains Mono micro-labels index every section.

## 9. Anti-patterns

Frameless, fully responsive Swiss / International-Typographic-Style agency homepage (no browser chrome, no device frame): every content section centers in mx-auto max-w-[1320px] with px-6 -> md:px-10 and snaps to a strict 12-column grid (.grid-12 gap-4); the nav and footer are 12-col rows; the hero scales its .display headline by viewport (19vw -> 15.5vw -> 200px); the work list hides its index/year columns and drops discipline under the title below md; the services grid is grid-cols-1 -> md:grid-cols-2 -> lg:grid-cols-4 built from gap-px hairlines; the contact and footer rows right-align on md and stack on mobile; the center nav links hide below md; the nav is sticky with bg-paper/95 backdrop-blur. Built with Tailwind via CDN plus a small tailwind.config registering the three custom colors (ink #0a0a0a, paper #ffffff, cobalt #1f4fff) and two font families (sans: Inter, mono: JetBrains Mono); Google Fonts loads Inter 400-900 + JetBrains Mono 400/500; icons are Iconify material-symbols glyphs (arrow-outward-rounded, grid-view-outline-rounded, web-asset, format-shapes-outline-rounded, bolt-rounded). Custom CSS provides .label (mono uppercase micro-label), .display (ss01 + tight tracking + 0.86 leading), .hairline / .hairline-cobalt rules, .grid-12, the marquee animation, and the work-row hover transitions; ::selection is cobalt-on-white. All copy and the 'Hervé Studio' brand are placeholders meant to be swapped: the transferable value is the Swiss aesthetic itself — a pure monochrome paper/ink palette with a SINGLE electric cobalt accent (#1f4fff, dosed onto the headline period, the 2px section rules, the marquee, work-row hover, the inverted 4th service card, and the contact-line hover), Inter for display+body with JetBrains Mono for every tracked uppercase label, hairline-only dividers, and a relentless 12-column grid that every row obeys — NOT the specific agency. Strictly no gradients, drop shadows, or rounded corners; structure is grid + hairlines + type only.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
