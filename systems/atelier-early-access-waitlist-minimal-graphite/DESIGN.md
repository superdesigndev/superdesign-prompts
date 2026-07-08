# Design System — Atelier · Early Access (waitlist-minimal-graphite)

> Category: Auth & Login  ·  Industry: SaaS
> Auto-scaffolded from prompt [`atelier-early-access-waitlist-minimal-graphite`](../../prompts/atelier-early-access-waitlist-minimal-graphite/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Strictly monochrome, editorial-minimal SaaS aesthetic. The canvas is warm off-white paper (#fbfbfa). All ink is near-black graphite #1c1c1e with a slightly lighter #2c2c2e for secondary fills and a single platinum grey #c7c7cc for tints; there is no color accent at all, the contrast IS the design. Type is Inter (weights 400-900); the hero headline is black-weight (900) with very tight tracking (-0.05em) and crushed ~0.92 leading, scaling up to ~5.25rem. Body text is graphite at graduated opacities (full for headings, ~65% for body/labels). Surfaces are white (#ffffff) or paper cards with hairline ink borders (ink at 6-10% opacity) and soft, low layered shadows (field-shadow: 0 1px 2px rgba(28,28,30,.04), 0 8px 24px -12px rgba(28,28,30,.18); btn-shadow deeper for the dark pill). The texture system: a faint dot-grain (radial-gradient #1c1c1e 0.5px dots on a 22px cell at ~4% opacity) plus large soft platinum/ink radial glows behind the hero, and 'stroke-deco' scattered short rotated graphite bars (monochrome confetti) replacing the reference's colored marks. Corners are soft (rounded-xl inputs/buttons, rounded-2xl cards, rounded-full pills/avatars). Selection is inverted (ink background, paper text). Everything reads soft, paper-like, confident and uncluttered.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#fbfbfa`
- `#1c1c1e`
- `#2c2c2e`
- `#c7c7cc`
- `#ffffff`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a minimal monochrome waitlist / early-access landing page. Use ONLY a graphite-on-paper palette: a warm off-white paper background #fbfbfa, near-black graphite ink #1c1c1e for type, accents, the dark CTA and the primary button, a slightly lighter graphite #2c2c2e for secondary fills, and one platinum grey #c7c7cc for tints; pure white #ffffff for input/card fills. No color accent whatsoever, the black-on-paper contrast is the whole look. Typography is Inter, weights 400 to 900: the hero headline is black (900) with very tight letter-spacing (-0.05em) and ~0.92 line-height, scaling from ~3.4rem to ~5.25rem; section headings are extrabold/black; eyebrows and labels are 12px uppercase with wide ~0.14-0.16em tracking in ink at 65%; body is 14-18px in ink at ~65%. Surfaces are white or paper with hairline borders (ink at 6-10% opacity) and soft low shadows (0 1px 2px rgba(28,28,30,.04) …

## 5. Layout

A full single-scroll landing: a slim sticky glass nav, a tall centered hero/waitlist section, a logo trust strip, a 3-step 'how it works' grid, a full-bleed dark closing CTA, and a footer. The hero is centered in a narrow max-w-3xl column (eyebrow pill, headline, subcopy, a one-row email+button form, then a social-proof avatar stack + count) over a full-bleed textured background with glows and scattered graphite strokes. The other sections center their content in a max-w-6xl container. The defining structural moves: the centered single-field waitlist form with overlapping social-proof avatars, and the monochrome scattered-stroke hero background.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

Minimal monochrome graphite-on-paper waitlist / early-access landing for an AI design tool: a warm off-white ground with near-black ink and one platinum grey (no color accent), a big tight black-weight headline, a centered single-field email + button waitlist form with overlapping social-proof avatars, scattered graphite confetti strokes, a logo trust strip, a 3-step how-it-works grid and an inverted full-bleed dark closing CTA.

## 9. Anti-patterns

Keep it STRICTLY monochrome: build everything from the paper #fbfbfa ground, graphite ink #1c1c1e (type, the primary button, the dark CTA section), a secondary #2c2c2e fill, and one platinum grey #c7c7cc; pure white #ffffff only for input/card fills. Do NOT introduce any color accent, the black-on-paper contrast is the entire design (the reference's colored confetti strokes must be recolored to graphite/platinum). Use Inter throughout: the hero headline must be black-weight (900) with very tight tracking (-0.05em) and crushed ~0.92 leading, scaling up to ~5.25rem; eyebrows/labels are 12px uppercase with wide ~0.14-0.16em tracking. Text is graphite at graduated opacities (full headings, ~65% body/labels), never a different hue. The hero is the centerpiece: a centered narrow max-w-3xl column (eyebrow pill -> big headline -> subcopy -> single-row email+button form -> overlapping avatar stack + count) over the textured background (dot-grain + soft platinum/ink glows + scattered graphite strokes). Depth is soft: hairline 1px borders in ink at 6-10%, rounded-xl inputs/buttons and rounded-2xl cards, soft low layered shadows (no hard edges). The page is a full single-scroll landing (sticky glass nav, hero/waitlist, logo trust strip, 3-step how-it-works grid, an inverted full-bleed dark closing CTA repeating the capture, footer); the hero centers in max-w-3xl and the rest in max-w-6xl. Everything must reflow cleanly: the email+button forms stack below sm, the nav center links hide below md and 'Sign in' below sm, the trust strip and how-it-works grid wrap/stack, the headline scales 3.4rem->5.25rem, no horizontal overflow at 390px. Copy is warm and human with zero em-dashes.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
