# Design System — High energy onboarding

> Category: Onboarding  ·  Industry: General
> Auto-scaffolded from prompt [`high-energy-onboarding`](../../prompts/high-energy-onboarding/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is characterized by its 'Hard-Shadow' neobrutalism and maximalist color palette. Typography pairings use Clash Display for bold, experimental headlines and Satoshi for clean, readable body text. Visual depth is achieved through animated background blobs, a constant 7% opacity noise grain, and 4px-8px solid-color offset shadows rather than blurs.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#2D1B4E`
- `#FF7D2E`
- `#00D4FF`
- `#FFD166`
- `#F9F7F4`

## 3. Typography

- `Clash Display`
- `Satoshi`
- `Hard Shadows`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

### Visual Language
- **Color Palette**: Primary Purple (#2D1B4E), Accent Orange (#FF7D2E), Accent Cyan (#00D4FF), Accent Gold (#FFD166), Background Offwhite (#F9F7F4).
- **Typography**: Display headlines in 'Clash Display' (Bold/Black weight, tracking-tighter). Body text in 'Satoshi' (Regular/Medium/Bold). Mono labels for technical metadata.
- **Shadows**: Use 'Hard Shadows' instead of blurs. Default: 4px 4px 0px 0px #2D1B4E. Large: 8px 8px 0px 0px #2D1B4E.
- **Effects**: Apply a fixed noise texture overlay (SVG fractalNoise at 0.07 opacity). Use glassmorphism (rgba(255,255,255,0.7) + 12px blur) for side panels.
- **Animations**: Entrance animations using cubic-bezier(0.16, 1, 0.3, 1). Floating elements use a 6s ease-in-out loop. Background blobs use 10s 'metaball' translation/scaling.

## 5. Layout

A dual-pane layout featuring a centered, wide content area for onboarding/input and a fixed 'Live Echo' preview sidebar for real-time visualization.

## 6. Components

- **Orbital Intelligence Dial** — A complex circular interaction module representing AI involvement levels.
- **Live Echo Panel** — A sticky glassmorphism sidebar that acts as a terminal and preview area.

## 7. Motion

REVIEW —
- Floating elements use a 6s ease-in-out loop

## 8. Voice & Brand

A maximalist, neobrutalist design system featuring unconventional geometric typography, high-contrast colors, and interactive card stacking. Built for energetic SaaS onboarding, creative platforms, or experimental fintech interfaces. Uses Clash Display and Satoshi fonts with hard shadows (#2D1B4E), vibrant accents in orange (#FF7D2E) and cyan (#00D4FF), and a signature noise-textured background overlay.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
