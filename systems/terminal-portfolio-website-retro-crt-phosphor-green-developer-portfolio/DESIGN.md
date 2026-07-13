# Design System — Terminal Portfolio Website: Retro CRT Phosphor-Green Developer Portfolio

> Category: Portfolios  ·  Industry: Personal & Portfolio
> Auto-scaffolded from prompt [`terminal-portfolio-website-retro-crt-phosphor-green-developer-portfolio`](../../prompts/terminal-portfolio-website-retro-crt-phosphor-green-developer-portfolio/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

A retro CRT phosphor-green TERMINAL aesthetic applied to a personal developer portfolio. A pure-black #000000 canvas is washed with two faint green radial glows (rgba(57,255,122,0.08) top-right, 0.05 left) and covered by a fixed CRT SCANLINE overlay so the whole page reads as a glowing monitor. Phosphor green #39ff7a is the single accent and carries the entire UI via text-shadow glow; supporting greens are dimmer #2bbf5c and faint #1c7a3c, body text is a muted sage #5f8d68, headings/strong ink is near-white #eafff1, and one disciplined amber #ffd24a marks a live 'available' status dot and one or two highlighted tags (a cyan #5cf6ff shows only on the path/prompt glyphs). EVERYTHING is monospace: JetBrains Mono (400-800, primary) + IBM Plex Mono (secondary); hierarchy comes from SIZE + WEIGHT + GLOW, not from a second typeface. The shape language is a flat console: near-black panels (#050805 / #070b07) hairlined in dim green (#143614 / brighter #1f4d1f), 3-8px radii only, ASCII '[x]' bracket bullets instead of icon ticks, blinking block cursors, and a fake-terminal window frame (traffic-light dots + a mono path label) around the whole page. The mood is a live REPL / hacker console, warm and dev-native, never soft, glossy or playful. Absolutely no purple/indigo gradient, no Inter, no emoji headings, no centered-everything blandness (this is left-aligned, command-driven).

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#000000`
- `#39ff7a`
- `#2bbf5c`
- `#1c7a3c`
- `#5f8d68`
- `#eafff1`
- `#ffd24a`
- `#5cf6ff`
- `#050805`
- `#070b07`
- `#143614`
- `#1f4d1f`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a retro CRT phosphor-green TERMINAL developer PORTFOLIO for a single 1440-wide desktop page, framed as one fake terminal window. Canvas: pure black #000000 washed with two faint green radial glows (rgba(57,255,122,0.08) top-right, rgba(57,255,122,0.05) left); cover the whole viewport with a fixed CRT SCANLINE overlay (a pointer-events-none, high-z-index element painted with a repeating-linear-gradient of faint dark horizontal lines at ~3-4px pitch, mix-blend-mode multiply, opacity ~0.5). Make PHOSPHOR GREEN #39ff7a the single accent doing all the work via a text-shadow glow (0 0 8px rgba(57,255,122,0.45), 0 0 24px rgba(57,255,122,0.18)); support it with dimmer #2bbf5c and faint #1c7a3c greens, a muted sage #5f8d68 for body text, near-white #eafff1 for headings/strong, and ONE disciplined amber #ffd24a for a live 'available' status dot + one or two highlighted tags. Use MONOSPACE e …

## 5. Layout

One fake terminal WINDOW frames the entire single-column page (max ~1120px). Title bar: three traffic-light dots + a mono path label 'ada@portfolio: ~/dev' + right-aligned mono nav (~/work, ~/stack, ~/contact) + an amber blinking 'available for work' status. Body reads top-to-bottom like a shell session, each section prefixed by a command prompt: (1) a 'whoami --full' HERO (glowing ~60px name banner + role line + intro + ASCII meta checks + two command-style CTA buttons); (2) a 'neofetch' IDENTITY CARD (pixel ASCII avatar left, key/value identity list right, color-swatch strip); (3) an 'ls -la ~/projects' 2x2 WORK GRID of framed project cards; (4) a 'cat stack.txt' PROFICIENCY block of mono skill-bar meters (two columns of four); (5) a './contact --hire' CTA panel (copyable mail command box + blinking caret + social pills); (6) a shell-echo FOOTER (copyright echo + blinking cursor + fake git status). Thin green gradient rules separate sections. On a narrow viewport the nav collapses, the project grid and skill columns stack to one column, and the neofetch card stacks the avatar above the identity list.

## 6. Components

- **Fake terminal window frame** — One macOS-style terminal window that frames the whole portfolio and instantly signals 'terminal' while staying a recognizable personal site.
- **CRT scanline + phosphor glow system** — The recurring retro-monitor treatment that gives the whole page its glowing-CRT terminal feel.
- **neofetch identity card** — The iconic developer identity block: a pixel ASCII avatar beside a key/value system-info list, which reads instantly as 'this is a developer's personal profile'.
- **ls ~/projects work card** — A framed project card styled as a directory listing entry, the portfolio's work/proof section and the most copy-worthy remixable block.
- **ASCII bar skill meter** — A monospace proficiency row that shows skills as glowing terminal-style bar graphs instead of generic dots.
- **Command-box CTA + blinking cursor** — A copyable shell-command contact box with a live blinking caret, the page's primary conversion artifact.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A retro CRT terminal-style developer PORTFOLIO website in phosphor green on a near-black canvas, framed as one fake terminal window with traffic-light dots and a monospace nav. Reads top-to-bottom like a shell session: a `whoami` hero with a big glowing name banner and role line, a neofetch-style identity card (a pixel ASCII avatar plus a key/value list of OS, role, stack, status), an `ls ~/projects` grid of framed project cards with tech tags and live/source links, a `cat stack.txt` block of ASCII skill-bar meters, and a `./contact` CTA with a copyable mail command and social pills. JetBrains Mono everywhere, a fixed CRT scanline overlay, phosphor-green glow text, blinking block cursors, and one disciplined amber accent. Grab this terminal portfolio prompt and swap in your own name, projects, stack and links.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
