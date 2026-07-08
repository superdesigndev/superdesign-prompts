# Design System — Glassmorphism Style

> Category: Design Systems & Styles  ·  Industry: General
> Auto-scaffolded from prompt [`glassmorphism-style`](../../prompts/glassmorphism-style/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is defined by its 'dark-mode-first' approach using an obsidian base (#0a0a0a) and high-vibrancy lime accents (#ccff00). Typography pairings involve 'Space Grotesk' for high-impact, tight-tracked headings and 'JetBrains Mono' for technical metadata. Glassmorphism is executed with subtle white overlays (3% opacity) combined with intense 16px background blurs. Visual depth is added through grainy noise textures and 60px grid backgrounds.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#0a0a0a`
- `#ccff00`
- `#000000`
- `#0c0c0c`
- `#10b981`
- `#ebebeb`

## 3. Typography

- `Space Grotesk`
- `JetBrains Mono`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Base theme: Deep black (#000000) shell with obsidian surfaces (#0c0c0c). Primary accent color: Neon Lime (#ccff00). Secondary accent: Emerald Glow (#10b981). Typography: Headings in 'Space Grotesk' (weights: 300 to 700, tracking: -0.06em), body in 'Space Grotesk' (weight: 400), and technical labels in 'JetBrains Mono' (uppercase, tracked out). Glassmorphism specs: Background: rgba(255, 255, 255, 0.03), Backdrop-filter: blur(16px), Border: 1px solid rgba(255, 255, 255, 0.1). Text colors: Primary White (#ebebeb), Secondary White (opacity 60%), Disabled/Muted (opacity 30%). Decorative elements: 60x60px linear-gradient grid pattern, 15% opacity noise SVG overlay, and large 'glow-sphere' radial gradients with 120px blur filters. Animation curves: ease-in-out for floating elements, cubic-bezier(0.4, 0, 0.2, 1) for transitions.

## 5. Layout

A 'floating shell' architecture where the entire site content resides in a rounded container (2.5rem radius) nested within a black viewport. The internal layout follows a bento-grid methodology for features and a high-contrast split-section for the hero.

## 6. Components

- **Glass Floating Card** — A multi-layered glass element that appears to float over the background.
- **Neon Pulse Button** — High-visibility primary action button with a glowing shadow.
- **System Status Tag** — Monospaced utility tag for technical labels.

## 7. Motion

REVIEW —
- Animation curves: ease-in-out for floating elements, cubic-bezier(0

## 8. Voice & Brand

A high-tech glassmorphism design system featuring neon lime accents, deep obsidian surfaces, and a sophisticated blend of architectural grid patterns and organic glowing gradients. Optimized for high-end SaaS, AI product studios, and fintech platforms, this style uses JetBrains Mono for a developer-centric feel and Space Grotesk for bold, editorial headings. Key elements include backdrop-blur effects (glassmorphism), grain/noise overlays, and a 'floating shell' layout that gives the web interface a premium, app-like quality.

## 9. Anti-patterns

MUST use #ccff00 as the primary accent. MUST NOT use standard system fonts; stick to Space Grotesk and JetBrains Mono. MUST maintain at least 16px blur on all glass elements to ensure legibility. MUST use grid patterns and noise overlays to prevent 'flat' dark mode looks. Ensure all container corners have a high radius (at least 2rem) for a modern, hardware-like feel.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
