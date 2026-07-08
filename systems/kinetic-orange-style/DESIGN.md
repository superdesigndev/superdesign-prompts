# Design System — Kinetic Orange Style

> Category: Design Systems & Styles  ·  Industry: General
> Auto-scaffolded from prompt [`kinetic-orange-style`](../../prompts/kinetic-orange-style/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

High-impact brutalist theme. It pairs the heavy weight of 'Archivo Black' for display text with the technical precision of 'Space Mono' for metadata and labels. The primary color is a vibrant electric orange (#FF4D00). Visuals are defined by thick borders (2px+), skewed sections, and continuous marquee animations.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#FF4D00`
- `#000000`
- `#FFFFFF`

## 3. Typography

- `Archivo Black`
- `Space Mono`
- `Inter`
- `Kinetic Orange`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a design with a primary background color of #FF4D00 and deep black #000000 text. 
- **Typography**: Headers in 'Archivo Black', uppercase, tracking -0.04em, line-height 0.85-0.9. Metadata and UI labels in 'Space Mono', tracking -0.02em. Body text in 'Inter'. 
- **Color Palette**: Brand Orange (#FF4D00), Solid Black (#000000), and Pure White (#FFFFFF) for high-contrast accents on black backgrounds. 
- **Borders**: 2px solid #000000 for section dividers and buttons. 
- **Motion**: Use linear marquees for text-heavy sections. Implement a 'spin' animation for circular indicators (12s duration). 
- **Interactions**: Hover states should include horizontal translations (translate-x-4) and scale transforms (scale-110). Selection color should be background: black; color: #FF4D00;

## 5. Layout

A vertically stacked layout with full-width sections. It uses a floating 'pill' navigation bar and incorporates skewed transitions between sections to break the grid.

## 6. Components

- **Rotating Scroll Indicator** — A circular SVG path with text that rotates infinitely.
- **Brutalist Service Card** — Interactive list item with reveal effects.

## 7. Motion

REVIEW —
- - **Motion**: Use linear marquees for text-heavy sections
- Implement a 'spin' animation for circular indicators (12s duration)
- - **Interactions**: Hover states should include horizontal translations (translate-x-4) and scale transforms (scale-110)
- It features bold, oversized editorial typography, technical monospace accents, and rhythmic motion through marquees and rotating elements

## 8. Voice & Brand

A high-energy brutalist design system characterized by a high-contrast 'Kinetic Orange' (#FF4D00) and black palette. It features bold, oversized editorial typography, technical monospace accents, and rhythmic motion through marquees and rotating elements. Ideal for creative agencies, fintech, modern portfolios, or AI-driven startups looking for a 'loud' and confident brand presence.

## 9. Anti-patterns

MUST: Maintain extremely high contrast. MUST: Use only uppercase for Archivo Black headers. MUST: Ensure all borders are sharp (no rounded corners except for pill-shaped buttons and navigation). DO NOT: Use gradients, drop shadows (except for navigation depth), or soft pastels. DO NOT: Use standard sans-serifs for headlines.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
