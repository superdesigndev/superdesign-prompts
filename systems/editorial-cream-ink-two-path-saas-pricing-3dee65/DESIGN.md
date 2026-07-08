# Design System — Editorial Cream + Ink Two-Path SaaS Pricing

> Category: Pricing Pages  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`editorial-cream-ink-two-path-saas-pricing-3dee65`](../../prompts/editorial-cream-ink-two-path-saas-pricing-3dee65/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Warm editorial-meets-dev-tool aesthetic: an off-white cream canvas, a tall serif display headline mixed with a clean grotesque body, an electric cobalt-blue accent for actions/highlights, near-black 'ink' surfaces for the premium Enterprise panel, and a muted gold reserved exclusively for Enterprise feature checks. Soft 2xl-rounded white cards on the cream, hairline beige borders, and a single deep drop-shadow on the popular plan to lift it off the page.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#f6f4ef`
- `#ffffff`
- `#e7e3da`
- `#101418`
- `#1b2127`
- `#2a323b`
- `#5a6671`
- `#7c8893`
- `#eef3ff`
- `#dbe5ff`
- `#3858f6`
- `#2c46d6`
- `#2438ad`
- `#c8a45a`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a warm cream/paper background (#f6f4ef) with pure-white cards (#ffffff) and hairline borders in a beige line color (#e7e3da). Text uses an 'ink' ramp: near-black #101418 for headings, #1b2127 for the dark Enterprise panel, body text #2a323b, muted text #5a6671, and faint labels #7c8893. The primary brand accent is electric cobalt blue with a ramp: #eef3ff (tint), #dbe5ff, #3858f6 (base), #2c46d6 (hover), #2438ad; use brand-50 chips, brand-500 fills/checks, brand-600 for the italic accent and links. Reserve a muted gold #c8a45a only for the Enterprise feature checkmarks. Typography: Fraunces (serif, 'display') for the H1, plan names, section H2s and the logo wordmark, weights 400-700 with a true italic for the colored accent word; Inter (sans, weights 400/450/500/600/700) for all body, nav, features, buttons, and prices. Apply tabular + lining numerals on price numbers. Surfaces are r …

## 5. Layout

A frameless, fully responsive web page (no browser chrome), max-width 7xl content column centered with px-6 gutters. Top is a sticky translucent nav; then a centered hero; then the pricing block built as a 12-column split (8 cols of self-serve cards beside a 4-col dark Enterprise panel) with a centered billing toggle above it; then a two-column FAQ section on a white band; then a minimal footer. Cards reflow responsively: the self-serve pair is 2-up on >=sm and stacks to 1; the 12-col split goes side-by-side on >=lg and stacks the Enterprise panel below on smaller screens. Overall the pricing grid behaves like a 3->2->1 column reflow as the viewport narrows, with the sticky nav persisting.

## 6. Components

- **Monthly/Annual billing toggle with live price swap** — A pill switch whose white knob slides with a cubic-bezier transition; flipping it recolors the active period label, retitles every card's 'billed annually/monthly' note, and live-swaps each price number between its monthly and annual value.
- **Highlighted 'Most popular' plan card** — The Pro card is visually elevated with a thick dark border, a deep soft shadow, and an overhanging pill badge so it reads as the recommended self-serve tier.
- **Dark Enterprise contact-sales panel** — A full-height near-black panel set apart from the light self-serve cards, using a paper-colored CTA and gold feature checks to signal premium, contact-sales tier.
- **Feature list rows with icon checks** — Consistent feature rows across all plans using small bold check icons, blue on light self-serve cards and gold on the dark Enterprise panel.

## 7. Motion

REVIEW —
- The primary brand accent is electric cobalt blue with a ramp: #eef3ff (tint), #dbe5ff, #3858f6 (base), #2c46d6 (hover), #2438ad; use brand-50 chips, brand-500 fills/checks, brand-600 for the italic accent and links

## 8. Voice & Brand

A warm editorial SaaS pricing page on a cream canvas: a serif headline with an electric-blue italic accent, two self-serve plan cards (one highlighted) beside a dark near-black Enterprise contact-sales panel with gold accents, plus a monthly/annual toggle.

## 9. Anti-patterns

Render as a FRAMELESS, fully responsive web page (no browser window chrome). The pricing layout is the hero of the page: a two-path 12-column split (8-col self-serve lane + 4-col dark Enterprise panel) that stacks vertically on smaller screens, with the self-serve cards reflowing 2->1. Treat the whole card grid as a 3->2->1 column reflow with a persistent sticky translucent nav. Icons are Phosphor (iconify ph:* set). The defining transferable moves to preserve: cream 'paper' canvas + white cards, Fraunces serif headline with one italic blue accent word, electric cobalt blue actions, a single highlighted plan (dark border + shadow + overhanging badge), and a near-black Enterprise panel with gold checks and a contact-sales CTA instead of a price. No em-dashes in copy; use a middot in the trust line.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
