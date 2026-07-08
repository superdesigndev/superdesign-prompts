# Design System — Focus Mode Detail

> Category: Mobile Apps  ·  Industry: General
> Auto-scaffolded from prompt [`focus-mode-detail`](../../prompts/focus-mode-detail/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is 'Editorial Minimalism' or 'Digital Paper.' It pairs the elegant serif 'Boska' for headings with the functional sans-serif 'Satoshi' for body text. The color palette is strictly limited to Paper (#FFFFFF), Ink (#1A1A1A), and subtle grays. Images are treated with grayscale and low contrast to maintain visual harmony. Animations are slow, purposeful fade-ups (cubic-bezier) that emphasize a calm atmosphere.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#FFFFFF`
- `#1A1A1A`
- `#888888`
- `#E5E5E5`

## 3. Typography

- `Editorial Minimalism`
- `Boska`
- `Satoshi`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

### Visual Style Guide

**Colors:**
- Primary Background (Paper): `#FFFFFF`
- Primary Text (Ink): `#1A1A1A`
- Secondary Text/Metadata: `#888888`
- Borders/Dividers: `#E5E5E5`

**Typography:**
- **Headings (Serif):** 'Boska', serif. Title size: `2.75rem` (44px), `leading-tight` (1.1). Subheadings: `1.5rem` (24px), often italicized.
- **Body Text (Sans):** 'Satoshi', sans-serif. Size: `1.125rem` (18px), `leading-relaxed`. High legibility.
- **Metadata/Labels:** 'Satoshi' Bold, uppercase, tracking `0.1em`, size `0.625rem` (10px).

**Imagery & Effects:**
- **Grayscale Treatment:** All images should have `grayscale(20%)` and `contrast(95%)` for an archival feel.
- **Borders:** Thin `1px` solid lines for dividers.
- **Shadows:** None. Use whitespace and borders for depth.

**Animations:**
- **Fade-Up Entry:** `opacity: 0` to `1`, `translateY(10px)` to `0`. Duration: `0.8s`. Curve: `cubic-bezie …

## 5. Layout

A vertical, single-column mobile layout focusing on a 90% content width. The UI uses a fixed header with backdrop-blur and a scroll-triggered reading progress bar.

## 6. Components

- **Typographic Drop Cap** — A stylized initial letter that sets the editorial tone.
- **Meta-Divider Row** — A high-contrast informational bar separating header from body.

## 7. Motion

REVIEW —
- Duration: `0
- - **Image Hover:** Subtle scale transition (`scale(1

## 8. Voice & Brand

Features include a reading progress indicator, drop-cap styling, and a grayscale image aesthetic. This design is ideal for long-form journalism, philosophical blogs, high-end lifestyle magazines, or premium SaaS documentation systems that prioritize content clarity over interface chrome.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
