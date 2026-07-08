# Design System — Futuristic SasS Landing Page

> Category: Landing Pages  ·  Industry: General
> Auto-scaffolded from prompt [`futuristic-sass-landing-page`](../../prompts/futuristic-sass-landing-page/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is 'Modern Atmospheric'. It pairs dark, deep backgrounds (#0f172a) in the hero and testimonials with clean, off-white surfaces (#f8f9fa) for detailed features. Typography is a critical pillar, using a serif font (Lora) for large, expressive headlines and a high-legibility sans (Inter) for body text. Animations are subtle but intentional: typing cursors, 180-degree logo rotations on hover, and 500ms smooth transitions for sticky navigation states.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#0f172a`
- `#f8f9fa`
- `#6366f1`

## 3. Typography

- `Modern Atmospheric`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

### Visual Language
- **Base Palette**: Primary Dark (#0f172a), Brand Indigo (#6366f1), Surface White (#f8f9fa), Border White (rgba(255,255,255,0.1)).
- **Typography**: 
  - Headlines: Serif (Lora), 400-700 weight, tracking-tight, leading 1.1.
  - UI/Body: Sans (Inter), 400-600 weight, leading-relaxed.
  - Accents/Branding: Display (Space Grotesk), tracking-tight.
- **Glassmorphism**: 
  - Soft: `background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1);`.
  - Strong: `background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.1); shadow: 0 4px 30px rgba(0, 0, 0, 0.1);`.
- **Effects**: 
  - Outer Glow: `radial-gradient(from-indigo-500 via-purple-500 to-pink-500), blur(20px), opacity(0.3)`. 
  - Grid Overlays: Subtle 1px grid pattern with linear-gradient masks.

## 5. Layout

A tiered layout starting with a 110vh atmospheric hero section, transitioning into a multi-column feature section with sticky side-navigation, followed by a glassmorphic masonry testimonial grid and a clean accordion-based FAQ.

## 6. Components

- **Vibe Input Box** — A high-fidelity text input that feels like a primary command center.
- **Sticky Feature Nav** — Vertical navigation that tracks user progress through content sections.

## 7. Motion

REVIEW —
- Animations are subtle but intentional: typing cursors, 180-degree logo rotations on hover, and 500ms smooth transitions for sticky navigation states
- The style emphasizes depth through backdrop blurs, subtle borders (1px), and smooth micro-interactions like scroll-triggered navigation and hover-based transforms

## 8. Voice & Brand

A modern, atmospheric SaaS design system featuring a high-contrast blend of dark mode hero sections and light mode content areas. Characterized by glassmorphism, sophisticated serif-sans typography pairing, and ethereal glows, it is ideal for AI startups, design tools, creative portfolios, and premium digital platforms. The style emphasizes depth through backdrop blurs, subtle borders (1px), and smooth micro-interactions like scroll-triggered navigation and hover-based transforms.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
