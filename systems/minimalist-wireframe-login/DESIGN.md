# Design System — Minimalist Wireframe Login

> Category: Auth & Login  ·  Industry: General
> Auto-scaffolded from prompt [`minimalist-wireframe-login`](../../prompts/minimalist-wireframe-login/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The design utilizes 'General Sans' across four weights (400-700) for strict hierarchy. The color palette is a monochromatic Slate scale: #FFFFFF (base), #0F172A (primary text/button), #64748B (secondary text), and #E2E8F0 (borders). Micro-interactions include a subtle scale-down effect (0.98x) on buttons and a 4px soft shadow focus ring for input fields. A recurring 40px grid pattern defines the 'wireframe' aesthetic.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#FFFFFF`
- `#0F172A`
- `#64748B`
- `#E2E8F0`
- `#CBD5E1`
- `#F1F5F9`

## 3. Typography

- `General Sans`
- `Wireframe`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a UI with a minimalist industrial 'Wireframe' aesthetic. 
- **Typography**: Font-family: 'General Sans'. Headings: 32px/1.1 leading, font-weight 600. Body text: 18px, color: #64748B. Labels: 14px, weight 500, color: #0F172A. 
- **Color Palette**: Background: #FFFFFF. Text/Buttons: #0F172A. Secondary Text: #64748B. Borders: #E2E8F0. Placeholder: #CBD5E1. 
- **Background**: Apply a subtle blueprint grid using linear gradients of #F1F5F9 at 1px thickness with 40px square size. 
- **Interactive Elements**: Inputs and Buttons should be exactly 56px height with a border-radius of 16px to 20px. 
- **Animation**: Button active state: `transform: scale(0.98)`. Transitions: `all 200ms ease-in-out`. 
- **Shadows**: Primary CTA uses a soft shadow: `box-shadow: 0 10px 15px -3px rgba(15, 23, 42, 0.1)`.

## 5. Layout

Three-tier vertical stack: Top identity section, middle input group, and bottom-anchored action footer with a sticky gradient background.

## 6. Components

- **Wireframe Logo Box** — A placeholder container representing the brand mark.
- **Industrial Input Field** — High-radius, clean input with custom focus state.

## 7. Motion

REVIEW —
- Transitions: `all 200ms ease-in-out`

## 8. Voice & Brand

A high-contrast, minimalist mobile login wireframe optimized for thumb reach and ergonomic ergonomics. It features a slate-heavy palette, industrial-style grid textures, and clean 'General Sans' typography. Suitable for SaaS dashboard entry, fintech authentication, developer tools, and high-end enterprise mobile applications requiring a professional, focus-oriented interface.

## 9. Anti-patterns

MUST ensure all clickable elements (inputs/buttons) have a minimum height of 56px for accessibility. MUST use the 40px grid background to maintain the wireframe concept. DO NOT use vibrant colors; keep the palette restricted to Slate and White. Ensure the secondary sign-up link uses a font-weight of 600 to distinguish it from static text.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
