# Design System — Interactive Multi-Step Onboarding Flow

> Category: Onboarding  ·  Industry: General
> Auto-scaffolded from prompt [`interactive-multi-step-onboarding-flow`](../../prompts/interactive-multi-step-onboarding-flow/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The design follows a 'clean-tech' aesthetic using the Switzer font family (font-sizes ranging from 12px labels to 32px headers). It employs a neutral grayscale palette dominated by Slate (#0F172A) and off-whites (#F8FAFC). Animations are snappy yet smooth, using a custom cubic-bezier timing function for all state transitions and sliding effects.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#0F172A`
- `#F8FAFC`
- `#64748B`
- `#94A3B8`
- `#E2E8F0`
- `#FFFFFF`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a design system using the Switzer font family. Color Palette: Primary Slate-900 (#0F172A) for headings and primary buttons; Secondary Slate-500 (#64748B) for body text; Accents in Slate-400 (#94A3B8) and Slate-200 (#E2E8F0); Backgrounds in Slate-50 (#F8FAFC) and pure white (#FFFFFF). Typography: H1 headers at 32px, leading-tight (1.1), tracking-tight; Labels at 12px, bold, uppercase, tracking-widest. Spacing: Standardized 24px (6 units) padding for containers. Animation: Use 'cubic-bezier(0.16, 1, 0.3, 1)' for all sliding movements with a 600ms duration. Buttons should have a subtle active scale effect (0.98) and soft drop shadows (shadow-lg with slate-200 color).

## 5. Layout

A vertical stack consisting of a fixed navigation header, a flex-1 sliding content viewport, and a fixed primary action footer. The content slides on a 400% width container divided into four 100vw sections.

## 6. Components

- **Interactive Selection Card** — A card that combines visual icons with checkbox logic for multi-select preferences.
- **Sliding Viewport Container** — The core navigation mechanic that handles step transitions.

## 7. Motion

REVIEW —
- 3, 1)' for all sliding movements with a 600ms duration

## 8. Voice & Brand

A minimalist, high-end multi-step onboarding flow designed for mobile-first SaaS and lifestyle applications. Characterized by a sophisticated Slate-based color palette (#0F172A), premium typography using the Switzer typeface, and fluid horizontal sliding transitions. Key features include a bento-grid interest selector, animated toggle switches, and a persistent progress-tracking header. Suitable for fintech, creative portfolios, productivity tools, and modern web platforms requiring a seamless user registration experience.

## 9. Anti-patterns

Must maintain a strict whitespace-heavy layout to ensure a premium feel. Do not use bright colors outside of the grayscale/slate spectrum. The 'Continue' button text and icon must update on the final step to signal completion (e.g., 'Get Started' with a rocket icon). Ensure all interactive elements have hover/active states using transition-all with 200ms duration.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
