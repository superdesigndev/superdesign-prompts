# Design System — Aurora Glass — Sign in to the canvas

> Category: Auth & Login  ·  Industry: SaaS
> Auto-scaffolded from prompt [`aurora-glass-sign-in-to-the-canvas`](../../prompts/aurora-glass-sign-in-to-the-canvas/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Dark glassmorphism with a vivid aurora gradient system. Near-black ink canvas (#0b0f14), frosted translucent surfaces with heavy backdrop-blur and a 1px white hairline border, neon aqua (#2dd4bf) and magenta (#e879f9) as the only accent hues, applied as soft radial blobs, gradient text, and a multi-stop CTA. Type pairs Space Grotesk (display) with Inter (body). High contrast, calm spacing, subtle inset highlights and deep drop shadows give the glass a real lift.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#0b0f14`
- `#2dd4bf`
- `#e879f9`
- `#ccfbf1`
- `#5eead4`
- `#0f766e`
- `#fbe9ff`
- `#f0abfc`
- `#a21caf`
- `#38bdf8`
- `#6366f1`
- `#312e81`

## 3. Typography

- `Space Grotesk`
- `Inter`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a premium dark glassmorphism aesthetic. Background: solid ink #0b0f14 (color-scheme: dark). Scatter 4-5 large soft blurred radial 'aurora' blobs (border-radius:9999px, filter blur ~4px) in three palettes: aqua [radial #ccfbf1->#5eead4->#2dd4bf->#0f766e], magenta [#fbe9ff->#f0abfc->#e879f9->#a21caf], deep [#38bdf8->#6366f1->#312e81], at varied opacities .32-.78. Over them add a masked grid veil (64px lines in rgba(45,212,191,.05) and rgba(232,121,249,.05), radial-ellipse mask fading to transparent) and a fine film grain (3px radial dots, opacity .5), then two darkening overlays so the center stays legible and edges sink to ink. Surfaces are glass: linear-gradient(155deg, rgba(255,255,255,.085), rgba(255,255,255,.025)), backdrop-filter blur(34px) saturate(140%), 1px rgba(255,255,255,.12) border, box-shadow with an inset top highlight (0 1px 0 rgba(255,255,255,.18) inset) plus a 0 30 …

## 5. Layout

Single full-height page, max-width 7xl (1280px) centered with px-6/px-8 gutters. A fixed translucent header nav. The hero is a 2-column grid on lg (left pitch / right card), stacking to one column on mobile with the card ordered first. Below the fold: a full-bleed trust logo strip, then a minimal footer. Everything sits over the shared aurora background layer.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

REVIEW —
- 22s transitions on hover/focus

## 8. Voice & Brand

Dark aurora-glass split sign-in screen: frosted glassmorphic auth card with a glowing aqua focus ring and an aqua-to-magenta gradient CTA, floating over neon aurora blobs on near-black ink, beside a product pitch column. Space Grotesk + Inter.

## 9. Anti-patterns

Color tokens (exact): ink #0b0f14, aqua #2dd4bf (light #5eead4), magenta #e879f9; blob deep stops #38bdf8/#6366f1/#312e81. Fonts: Space Grotesk (display, 400-700) + Inter (body, 400-700), loaded from Google Fonts; phosphor + logos icon sets via Iconify. Built on Tailwind (CDN) with custom utility classes (.aurora/.glass/.glass-nav/.field/.cta/.social-btn/.pill/.gradient-text/.check/.divider-line). Keep accents strictly aqua + magenta. The password field is intentionally rendered focused to showcase the glow ring. Fully responsive: 2-col on lg collapsing to a single stacked column on mobile with the auth card moved to the top. color-scheme: dark, antialiased, smooth scroll.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
