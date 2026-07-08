# Design System — Momentum — Ship Your Startup Launch Before the Idea Cools

> Category: Waitlist & Coming Soon  ·  Industry: SaaS
> Auto-scaffolded from prompt [`momentum-ship-your-startup-launch-before-the-idea-cools`](../../prompts/momentum-ship-your-startup-launch-before-the-idea-cools/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Bold optimistic SaaS gradient. Bright teal #14b8a6 to lime #a3e635 brand gradient (extended with deep teal #0d9488, mint #5eddc4, olive-green #65a30d) used for fills, text-clip headlines, 1.5px gradient rings, and a radial hero aura. Base is a soft warm-white 'paper' #fbfdfb; text is near-black warm ink #0c1a17 with muted slate #475a54 for secondary copy. Plus Jakarta Sans throughout (400-800, plus one italic 500), extrabold tight-tracked headlines. Generous whitespace, rounded geometry (rounded-lg/xl/2xl/3xl), soft layered shadows plus a signature teal glow shadow, a faint radial dot-grid texture, and frameless product mock bands rather than browser/device chrome.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#14b8a6`
- `#a3e635`
- `#0d9488`
- `#5eddc4`
- `#65a30d`
- `#fbfdfb`
- `#0c1a17`
- `#475a54`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design in a bold, optimistic SaaS-gradient style. Palette: warm-white paper base #fbfdfb, near-black warm ink text #0c1a17, muted slate secondary text #475a54, brand teal #14b8a6 and lime #a3e635 with supporting deep-teal #0d9488, mint #5eddc4 and olive-green #65a30d. Build the brand gradient as linear-gradient(105deg, #14b8a6 0%, #5eddc4 46%, #a3e635 100%) for fills (call it grad-fill), and linear-gradient(100deg, #0d9488, #14b8a6 38%, #65a30d 78%, #a3e635 100%) clipped to text for headline accents (grad-text). Use Plus Jakarta Sans for everything (weights 400/500/600/700/800, one italic 500); headlines are extrabold with tight tracking (-0.02em to -0.03em) and leading ~1.04-1.1. Geometry is rounded (rounded-lg 0.5rem through rounded-3xl 1.5rem) and pill badges. Apply a 1.5px gradient ring/border on cards, inputs and badges via a ::before mask trick (linear-gradient(120deg,#14b8a6,#a3e6 …

## 5. Layout

Single-column long-form landing page in a centered max-w-6xl (72rem) container with px-6 gutters. Top-down order: sticky blurred header nav; full-bleed gradient-aura hero (centered eyebrow pill, gradient-clip headline, sub-paragraph, inline waitlist email form, reassurance row, frameless product-preview band, and a logo trust row); a features section (one wide white card + one solid gradient accent card, then a 3-up white-card row); a full-bleed gradient traction band (left copy + right 2x2/4-up stat cards); a templates strip (header row + 3-up template preview cards); a dark ink CTA block (rounded-3xl, gradient aura, second waitlist form); and a 4-column footer with a bottom bar. Responsive: nav links hide below md; the hero form stacks below sm; feature/template/stat grids collapse from 3/4 to 2 to 1; gradient auras are clipped by section overflow-hidden so they never cause horizontal scroll.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

Bold optimistic startup launch / waitlist landing page: teal-to-lime gradient brand on warm-white paper, sticky blurred nav, gradient-aura hero with an inline email-capture form and a frameless prompt-to-page preview, feature cards, a gradient traction band, launch-template cards, a dark ink CTA, and a 4-column footer.

## 9. Anti-patterns

Fonts: Plus Jakarta Sans only, loaded from Google Fonts (ital,wght 0,400;0,500;0,600;0,700;0,800;1,500). Built with Tailwind via the CDN (cdn.tailwindcss.com) using a custom theme: colors ink #0c1a17, slate #475a54, teal #14b8a6, lime #a3e635, paper #fbfdfb; custom boxShadow tokens soft / lift / glow; sans font-family mapped to Plus Jakarta Sans. Icons via iconify-icon web component (Phosphor 'ph:' set). html has scroll-behavior:smooth and all gradient-aura/blob sections use overflow-hidden so the blurred washes never cause horizontal scroll. No real product screenshots or photos are used: everything is rendered with CSS gradients, dot-grid texture and skeleton bar/block placeholders. Keep the mood bright, optimistic and fast-shipping; never dark-mode-default, neon-cyberpunk, or corporate-stiff. The only dark surface is the single ink CTA card.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
