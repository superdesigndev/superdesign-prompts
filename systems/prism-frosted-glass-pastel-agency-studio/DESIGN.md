# Design System — Prism — Frosted-Glass Pastel Agency Studio

> Category: Portfolios  ·  Industry: Agency & Studio
> Auto-scaffolded from prompt [`prism-frosted-glass-pastel-agency-studio`](../../prompts/prism-frosted-glass-pastel-agency-studio/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Soft, premium, light-mode glassmorphism. The page floats on a #fbfcff canvas washed by four overlapping pastel radial glows (peach #ffd8c2, sky #cfe3ff, mint #d3f5e3) so the background is always softly colored, never flat white. On top sit translucent frosted-glass surfaces: a lighter .glass (rgba(255,255,255,0.55) + blur(22px) saturate(140%)) for the nav, pills and bento tiles, and a heavier .glass-deep (rgba(255,255,255,0.42) + blur(28px) saturate(150%)) for the big hero cards and services/CTA panels, each ringed by a bright 1px white border. Depth is soft and colored: shadow-soft and shadow-float use blue-violet-tinted, heavily-feathered drop shadows (rgba(60,70,110,..) / rgba(50,60,105,..)), and a faint dotted .grain overlay (mix-blend overlay, opacity .18) gives the glass a frosted, photographic texture. The single high-contrast accent is near-black ink #15161b: it fills the primary pill CTAs, the logo square, and exactly one dark card per section (the +240% stat tile, the 'Most loved' service card, the feature testimonial). Pastel tints (peach/sky/mint) appear only as gentle gradient washes on glass cards, traffic-light dots, status dots, avatars, mini-chart bars and icon chips. Everything is heavily rounded (rounded-full pills + rounded-[26-40px] cards) and the type is tight Inter black, which keeps the whole thing premium, friendly and engineered rather than toy-like.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#fbfcff`
- `#ffd8c2`
- `#cfe3ff`
- `#d3f5e3`
- `#15161b`
- `#5c606e`
- `#e88a5a`
- `#d9743f`
- `#4f8cd6`
- `#3f72c4`
- `#3fae7a`

## 3. Typography

- `Most loved`
- `Inter`
- `See the work`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Light, premium glassmorphism agency site on a soft pastel mesh-gradient canvas. Load Tailwind via CDN and register exact custom colors in tailwind.config theme.extend.colors: ink '#15161b', slate2 '#5c606e', peach '#ffd8c2', sky '#cfe3ff', mint '#d3f5e3'; fontFamily.sans = ['Inter','system-ui','sans-serif']; letterSpacing.tightest '-0.045em'. Body is class 'mesh font-sans text-ink antialiased overflow-x-hidden'. The .mesh background = background-color:#fbfcff with four layered radial-gradients of the pastel tints: radial-gradient(58% 52% at 12% 8%, rgba(255,216,194,0.9) 0%, transparent 60%), radial-gradient(55% 50% at 88% 14%, rgba(207,227,255,0.95) 0%, transparent 62%), radial-gradient(60% 55% at 78% 72%, rgba(211,245,227,0.9) 0%, transparent 60%), radial-gradient(48% 44% at 30% 88%, rgba(255,216,194,0.55) 0%, transparent 60%). A .mesh-band variant (mint-left / sky-right / peach-bottom  …

## 5. Layout

A single-column, vertically stacked, frameless responsive marketing page on the pastel mesh canvas. Almost every section centers in mx-auto max-w-6xl with px-5. Order top to bottom: a floating pill-shaped sticky glass nav (header sticky top-0 z-50, the nav itself a rounded-full glass bar inset by px-5 pt-4); a centered hero (three glass pill badges, a huge Inter-black headline, a slate lead paragraph, a dark pill primary CTA + a glass secondary pill) sitting above a band of three fanned, overlapping translucent glass UI cards (a left mint-tinted card rotated -6deg, a right sky-tinted card rotated +6deg, and a centered frosted browser-style card on top); a faded centered trust logo strip (5 Phosphor-glyph wordmarks); a frosted bento WORK grid; a large glass-deep SERVICES panel (mesh-band tinted) holding three service cards; a centered three-up testimonial/clients row; a frosted closing CONTACT CTA panel; and a footer divided by white hairline borders. Reflow: the nav center links hide below md (logo + CTA remain); the hero headline drops its <br> below sm; the floating-card band scales height 300px -> sm:380px -> md:440px and cards shift inward (md:left-[8%]/right-[8%]); the bento grid is grid-cols-1 -> md:grid-cols-6 with md:auto-rows-[230px] and explicit col-span/row-span (a 4x2 feature, a 2-col dark stat, a 2-col small, two 3-col wides); the services grid is grid-cols-1 -> md:grid-cols-3; testimonials grid-cols-1 -> md:grid-cols-3; the footer is a flex-col -> md:flex-row with a 2 -> sm:3 col link grid; everything collapses to one column on mobile with no horizontal overflow (body overflow-x-hidden).

## 6. Components

- **Frosted-glass surface system (.glass / .glass-deep)** — The signature material: every nav, pill, badge, card and panel is translucent frosted glass that lets the pastel mesh bleed through, with a bright 1px white inner border so each shape reads as a sheet of glass.
- **Pastel mesh-gradient canvas (.mesh / .mesh-band)** — The whole page floats on a soft off-white canvas blooming with overlapping peach, sky and mint radial-gradient clouds; a tighter .mesh-band variant re-tints the large glass panels so they glow from within.
- **Fanned, overlapping translucent UI cards (hero)** — In place of a single product hero shot, three frosted UI mock cards fan out and overlap under the headline (a -6deg mint card, a +6deg sky card, and an upright centered browser-style card on top), each a tinted gradient glass-deep sheet with a soft floating shadow and grain.
- **Dark accent card on glass (.btn-dark / near-black ink #15161b)** — Near-black #15161b is the single high-contrast accent against all the pastel glass: it fills the primary CTA pills, the brand logo square, the bento +240% stat card, the highlighted 'Most loved' service card, and the dark feature testimonial, giving the airy page weight and a clear visual hierarchy.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A light, frosted-glass pastel agency studio homepage on a soft mesh-gradient canvas (off-white #fbfcff washed with peach #ffd8c2, sky #cfe3ff, and mint #d3f5e3 radial blooms): a floating pill-shaped glass sticky nav, a centered black-on-pastel hero (huge Inter-black headline, glass pill badges, a dark pill CTA + a glass 'See the work' pill) over fanned, overlapping translucent glass UI cards, a faded trust logo strip, a frosted bento work grid with one dark stat card (+240%), a big glass services panel with a dark featured 'Most loved' card, a three-up testimonial row with a dark feature quote, a frosted closing CTA, and a clean glass-divided footer. Award-winning soft-pastel glassmorphism with near-black #15161b ink.

## 9. Anti-patterns

Frameless, fully responsive light glassmorphism agency homepage (no browser chrome / device frame around the page itself; the only 'browser' is the decorative center hero mock card): every section centers in mx-auto max-w-6xl with px-5 and the nav floats as a rounded-full glass bar inset by px-5 pt-4. Built with Tailwind via CDN plus a small tailwind.config registering the exact custom colors (ink #15161b, slate2 #5c606e, peach #ffd8c2, sky #cfe3ff, mint #d3f5e3), the Inter font family, and letterSpacing.tightest -0.045em; Google Fonts loads Inter 400-900; icons are Iconify Phosphor (ph:) fill glyphs. Reflow: the nav center links hide below md; the hero <br> drops below sm; the floating-card band is h-300/sm:380/md:440 and the side cards shift to md:left-8%/right-8%; the bento grid is grid-cols-1 -> md:grid-cols-6 with md:auto-rows-[230px] and explicit col-span/row-span; services + testimonials are grid-cols-1 -> md:grid-cols-3; the footer is flex-col -> md:flex-row with a 2 -> sm:3 col link grid; body has overflow-x-hidden so nothing scrolls sideways on mobile. All copy and the 'Prism' brand are placeholders meant to be swapped: the transferable value is the soft-pastel glassmorphism SYSTEM (a #fbfcff mesh-gradient canvas blooming peach #ffd8c2 / sky #cfe3ff / mint #d3f5e3, frosted .glass rgba(255,255,255,0.55)+blur(22px) and .glass-deep rgba(255,255,255,0.42)+blur(28px) surfaces with 1px white borders, soft colored drop-shadows, faint grain, and near-black #15161b ink as the single accent on CTAs/stat/feature cards) plus the full agency-site LAYOUT (floating pill glass nav -> centered black-on-pastel hero over fanned translucent UI cards -> faded logo strip -> frosted bento work grid with a dark stat tile -> big glass services panel with a dark featured card -> three-up testimonial row with a dark feature quote -> frosted closing CTA -> glass-divided footer), NOT the specific studio. Keep the palette light and pastel; the ONLY dark surface is the #15161b ink used sparingly for contrast.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
