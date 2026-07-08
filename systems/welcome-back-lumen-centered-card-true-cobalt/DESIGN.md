# Design System — Welcome back · Lumen — centered-card (true cobalt)

> Category: Auth & Login  ·  Industry: SaaS
> Auto-scaffolded from prompt [`welcome-back-lumen-centered-card-true-cobalt`](../../prompts/welcome-back-lumen-centered-card-true-cobalt/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Clean, modern SaaS auth aesthetic built on a single true-cobalt accent (a pigment-rich, violet-leaning blue, NOT stock Tailwind blue) over a soft off-white canvas and slate-grey neutrals. Inter throughout with tight tracking, generous rounding (rounded-3xl card, rounded-xl controls), and a layered, mixed cobalt gradient (not flat) for the logo tiles, the top accent rail and the primary button. Depth comes from a multi-stop card shadow, a glowing button shadow with an inset top highlight, faint cobalt radial background glows, and a center-masked faint grid. Inputs are bordered, filled shells with floating labels that animate up and turn cobalt on focus, plus a 4px cobalt focus ring.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#2563eb`
- `#eef0ff`
- `#dde2ff`
- `#c2caff`
- `#9aa6ff`
- `#6b78f6`
- `#3f46e8`
- `#2a2fd4`
- `#1f24ad`
- `#1a2289`
- `#171f6b`
- `#0e1347`
- `#f4f5fb`
- `#101524`
- `#454c66`
- `#5e667f`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a clean modern SaaS authentication aesthetic anchored on a single TRUE-COBALT accent: a pigment-rich, violet-leaning blue (NOT #2563eb stock Tailwind blue), built as a cobalt ramp 50 #eef0ff, 100 #dde2ff, 200 #c2caff, 300 #9aa6ff, 400 #6b78f6, 500 #3f46e8, 600 #2a2fd4, 700 #1f24ad, 800 #1a2289, 900 #171f6b, 950 #0e1347. Page background is soft off-white #f4f5fb; body ink is #101524, secondary/label text 'slatey' #454c66, and muted placeholder text 'mute' #5e667f. Typeface is Inter (weights 400-800) loaded from Google Fonts, antialiased with text-rendering optimizeLegibility, font-feature-settings 'cv11','ss01' and letter-spacing -0.011em; headings are extrabold with tight tracking. The signature brand fill is a mixed (not flat) cobalt gradient: background-color #2a2fd4 with linear-gradient(150deg, #3f46e8 0%, #2a2fd4 46%, #1f24ad 100%), used on the logo tiles, the thin top accent rai …

## 5. Layout

A sticky full-bleed top nav above a single full-bleed auth main that vertically centers one card. The main is min-h-[calc(100vh-4rem)], grain background with the masked grid, and an inner max-w-6xl wrapper. The card itself is max-w-[440px], centered, with a header block (top accent rail, logo, heading, sub) over a body block (social row, divider, form). A footer sign-up link and a security/Terms line sit below the card. The layout reflows cleanly to a narrow single column on mobile (nav links and the 'Need help?' link hide; the card and its paddings shrink).

## 6. Components

_REVIEW: no components captured._

## 7. Motion

REVIEW —
- 5px solid #d3d8e6 border, 14px radius, hover border #b9c0d6; on focus the border becomes #2a2fd4 with a white fill and a 4px rgba(42,47,212,0
- Buttons and links use smooth cubic-bezier transitions (CTA lifts -1px and brightens on hover; nav links get an animated 2px cobalt underline)

## 8. Voice & Brand

A clean centered-card sign-in page on a soft off-white canvas with a single true-cobalt accent: sticky nav, a white rounded-3xl auth card (Google + GitHub social, floating-label email/password with a show/hide toggle, remember-me + forgot, gradient Sign in CTA), and ambient cobalt glows.

## 9. Anti-patterns

Single TRUE-COBALT accent only (the cobalt ramp), a pigment-rich violet-leaning blue, NOT stock Tailwind blue (#2563eb). Keep the brand fill as the mixed gradient (background #2a2fd4 + linear-gradient(150deg, #3f46e8, #2a2fd4, #1f24ad)), not a flat color. This is a single centered-card layout (no split panel) on a full-bleed grain background with a sticky nav above. Preserve the exact field focus treatment (#2a2fd4 border + 4px rgba(42,47,212,0.12) ring + floating cobalt label) and the named shadows (card/btn/logo). Inter throughout, rounded-3xl card / rounded-xl controls / 14px-radius fields. The page reflows to a clean narrow single column on mobile (nav links + 'Need help?' hide). No em-dashes in copy.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
