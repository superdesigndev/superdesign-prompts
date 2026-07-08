# Design System — Create your account · Promptly — split-image emerald sign-up

> Category: Auth & Login  ·  Industry: SaaS
> Auto-scaffolded from prompt [`create-your-account-promptly-split-image-emerald-sign-up`](../../prompts/create-your-account-promptly-split-image-emerald-sign-up/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Clean, modern SaaS aesthetic in the Inter typeface, built on a slate neutral scale with a single emerald accent. The left form half is bright white with soft slate-50 input fills; the right half is a dark navy-to-near-black radial 'mesh' with emerald glow blooms and a faint 56px grid masked by a radial fade. Generous rounding (rounded-xl / 2xl), soft layered shadows tinted emerald, and micro-interactions (lift-on-hover CTA, focus ring, floating card, pulsing 'generating' dot).

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#f8fafc`
- `#f1f5f9`
- `#e2e8f0`
- `#cbd5e1`
- `#94a3b8`
- `#64748b`
- `#475569`
- `#334155`
- `#1e293b`
- `#0f172a`
- `#020617`
- `#ecfdf5`
- `#d1fae5`
- `#a7f3d0`
- `#6ee7b7`
- `#34d399`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a modern SaaS account-creation screen using the Inter font family (weights 400/500/600/700/800, antialiased, font-feature-settings cv11 + ss01). Use a slate neutral palette (slate-50 #f8fafc, 100 #f1f5f9, 200 #e2e8f0, 300 #cbd5e1, 400 #94a3b8, 500 #64748b, 600 #475569, 700 #334155, 800 #1e293b, 900 #0f172a, 950 #020617) with a single emerald accent (emerald-50 #ecfdf5, 100 #d1fae5, 200 #a7f3d0, 300 #6ee7b7, 400 #34d399, 500 #10b981, 600 #059669, 700 #047857, 800 #065f46, 900 #064e3b). Body text slate-900 on white. The primary CTA is emerald-700 #047857 filled with white text and an emerald-tinted shadow (shadow-lg shadow-emerald-700/30). Use generous border-radius: inputs and the CTA rounded-xl (12px), logo marks rounded-xl/2xl, social buttons rounded-xl, pills rounded-full. Inputs have a 1px slate-200 border on a translucent slate-50/60 fill; on focus the border turns emerald-500 …

## 5. Layout

A full-height page = sticky 64px (h-16) nav + a CSS grid main that is one column on mobile and two columns at lg (grid-cols-[1fr_1.04fr], the brand panel slightly wider). Left = vertically + horizontally centered form column capped at max-w-[420px]; right = a dark aside that only shows at lg and arranges its content top (brand chip) / middle (floating mock) / bottom (testimonial) via flex justify-between with p-12 to p-16 padding.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

REVIEW —
- Generous rounding (rounded-xl / 2xl), soft layered shadows tinted emerald, and micro-interactions (lift-on-hover CTA, focus ring, floating card, pulsing 'generating' dot)
- Hover the CTA lifts 1px (translateY) with a deeper emerald-800 #065f46 background and a 14px/30px emerald shadow

## 8. Voice & Brand

A two-column desktop sign-up page: focused email + Google/GitHub social form on a bright white left half, dark emerald 'brand-mesh' panel with a floating product mock and testimonial on the right; sticky translucent nav, Inter, slate neutrals with a single emerald accent.

## 9. Anti-patterns

Single-accent system: emerald is the only chromatic color, everything else is the slate neutral scale, so the accent always reads as the action. The dark right panel is purely decorative social proof (hidden < lg) and the form alone must stand on its own when it collapses. Inter is loaded from Google Fonts with cv11/ss01 stylistic sets enabled. All emerald and slate hex values are exact and should be preserved. No em-dashes in any copy; the 'Prompt → UI' arrow and CTA arrows use icon glyphs, not text dashes.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
