# Design System — Modal Design · success-celebration (pastel) — legibility fixed

> Category: Onboarding  ·  Industry: General
> Auto-scaffolded from prompt [`modal-design-success-celebration-pastel-legibility-fixed`](../../prompts/modal-design-success-celebration-pastel-legibility-fixed/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

A joyful, premium pastel light aesthetic that reads like a polished SaaS celebration screen: a cream-and-sky radial field warmed by a coral wash, soft generous rounding (up to 2.75rem), and three layered shadow tokens (dialog/soft/pill) that lift every card off the page without a single hard border. The brand 'color' is a sky-blue + coral pastel pairing, but the system is split into a decorative layer and a text/CTA layer so it stays legible on light: pastel sky #38bdf8 and coral #fb7185 appear only as confetti, badge fills and tint backgrounds, while any sky- or coral-colored TEXT or icon on a light field uses a darkened token (skyText/coralText = #0369a1 / #be123c, >=4.5:1) and every gradient button runs deep-to-deep stops (skyDeep #0369a1 -> skyDeep2 #075985, or skyDeep -> coralDeep #be123c) so white text always clears contrast. Ink #1f2433 is the heading/text color and slate #5b6172 the muted body. Motion is the joy: a checkmark badge that pops + draws its tick, two staggered pulsing rings, falling confetti and a gentle all-over floating scatter. Poppins (400-800) carries everything, extra-bold for headlines.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#38bdf8`
- `#fb7185`
- `#0369a1`
- `#be123c`
- `#075985`
- `#1f2433`
- `#5b6172`
- `#eaf6fd`
- `#e9f7ff`
- `#fdeef0`
- `#f3fbff`
- `#fdf9f3`

## 3. Typography

- `Continue to dashboard`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a soft pastel light design system. Body base #eaf6fd; the hero is a .field gradient = radial-gradient(120% 80% at 12% 0%, #e9f7ff 0%, transparent 55%) + radial-gradient(120% 90% at 90% 8%, #fdeef0 0%, transparent 50%) + linear-gradient(180deg, #eaf6fd 0%, #f3fbff 45%, #fdf9f3 100%). Define a SPLIT color system so pastels stay legible on light: decorative-only fills cream #fdf9f3, sky #38bdf8, coral #fb7185; legible TEXT/icon tokens skyText #0369a1 and coralText #be123c (>=4.5:1 on light); CTA gradient stops skyDeep #0369a1, skyDeep2 #075985, coralDeep #be123c (always behind white text); plus ink #1f2433 (headings/text) and slate #5b6172 (muted body). NEVER use raw #38bdf8 or #fb7185 as text on a light field — use the darker token. One Google Font: Poppins (400/500/600/700/800) as font-sans, extra-bold (800) for headlines with tracking-tight. Custom radii borderRadius 4xl 2rem / 5xl 2 …

## 5. Layout

A single scrolling product page on a centered max-w-6xl mx-auto px-6 container, anchored by a sticky top-0 z-50 glass nav, then five regions: (1) a min-h-[86vh] celebration hero (the .field gradient) with a full-bleed two-layer confetti background — a falling-confetti layer + a gently floating all-over scatter — behind a centered column holding an uppercase eyebrow chip, the success MODAL as the centerpiece, and a caption line; (2) a full-bleed cream 'pattern library' band with a centered intro + a 3-up grid of white pattern cards; (3) a sky-tinted 'starter kit' split (lg:grid-cols-2): a left benefits column (eyebrow + H2 + lead + a 3-item check list + a dark CTA) and a right stacked mini upgrade-modal preview offset by a coral tint card behind it; (4) a full-bleed dark-ink CTA band with two blurred color glows, an eyebrow chip, a big two-line headline, lead, two CTAs and a trust line; (5) a cream footer with a brand lockup, a copyright line and three text links. Everything reflows to a single column on mobile: the modal stays max-w-md and centered, the pattern grid goes 3 -> 1, the kit split stacks (the coral offset card hides below lg), the CTA buttons stack, the nav hides its center links + 'Sign in' below md/sm while the 'Get the kit' button persists, and the footer goes column.

## 6. Components

- **** — 
- **** — 
- **** — 
- **** — 
- **** — 

## 7. Motion

REVIEW —
- Motion is the joy: a checkmark badge that pops + draws its tick, two staggered pulsing rings, falling confetti and a gentle all-over floating scatter
- 5 on hover; the dark CTA band button is the only place coral enters a gradient
- Motion tokens: @keyframes pop (scale 0
- 35s ease-out) to draw the tick; @keyframes ring (scale 0

## 8. Voice & Brand

A joyful pastel success-celebration modal as the live centerpiece of a light SaaS page: a cream rounded-5xl dialog with a pulsing-ring animated checkmark badge, a gradient 'Continue to dashboard' CTA and a ghost secondary, floating over a full-bleed confetti layer on a cream-to-sky radial field. Below it a 3-up pattern-library card band, a starter-kit split with a stacked mini upgrade modal, a dark-ink CTA band and a cream footer. Pastel sky + coral are decorative-only; all colored text uses darkened >=4.5:1 tokens (#0369a1 / #be123c) and every gradient button runs deep stops behind white — legibility fixed. Poppins throughout.

## 9. Anti-patterns

One Google Font: Poppins (weights 400/500/600/700/800) as font-sans for everything; extra-bold (800) headlines with tracking-tight. Icons are Phosphor via Iconify, colored only with the LEGIBLE text tokens or white, never the raw pastels (ph:sparkle-fill, ph:confetti-fill, ph:x-bold, ph:arrow-right-bold, ph:check-circle-fill, ph:warning-fill, ph:check-bold, ph:heart-fill, ph:rocket-launch-fill). THE LEGIBILITY RULE (the whole point of this variant): the pastel sky #38bdf8 and coral #fb7185 are DECORATIVE-ONLY (confetti, badge/tint fills, blurred glows); any sky/coral-colored TEXT or icon on a light field must use the darkened token skyText/coralText = #0369a1 / #be123c (>=4.5:1), and every gradient CTA runs deep stops behind white (skyDeep #0369a1 / skyDeep2 #075985 / coralDeep #be123c) — raw pastels never carry white text. The only place pastels appear as text/fills is the dark-ink band, where contrast is fine. Exact tokens — cream #fdf9f3, sky #38bdf8 (decor), skyText/skyDeep #0369a1, skyDeep2 #075985, coral #fb7185 (decor), coralText/coralDeep #be123c, ink #1f2433 (headings/text), slate #5b6172 (muted body); plus confetti accents amber #fbbf24, emerald #34d399, violet #a78bfa (with #7c3aed / #f43f5e used as the violet/rose text+gradient tokens). Body base #eaf6fd; the hero .field = radial(120% 80% at 12% 0%, #e9f7ff) + radial(120% 90% at 90% 8%, #fdeef0) + linear(180deg, #eaf6fd -> #f3fbff -> #fdf9f3). Custom radii 4xl 2rem / 5xl 2.75rem (cards rounded-4xl/5xl, buttons rounded-full). Three shadow tokens: dialog '0 40px 90px -30px rgba(31,36,51,0.35), 0 18px 40px -24px rgba(56,189,248,0.35)', soft '0 18px 50px -24px rgba(31,36,51,0.30)', pill '0 14px 30px -10px rgba(56,189,248,0.55)'. A .glass nav utility = bg rgba(253,249,243,0.72) + backdrop saturate(160%) blur(14px). Motion: @keyframes pop on .badge-pop, @keyframes draw on .check-path, @keyframes ring on two .ring-pulse halos (one .delay), @keyframes fall on .confetti spans, @keyframes floaty on a gentle .float scatter. The page is a sticky top-0 z-50 glass nav over five max-w-6xl regions (celebration hero, pattern band, kit split, dark CTA band, footer) and reflows to a single column on mobile: the modal stays max-w-md centered, the pattern grid goes 3 -> 1, the kit split stacks and the coral offset card hides below lg, the CTA buttons stack, the nav center links + 'Sign in' hide below md/sm while 'Get the kit' persists, the H2 line break shows only sm+, and the footer goes column.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
