# Design System — Flowing Menu: Kinetic Fullscreen Studio Navigation with Marquee Hover Reveal

> Category: Components  ·  Industry: Agency & Studio
> Auto-scaffolded from prompt [`flowing-menu-kinetic-fullscreen-studio-navigation-with-marquee-hover-reveal`](../../prompts/flowing-menu-kinetic-fullscreen-studio-navigation-with-marquee-hover-reveal/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Bold, kinetic, high-contrast editorial. STRICT three-color palette: near-white canvas (#f4f4f2), near-black ink (#0a0a0a), and ONE electric-blue accent (#1f3bff) used only for the hover-reveal panel + marquee; 1px hairlines are ink at ~12% opacity. No gradients (except tiny duotone shapes inside the marquee tiles), no second accent, and deliberately NOT the default purple/indigo AI gradient. TWO typefaces by role: a super-condensed heavy display face (Anton) for the giant uppercase menu labels, and a monospace (IBM Plex Mono) for ALL furniture (index numbers, wordmark, descriptors, footer meta) at ~11-12px uppercase, letter-spacing ~0.14em. Aggressive scale ratio (giant labels vs tiny mono labels). The resting screen is near-monochrome and calm so the electric-blue reveal reads as pure energy; motion is the message.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#f4f4f2`
- `#0a0a0a`
- `#1f3bff`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a 100vh fullscreen navigation menu overlay for a creative studio using STRICTLY three colors: canvas #f4f4f2, ink #0a0a0a, and a single electric-blue accent #1f3bff (hairlines = ink at ~12%). NO gradients, no purple/indigo, no second accent. Use TWO typefaces by role: Anton (super-condensed heavy) for the giant uppercase menu labels, and IBM Plex Mono for ALL furniture (index numbers, wordmark, descriptors, footer meta) at 11-12px uppercase, letter-spacing ~0.14em. Keep an aggressive scale ratio (labels ~clamp(52px,8.5vw,120px) vs ~11px mono). Keep resting rows near-monochrome and calm so the electric-blue hover reveal pops. Motion is the point but legibility comes first.

## 5. Layout

A single 100vh screen as a CSS grid: a ~64px top bar, a 1fr menu stack of five equal full-width rows, and a ~44px footer bar (totaling exactly the viewport, no page scroll). Each menu row is a horizontal grid: mono index left, giant label center-left, mono descriptor + arrow right, with 1px hairline dividers between rows. The top row is frozen in its active reveal state to demonstrate the interaction; the other four are at rest. Each row is position:relative with overflow:hidden so the absolutely-positioned reveal panel is clipped to the row and can never spill into the header or a neighbor. Reflows to a taller stacked list on mobile.

## 6. Components

- **Flowing-menu row with vertical panel reveal** — The core interaction: a full-width menu row whose colored panel slides up on hover.
- **Horizontal text marquee with interleaved tiles** — The scrolling repeated label + thumbnail tiles that fill the revealed panel.
- **Giant condensed-grotesk menu label** — One oversized word per row, the visual spine of the menu.
- **Mono furniture system (index + descriptors + meta)** — All the small type: row numbers, wordmark, descriptors, footer.
- **Duotone marquee tile** — The small rounded image chips that ride the marquee.

## 7. Motion

REVIEW —
- STRICT three-color palette: near-white canvas (#f4f4f2), near-black ink (#0a0a0a), and ONE electric-blue accent (#1f3bff) used only for the hover-reveal panel + marquee; 1px hairlines are ink at ~12% opacity
- The resting screen is near-monochrome and calm so the electric-blue reveal reads as pure energy; motion is the message
- Keep resting rows near-monochrome and calm so the electric-blue hover reveal pops
- Motion is the point but legibility comes first
- A bold, kinetic fullscreen navigation menu (the "flowing menu" pattern) for a creative or motion studio

## 8. Voice & Brand

A bold, kinetic fullscreen navigation menu (the "flowing menu" pattern) for a creative or motion studio. Five oversized condensed-grotesk menu rows (WORK / STUDIO / SERVICES / JOURNAL / CONTACT) stack full-width, each with a mono index number, the giant uppercase label, and a small mono descriptor plus an arrow. On hover a solid electric-blue panel slides up to fill the row and a horizontal marquee scrolls the repeating item name interleaved with small rounded thumbnail tiles, the label flipping to white. A thin top bar (studio wordmark + a MENU / close glyph) and a mono footer (location, email, socials) frame it. Strictly three colors: near-white canvas, near-black ink, one electric-blue accent, so the blue reveal pops. Anton for the giant labels, a mono for all furniture. Reusable as the animated nav / menu overlay for any studio, agency, portfolio, or bold marketing site.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
