# Design System — The Atelier Brief — an editorial intake form, set like a letter

> Category: Forms & Contact  ·  Industry: General
> Auto-scaffolded from prompt [`the-atelier-brief-an-editorial-intake-form-set-like-a-letter`](../../prompts/the-atelier-brief-an-editorial-intake-form-set-like-a-letter/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Editorial, literary form UI that reads like a page in a quiet book. A warm cream paper ground (#faf6ef, deeper panels #f3ecdf) under a faint dotted 'grain' radial-dot texture (rgba(28,24,21,0.025), 4px tile). A near-black warm ink (#1c1815) for primary text and a softer ink (#54493f) for secondary, with a single muted burgundy accent (DEFAULT #7b2d3b, deep #5e1f2b, light #c98a93, bright #e3aab2 for use on dark grounds). A two-typeface system: Fraunces (an optical-size variable serif, weights 300-700, used at large opsz for display and 'opsz' 24 for field labels) is the editorial voice for headlines, labels and accents; Inter (sans, 300-600) carries body copy and small UI text. Generous whitespace, tight negative letter-spacing on the big serif display (tracking -0.01em) and wide uppercase tracking (0.22-0.28em) on eyebrows, links and buttons. No card chrome and almost no borders: structure comes from hairline rules (a 1px center-fading gradient rule), full-bleed color bands (cream / deep-ink / cream) and rhythm, not boxes. Inputs are borderless underline fields (transparent, only a 1px bottom border) that on focus deepen to burgundy with a soft 1px burgundy shadow under the line. Interactions are restrained and typographic: quiet links draw a burgundy underline left-to-right on hover (.link-quiet), the ink submit button darkens to burgundy, lifts 1px and widens its letter-spacing on hover; arrow icons nudge right. Calm, refined, human, unhurried, never busy or sterile.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#faf6ef`
- `#f3ecdf`
- `#1c1815`
- `#54493f`
- `#7b2d3b`
- `#5e1f2b`
- `#c98a93`
- `#e3aab2`

## 3. Typography

- `Selected work`
- `Submit the brief`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a warm, editorial form UI that reads like a letter set in a quiet book. Palette: cream paper background #faf6ef and a slightly deeper panel cream #f3ecdf; warm near-black ink #1c1815 for primary text and a softer ink #54493f for secondary text; a single muted burgundy accent #7b2d3b (deep #5e1f2b for hovers, light #c98a93 and bright #e3aab2 for accents on dark grounds). Lay a very faint dotted 'grain' texture over the whole body: background-image radial-gradient(rgba(28,24,21,0.025) 1px, transparent 1px) with background-size 4px 4px. Typography is a strict two-typeface system: Fraunces (a variable optical-size serif, weights 300-700, italic available) for every display word, section heading and form label (set big at high optical size with font-variation-settings 'opsz' 144 for the hero clamp and 'opsz' 24 for labels) and Inter (sans, weights 300-600) for body copy and small UI/ey …

## 5. Layout

A single editorial page in full-bleed horizontal bands: a sticky translucent nav, a tall serif hero, a full-bleed cream trust strip, THE form section (a two-column editorial layout: a narrow left intro column + a wider right form of underline inputs), a full-bleed near-black ink 'Selected work' band, a light 'Process' section, and a cream footer. The nav / hero / work / process / footer use a wide max-w-6xl column; the form section narrows to max-w-5xl for a more letter-like measure. Everything reflows to a single column on mobile: the nav links hide behind the persistent 'Start a brief' link, the form's two intro/form columns stack and the paired fields (Name/E-mail, Project/Budget) collapse to one-up, the trust strip condenses its brand list, and the work grid goes one-up.

## 6. Components

- **Underline input (.underline-input)** — 
- **Editorial serif label (.ed-label)** — 
- **Quiet link (.link-quiet)** — 
- **Ink submit button (.btn-submit)** — 
- **Hairline rule (.rule)** — 
- **Grain texture (.grain)** — 
- **Outline monogram brand mark** — 

## 7. Motion

REVIEW —
- Interactions are restrained and typographic: quiet links draw a burgundy underline left-to-right on hover (
- link-quiet), the ink submit button darkens to burgundy, lifts 1px and widens its letter-spacing on hover; arrow icons nudge right
- link-quiet' underline animates from width 0 to 100% in burgundy on hover (an ::after 1px bar); the primary button is an ink-filled #1c1815 rectangle with cream text and 0
- 22em uppercase tracking that on hover goes burgundy-deep #5e1f2b, translateY(-1px) and widens letter-spacing to 0
- 26em; arrow icons (lucide arrow-right / arrow-up-right) translate-x on hover

## 8. Voice & Brand

An editorial intake form set like a letter: a warm cream page in Fraunces serif + Inter with a single burgundy accent, borderless underline inputs with serif labels (Name / E-mail, Project / Budget, Message), structured by full-bleed cream/ink/cream bands and hairline rules instead of cards, and a quiet ink 'Submit the brief' button.

## 9. Anti-patterns

Built on the Tailwind CDN with a tailwind.config extend: custom colors cream #faf6ef, creamdeep #f3ecdf, ink #1c1815, inksoft #54493f, burgundy #7b2d3b, burgundydeep #5e1f2b, burgundylt #c98a93, burgundybright #e3aab2; fontFamily serif = Fraunces, sans = Inter. Fonts load from Google Fonts (Fraunces ital,opsz 9..144,wght 300..700 + Inter 300-600); icons are Iconify lucide:* via the iconify CDN. The body carries the .grain dotted texture and #faf6ef background with smooth scroll-behavior. The signature move is the borderless underline-input form (.underline-input) set with Fraunces serif labels (.ed-label, 'opsz' 24), structured by full-bleed cream/ink/cream bands, hairline gradient rules (.rule) and whitespace rather than cards or borders, with quiet typographic interactions (the .link-quiet underline reveal, the .btn-submit hover that goes burgundy + lifts + widens letter-spacing). The form is a real, accessible native HTML form (text/email inputs + textarea, real <label for> pairings); onsubmit is no-opped for the static demo. On a single static frame the underline-focus color shift, the .link-quiet underline reveal and the .btn-submit hover only fully show live. 'Atelier Brief', the brand names in the trust strip / selected-work band, and the contact details are illustrative placeholders for a by-correspondence design-studio intake/contact form.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
