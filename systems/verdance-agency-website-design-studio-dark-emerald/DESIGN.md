# Design System — Verdance — Agency Website Design Studio (Dark Emerald)

> Category: Portfolios  ·  Industry: Agency & Studio
> Auto-scaffolded from prompt [`verdance-agency-website-design-studio-dark-emerald`](../../prompts/verdance-agency-website-design-studio-dark-emerald/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Premium, calm, editorial dark mode in a deep emerald 'forest' palette with a brass metallic accent. The page is built from just two near-black green surfaces (forest #0d1f17 as the warmer base and forestDeep #0a1711 as the deeper alternating band) separated by 1px brass hairlines (rgba(201,162,39,0.32)) rather than by hard color blocks. Text is cream #f1ede3 for primary and a soft muted creamDim #b8b3a6 for secondary/eyebrows. There are two accents working together: a green pair (emerald #1f6f4f and the lighter emeraldSoft #2c8a63) used for glows, washes, the script-italic headline accents, and service icons; and a single brass/gold #c9a227 metallic used for ALL hairlines, the bracketed uppercase section labels, award diamonds, primary pill buttons, and link underlines. The signature contrast is typographic: a tight, heavy Inter display face (font-weight 700, letter-spacing -0.045em, line-height 0.92) for the GIANT uppercase headlines, set against an italic Fraunces serif ('script') used for small lyrical accents ('that win', 'considered', 'projects', 'in mind?') and for editorial stat numbers and pull-quotes. Atmosphere comes from craft, not noise: a faint fractal-noise grain overlay (opacity 0.05) on the hero and CTA, large soft emerald radial blur glows, photos pushed into the palette with a desaturate+sepia 'work-img' filter plus an emerald multiply 'tint', a centered brass-line gradient hairline (transparent -> brass -> transparent), and an infinite CSS marquee. Restrained, high-craft, Awwwards-studio energy.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#0d1f17`
- `#0a1711`
- `#f1ede3`
- `#b8b3a6`
- `#1f6f4f`
- `#2c8a63`
- `#c9a227`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Dark-emerald editorial design-studio / agency website with a single brass metallic accent. Exact palette via tailwind.config custom colors: forest #0d1f17 (warmer base surface + body bg), forestDeep #0a1711 (deeper alternating band / footer / marquee), emerald #1f6f4f and emeraldSoft #2c8a63 (green accent pair for glows/washes/script accents/service icons), cream #f1ede3 (primary text), creamDim #b8b3a6 (secondary text + uppercase eyebrows), brass #c9a227 (the ONE metallic accent: all hairlines, bracketed labels, award diamonds, primary buttons, link underlines). Body is bg-forest text-cream font-sans antialiased with selection:bg-emerald selection:text-cream. Two font families: sans = Inter (system-ui fallback), serif = Fraunces (Georgia fallback). Define .display { font-family: Inter; font-weight: 700; letter-spacing: -0.045em; line-height: 0.92 } for the giant uppercase headlines, and …

## 5. Layout

A single-column, vertically stacked, frameless responsive marketing page that alternates between the two forest surfaces. Almost every section centers inside mx-auto max-w-[1240px] with px-6 -> lg:px-10 padding. Order top to bottom: a fixed glassy nav; a hero (a small meta row, a giant two-line display headline with an italic script accent, a 2-column studio-statement + scroll-cue row, then a full-bleed feature photo capped by a brass hairline with a script caption); an infinite-scroll trust marquee of award names on the deeper surface; a serif studio statement section (a 3/9 label + paragraph split, with a 4-up stat grid built from 1px brass gridlines); an asymmetric work grid (a tall col-span row + two square cards in a 2-col grid, then a full-width wide editorial card) with bottom-gradient captions; a thin numbered services list (4 hairline-divided rows on a 12-col grid, no cards); a recognition strip (a 3-up award-card grid built from brass gridlines + a centered wrapping press-logo row) on the deeper surface; a centered closing CTA over a grain wash with two pill CTAs + a social-icon row; and a dark 4-column footer with a hairline divider and a bottom legal row. Reflow: the hero statement row is lg:grid-cols-12 (paragraph col-span-6 + right-aligned scroll cue col-span-6) -> stacked; the studio split is lg:grid-cols-12 (3/9) and its stat grid grid-cols-2 -> md:grid-cols-4; the work grid is md:grid-cols-2 with the first card md:row-span-2 (tall) and the wide card full-width below; the services rows are grid-cols-12 with the description hidden below lg; the recognition cards are md:grid-cols-3; the footer is md:grid-cols-12 (5 / 3-at-7 / 3); the nav links + the desktop CTA hide below md and swap to a brass-bordered hamburger that opens a full-width mobile menu panel; everything collapses to one column on mobile.

## 6. Components

- **Giant display headline with italic serif script accent** — The brand signature: a huge, tight, uppercase Inter display headline (AGENCY / WEBSITES) with a small italic Fraunces serif accent in emerald-soft green ('that win') tucked at the baseline, and the same display-vs-script pairing reused for every section H2 ('Recent projects', 'Services, end to end', 'Have a project in mind?').
- **Brass-hairline grid system + brass-line divider** — Instead of color blocks, the page is structured by a single brass metallic at low opacity: hairline section borders, the stat/award grids built as gap-px on a brass/20 base, and a centered transparent->brass->transparent gradient rule.
- **Palette-tinted work photography (.work-img + .tint)** — All portfolio imagery is pushed into the emerald palette so photos never break the dark-green mood: a desaturate + sepia + dim filter that warms on hover, plus an emerald multiply overlay, with extra forest floors on the text-bearing wide card so captions stay legible.
- **Infinite award marquee** — A seamless horizontally-scrolling strip of award/press names separated by brass diamonds, sitting on the deeper forestDeep band as a quiet credibility bar.
- **Numbered hairline services list with sliding brass arrow** — A thin, card-less services list where each discipline is a full-width row (index + icon + title + description + arrow) divided by brass hairlines, with a green wash and a sliding brass arrow on hover.

## 7. Motion

REVIEW —
- 12); transition transform
- work-card:hover, plus a
- nav-link::after brass underline that grows from width 0 to 100% on hover
- Honor prefers-reduced-motion (disable marquee + smooth scroll)

## 8. Voice & Brand

A dark-emerald design-studio / agency website with a single brass metallic accent: two forest-green surfaces (#0d1f17 / #0a1711), cream #f1ede3 text, an emerald/emeraldSoft green pair, and brass #c9a227 for all hairlines, bracketed labels, award diamonds and primary pills. A fixed glass nav over a hero whose giant tight Inter display headline (AGENCY / WEBSITES) carries an italic Fraunces serif accent (that win), a full-bleed palette-tinted feature photo, an infinite award marquee, a serif studio statement with a brass-gridline stat grid, an asymmetric work grid, a thin numbered services list, a recognition strip, a grain CTA, and a 4-column footer. High-craft editorial Awwwards-studio energy.

## 9. Anti-patterns

Frameless, fully responsive editorial design-studio / agency website (no browser chrome / no device frame): every section centers in mx-auto max-w-[1240px] with px-6 -> lg:px-10 and alternates between the two forest surfaces (forest #0d1f17 and forestDeep #0a1711). Reflow: the hero statement row is lg:grid-cols-12 (paragraph col-span-6 + scroll cue col-span-6); the studio split is lg:grid-cols-12 (3/9) with a grid-cols-2 -> md:grid-cols-4 stat grid; the work grid is md:grid-cols-2 with the first card md:row-span-2 (tall) and a full-width wide editorial card below; services are grid-cols-12 rows with the description hidden below lg; recognition is md:grid-cols-3; the footer is md:grid-cols-12 (5 / 3-at-7 / 3); below md the nav links + desktop CTA hide and a brass hamburger opens a full-width backdrop-blur mobile menu (JS toggles .hidden, swaps ph:list/ph:x, closes on link/Escape/>=768px); everything collapses to one column on mobile. Built with Tailwind via CDN plus a small tailwind.config registering the custom colors (forest #0d1f17, forestDeep #0a1711, emerald #1f6f4f, emeraldSoft #2c8a63, cream #f1ede3, creamDim #b8b3a6, brass #c9a227) and two font families (sans: Inter, serif: Fraunces). Google Fonts loads Inter 400-700 and Fraunces italic (opsz 9..144, 400;500); icons are Iconify Phosphor (ph:) glyphs. All copy and the 'Verdance' brand are placeholders meant to be swapped: the transferable value is (1) the dark-emerald two-surface palette with a SINGLE brass metallic accent and a cream/creamDim text scale, (2) the Inter-display-vs-italic-Fraunces-script typographic signature (giant tight uppercase headline + lyrical serif accent words), and (3) the high-craft editorial agency LAYOUT (glass nav -> giant-headline hero with full-bleed tinted feature photo -> award marquee -> serif studio statement with a brass-gridline stat grid -> asymmetric work grid with palette-tinted photography -> thin numbered services list -> recognition cards + press row -> grain CTA -> 4-column footer), NOT the specific studio. Strictly keep the palette: emerald greens + a single brass gold on deep forest; no other accent hue.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
