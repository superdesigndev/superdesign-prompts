# Design System — Plume · Sign in to your design canvas

> Category: Auth & Login  ·  Industry: SaaS
> Auto-scaffolded from prompt [`plume-sign-in-to-your-design-canvas`](../../prompts/plume-sign-in-to-your-design-canvas/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Soft, rounded, friendly SaaS aesthetic in a sky-blue + coral palette on a near-white cloud background. Heavy use of large border radii (2rem / 2.75rem), layered soft shadows with sky-tinted glows, blurred floating blobs, a faint blue dot-grid, and a hand-drawn coral underline accent. Typography is the rounded Nunito family pushed to very heavy weights (800-900) for warmth and confidence.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#f7fbff`
- `#38bdf8`
- `#0ea5e9`
- `#0284c7`
- `#0369a1`
- `#0c4a6e`
- `#f0f9ff`
- `#e0f2fe`
- `#bae6fd`
- `#7dd3fc`
- `#fda4af`
- `#fb7185`
- `#f43f5e`
- `#e11d48`
- `#0f2030`
- `#33485c`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a friendly, rounded SaaS landing-plus-auth page. Palette: cloud near-white background #f7fbff; primary sky blues sky-400 #38bdf8, sky-500 #0ea5e9, sky-600 #0284c7, sky-700 #0369a1, deep sky-900 #0c4a6e, light sky-50 #f0f9ff / sky-100 #e0f2fe / sky-200 #bae6fd / sky-300 #7dd3fc; coral accents coral-300 #fda4af, coral-400 #fb7185, coral-500 #f43f5e, coral-600 #e11d48; ink text ink-900 #0f2030 (headings), ink-700 #33485c (body strong), ink-500 #5b7184 (muted). Typography: Nunito (Google Font) for everything, weights 600-900, very heavy 900 for headings and buttons, tight tracking on large headings. Shapes: large rounded corners everywhere (rounded-2xl through rounded-5xl = 2rem/2.75rem), pill buttons, soft sky-tinted shadows (e.g. 0 24px 60px -22px rgba(56,189,248,0.45) for primary, 0 40px 90px -30px rgba(15,32,48,0.30) for cards). Texture: subtle radial dot-grid (sky dots at 22px sp …

## 5. Layout

Single vertical scroll, all sections centered in a max-width 72rem (max-w-6xl) container with px-5 / sm:px-8 gutters. Order top-to-bottom: sticky nav, full-bleed hero with two-column pitch + sign-in card, logo strip, three-up feature grid, full-bleed gradient showcase band, centered CTA card, dark footer. The hero uses an asymmetric 1.05fr / 1fr two-column grid on large screens and stacks to a single centered column on mobile.

## 6. Components

- **Two-panel side-panel sign-in card** — 
- **Auth form fields** — 
- **Primary submit + social auth** — 
- **Floating ambient decoration** — 

## 7. Motion

REVIEW —
- Texture: subtle radial dot-grid (sky dots at 22px spacing, ~20-60% opacity) and several large blurred pastel circles floating with slow ease-in-out animations

## 8. Voice & Brand

Warm, illustrated AI design-agent sign-in landing in sky-blue and coral: a sticky frosted nav over a two-panel side-panel login card (gradient illustration aside plus email, password and social auth), floating blobs, dot-grid texture and rounded-everything Nunito type.

## 9. Anti-patterns

Fonts: Nunito only (Google Fonts, weights 400-900 + italic 700). Built with Tailwind (CDN) using a custom theme: sky/coral/ink/cloud color scales (exact hex above), borderRadius 4xl=2rem & 5xl=2.75rem, and three named shadows soft/card/lift. Icons are Phosphor via iconify-icon (ph:feather-fill, ph:sparkle-fill, ph:arrow-right-bold, ph:envelope-simple-bold, ph:lock-simple-bold, ph:eye-bold, ph:shield-check-fill, etc.) plus logos:google-icon. No em-dashes anywhere in the copy (it's even a footer joke). Voice is warm and human. Animations are pure CSS keyframes; respect the playful-but-restrained motion. Fully responsive: hero collapses from a 1.05fr/1fr grid to a single centered column, the card's two panels stack below sm, and the feature/showcase grids reflow to one column on mobile.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
