# Design System — Chronological Content Feed

> Category: Blog & Editorial  ·  Industry: E-commerce & Retail
> Auto-scaffolded from prompt [`chronological-content-feed`](../../prompts/chronological-content-feed/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is minimalist and high-contrast, utilizing 'General Sans' as the primary font with weights ranging from 400 to 700. The color palette is strictly grayscale: White (#FFFFFF) background, Dark Gray (#111827) for headings and primary text, and Medium Gray (#4B5563) for body text and metadata. Visual interest is generated through large heading sizes (4xl to 5xl), tracking-tight letter spacing, and subtle hover states like 1px underlines with 4px offsets. Transitions are smooth and subtle, focusing on color and text-decoration changes.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#FFFFFF`
- `#111827`
- `#4B5563`
- `#6B7280`
- `#F3F4F6`
- `#E5E7EB`
- `#9CA3AF`

## 3. Typography

- `General Sans`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Apply a minimalist editorial style using 'General Sans' font family. Background must be #FFFFFF. Text colors: Primary #111827, Secondary #4B5563, Metadata/Dates #6B7280. Headlines should use font-size: 3rem (48px) with -0.025em tracking-tight. Post titles should be 1.5rem (24px) with font-weight: 500. Borders and dividers should be #F3F4F6 or #E5E7EB with a 1px thickness. Images must maintain a 3:2 aspect ratio with a #F3F4F6 light gray background and centered Lucide-style icons in #9CA3AF. Hover effects on titles should trigger a 1px underline with a 4px offset. Animation: all transitions (colors, backgrounds) should use ease-in-out over 200ms.

## 5. Layout

The layout is a single-column container centered on the page with a maximum width of 896px. It follows a top-down hierarchy: a centralized hero header, a vertical list of blog articles separated by horizontal rules, and a functional bottom pagination bar.

## 6. Components

- **Interactive Article Heading** — A title that utilizes CSS text-decoration-thickness and underline-offset for a sophisticated hover effect.
- **Minimal Image Placeholder** — Structured placeholder box representing future photography.

## 7. Motion

REVIEW —
- Visual interest is generated through large heading sizes (4xl to 5xl), tracking-tight letter spacing, and subtle hover states like 1px underlines with 4px offsets
- Hover effects on titles should trigger a 1px underline with a 4px offset
- Animation: all transitions (colors, backgrounds) should use ease-in-out over 200ms

## 8. Voice & Brand

A straightforward vertical list of blog posts ordered by date. Each entry includes a thumbnail placeholder, title, excerpt, and metadata. Optimized for reading flow and content discovery over time.

Best suited for
Content marketing blogs, product updates, founder blogs, SEO-driven publishing.

## 9. Anti-patterns

MUST: Maintain strict 3:2 aspect ratio for all thumbnails to ensure editorial consistency. MUST: Use 'General Sans' or a similar geometric sans-serif to preserve the clean aesthetic. MUST NOT: Use any shadows or gradients; depth should be created solely through border contrasts and grayscale tones. MUST: Ensure the 'Read Article' text and the Arrow icon are perfectly aligned horizontally.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
