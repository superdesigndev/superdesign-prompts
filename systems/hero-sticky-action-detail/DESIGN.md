# Design System — Hero + Sticky Action Detail

> Category: Mobile Apps  ·  Industry: General
> Auto-scaffolded from prompt [`hero-sticky-action-detail`](../../prompts/hero-sticky-action-detail/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is defined by its 'Satoshi' sans-serif typography, ranging from extra-bold headers to wide-tracked uppercase tags. The color palette is strictly grayscale (using Tailwind's gray-50 through gray-900) with a focus on tactile interaction through subtle scale transforms and backdrop blurs. Shadows are minimal, relying instead on 1px borders (#E5E7EB) and background shifts for depth.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#E5E7EB`
- `#FFFFFF`
- `#F9FAFB`
- `#71717A`
- `#111827`

## 3. Typography

- `Satoshi`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a design system using the 'Satoshi' font family. Use a grayscale color palette: White (#FFFFFF), Ghost White (#F9FAFB), Platinum (#E5E7EB), Slate Gray (#71717A), and Onyx (#111827). Typography: Headers use 700-900 weight with tight tracking (-0.025em), labels use 500 weight with wide tracking (0.1em). Corners should be rounded with '2xl' (16px) or 'full' radius. Apply backdrop-filter: blur(12px) to fixed elements. Animations should use 'active:scale-95' for haptic feedback and cubic-bezier(0.4, 0, 0.2, 1) for transitions.

## 5. Layout

A vertical scrollable container with a fixed top navigation and a sticky bottom action bar. The content flows from a large visual hero into a structured information hierarchy.

## 6. Components

- **Haptic Button** — A button that provides visual feedback on tap.
- **Geometric Variant Card** — A rich variant selector card with visual and text cues.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

Features a fixed action bar with safe-area anchoring, 4:5 hero visuals, and subtle glassmorphism effects on floating elements. Ideal for luxury retail, furniture showcases, editorial commerce, and minimalist lifestyle apps.

## 9. Anti-patterns

MUST use Satoshi or a similar high-quality geometric sans-serif. MUST ensure the bottom action bar includes the iOS/Android safe area padding to prevent overlap with home indicators. DO NOT use vibrant colors; stick to the grayscale palette except for very specific functional icons (rating stars, heart). MUST use backdrop blurs for all fixed overlays to maintain the 'glass' feel.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
