# Design System — Electric-Lime Single-Plan SaaS Pricing

> Category: Pricing Pages  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`electric-lime-single-plan-saas-pricing`](../../prompts/electric-lime-single-plan-saas-pricing/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

High-contrast editorial dark-frame aesthetic: a near-black charcoal page background wraps a warm off-white 'paper' panel (subtle dot-grain texture), with one electric lime accent and a soft sky-blue secondary. Big tight-tracked Space Grotesk display type does the heavy lifting; mono labels in caps with wide letter-spacing add a technical/zine feel. Generous whitespace, fully rounded corners (pills + 28px cards), soft long-throw shadows, and a lime blur glow behind the price card.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#0a0a0b`
- `#f4f3ef`
- `#c8f04a`
- `#bfe0ff`
- `#ffffff`

## 3. Typography

- `Space Grotesk`
- `Instrument Sans`
- `JetBrains Mono`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a charcoal near-black page background (#0a0a0b, the 'ink' color) that frames an inner warm off-white 'paper' panel (#f4f3ef) with rounded-[28px] corners and a faint radial dot-grain texture overlay. Accent everything with one electric lime (#c8f04a) for CTAs, badges, the logo mark glyph, and a soft blurred glow; use a pale sky-blue (#bfe0ff) as the secondary surface for the features card. Text is the ink color at varying opacities (full ink for headings, ink/60 for body, ink/45 for mono meta). Cards and surfaces are pure white (#ffffff) sitting on the paper. Typography: 'Space Grotesk' (700 weight, tracking-[-0.04em], leading-[0.92]) for huge display headlines and the price numeral; 'Instrument Sans' for body copy; 'JetBrains Mono' for small UPPERCASE labels with wide letter-spacing (tracking 0.12em-0.18em). Pills and badges are fully rounded; cards use rounded-[28px] with soft long- …

## 5. Layout

A frameless, responsive single-page pricing layout living inside a rounded charcoal 'browser shell'. Top to bottom: a sticky floating pill nav, a centered hero headline, the pricing centerpiece (a two-card offset composition: a tall white price card with billing toggle + a tilted sky-blue feature card overlapping behind it), a 3-item FAQ accordion, and a slim footer. It is fully responsive: the two pricing cards sit side-by-side on desktop and reflow/stack to a single column on mobile (the tilt straightens out), and the nav stays sticky.

## 6. Components

- **Billing period toggle** — A pill switch that flips the single plan between Quarterly and Annual, animating a knob and live-swapping the price, terms line, label emphasis, and showing a lime '-25%' savings tag on the Annual side.
- **Offset / tilted card pairing** — The signature composition: a white price card layered over a tilted sky-blue feature card so they overlap into one object, then flatten and stack on mobile.
- **Pinned ribbon badge** — A lime mono-caps pill badge pinned to the top edge of the price card to flag the single-plan offer.
- **Lime glow halo** — A soft blurred lime ellipse behind the price card that makes the centerpiece glow off the warm paper.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A bold editorial single-plan pricing page with a giant toggling price card, a tilted sky-blue feature card, and one electric-lime accent on warm paper inside a charcoal frame.

## 9. Anti-patterns

This is a FRAMELESS, fully RESPONSIVE single web page (not a fixed-size artboard): the rounded charcoal shell, sticky pill nav, and clamp()-based type all scale with the viewport, and the pricing/feature cards reflow from a side-by-side offset pair (3->2->1 effective columns across the page's grids) down to a single stacked column on mobile, where the blue card's tilt straightens to 0deg. It is a SINGLE-PLAN pricing model (one product, billing-period toggle only), so there is no multi-tier comparison table or per-tier columns. The whole vibe depends on three moves: the warm-paper-inside-charcoal frame, the one electric-lime accent against muted ink text, and the offset tilted two-card composition. Icons use the Phosphor (ph:) set via Iconify; fonts are Space Grotesk / Instrument Sans / JetBrains Mono.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
