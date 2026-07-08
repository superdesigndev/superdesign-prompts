# Design System — BabyBites - Sophisticated Palette

> Category: Mobile Apps  ·  Industry: General
> Auto-scaffolded from prompt [`babybites-sophisticated-palette`](../../prompts/babybites-sophisticated-palette/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is defined by its 'Sophisticated Playful' aesthetic. It uses Nunito as its primary typeface across all weights (400-900) to create clear hierarchy. The color palette uses Charcoal (#171e19) for primary text and backgrounds, Vibrant Red (#ca0013) for high-impact CTAs, and Gray-Green (#b7c6c2) for borders and secondary labels. Soft shadows (0_20px_50px_-12px_rgba(0,0,0,0.08)) and glassmorphism-lite effects on cards create depth.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#171e19`
- `#ca0013`
- `#b7c6c2`
- `#eeebe3`
- `#ffffff`

## 3. Typography

- `Sophisticated Playful`
- `Nunito`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Apply a sophisticated color palette: Charcoal (#171e19), Gray-Green (#b7c6c2), Vibrant Red (#ca0013), Off-White (#eeebe3), and White (#ffffff). Typography: Use 'Nunito' for all text; Headings at 32px/Font-Black, Subheadings at 20px/Font-Black, Labels at 10px/Font-Bold with uppercase tracking. UI Elements: Use border-radius of 40px (2.5rem) for main cards and 24px (1.5rem) for nested items. Borders should be 1px solid #b7c6c2 at 20-30% opacity. Animations: Implement view-transitions with a 0.25s ease-in/out fade. Buttons: Primary CTAs in Red, secondary in White with gray-green borders. Shadows: Use subtle large-spread shadows for depth.

## 5. Layout

A mobile-first, single-column layout with a fixed floating navigation bar. The structure prioritizes contextual discovery via a horizontal scrollable selector and a high-impact hero section for primary content.

## 6. Components

- **Floating Center Action Button** — A high-visibility floating action button (FAB) integrated into the navigation bar.
- **Bento Metric Card** — Small information cards used for displaying specific data points within a larger section.

## 7. Motion

REVIEW —
- 25s ease-in/out fade

## 8. Voice & Brand

BabyBites style guide featuring a sophisticated high-contrast palette of dark charcoal, vibrant red, and sage-green. Characterized by playful but professional editorial typography, oversized rounded corners (up to 40px), and a clean, card-based layout. Ideal for parenting, nutrition, healthcare, and educational SaaS platforms. Includes scroll-triggered animations and custom view transitions for fluid mobile-first navigation.

## 9. Anti-patterns

MUST use #ca0013 exclusively for actions and critical alerts to maintain its semantic weight. MUST NOT use pure black; always substitute with #171e19 Charcoal. MUST maintain the oversized 40px border-radius on main containers to preserve the signature 'soft but modern' look. MUST ensure all icons are visually balanced within circular or square containers.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
