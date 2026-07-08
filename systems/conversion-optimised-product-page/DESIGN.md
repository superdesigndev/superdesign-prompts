# Design System — Conversion-optimised Product Page

> Category: E-commerce  ·  Industry: E-commerce & Retail
> Auto-scaffolded from prompt [`conversion-optimised-product-page`](../../prompts/conversion-optimised-product-page/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The design uses a strictly monochrome palette (#FFFFFF, #F5F5F5, #111827) and 'General Sans' typography to create a high-end, editorial feel. It emphasizes clean lines via 1px borders (#E5E7EB) and subtle micro-interactions like 500ms image zooms and ring-offset focus states for interactive elements. Layout follows a strict 1440px grid with variable padding based on screen size (24px to 80px).

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#FFFFFF`
- `#F5F5F5`
- `#111827`
- `#E5E7EB`
- `#F9FAFB`
- `#6B7280`
- `#D1D5DB`

## 3. Typography

- `General Sans`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a minimalist monochrome design system. **Colors**: Primary Background: #FFFFFF; Secondary Background (sections/cards): #F9FAFB; Text: #111827; Secondary Text: #6B7280; Borders/Dividers: #E5E7EB; Accents: #111827 (Primary Button), #D1D5DB (Placeholders). **Typography**: Use 'General Sans' (or similar geometric sans). H1: 36px/40px weight 500, tight tracking; H2: 24px weight 500; Body: 16px weight 400, leading 1.6; Labels/Small: 14px weight 500; Captions: 12px. **Spacing**: Base unit 4px. Use 24px (6 units) for standard gaps, 48px (12 units) for section padding, and 96px (24 units) for major vertical breathing room. **Interactive Elements**: Buttons must have 6px border-radius. Product swatches should use a ring-offset-2 effect when active. Hover states for cards should trigger a 1.05 scale transform over 500ms. All borders should be 1px solid unless specified.

## 5. Layout

A top-down flow starting with a functional header, moving into a 2-column product detail section (Gallery 60% / Info 40%), followed by trust-building horizontal strips (Social Proof/Benefits) and ending with a 4-column related products grid.

## 6. Components

- **Sticky Conversion Bar** — A fixed bottom bar that captures attention for conversion.
- **Minimalist Variant Selector** — A clean grid for size selection with interactive states.

## 7. Motion

REVIEW —
- Hover states for cards should trigger a 1

## 8. Voice & Brand

Traditional PDP enhanced with a sticky purchase module that remains visible during scroll. Reinforces CTAs with social proof and benefit blocks to reduce hesitation.

Best suited for
High-volume DTC brands, ads-driven traffic, products optimized for CRO.

## 9. Anti-patterns

MUST maintain strict monochrome color usage; do not introduce accent colors other than black/white/gray. MUST use 4:5 and 3:4 aspect ratios for all product imagery to maintain an editorial vertical feel. MUST ensure the sticky purchase bar only appears after the user scrolls past the primary 'Add to Cart' button. DO NOT use heavy drop shadows; use 1px borders for depth instead.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
