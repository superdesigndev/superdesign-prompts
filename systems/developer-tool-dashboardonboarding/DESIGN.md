# Design System — Developer tool dashboard/onboarding

> Category: Dashboards  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`developer-tool-dashboardonboarding`](../../prompts/developer-tool-dashboardonboarding/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is defined by its 'Late-night focus' theme: no rounded corners, no gradients, and a matte dark color palette. It uses Space Grotesk for bold, uppercase headers and JetBrains Mono for all technical and descriptive text. The color scheme is monochrome (#111111 background, #FFFFFF accents, #333333 borders) with subtle syntax highlighting for terminal output. Motion is clinical and near-instant (100ms) with no easing.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#111111`
- `#FFFFFF`
- `#333333`
- `#050505`
- `#1A1A1A`
- `#E5E5E5`
- `#555555`
- `#4ADE80`

## 3. Typography

- `Space Grotesk`
- `JetBrains Mono`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

### Color Palette - Background: #111111 (Primary), #050505 (Terminal), #1A1A1A (Surface/Hover) - Border: #333333 - Text: #FFFFFF (Titles), #E5E5E5 (Body), #555555 (Muted) - Accent: #FFFFFF (Primary Action), #4ADE80 (Success/Active Pulse) ### Typography - Display: 'Space Grotesk', Sans-Serif; Weights: 500, 700. Used for section headers and primary buttons. - Monospace: 'JetBrains Mono', Monospace; Weights: 400. Used for all labels, versioning, data, and terminal output. - Sizes: 10px (labels), 12px (body), 24px (h1). ### Effects & Grid - Grid: 40px x 40px background grid using 1px lines at 3% white opacity, masked with a bottom fade. - Border Radius: 0px everywhere. - Cursor: crosshair. - Animation: Instant state changes (<100ms), no cubic-bezier easing; transitions should feel mechanical.

## 5. Layout

A two-pane responsive layout: a main scrollable configuration area (left) and a fixed-width live terminal echo panel (right/sidebar). The main area uses a vertical section-by-section flow with high density and minimal padding.

## 6. Components

- **The Dismiss Item** — A checkable list item that visually 'kills' its content.
- **Vertical Node Dial** — A node-based selection list mimicking a vertical step indicator.
- **Terminal Code Block** — A syntax-highlighted code preview simulating real-time environment changes.

## 7. Motion

REVIEW —
- Motion is clinical and near-instant (100ms) with no easing
- ### Color Palette - Background: #111111 (Primary), #050505 (Terminal), #1A1A1A (Surface/Hover) - Border: #333333 - Text: #FFFFFF (Titles), #E5E5E5 (Body), #555555 (Muted) - Accent: #FFFFFF (Primary Action), #4ADE80 (Success/Active Pulse) ### Typography - Display: 'Space Grotesk', Sans-Serif; Weights: 500, 700

## 8. Voice & Brand

A high-density, terminal-inspired dark mode design system optimized for developer tools, SaaS configuration panels, and technical dashboards. It features a matte #111111 background with a subtle 40px grid pattern, utilitarian typography pairing Space Grotesk with JetBrains Mono, and a high-contrast #FFFFFF accent color. The aesthetic is brutalist and tool-like, utilizing zero border-radius, instant transitions (<100ms), and a dual-pane layout with a live code terminal echo. Ideal for power-user interfaces where information density and technical focus are prioritized over visual decoration.

## 9. Anti-patterns

- MUST NOT use any border-radius; all corners must be 90-degree sharp. - MUST NOT use drop shadows or gradients; depth is achieved solely through border layers and hex color shifts. - MUST maintain high density: vertical padding between major sections should not exceed 40px. - MUST use terminal-adjacent symbols like '//', '>', and '[]' for UI adornment.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
