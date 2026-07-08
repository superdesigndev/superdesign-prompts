# Design System — Cinematic Noir Style

> Category: Design Systems & Styles  ·  Industry: General
> Auto-scaffolded from prompt [`cinematic-noir-style`](../../prompts/cinematic-noir-style/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is built on a high-contrast monochromatic palette with a singular pop of red (#ef4444) for selections. Typography uses the ZTNature font family with extreme weight pairings (Thin Italic next to Black). Layouts use generous white (or black) space. Motion is fluid and scroll-bound, utilizing scale and opacity transforms to simulate lens focal shifts.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#ef4444`
- `#000000`
- `#09090b`
- `#18181b`
- `#FFFFFF`
- `#fafafa`
- `#e5e5e5`
- `#888`

## 3. Typography

- `ZTNature`
- `Cinematic Noir`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Color Palette: Backgrounds: Deep Black (#000000), Zinc Black (#09090b), Surface Gray (#18181b), Pure White (#FFFFFF), Ghost White (#fafafa). Foreground: Off-White (#e5e5e5), Muted Gray (#888), Deep Black (#000000). Highlight: Red (#ef4444). 
Typography: Font family 'ZTNature'. Headings: 11vw-12vw size, font-weight 900 (Black) or 500 (Medium), tracking -0.03em. Body: 1.25rem (20px) font-weight 300 (Light) or 400 (Regular), tracking tight. Sub-labels: 14px Mono for categories. 
Effects: Noise overlay at 15% opacity using mix-blend-overlay. Radial gradient background: radial-gradient(ellipse at center, rgba(139,69,69,0.4) 0%, rgba(20,20,20,0.8) 60%, rgba(0,0,0,0.95) 100%). 
Motion: Use cubic-bezier(0.16, 1, 0.3, 1) for entrance animations. Scroll-linked transforms: Scale 1.0 -> 1.27 for backgrounds, 1.0 -> 0.89 for hero headings.

## 5. Layout

A vertical narrative structure consisting of a full-screen immersive hero, a high-contrast grid for featured work, a focused minimalist manifesto section, and a heavy-type footer.

## 6. Components

- **Scroll-Linked Zoom Header** — A hero text component that creates a 'receding' effect into the screen as the user scrolls down, simulating depth.
- **Interactive Project Card** — A card with a sophisticated reveal animation that shifts metadata and icons simultaneously.

## 7. Motion

REVIEW —
- Motion is fluid and scroll-bound, utilizing scale and opacity transforms to simulate lens focal shifts
- Motion: Use cubic-bezier(0

## 8. Voice & Brand

A high-end 'Cinematic Noir' design system characterized by dramatic dark-mode aesthetics, high-contrast editorial typography, and immersive scroll-driven parallax effects. Suitable for creative agencies, luxury fashion, fintech, and high-end portfolios. Features include grain overlays, radial gradients with subtle warm tints, and brutalist-scale headings that blur the line between digital interface and cinematic experience.

## 9. Anti-patterns

MUST: Use 'ZTNature' or a similar high-contrast serif/sans-serif pair with weights from 100 to 900. MUST: Apply a subtle grain overlay to the entire site to achieve the 'Noir' look. MUST: Maintain 'mix-blend-difference' on the navigation to handle the white/black section transitions. DO NOT: Use vibrant colors except for the #ef4444 selection color. DO NOT: Add rounded corners; all edges should be sharp and architectural.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
