# Design System — The Quote, Set in Burgundy

> Category: Blog & Editorial  ·  Industry: General
> Auto-scaffolded from prompt [`the-quote-set-in-burgundy`](../../prompts/the-quote-set-in-burgundy/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Warm, premium editorial / print-magazine aesthetic. A single cream paper background with near-black 'ink' text and one deep burgundy accent used for emphasis, the logo, the slide number, and italic key words inside the quote. Pairs a high-contrast Fraunces serif (the 'display' voice, used for the quote, logo wordmark, slide counter and name) with Inter for all small UI/labels. Identity comes from typography and restraint, not decoration: a faint two-spot paper grain, a giant translucent burgundy opening quote mark behind the text, hairline ink rules, and uppercase wide-tracked micro-labels. Soft, expensive shadow only on the portrait.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#faf6ef`
- `#1c1815`
- `#7b2d3b`

## 3. Typography

- `Fraunces`
- `Inter`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a warm cream paper background #faf6ef with a near-black 'ink' text color #1c1815 and a single deep burgundy accent #7b2d3b. Typography is the identity: load 'Fraunces' (an optical serif, weights 300-700) as the display family for the big quote, the logo wordmark, the slide counter and the attributed name, and 'Inter' (400/500/600) for every small label, nav link and button. Set the giant blockquote in Fraunces at a normal/400 weight, very tight leading (~1.08) and slightly negative tracking (-0.02em), and italicize one or two key words inside it in burgundy for emphasis. Keep the palette to just cream + ink + burgundy; express tints by opacity (e.g. text-ink/70 for nav, ink/45-55 for micro-labels, burgundy/8% for the ghost quote mark). Add a faint 'paper-grain' via two soft radial gradients (burgundy at ~5% top-left, ink at ~4% bottom-right). Use uppercase Inter micro-labels with ver …

## 5. Layout

A frameless, fully responsive single 'slide' that fills the viewport height (min-h calc(100vh - nav)) and vertically centers one testimonial. A sticky translucent nav sits on top. Inside a centered max-width column (~1180px): a top meta row (left = overlapping avatar stack + 'From the studio' eyebrow, right = big burgundy '01 / 03' counter), then the oversized serif pull-quote, then a portrait + vertical-rule + name/role byline, then a full-width hairline, then a footer control row (left = round prev/next arrow buttons, right = progress dots). A huge ghosted opening quotation mark is absolutely positioned behind the upper-left of the content. It reads as one slide of a testimonial carousel, not a list of cards.

## 6. Components

- **Ghosted oversized quotation mark** — A giant translucent serif opening-quote glyph behind the text that signals 'this is a quote' without a literal quote-card.
- **Slide counter (01 / 03)** — An editorial 'which slide am I on' index that doubles as a strong typographic accent.
- **Overlapping avatar trust cluster with +N pill** — A stacked group of reviewer photos ending in a burgundy '+9' chip to imply many voices behind this one quote.
- **Carousel chrome: prev/next arrows + progress dots** — Minimal slider controls that make the single quote feel like one of several, with motion affordances.
- **Animated burgundy underline nav link** — Nav links draw a thin burgundy underline from left to right on hover.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A magazine-style single-slide testimonial on a warm cream canvas: one oversized Fraunces serif pull-quote with burgundy italic emphasis, a ghosted giant quote mark, an avatar trust cluster, a portrait byline, and prev/next carousel chrome with progress dots.

## 9. Anti-patterns

Frameless, fully responsive single-slide web layout (no device chrome). It fills the viewport (min-h calc(100vh - 72px) with the content vertically centered. Responsive reflow: the quote scales fluidly (~2.05rem -> 3.6rem -> 4.4rem), the 'From the studio' eyebrow and 'Sign in' link hide below sm, nav links hide below md, the byline role line wraps and swaps its separator on mobile, and portrait/avatars shrink. Palette is strictly cream #faf6ef + ink #1c1815 + burgundy #7b2d3b, with tints expressed via opacity. Fonts: Fraunces (display/serif) for the quote, logo, counter and name; Inter for all UI/labels. Icons via Iconify lucide set (arrow-up-right, arrow-left, arrow-right). The avatar photos use pravatar placeholders and the copy/brand ('Praxis', 'Mara Delacroix', 'Northwind') is placeholder, swap for the user's real quote, person and company. The prev/next arrows + dots are presentational chrome unless wired to a real multi-slide carousel.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
