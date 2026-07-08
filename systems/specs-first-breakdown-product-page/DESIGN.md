# Design System — Specs-First Breakdown Product Page

> Category: E-commerce  ·  Industry: E-commerce & Retail
> Auto-scaffolded from prompt [`specs-first-breakdown-product-page`](../../prompts/specs-first-breakdown-product-page/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is defined by a 'Tech-Blueprint' aesthetic. It uses a primary typeface of General Sans for UI readability and JetBrains Mono for technical data and labels. The color palette is strictly neutral (#FFFFFF background, #171717 text, #E5E5E5 borders). Design elements use diagonal hatching patterns for placeholders and 1px solid borders to create a structural, wireframe feel without looking unfinished.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#FFFFFF`
- `#171717`
- `#E5E5E5`
- `#f5f5f5`

## 3. Typography

- `General Sans`
- `JetBrains Mono`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a design with a strict grayscale wireframe aesthetic. Background: #FFFFFF. Text: #171717 (Neutral-900). Borders: 1px solid #E5E5E5 (Neutral-200). Typography: Use 'General Sans' for headings and primary UI; use 'JetBrains Mono' at 12px-14px for technical specs, prices, and SKU identifiers. Placeholder elements must feature a diagonal stripe pattern using `repeating-linear-gradient(45deg, transparent, transparent 10px, #f5f5f5 10px, #f5f5f5 20px)`. Buttons: Primary is solid #171717 with white text; secondary is white with #E5E5E5 border. Micro-interactions: Use scale(0.99) for active button states and 0.3s cubic-bezier for hover transitions. Borders should be used to define all sections (border-b and border-r patterns).

## 5. Layout

A top-down structured layout within a fixed max-width container (1440px) with explicit vertical border boundaries. Content is organized in high-density sections separated by horizontal lines.

## 6. Components

- **Wireframe Placeholder** — Functional image substitute with technical meta-data.
- **Segmented Control Toggle** — A brutalist tab/toggle switcher.

## 7. Motion

REVIEW —
- 3s cubic-bezier for hover transitions

## 8. Voice & Brand

Information-dense layout with a prominent specification table beneath the primary product info. Prioritizes structured data, clarity, and comparison readiness.

Best suited for
Electronics, hardware, supplements, tools, B2B products, technically informed buyers.

## 9. Anti-patterns

MUST: Maintain perfect alignment with a 1px border grid. MUST: Use Monospace font for any and all numerical data (price, SKU, dimensions). MUST NOT: Use border-radius; all corners must be sharp 0px or very minimal 2px. MUST NOT: Use drop shadows except for very subtle hover effects on comparison cards.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
