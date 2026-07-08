# Design System — System Interface Feature Announcement

> Category: Other  ·  Industry: AI & Tech
> Auto-scaffolded from prompt [`system-interface-feature-announcement`](../../prompts/system-interface-feature-announcement/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Brutalist and utilitarian style. Typography combines JetBrains Mono (700 for headings, 400 for technical data) and Inter (400 for body prose). Color palette: Background #F5F5F5, Text #1A1A1A, Accents #00CC00 (Green) and #FFA500 (Amber), Borders #CCCCCC. Animations are 'stepped' and mechanical (no smooth easing), featuring cursor blinks and line-by-line reveals.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#F5F5F5`
- `#1A1A1A`
- `#00CC00`
- `#FFA500`
- `#CCCCCC`
- `#EBEBEB`
- `#000000`

## 3. Typography

- `Technical Brutalism`
- `JetBrains Mono`
- `Inter`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a design system based on 'Technical Brutalism'. 

### Colors
- Primary Background: #F5F5F5
- Primary Text: #1A1A1A
- Accent Color (Action/Success): #00CC00 (Terminal Green)
- Warning Color: #FFA500 (Amber)
- Border Color: #CCCCCC (Solid 1px)
- Code Block Background: #EBEBEB

### Typography
- Technical/Data Font: 'JetBrains Mono', monospace. Use for headers, metadata, and status bars.
- Prose/Reading Font: 'Inter', sans-serif. Use for long-form explanations.
- Heading 1: font-weight 700, size 72pt-96pt, tracking-tighter, uppercase, line-height 0.9.
- Metadata: font-size 10px-12px, uppercase, tracking-widest.

### Effects & Borders
- Borders: Solid 1px #CCCCCC on all container edges. Use 'divide-x' and 'divide-y' patterns for grids.
- Shadows: Strictly NO soft shadows. Use hard-offset shadows for interactive elements: 4px 4px 0px 0px #000000.
- Corners: 0px (No rounding on any eleme …

## 5. Layout

The layout follows a strict modular grid where every section is defined by clear 1px horizontal and vertical dividers. It prioritizes vertical stacking with dense, multi-column metadata grids.

## 6. Components

- **Hard-Shadow Node** — A utilitarian card component for data display.
- **Terminal Accordion** — An FAQ or detail component that feels like a directory expansion.
- **Monospace CTA** — A high-visibility system action button.

## 7. Motion

REVIEW —
- - Transitions: Duration 0ms (Instant) or 'steps' timing functions
- - Micro-interactions: Background color flips (Invert) on hover for buttons

## 8. Voice & Brand

A brutalist, typography-driven system interface design optimized for technical documentation and feature announcements. Featuring a high-density information layout, rigid grid alignment, and a mechanical aesthetic, it uses JetBrains Mono for a terminal-like feel and Inter for readability. Perfect for developer tools, SaaS infrastructure updates, engineering blogs, and fintech platforms. Key elements include visible 1px borders, a 'system status' header, stepped animations, and a monochrome palette with terminal-green accents.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
