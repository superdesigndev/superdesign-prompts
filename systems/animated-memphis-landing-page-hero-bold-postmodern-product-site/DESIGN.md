# Design System — Animated Memphis Landing Page Hero (Bold Postmodern Product Site)

> Category: Animations & Backgrounds  ·  Industry: SaaS
> Auto-scaffolded from prompt [`animated-memphis-landing-page-hero-bold-postmodern-product-site`](../../prompts/animated-memphis-landing-page-hero-bold-postmodern-product-site/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Bold, playful MEMPHIS / postmodern product-landing aesthetic - loud, flat, and characterful, the opposite of a beige corporate dashboard. A warm CREAM #f5efe2 ground carries near-black #17140d ink and a flat, saturated Memphis palette: teal #12b3a4, coral #ff5b57, mustard #ffc531, violet #6b5be6, and a sky-blue #3aa0ff, each used as a solid fill (never a gradient). The defining move is the MEMPHIS GRAPHIC LANGUAGE scattered across the background: geometric CONFETTI shapes (triangles, quarter-arcs, half-circles, dotted circles, plus-signs), a black SQUIGGLE 'bacteria' line, a ZIGZAG, and a STRIPED / terrazzo pattern-filled circle, every one wearing a thick black outline. Depth comes from craft, not realism: every button, card, chip, and shape has a 3px BLACK OUTLINE and a flat HARD OFFSET SHADOW (box-shadow 8px 8px 0 #17140d on hero elements, 5px 5px 0 on smaller ones, collapsing on hover as the element nudges down) - no blur, no soft shadow, no gradient anywhere. Type is a two-face system: Bricolage Grotesque (700/800) does the big display headings and the wordmark with tight tracking; DM Sans (400/500/700) does body, labels, and UI. Hierarchy is aggressive (76px hero display vs 14-16px labels). Accent MARKER-HIGHLIGHT bars sit behind chosen headline words (a flat mustard or teal rectangle, slightly rotated). Motion is gentle and looping via CSS keyframes only (drift, spin, bob, sway on the background confetti) so the page feels alive but the visible frame is always legible. Flat vector + pattern only, no photography.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#f5efe2`
- `#17140d`
- `#12b3a4`
- `#ff5b57`
- `#ffc531`
- `#6b5be6`
- `#3aa0ff`

## 3. Typography

- `Start free`
- `Watch the demo`
- `Trusted by`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a bold, playful MEMPHIS / postmodern ANIMATED landing page HERO for a SaaS / product site on a single 1440-wide desktop viewport, on a warm CREAM #f5efe2 canvas with near-black #17140d ink. Use a flat, saturated Memphis palette of SOLID fills only (no gradients anywhere): teal #12b3a4, coral #ff5b57, mustard #ffc531, violet #6b5be6, sky #3aa0ff. Scatter the background with ANIMATED GEOMETRIC CONFETTI - a coral triangle, a teal quarter-arc, a mustard dotted circle, a violet plus-sign, a black squiggle 'bacteria' line, a mustard half-circle, a small teal dot, a sky zigzag, and a coral striped/terrazzo circle - each a thick-black-outlined inline SVG animated by CSS keyframes (gentle drift / spin / bob / sway, NO JS) so the page feels alive while the visible frame stays legible. Give EVERY button, card, chip, and shape a 3px BLACK OUTLINE and a flat HARD OFFSET SHADOW (box-shadow 8px  …

## 5. Layout

A vertical scroll on cream: (1) a minimal top nav - logo tile + wordmark left, four center links, a teal 'Start free' pill CTA right; (2) an asymmetric HERO grid (~1.05fr copy / .95fr product card): left column = a violet eyebrow pill, a 76px Bricolage headline with marker-highlight words, a lead paragraph, a dual CTA row, and an avatar trust row; right column = a tilted (-2deg) product-dashboard mockup card (browser chrome + sprint-velocity bar chart + checklist), with animated Memphis confetti shapes scattered across the whole hero background; (3) a full-bleed BLACK logo strip ('TRUSTED BY TEAMS AT' + five cream wordmarks); (4) a centered FEATURES section (violet eyebrow pill + two-line Bricolage heading) over a three-column feature-card row. On a narrow viewport the hero stacks to one column (product card below copy), the headline steps down to ~52px, the nav links collapse, and the feature grid becomes one column.

## 6. Components

- **Animated Memphis confetti shape** — The signature background motif: flat, black-outlined geometric shapes that drift and spin via CSS keyframes only.
- **Candy CTA pill with hard offset shadow** — The tactile button system - a solid fill on a thick black outline sitting on a flat offset shadow.
- **Marker-highlight headline word** — A flat colored bar behind a chosen headline word, like a highlighter swipe.
- **Tilted product dashboard mockup** — An in-page app screenshot that makes the hero read as a real product landing.
- **Outlined feature card with corner accent** — The reusable feature-row card unit.
- **Full-bleed black logo strip** — A social-proof band that breaks the cream with a hard black block.

## 7. Motion

REVIEW —
- Depth comes from craft, not realism: every button, card, chip, and shape has a 3px BLACK OUTLINE and a flat HARD OFFSET SHADOW (box-shadow 8px 8px 0 #17140d on hero elements, 5px 5px 0 on smaller ones, collapsing on hover as the element nudges down) - no blur, no soft shadow, no gradient anywhere
- Motion is gentle and looping via CSS keyframes only (drift, spin, bob, sway on the background confetti) so the page feels alive but the visible frame is always legible
- Give EVERY button, card, chip, and shape a 3px BLACK OUTLINE and a flat HARD OFFSET SHADOW (box-shadow 8px 8px 0 #17140d on hero elements, 5px 5px 0 on smaller ones, pressing in on hover) - never a blur or a soft shadow

## 8. Voice & Brand

A loud, playful ANIMATED landing page hero in the MEMPHIS / postmodern style for a bold SaaS or product site. A warm cream canvas is scattered with animated geometric confetti (squiggles, triangles, dotted circles, quarter-arcs, zigzags, a striped circle) that drift and spin via CSS keyframes, behind an asymmetric hero: a chunky bold-grotesk headline with marker-highlight underlines, a violet eyebrow pill, two candy-outlined CTAs (a coral "Start free" + a ghost "Watch the demo") with thick black outlines and hard offset shadows, an avatar trust row, and a tilted product-dashboard mockup (bar chart + checklist). Below: a black full-bleed "Trusted by" logo strip and a three-up feature-card row. Every shape has a thick black outline and a flat hard offset shadow, no gradients. Reusable for any bold, playful product / SaaS / app landing that wants postmodern personality.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
