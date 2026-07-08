# Design System — Minimalist Beta Capture

> Category: Waitlist & Coming Soon  ·  Industry: General
> Auto-scaffolded from prompt [`minimalist-beta-capture`](../../prompts/minimalist-beta-capture/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style essence is 'Modern Obsidian'. It pairs high-impact serif italics with technical monospace and functional sans-serif. The palette is strictly monochromatic (#080808 to #FFFFFF) with silver gradients. Layouts use extreme spacing (fluid 92vw) and a noise-textured background to create depth without color. Animation is purposeful, using cubic-bezier curves for slide-up entry and smooth transitions.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#080808`
- `#FFFFFF`
- `#E2E8F0`
- `#F8FAFC`
- `#94A3B8`

## 3. Typography

- `Modern Obsidian`
- `DM Serif Display`
- `Geist Mono`
- `Inter`
- `Editorial Brutalist`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

### Core Style Specs
- **Palette**: Obsidian Background (#080808), Pure White (#FFFFFF), Silver Text (#E2E8F0), Silver Gradient (linear-gradient 135deg, #F8FAFC 0%, #94A3B8 100%).
- **Typography**:
  - **Serif (Headlines)**: 'DM Serif Display', italicized, tracking-tighter, leading-0.85. Hero size: clamp(42px, 10vw, 140px).
  - **Mono (System/UI)**: 'Geist Mono', weight 100-900. Used for labels, buttons, and metadata at 10px-14px. Tracking: 0.2em to 0.5em uppercase.
  - **Sans (Body)**: 'Inter', weight 300-600. Used for readability at 14px-18px.
- **Borders & Corners**: Border color `rgba(255, 255, 255, 0.08)`. Hero radius: 4rem (desktop), 2rem (mobile). Card radius: 1rem (16px).
- **Effects**:
  - **Noise**: SVG fractal noise overlay at 0.05 opacity.
  - **Glass**: `background: rgba(255, 255, 255, 0.02)`, `backdrop-filter: blur(24px)`.
  - **Buttons**: Silver gradient background, black  …

## 5. Layout

The page follows a vertical narrative flow: Navigation -> Explosive Hero -> Data Metadata -> Capture Form -> Urgency/Social Proof -> Feature Bento -> Value Proposition -> Testimonials -> Final CTA -> Footer.

## 6. Components

- **Countdown Timer** — Editorial style countdown with serif numerals and slash separators.
- **Floating Mobile Bottom Nav** — A pill-shaped navigation bar that appears only after the hero section is passed.
- **Member Registry Card** — A bento card showing small user badges with hover interactions.

## 7. Motion

REVIEW —
- - **Buttons**: Silver gradient background, black text, 1px lift on hover with `box-shadow: 0 0 20px rgba(255,255,255,0
- 8s duration)

## 8. Voice & Brand

A high-end 'Editorial Brutalist' style guide optimized for SaaS waitlists, fintech, or premium developer tools. It features a dark-mode palette (#080808), high-contrast monochromatic typography (DM Serif Display + Geist Mono), and sophisticated glassmorphism. The layout utilizes a bento-grid structure and fluid width (92vw) with oversized hero typography. Key features include scroll-triggered slide-up animations, a silver-metallic gradient system, and a persistent floating mobile navigation bar.

## 9. Anti-patterns

MUST maintain the strict monochrome/silver palette; any standard colors (blue, red, green) will break the premium aesthetic. MUST use 'Geist Mono' for all technical labels to maintain the 'engineered' feel. MUST use fluid width (92vw) instead of standard Tailwind containers to maximize editorial impact. MUST NOT use standard box-shadows; use borders or backdrop-blurs for depth. MUST NOT use non-italicized serif for headlines.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
