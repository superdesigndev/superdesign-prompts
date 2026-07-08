# Design System — Cinematic Style

> Category: Design Systems & Styles  ·  Industry: General
> Auto-scaffolded from prompt [`cinematic-style`](../../prompts/cinematic-style/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style utilizes a base of #050505 for depth. Typography is centered around 'Aspekta' (weights 300, 500, 700, 900), prioritizing font-weight: 900 for hero headings and font-weight: 700 with wide tracking (0.2em) for secondary labels. Color accents are minimal but punchy: a gradient from cyan (#06B6D4) to pink (#EC4899) for primary buttons, and a purple glow (#7C3AED) for functional sections. Interactive elements use backdrop-filter: blur(8px) and border: 1px solid rgba(255, 255, 255, 0.1).

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#050505`
- `#06B6D4`
- `#EC4899`
- `#7C3AED`
- `#111111`
- `#FFFFFF`
- `#999999`

## 3. Typography

- `Aspekta`
- `Cinematic`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Theme: Cinematic Dark Mode.
- Colors: Background: #050505; Card Surface: #111111; Text Primary: #FFFFFF; Text Secondary: #999999; Accent Gradient: linear-gradient(to right, #06B6D4, #EC4899).
- Typography: Primary font 'Aspekta'. Hero Headings: size 12vw, weight 900, tracking-tighter. Section Headers: size 10vw, weight 900. Body: size 1.125rem, weight 300.
- Effects: Perspective: 2000px; Backdrop Blur: 8px; Glassmorphism borders: 1px solid rgba(255,255,255,0.1).
- Interactions: Button scale 1.02 on hover; Link transition 0.2s duration; Image grayscale 100% to 0% on hover.

## 5. Layout

The layout follows a modular vertical stack with a fixed, blend-mode-enabled navigation. It transitions from a 3D immersive hero to a bento-style project grid, then into a high-contrast pricing section with deep glow effects, concluding with a massive-scale editorial footer.

## 6. Components

- **3D Transform Cube** — A rotating 4-sided prism used for feature displays.
- **Glass-morphism Price Calculator** — A custom range input for interactive price estimation.

## 7. Motion

REVIEW —
- 02 on hover; Link transition 0
- 2s duration; Image grayscale 100% to 0% on hover

## 8. Voice & Brand

A high-end 'Cinematic' design system characterized by deep-space dark backgrounds, sophisticated 3D CSS transforms, and bold editorial typography. Optimized for premium portfolios, creative agencies, fintech, and high-tech SaaS. It features a signature 3D rolodex/cube hero section, glassmorphism elements, and smooth GSAP-driven scroll parallax. Key aesthetics include 'mix-blend-difference' navigation, vibrant neon gradients (cyan to pink), and a monochromatic 'Aspekta' font foundation with heavy weights and tight tracking.

## 9. Anti-patterns

MUST maintain the perspective: 2000px on the hero container for 3D depth. DO NOT use standard shadows; use border-white/10 and backdrop-blur for depth. MUST use 'mix-blend-difference' on the header to ensure visibility over shifting background colors. Typography must be uppercase for all headings to maintain the cinematic editorial feel.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
