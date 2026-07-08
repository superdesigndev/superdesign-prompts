# Design System — Editorial SaaS Onboarding

> Category: Onboarding  ·  Industry: SaaS
> Auto-scaffolded from prompt [`editorial-saas-onboarding`](../../prompts/editorial-saas-onboarding/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is 'Editorial Minimalist'—combining the structure of a modern application with the readability of a high-end magazine. It utilizes a warm neutral palette (Stone/Beige) instead of pure grays to create a 'calm' atmosphere. Key features include serif headings for a literary feel, tactile borders (1px) over drop shadows, and a muted terracotta accent for focus.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#F5F2EF`
- `#FAF9F6`
- `#E6E2DE`
- `#292524`
- `#78716C`
- `#A85338`
- `#FDF3F0`

## 3. Typography

- `Editorial Minimalist`
- `Crimson Pro`
- `Inter`
- `Satoshi`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a design system with a warm, editorial aesthetic. 

### Colors:
- **Backgrounds**: Main page bg: #F5F2EF (Stone-100); Sidebar bg: #FAF9F6 (Stone-50).
- **Borders**: Subtle 1px lines using #E6E2DE (Stone-200).
- **Typography**: Primary text #292524 (Stone-900); Secondary text #78716C (Stone-500).
- **Accent**: Muted Terracotta #A85338 for primary actions and active states; #FDF3F0 for light accent backgrounds.

### Typography:
- **Headings**: Serif font 'Crimson Pro'. Sizes: 48px (h1), 24px (h2). Weight: 400 (regular) or 600 (semibold). Line-height: 1.15.
- **UI & Body**: Sans-serif font 'Inter' or 'Satoshi'. Sizes: 14px (body/UI), 12px (labels), 18px (intro paragraphs). Weight: 400-500.

### Components & Effects:
- **Borders**: 1px solid #E6E2DE. Use rounded corners (8px) for cards.
- **Shadows**: Minimize shadows. Use a subtle 'Stone-200' shadow only on primary CTAs (e.g., `shado …

## 5. Layout

A classic dashboard layout with a fixed sidebar and header, where the central onboarding content is a long, naturally scrollable column focused on a single-column container.

## 6. Components

- **Interactive Mode Card** — Tall, vertically oriented cards used for primary selection.
- **Density Toggle** — A segmented control for UI density selection.

## 7. Motion

REVIEW —
- - **Animations**: Use 300ms transitions for hover states
- Scale icons by 10% on card hover

## 8. Voice & Brand

An editorial SaaS onboarding experience featuring a calm, sophisticated aesthetic. It uses a muted warm stone palette with terracotta accents, high-contrast serif headlines (Crimson Pro) paired with clean sans-serif UI text (Inter). The layout follows a natural document flow within a product shell, avoiding scroll-locks or overlays. Suitable for premium B2B SaaS, design tools, publishing platforms, and luxury fintech applications that prioritize a confident, professional, and non-intrusive user experience.

## 9. Anti-patterns

Must maintain a calm, quiet aesthetic; never use exclamation marks or 'hype' sales language. Ensure the page length is significant enough to require scrolling (min-height: 100vh). Use icons from a consistent thin-line set (like Lucide). Use natural document flow—do not hide content behind tabs if they can be scrolled through.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
