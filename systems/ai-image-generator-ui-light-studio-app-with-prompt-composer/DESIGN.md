# Design System — AI Image Generator UI: Light Studio App with Prompt Composer

> Category: AI Chat  ·  Industry: AI & Tech
> Auto-scaffolded from prompt [`ai-image-generator-ui-light-studio-app-with-prompt-composer`](../../prompts/ai-image-generator-ui-light-studio-app-with-prompt-composer/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Calm, precise, content-forward creative-tool product UI - a real working AI image studio, not a landing page. Neutral chrome so the generated art carries all the color: a cool off-white #f7f8fa ground, white panels, ONE grotesk (Geist) in near-black #111318 with hierarchy from size and weight (14px/400 body, 500 labels and nav, 16 to 18px/600 panel titles), muted #6b7280 captions, and a mono only for the seed and dimensions. The shape language is FLAT and BORDER-ONLY: 1px #e6e8ec hairlines separate the three panes and every card, radii are tight (10 to 12px cards, 8px inputs and pills, 999px chips), and NO drop shadows sit on the app chrome. Color is rationed to a SINGLE channel - a cyan accent #06b6d4 on interactive and active states (active nav dot, selected-aspect ring, slider tracks, the Generating progress bar, the credits pill, the Generate spark), with a darker cyan #0891b2 for cyan text on white; the one filled control is the near-black #111318 Generate pill. Every saturated hue lives INSIDE the generated-image tiles, which are pure-CSS generative art, so the register stays quiet, neutral, and precise while the content pops. Anti-slop: never the default indigo/purple gradient chrome and never the dark-violet AI-chat cliche.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#f7f8fa`
- `#111318`
- `#6b7280`
- `#e6e8ec`
- `#06b6d4`
- `#0891b2`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a LIGHT, refined AI image-generation studio web app as a THREE-PANE app shell on a cool off-white #f7f8fa canvas, generically branded. Use ONE grotesk typeface (Geist) with hierarchy from size and weight, and a mono only for the seed and dimensions. Keep the chrome strictly FLAT and BORDER-ONLY: 1px #e6e8ec hairlines separate the panes and cards, tight radii (10 to 12px cards, 8px inputs and pills), NO drop shadows on chrome. Ration color to a SINGLE cyan accent #06b6d4 on active and interactive states (with darker cyan #0891b2 for cyan text on white); the only filled control is a near-black #111318 Generate pill. Put ALL saturated color inside the generated-image tiles only, rendered as pure-CSS generative art (layered conic + radial + linear gradients + a subtle feTurbulence grain), each a different vivid palette, never a stock photo. Build the three panes exactly: a fixed left  …

## 5. Layout

A three-pane creative-tool app shell on a cool off-white #f7f8fa canvas: a fixed ~230px left rail, a fluid center generation canvas, and a fixed ~300px right settings inspector, separated by 1px #e6e8ec hairlines. LEFT: brand mark + wordmark, a dark New-generation pill, a nav group (Generate active with a cyan dot, Gallery, Upscale, Edit / Inpaint, Assets), a HISTORY list of recent runs (tiny gradient thumb + truncated prompt + time), and a footer (cyan credits pill + Settings + user card). CENTER: a top strip (prompt echo + '4 variations, 1024x1024, Photoreal v3' meta + regenerate/download/favorite/share icons), a 2x2 grid of large generated-image tiles (per-tile hover toolbar + mono seed chip; one tile Generating... 62% over a skeleton), and a pinned prompt composer (textarea + aspect/model/style/reference chips + Generate pill). RIGHT: Settings - Model, Aspect ratio (segmented, selected cyan-ringed), Style chips, Steps + Guidance sliders (cyan tracks), a mono Seed with a randomize die, a Negative-prompt disclosure, a Batch-size stepper, and an estimated cost. On mobile the rail collapses to a top bar, the grid is one column, and the composer stays pinned full-width; nothing clips or overflows horizontally.

## 6. Components

- **Generated-image tile (pure-CSS generative art)** — A large aspect-square result tile whose image is layered CSS gradients (conic + radial + linear) plus a subtle feTurbulence grain overlay, so it reads as an AI-generated image with zero external assets. Hover reveals a frosted toolbar (upscale, variations, download, favorite) top-right and a mono seed chip bottom-left.
- **In-progress generation tile** — The loading state of a result: a soft cool skeleton with a gentle background pan and a centered frosted card showing 'Generating...', a cyan percentage, and a cyan progress bar - so an empty slot reads as an image forming, not a blank card.
- **Prompt composer with quick chips** — The docked input: a bordered white card with a borderless textarea and a row of quick chips (aspect / model / style / reference) plus the near-black Generate pill with a cyan spark and a keyboard hint.
- **Settings inspector control stack** — The right-pane diffusion controls: Model select, segmented Aspect ratio, Style chips, Steps + Guidance sliders on a cyan track, a mono Seed field with a randomize die, a Negative-prompt disclosure, a Batch-size stepper, and an estimated cost - the taxonomy a real text-to-image tool exposes.

## 7. Motion

REVIEW —
- Build the three panes exactly: a fixed left rail (brand, New-generation pill, nav with Generate active, a HISTORY list), a fluid center canvas (prompt echo + meta line, a 2x2 generated-image grid with per-tile hover toolbars + mono seed chips + one in-progress tile, and a pinned prompt composer with aspect/model/style/reference chips + the Generate pill), and a fixed right settings inspector (Model, Aspect ratio segmented, Style chips, Steps + Guidance sliders, a mono Seed with randomize, Negative-prompt disclosure, Batch-size stepper, estimated cost)

## 8. Voice & Brand

A clean, light AI image generation studio you can actually ship. It's a three-pane app: a left rail (brand, New-generation, nav, run history, credits), a center canvas with a prompt composer and a 2x2 grid of generated images (one mid-generation at 62%), and a right settings inspector with Model, Aspect ratio, Style, Steps, Guidance, Seed and Batch controls. Cool off-white chrome, a single cyan accent, flat border-only hairlines, one Geist grotesk. The generated tiles are pure-CSS generative art so there are no stock photos, and it is fully responsive. No default indigo/purple slop. Reusable for any text-to-image or AI creative tool.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
