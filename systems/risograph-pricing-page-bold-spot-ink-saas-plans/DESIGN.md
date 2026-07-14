# Design System — Risograph Pricing Page: Bold Spot-Ink SaaS Plans

> Category: Pricing Pages  ·  Industry: SaaS
> Auto-scaffolded from prompt [`risograph-pricing-page-bold-spot-ink-saas-plans`](../../prompts/risograph-pricing-page-bold-spot-ink-saas-plans/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Risograph print aesthetic on warm cream paper. A strictly limited spot-ink palette is the whole personality: cream paper (#f4eede), a deep blue-black ink (#191b2f) for text + borders + shadows, federal blue (#2436c8) as the primary / featured ink, fluoro pink (#ff4d9d) as the accent / most-popular ink, and a whisper of yellow (#ffcf33) for tiny sparks; overprints where pink and blue overlap multiply to purple. Everything is FLAT like a print: NO soft blur shadows, NO gradients-for-depth. Depth and texture come instead from hard OFFSET solid-ink shadows (a card casts a 7px hard ink block, the featured card a pink one), thick 2.5px ink borders, halftone dot fields (radial-gradient dots in a spot ink), overprinted circles (mix-blend-mode: multiply), a deliberate mis-registration ghost on the hero word, and a grain overlay (SVG feTurbulence at low opacity, multiply) over the entire page. Type is Bricolage Grotesque (a characterful modern grotesque) for display + body at 700/800 for headings and prices, and DM Mono for eyebrows, small labels and the '/ mo' price suffix (uppercase, letter-spacing ~0.18em). Hierarchy is built from size + weight, not a second color. Corners are square-ish (flat print), buttons and cards are hard-edged with visible ink borders. The mood: bold, warm, tactile, print-shop, editorial, a little playful, unmistakably crafted.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#f4eede`
- `#191b2f`
- `#2436c8`
- `#ff4d9d`
- `#ffcf33`

## 3. Typography

- `Most popular`
- `Trusted by`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a SaaS pricing page as a RISOGRAPH print. Canvas is warm cream paper #f4eede; text, borders and shadows are a deep blue-black ink #191b2f. Use a STRICTLY limited spot-ink palette: federal blue #2436c8 (primary + the featured plan fill), fluoro pink #ff4d9d (accent + most-popular + mis-registration ghost), and a whisper of yellow #ffcf33 for tiny sparks only; let overlapping pink and blue overprint to purple via mix-blend-mode: multiply. Keep EVERYTHING FLAT like a print run: NO soft blur box-shadows and NO gradients used for depth. Get depth + texture from print devices instead: (1) hard OFFSET solid-ink shadows, e.g. box-shadow: 7px 7px 0 #191b2f on cards, 3px 3px 0 on buttons, and a PINK 7px offset on the featured card; (2) thick 2.5px ink borders; (3) halftone dot fields via radial-gradient (a spot-ink dot on a ~9px grid); (4) overprinted circles (absolute, border-radius:50%, m …

## 5. Layout

A vertical scroll on a max-w-[1180px] container: (1) a sticky cream nav with a halftone logo tile + wordmark, center links, and a solid-pink 'Get started' pill; (2) a left-aligned hero over overprint circles + a halftone field: a DM Mono eyebrow tag, a mis-registered 800 H1, a one-line sub, and a segmented monthly/annual pill toggle + a pink 'Save 20% annually' tag; (3) THE PRICING: three tier cards (Starter / Studio featured / Press), each with a hard offset ink shadow, the featured one ink-inverted to blue with a pink offset shadow + 'Most popular' tab + raised; (4) a monochrome 'Trusted by 4,000+ studios' logo strip between ink hairlines; (5) a 4-card FAQ grid; (6) a solid-blue CTA band with overprint + halftone; (7) a 4-column footer. All flat; grain over everything. Reflows on mobile: the three cards stack (max-w-[440px], featured un-raised), the FAQ and footer collapse to fewer columns, nav links hide.

## 6. Components

- **Mis-registration hero headline** — A print off-register effect faked in CSS: one hero word carries a spot-ink ghost offset behind the ink word.
- **Hard offset print shadow** — Flat solid-ink offset shadows that replace all soft blur, giving the print-registration look.
- **Overprint circles** — Overlapping spot-ink circles that multiply to a third color where they stack.
- **Halftone dot field** — A print halftone texture drawn from a radial-gradient dot grid in a spot ink.
- **Ink-inverted featured plan card** — The one recommended tier flipped to a solid spot-ink fill so it dominates without a second accent.
- **Segmented monthly/annual pill toggle** — A flat print-styled billing toggle where the active segment is a solid ink pill.
- **Spot-ink feature tick** — A small square print tick that swaps ink color per plan context.
- **Grain overlay** — A page-wide risograph paper grain that ties every section into one print.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A bold risograph SaaS pricing page: warm cream paper with federal-blue and fluoro-pink spot inks, halftone dot fields, overprint that multiplies to purple, deliberate mis-registration, grain, and hard flat offset "print" shadows on the cards. Three clear tiers (Starter / Studio featured / Press) with a big bold price on each, a monthly/annual segmented-pill toggle with a "Save 20%" tag, a "Most popular" badge on the ink-inverted featured plan, per-tier CTAs and checked feature lists, a monochrome "Trusted by" logo strip, a 4-card FAQ, a solid-blue CTA band, and a footer. Bricolage Grotesque display + DM Mono labels. Recognizable as a pricing page while carrying a real print-shop point of view. Reusable for any indie, creative-tool, or studio SaaS that wants pricing with personality.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
