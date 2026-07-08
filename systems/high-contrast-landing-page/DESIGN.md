# Design System — High Contrast Landing Page

> Category: Landing Pages  ·  Industry: General
> Auto-scaffolded from prompt [`high-contrast-landing-page`](../../prompts/high-contrast-landing-page/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is defined by its Swiss minimalist roots: heavy use of 'Clash Display' for bold, oversized headlines and 'Satoshi' for clean, functional body text. Colors are strictly neutral (#f2f2f2 background, #111111 text) with a gradient of grays (#bfbfbf to #d9d9d9) used for depth-creating background layers. The aesthetic is devoid of traditional icons or illustrative fluff, relying instead on geometric shapes, sharp borders, and high-impact font pairing.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#f2f2f2`
- `#111111`
- `#bfbfbf`
- `#d9d9d9`
- `#b6b5b5`
- `#838282`

## 3. Typography

- `Clash Display`
- `Satoshi`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a high-contrast minimalist UI using a Swiss-style aesthetic. 
- **Palette**: Backgrounds in off-white (#f2f2f2), primary text in deep black (#111111), and secondary elements in muted grays (#b6b5b5, #838282).
- **Typography**: Headlines in 'Clash Display' (bold, weight 700), tracking -0.05em, leading 0.9. Body text in 'Satoshi' (medium, weight 500). 
- **The Echo Effect**: Primary hero text should be layered with 4-5 background repetitions. Each background layer is offset by -0.04em, -0.08em, -0.12em, and -0.16em respectively, with colors fading from #bfbfbf to #d9d9d9.
- **Micro-interactions**: Use 700ms cubic-bezier(0.77, 0, 0.175, 1) for image reveals (clip-path: inset). Interactive elements should utilize grayscale-to-color transitions and subtle scale transforms (1.05x).

## 5. Layout

The structure follows a clean vertical flow with significant whitespace and an asymmetrical grid for showcase sections. It moves from a high-impact typographic hero to a structured three-column informational grid, followed by a dynamic masonry-style image layout.

## 6. Components

- **Typographic Echo Stack** — A rhythmic text layering technique using CSS absolute positioning.
- **Pill-Shaped Vertical Showcase** — A high-aspect ratio container with full border radius for editorial imagery.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A high-contrast Swiss-style minimalist design system utilizing brutalist typography and editorial layouts. Characterized by a neutral palette of off-whites, deep blacks, and monochromatic grays, this style emphasizes rhythmic patterns through stacked text 'echo' effects and asymmetrical grids. Ideal for luxury travel, architecture portfolios, high-end fashion, and premium editorial content where typography acts as the primary visual driver.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
