# Design System — Forge — Launch Waitlist (dark, warm-ember)

> Category: Waitlist & Coming Soon  ·  Industry: SaaS
> Auto-scaffolded from prompt [`forge-launch-waitlist-dark-warm-ember`](../../prompts/forge-launch-waitlist-dark-warm-ember/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Dark warm-ember minimal launch page. Near-black ink base (#0a0a0f) with warm off-white text (#f4f3ef), one hot coral accent (#ff5a4d) used for the logo mark, ping dot, emphasis word, feature numerals/icons, focus ring and the primary CTA. Space Grotesk for all display headings (weights 600-700, tight -0.03em tracking) and Inter for body/UI (slightly negative -0.01em letter-spacing, antialiased). Mood: confident, fast, indie-founder. Atmosphere comes from large blurred coral/amber radial 'streak' glows behind the hero, a subtle white-dot grain overlay, glassmorphism (blurred translucent dark panels with hairline white borders) on the nav pill and waitlist card, fully-rounded pill controls, and a soft coral box-shadow glow on the brand mark and CTA. Headlines use a white-to-grey vertical gradient text clip.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#0a0a0f`
- `#f4f3ef`
- `#ff5a4d`
- `#ff8c3c`
- `#ffaa5a`
- `#ffffff`
- `#b9b8b3`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design in a dark, warm-ember, minimal startup-launch style. Palette: near-black ink base #0a0a0f, warm off-white text #f4f3ef, a single hot coral accent #ff5a4d (with warmer amber #ff8c3c / #ffaa5a only inside the ambient glows). Headings use Space Grotesk (weights 600-700, tracking -0.03em, leading ~0.98); body and UI use Inter (weights 400-600, letter-spacing -0.01em, -webkit-font-smoothing antialiased). Use glassmorphism for floating panels: linear-gradient dark fill (rgba(22,22,28,0.92)->rgba(13,13,18,0.92)), backdrop-blur ~16px, 1px rgba(255,255,255,0.07) border; the nav pill uses rgba(20,20,26,0.7) + blur 14px. Behind the hero place 3 large blurred (filter: blur(90px)) coral/amber radial 'streak' ellipses at ~0.55 opacity, plus a faint white radial-dot grain (rgba(255,255,255,0.025) 1px dots on a 3px grid). All buttons, the badge, the input shell and social icons are fully-rounded  …

## 5. Layout

Single-column, centered, long-scroll launch page in a max-w-6xl (72rem) container with px-5 / sm:px-8 gutters. Top-down order: a floating sticky glass pill nav, a centered hero (badge -> gradient headline -> one-line statement -> glass waitlist card -> social icon row) over blurred warm-ember glows + grain, an uppercase 'backed by' logo row, an editorial feature spread (12-col grid: a sticky 4-col title column + an offset, staggered 3-item numbered feature list), and a quiet split footer. Responsive: nav links hide below md, the waitlist form stacks vertically below sm, the feature grid collapses from 12 cols to a single stacked column on mobile and the second feature row loses its sm:pl-10 offset.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

Dark, warm-ember startup launch / waitlist landing page: near-black ink base with a single hot coral accent, Space Grotesk display + Inter body, blurred coral/amber ambient glows, a floating glass pill nav, a centered gradient headline, a glassmorphic email-capture waitlist card, a 'backed by' logo row, and a sticky-titled editorial 3-step feature spread.

## 9. Anti-patterns

Fonts loaded from Google Fonts: Space Grotesk (weights 400-700, display) and Inter (weights 400-600, body/UI). Styled with Tailwind via CDN using a custom theme (colors ink #0a0a0f and coral #ff5a4d; fontFamily display = Space Grotesk, sans = Inter); icons via the Iconify iconify-icon web component (Phosphor 'ph:*' set). Body background #0a0a0f, text #f4f3ef, html scroll-behavior smooth. The mood must stay dark, warm and ember-toned (coral/amber on near-black), never cold blue, purple or neon. Copy and brand 'Forge' are placeholders; the transferable value is the dark warm-ember launch/waitlist STYLE + the centered-hero + glass-card + editorial-feature LAYOUT.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
