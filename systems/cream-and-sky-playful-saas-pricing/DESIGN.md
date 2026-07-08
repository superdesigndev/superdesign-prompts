# Design System — Cream & Sky Playful SaaS Pricing

> Category: Pricing Pages  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`cream-and-sky-playful-saas-pricing`](../../prompts/cream-and-sky-playful-saas-pricing/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

A soft, playful, light-mode SaaS aesthetic: a warm cream paper canvas with a subtle dotted-grain texture, a friendly sky-blue accent system, and rounded everything. Big serif display headlines (Fraunces) paired with a clean humanist sans (Plus Jakarta Sans) for body. Generous border radii (28-36px cards, full-pill buttons), pastel decorative blobs floating behind the hero, hand-drawn squiggle underline on a keyword, gentle tilted icon chips, and emoji-adjacent Phosphor glyphs. Warm, human, low-pressure. Shadows are soft and tinted blue, never harsh.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#fdfbf4`
- `#f0f8ff`
- `#e0f1ff`
- `#bfe2ff`
- `#8fcaff`
- `#5aadff`
- `#2e8fff`
- `#1a72ed`
- `#1554b0`
- `#0f4796`
- `#0b3678`
- `#fbf5e6`
- `#f6ecd2`
- `#f0e0b8`
- `#15233b`
- `#5a6b85`

## 3. Typography

- `Fraunces`
- `Plus Jakarta Sans`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a warm, playful light-mode SaaS page. Background is cream paper #fdfbf4 with a faint dotted grain texture (radial-gradient dots, ~22px grid, rgba(21,35,59,0.025)). Primary accent is a full sky-blue ramp: sky-50 #f0f8ff, sky-100 #e0f1ff, sky-200 #bfe2ff, sky-300 #8fcaff, sky-400 #5aadff, sky-500 #2e8fff, sky-600 #1a72ed, sky-700 #1554b0, sky-800 #0f4796, sky-900 #0b3678. Secondary warm cream tones: cream-50 #fdfbf4, cream-100 #fbf5e6, cream-200 #f6ecd2, cream-300 #f0e0b8. Ink (near-black navy) for text #15233b, muted slate #5a6b85 for secondary copy. Typography: display headings in 'Fraunces' serif (weights 400-700, optical-size aware), body and UI in 'Plus Jakarta Sans' (400-800). Use very rounded shapes: cards at 28-36px radius, all buttons fully pill-shaped, icon chips in 16-22px squircles often tilted -6deg/+4deg/12deg. Soft tinted shadows only: soft '0 18px 50px -18px rgba(26, …

## 5. Layout

A frameless, responsive single-page pricing layout. Top to bottom: sticky blurred nav, a centered hero with badge + serif headline (with squiggle-underlined keyword) + subcopy + a monthly/yearly billing toggle, then the core pricing region of three side-by-side tier cards with the middle one lifted and highlighted, a reassurance line, a three-up 'every plan includes' value strip, a big gradient CTA band, an accordion FAQ, and a footer. Max content width ~1152px (max-w-6xl), centered, generous vertical rhythm. Fully responsive: the 3 pricing cards reflow 3->2->1 column, the value strip 3->2->1, nav links collapse on mobile, and the sticky header stays pinned on scroll.

## 6. Components

- **Springy billing toggle** — Custom pill switch that flips monthly<->yearly, animating the knob with a bouncy cubic-bezier(.4,1.2,.5,1) easing and live-swapping prices + billing captions.
- **Squiggle keyword underline** — Hand-drawn SVG squiggle stroke underlining the accent keyword in the serif headline.
- **Highlighted 'Most loved' tier card** — The center Pro card visually elevated: blue gradient fill, negative top margin lift, pop shadow, an edge-pinned uppercase badge, and a tilted winking-smiley mascot dot.
- **Tilted icon chips** — Recurring squircle icon containers rotated a few degrees for a playful, hand-placed feel.
- **Dashed-divider feature checklist** — Tier feature lists where rows are separated by dashed hairlines, with check / x icons.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A warm, friendly light-mode SaaS pricing page on a cream paper canvas with sky-blue accents, serif display type, rounded cards, a monthly/yearly toggle, and a highlighted middle tier.

## 9. Anti-patterns

Frameless, fully responsive web page (no device/browser chrome). Light mode only; the warmth comes from the cream paper background + dotted grain, not a white card on grey. The signature move is the playful contrast: serious serif display type (Fraunces) over a friendly cream-and-sky palette with tilted chips, pastel blobs, a squiggle underline, and emoji-energy Phosphor icons. Pricing structure = 3 tiers with the middle one highlighted + lifted, a monthly/yearly toggle that recalculates prices, a reassurance line, and an accordion FAQ. Keep all radii large and all shadows soft + blue-tinted. Responsive behavior: pricing cards reflow 3->2->1 column (the lifted Pro card drops its negative margin when stacked), the value strip goes 3->2->1, the nav links hide on mobile while the sticky blurred header stays pinned, and content is capped at ~1152px and centered. Uses Tailwind (CDN) + Phosphor via Iconify; voice is warm and human ('Most loved', 'Made with a little chaos and a lot of love').

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
