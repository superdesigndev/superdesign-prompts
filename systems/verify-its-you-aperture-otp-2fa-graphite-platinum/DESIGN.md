# Design System — Verify it's you · Aperture (OTP / 2FA, graphite-platinum)

> Category: Auth & Login  ·  Industry: SaaS
> Auto-scaffolded from prompt [`verify-its-you-aperture-otp-2fa-graphite-platinum`](../../prompts/verify-its-you-aperture-otp-2fa-graphite-platinum/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Calm, premium, light-mode security UI built on a graphite + platinum + warm-paper system, with zero saturated color. Canvas is a warm off-white 'paper' (#f6f5f2) deepening to 'paper2' (#efeee9); near-black 'ink' graphite (#1c1c1e) carries text, the lock icon, the primary button and focus states; a cool 'platinum' grey (#c7c7cc, dim #9a9aa0) is the only secondary accent, used for the card accent rail, the OTP separator dash, the progress dots and muted icons. Surfaces are subtle translucent white glass (white at ~85% over paper) with hairline ink/10 borders and very soft, deep, low-opacity shadows. Inter throughout (400-800) with tight tracking on the heading and OpenType features (ss01/cv11/cv05) on. Generous rounded corners (card ~26px, button ~16px, OTP inputs ~12px), an inner-gloss top sheen on the card, and a graphite focus ring on the inputs give it a high-end, trustworthy, almost stationery-like feel.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#f6f5f2`
- `#efeee9`
- `#1c1c1e`
- `#c7c7cc`
- `#9a9aa0`
- `#222224`
- `#2c2c2e`
- `#3a3a3c`
- `#d6d6db`

## 3. Typography

- `Inter`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a calm, premium light-mode security/auth aesthetic with NO saturated color. Background: warm off-white 'paper' #f6f5f2 deepening to 'paper2' #efeee9 (use a vertical gradient from-paper via-paper to-paper2). Build an ambient backdrop layer (pointer-events-none, absolute inset-0, -z-10): the paper gradient + a large soft platinum glow blob (h ~420px, w ~820px, bg platinum at ~25% alpha, blur-3xl) top-center; add a faint two-spot 'grain' veil via radial-gradients of ink at 4-5% alpha. Text & primary surfaces in near-black graphite 'ink': ink-900 #1c1c1e, ink-800 #222224, ink-700 #2c2c2e, ink-600 #3a3a3c. The ONLY secondary accent is a cool platinum grey: platinum #c7c7cc, platinum-soft #d6d6db, platinum-dim #9a9aa0 (used for the card top accent rail, the OTP separator dash, progress dots and muted icons). Surfaces are glass: bg white at 70-85% alpha, 1px ink/10 border, big radius (~2 …

## 5. Layout

A single full-height page centered on one narrow auth column (max-width ~440px). A sticky translucent top nav and a full-bleed paper2 footer bracket a min-h-screen hero/auth main that vertically and horizontally centers the card over the ambient backdrop. Above the card sits an eyebrow 'Two-factor' pill; the card itself stacks the verify flow top to bottom (lock icon -> title -> subtitle -> six OTP inputs -> Verify button -> progress dots -> resend); below it sit an encryption reassurance line and a two-link helper row.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

REVIEW —
- Interaction states: OTP input focus = ink border + 4px ink/8 ring + a soft drop shadow + a 1px translateY lift; filled input = ink-700 border + solid white bg; primary button hover = 1px lift + a deep ink-tinted shadow

## 8. Voice & Brand

OTP / two-factor verification screen on warm paper with a graphite + platinum palette: a Two-factor eyebrow pill, a glass card with a lock icon, six single-digit code boxes, progress dots, a live resend countdown and a Verify code button. Inter, light mode, no saturated color.

## 9. Anti-patterns

Color tokens (exact): ink-900 #1c1c1e, ink-800 #222224, ink-700 #2c2c2e, ink-600 #3a3a3c; platinum DEFAULT #c7c7cc, platinum-soft #d6d6db, platinum-dim #9a9aa0; paper #f6f5f2, paper2 #efeee9. Two-tone system: graphite (ink) for text/CTA/focus, platinum as the ONLY secondary accent (rail, OTP dash, dots, muted icons) — NO saturated color anywhere. Font: 'Inter' everywhere (weights 400/500/600/700/800) via Google Fonts, with font-feature-settings 'ss01','cv11','cv05' and a custom letterSpacing 'tightest' = -0.04em. Built on Tailwind (CDN) with a custom theme (ink/platinum/paper scales) and a small CSS layer for the .otp input states (focus = ink border + 4px ink/8 ring + lift, .filled state), the .verify-btn hover lift, the .hairline sheen, the .nav-link grow-from-left underline, the .grain veil and a @keyframes floatUp 'rise' entrance. Icons via Iconify (phosphor 'ph:*' set: aperture-bold, shield-check-fill, lock-key-fill, arrow-right-bold, clock-countdown, lock-simple, arrow-u-up-left). OTP JS handles auto-advance, backspace, numeric-only (blocks 'e'), paste-to-fill, dot syncing and a 30s resend countdown. The masked destination ('•••• 4471'), the 'Aperture' brand and the copy are illustrative placeholders. Fully responsive: the narrow 440px card recenters on all widths; OTP boxes widen 44px->50px at sm; nav center links hide below md and 'Sign in' hides below sm; the footer row stacks on mobile. Light mode, antialiased, smooth scroll.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
