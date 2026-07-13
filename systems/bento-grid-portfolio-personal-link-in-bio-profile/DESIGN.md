# Design System — Bento Grid Portfolio (Personal Link-in-Bio Profile)

> Category: Portfolios  ·  Industry: Personal & Portfolio
> Auto-scaffolded from prompt [`bento-grid-portfolio-personal-link-in-bio-profile`](../../prompts/bento-grid-portfolio-personal-link-in-bio-profile/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Clean, modern, confident bento aesthetic on a cool paper-grey canvas (#f2f3f5) carrying a faint 24px dotted grid. The accent system is deliberately disciplined: a single teal (#0f9d8f, deep #0b7d72, tint #e7f5f1) as the primary color and a single warm apricot (#fb923c, deep #e07a1f) as the lone contrast pop, anchored by a near-black charcoal ink (#17181c) and a muted grey (#5b5e68) for secondary text. This is NOT a candy-multicolor bento: most tiles are white with a faint hairline border (rgba(23,24,28,0.09)); color pops are rationed to exactly one teal tile, one apricot tile, and two charcoal tiles, so the page reads modern-restrained, never busy. Everything is built from big friendly rounded-[26px] tiles, full-pill buttons and chips, generous padding, and two soft layered shadows (soft = 0 14px 34px -18px rgba(20,22,28,0.18), lift = 0 22px 50px -22px rgba(20,22,28,0.28)). Type is a two-face system: Bricolage Grotesque (600/700/800) for the name, tile headings and big stat numbers (characterful, tracking-tight), and Inter (400/500/600) for body and labels; uppercase tracked (0.16em) micro-labels ('NOW PLAYING', 'LATEST PROJECT', 'TOOLBOX', 'THE WEEKLY') act as tile eyebrows. Icons are Phosphor (ph:*-bold / -fill) via Iconify. Tiles lift on hover: translateY(-4px) via a springy cubic-bezier(.34,1.56,.64,1) over .35s. Keep copy warm, human, first-person, and free of em-dashes.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#f2f3f5`
- `#0f9d8f`
- `#0b7d72`
- `#e7f5f1`
- `#fb923c`
- `#e07a1f`
- `#17181c`
- `#5b5e68`

## 3. Typography

- `NOW PLAYING`
- `LATEST PROJECT`
- `TOOLBOX`
- `THE WEEKLY`
- `Say hello`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Build a clean, modern bento-grid personal profile page (link-in-bio style) on a cool paper-grey canvas, all rounded and confident. Load Bricolage Grotesque (600/700/800) and Inter (400/500/600) from Google Fonts. Configure a Tailwind palette: canvas #f2f3f5, ink #17181c, inksoft #5b5e68, line rgba(23,24,28,0.09), teal #0f9d8f, tealdeep #0b7d72, tealtint #e7f5f1, apricot #fb923c, apricotdeep #e07a1f. Set body bg-canvas with a faint dotted grid (radial-gradient dots rgba(23,24,28,0.035) 1px on a 24px tile). Define two shadows: soft = 0 14px 34px -18px rgba(20,22,28,0.18) and lift = 0 22px 50px -22px rgba(20,22,28,0.28). Center everything in a max-w-[1120px] container. Tiles use rounded-[26px]; buttons and chips are full pills. Give every tile a '.tile' class that lifts on hover (translateY(-4px) via transition cubic-bezier(.34,1.56,.64,1) .35s). Discipline the color: most tiles are white w …

## 5. Layout

A single centered column (max-w-[1120px]) with a slim top bar, the bento grid, and a small footer. The grid is grid-cols-1 on mobile and md:grid-cols-4 with auto-rows-[176px] and gap-4, tiling into a 4x4. Source/placement order and spans: (1) profile tile md:col-span-2 md:row-span-2, (2) photo tile md:col-span-2, (3) now-playing tile 1x1, (4) stat tile 1x1, (5) featured-project tile md:col-span-2, (6) map tile 1x1, (7) newsletter tile 1x1, (8) toolbox tile md:col-span-2, (9) email-CTA tile md:col-span-2. On mobile every tile becomes a single full-width row (spans reset) so nothing clips.

## 6. Components

- **Mixed-span bento grid** — The signature surface: a 4-column grid of very-rounded tiles that tiles into a 4x4 via one 2x2 anchor and several 2-wide and 1x1 tiles.
- **Bento profile anchor tile** — The 2x2 identity card that grounds the grid.
- **Now-playing tile with CSS equalizer** — A dark tile showing a currently-playing track with a live animated equalizer.
- **Stat pop tile** — A single saturated tile carrying one hero metric.
- **Inline-SVG map tile with pin** — A location card drawn entirely in CSS + SVG (no map tiles or external images).
- **Featured-project link tile** — A 2-wide row linking to the maker's latest work.
- **Rationed accent system** — The anti-candy discipline that keeps the bento reading modern, not busy.
- **Springy hover-lift** — A '.tile' interaction giving every tile a tactile lift.

## 7. Motion

REVIEW —
- Tiles lift on hover: translateY(-4px) via a springy cubic-bezier(
- tile' class that lifts on hover (translateY(-4px) via transition cubic-bezier(
- Bricolage Grotesque display plus Inter body, Phosphor icons; every tile lifts on hover

## 8. Voice & Brand

A clean, modern bento-grid personal portfolio / link-in-bio profile page on a cool paper-grey canvas with a disciplined teal (#0f9d8f) and apricot (#fb923c) accent duo and charcoal ink. A slim top bar sits over a mixed-span bento grid that tiles into a 4x4: a 2x2 profile tile (avatar, name, role, bio, an availability pill and four social buttons) anchors a workspace photo tile, a dark now-playing tile with a live CSS equalizer, a teal follower-stat tile, a featured-project tile, a teal-tint map tile with a location pin, an apricot subscribe tile, a toolbox chip tile, and a charcoal 'Say hello' contact tile. Bricolage Grotesque display plus Inter body, Phosphor icons; every tile lifts on hover. Reusable for any personal site, portfolio, or link-in-bio profile.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
