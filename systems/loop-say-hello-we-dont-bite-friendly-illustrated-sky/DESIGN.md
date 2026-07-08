# Design System — Loop · Say hello, we don't bite (friendly illustrated sky)

> Category: Forms & Contact  ·  Industry: General
> Auto-scaffolded from prompt [`loop-say-hello-we-dont-bite-friendly-illustrated-sky`](../../prompts/loop-say-hello-we-dont-bite-friendly-illustrated-sky/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

A warm, playful, friendly LIGHT aesthetic on a soft sky-blue cloud canvas (cloud #f0f9ff) decorated with big blurred orbs (sky-soft #bae6fd at /40-/60 and coral-soft #fecdd3 at /50) and a faint .grain polka wash (radial-gradient rgba(56,189,248,0.16) 1px dots on a 22px grid). The palette is a friendly two-accent system over a deep sea-ink: register a custom Tailwind theme of sky DEFAULT #38bdf8 / sky.soft #bae6fd / sky.deep #0ea5e9 / sky.ink #0c4a6e, coral DEFAULT #fb7185 / coral.soft #fecdd3 / coral.deep #f43f5e / coral.ink #be123c, cloud #f0f9ff and slatey #475569, plus borderRadius tokens 4xl = 2.25rem and 5xl = 3rem, plus three named boxShadows: card (0 30px 80px -30px rgba(56,189,248,0.45), 0 10px 30px -20px rgba(15,23,42,0.22)), soft (0 12px 30px -12px rgba(2,132,199,0.35)) and pill (0 12px 24px -8px rgba(251,113,133,0.55)). sky-ink #0c4a6e carries headings + primary text + the footer band; sky #38bdf8 / sky-deep #0ea5e9 / a mid #0369a1 do the cool accents (logo gradient, input icons, hovers, one headline word); coral #fb7185 / coral-deep #f43f5e / coral-ink #be123c do the warm accents (the pulsing status dot, one headline word, the inline 'say hi on email' link underline, the bug-report chip, hearts); slatey #475569 carries body + labels + placeholders. The signature DECORATION is a hand-built CSS+SVG illustration panel inside a rounded-4xl bg-gradient-to-br from-cloud to-sky-soft/40 box: a coral gradient sun (from-coral to-coral-deep) in the top-right, two white cloud SVG puffs, a center row of three circular channel bubbles (a sky compass, a big sky-ink envelope ringed in white, a coral phone), a row of six rounded grass blades in alternating sky/coral, and a white horizon bar; the sun + clouds + bubbles all drift on float-a/float-b/float-c keyframe animations (translateY -9..-16px over 6-8s ease-in-out infinite). Form .field controls are rounded-2xl bg-cloud with a 2px border-sky-soft/70 and a slatey placeholder, that on :focus drop outline, turn the border sky #38bdf8, go bg-white and punch a soft 4px sky ring (box-shadow 0 0 0 4px rgba(56,189,248,0.18)), eased .2s. The primary button is a gradient bg-gradient-to-r from-[#0369a1] to-sky-ink rounded-2xl with shadow-soft that on :hover gains shadow-pill and lifts -translate-y-0.5. Topic chips are rounded-full pills (sky-soft/60 sky-ink, the coral one coral-soft coral-ink) that fill solid sky/coral with white text on hover. The sticky nav uses bg-cloud/80 backdrop-blur-md over a border-b border-sky-soft/60, and the nav CTA is a rounded-full bg-sky-ink pill ringed in coral/50 (ring-2). Type is Nunito only (Google Fonts, weights 400/600/700/800/900 + italic 700, mapped to fontFamily.sans), rendered -webkit-font-smoothing antialiased, leaning hard on the black 900 weight for the wordmark + headlines and extrabold/bold for nav, labels and chips. Corners are soft and bubbly throughout (rounded-2xl logo tile + inputs + button, rounded-4xl illustration panel + alt cards, rounded-5xl the main card, rounded-full pills + bubbles + status pill + chips). Mood: cheerful, approachable, hand-made, human and a little playful (the '2am idea', 'we don't bite', 'No spam, ever. We hate it too.'), never a cold corporate contact form.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#f0f9ff`
- `#bae6fd`
- `#fecdd3`
- `#38bdf8`
- `#0ea5e9`
- `#0c4a6e`
- `#fb7185`
- `#f43f5e`
- `#be123c`
- `#475569`
- `#0369a1`
- `#ffffff`
- `#08344d`
- `#67e8f9`

## 3. Typography

- `Let`
- `Loop`
- `Contact`
- `Log in`
- `Fast replies`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a warm, playful, friendly LIGHT contact page for a maker brand on a soft sky-blue cloud canvas (cloud #f0f9ff) decorated with big blurred orbs (sky-soft #bae6fd at /40-/60 and coral-soft #fecdd3 at /50) and a faint .grain polka wash (radial-gradient rgba(56,189,248,0.16) 1px dots on a 22px grid). Register a friendly two-accent Tailwind theme over a deep sea-ink: sky DEFAULT #38bdf8 / sky.soft #bae6fd / sky.deep #0ea5e9 / sky.ink #0c4a6e, coral DEFAULT #fb7185 / coral.soft #fecdd3 / coral.deep #f43f5e / coral.ink #be123c, cloud #f0f9ff, slatey #475569, plus borderRadius 4xl = 2.25rem and 5xl = 3rem, and three boxShadows card (0 30px 80px -30px rgba(56,189,248,0.45), 0 10px 30px -20px rgba(15,23,42,0.22)), soft (0 12px 30px -12px rgba(2,132,199,0.35)) and pill (0 12px 24px -8px rgba(251,113,133,0.55)). Use Nunito only (Google Fonts, weights 400/600/700/800/900 + italic 700, mapped t …

## 5. Layout

A full-bleed light contact page, content centered inside a mx-auto max-w-6xl px-6 (lg:px-8) container, stacked top to bottom as: (1) a sticky blurred cloud-tinted nav, (2) a full-bleed centered HERO band over a .grain polka wash + three blurred orbs, (3) THE CONTACT CARD section (the centerpiece), (4) a full-width row of three alt-contact cards, and (5) a full-bleed sky-ink footer. The defining structural move is THE CONTACT CARD: a single huge relative rounded-5xl bg-white shadow-card ring-1 ring-sky-soft/70 overflow-hidden card (pulled up -mt-1 to overlap the hero) topped by a h-1.5 w-full bg-gradient-to-r from-sky via-cyan-300 to-coral seam, whose body is a grid lg:grid-cols-2 gap-10 (lg:gap-16) p-8 (sm:p-12 lg:p-16) split into a LEFT copy + illustration column and a RIGHT form. The LEFT column (flex flex-col) stacks a font-black sub-headline ('Say hello, we don't bite'), a font-semibold lead with an inline coral-underlined 'say hi on email' link, a hand-built rounded-4xl illustration panel (pinned toward the bottom with lg:mt-auto), and a row of two trust chips. The RIGHT column is a flex flex-col gap-6 <form>: a Full name input (with a sky user-icon prefix), an Email input (with a sky envelope-icon prefix), a What's-on-your-mind textarea, a flex-wrap row of four topic chips, a full-width gradient submit button, and a centered lock-icon 'No spam, ever' privacy line. Below the card, a mt-8 grid sm:grid-cols-3 items-stretch gap-5 of three equal-height alt-contact cards (Email us / Live chat / Community), each a rounded-4xl bg-white p-6 ring-1 ring-sky-soft/70 shadow-soft card with a rounded-2xl icon tile, a font-black title and a slatey detail line, that lift -translate-y-1 on hover. Everything reflows to a single column below lg (the form drops below the copy/illustration column; the LEFT panel loses its mt-auto pin); the alt cards go 1-up below sm; the nav center links hide below md and the Log in link below sm; the trust chips + headline reflow cleanly; no horizontal overflow at 390px.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

REVIEW —
- -16px over 6-8s ease-in-out infinite)
- The primary button is a gradient bg-gradient-to-r from-[#0369a1] to-sky-ink rounded-2xl with shadow-soft that on :hover gains shadow-pill and lifts -translate-y-0
- Topic chips are rounded-full pills (sky-soft/60 sky-ink, the coral one coral-soft coral-ink) that fill solid sky/coral with white text on hover
- -16px over 6-8s ease-in-out infinite, float-c also rotating 4deg)
- Make the submit a gradient bg-gradient-to-r from-[#0369a1] to-sky-ink rounded-2xl shadow-soft button that on :hover gains shadow-pill and lifts -translate-y-0

## 8. Voice & Brand

A warm, playful illustrated contact page (Loop) in a sky-blue + coral two-accent palette on a cloud-white canvas: a sticky blurred nav, a centered two-tone "Let's chat about anything you're building" hero with a pulsing reply-time pill, and one giant rounded white card splitting a hand-drawn CSS+SVG illustration panel (floating sun, clouds, channel bubbles, grass) and copy on the left against a multi-field form with icon-prefixed sky-ring inputs, emoji topic chips and a gradient send button on the right, then a row of three alt-contact cards and a deep sky-ink footer. Heavy rounded Nunito (up to black 900), bubbly corners, cheerful and human, never a cold corporate form.

## 9. Anti-patterns

Keep the FRIENDLY-ILLUSTRATED-SKY contact system intact, it is the whole point: a soft sky-blue cloud canvas (cloud #f0f9ff) with blurred sky/coral orbs + a faint polka grain, a friendly sky (#38bdf8) + coral (#fb7185) two-accent palette over deep sea-ink (#0c4a6e) text, a heavy rounded Nunito type ramp (up to black 900), and ONE giant rounded-5xl white card holding a left copy + hand-built illustration column beside a right multi-field form. Register the full Tailwind theme: colors sky DEFAULT #38bdf8 / soft #bae6fd / deep #0ea5e9 / ink #0c4a6e, coral DEFAULT #fb7185 / soft #fecdd3 / deep #f43f5e / ink #be123c, cloud #f0f9ff, slatey #475569; borderRadius 4xl = 2.25rem and 5xl = 3rem; boxShadow card (0 30px 80px -30px rgba(56,189,248,0.45), 0 10px 30px -20px rgba(15,23,42,0.22)), soft (0 12px 30px -12px rgba(2,132,199,0.35)), pill (0 12px 24px -8px rgba(251,113,133,0.55)). Use Nunito only (family=Nunito:ital,wght@0,400;0,600;0,700;0,800;0,900;1,700, fontFamily.sans, antialiased) and inline hand-coded SVG icons (no icon font, no real imagery). Draw the ILLUSTRATION PANEL entirely in CSS + SVG inside a rounded-4xl bg-gradient-to-br from-cloud to-sky-soft/40 ring-1 ring-sky-soft/70 box: a coral gradient sun (from-coral to-coral-deep opacity-90), two white cloud puffs, a center row of three channel bubbles (a w-16 sky compass, a big w-24 sky-ink envelope ringed ring-4 ring-white, a w-16 coral phone), six alternating sky/coral grass blades and a white horizon bar, with the sun/clouds/bubbles float-animated via float-a/float-b/float-c keyframes (translateY -9..-16px over 6/7/8s ease-in-out infinite, float-c rotating 4deg). Keep the .field inputs (rounded-2xl bg-cloud border-2 border-sky-soft/70, slatey placeholder, the name+email prefixed by an absolute sky SVG icon at pl-12) with their SKY focus signal (on :focus outline:none, border sky #38bdf8, bg-white, box-shadow 0 0 0 4px rgba(56,189,248,0.18)), eased .2s, and the gradient submit button (bg-gradient-to-r from-[#0369a1] to-sky-ink, shadow-soft -> hover shadow-pill + -translate-y-0.5, trailing paper-plane). Spend the two accents warmly: sky for cool structure (logo gradient, input icons, hovers, compass + grass + the 'anything' word) and coral for warmth (the pulsing status dot + ping, the 'you're building' word, the 'say hi on email' coral-underlined link, the bug-report chip, the phone bubble, hearts, the sun). Lean hard on Nunito black 900 for the wordmark + both headlines and extrabold/bold for nav, labels, chips. Keep corners soft and bubbly: rounded-2xl inputs/button/logo tile, rounded-4xl illustration panel/alt-cards, rounded-5xl main card, rounded-full pills/bubbles/chips/status. The structure is a full-bleed page inside a max-w-6xl container: a sticky bg-cloud/80 backdrop-blur nav (coral-ringed 'Start free' CTA), a centered HERO band (pulsing status pill + two-tone font-black headline 'Let's chat about anything you're building' + a '2am idea' sub) over three blurred orbs + the polka grain, THE CONTACT CARD (the seam + the split copy/illustration | form), a mt-8 sm:grid-cols-3 row of three alt-contact cards (Email us / Live chat / Community), and a full-bleed bg-sky-ink footer (a Loop logo tile + '© 2026 Loop Design. Made with [heart] for makers.' + three social icon links). Everything must reflow cleanly: the card stacks to one column below lg (the form drops below the copy/illustration column, the LEFT panel loses its lg:mt-auto pin), the alt cards go 1-up below sm, the nav center links hide below md and the Log in link below sm, the headline + trust chips reflow, and there is no horizontal overflow at 390px. Copy is warm, playful and human with ZERO em-dashes ('Say hello, we don't bite', 'a half-baked idea at 2am', 'Stuck on a design? Got a wild idea? Just want to nerd out about UI?', 'Real humans, promise.', 'The weirder the idea, the better.', 'No spam, ever. We hate it too.', 'Loved by 57k makers'). The page must never load real imagery, an icon font or a second type family: it is a cheerful, hand-made sky-and-coral light surface drawn in CSS + inline SVG with Nunito, with playful warmth as the design POV.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
