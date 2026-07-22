# Design System — Puffy Cornflower + Coral Budgeting App Landing Page

> Category: Landing Pages  ·  Industry: Finance & Crypto
> Auto-scaffolded from prompt [`puffy-cornflower-coral-budgeting-app-landing-page`](../../prompts/puffy-cornflower-coral-budgeting-app-landing-page/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Claymorphism / soft-UI marketing register - a calm, friendly, confident landing where every surface is a puffy extruded piece of clay. Ground is a cool cornflower/periwinkle #c4cdec; raised clay panels are a touch lighter #cad3f1, recessed wells a touch darker #b7c1e6. Primary text is deep-indigo #2a3160 (the value anchor), muted text #5b628f. ONE warm coral accent #ff6f5e is reserved for primary CTAs and one full-bleed feature band; supporting jewel accents (teal #22b3a3, marigold #f4b73f, lilac #9b8cf0) appear ONLY as feature-card icon wells and the growth-chart bars. ONE rounded display face (Fredoka 700/600) carries the H1 and section headings; ONE body face (Figtree 400/500/600) carries the lead and body, with hierarchy from size and weight. Everything is rounded - cards ~26px, pills fully rounded (999px), icon wells circular. The clay material is pure CSS: a raised surface uses an outer light top-left highlight + an outer dark bottom-right shadow + a light inset top-left + a dark inset bottom-right; a recessed well inverts that with two inset shadows only; the coral CTA is a raised coral with a warm coral-deep shadow and a white inner gloss. HARD anti-washout rule: because clay collapses onto one tonal value when it goes monochrome, the load-bearing elements (headline, primary CTA, key numbers, product-demo widgets) must be the STRONGEST, highest-contrast things on screen - the demos sit on true-white cards so their ink numerals and colored fills read instantly. Calm and playful, never toy-ish or dated; no JavaScript is needed for the visible frame.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#c4cdec`
- `#cad3f1`
- `#b7c1e6`
- `#2a3160`
- `#5b628f`
- `#ff6f5e`
- `#22b3a3`
- `#f4b73f`
- `#9b8cf0`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a full desktop SaaS landing page whose entire personality is CLAYMORPHISM built purely from layered CSS box-shadows, no JavaScript. Use a cool cornflower/periwinkle clay ground #c4cdec, raised clay panels #cad3f1, recessed wells #b7c1e6, deep-indigo ink #2a3160 and muted #5b628f. Reserve ONE warm coral accent #ff6f5e for primary CTAs and one full-bleed band; use jewel accents (teal #22b3a3, marigold #f4b73f, lilac #9b8cf0) ONLY for feature-card icon wells and chart bars. Set the H1 (~56px, clamp) and section headings in Fredoka 700/600 and the lead/body in Figtree; build hierarchy from size and weight. Round everything: cards ~26px, buttons as fully-rounded pills, icon wells circular. Make the clay material as reusable CSS classes: raised = box-shadow of an outer light top-left highlight + an outer dark bottom-right shadow + a light inset top-left + a dark inset bottom-right; inse …

## 5. Layout

A vertical marketing page anchored on a real measured landing's furniture. Top: an airy STICKY NAV (raised clay logo chip + wordmark left, center ghost links, a recessed 'Log in' pill + a coral 'Try free' pill right). HERO (centered): a big bold indigo H1, a muted lead, a single ROW of three recessed clay trust-bullet chips with coral checks, then a CTA row (filled coral pill + raised ghost pill), with two very soft clay orbs as faint corner ambiance. TWO SIDE-BY-SIDE RAISED CLAY FEATURE CARDS, each: a jewel clay icon well, a heading, a body line, and a WHITE app-widget mockup (a savings card with a progress bar; a growth chart of colored clay bars). A FULL-BLEED SATURATED CORAL BAND: left a pill + heading + lead + white text link, right a big extruded clay savings RING (conic-gradient arc inside stacked coral clay discs). A THREE-UP RECESSED CLAY STAT STRIP with big ink numerals. A CLOSING CTA on one large raised clay panel (heading + coral pill + tiny social-proof caption). A CLAY FOOTER (logo + tagline + three link columns). On a narrow viewport the nav collapses to a compact bar (center links hide), the two hero cards stack full-width, the coral band stacks the ring above the copy, and the headline steps down via clamp.

## 6. Components

- **Pure-CSS clay material system** — The whole aesthetic is three reusable box-shadow recipes, so it needs no images and reproduces faithfully from a static template. Raised = puffy panels/buttons; inset = recessed wells, pressed pills and inputs; a coral variant for the primary CTA.
- **Clay savings ring (conic-gradient progress)** — A copy-worthy circular progress gauge that reads as extruded clay on the coral band, built with a CSS conic-gradient and no SVG (so no viewBox/seam risk).
- **White app-widget demos on clay cards (anti-washout)** — The two feature-card mockups deliberately break out of the periwinkle tonal band onto true-white cards so the product proof is the most readable thing on the card - the fix that keeps a clay page from washing to one value.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A puffy claymorphism landing page for a calm budgeting and savings app on a cool cornflower ground with one warm coral accent: an airy nav, a big rounded hero with trust bullets and dual CTAs, two feature cards with white app-widget mockups (a savings card and a colored-bar growth chart), a full-bleed coral band with a soft savings ring, a stat strip, a closing CTA and a footer. Reusable for any friendly, high-contrast soft-UI / neumorphism marketing site that must not wash out.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
