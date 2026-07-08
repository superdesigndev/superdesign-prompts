# Design System — Editorial Image Lightbox

> Category: Blog & Editorial  ·  Industry: General
> Auto-scaffolded from prompt [`editorial-image-lightbox`](../../prompts/editorial-image-lightbox/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

A warm, editorial, magazine-grade aesthetic built to make a generated lightbox feel typeset rather than default. The mood splits into two registers: a bright cream editorial body (#faf6ef) for the marketing surfaces, and a near-black 'stage' for the lightbox itself so the photograph leads. Color is strictly disciplined: ink #1c1815 carries nearly all text and the dark CTA/footer surfaces, cream #faf6ef carries every light surface and all reversed text, coal #0c0a09 is the deepest near-black for the modal body and footer, and a single burgundy accent (#7b2d3b, deepening to #5e2029 on hover) is RESERVED for emphasis only (the brand period, eyebrow labels, the active filter pill, italic headline words, prev/next/close hover states, primary CTAs). The dark stage is a layered 'backdrop-vignette' (a radial coal gradient from rgba(12,10,9,0.55) at center to rgba(12,10,9,0.97) at the edges over #0c0a09) dusted with a faint 'grain' dot texture. Surfaces are translucent panels hairlined with ink/10-12 (light) or cream/10-15 (dark) borders, generous rounding (rounded-xl tiles, rounded-2xl cards + the modal, rounded-full pills + controls), and a deep modal shadow (0 50px 120px -30px rgba(0,0,0,0.85) plus a 1px white/5 ring). Type pairs Fraunces (a variable optical-size serif, opsz 120 on display headlines, with true italics for accent words) for headlines, counters and titles against Inter for body, labels and UI. Eyebrows are uppercase, widely letter-spaced (tracking 0.18-0.22em) in burgundy. Motion is restrained: cards lift -4px on hover, prev/next carets nudge on hover, and selection paints burgundy-on-cream. The whole point: burgundy is scarce so it reads as editorial emphasis, and the cream/coal split keeps the marketing legible while letting the photograph own the stage.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#faf6ef`
- `#1c1815`
- `#0c0a09`
- `#7b2d3b`
- `#5e2029`

## 3. Typography

- `Featured`
- `Aperture Series`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a warm editorial design system that splits between a bright cream body and a near-black photographic stage. EXACT palette tokens (Tailwind config): ink #1c1815, cream #faf6ef, burgundy #7b2d3b, burgundy-deep #5e2029, coal #0c0a09. Body background #faf6ef; default text ink #1c1815. Selection: background #7b2d3b, color #faf6ef. Discipline rule: ink carries nearly all text and the dark CTA + footer surfaces; cream carries every light surface and all reversed text; coal #0c0a09 is the modal body + footer; burgundy #7b2d3b is RESERVED for accents only (the brand '.', uppercase eyebrow labels, the active filter pill fill, the italic headline word 'composed', prev/next/close hover fills, primary CTAs, the location pin eyebrow, the 'Featured' tag), deepening to burgundy-deep #5e2029 on primary-button hover. Fonts via Google Fonts: Fraunces (ital + opsz 9..144 + wght 300..900, optical-sizing  …

## 5. Layout

A single vertically-scrolling editorial product page on a shared max-w-7xl mx-auto px-6 lg:px-10 container, with the image lightbox as a full-bleed dark 'stage' band roughly mid-page (the modal shown live, in context, not floated on a blank artboard). Order: (1) a sticky top-0 z-50 frosted cream nav (cream/85 + backdrop-blur-md, border-b border-ink/10); (2) a cream hero with a 12-column grid (left col-span-7: an eyebrow chip + a two-line Fraunces display headline with an italic burgundy accent word + a lead + two CTAs; right col-span-5: a translucent 'The numbers' stats card) and a soft burgundy blur orb top-right; (3) the full-bleed .backdrop-vignette + .grain 'preview' stage holding a section label row and the centered lightbox modal (with a faded 3-up gallery behind it and a keyboard-hint ticker beneath); (4) a cream library band with a header row + a 3-up card grid (one featured dark card + two light mini-mockup cards); (5) a white anatomy band with a 12-column grid pairing a copy column with a 2x2 hairlined cell grid; (6) a dark ink CTA band with a two-column headline + CTA pair and a burgundy blur orb; then a coal footer. It reflows cleanly to mobile: the hero, anatomy and CTA grids collapse to one column (lg:grid-cols-12 / lg:grid-cols-2 -> stacked), the library grid steps 1 -> 2 -> 3 (with the featured card spanning sm:col-span-2 lg:col-span-1), the nav center links + 'Sign in' hide (md:flex / sm:block) while the burgundy pill CTA persists, the modal control rail wraps (the filter pills become a full-width order-3 scrollable .filmstrip row while the close button stays pinned), the modal caption panel stacks (sm:flex-row -> column) and the 'Plate 03 / Aperture Series' label + footer rows hide/stack on small screens.

## 6. Components

- **** — 
- **** — 
- **** — 
- **** — 
- **** — 

## 7. Motion

REVIEW —
- Color is strictly disciplined: ink #1c1815 carries nearly all text and the dark CTA/footer surfaces, cream #faf6ef carries every light surface and all reversed text, coal #0c0a09 is the deepest near-black for the modal body and footer, and a single burgundy accent (#7b2d3b, deepening to #5e2029 on hover) is RESERVED for emphasis only (the brand period, eyebrow labels, the active filter pill, italic headline words, prev/next/close hover states, primary CTAs)
- Motion is restrained: cards lift -4px on hover, prev/next carets nudge on hover, and selection paints burgundy-on-cream
- ', uppercase eyebrow labels, the active filter pill fill, the italic headline word 'composed', prev/next/close hover fills, primary CTAs, the location pin eyebrow, the 'Featured' tag), deepening to burgundy-deep #5e2029 on primary-button hover
- Motion: a
- lift utility = transition transform

## 8. Voice & Brand

An editorial image lightbox modal as the live hero of a product page: a near-black coal (#0c0a09) figure with a top rail (serif 04/28 plate counter + 'Aperture Series' label, scrollable category filter pills, a circular close), a full-bleed photograph with circular glass prev/next carets and a bottom legibility gradient, and a cream (#faf6ef) caption panel (burgundy location eyebrow, a Fraunces headline, a description, Save / Copy-prompt actions), floated over a vignetted grain stage with a faded 3-up gallery echo behind and an 'Esc / arrows / 28 plates' keyboard ticker beneath. Around it: a frosted sticky cream nav, a hero with a stats card, a 3-up library grid, a four-cell anatomy band, a dark CTA band and a coal footer. Ink-on-cream editorial with a single reserved burgundy #7b2d3b accent; Fraunces + Inter, Phosphor icons.

## 9. Anti-patterns

Two Google Fonts: Fraunces (serif display — ital + opsz 9..144 + wght 300..900, optical-sizing auto; a .display utility forces font-variation-settings 'opsz' 120) for headlines, the plate counter and titles (with true italics for the accent word 'composed'), and Inter (wght 300..700, font-sans) for body, labels, UI and eyebrows. Icons are Phosphor via Iconify (ph:frame-corners-bold, ph:sparkle-fill, ph:arrow-down-right-bold, ph:images-square-duotone, ph:stack-duotone, ph:image-square-duotone, ph:x-bold, ph:caret-left-bold, ph:caret-right-bold, ph:map-pin-fill, ph:download-simple-bold, ph:copy-bold, ph:arrow-right-bold, ph:x, ph:text-aa-bold, ph:arrows-left-right-bold, ph:x-circle-bold, ph:arrow-up-right-bold, ph:x-logo-bold, ph:github-logo-bold). EXACT tokens (Tailwind config) — ink #1c1815, cream #faf6ef, burgundy #7b2d3b, burgundy-deep #5e2029, coal #0c0a09. THE CORE DISCIPLINE (the point of this item): the page splits into a bright cream editorial body and a near-black photographic stage so the lightbox's photograph always leads, and burgundy #7b2d3b is RESERVED for emphasis only — the brand '.', uppercase eyebrows, the active filter pill, the italic headline word, prev/next/close hover fills, primary CTAs, the location pin eyebrow and the 'Featured' tag — so it reads as editorial accent, never decoration. Radii: rounded-xl tiles, rounded-2xl cards + the modal figure, rounded-full pills + circular controls. Effects: the dark stage .backdrop-vignette (radial coal gradient 0.55 -> 0.97 over #0c0a09) + a .grain dot texture (radial-gradient white/0.04 1px dots at 3px); the modal shadow 0 50px 120px -30px rgba(0,0,0,0.85) + ring-1 ring-white/5; a bottom from-black/70 caption-legibility gradient on the image; a faded blurred 3-up gallery echo behind the modal; soft bg-burgundy blur-3xl orbs on the hero and CTA bands; a frosted sticky nav (cream/85 + backdrop-blur-md); .filmstrip rows hide their scrollbar. Motion: a .lift utility (transition transform .35s cubic-bezier(.2,.7,.2,1) + box-shadow, hover translateY(-4px)) on the library cards, prev/next carets nudge ±0.5 on group-hover, and ::selection paints burgundy-on-cream. Layout: a sticky top-0 z-50 frosted cream nav over a shared max-w-7xl mx-auto px-6 lg:px-10 container — a 12-col cream hero (copy + a stats card), a full-bleed dark .backdrop-vignette stage holding the lightbox modal (faded gallery echo behind + a keyboard-hint ticker below), a cream 3-up library grid (a featured dark card + two light mini-mockup cards), a white 12-col anatomy band (copy + a 2x2 hairlined cell grid), a dark ink CTA band, and a coal footer. Responsive reflow: the hero/anatomy/CTA grids collapse to one column, the library grid steps sm:grid-cols-2 lg:grid-cols-3 (the featured card sm:col-span-2 lg:col-span-1), the nav center links + 'Sign in' hide (md:flex / sm:block) while the burgundy pill persists, the modal control rail wraps (filter pills become a full-width order-3 scrollable .filmstrip while close stays pinned) and its caption panel stacks (sm:flex-row -> column), and the 'Plate 03' label hides on small screens. Accessibility intent: aria-label on the close + prev/next buttons, aria-hidden on the decorative gallery echo, and a from-black/70 gradient that keeps any over-image text legible.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
