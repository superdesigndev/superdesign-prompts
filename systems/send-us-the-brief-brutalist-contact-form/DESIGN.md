# Design System — Send Us the Brief — Brutalist Contact Form

> Category: Forms & Contact  ·  Industry: General
> Auto-scaffolded from prompt [`send-us-the-brief-brutalist-contact-form`](../../prompts/send-us-the-brief-brutalist-contact-form/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Neo-brutalist / brutalist aesthetic on a warm off-white 'paper' canvas (paper #f4f1ea) with near-black 'ink' text and borders (ink #0a0a0a) and exactly ONE high-voltage accent: acid yellow (acid #e8ff00). The defining moves are (1) thick flat ink borders everywhere (border-2 = 2px on small chips/inputs-in-nav, border-4 = 4px on cards, fields, buttons and section dividers), (2) HARD OFFSET DROP SHADOWS with zero blur and zero spread, rendered as solid ink rectangles via custom utilities: .shadow-hard = box-shadow 8px 8px 0 0 #0a0a0a, .shadow-hard-sm = 5px 5px 0 0 #0a0a0a, .shadow-hard-lg = 12px 12px 0 0 #0a0a0a (the dark footer CTA inverts this to a paper shadow, shadow-[8px_8px_0_0_#f4f1ea]), (3) a tactile button-press interaction .btn-press that on :active translates the element translate(4px,4px) and shrinks its shadow to 2px 2px 0 0 #0a0a0a, so chunky buttons physically depress into their shadow, and (4) an acid focus signal on form fields .field:focus = box-shadow 8px 8px 0 0 #e8ff00, 0 0 0 4px #0a0a0a (an acid hard shadow plus a 4px ink ring) with no default outline. Type is a brutalist pairing: Archivo (Google Fonts, weights 400/500/600/700/800/900) as the grotesk display/body face, almost always UPPERCASE and tracking-tight at the heaviest weight (font-900) for headlines, labels and buttons; and Space Mono (Google Fonts, weights 400/700) as the mono face for eyebrows, kickers, the marquee and micro-labels, set uppercase with wide letter-spacing (tracking-[0.2em] / [0.3em]). The hero headline is enormous (text-[15vw] -> sm:text-7xl -> lg:text-8xl, leading-[0.86]) with selected words wrapped in an acid highlight (bg-acid box-decoration-clone). Surfaces are hard-edged (no border-radius anywhere) and high-contrast: paper cards on a paper page outlined in ink with hard shadows, an inverted ink+acid logo tile and marquee, acid-filled accent chips and the primary button. Inputs sit on a pure-white fill (bg-white) inside their 4px ink border. ::selection is acid-on-ink. Mood: loud, blunt, confident, anti-mush, structural, a little playful, never soft or corporate.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#f4f1ea`
- `#0a0a0a`
- `#e8ff00`
- `#ffffff`

## 3. Typography

- `Three blunt steps`
- `Style`
- `Start`
- `Send`
- `We cast it`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a loud neo-brutalist contact page for a design-tool brand on a warm off-white 'paper' canvas (paper #f4f1ea) with near-black 'ink' text and borders (ink #0a0a0a) and exactly ONE accent: high-voltage acid yellow (acid #e8ff00). Register these as Tailwind theme colors (paper #f4f1ea, ink #0a0a0a, acid #e8ff00) and use Archivo (weights 400-900) as the grotesk display/body face plus Space Mono (400/700) as the mono face. Make the brutalist hardware the centerpiece: put thick flat ink borders on everything (2px on small chips, 4px on cards/fields/buttons/section dividers) with NO border-radius anywhere, and give cards and buttons HARD OFFSET DROP SHADOWS with zero blur rendered as solid ink rectangles via utilities .shadow-hard = box-shadow 8px 8px 0 0 #0a0a0a, .shadow-hard-sm = 5px 5px 0 0 #0a0a0a, .shadow-hard-lg = 12px 12px 0 0 #0a0a0a (invert to a paper shadow shadow-[8px_8px_0_0_# …

## 5. Layout

A full-bleed neo-brutalist one-page contact site on a paper canvas, all sections separated by full-width 4px ink borders (border-b-4 border-ink) and laid out inside a centered max-w-[1240px] mx-auto px-5 (md:px-8) container: (1) a sticky paper nav, (2) a scrolling ink marquee strip, (3) a hero with a 12-col grid (an 8-col headline block + a 4-col turnaround stat card, items-end), (4) THE FORM section as a 12-col grid (a 4-col left instruction rail beside an 8-col bordered form card; on mobile the card comes first via order), (5) a 'Three blunt steps' 3-card row, and (6) a dark ink footer with an acid CTA. The defining structural moves are the thick ink section dividers, the asymmetric 4/8 form split (a numbered instruction rail beside an oversized two-field form card), the label-left field rows (a 160px label column beside a 1fr input), the hard-offset-shadow cards, and the chunky depress-on-press buttons. Everything reflows to a single column below lg/md with no horizontal overflow at 390px.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

REVIEW —
- A sticky paper nav (an ink+acid logo tile + a FORMCAST wordmark, How it works/Library/Brief us hover-fill links and an acid 'Start' button) sits over a scrolling ink marquee strip and a hero (an acid eyebrow pill, a giant uppercase 'SEND US THE BRIEF

## 8. Voice & Brand

Loud neo-brutalist contact page for a design-tool brand (Formcast), built around a blunt two-field 'brief box'. A paper-and-ink base (paper #f4f1ea canvas, ink #0a0a0a text/borders) with exactly one high-voltage acid-yellow accent (#e8ff00), thick 2px/4px ink borders, hard offset drop shadows (zero blur, e.g. 8px 8px 0 0 #0a0a0a), depress-on-press chunky buttons, and an acid focus shadow on the fields, in a heavy Archivo (up to 900) + Space Mono pairing. A sticky paper nav (an ink+acid logo tile + a FORMCAST wordmark, How it works/Library/Brief us hover-fill links and an acid 'Start' button) sits over a scrolling ink marquee strip and a hero (an acid eyebrow pill, a giant uppercase 'SEND US THE BRIEF.' headline with 'brief.' highlighted in acid, and a '38s' avg-turnaround stat card). The centerpiece is a contact section split into a left rail of three numbered instruction tiles and a big bordered FORM CARD with an oversized E-Mail input + Message textarea, a Brutalist/Editorial/Minimal/Surprise-me style-chip row, and a chunky Cancel + acid 'Send' button row. A 'Three blunt steps' card row and a dark ink footer with an acid CTA close the page. The reusable signature is the neo-brutalist contact form: thick ink borders + hard offset shadows + one acid accent + a heavy Archivo/Space Mono voice.

## 9. Anti-patterns

Keep the neo-brutalist system intact, it is the whole point: a warm off-white 'paper' canvas (paper #f4f1ea) with near-black 'ink' text/borders (ink #0a0a0a) and EXACTLY ONE accent, high-voltage acid yellow (acid #e8ff00). Register these three as Tailwind theme colors and never introduce a second accent, a gradient, or any border-radius (every corner is hard). The brutalist hardware must stay: thick flat ink borders (border-2 on small chips/nav-icons, border-4 on cards/fields/buttons/section dividers), full-width border-b-4 border-ink section dividers, and HARD OFFSET DROP SHADOWS with zero blur rendered as solid ink rectangles via .shadow-hard (8px 8px 0 0 #0a0a0a) / .shadow-hard-sm (5px 5px) / .shadow-hard-lg (12px 12px), inverted to a paper shadow shadow-[8px_8px_0_0_#f4f1ea] on the dark footer CTA. Keep the tactile .btn-press depress (on :active transform translate(4px,4px) + shadow shrinks to 2px 2px 0 0 #0a0a0a) and the acid .field:focus signal (box-shadow 8px 8px 0 0 #e8ff00, 0 0 0 4px #0a0a0a, outline:none, ink/35 placeholders). Type is a brutalist pairing: Archivo (Google Fonts, 400-900) as the grotesk display/body face used almost entirely UPPERCASE at font-900 tracking-tight for headlines/labels/buttons (the hero H1 is text-[15vw]->sm:text-7xl->lg:text-8xl leading-[0.86] with the word 'brief.' wrapped in a bg-acid box-decoration-clone highlight), and Space Mono (400/700) as the mono face for the eyebrow pill, marquee, kickers, the 'Style' label and the footer credit, set uppercase with wide tracking ([0.2em]/[0.3em]). The structure is a one-page contact site inside a max-w-[1240px] container: a sticky bg-paper nav (an ink+acid logo tile + a FORMCAST wordmark, How it works/Library/Brief us hover-fill links, an acid 'Start ->' button) over an ink marquee strip (acid slogans, 22s loop), a hero (an acid eyebrow pill, a giant 'SEND US THE BRIEF.' headline with 'brief.' highlighted acid, a '38s' avg-turnaround stat card), THE FORM section (a grid lg:grid-cols-12: a lg:col-span-4 left rail of three numbered instruction tiles beside a lg:col-span-8 border-4 bg-paper .shadow-hard-lg FORM CARD with an E-Mail input + an 11-row Message textarea in label-left grid md:grid-cols-[160px_1fr] rows, a Brutalist/Editorial/Minimal/Surprise-me style-chip row, and a border-t-4 Cancel + acid 'Send ->' button row; on mobile the form card comes first via order), a 'Three blunt steps' grid md:grid-cols-3 of border-4 .shadow-hard cards (the middle one acid-filled), and a bg-ink text-paper footer ('Got a form to build? / Send the brief.' with 'Send the brief.' in acid + an acid 'Start now ->' CTA with the inverted paper shadow). Everything must reflow cleanly: the hero 12-col grid stacks below lg, the form 12-col grid stacks below lg (and the form card jumps above the instruction rail on mobile via order-1/order-2), the label-left field rows collapse to single-column below md, the step cards go single-column below md, the button row goes flex-col-reverse below sm (Send on top), the nav center links hide below md, and there is no horizontal overflow at 390px. Use Iconify MDI icons (mdi:vector-square, mdi:numeric-1-box, mdi:numeric-2-box, mdi:numeric-3-box, mdi:arrow-right-thick, mdi:keyboard-outline, mdi:auto-fix, mdi:export-variant). Copy is blunt, confident and human with zero em-dashes ('Send us the brief.', 'No fluff, no fake urgency.', 'Ship the form, not the meeting.', 'Done by lunch.'). Set ::selection to acid #e8ff00 background on ink #0a0a0a text.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
