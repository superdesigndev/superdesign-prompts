# Design System — Architectural Type System Style

> Category: Waitlist & Coming Soon  ·  Industry: General
> Auto-scaffolded from prompt [`architectural-type-system-style`](../../prompts/architectural-type-system-style/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is built on a foundation of pure black (#000000) and white (#FFFFFF) with a single functional accent (Indigo #6366f1). Typography is the primary visual element, using 'Inter Tight' for massive, tightly-spaced headlines and 'JetBrains Mono' for technical data. Layouts are strictly divided by 0.5px hairlines. A subtle noise grain (5% opacity) is layered over the entire interface to provide an organic, tactile feel to the digital canvas.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#000000`
- `#FFFFFF`
- `#6366f1`

## 3. Typography

- `Inter Tight`
- `JetBrains Mono`
- `Inter`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Apply an architectural, Swiss-brutalist style. Palette: Background #000000, Foreground #FFFFFF, Accents #6366f1. Typography: Headlines use 'Inter Tight' (Weight 900, Tracking -0.06em, Uppercase). Metadata and labels use 'JetBrains Mono' (Weight 500, Tracking 0.2em to 0.4em, Size 8px-11px). Body text uses 'Inter' (Weights 300-400). UI Borders: Use 'hairlines' (0.5px width, color rgba(255, 255, 255, 0.15)). Effects: Apply a global noise texture overlay using a fractal noise SVG at 0.05 opacity. Interactions: Hover states should transition over 300ms, typically swapping black/white or shifting to #6366f1. Components should have 0px border-radius unless they are 'pill' buttons.

## 5. Layout

The layout follows a 'Grid Matrix' philosophy where the screen is divided into quadrants and zones using hairline borders. Sections are often 100vh on desktop to create a focused 'fold' experience. Content is pinned to corners or centered within grid cells.

## 6. Components

- **Status Countdown** — A technical timer indicating urgency or system status.
- **The Hairline Border** — A specific border style used to define all containers.
- **Interactive Geometric Card** — A card containing a rotating geometric element.

## 7. Motion

REVIEW —
- Interactions: Hover states should transition over 300ms, typically swapping black/white or shifting to #6366f1

## 8. Voice & Brand

A high-contrast, architectural design system rooted in Swiss Modernism and Brutalist minimalism. Characterized by a monochrome palette, massive 'Inter Tight' display typography, and a rigid grid defined by 0.5px hairlines. Features a technical 'JetBrains Mono' font for metadata and system status indicators, creating an engineering-first aesthetic. Suitable for high-end SaaS, developer tools, fintech, architecture portfolios, and design agencies. Includes a persistent noise overlay for texture and grid-based layouts that utilize viewport-relative sizing for maximalist impact.

## 9. Anti-patterns

MUST: Maintain strict monochrome balance; only use the accent color for one primary action or specific data points. MUST: Use underscores instead of spaces in mono-spaced metadata labels (e.g., NO_CREDIT_CARD). MUST: Align text to the very edges of grid cells for the 'architectural' feel. DO NOT: Use rounded corners on grid cells or input fields. DO NOT: Use shadows or gradients; depth is achieved solely through line-work and contrast.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
