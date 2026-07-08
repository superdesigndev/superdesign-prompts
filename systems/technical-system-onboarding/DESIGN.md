# Design System — Technical System Onboarding

> Category: Onboarding  ·  Industry: AI & Tech
> Auto-scaffolded from prompt [`technical-system-onboarding`](../../prompts/technical-system-onboarding/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Industrial/technical theme with a heavy emphasis on typography hierarchy. Primary font is Space Grotesk for geometric display headers, Inter for readable sans-serif body text, and JetBrains Mono for system-level metadata. Color palette is dominated by Slate-950 (#020617) backgrounds with accent color Signal Orange (#FF4F00). Animations are minimal and functional, utilizing cubic-bezier curves for 'slide-up' and 'fade-in' transitions.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#020617`
- `#FF4F00`
- `#0a0f1c`
- `#0f172a`
- `#FF6A26`
- `#1e293b`

## 3. Typography

- `Space Grotesk`
- `Inter`
- `JetBrains Mono`
- `Tech Borders`
- `Capabilities Matrix`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

### Visual Language & Style Guide

**1. Colors:**
- **Primary Background:** Slate-950 (#020617)
- **Secondary Panels:** Slate-925 (#0a0f1c) and Slate-900 (#0f172a)
- **Primary Accent (CTA):** Signal Orange (#FF4F00), Hover: #FF6A26
- **Borders/Dividers:** Slate-800 (#1e293b) at 60% opacity
- **Status Colors:** Online: Emerald-500; Warning/Limit: Deep Orange-900

**2. Typography:**
- **Display/Headers:** 'Space Grotesk', Medium (500) or Bold (700). Characterized by geometric shapes. 
- **Body Text:** 'Inter', Light (300) or Regular (400). Line height: 1.625.
- **Technical Metadata:** 'JetBrains Mono', Regular (400). Used for versions, step counts, and system status.

**3. Effects & UI Elements:**
- **Grid Background:** 40px x 40px grid pattern in Slate-800, opacity 7%, with a radial mask fade.
- **Borders:** 1px solid Slate-800. Use 'Tech Borders' (simulated by L-shaped corner strokes) in …

## 5. Layout

The interface follows a 'Locked Terminal' layout with a fixed header and footer, and a scrolling central content panel. The main interaction area is a centered 12-column grid container with a 5/7 ratio split between high-level description and technical parameters.

## 6. Components

- **Signal CTA Button** — A high-visibility primary action button with an internal shimmer effect.
- **Capabilities Matrix Card** — A technical listing card for system parameters.

## 7. Motion

REVIEW —
- - **Primary Accent (CTA):** Signal Orange (#FF4F00), Hover: #FF6A26

## 8. Voice & Brand

A technical, research-backed onboarding system design using a dark slate palette with high-visibility signal orange accents. Optimized for high-fidelity AI systems, data science dashboards, fintech terminals, and developer tools. Features editorial modern grotesk typography, monospace metadata, grid-based layouts, and a modular 'Capabilities Matrix' structure. Emphasizes reliability, transparency, and deterministic control through structured information hierarchy and a professional, no-nonsense aesthetic.

## 9. Anti-patterns

MUST maintain high information density without clutter. MUST avoid all 'soft' design elements like large border radii, pastel gradients, or playful emojis. MUST ensure all technical metadata (v4.2.0, STEP 01) is set in monospace. DO NOT use glowing text effects except for the small step-indicator bar.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
