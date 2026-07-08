# Design System — Electric Dark Usage-Based Pricing Calculator

> Category: Pricing Pages  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`electric-dark-usage-based-pricing-calculator-20e556`](../../prompts/electric-dark-usage-based-pricing-calculator-20e556/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Electric dark dev-tool aesthetic: deep ink/near-black backgrounds with a subtle white engineering grid and dual radial glows (violet iris + acid lime), high-contrast white headings in a geometric display face, lime as the single high-energy accent, and JetBrains Mono for all numbers/prices to read like a console. Cards are large-radius panels with hairline borders and deep, soft drop shadows.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#0B0C12`
- `#11131C`
- `#161927`
- `#232739`
- `#8A90A6`
- `#B6BBD0`
- `#FFFFFF`
- `#C6F24E`
- `#7C6CFF`
- `#5B4BE0`

## 3. Typography

- `Space Grotesk`
- `Inter`
- `JetBrains Mono`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a dark, high-contrast 'electric dev-tool' palette. Exact colors: page/base background ink #0B0C12; panel surface #11131C; card surface #161927 (and translucent #161927 at ~40% for secondary cards); hairline borders #232739 (line); muted text #8A90A6 (mute); soft body text #B6BBD0 (soft); pure #FFFFFF for headings; primary accent lime #C6F24E (CTAs, slider thumb/track-fill, highlights, check icons); secondary accent iris violet #7C6CFF with a darker #5B4BE0, used in low-opacity gradient washes and active table-row tints. Selection highlight = lime background with ink text. Background texture: a faint white engineering grid (linear-gradient lines at ~3.5% white, 56px x 56px cells) plus two soft radial glows up top — a violet glow (~rgba(124,108,255,0.22)) centered and a lime glow (~rgba(198,242,78,0.10)) upper-right. Fonts: display/headings 'Space Grotesk' (weights 600-700, tight track …

## 5. Layout

Frameless, fully responsive web page on a max-width 1200px centered container. Top to bottom: sticky translucent nav, a centered hero, the headline interactive cost calculator (3-column inner grid that collapses on mobile), a trust line, a 3-up plan comparison card row (reflows 3->2->1 columns), a centered FAQ accordion, and a slim footer. Sticky nav stays pinned; cards reflow responsively.

## 6. Components

- **Usage cost calculator (slider-driven pricing estimator)** — The defining element: an interactive estimator where a range slider sets monthly generation volume and the page live-computes included quota vs tiered pay-as-you-go overage, updating a big readout, the highlighted rate-table band, and the sticky estimate card + breakdown.
- **Custom lime range slider** — A restyled native range input: thin pill track that fills lime up to the thumb, with a large lime circular thumb ringed in ink and a lime glow.
- **Segmented tier toggle + annual switch** — Two compact controls in the calculator header: a Studio|Scale segmented button group and a Monthly/Annual pill toggle with a sliding lime knob and a '-20%' chip.
- **Live rate table with active-band highlight** — A pay-as-you-go price ladder where the row matching the current slider volume is tinted and tagged.
- **Highlighted 'Most popular' plan card** — The middle plan card visually elevated with a lime-tinted border, iris gradient, glow shadow, and a ribbon.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

An electric dark dev-tool pricing page built around an interactive slider calculator that live-computes included quota plus tiered pay-as-you-go overage, with a lime accent, a highlighted plan card row, and an FAQ accordion.

## 9. Anti-patterns

Frameless, fully responsive web page (not an app screen): single centered max-width 1200px container, sticky blurred nav, and grids that reflow (calculator inner grid 200px/1fr/320px -> single column with the metric rail becoming a horizontal scroll; plan cards 3 -> 2 -> 1 columns). Single high-energy accent discipline: lime #C6F24E carries all CTAs/active states/numbers-emphasis, iris #7C6CFF is reserved for low-opacity gradient washes and the active table-row tint. ALL numerals and prices use JetBrains Mono for the console feel; headings use Space Grotesk, body uses Inter. Built with Tailwind (CDN config maps the named colors), Phosphor icons via Iconify, and a small vanilla-JS controller that wires the slider, tier toggle, and annual switch to live price math. No em-dashes in copy.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
