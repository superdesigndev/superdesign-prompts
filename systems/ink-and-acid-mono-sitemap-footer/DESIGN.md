# Design System — Ink & Acid Mono Sitemap Footer

> Category: Forms & Contact  ·  Industry: General
> Auto-scaffolded from prompt [`ink-and-acid-mono-sitemap-footer`](../../prompts/ink-and-acid-mono-sitemap-footer/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Near-black 'ink' palette: page base #0a0c0b, surfaces #101413 (ink-900) and #161b19 (ink-850) at low opacity, raised tones #1c2321 / #283230. Acid-green accent ramp #5ff2a6 (acid-400), #27e08a (acid-500), #16c476 (acid-600) used for the wordmark glyph gradient, link hover, the primary send button, focus rings and the live status dot. Text is white at graded opacity (white, white/75, white/70, white/60). Fonts via Google Fonts: Space Grotesk for sans / body and JetBrains Mono for all labels, eyebrows, links-as-code, status text and legal. Mood: technical, confident, terminal-adjacent but premium; accents stay restrained (thin glows, 0.06-0.15 alpha green washes), never neon-flooded. Subtle grain via two faint radial green gradients in the corners and a hairline top border glow (transparent -> acid-500/40 -> transparent).

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#0a0c0b`
- `#101413`
- `#161b19`
- `#1c2321`
- `#283230`
- `#5ff2a6`
- `#27e08a`
- `#16c476`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

_none captured_

## 5. Layout

_REVIEW_

## 6. Components

_REVIEW: no components captured._

## 7. Motion

REVIEW —
- Acid-green accent ramp #5ff2a6 (acid-400), #27e08a (acid-500), #16c476 (acid-600) used for the wordmark glyph gradient, link hover, the primary send button, focus rings and the live status dot

## 8. Voice & Brand

A near-black ink footer with acid-green accents and mono labels: four link columns, a newsletter, a live status pill, and a giant ghost wordmark.

## 9. Anti-patterns

Frameless: render the footer alone with no browser chrome, device mockup, or window frame. Full-bleed background to the viewport edges while content stays in the 1240px container. The wordmark watermark and top hairline glow are pure decoration (pointer-events none, select none) and must clip cleanly at the footer edges. Keep text WCAG-legible against #0a0c0b (lightest body text stays at white/70 or above; acid green only on dark, never as body copy). Mono is for micro-copy and labels, not long sentences. Avoid generic indigo/violet SaaS slop, glassmorphism blur cards, and stock gradient blobs: the only color is the disciplined acid-green ramp on near-black ink.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
