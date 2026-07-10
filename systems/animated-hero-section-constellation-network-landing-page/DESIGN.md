# Design System — Animated Hero Section: Constellation Network Landing Page

> Category: Landing Pages  ·  Industry: General
> Auto-scaffolded from prompt [`animated-hero-section-constellation-network-landing-page`](../../prompts/animated-hero-section-constellation-network-landing-page/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Cool-neutral, editorial, single-accent hero minimalism with motion — a crisp 2026 SaaS/AI landing hero, not a 2015 dark particle cliché. A pale cool canvas #f4f6f2 with near-black ink #0d1211 and muted #5f6b64; hierarchy comes from an aggressive type scale (a ~72px Space Grotesk display headline against ~12.5px tracked caps eyebrows/labels) and from left-aligned editorial rhythm, never from color. Color is rationed to a SINGLE acid-lime accent #a3e635 (deeper #84cc16 for dark-text contrast) confined to the primary CTA, the eyebrow dot, the headline highlight sweep, and one glowing 'live' node cluster — everything else is ink / muted / hairline. TWO typefaces by role: Space Grotesk (display headline + wordmark, tight negative tracking) and Inter (nav, subhead, labels, buttons). The shape language is flat and airy: pill CTAs, hairline nav divider, generous negative space, and a full-bleed animated node-network that stays subtle behind the copy. Motion is quiet and pure-CSS (drifting/breathing layers, a gently pulsing accent cluster) — animated-feeling but calm, and legible with motion disabled. The mood is confident, techy, and premium without a single gradient or frosted panel.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#f4f6f2`
- `#0d1211`
- `#5f6b64`
- `#a3e635`
- `#84cc16`

## 3. Typography

- `Read the docs`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design an animated landing-page hero in a cool-neutral, single-accent register. Use a pale cool canvas #f4f6f2 (NOT warm ivory, NOT pure white), ink #0d1211, muted #5f6b64, and hairlines rgba(13,18,17,0.10). Ration color to a SINGLE acid-lime accent #a3e635 (use deeper #84cc16 where dark text sits on lime) — use it ONLY for the primary CTA fill (ink text), the small eyebrow status dot, a translucent highlight sweep behind the second headline line, and one glowing 'live' node cluster in the background. Set the display headline and wordmark in Space Grotesk (big ~72px, line-height ~1.02, letter-spacing -0.03em, weight 500-600) and everything else in Inter; drive hierarchy from the aggressive type scale and a LEFT-ALIGNED editorial column, never from extra color. Keep it flat and airy: pill buttons, a 1px nav hairline, generous whitespace. Do NOT use any purple/indigo/blue gradient, any fro …

## 5. Layout

A full-viewport (100vh) hero: (1) a thin transparent top NAV over the canvas — a ring-glyph wordmark left, center nav links, and right a ghost 'Sign in' + a solid-lime CTA, with a 1px bottom hairline; (2) a LEFT-ALIGNED hero column in a max-width container — a tracked eyebrow with a lime dot, a two-line Space Grotesk headline with a lime highlight sweep behind the second line, a muted Inter subhead (~48ch), a CTA row (solid-lime primary + ghost secondary), and a muted 'trusted by' wordmark row; (3) a full-bleed animated CONSTELLATION background behind all content (inline-SVG node-network, denser to the right, faded behind the text); and (4) small bottom cues (a 'SCROLL' hint and a 'live nodes' tag). On a narrow viewport the nav links collapse to a menu, the headline drops to ~40-54px, the constellation thins and shifts fully behind the copy, and the trust wordmarks wrap — the hero stays full-bleed and single-column.

## 6. Components

- **Animated SVG constellation / node-network background** — A full-bleed inline-SVG field of ~48 faint-ink nodes and connecting lines with one glowing acid-lime 'live' cluster, animated on pure CSS keyframes so a still frame is complete and legible.
- **Oversized Space-Grotesk headline with lime highlight sweep** — A two-line display headline in Space Grotesk with a translucent acid-lime bar painted behind the second line, so the ink type stays fully legible while the accent adds energy.
- **Single acid-lime CTA system (solid primary + ghost secondary)** — A restrained action pair — one solid-lime pill primary with ink text and one ghost/text secondary — plus a matching solid-lime nav button, the only filled controls on the page.
- **Tracked eyebrow + muted trust-logo row** — A tracked all-caps eyebrow with a small lime status dot above the headline, and a quiet monochrome 'trusted by' wordmark row below the CTAs as a low-key trust signal.

## 7. Motion

REVIEW —
- Cool-neutral, editorial, single-accent hero minimalism with motion — a crisp 2026 SaaS/AI landing hero, not a 2015 dark particle cliché
- Motion is quiet and pure-CSS (drifting/breathing layers, a gently pulsing accent cluster) — animated-feeling but calm, and legible with motion disabled
- Keep all motion quiet and pure-CSS so the frame reads complete and legible even with animation disabled
- Copy this hero for any SaaS, AI, or developer-tool landing page that wants real motion without looking like generic AI slop

## 8. Voice & Brand

An animated landing-page hero built around a living constellation of connected nodes. A cool pale canvas carries near-black ink type and a single acid-lime accent: a thin nav with a solid-lime CTA, then a left-aligned editorial column with a tracked eyebrow, a huge two-line Space Grotesk headline (with a lime highlight sweep behind the second line), a muted subhead, a solid-lime primary button beside a ghost 'Read the docs' link, and a quiet 'trusted by' wordmark row. Behind everything, a full-bleed SVG node-network drifts on pure CSS keyframes: most nodes and links are faint ink, one small cluster glows acid-lime as the 'live' part of the graph, and a radial fade keeps the headline perfectly legible. Two typefaces by role (Space Grotesk display + Inter body), one restrained accent, no gradient and no glass. Copy this hero for any SaaS, AI, or developer-tool landing page that wants real motion without looking like generic AI slop. Responsive down to a single-column mobile hero.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
