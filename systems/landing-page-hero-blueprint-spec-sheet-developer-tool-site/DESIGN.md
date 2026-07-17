# Design System — Landing Page Hero: Blueprint Spec Sheet Developer Tool Site

> Category: Landing Pages  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`landing-page-hero-blueprint-spec-sheet-developer-tool-site`](../../prompts/landing-page-hero-blueprint-spec-sheet-developer-tool-site/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Industrial blueprint / spec-sheet restraint - a technical document that happens to sell a product. A cool slate #eef1f5 drafting-grid ground with near-black navy #101b28 ink, hairline #d3dae2 rules doing ALL separation, and exactly ONE signal-orange #e4572e accent that only ever marks meaning (the primary action, the running state, the one PASS, the SIGNED stamp) and never decorates. Everything is flat and sharp-cornered: no gradients, no glass, no glow, no bevels, one soft neutral shadow at most. Hierarchy comes from SIZE, CASE and SPACING - a massive tightly-tracked Archivo display against tiny 11px mono UPPERCASE labels - not from color. The register is instrument panel, not splash page: measurement rules, corner ticks, spec eyebrows, checksums, version numbers. The anti-slop signal is that the concept is STRUCTURED rather than asserted - the product's promise (a signed receipt for every deploy) is physically built as a perforated receipt block with a rotated rubber stamp, so the aesthetic generates the artifacts instead of skinning a generic dark-mono dev-tool page. No purple, no indigo, no violet, no default AI gradient, no centered-everything, no emoji, no lorem, no placeholder logo walls.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#eef1f5`
- `#101b28`
- `#d3dae2`
- `#e4572e`
- `#5a6675`
- `#ffffff`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a restrained INDUSTRIAL BLUEPRINT / SPEC-SHEET landing-page HERO for a developer or infra SaaS product on a single 1440-wide desktop viewport, and make it read like a technical document rather than a marketing splash. Ground it in cool blueprint slate #eef1f5 tinted by a faint 24px CSS drafting grid (repeating-linear-gradient, ~35% opacity, subtle - drafting paper, never a checkerboard), with near-black navy ink #101b28, muted #5a6675, white #ffffff surfaces, and 1px #d3dae2 hairlines doing ALL the separating. Use EXACTLY ONE chroma - signal-orange / vermilion #e4572e - and spend it ONLY where it means something: the primary button, the eyebrow tick, the version number, the single running state, the one PASS token, the stat underline ticks, the SIGNED stamp. Use THREE type roles strictly: Archivo 700 for a giant LEFT-aligned display headline (76px / line-height 1.02 / letter-spaci …

## 5. Layout

A single top-of-page hero on a blueprint-grid ground. A hairline-ruled nav on top; then an ASYMMETRIC 58/42 split hero, left-aligned, with the eyebrow + giant headline left and the subtitle + butt-joined CTA/command-pill + risk-reversal line right; then a full-width product mockup card with corner ticks and a measurement rule holding a stage rail, a stage timeline, a log table and a signed-receipt block; then a three-cell stat band divided by vertical hairlines; then a full-width ink mono ticker. On a narrow viewport the nav collapses to the monogram + primary button, the headline steps down in size and eases its tracking, the split stacks to one column, the mockup's rail becomes a horizontal scrollable row of stage chips, the log table drops its TIMESTAMP column (never the ARTIFACT column, which carries the concept's evidence), the receipt block stacks with the stamp staying stamp-sized and left-anchored, and the stat band becomes three stacked cells divided by horizontal hairlines.

## 6. Components

- **Signed-receipt block with perforation and rotated rubber stamp** — The page's concept payoff and its most stealable device: a torn-off receipt joined under the pipeline log table, carrying mono receipt-number / sha256-checksum / signer data pairs and a rotated vermilion SIGNED stamp. It turns the headline's promise ('a receipt for every commit') into a real artifact instead of a claim, which is what lifts the page out of the generic slate-and-mono dev-tool genre.
- **Blueprint measurement chrome (drafting grid, corner ticks, dimension rule)** — The pure-CSS technique that makes the spec-sheet register real rather than asserted, and the reason the style survives a static screenshot and template reproduction: a drafting-paper grid, L-shaped corner ticks and a labelled dimension rule over the product mockup.
- **Reconciling pipeline mockup (stage rail + fluid timeline + log table)** — The copy-worthy asset: an HTML-native product mockup (not an image) whose four surfaces tell ONE consistent story, so a builder can drop their own stages in and ship it. Its fluid-HTML timeline deliberately avoids scaled-SVG text, which renders oversized on desktop and illegible on mobile.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A restrained BLUEPRINT-style landing page hero for a developer / infra SaaS product, built like an industrial spec sheet rather than a marketing splash. A cool slate #eef1f5 drafting-grid ground, near-black navy ink, hairline rules and sharp radius-0 corners, with ONE signal-orange #e4572e accent. An asymmetric split puts a giant Archivo headline against a right column with the subtitle and a primary button butt-joined to a `$ npx forge init` command pill. The signature move is a product mockup card with corner ticks and a measurement rule holding a pipeline run: a stage rail with durations, a stage timeline, a log table, and a signed-receipt block with a perforation and a rotated SIGNED stamp. Closes with a stat band and a mono ticker. Reusable for any CI/CD, build, observability, security or infra-tool landing hero.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
