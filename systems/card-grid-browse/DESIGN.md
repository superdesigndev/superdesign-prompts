# Design System — Card Grid Browse

> Category: Mobile Apps  ·  Industry: General
> Auto-scaffolded from prompt [`card-grid-browse`](../../prompts/card-grid-browse/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Minimalist editorial style using 'General Sans' for a modern feel. The palette is dominated by pure white (#FFFFFF), slate grays (#F1F5F9, #64748B, #0F172A), and sharp black accents. Animations are subtle, featuring 700ms image transitions and 95% scaling on active touch states. Borders are thin (1px) and used sparingly to define hierarchy without clutter.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#FFFFFF`
- `#F1F5F9`
- `#64748B`
- `#0F172A`
- `#F8FAFC`
- `#000000`

## 3. Typography

- `General Sans`
- `Minimalist Editorial`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a design with a 'Minimalist Editorial' aesthetic. 
- **Typography**: Primary font 'General Sans'. Use font-weight 600 for headings (24px, -0.025em tracking) and product titles (14px). Use font-weight 400 for categories (12px, #64748B).
- **Color Palette**: Backgrounds in #FFFFFF; Secondary surfaces in #F8FAFC; Borders in #F1F5F9; Primary text in #0F172A; Accents in #000000.
- **Shadows & Borders**: Avoid heavy shadows. Use 1px solid borders in #F1F5F9 for headers, footers, and pills.
- **Interactions**: Implement a `duration-700` ease-out transition on image hover (scale: 105%). Use `active:scale-95` for all clickable buttons and pills for tactile feedback.
- **Radius**: Large radius (9999px) for category pills and circular icon buttons; sharp corners (0px) for product images to maintain a professional look.

## 5. Layout

A vertical-scrolling mobile layout composed of a sticky header, a scrollable category filter, a fixed-width grid, and a persistent bottom navigation bar.

## 6. Components

- **Interactive Filter Button** — Action icon with a status indicator
- **Status Badges** — Minimalist overlay labels on images

## 7. Motion

REVIEW —
- - **Interactions**: Implement a `duration-700` ease-out transition on image hover (scale: 105%)

## 8. Voice & Brand

A sophisticated, mobile-first product browsing layout emphasizing whitespace, clean typography, and a stable 2-column grid. The design utilizes a monochrome base with slate-toned neutrals to create a high-end 'boutique' feel, prioritizing product imagery and effortless navigation. Suitable for premium furniture, fashion, architecture, or design-focused platforms.

## 9. Anti-patterns

MUST: Maintain strict 3:4 aspect ratios for product images. MUST: Use 'General Sans' or a very clean geometric sans-serif to maintain the high-end feel. DO NOT: Use heavy drop shadows or rounded corners on images. DO NOT: Allow the header to obscure content without a backdrop-blur effect (bg-white/95 backdrop-blur-sm).

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
