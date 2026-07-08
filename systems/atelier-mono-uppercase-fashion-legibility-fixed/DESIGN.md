# Design System — ATELIER — Mono Uppercase Fashion (legibility-fixed)

> Category: E-commerce  ·  Industry: Fashion & Beauty
> Auto-scaffolded from prompt [`atelier-mono-uppercase-fashion-legibility-fixed`](../../prompts/atelier-mono-uppercase-fashion-legibility-fixed/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

A stark, editorial, high-fashion monochrome aesthetic, the kind of pared-back luxury-retail look used by houses like Toteme: a strictly two-color palette of pure black ink (#0a0a0a) on pure white paper (#ffffff), no greys except as low-opacity tints of the ink/paper (text drops to ink/70, ink/65, ink/60, paper/75, paper/55, paper/50, paper/45, paper/40 for hierarchy). The signature is typography, not color: an Archivo Expanded display face used UPPERCASE for the wordmark, headlines and section labels with tight negative tracking on the big type, contrasted with very wide positive letter-spacing on the small uppercase chrome (custom tracking utilities 0.34em / 0.22em / 0.14em). Everything is hairline and flat: a single 1px border at rgba(10,10,10,0.12) ('hairline') separates sections, there are no rounded corners, no drop shadows, no gradients, no fills except solid black plates that invert to white text. Motion is restrained and couture: nav links and CTAs get a 1px underline that wipes in left-to-right on a long cubic-bezier(.16,1,.3,1) ease, content reveals fade-and-rise on scroll, and a slash-separated marquee scrolls horizontally. The feel is gallery-clean, confident, and expensive: lots of whitespace, oversized display type, monochrome image plates, and zero decoration that does not earn its place.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#0a0a0a`
- `#ffffff`

## 3. Typography

- `ATELIER`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Use a strict monochrome editorial-fashion design system on the Tailwind CDN with exactly two custom colors: `ink` #0a0a0a and `paper` #ffffff. Body is `background:#ffffff; color:#0a0a0a` with `-webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; scroll-behavior: smooth`. NEVER use literal grey hexes for hierarchy: instead tint with opacity (text-ink/70, /65, /60; on dark sections text-paper/75, /55, /50, /45, /40). Fonts via Google Fonts: `Archivo` (weights 300/400/500/600) set as `font-sans` and the body default, and `Archivo Expanded` (weights 400/500/600) set as `font-wide` for the wordmark, all headlines, and section labels. Define three letter-spacing utilities: `.tracking-mono { letter-spacing: 0.34em }`, `.tracking-wide-2 { letter-spacing: 0.22em }`, `.tracking-wide-1 { letter-spacing: 0.14em }`. Set everything in the chrome and headlines UPPERCASE. Use a singl …

## 5. Layout

A `sticky top-0 z-50` frosted-white `<header>` (`bg-paper/90 backdrop-blur-md` over a `border-b hairline`, with a `transition-colors duration-500` that gains a faint hairline shadow once the page scrolls past 8px) whose inner `<nav>` centers in a `max-w-[1400px] mx-auto px-6 md:px-10` column. The nav row is `relative flex items-center justify-between` at a fixed `h-[68px] md:h-[88px]` and carries THREE zones in one bar: (1) on the LEFT a `hidden lg:flex` row of four uppercase wide-tracked text links (New / Library / Studio / About) which is replaced below lg by a single `ph:list` hamburger button; (2) in the DEAD CENTER an `absolute left-1/2 -translate-x-1/2` Archivo Expanded wordmark 'ATELIER' that holds its 0.34em tracking at every breakpoint; (3) on the RIGHT a utility cluster of two more uppercase links (Search, Account, lg-only) plus a `ph:magnifying-glass` (mobile-only) and a `ph:handbag` bag icon with a '(0)' count. A `lg:hidden` drawer (`max-h-0` -> animated `max-h`) drops below the bar on mobile with the four links stacked. Beneath the header is a full editorial landing page (a giant display hero + a 4-plate monochrome process strip, a slash marquee, an editorial product grid, a dark split 'Studio' section, a centered manifesto, a dark CTA, and a footer) so the sticky bar scrolls over real content.

## 6. Components

- **** — 
- **** — 
- **** — 
- **** — 
- **** — 
- **** — 

## 7. Motion

REVIEW —
- Motion is restrained and couture: nav links and CTAs get a 1px underline that wipes in left-to-right on a long cubic-bezier(
- 3,1) ease, content reveals fade-and-rise on scroll, and a slash-separated marquee scrolls horizontally
- nav-link::after { content:''; position:absolute; left:0; right:0; bottom:-6px; height:1px; background:#0a0a0a; transform: scaleX(0); transform-origin:left; transition: transform
- nav-link:hover::after { transform: scaleX(1) }`
- reveal { opacity:0; transform: translateY(18px); transition: opacity 1s cubic-bezier(

## 8. Voice & Brand

A stark monochrome high-fashion editorial navbar (Toteme-style): a sticky frosted-white bar that packs three zones at once: uppercase wide-tracked text links pinned left (New / Library / Studio / About), an absolutely-centered Archivo Expanded 'ATELIER' wordmark in the dead center, and a right cluster of two more uppercase links (Search, Account) plus a Phosphor handbag icon with a '(0)' bag count. Pure black ink (#0a0a0a) on white (#ffffff) over a single hairline border, with a 1px underline that wipes in under each link on a long couture ease. Below lg the left links collapse into a hamburger drawer while the wordmark stays centered, and the legibility fix keeps the wordmark's 0.34em letter-spacing at every breakpoint.

## 9. Anti-patterns

Exact tokens (Tailwind config): only two colors, `ink` #0a0a0a and `paper` #ffffff; all hierarchy is opacity tints of those (text-ink/70, /65, /60 on light; text-paper/75, /55, /50, /45, /40 on dark; borders rgba(10,10,10,0.12) light via `.hairline` and `border-paper/15` on dark). Fonts (Google Fonts): Archivo 300/400/500/600 as `font-sans` + body default, Archivo Expanded 400/500/600 as `font-wide` for wordmark/headlines/labels; `-webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility`. Letter-spacing utilities: `.tracking-mono` 0.34em, `.tracking-wide-2` 0.22em, `.tracking-wide-1` 0.14em; big display type uses `tracking-tight`. Single hairline border everywhere: `.hairline { border-color: rgba(10,10,10,0.12) }`; NO rounded corners, NO shadows except an optional on-scroll `shadow-[0_1px_0_rgba(10,10,10,0.06)]` under the nav; NO gradients; solid `bg-ink text-paper` plates invert for contrast. Signature `.nav-link::after` underline = 1px black bar inset 0, bottom -6px, scaleX(0)->scaleX(1) on hover over .4s cubic-bezier(.16,1,.3,1). `.reveal` fade-and-rise on scroll (opacity 0 + translateY(18px) -> in) via IntersectionObserver, with a load-time safety net that reveals everything after 600ms. `.marquee-track` = 28s linear infinite horizontal loop (translateX 0 -> -50%) of a slash-separated term list. Header: `sticky top-0 z-50 w-full bg-paper/90 backdrop-blur-md` over `border-b hairline`, centered in `max-w-[1400px] mx-auto px-6 md:px-10` at `h-[68px] md:h-[88px]`; the wordmark is `absolute left-1/2 -translate-x-1/2`. LEGIBILITY FIX baked into this version: the centered wordmark keeps its 0.34em `.wordmark` tracking at EVERY breakpoint (verified to still fit at 390px) instead of tightening on mobile. Icons: Iconify Phosphor (ph:list, ph:magnifying-glass, ph:handbag). Reference inspiration: the monochrome high-fashion editorial retail header (e.g. Toteme, https://toteme.com/en-au), recreated as an original prompt-library product for the placeholder brand 'Atelier'. The page beneath the bar (a giant display hero + a 4-plate process strip, a slash marquee, an editorial product grid, a dark studio split, a centered manifesto, a dark CTA, and a footer) is demo context so the sticky bar has real content to scroll over; the prompt-library value is the tri-zone monochrome fashion navbar pattern itself.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
