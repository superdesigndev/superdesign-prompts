# Design System — Atlas Studio — Charting Your Account, Step One of Three

> Category: Auth & Login  ·  Industry: Agency & Studio
> Auto-scaffolded from prompt [`atlas-studio-charting-your-account-step-one-of-three`](../../prompts/atlas-studio-charting-your-account-step-one-of-three/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Dark, premium SaaS aesthetic. A near-black midnight-navy canvas (#07162b) layered with soft radial amber + steel-blue glows (the .grain wash) and a masked dot grid (#aebfd8 at 10% opacity, 26px). Surfaces are translucent navy cards (navy-800 at ~55% over the glow) with thin 1px navy-600 hairline borders, generous 24px rounded corners and a soft elevated shadow plus subtle backdrop blur. Type is Inter (400-900). The single accent is warm amber (#f0b429): used for the logo tile, the active progress node, the primary CTA, focus rings, icons and 5-star ratings. Text is cream (#f6f1e7) at varied opacities (full for headings, ~65-80% for body, ~35-45% for hints). No second accent color, no hard borders, no heavy gradients on text. Everything reads soft, glassy and deliberate.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#07162b`
- `#aebfd8`
- `#f0b429`
- `#f6f1e7`
- `#34527f`
- `#f4c44f`
- `#de9b18`
- `#f7d070`
- `#0f263e`
- `#234066`
- `#7e96bd`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a premium dark SaaS onboarding screen. Background: a deep midnight navy #07162b, washed with soft radial glows (a warm amber glow #f0b429 at ~16% from the top-right, a steel-blue glow #34527f at ~45% from the top-left, and a darkening vignette toward the bottom), plus a faint dot grid (radial-gradient dots in #aebfd8 at 10% opacity on a 26px cell, masked to fade at top and bottom). Typography is Inter, weights 400 to 900; headings are extrabold (800/900) with tight tracking and ~1.05 leading; body is 13-16px in cream #f6f1e7 at 55-80% opacity. The single accent is warm amber: amber-500 #f0b429 (with amber-400 #f4c44f and amber-600 #de9b18 for the progress bar gradient, amber-300 #f7d070). Surfaces are translucent cards: fill navy-800 #0f263e at ~55% over the glow, 1px hairline border in navy-600 #234066 at ~60% opacity, 24px (rounded-3xl) corners, a soft layered shadow (0 30px 60p …

## 5. Layout

A full-height screen: a slim sticky glass top nav, a full-bleed centered onboarding section, and a footer. The section is centered in a max-w-7xl container with ~20-32px side padding: a centered eyebrow pill, a centered headline + subhead, then a two-column body (lg:grid-cols-[1.55fr_1fr]) with the form card on the left (wider) and a stacked context column on the right (value panel + testimonial + 'log in' line). Below the two columns sits a centered trust strip. Below the lg breakpoint the two columns stack to a single column (form first, then context). The defining structural element is the 3-step progress tracker at the top of the form card.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

REVIEW —
- 55)); it lifts -1px on hover

## 8. Voice & Brand

Premium dark-navy multi-step signup / onboarding screen (step 1 of 3) for an AI design tool: a 3-step progress tracker, glassy translucent cards on a midnight-navy ground with soft amber glows, a single warm amber accent, focus-reactive fields, a password strength meter, a role selector, and a 'what you unlock' value panel with a testimonial.

## 9. Anti-patterns

Keep it to ONE accent (warm amber #f0b429) on the deep-navy ground; do not introduce a second hue. The depth model is soft glass, not hard edges: thin 1px hairline borders, 24px rounded-3xl corners, soft layered shadows and backdrop blur (no thick borders, no hard offset shadows). The mandatory hero element is the 3-step progress tracker (Step 1 of 3, 33% bar, active amber node 1 + outlined nodes 2/3) at the top of the form card, since this is a multi-step onboarding rather than a single signup. Use Inter throughout (extrabold 800/900 for headings, 400-600 for body). Text is cream #f6f1e7 at graduated opacities (full headings, 55-80% body, 35-45% hints) - never pure white. Layout is a wider form (1.55fr) beside a narrower context column (1fr) on desktop, stacking to one column below lg; everything stays centered in a max-w-7xl container with no horizontal overflow at 390px.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
