# Design System — Neon Velocity Countdown

> Category: Waitlist & Coming Soon  ·  Industry: General
> Auto-scaffolded from prompt [`neon-velocity-countdown`](../../prompts/neon-velocity-countdown/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is built on a high-contrast foundation of deep blacks (#050505) and vibrant neon lime (#BFFF00). It employs 'Plus Jakarta Sans' (800 weight) for heavy, tightly-tracked headlines and 'Geist Mono' for technical, wide-tracked labels. Key visual techniques include 3D perspective transforms, grain/noise overlays for texture, and luminosity-based hover states that make components feel light-emitting.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#050505`
- `#BFFF00`
- `#FFFFFF`

## 3. Typography

- `Plus Jakarta Sans`
- `Geist Mono`
- `Inter`
- `Laser Green`
- `Navy Black`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

### Core Aesthetics
- **Color Palette**: Primary Background: `#050505`; Accent Green: `#BFFF00`; Text Primary: `#FFFFFF`; Text Secondary: `rgba(255, 255, 255, 0.4)`; Borders: `rgba(255, 255, 255, 0.1)`.
- **Typography**:
  - **Headlines**: 'Plus Jakarta Sans', weight 800, tracking -0.05em, uppercase. Fluid sizing: `clamp(2.6rem, 10vw, 8.75rem)`.
  - **Technical Meta**: 'Geist Mono', weight 400-600, tracking 0.2em to 0.5em, uppercase, font-size: 10px-12px.
  - **Body**: 'Inter', weight 300-400, leading-relaxed.
- **Visual Effects**:
  - **Noise Overlay**: Subtle SVG fractal noise at 3% opacity fixed to the viewport.
  - **Refraction Glow**: Large, blurred radial gradients (`#BFFF00` at 15% opacity) acting as background ambiance.
  - **Glassmorphism**: `backdrop-filter: blur(12px)` with 1px solid white borders at 8% opacity.
- **Animations**: Use `cubic-bezier(0.16, 1, 0.3, 1)` for all tra …

## 5. Layout

The layout is a single-column flow with wide containers (max-width 1600px). It uses a '3D Glass' background to anchor the hero and a modular bento-grid for feature sections.

## 6. Components

- **Laser Button** — A high-energy interactive button with a sweeping light effect.
- **Luminosity Card** — A responsive container that reacts to mouse proximity with light.

## 7. Motion

REVIEW —
- Key visual techniques include 3D perspective transforms, grain/noise overlays for texture, and luminosity-based hover states that make components feel light-emitting

## 8. Voice & Brand

A high-velocity, futuristic dark-mode design system characterized by neon accents, brutalist typography, and 3D glassmorphism. Featuring a 'Laser Green' and 'Navy Black' palette, it utilizes 'Plus Jakarta Sans' for high-impact headlines and 'Geist Mono' for technical metadata. This aesthetic is ideal for high-growth tech startups, SaaS platforms, developer tools, and fintech products that want to convey speed, precision, and cutting-edge innovation. The layout uses a bento-grid structure, fluid typography, and sophisticated scroll-triggered reveal animations.

## 9. Anti-patterns

MUST: Use uppercase for all technical labels and headlines to maintain the brutalist feel. MUST: Use `tabular-nums` for the countdown to prevent horizontal layout shift during ticks. MUST: Maintain a minimum touch target of 48px for the mobile bottom nav buttons. DO NOT: Use standard rounded corners on the large Hero border-box; keep them sharp (0px) to contrast with the rounded cards below. DO NOT: Use pure black (#000) for backgrounds; stick to the slightly lighter `#050505` to allow the noise texture to be visible.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
