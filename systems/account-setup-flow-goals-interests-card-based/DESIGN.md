# Design System — Account Setup Flow — Goals / Interests (Card-Based)

> Category: Mobile Apps  ·  Industry: General
> Auto-scaffolded from prompt [`account-setup-flow-goals-interests-card-based`](../../prompts/account-setup-flow-goals-interests-card-based/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Modern minimalist aesthetic utilizing 'General Sans' for a clean, editorial look. Palette is strictly monochrome: Pure White (#FFFFFF), Deep Black (#000000), and a range of functional grays (#F3F4F6 for backgrounds, #9CA3AF for secondary text). Animations use the View Transitions API with custom slide-up keyframes and cubic-bezier(0.16, 1, 0.3, 1) easing for a 'snappy' but smooth feel.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#FFFFFF`
- `#000000`
- `#F3F4F6`
- `#9CA3AF`
- `#E5E7EB`
- `#6B7280`

## 3. Typography

- `General Sans`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a design system with a monochrome high-contrast theme. 
- **Typography**: Use 'General Sans'. Headings should be font-weight: 700 (Bold) with tracking: -0.025em. Body text should be font-weight: 400 or 500 (Medium). Labels should be uppercase with tracking: 0.05em.
- **Colors**: Primary Background: #FFFFFF; Primary Action: #000000; Secondary Background: #F3F4F6; Border: #E5E7EB; Secondary Text: #6B7280; Subtitle: #9CA3AF.
- **Interactions**: Buttons and cards should have a scale-down effect on click (scale: 0.95 or 0.98). Transitions between steps must use a slide-up animation (20px to 0px) with opacity fade (0 to 1) over 500ms using cubic-bezier(0.16, 1, 0.3, 1).
- **Shadows**: Use a subtle upward shadow for the footer: shadow-[0_-4px_20px_rgba(0,0,0,0.03)]. Primary CTA button should have a drop shadow: shadow-lg shadow-gray-200.

## 5. Layout

A vertically stacked mobile layout consisting of a persistent progress bar at the very top, a fixed header with contextual titles, a scrollable main content area for user input, and a fixed footer with the primary action button.

## 6. Components

- **Selection Card** — An interactive card that serves as a single or multiple choice input.
- **Toggle Switch** — A custom push-notification style toggle.

## 7. Motion

REVIEW —
- Features high-contrast black and white aesthetics, modern typography using General Sans, and fluid motion using the View Transitions API

## 8. Voice & Brand

A sleek, minimalist, and highly interactive 4-step onboarding flow designed for mobile-first experiences. Features high-contrast black and white aesthetics, modern typography using General Sans, and fluid motion using the View Transitions API. Ideal for SaaS, fintech, or lifestyle apps needing a premium, frictionless user registration or configuration sequence. Key elements include a persistent progress bar, springy micro-interactions, and clear, bold editorial typography.

## 9. Anti-patterns

MUST maintain the high-contrast ratio for accessibility. DO NOT use rounded-full for the main CTA; use rounded-xl (12px) for a more modern 'app' feel. Transitions MUST be synchronized so that the progress bar, header text, and main content animate together using the View Transitions API or equivalent motion library. MUST include an active scale effect on all clickable elements to provide tactile feedback.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
