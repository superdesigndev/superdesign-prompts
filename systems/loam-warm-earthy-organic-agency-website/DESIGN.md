# Design System — Loam — Warm Earthy Organic Agency Website

> Category: Portfolios  ·  Industry: Agency & Studio
> Auto-scaffolded from prompt [`loam-warm-earthy-organic-agency-website`](../../prompts/loam-warm-earthy-organic-agency-website/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Warm earthy organic editorial. Grounded, handcrafted, slow-and-soft mood: sand/cream base (#efe7d8), terracotta primary action color (#c4633f), muted olive (#6b7048) and clay (#cf9a6f) accents, near-black warm ink for text (#2b251d). Fraunces serif for all headings (optical sizing, weights 600-700, with italics for emphasis), Inter for UI/body. Organic blobby radii (border-radius:'organic' = 2.5rem plus custom leaf-blob shapes), generous whitespace, soft layered shadows tinted by ink/terra, a faint radial-dot paper grain, and large blurred organic background washes behind sections.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#efe7d8`
- `#c4633f`
- `#6b7048`
- `#cf9a6f`
- `#2b251d`
- `#e6dac5`
- `#f6f0e4`
- `#a64f30`
- `#565a39`
- `#dcae84`
- `#5c5345`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design in a warm earthy organic editorial style. Palette: sand base #efe7d8 (darker sand #e6dac5, lighter sand #f6f0e4), terracotta primary #c4633f (dark #a64f30), olive #6b7048 (dark #565a39), clay #cf9a6f (light #dcae84), warm ink text #2b251d (soft #5c5345). Headings use the Fraunces serif (font-optical-sizing:auto, weights 600/700, italic for one emphasized phrase); body and UI use Inter (400-700). Use organic blob border-radii: a reusable 'organic' radius of 2.5rem on cards and the contact form, plus irregular leaf-blob radii (e.g. 64% 36% 57% 43% / 47% 56% 44% 53%) for the hero photo, about photo and large blurred background washes. Apply a faint paper grain via a radial-dot background (rgba(43,37,29,0.035) 1px dots on a 4px grid). Use soft, warm-tinted layered shadows (shadow-ink/20, shadow-terra/25). Buttons are fully rounded pills; eyebrow labels are uppercase with wide 0.22em l …

## 5. Layout

Single-column long-form landing page, max-width 7xl (80rem) container with px-6 / lg:px-10 gutters. Top-down order: sticky blurred header nav, hero (12-col grid: 6 copy / 6 organic photo), dark ink stats band (4 stats), Selected Work (4-up card grid), Services (4 intro col + 8 list col, numbered rows), About/Values (5 photo / 7 values with 3 cards), terracotta Contact block (6 copy / 6 form card), dark footer (4 columns + bottom bar). Sections alternate sand / sandhi / ink / terra backgrounds for rhythm. Responsive: grids collapse to 1-2 cols on mobile, nav links hide behind lg, blob washes clip via overflow-hidden.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

Warm earthy organic agency / studio website: sand + terracotta palette, Fraunces serif display type, organic leaf-blob shapes, sticky blurred nav, project-card grid, numbered services list, and a terracotta contact block with a mock prompt form.

## 9. Anti-patterns

Fonts loaded from Google Fonts: Fraunces (opsz 9..144, weights 400-800, serif display, optical sizing on) and Inter (400-700, sans UI/body). Styled with Tailwind via CDN using a custom theme palette (sand/sandlo/sandhi, terra/terradk, olive/olivedk, clay/claylo, ink/inksoft) and a custom 'organic' border radius. Photos are Unsplash earthy nature shots (soil, fields, foliage) with gradient overlays. html has scroll-behavior:smooth and overflow-x:hidden so the large blurred blobs never cause horizontal scroll. The mood must stay warm, grounded and handcrafted, never cold, neon or corporate.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
