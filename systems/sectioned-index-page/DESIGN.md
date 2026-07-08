# Design System — Sectioned Index Page

> Category: Mobile Apps  ·  Industry: General
> Auto-scaffolded from prompt [`sectioned-index-page`](../../prompts/sectioned-index-page/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is 'Minimalist Editorial' using a strict monochrome color palette (#FFFFFF to #111827). Typography centers on 'General Sans' with variable weights to denote importance. Animations are subtle: image scaling (1.05x) on hover and a slight compression (0.99x) on active tap states to simulate physical feedback. Rounded corners are generous (16px to 24px) to soften the layout.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#FFFFFF`
- `#111827`
- `#6B7280`
- `#9CA3AF`
- `#F9FAFB`
- `#F3F4F6`
- `#000000`

## 3. Typography

- `Minimalist Editorial`
- `General Sans`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

### Visual Identity System
- **Typography**: Primary font is 'General Sans'. Weights: 700 for H1 (30px), 700 for H2 (18px), 600 for H3/H4 (14px-18px), 400 for body text (14px). Use `tracking-tight` on headings and `tracking-wide` with uppercase for labels.
- **Color Palette**:
  - Background: Primary White (#FFFFFF)
  - Primary Text: Gray-900 (#111827)
  - Secondary Text: Gray-500 (#6B7280)
  - Muted Text/Labels: Gray-400 (#9CA3AF)
  - Surface/Fills: Gray-50/50 (#F9FAFB with 50% opacity)
  - Borders: Gray-100 (#F3F4F6)
- **Elevation & Corners**:
  - Large Cards: `border-radius: 1rem` (16px)
  - Full Gallery Cards: `border-radius: 1.5rem` (24px)
  - Shadows: None (flat design with borders) or extremely subtle soft-diffused shadows (#000000 at 0.05 opacity).
- **Animations**:
  - Image Transitions: `duration: 500ms`, `cubic-bezier(0.4, 0, 0.2, 1)`
  - Hover State: `scale(1.05)` for images
 …

## 5. Layout

A vertically scrollable stack of content modules. Each section begins with a header row (Heading + 'See All' button) followed by specialized content blocks: Gallery (Horizontal), Activity (Vertical), and Recommendations (Grid).

## 6. Components

- **Interactive List Card** — A list item designed for tactile mobile interaction.
- **Micro-Tag (Glassmorphism)** — Overlay tag used on top of imagery.

## 7. Motion

REVIEW —
- 05x) on hover and a slight compression (0
- - Image Transitions: `duration: 500ms`, `cubic-bezier(0
- - Hover State: `scale(1
- 99)` with `transition-transform duration-100`

## 8. Voice & Brand

Features a mixed-media layout including horizontal snap-scrolling cards, vertical activity feeds, and a bento-style recommendation grid. Ideal for content aggregators, interior design apps, portfolio indexes, or minimalist fintech dashboards.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
