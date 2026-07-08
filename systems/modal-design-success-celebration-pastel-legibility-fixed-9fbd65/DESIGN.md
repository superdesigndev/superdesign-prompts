# Design System — Modal Design · success-celebration (pastel) — legibility fixed

> Category: Onboarding  ·  Industry: General
> Auto-scaffolded from prompt [`modal-design-success-celebration-pastel-legibility-fixed-9fbd65`](../../prompts/modal-design-success-celebration-pastel-legibility-fixed-9fbd65/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

A warm, playful, premium-pastel aesthetic that turns a 'success' state into a designed payoff moment, with legibility engineered into the palette. The mood is soft and celebratory: a pale sky-to-cream gradient field (radial sky + radial blush washes over a vertical #eaf6fd -> #f3fbff -> #fdf9f3 ramp) carpeted with small multicolor confetti rectangles and dots that both fall (CSS keyframe) and gently float (floaty keyframe), so the page feels alive without motion clutter. The key discipline is a two-tier color system: the bright candy tones (sky #38bdf8, coral #fb7185, plus accent #fbbf24 amber, #34d399 emerald, #a78bfa violet) are used ONLY as decorative fills (confetti, badge ring pulses, soft icon-tile backgrounds at ~15-20% opacity, blurred glows); every place a brand color becomes TEXT or a CTA fill on a light field, it switches to a deepened variant that clears 4.5:1 contrast (skyText/skyDeep #0369a1, skyDeep2 #075985, coralText/coralDeep #be123c). Surfaces are cream (#fdf9f3) and white with generous rounding (rounded-4xl 2rem, rounded-5xl 2.75rem) and soft, colored, deeply-offset shadows (a 'dialog' shadow tinted with sky, a plain 'soft' shadow, a sky-tinted 'pill' shadow on CTAs). Type is all Poppins, leaning extrabold (800) for headlines with tight tracking and a friendly mid-slate (#5b6172) for body. The one dark moment is the closing ink (#1f2433) CTA band, where the bright sky/coral return as text and blurred glows because the field is finally dark enough to carry them.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#eaf6fd`
- `#f3fbff`
- `#fdf9f3`
- `#38bdf8`
- `#fb7185`
- `#fbbf24`
- `#34d399`
- `#a78bfa`
- `#0369a1`
- `#075985`
- `#be123c`
- `#5b6172`
- `#1f2433`
- `#e9f7ff`
- `#fdeef0`
- `#7c3aed`

## 3. Typography

- `You`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a joyful pastel design system on a soft sky-to-cream field. Body base #eaf6fd; the hero/showcase field is layered gradients: radial-gradient(120% 80% at 12% 0%, #e9f7ff 0%, transparent 55%) + radial-gradient(120% 90% at 90% 8%, #fdeef0 0%, transparent 50%) over linear-gradient(180deg, #eaf6fd 0%, #f3fbff 45%, #fdf9f3 100%). CRITICAL two-tier color rule for legibility: the bright tones sky #38bdf8 and coral #fb7185 (plus accents amber #fbbf24, emerald #34d399, violet #a78bfa) are DECORATIVE fills ONLY (confetti, ring pulses, soft 15-20% icon-tile backgrounds, blurred glows); any sky/coral used as TEXT or a CTA gradient on a light surface MUST use the deepened >=4.5:1 variants instead — skyText #0369a1, skyDeep #0369a1, skyDeep2 #075985, coralText #be123c, coralDeep #be123c. Neutrals: surface cream #fdf9f3, white panels, ink text #1f2433, body/muted slate #5b6172. Fonts: Poppins via Go …

## 5. Layout

A single vertically-scrolling product page made of five full-bleed bands on a shared max-w-6xl mx-auto px-6 container, with the success modal as the hero centerpiece rather than an overlay on a blank artboard. Order: (1) a sticky top-0 z-50 frosted-glass nav; (2) a tall (min-h-[86vh]) hero/showcase band on the pastel confetti field that centers a small uppercase eyebrow chip, THE success dialog card, and a caption line; (3) a full-bleed cream 'pattern library' band with a centered intro and a 3-up responsive card grid; (4) a split 'starter kit' band (sky-tinted gradient) with a left copy column (eyebrow + H2 + checklist of three icon-bullets + ink CTA) and a right stacked mini upgrade-dialog preview; (5) a full-bleed dark ink CTA/'start' band with two blurred color glows, an eyebrow chip, a big two-line headline, two CTAs and a trust line; then a cream footer. It reflows cleanly to mobile: the nav center links and 'Sign in' hide (only the 'Get the kit' pill persists), the dialog and grids collapse to one column (grid sm:grid-cols-2 lg:grid-cols-3 -> 1), the starter-kit split stacks (lg:grid-cols-2 -> 1) and its decorative offset backdrop hides (lg:block), the dark-band CTA pair stacks (sm:flex-row -> column) and the footer goes column.

## 6. Components

- **** — 
- **** — 
- **** — 
- **** — 
- **** — 

## 7. Motion

REVIEW —
- The mood is soft and celebratory: a pale sky-to-cream gradient field (radial sky + radial blush washes over a vertical #eaf6fd -> #f3fbff -> #fdf9f3 ramp) carpeted with small multicolor confetti rectangles and dots that both fall (CSS keyframe) and gently float (floaty keyframe), so the page feels alive without motion clutter
- 5 on hover; the dark-band hero CTA uses from-skyDeep to-coralDeep
- Motion (all decorative, reduced-motion-safe in spirit): a badge 'pop' scale-in, an SVG check 'draw' (stroke-dashoffset 60 -> 0), two staggered 'ring' pulse halos behind the badge (sky/25 then coral/20), a 'fall' confetti keyframe and a slow 'floaty' bob

## 8. Voice & Brand

A joyful pastel success-celebration modal as the live hero centerpiece of a product page: a rounded-5xl cream dialog with an animated deep-sky checkmark badge (pulsing rings + a drawn check), a 'You're all set! 🎉' headline and a deep-sky gradient CTA, floating over a soft sky-to-cream field full of gently floating multicolor confetti, a frosted-glass sticky nav, a 3-up pattern-library grid, a starter-kit split with a stacked upgrade-dialog preview, and a dark ink CTA band. Legibility-fixed: bright sky/coral stay decorative while every text + CTA tone uses deepened >=4.5:1 variants. All Poppins, Phosphor icons.

## 9. Anti-patterns

Single Google Font: Poppins (weights 400/500/600/700/800) as the only family — headlines extrabold (800) with tight tracking, body in mid-slate. Icons are Phosphor via Iconify (ph:sparkle-fill, ph:confetti-fill, ph:x-bold, ph:arrow-right-bold, ph:check-circle-fill, ph:warning-fill, ph:check-bold, ph:heart-fill, ph:rocket-launch-fill). EXACT tokens — cream #fdf9f3, ink #1f2433, slate #5b6172, page base #eaf6fd; DECORATIVE-ONLY bright tones sky #38bdf8 + coral #fb7185 (+ amber #fbbf24, emerald #34d399, violet #a78bfa); LEGIBILITY-FIXED text/CTA tones skyText=skyDeep #0369a1, skyDeep2 #075985, coralText=coralDeep #be123c, plus violet text #7c3aed. THE CORE LEGIBILITY RULE (the point of this item): bright sky/coral are used ONLY as decorative fills (confetti, ring-pulse halos, ~15-20% soft icon-tile backgrounds, blurred dark-band glows); wherever a brand color becomes TEXT or a CTA gradient on a light field it switches to the deepened >=4.5:1 variant, so contrast is never sacrificed for the pastel mood. Radii: rounded-2xl tiles, rounded-4xl (2rem) pattern cards, rounded-5xl (2.75rem) dialog + mini-preview. Shadows: shadow-dialog 0 40px 90px -30px rgba(31,36,51,0.35) + 0 18px 40px -24px rgba(56,189,248,0.35); shadow-soft 0 18px 50px -24px rgba(31,36,51,0.30); shadow-pill 0 14px 30px -10px rgba(56,189,248,0.55). Effects: a .glass frosted nav (rgba(253,249,243,0.72) + saturate(160%) blur(14px)); the layered .field hero gradient; and decorative animations only — 'pop' badge scale-in, 'draw' SVG check, two staggered 'ring' halo pulses, a 'fall' confetti drop and a slow 'floaty' bob (all decorative, safe to disable for reduced motion). Layout: a sticky top-0 z-50 .glass nav over five full-bleed bands on a shared max-w-6xl mx-auto px-6 container (hero confetti field with the dialog centerpiece, cream 3-up pattern grid, sky-tinted starter-kit split with a stacked mini upgrade-dialog, dark ink CTA band, cream footer). Responsive reflow: nav center links + 'Sign in' hide on mobile (only 'Get the kit' persists), the dialog and pattern grid go single-column (sm:grid-cols-2 lg:grid-cols-3 -> 1), the starter-kit split stacks (lg:grid-cols-2 -> 1) and its -left-3 offset backdrop hides, the dark-band CTA pair stacks (sm:flex-row -> column) and the footer goes column. Accessibility/clarity intent: the whole palette was re-derived so the playful pastel never costs contrast — every text and CTA tone clears 4.5:1 while the candy brights live only in decoration.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
