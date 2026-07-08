# Design System — Neural Noir Interface Style

> Category: Design Systems & Styles  ·  Industry: General
> Auto-scaffolded from prompt [`neural-noir-interface-style`](../../prompts/neural-noir-interface-style/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The design uses a monochromatic dark base (#0a0a0a) accented by a gradient of golds and bronzes. Typography pairings include 'Playfair Display' (Italic) for an editorial feel and 'Inter' for UI precision. Visual interest is driven by a 'bg-dots' radial pattern and blurred glassmorphism layers (rgba 255,255,255, 0.03) with high-radius corners (24px-48px).

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#0a0a0a`
- `#a78b71`
- `#c9b8a0`
- `#e8d5b7`

## 3. Typography

- `Playfair Display`
- `Inter`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a design system with a background of #0a0a0a and a radial dot grid overlay (32px spacing, white at 8% opacity). Use 'Playfair Display' (Italic) for headings and 'Inter' (300-700 weight) for body text. Accent color palette: Base Gold #a78b71, Light Gold #c9b8a0, and Hover Gold #e8d5b7. Implement 'glassmorphism' for all cards: background rgba(255,255,255, 0.03), backdrop-filter blur(10px), and border 1px solid rgba(255,255,255, 0.1). Animations should use 'cubic-bezier(0.4, 0, 0.2, 1)' for transitions and 'power4.out' for entrance reveals. Include a central glow effect using box-shadow: 0 0 100px rgba(167, 139, 113, 0.2).

## 5. Layout

A vertically structured single-page layout that transitions from a complex, interactive hero section into clean, grid-based content blocks.

## 6. Components

- **Neural Connection Lines** — SVG paths that dynamically connect UI elements to a central point.
- **Satellite Media Cards** — Floating preview cards that interact with the mouse and central node.
- **Live Notification Pill** — A floating status indicator with a breathing animation.

## 7. Motion

REVIEW —
- Accent color palette: Base Gold #a78b71, Light Gold #c9b8a0, and Hover Gold #e8d5b7

## 8. Voice & Brand

The Neural Noir Interface Style is a high-end, futuristic aesthetic characterized by a 'tech-noir' atmosphere. It blends deep dark backgrounds (#0a0a0a) with sophisticated gold and bronze accents (#a78b71, #e8d5b7) and editorial typography. Key features include glassmorphism, neural network-inspired SVG connection lines, and a bento-grid layout. This style is optimized for premium AI platforms, creative design engines, high-end SaaS, and editorial-driven tech portfolios. It utilizes a combination of sleek sans-serif (Inter) for functional elements and elegant serif italics (Playfair Display) for headlines, creating a contrast between high-tech performance and classic sophistication.

## 9. Anti-patterns

MUST: Maintain a high level of contrast between the #0a0a0a background and white/gold elements. MUST NOT: Use standard blue/purple gradients common in tech; stick strictly to the gold/bronze spectrum. MUST: Use heavy letter-spacing on small uppercase text (labels, roles) to maintain the premium feel. MUST: Apply backdrop-filter: blur(10px) to all overlapping layers to prevent visual clutter.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
