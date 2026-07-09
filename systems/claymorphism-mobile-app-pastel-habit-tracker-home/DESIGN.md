# Design System — Claymorphism Mobile App: Pastel Habit Tracker Home

> Category: Mobile Apps  ·  Industry: Health & Wellness
> Auto-scaffolded from prompt [`claymorphism-mobile-app-pastel-habit-tracker-home`](../../prompts/claymorphism-mobile-app-pastel-habit-tracker-home/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Light claymorphism / soft inflated pastel UI. A cool cream-grey clay ground, harmonized low-saturation pastels (sage, peach, butter, sky), very large corner radii, a rounded geometric sans, and the signature clay shadow (outer soft drop + outer white highlight + inset pair) so every card and icon reads as puffy and inflated. Charcoal text, never pure black. Left-aligned, calm, friendly.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#eef0f5`
- `#f6f7fb`
- `#bfe3c6`
- `#3f6b48`
- `#ffd9c2`
- `#a4593a`
- `#ffe9b0`
- `#8a6d1f`
- `#c9e4f6`
- `#3a6a8a`
- `#3a3f4a`
- `#8a90a0`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a LIGHT claymorphism mobile screen. Ground: cool cream-grey #eef0f5; card surface #f6f7fb (slightly lighter than the ground so the puffiness reads). Palette is harmonized low-saturation pastels, NO purple/indigo anywhere: sage #bfe3c6 (text #3f6b48), peach #ffd9c2 (text #a4593a), butter #ffe9b0 (text #8a6d1f), sky #c9e4f6 (text #3a6a8a); ink text #3a3f4a, muted #8a90a0. Tinted cards/icons pair the pastel fill with its darker shade for legible text (contrast >= 4.5:1). Font: Nunito (800 for greetings/metric numbers, 700 for card titles, 600 tracked labels/meta, 400-500 body). Very large radii: hero card 34px, standard cards 26px, icon tiles 20px, pills 18px, avatars/circles 50%. THE CORE is the clay shadow on every raised surface = an outer soft drop bottom-right (e.g. 10px 12px 24px rgba(163,170,190,.45)) + an outer white highlight top-left (-8px -8px 20px rgba(255,255,255,.9)) +  …

## 5. Layout

A single vertical mobile home screen in natural document flow (no fixed overlay clipping content): status bar, header (date eyebrow + single greeting + avatar), sage progress hero card, a two-up stat-tile row, a 'Today's habits' list of clay rows, and an in-flow floating tab bar with a raised '+' FAB. Real ~390-430px phone width, 20px side padding, 16px gaps.

## 6. Components

- **Claymorphism card** — The inflated puffy surface used for every raised element.
- **Pastel icon tile** — A soft rounded clay chip holding a line icon, color-coded per habit.
- **Sage progress hero** — The tinted primary card summarizing today's completion.
- **Clay toggle states** — The done-vs-pending habit checkbox, made unambiguous.
- **Floating clay tab bar with FAB** — The bottom navigation, in-flow so it never clips content.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A light claymorphism mobile app home screen for a friendly habit and wellness tracker. Soft, inflated pastel "clay" cards (sage, peach, butter-yellow, sky-blue) on a cool cream-grey ground, with the signature dual soft shadow plus inset highlight that makes every surface look puffy. A rounded Nunito type scale, a tracked-caps date over a single bold greeting, a sage progress hero card with a rounded-cap progress bar and a streak chip, two puffy stat tiles, a scannable habit list with clear done-versus-pending toggle states, and an in-flow floating tab bar with a raised peach round add button. Light mode, real phone proportions, no dark neumorphism and no purple gradient. Reusable for any friendly consumer app home (habit, wellness, mood, budgeting, language learning).

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
