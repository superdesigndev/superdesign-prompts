# Design System — Modular Card Dashboard

> Category: Dashboards  ·  Industry: General
> Auto-scaffolded from prompt [`modular-card-dashboard`](../../prompts/modular-card-dashboard/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is built on a grayscale wireframe foundation. It uses thin but distinct #111111 borders, a light gray background (#F5F5F5) for contrast against white cards, and bold neubrutalist interactions. Typography relies on the Switzer sans-serif family for an editorial, modern feel. Micro-interactions include vertical translations and solid hard-shadow reveals that suggest tactile depth.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#111111`
- `#F5F5F5`
- `#FFFFFF`
- `#6B7280`

## 3. Typography

- `Switzer`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Apply a minimalist wireframe aesthetic. Background color: #F5F5F5. Card background: #FFFFFF. Primary text and borders: #111111. Secondary text: #6B7280. Borders: 1px solid #111111. Typography: Use 'Switzer' font family; Headings at font-weight 600, labels at font-weight 500 with letter-spacing 0.05em. Interactive states: When a card is hovered or focused, it should translate -2px on the Y-axis and gain a hard shadow: box-shadow: 4px 4px 0px 0px rgba(0,0,0,1). Use a 200ms ease-in-out transition for all state changes. Spacing: 24px (6 units) standard padding for sections, 20px (5 units) internal card padding.

## 5. Layout

A vertical mobile-first layout (max 375px) designed for infinite scroll. It follows a hierarchy of priority: Header -> Hero Card -> Repeating Stack -> Dense Grid -> Action Footer.

## 6. Components

- **Neubrutalist Interactive Card** — A white container with a sharp black border and a solid black shadow that appears on interaction.
- **Wireframe Bar Chart** — A minimalist data representation using simple geometric blocks.

## 7. Motion

REVIEW —
- Use a 200ms ease-in-out transition for all state changes
- Characterized by a 'neubrutalism-lite' aesthetic with heavy black borders, hard shadows on hover, and a strict grayscale palette

## 8. Voice & Brand

A high-contrast wireframe dashboard style featuring a modular card-based system. Characterized by a 'neubrutalism-lite' aesthetic with heavy black borders, hard shadows on hover, and a strict grayscale palette. It utilizes clean editorial typography (Switzer) and a minimalist approach to data visualization. Perfect for SaaS management tools, fintech mobile apps, developer dashboards, and productivity interfaces where structural clarity and modularity are prioritized over colorful decoration.

## 9. Anti-patterns

Must maintain strict grayscale; do not use accent colors except for specific status indicators (e.g., green for 'On Track'). Ensure all cards have the exact same 1px #111111 border to maintain the wireframe look. Use 'no-scrollbar' utility to keep the mobile UI clean. The hard-shadow on hover must not have a blur-radius (it should be a solid offset color).

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
