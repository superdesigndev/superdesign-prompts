# Design System — Glassmorphism card

> Category: Design Systems & Styles  ·  Industry: General
> Auto-scaffolded from prompt [`glassmorphism-card`](../../prompts/glassmorphism-card/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style relies on the Inter font family for a clean, modern look. It features two primary modes: a high-contrast dark mode using deep blacks (#000000) and translucent glass layers, and a light mode using soft zinc grays (#F4F4F5). Animations are smooth, utilizing cubic-bezier curves for entry and hover states. Key visual elements include 20px-blur glass containers and a subtle grain overlay.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#000000`
- `#F4F4F5`
- `#18181B`
- `#34D399`
- `#71717A`

## 3. Typography

- `Inter`
- `Superdesign`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

### Visual Foundations
- **Color Palette:** Primary Dark (#000000), Light Background (#F4F4F5), Zinc Accent (#18181B), Emerald Highlight (#34D399), Subtle Border (rgba(255, 255, 255, 0.1)).
- **Typography:** Font: 'Inter', sans-serif. 
  - Headings: font-weight 500-700, tracking -0.05em, leading 1.05.
  - Body: font-weight 300-400, color: Zinc-500 (#71717A).
  - Labels: font-weight 700, size 10px, tracking 0.2em, uppercase.
- **Glassmorphism:** 
  - `background: rgba(255, 255, 255, 0.05)`
  - `backdrop-filter: blur(12px)`
  - `border: 1px solid rgba(255, 255, 255, 0.1)`
- **Grain Overlay:** Use a noise SVG as a fixed overlay at 15% opacity to add texture to dark sections.
- **Corner Radius:** Standardize large containers at `2.5rem (40px)` and internal cards at `1rem (16px)` to `1.5rem (24px)`.
- **Animations:** 
  - Entry: `fade-in-up` (TranslateY: 20px to 0, Opacity: 0 to 1) using `cub …

## 5. Layout

The layout is built within a max-width 1600px container. It uses a tiered structure: an immersive full-height hero section with absolute-positioned glass elements, followed by a grid-based feature section, a dark 'productivity' block, and a bento-grid pricing layout.

## 6. Components

- **Interactive Action Button** — A pill-shaped button with a nested circular icon container.
- **Glass Stat Card** — A high-transparency card used for metrics within dark sections.

## 7. Motion

REVIEW —
- Animations are smooth, utilizing cubic-bezier curves for entry and hover states
- - Hover: Scaling effects (105%) and background color transitions (300ms duration)

## 8. Voice & Brand

A premium, high-tech glassmorphism design system characterized by deep translucent layers, dark-to-light transitions, and editorial typography. Featuring a 'Superdesign' aesthetic, it utilizes heavy background blurs, grain textures, and emerald accents. This style is ideal for SaaS, AI platforms, fintech, and high-end design agencies requiring a sophisticated, futuristic feel with bento-grid layouts and fluid animations.

## 9. Anti-patterns

MUST: Maintain the 2.5rem corner radius for all major section wrappers to ensure visual rhythm. MUST: Use 'grainy-gradients' noise textures on dark backgrounds to prevent banding and add 'analog' depth. MUST: Ensure all glass elements have a 1px white border with 10% opacity for edge definition. DO NOT: Use flat colors for dark backgrounds; always apply a subtle bottom-heavy gradient.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
