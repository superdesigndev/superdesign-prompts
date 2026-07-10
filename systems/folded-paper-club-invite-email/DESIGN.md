# Design System — Folded-Paper Club Invite Email

> Category: Email & Newsletter  ·  Industry: General
> Auto-scaffolded from prompt [`folded-paper-club-invite-email`](../../prompts/folded-paper-club-invite-email/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Edgy, industrial, underground. Extreme contrast between a deep-black canvas and a bright-red hero panel that simulates a creased, folded sheet of paper (a grid of fold lines + soft crease shadows + paper grain). Flat near-black type is 'printed' on the red paper, with microcopy slightly rotated to follow the folds. Minimal, no-nonsense: Inter Tight sans, italics to differentiate data points, tracked-caps micro-labels.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#0a0a0a`
- `#050505`
- `#e5342b`
- `#141210`

## 3. Typography

- `The Night`
- `Entry`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design an underground club / event RSVP email in a centered max-width 600px column on a near-black surface (#0a0a0a) over a black body (#050505). Typeface: Inter Tight. The centerpiece is a bright-red (#e5342b) hero panel that reads as a FOLDED SHEET OF PAPER, built purely in CSS: a base red, per-cell tonal shading (so each folded rectangle catches light differently), a grid of fold creases (each a dark valley + a light ridge), a subtle SVG fractal-noise grain, and an inset shadow. Flat near-black (#141210) type is printed on the paper; microcopy is slightly rotated (-2deg to +1deg) to sit on the folds. A ~64px font-800 uppercase headline, a rotated credits grid, and a solid near-black RSVP button (red label). Below the flyer, brief text blocks on black use a red tracked-caps kicker + white/60 body. Email-safe: centered column, no sticky nav.

## 5. Layout

Centered ~600px column: (1) header (series name + volume), (2) folded red-paper flyer panel holding all key info + RSVP, (3) two brief text blocks ('The Night' / 'Entry') on black, (4) footer with unsubscribe. Reflows to one column at ~380px (credits grid stays 2-up).

## 6. Components

_REVIEW: no components captured._

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

An edgy, underground event RSVP email in a centered 600px column: a deep-black surface framing a bright-red hero panel that reads like a folded-paper flyer or ticket stub, with fold-crease grid lines and flat near-black type. The flyer embeds the key info (host, music, doors, date, location) plus an RSVP button; brief 'The Night' / 'Entry' text blocks sit below on black. Reusable for nightclubs, secret gigs, limited-capacity events, and streetwear drops.

## 9. Anti-patterns

Email layout: centered ~600px column, no sticky nav. IMPORTANT for implementers: keep the flyer's vital info (host, music, doors, date, location, RSVP) as LIVE HTML TEXT layered over the CSS paper texture, do NOT rasterize the flyer into a single background image, so the info still shows when a client blocks images; if a texture image is used, provide a real fallback text block + alt text. Generic placeholder event ('Basement Series') and sample details so the spec is reusable. The reusable value is the folded-paper 'printed flyer' email system (CSS crease texture + flat rotated type) and the intimate RSVP structure. Source system: reverse-engineered from a Canva typographic club-flyer (measured black + crumpled red-paper #e5342b, Helvetica Now, rotated microcopy).

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
