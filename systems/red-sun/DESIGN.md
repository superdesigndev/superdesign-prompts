# Design System — Red sun

> Category: Landing Pages  ·  Industry: General
> Auto-scaffolded from prompt [`red-sun`](../../prompts/red-sun/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is defined by its high-contrast color duo: Coral (#EF4623) and Ink (#2D3B42). Typography follows an editorial hierarchy: 'Instrument Serif' for expressive, large-scale headlines (italicized for emphasis) and 'Manrope' (weights 300-700) for functional UI elements and body copy. UI elements use large corner radii (rounded-3xl to rounded-[3rem]) and subtle depth through 'Soft Peach' (#FDF1EE) background accents and soft blurs.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#EF4623`
- `#2D3B42`
- `#FDF1EE`

## 3. Typography

- `Instrument Serif`
- `Manrope`
- `Soft Peach`
- `Coral and Ink`
- `Red Sun`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Apply a 'Coral and Ink' editorial style. Primary color: #EF4623 (Coral); Secondary color: #2D3B42 (Ink); Background Accent: #FDF1EE (Soft Peach). Typography: Use 'Instrument Serif' for headings (sizes 60px to 160px, tracking-tight) and 'Manrope' for body (18px, leading-relaxed). For animations, use a custom cubic-bezier(0.16, 1, 0.3, 1) curve for 'fade-up' effects that include a starting 2-degree rotation. Navigation must be a glassmorphism header (backdrop-blur 12px, white/80 opacity). Buttons should have a 30px corner radius and include a shadow-lg shadow-primary/20. Use ambient background blurs (#EF4623 at 10% opacity) with 100px-120px blur radii to create depth.

## 5. Layout

An asymmetrical, modular structure using a mix of full-width hero sections and bento-grid feature areas. Content is revealed via scroll-triggered transitions.

## 6. Components

- **Animated UI Simulator** — A floating mockup window representing a software interface.
- **The 'Rotating Logo' Brand Mark** — A simple but dynamic logo mark.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A sophisticated editorial-style design system named 'Red Sun', characterized by a high-contrast 'Coral and Ink' color palette. This style blends 'Instrument Serif' for high-impact typography with 'Manrope' for technical precision. Features include bento-grid layouts, glassmorphism navigation, scroll-triggered animations with subtle rotations, and soft ambient background blurs. Ideal for premium SaaS, creative agencies, AI product design tools, and fintech platforms looking for a balance between warmth and authority.

## 9. Anti-patterns

MUST: Use 'Instrument Serif' specifically for emphasis and large headers to maintain the editorial feel. MUST: Use the cubic-bezier(0.16, 1, 0.3, 1) curve for all entry animations. MUST: Use large corner radii (min 24px) for all containers. DO NOT: Use standard blue or green for primary actions; stick strictly to #EF4623. DO NOT: Use sharp 90-degree corners on any primary UI containers.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
