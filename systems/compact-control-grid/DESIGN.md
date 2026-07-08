# Design System — Compact Control Grid

> Category: Mobile Apps  ·  Industry: General
> Auto-scaffolded from prompt [`compact-control-grid`](../../prompts/compact-control-grid/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Modern high-density aesthetic using the 'Satoshi' font family for crisp readability. The palette is grounded in Slate neutrals (#F2F4F6 background, #1E293B text) with semantic colors for status: Emerald for active/safe (#10B981), Orange for heating/warning (#F97316), and Yellow for lights (#FACC15). Elements use a consistent 16px (2xl) border radius, subtle 1px borders, and micro-interactions like 0.98x scale-down on press.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#F2F4F6`
- `#1E293B`
- `#10B981`
- `#F97316`
- `#FACC15`
- `#64748B`
- `#2563EB`
- `#6366F1`
- `#9333EA`
- `#E2E8F0`
- `#F1F5F9`
- `#EF4444`

## 3. Typography

- `Satoshi`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

### Visual Style Guide
- **Typography**: Primary font 'Satoshi'. Headers: 14px bold leading-tight. Subtext/Secondary: 10px-12px medium/bold. Use uppercase with 0.1em tracking for section headers.
- **Color Palette**:
  - Background: #F2F4F6
  - Primary Text: #1E293B (Slate 800)
  - Secondary Text: #64748B (Slate 500)
  - Semantic Accents: Emerald (#10B981), Orange (#F97316), Yellow (#FACC15), Blue (#2563EB), Indigo-to-Purple Gradient (#6366F1 to #9333EA).
- **Borders & Shadows**: 1px solid #E2E8F0 (Slate 200) or #F1F5F9 (Slate 100). Subtle shadow-sm for cards.
- **Rounding**: 16px (2xl) for cards and modular blocks; pill-shaped (full) for toggles and status chips.
- **Animations**: 
  - Micro-interaction: `transform: scale(0.98)` on active state (100ms duration).
  - Pulse: Red dot (#EF4444) for live indicators.
  - Music Visualizer: 3 vertical bars with staggered infinite bounce animati …

## 5. Layout

A vertically stacked mobile layout consisting of a fixed-width container with three primary zones: a system status header, a scrollable main dashboard, and a bottom navigation bar.

## 6. Components

- **Media Control Card** — Vibrant gradient card with a mini-visualizer.
- **Live Camera Card** — Dark-themed card with live recording indicator.

## 7. Motion

REVIEW —
- 98)` on active state (100ms duration)

## 8. Voice & Brand

A dense arrangement of controls using grids and grouped sections. Prioritizes scanability and speed over storytelling.

Best Suitable For
Utilities, device controllers, system tools, internal apps.

## 9. Anti-patterns

MUST: Maintain tight spacing (12px gap in grids) to achieve 'dense' feel. MUST: Use high-contrast between headers and subtext (Bold 14px vs Medium 10px). DO NOT: Use standard 16px body text as it breaks the information density. MUST: Include a scale-down effect on every clickable modular card for tactile feedback.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
