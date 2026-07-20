# Design System — Pop Art Landing Page (Comic Halftone Product Site, Yellow + Red)

> Category: Landing Pages  ·  Industry: SaaS
> Auto-scaffolded from prompt [`pop-art-landing-page-comic-halftone-product-site-yellow-red`](../../prompts/pop-art-landing-page-comic-halftone-product-site-yellow-red/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

1960s pop art / comic print applied as a disciplined web style. A saturated sun-yellow canvas (#ffc900) with near-black ink (#0f0d0a), signal red (#dc341e) and process blue (#1e40c9) accents, white panels and a warm newsprint (#f6f1e6) alternating band. Everything is drawn with 3px ink outlines and HARD zero-blur offset shadows (6px 6px 0), never soft shadows or gradients. Ben-day halftone dot fields (CSS radial-gradient at 8px and 16px screen scales) texture the hero, the logo strip, the changelog masthead and the CTA band like real print screens. Type is Archivo Black for display (poster-grade, no novelty comic fonts) and Inter for UI/body, with hierarchy from size. Comic motifs are structural, not stickers: numbered panel corner chips, a rotated SVG starburst badge, speech-bubble testimonials with real tails, and a red marker underline in the headline. Whitespace inside panels stays generous, so the page reads loud but never cluttered.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#ffc900`
- `#0f0d0a`
- `#dc341e`
- `#1e40c9`
- `#f6f1e6`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a saturated sun-yellow page canvas (#ffc900) with near-black ink (#0f0d0a), signal red (#dc341e), process blue (#1e40c9), white panels, and a warm newsprint (#f6f1e6) alternating band. Draw every card, chip and button with a 3px solid ink border and a HARD offset shadow (box-shadow: 6px 6px 0 ink, zero blur); never use soft shadows, gradients, or any purple. Add ben-day halftone dot fields with CSS radial-gradient (circle, color 1.5-2px, transparent) at 8px and 16px background-size, in red, ink and white, as backdrop screens on the hero corner, band edges and mock mastheads. Set display type in Archivo Black only (all-caps, tight tracking, hero at clamp(44px, 8vw, 96px)) and body/UI in Inter 400/600/800; do not use novelty comic fonts. Express the comic register through structure: rotated numbered corner chips on panels, a rotated 16-point SVG starburst badge, ink-outlined speech bub …

## 5. Layout

A vertical scroll of eight full-width bands with a deliberate background rhythm (yellow, newsprint, white, newsprint, yellow, ink, blue, newsprint): sticky pill-nav top bar; centered hero with dot field, eyebrow chip, display headline + starburst, subhead, CTA pair, microline; logo strip between rules; three-panel how-it-works grid; two-column product preview (copy + checklist beside a browser-chrome changelog mock); three-column speech-bubble testimonial band; three-column stat band; centered CTA band; four-column footer. All grids collapse to one column at mobile with the type clamped down; zero horizontal overflow at 390px and 1440px.

## 6. Components

- **Ben-day halftone dot fields** — Print-style dot screens as pure-CSS backdrops at varied scales.
- **Hard-shadow comic panel with numbered corner chip** — The how-it-works cards drawn as numbered comic frames.
- **Speech-bubble testimonial with true tail** — Quote cards that read as comic speech bubbles, not styled rectangles.
- **Rotated SVG starburst NEW! badge** — The classic pop-art price-sticker burst, anchored to the headline.
- **Red marker underline** — A thick hand-drawn-feeling stroke under the key headline word.
- **Browser-chrome changelog mock** — A believable product preview inside a comic-outlined browser frame.
- **Press-down interactive states** — Buttons that physically press into their hard shadows.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A bold pop art landing page for a SaaS product, done as a comic-print website: ben-day halftone dot fields, thick ink outlines with hard offset shadows, a rotated NEW! starburst badge, numbered comic panels for the how-it-works section, and speech-bubble testimonials. A sun-yellow canvas with signal-red and process-blue accents, Archivo Black display type and Inter body. The full landing skeleton is here: pill nav, oversized hero with CTA pair, logo strip, three feature panels, a browser-mock changelog preview, testimonials, a stat band, a blue closing CTA and footer. Copy it for any product launch site, developer tool, or brand that wants loud retro-print personality without losing conversion structure.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
