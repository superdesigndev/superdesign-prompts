# Design System — Animated Wave-Line Landing Hero

> Category: Animations & Backgrounds  ·  Industry: General
> Auto-scaffolded from prompt [`animated-wave-line-landing-hero`](../../prompts/animated-wave-line-landing-hero/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Modern, crisp, techy, a little kinetic - the opposite of a dark neon hero. The whole character comes from a calm animated LINE field plus one warm accent on a cool light ground. Everything is neutral except a single electric-tangerine accent, so the composition stays quiet and premium while the moving wave-lines give it life. The lines are crisp STROKES (a wave-LINE field), never blurred gradient blobs or an aurora glow. Type is a clean grotesk system: an Instrument Sans display headline for weight and character, Inter for body, and a JetBrains-Mono micro-label for the eyebrow and captions, so hierarchy is built from size and weight, never color. The register to hit is light, airy, confident, and subtly in motion.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#eef2f7`
- `#e6ebf2`
- `#94a3b8`
- `#5b6b8c`
- `#ff6a2b`
- `#141a24`
- `#475569`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a modern developer-tool / SaaS landing-page HERO whose entire canvas is a LIGHT cool ice-white ground (#eef2f7, optionally a faint gradient to #e6ebf2) filled by an AMBIENT ANIMATED BACKGROUND of flowing horizontal wave-lines. Build the field as a single full-bleed inline SVG (explicit viewBox 0 0 1440 900, preserveAspectRatio slice) of ~12 smooth cubic wave-line paths, 1.4px strokes in quiet slate (#94a3b8 and #5b6b8c), spaced down the whole height. Animate them with CSS @keyframes ONLY (no JavaScript): a slow horizontal translateX drift with a different phase offset per line plus a gentle vertical breathing, 18-30s ease-in-out infinite, so it undulates like calm sound-wave contours. Draw ONE 'active' ridge near the vertical center in electric tangerine #ff6a2b with a soft drop-shadow glow, and put a small solid tangerine locator DOT on that ridge; make sure a frozen mid-frame re …

## 5. Layout

A single full-bleed hero viewport: the animated wave-line SVG is the whole background canvas (z-0), and everything else floats over it. Top: a floating TRANSPARENT nav (emblem + wordmark left, center menu links with one dropdown chevron, a 'Sign in' text link + a tangerine pill CTA right). Middle: a centered stack - a mono uppercase eyebrow, a one-line display headline, a two-line subtitle (max 640px), and two CTAs side by side (a solid tangerine pill + a ghost/outline button with an arrow). Bottom: a quiet full-width 'trusted by' strip with a mono caption over a muted single-color row of 5-6 placeholder wordmark logos. On a narrow viewport the nav collapses to emblem + a compact menu button, the headline steps down (~40px), the two CTAs stack full-width, and the logo row wraps.

## 6. Components

- **Animated wave-line background field** — The signature: a full-bleed field of flowing horizontal wave-lines that undulate via CSS keyframes, with no JavaScript, so it is freeze-safe and drop-in.
- **Tangerine active ridge + locator dot** — The single accent in the background: one wave-line highlighted in glowing tangerine with a small dot riding it, telegraphing that the field is in motion.
- **Single-accent tangerine pill CTA** — The one saturated UI accent - a solid tangerine pill reused for the nav CTA and the hero primary CTA, paired with a neutral ghost button.
- **Floating transparent nav with dropdown** — A top nav with no background fill that floats directly over the animated canvas, its center menu carrying a small dropdown chevron.

## 7. Motion

REVIEW —
- The register to hit is light, airy, confident, and subtly in motion
- Animate them with CSS @keyframes ONLY (no JavaScript): a slow horizontal translateX drift with a different phase offset per line plus a gentle vertical breathing, 18-30s ease-in-out infinite, so it undulates like calm sound-wave contours

## 8. Voice & Brand

An animated developer-tool / SaaS landing hero whose signature is an ambient animated background: a full-bleed field of flowing horizontal wave-lines that undulate in pure CSS and inline SVG (no JavaScript). Light cool ice-white ground, one electric-tangerine accent ridge with a locator dot, a clean Instrument Sans headline, dual CTAs, and a quiet trusted-by logo strip. Copy the animated background or the whole hero layout.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
