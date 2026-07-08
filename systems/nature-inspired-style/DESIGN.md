# Design System — Nature Inspired Style

> Category: Design Systems & Styles  ·  Industry: General
> Auto-scaffolded from prompt [`nature-inspired-style`](../../prompts/nature-inspired-style/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style uses a high-contrast 'Forest and Sage' color story. Typography is a mix of heavy, condensed display faces (Anton) for impact and clean, tracked-out sans-serifs (Inter) for utility. Visuals are treated with a persistent SVG noise overlay (4% opacity) to add texture. Animations focus on vertical reveals using a custom cubic-bezier for a 'snappy yet smooth' high-end feel.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#01472e`
- `#ccd5ae`
- `#e9edc9`
- `#fefae0`
- `#a3b18a`

## 3. Typography

- `Forest and Sage`
- `Anton`
- `Inter`
- `Forest`
- `Organic Brutalist`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a design system using an earthy, organic palette: Forest (#01472e), Sage (#ccd5ae), Olive (#e9edc9), Cream (#fefae0), and Moss (#a3b18a). 

### Typography
- **Display/Headings**: Use 'Anton' (sans-serif/impactful). Hero size: 23vw, leading: 0.75, letter-spacing: -0.05em. Section titles: 15vw.
- **Body/Utility**: Use 'Inter'. Font weights: 400 (regular), 700 (bold). Use uppercase with letter-spacing 0.2em - 0.4em for all labels and buttons.

### Texture & Effects
- **Noise Overlay**: Apply a fixed SVG fractal noise overlay at 0.04 opacity across the entire viewport.
- **Corners**: Use extreme rounding: `border-radius: 5rem` for large sections, `border-radius: 2.5rem` for cards/images.
- **Shadows**: Soft, deep shadows for floating elements: `shadow-2xl` with a tint of the 'Forest' color (rgba(1, 71, 46, 0.2)).

### Animation
- **Reveal Logic**: Components should slide up from `tran …

## 5. Layout

A vertically stacked layout with distinct color-blocked sections using ultra-rounded top corners to separate themes. Employs a fixed navigation bar and high-impact hero section.

## 6. Components

- **Floating Organic Cards** — Images with extreme rounding and parallax rotation.
- **Blur-Reveal Button** — Hover interaction for product cards.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A nature-inspired 'Organic Brutalist' design system perfect for wellness, sustainable CPG, eco-friendly lifestyle brands, or high-end nutrition. Characterized by a palette of deep forest greens and earthy sages, the style utilizes massive editorial typography (Anton) paired with functional sans-serifs (Inter). The layout features 'bento-adjacent' rounded grids, floating organic elements with parallax effects, and a subtle film grain noise overlay that gives the digital experience a tactile, premium paper-like feel. Key elements include oversized headings, ultra-rounded corners (up to 5rem), and fluid reveal animations.

## 9. Anti-patterns

MUST: Maintain the noise overlay for the 'analog' feel. MUST: Use the exact cubic-bezier (0.16, 1, 0.3, 1) for all transitions to ensure the 'premium' motion signature. DO NOT: Use standard sharp corners; everything must have at least a small radius, but primary containers must use the 5rem radius. DO NOT: Use standard black text; always use the Forest (#01472e) color for dark text.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
