# Design System — Luxury-focused Design System

> Category: Design Systems & Styles  ·  Industry: General
> Auto-scaffolded from prompt [`luxury-focused-design-system`](../../prompts/luxury-focused-design-system/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is built on 'League Spartan' sans-serif, using weight and letter-spacing for hierarchy. The color palette is a warm off-white (#fdf8f3), charcoal (#262626), and a dusty rose accent (#e4a4bd). It uses smooth transitions (cubic-bezier) and grayscale-to-color hover effects to signify premium quality.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#fdf8f3`
- `#262626`
- `#e4a4bd`
- `#f5f0eb`

## 3. Typography

- `League Spartan`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use 'League Spartan' as the primary font family for all elements. Primary background: #fdf8f3; Secondary background: #f5f0eb; Accent color: #e4a4bd; Primary text: #262626. For headings, use font-weight 700-900, tracking-tighter, and line-height 0.8. For utility labels, use font-size 10px, font-weight 900, and tracking 0.4em. Animations must use `cubic-bezier(0.16, 1, 0.3, 1)` with a 1s duration. Hover states on images should transition from grayscale(100%) to grayscale(0%) and scale up to 1.08. Navigation should be a glassmorphism effect with `backdrop-filter: blur(12px)` and a subtle 1px border at 5% opacity.

## 5. Layout

The layout uses a 12-column grid system with significant whitespace. It features a high-impact hero section, a clean 3-column service grid, and a signature staggered gallery for portfolio items.

## 6. Components

- **Floating Concierge Badge** — A floating circular element used for highlighting status or rank.
- **Reveal-Up Wrapper** — Scroll-triggered entrance animation for all content blocks.

## 7. Motion

REVIEW —
- It uses smooth transitions (cubic-bezier) and grayscale-to-color hover effects to signify premium quality
- 3, 1)` with a 1s duration
- Hover states on images should transition from grayscale(100%) to grayscale(0%) and scale up to 1

## 8. Voice & Brand

A refined, editorial-style design system characterized by heavy geometric sans-serif typography, a sophisticated dusty rose and charcoal palette, and staggered grid layouts. This aesthetic is optimized for high-end luxury services, boutique hospitality, premium fashion brands, or architectural portfolios. It features scroll-triggered reveal animations, grayscale-to-color image transitions, and a 'glassmorphism' navigation bar. The layout focuses on massive, bold headlines paired with hyper-minimalist utility text, creating a contrast that feels modern yet timeless.

## 9. Anti-patterns

MUST use 'League Spartan' for both body and headers to maintain geometric consistency. MUST NOT use vibrant gradients; keep colors solid and muted. ALL reveal animations must use the specific cubic-bezier(0.16, 1, 0.3, 1) to ensure a high-end, 'weighted' motion feel. Images MUST be grayscale by default and reveal color only on interaction.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
