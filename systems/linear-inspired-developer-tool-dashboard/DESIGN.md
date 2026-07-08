# Design System — Linear inspired developer tool dashboard

> Category: Dashboards  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`linear-inspired-developer-tool-dashboard`](../../prompts/linear-inspired-developer-tool-dashboard/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Deep dark mode theme using #0e0e0e for background and #111113 for surfaces. Typography features Inter (Sans) for UI elements and JetBrains Mono for data/technical metadata. Primary accent color is #5e6ad2. Animations are crisp, using cubic-bezier(0.16, 1, 0.3, 1) for rapid yet smooth transitions.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#0e0e0e`
- `#111113`
- `#5e6ad2`
- `#f3f4f6`
- `#9ca3af`
- `#6b7280`
- `#4b5563`
- `#f97316`
- `#10b981`
- `#ef4444`

## 3. Typography

- `Inter`
- `JetBrains Mono`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

### Visual Language & Style Guide

**Color Palette:**
- **Base Background:** `#0e0e0e` (main canvas).
- **Surface Background:** `#111113` (sidebar, panels).
- **Accent Color:** `#5e6ad2` (Indigo-blue) used for primary buttons, active states, and focus rings.
- **Border Color:** `rgba(255, 255, 255, 0.05)` (highly subtle separation).
- **Text Colors:** Primary: `#f3f4f6`, Secondary: `#9ca3af`, Tertiary: `#6b7280`, Muted/Mono: `#4b5563`.
- **Status Colors:** In-progress: `#f97316` (Orange), Active/Success: `#10b981` (Emerald), Error: `#ef4444` (Red).

**Typography:**
- **Sans-Serif:** 'Inter', sans-serif. Use 14px (0.875rem) for main text, 13px (0.8125rem) for secondary UI, and 11px (0.6875rem) for uppercase category labels.
- **Monospace:** 'JetBrains Mono', monospace. Use for IDs, version numbers, and system logs at 10px-12px.
- **Font Weights:** Medium (500) for headers/buttons, Regular …

## 5. Layout

Triple-column layout with fixed-width navigation and contextual panels, flanking a flexible main content area.

## 6. Components

- **AI Agent Control Card** — A specialized block for adjusting AI parameters within the detail view.
- **Keyboard Shortcut Toast** — Floating hint for keyboard-driven users.
- **Status Metadata Badge** — Small technical tags for categorizing items.

## 7. Motion

REVIEW —
- - **Hover Transitions:** 150ms-200ms ease-in-out on backgrounds and text colors
- 2s duration using `cubic-bezier(0

## 8. Voice & Brand

A high-performance dark-mode console design inspired by Linear and high-end developer tools. Featuring a deep charcoal and black palette (#0e0e0e, #111113) with a vibrant indigo accent (#5e6ad2). The layout uses a classic three-pane structure: a 240px navigation sidebar, a central list view, and a 480px sliding contextual detail panel. Key aesthetics include minimal borders (white/5), Inter/JetBrains Mono typography pairing, glassmorphism overlays, and precise status indicators with subtle animations. Optimized for SaaS dashboards, developer platforms, and AI-driven workflow management tools.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
