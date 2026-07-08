# Design System — Tech Editorial

> Category: Landing Pages  ·  Industry: General
> Auto-scaffolded from prompt [`tech-editorial`](../../prompts/tech-editorial/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The design uses a trio of typefaces: Playfair Display (Serif) for headers and emotional impact, Space Grotesk (Sans) for readability, and Space Mono (Mono) for all technical data, labels, and buttons. The color palette is organic and muted: Background (#f7f6f2), Foreground (#1c1c1c), and Primary Accent (#3d7068). Layouts are governed by a strict 4-column vertical guide system and 1px borders. Transitions use a custom 'editorial' cubic-bezier(0.16, 1, 0.3, 1) for a smooth, high-fashion feel.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#f7f6f2`
- `#1c1c1c`
- `#3d7068`
- `#e5e4de`

## 3. Typography

- `Playfair Display`
- `Space Mono`
- `Space Grotesk`
- `Tech Editorial`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Apply an editorial tech aesthetic using background #f7f6f2 and foreground #1c1c1c. Typography: Headings in 'Playfair Display' (light weight, tight tracking), UI labels and buttons in 'Space Mono' (uppercase, tracking 0.2em-0.3em), and body text in 'Space Grotesk'. Use #3d7068 as the primary accent color for buttons and highlights. Implement 1px borders using #e5e4de. All animations must use cubic-bezier(0.16, 1, 0.3, 1) with a 700ms-1000ms duration. Include a fixed background grid of 40px squares with a radial mask that fades toward the edges.

## 5. Layout

The layout is built on a max-width 7xl container with visible structural vertical dividers. Sections are clearly demarcated by 1px horizontal borders. The navigation is a floating-to-fixed transition element with backdrop blur.

## 6. Components

- **Scan-Line Progress Bar** — A technical loading indicator used for status updates.
- **Animated CTA Button** — High-intent button with character-spacing and background-fill transitions.
- **Editorial Word Reveal** — Scroll-synced typography effect.

## 7. Motion

REVIEW —
- 3, 1) with a 700ms-1000ms duration

## 8. Voice & Brand

A high-end 'Tech Editorial' aesthetic that merges brutalist precision with classic editorial sophistication. It features a muted, paper-like color palette (#f7f6f2), a structured grid-line system, and a unique pairing of high-contrast Serif (Playfair Display) for display headers and technical Mono (Space Mono) for functional UI. The style is characterized by scroll-triggered text reveals, glassmorphism navigation, and 'scan-line' animations that suggest a sophisticated AI-driven process. Ideal for high-tech SaaS, AI research labs, design agencies, and premium fintech platforms.

## 9. Anti-patterns

MUST: Maintain the #f7f6f2 background to avoid a 'clinical' white look. MUST: Use 1px borders instead of shadows for section separation. MUST: Ensure 'Space Mono' is used for all metadata and numeric data. MUST NOT: Use rounded corners larger than 2px. MUST NOT: Use vibrant gradients; stick to solid fills and simple opacity transitions.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
