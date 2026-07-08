# Design System — Clean fluid

> Category: Landing Pages  ·  Industry: General
> Auto-scaffolded from prompt [`clean-fluid`](../../prompts/clean-fluid/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style centers on 'Premium Fluidity'. It pairs the elegance of Playfair Display (serif) with the technical precision of JetBrains Mono and the legibility of Inter. The color palette is grounded in a warm cream (#fcfbf9) and deep neutral black (#171717), accented by a vibrant indigo (#4338ca). Motion is governed by a signature cubic-bezier(0.22, 1, 0.36, 1) easing, applied to scroll reveals and hover states.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#fcfbf9`
- `#171717`
- `#4338ca`
- `#e5e5e5`

## 3. Typography

- `Premium Fluidity`
- `Playfair Display`
- `Inter`
- `JetBrains Mono`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

### Design System: Organic Intelligence

**1. Palette:**
- Background Primary: `#fcfbf9` (Cream)
- Background Dark: `#171717` (Rich Charcoal)
- Accent: `#4338ca` (Indigo)
- Secondary Accents (Mesh): Indigo-200/50, Purple-200/40
- Borders/Lines: `#e5e5e5` (Light Grey)

**2. Typography:**
- Heading/Display: 'Playfair Display', serif. Use italics for emphasis/subheadings. Weights: 400, 700. Size for Hero: 11vw-14vw.
- Body Text: 'Inter', sans-serif. Weights: 400, 500. Leading: 1.2 to 1.5.
- Functional/Labels: 'JetBrains Mono', monospace. Uppercase, tracking: 0.3em to 0.5em. Size: 10px-14px.

**3. Motion & Animation:**
- Ease: `cubic-bezier(0.22, 1, 0.36, 1)` (Premium Ease)
- Reveal: `translateY(40px)` and `opacity: 0` to `translateY(0)` and `opacity: 1` over 1000ms.
- Background Mesh: 30s infinite linear rotation/scale drift.
- Button Pulse: Gentle scale(1.02) with 20px blur indigo shadow,  …

## 5. Layout

A section-based layout that transitions between expansive hero containers and structured grids, linked by a signature curved wave element.

## 6. Components

- **Wave Transition** — A concave sectional bridge that creates an organic flow between the hero and content.
- **Intelligent Card Hover** — A depth-focused hover interaction for project items.

## 7. Motion

REVIEW —
- Motion is governed by a signature cubic-bezier(0
- 36, 1) easing, applied to scroll reveals and hover states
- Motion & Animation:**
- - Ease: `cubic-bezier(0
- 36, 1)` (Premium Ease)

## 8. Voice & Brand

A high-end, editorial design system blending luxury serif typography with technical monospace accents. Characterized by fluid 'premium ease' animations, a sophisticated cream and dark charcoal palette (#fcfbf9, #171717), and organic curved transitions. Optimized for AI startups, design studios, fintech dashboards, and luxury tech brands requiring a balance of intelligence and elegance. Key features include scroll-triggered reveal animations, mesh gradient backgrounds, and a signature concave wave transition between sections.

## 9. Anti-patterns

MUST: Use 'mix-blend-difference' on the header to ensure legibility across color transitions. MUST: Use Playfair Display specifically in italic for emphasis words within headers. MUST: Maintain high letter-spacing (0.3em+) on all monospace fonts. MUST-NOT: Use harsh box-shadows; prefer soft, colored blurs or subtle 1px borders. MUST-NOT: Use standard easing; strictly adhere to the premium cubic-bezier specified.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
