# Design System — Coverflow — Carousels that turn heads (dark coverflow aurora)

> Category: Mobile Apps  ·  Industry: AI & Tech
> Auto-scaffolded from prompt [`coverflow-carousels-that-turn-heads-dark-coverflow-aurora`](../../prompts/coverflow-carousels-that-turn-heads-dark-coverflow-aurora/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

A premium dark, aurora-lit aesthetic: a near-black blue-ink ground (#0b0f14) lit from the corners by large blurred aurora blobs in a teal-to-magenta family. The two signature accents are aqua/teal (#2dd4bf) and magenta (#e879f9), used together as gradients (logo chip, hero 'turn heads' gradient text, active-card glow, active dot, primary CTA, template thumbs) and individually as section eyebrows and feature-icon tints. Text is light slate (Tailwind slate-200/300/400) on the dark ground; the only light surfaces are the white 'Start free' pill and the white CTA button (with dark #0b0f14 'ink' text on them). Surfaces are 'glass': translucent white panels (linear-gradient of rgba(255,255,255,0.06) to 0.015) with a hairline rgba(255,255,255,0.08) border and a 14px backdrop blur, plus deep drop shadows (0 30px 70px -28px rgba(0,0,0,0.85)); the active coverflow card swaps in a teal glow shadow + teal ring (0 40px 90px -30px rgba(45,212,191,0.35), 0 0 0 1px rgba(45,212,191,0.25)). Depth comes from layered atmosphere: two large corner aurora blobs (teal top-left ~620px, magenta bottom-right ~680px, blur 90px, opacity .5), a central teal-magenta ellipse glow (blur 110px), and a faint 56px grid texture masked to a soft radial vignette around the hero. Corners are generously rounded (rounded-full pills/buttons/dots, rounded-2xl glass cards, 22px coverflow cards, rounded-xl/lg chips). Typography pairs Inter (sans body/UI, weights 400-700) with Space Grotesk (display headings + card titles, weights 500-700), with tight tracking on the big display heading. The overall feel is cinematic and motion-forward: real 3D perspective, smooth cubic-bezier(.22,.61,.36,1) card transitions over .55s, a glowing active slide, and gentle hover scales on the nav buttons.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#0b0f14`
- `#2dd4bf`
- `#e879f9`
- `#0e141b`
- `#7defe0`
- `#000`

## 3. Typography

- `Start free`
- `Inter`
- `Space Grotesk`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a premium dark, aurora-lit design system on the Tailwind CDN with Inter (body/UI) + Space Grotesk (display) and Iconify Phosphor icons. Extend the Tailwind theme with custom colors `ink` #0b0f14, `ink2` #0e141b, `aqua` #2dd4bf, `magenta` #e879f9, and `fontFamily.sans = ['Inter','system-ui','sans-serif']`, `fontFamily.display = ['Space Grotesk','Inter','sans-serif']`; load Inter (400;500;600;700) + Space Grotesk (500;600;700) from Google Fonts and Iconify 3.1.1 from its CDN. Body is `font-sans text-slate-200 antialiased selection:bg-aqua/30` with `body { background-color:#0b0f14 }` and `html { scroll-behavior:smooth }`. The ground is near-black blue-ink (#0b0f14); the only light surfaces are a white `rounded-full` 'Start free' pill and the white CTA button, both with `text-ink` (#0b0f14) dark text. Use TWO accents as a teal->magenta pair: aqua #2dd4bf and magenta #e879f9, combined as  …

## 5. Layout

A single dark scrolling landing page: sticky nav, a tall hero whose centerpiece is a 3D coverflow stage with controls, then a logo strip, a 3-up feature grid, a 2-col showcase split, a 3-up templates grid, a dark CTA section, and a footer. The `<nav>` is `sticky top-0 z-50 border-b border-white/5 bg-ink/70 backdrop-blur-xl` with a centered `mx-auto max-w-6xl flex items-center justify-between px-6 py-4` row (brand cluster left, `hidden md:flex` link row center, sign-in/Start-free/hamburger right) plus a `hidden md:hidden` slide-down mobile menu. The `<header>` hero is `relative overflow-hidden` and stacks an `.aurora` + `.aurora-mid` + `.grid-tex` backdrop, then a centered `max-w-6xl px-6 pt-16 pb-10 text-center` intro (a glass status pill, the two-line gradient-accent heading, a lead), then a `max-w-5xl px-4 pb-6` coverflow region (a soft teal glow oval behind, the `.coverflow` perspective stage, and a centered control row of prev / dots / next), then a `max-w-6xl px-6 pb-16 text-center` CTA pair + trust line. The coverflow stage is `position:relative; height:440px; perspective:1600px; transform-style:preserve-3d` holding seven `.cf-card` tiles (`position:absolute; top/left 50%; 280x372px; margin offsets to center; border-radius 22px; overflow:hidden`), each JS-injected with a vertical gradient background, a top-left radial sheen, and a bottom `.label` (uppercase category + Space Grotesk title). Sections below share `mx-auto max-w-6xl px-6`: a `border-y border-white/5 bg-ink2/60` logo strip (six Space Grotesk wordmarks), a `py-24` features section (centered eyebrow/heading/lead + a `grid md:grid-cols-3 gap-5` of glass feature cards), a `border-t border-white/5 bg-ink2/50 py-24` showcase split (`grid lg:grid-cols-2` of copy+checklist+CTA vs a glass terminal card), a `py-24` templates section (a header row + a `grid sm:grid-cols-2 lg:grid-cols-3 gap-5` of glass cards with gradient thumbs), a `border-t border-white/5 py-24` CTA section (an `.aurora-mid` glow + a centered `max-w-3xl` heading/lead/button-pair), and a `border-t border-white/5 bg-ink2/60` footer (brand / copyright / social icon row). Responsive: at <=860px the stage is 400px tall with smaller cards and the far cards fade out; at <=480px it is 360px with only the active + immediate neighbours visible; below md the nav links collapse into the hamburger menu and headings/CTAs scale and stack.

## 6. Components

- **** — 
- **** — 
- **** — 
- **** — 
- **** — 
- **** — 
- **** — 
- **** — 

## 7. Motion

REVIEW —
- The overall feel is cinematic and motion-forward: real 3D perspective, smooth cubic-bezier(
- 55s, a glowing active slide, and gentle hover scales on the nav buttons
- Motion: coverflow cards transition `transform
- 55s ease, filter
- 55s ease`; nav buttons scale 1

## 8. Voice & Brand

A dark, aurora-lit 3D coverflow carousel landing page: a sticky frosted-ink nav, then a centered hero (a 'depth-aware coverflow engine' status pill, a big 'Carousels that turn heads, not stomachs.' heading whose 'turn heads' is teal-to-magenta gradient text, and a soft lead) wrapping a real CSS 3D coverflow stage. Seven gradient cards sit on a 1600px perspective stage: the active card faces front with a teal glow ring while neighbours rotate ~42-48deg and recede in Z, scaling and fading by distance, each card carrying a top-left sheen and a bottom gradient label. Below the stage, a round glass prev button, pill dots (active = a wide teal-to-magenta gradient bar), and a next button; clicks, dots, arrows and the left/right keys re-lay the stage. Then a CTA pair, a grayscale logo strip, a 3-up glass feature grid, a 'from prompt to motion' showcase split with a faux terminal card, a gradient-thumb templates grid, a dark gradient CTA, and a social footer. Inter + Space Grotesk fonts, near-black ink #0b0f14 ground, aqua #2dd4bf + magenta #e879f9 accents, glass panels and aurora blobs, Iconify Phosphor icons; responsive geometry drops far cards on small screens and collapses the nav into a hamburger.

## 9. Anti-patterns

Exact tokens (Tailwind config extend): colors `ink` #0b0f14, `ink2` #0e141b, `aqua` #2dd4bf, `magenta` #e879f9; `fontFamily.sans = ['Inter','system-ui','sans-serif']`, `fontFamily.display = ['Space Grotesk','Inter','sans-serif']`. Fonts: Inter (Google Fonts weights 400;500;600;700) + Space Grotesk (500;600;700); Iconify 3.1.1 (Phosphor `ph:` set) from https://code.iconify.design/3/3.1.1/iconify.min.js. Body `font-sans text-slate-200 antialiased selection:bg-aqua/30` with `body { background-color:#0b0f14 }` and `html { scroll-behavior:smooth }`. Two accents only (aqua #2dd4bf + magenta #e879f9), used as gradients and as individual eyebrow/icon tints; the only light surfaces are the white 'Start free' pill and the white CTA button, both `text-ink`. `.glass`: `linear-gradient(160deg, rgba(255,255,255,0.06), rgba(255,255,255,0.015))`, `border:1px solid rgba(255,255,255,0.08)`, `backdrop-filter: blur(14px)`. `.gradient-text`: `linear-gradient(100deg,#2dd4bf 0%,#7defe0 35%,#e879f9 100%)` clipped to text. Atmosphere: `.aurora::before` ~620px teal radial blob top-left, `.aurora::after` ~680px magenta radial blob bottom-right (blur 90px, opacity .5); `.aurora-mid` ~520x320px teal-magenta ellipse (blur 110px); `.grid-tex` 56px line grid masked by `radial-gradient(ellipse 90% 62% at 50% 38%, #000 18%, transparent 72%)`. Coverflow: `.coverflow { height:440px; perspective:1600px; transform-style:preserve-3d }`; `.cf-card { 280x372px; margin-left:-140px; margin-top:-186px; border-radius:22px; background:#0e141b; box-shadow:0 30px 70px -28px rgba(0,0,0,0.85); transition: transform .55s cubic-bezier(.22,.61,.36,1), opacity .55s ease, filter .55s ease }`. Position transforms: pos-0 `translate3d(0,0,140px) rotateY(0) scale(1)` + glow `box-shadow:0 40px 90px -30px rgba(45,212,191,0.35), 0 0 0 1px rgba(45,212,191,0.25)`; pos-1/n1 `±168px,0,-40px rotateY ∓42deg scale .86 opacity .92`; pos-2/n2 `±310px,0,-200px rotateY ∓46deg scale .7 opacity .55`; pos-3/n3 `±420px,0,-360px rotateY ∓48deg scale .56 opacity .22`; cf-hidden `0,0,-520px scale .4 opacity 0`. Dots: `.dot 8px rgba(255,255,255,0.22)`, `.dot.active width:26px; background:linear-gradient(90deg,#2dd4bf,#e879f9); box-shadow:0 0 14px rgba(45,212,191,0.6)`. `.nav-btn 44px round, place-items center`, hover scale 1.08 + teal border. JS: a `slides` array of 7 `{title,sub,g}` objects (featured 'Moonrise' is true-aqua `linear-gradient(150deg,#2dd4bf 0%,#22a89a 45%,#0c3b45 78%)`), each rendered as a `.cf-card` with a top-left radial sheen + a bottom gradient `.label` (uppercase 11px category + 17px Space Grotesk title); `active` starts at 3; a single `render()` maps signed distance->position class and toggles the active dot; `#next`/`#prev` and ArrowRight/Left clamp active to `[0,6]`; card/dot clicks jump. Responsive: <=860px stage 400px, cards 230x312, neighbours pull in, far cards hidden; <=480px stage 360px, cards 200x272, only active+/-1 visible; below md nav links collapse into the hamburger `#mobileMenu`, 'Sign in' is `hidden sm:block`, headings/CTAs scale and stack. This is an original prompt-library product for the placeholder brand 'Coverflow' (faithfully reproducing the build HTML); the library value is the reusable dark aurora-lit CSS-3D coverflow pattern itself -- a perspective stage of rotating, receding gradient cards with a glowing active slide, pill-dot pagination, keyboard + click control, and a responsive geometry that drops far cards on small screens.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
