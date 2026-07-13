# Design System — AI Chat Workspace UI: Emerald Agent Builder with Live Preview

> Category: AI Chat  ·  Industry: AI & Tech
> Auto-scaffolded from prompt [`ai-chat-workspace-ui-emerald-agent-builder-with-live-preview`](../../prompts/ai-chat-workspace-ui-emerald-agent-builder-with-live-preview/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Fresh, calm, premium modern-SaaS AI product aesthetic that deliberately rejects the default indigo/violet/blue AI cliche in favor of a single confident emerald accent on a cool porcelain canvas. Canvas is near-white #fcfdfc, ink is a cool near-black #131815, muted text #5b655e, hairlines #e4e9e4; the icon rail is porcelain #eef1ed and the preview stage is pale mint-grey #f1f5f1. ONE accent, emerald #0ea968 (deep #0b8a54 for text-on-light), used sparingly for the brand mark, the active nav pill, the model dot, links, checks, and every primary button; tints are #e7f4ec fill with #cde7d7 borders, and the user bubble is #e8f4ee with a #d2e9db border. Three typefaces with clear jobs: Space Grotesk (geometric display) for the brand, project title, assistant name, headings and big numbers; Inter for all body and UI; JetBrains Mono for meta labels, file names, model chips, and the URL pill. Generous whitespace, soft 10-16px radii, hairline dividers, and restrained soft shadows (emerald-tinted only on primary buttons and the preview frame). Light mode, frameless: the app fills the whole viewport as a real desktop workspace, no browser or device chrome around it.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#fcfdfc`
- `#131815`
- `#5b655e`
- `#e4e9e4`
- `#eef1ed`
- `#f1f5f1`
- `#0ea968`
- `#0b8a54`
- `#e7f4ec`
- `#cde7d7`
- `#e8f4ee`
- `#d2e9db`

## 3. Typography

- `Verde`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a light, modern AI builder / chat workspace. Canvas near-white #fcfdfc, ink cool near-black #131815, muted #5b655e, hairline #e4e9e4; icon rail #eef1ed, preview stage pale mint-grey #f1f5f1. Use ONE accent, emerald #0ea968 (deep #0b8a54 on light), sparingly: brand mark, active nav pill, model dot, links, checks, primary buttons. Tints #e7f4ec with #cde7d7 borders; user bubble #e8f4ee / #d2e9db. Type: Space Grotesk for brand, titles, headings and big numbers; Inter for body and UI; JetBrains Mono for meta labels, file names, model chips, the URL pill. Soft 10-16px radii, hairline dividers, restrained emerald-tinted shadows only on primary buttons and the preview frame. Keep it light-mode and frameless, filling the viewport as a real desktop app. Do NOT use purple / indigo / violet, do NOT wrap it in a browser or device mockup, and do NOT let the accent green turn neon.

## 5. Layout

A three-zone desktop workspace that fills the viewport (height:100vh, panes scroll internally, no page scroll): a fixed 64px icon rail, a fixed 452px chat column, and a flexible live-preview panel. The chat column has a sticky header, a scrolling thread, and a sticky composer so the conversation scrolls between two pinned bars. The preview panel has a sticky toolbar over a scrolling canvas that holds a browser-framed render of the generated page. On narrow screens the icon rail and chat column collapse and the preview goes full-width.

## 6. Components

- **Generated-files card** — A manifest of the files the AI just produced, with per-language icon colors and line counts.
- **Model-picker chip** — A compact model selector used in both the header and the composer.
- **Preview / Code toggle** — A segmented control that switches the right panel between the rendered artifact and its source.
- **Browser-framed artifact canvas** — The device frame that makes the AI's output read as a live preview, not the product itself.
- **Assistant turn with checklist** — A frameless AI reply that shows reasoning as a scannable list of what it did.
- **Live-events stat mock** — The mini product screenshot inside the generated hero that sells the analytics story.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

An AI chat interface for an AI builder / agent workspace, the kind of UI you would copy to ship an AI product or coding agent. A slim icon rail, a chat thread where a "Verde" assistant streams a reply, drops a generated-files card (index.html, theme.css, pricing.tsx), and lists what it built, then a composer with an attach button, a "Verde 2 . Build" model picker, and a round emerald send button. On the right, a live Preview/Code panel frames the generated landing page (nav, hero, real-time stats, feature grid, pricing) inside a browser chrome with a Publish button, so it reads as the artifact the AI just built. Fresh emerald-on-porcelain palette, Space Grotesk display + Inter UI + JetBrains Mono, light mode, frameless. Reusable for any AI assistant, chatbot, LLM playground, agent builder, coding-agent front end, or copilot product.

Source: https://dribbble.com/shots/26274219-AI-Assistant-Sidebar-Interaction

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
