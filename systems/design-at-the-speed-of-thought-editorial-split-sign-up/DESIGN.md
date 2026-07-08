# Design System — Design at the Speed of Thought — Editorial Split Sign-Up

> Category: Auth & Login  ·  Industry: SaaS
> Auto-scaffolded from prompt [`design-at-the-speed-of-thought-editorial-split-sign-up`](../../prompts/design-at-the-speed-of-thought-editorial-split-sign-up/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

A warm, editorial / magazine aesthetic that treats a sign-up like the cover spread of a design journal. Three grounds carry the page: a cream paper #faf6ef, a deep wine burgundy #7b2d3b (the brand pane), and a near-black ink #1c1815 (the form column + footer), with a lighter burgundy #a9485a as the secondary accent and a darker burgundy #5e202b for shadows/blooms. Typography pairs Fraunces (an optical-size serif) for oversized display headlines, the brand wordmark, the pull-quote and the section labels with Inter for body/UI. The burgundy pane is textured: a fine SVG fractal-noise film grain at 5% overlay, faint concentric stroke arcs top-right and a soft blurred burgundy-dark radial bloom bottom-left. Color discipline is tight: cream type on burgundy, cream type on ink, burgundy as the single action color (the CTA, links, the brand tile, focus rings). Inputs are white cards on the dark column that get a burgundy focus ring; links use an animated underline-grow; the CTA and OAuth buttons lift on hover. Calm, high-craft, print-like; warm and human copy with zero em-dashes.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#faf6ef`
- `#7b2d3b`
- `#1c1815`
- `#a9485a`
- `#5e202b`
- `#f3ecdf`
- `#2a241f`
- `#ffffff`
- `#d8cdbb`
- `#fffdfa`
- `#a89a85`
- `#9a8c77`
- `#b9ab95`

## 3. Typography

- `Fraunces`
- `Georgia`
- `Inter`
- `Create account`
- `Trusted in the studios shipping fastest`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Editorial / magazine-style sign-up landing on a warm cream + deep burgundy + near-black ink palette. Tailwind CDN with a custom theme.extend.colors: cream #faf6ef, creamlo #f3ecdf, ink #1c1815, inksoft #2a241f, burg #7b2d3b, burgdk #5e202b, burglt #a9485a; theme.extend.fontFamily serif ['Fraunces','Georgia','serif'] and sans ['Inter','system-ui','sans-serif']. Load Fraunces (ital, optical-size opsz 9..144, weights 300..700) + Inter (400;500;600) from Google Fonts; body font-family Inter, antialiased + optimizeLegibility, html scroll-behavior smooth. Display class = letter-spacing -0.02em, line-height 0.95; .font-serif uses font-optical-sizing auto. The burgundy brand pane is textured: a .grain::before overlay (a tiled SVG feTurbulence fractalNoise data-URI, opacity 0.05, mix-blend-mode overlay), faint concentric circle SVG arcs (stroke cream at ~0.16 opacity) bleeding off the top-right,  …

## 5. Layout

A sticky translucent cream nav, then a full-height two-pane split main (LEFT a burgundy editorial brand panel, RIGHT a near-black ink sign-up form column), then a full-bleed cream 'Trusted in the studios shipping fastest' proof strip, then a dark ink FAQ/footer (an accordion + a brand column + a legal bar). The split main is a grid lg:grid-cols-[1.04fr_1fr] at min-h-[calc(100vh-4rem)]; below lg it stacks and the order flips so the form column comes first. Most containers center in mx-auto max-w-[1240px] px-6 sm:px-8.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

REVIEW —
- Inputs are white cards on the dark column that get a burgundy focus ring; links use an animated underline-grow; the CTA and OAuth buttons lift on hover
- oauth) lift on hover (translate-y -1px + a soft shadow + a #b9ab95 border)
- cta) is a solid burg #7b2d3b button that on hover lifts and casts a 0 12px 30px -8px rgba(123,45,59,0
- ulink) use an animated background-size underline-grow from 0% to 100% on hover

## 8. Voice & Brand

An editorial, magazine-style sign-up screen built as a full split-screen landing: a sticky translucent cream nav over a two-pane main. The LEFT is an oversized Fraunces-serif brand panel on a textured deep-burgundy ground (film grain, faint concentric arcs, a soft bloom) with an 'Issue 06 . The Design Agent' eyebrow, a 'Design at the speed of thought.' display headline (italic 'speed'), a value paragraph and a pull-quote testimonial with an initials avatar plus a three-icon feature row. The RIGHT is a near-black ink account-creation column: a 'Start designing, free.' heading, Google + GitHub OAuth buttons above an 'or with email' divider, white burgundy-focus-ring email + password fields (an eye toggle + a four-segment strength meter) and a burgundy 'Create account' CTA. Below the split: a full-bleed cream 'Trusted in the studios shipping fastest' proof strip and a dark ink FAQ/footer accordion. Cream + burgundy + ink palette, Fraunces serif + Inter.

## 9. Anti-patterns

Built on the Tailwind CDN with a custom theme.extend: colors cream #faf6ef, creamlo #f3ecdf, ink #1c1815, inksoft #2a241f, burg #7b2d3b, burgdk #5e202b, burglt #a9485a; fontFamily.serif = ['Fraunces','Georgia','serif'] and fontFamily.sans = ['Inter','system-ui','sans-serif']. Google Fonts: Fraunces (ital, opsz 9..144, weights 300..700 roman + 300..600 italic) + Inter (weights 400;500;600). CSS keys: html scroll-behavior smooth; body font-family Inter, antialiased, optimizeLegibility; .display = letter-spacing -0.02em + line-height 0.95; .font-serif font-optical-sizing auto. .grain::before = content '', absolute inset-0, pointer-events none, opacity 0.05, mix-blend-mode overlay, background a tiled SVG feTurbulence fractalNoise data-URI (baseFrequency 0.85, numOctaves 2). .field = background #ffffff + 1px #d8cdbb border, transition border-color/box-shadow/background .18s; .field:focus-within = border-color #7b2d3b + box-shadow 0 0 0 3px rgba(123,45,59,0.12) + background #fffdfa; .field input background transparent, outline none; placeholder #a89a85; leading icons #9a8c77. .oauth:hover = border-color #b9ab95 + box-shadow 0 2px 14px rgba(28,24,21,0.06) + translate-y -1px. .cta:hover = translate-y -1px + box-shadow 0 12px 30px -8px rgba(123,45,59,0.45); .cta:active translate-y 0. .ulink = an underline-grow via background-image linear-gradient(currentColor,currentColor) + background-size 0% 1px -> 100% 1px on hover (background-position 0 100%). .rule = linear-gradient(90deg, transparent, rgba(250,246,239,0.32), transparent) hairline. .nav-blur = backdrop-filter saturate(140%) blur(10px). .meter-seg = height 4px + border-radius 99px. FAQ uses native <details>/<summary> with list-style none + ::-webkit-details-marker hidden and a .chev that rotates 180deg in details[open] (transition .25s). The RIGHT ink form pane carries a lg-only left edge-light (a before pseudo-element vertical gradient hairline from-transparent via-burglt/40 to-transparent). Icons via Iconify (Phosphor 'ph:*' set, logos:google-icon, mdi:github). Burgundy #7b2d3b is the single action/accent color (the CTA, the brand tile, links, the focus ring, the strength bars use burglt #a9485a); cream #faf6ef is the type-on-dark color; the form column is near-black ink #1c1815. The reusable prompt-library value is the EDITORIAL SPLIT sign-up: an oversized Fraunces serif brand panel on a textured burgundy ground (film grain + concentric arcs + a pull-quote testimonial) beside a near-black ink OAuth-first form column (white burgundy-focus-ring fields + a password-strength meter + a burgundy CTA), wrapped in a complete one-screen sign-up landing (sticky translucent nav + a full-bleed cream trust strip + a dark FAQ/footer accordion). Original prompt-library product for the placeholder brand 'Atelier'. Responsive: the split flips order and stacks below lg, nav center links hide below md, the 'Already with us?' label hides below sm, the display headline clamps, the trust strip and FAQ collapse to one column, no overflow at 390px.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
