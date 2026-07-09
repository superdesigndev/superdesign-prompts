# Design System — Warm Terracotta AI Chat Interface

> Category: AI Chat  ·  Industry: AI & Tech
> Auto-scaffolded from prompt [`warm-terracotta-ai-chat-interface`](../../prompts/warm-terracotta-ai-chat-interface/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Warm terracotta editorial, the deliberate opposite of the default dark-indigo/violet AI-chat cliché. A cream/paper canvas (#FAF6F0) with near-black ink (#1A1A1A) and ONE warm accent, terracotta (#C4552F, deep #A8421F on hover / inline code), used sparingly for the brand mark, active states, links, list numerals, and the send button. Three typefaces with clear jobs: Fraunces (serif display, some italic) for the brand wordmark, conversation title, assistant name, and list numerals; Inter for all body and UI; JetBrains Mono for code. Hairline dividers (#E7DCCC), soft paper surfaces (#F4ECE1) for the sidebar and inline code, and soft-terracotta (#F0E3D5, border #EAD6C4) for the user bubble and active history pill. The code block is a warm charcoal (#262019, header #1F1A15) with muted syntax tones (keyword #E39B6E, string #C9B78E, comment #8A7E6C, function #EAD9BE), not neon. Generous whitespace and an editorial, restrained rhythm rather than a dense dashboard. Light mode; frameless (a real full-viewport app screen, no browser or device chrome).

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#FAF6F0`
- `#1A1A1A`
- `#C4552F`
- `#A8421F`
- `#E7DCCC`
- `#F4ECE1`
- `#F0E3D5`
- `#EAD6C4`
- `#262019`
- `#1F1A15`
- `#E39B6E`
- `#C9B78E`
- `#8A7E6C`
- `#EAD9BE`

## 3. Typography

- `New conversation`
- `Terra`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a warm, editorial AI chat interface. Canvas is cream #FAF6F0, text near-black #1A1A1A, with ONE accent, terracotta #C4552F (deep #A8421F for hover and inline code), used sparingly. Use Fraunces (serif, some italic) for the brand wordmark, conversation title, assistant name, and ordered-list numerals; Inter for all body and UI; JetBrains Mono for code. Sidebar and inline-code surfaces are paper #F4ECE1; the user bubble and active history item are soft-terracotta #F0E3D5 with a #EAD6C4 border; dividers are hairline #E7DCCC. The code block is warm charcoal #262019 with muted syntax tones, never neon. Keep it light-mode, frameless (the app screen fills the viewport, no browser/device frame), with generous whitespace and an editorial rhythm. Do NOT use any purple / indigo / violet, do NOT use a dark background for the whole app, and do NOT center everything.

## 5. Layout

A classic two-pane chat app: a fixed 264px left conversation sidebar and a flex main column. The main column is a single scroll container with a sticky top bar, a centered ~760px message thread, and a sticky bottom composer, so content scrolls between two pinned chrome bars. On mobile the sidebar collapses behind a hamburger and the thread + composer go full-width.

## 6. Components

- **Frameless message thread (user card + frameless assistant)** — Asymmetric turn treatment that reads instantly without heavy bubbles.
- **Model chip in the composer** — An inline model selector that names the assistant + mode.
- **Warm code block with filename + Copy header** — A syntax-highlighted code block that matches the warm palette instead of a neon IDE theme.
- **Date-grouped chat history with active pill** — A scannable sidebar history grouped by day.
- **Serif-numeral ordered list** — Editorial ordered-list styling that reinforces the brand's serif voice.
- **Terracotta typing indicator** — A loading state for the assistant turn.

## 7. Motion

REVIEW —
- A cream/paper canvas (#FAF6F0) with near-black ink (#1A1A1A) and ONE warm accent, terracotta (#C4552F, deep #A8421F on hover / inline code), used sparingly for the brand mark, active states, links, list numerals, and the send button
- Canvas is cream #FAF6F0, text near-black #1A1A1A, with ONE accent, terracotta #C4552F (deep #A8421F for hover and inline code), used sparingly
- User turns are right-aligned soft-terracotta cards; assistant turns are left-aligned, frameless, with a serif-italic "Terra" name, editorial paragraphs, a serif-numeral ordered list, a dark warm code block with a filename + Copy header, a check-icon bullet list, and a hover action row

## 8. Voice & Brand

A warm, editorial AI chat interface (chatbot UI) that ditches the default dark-purple AI look for a cream-paper canvas, near-black ink, and a single terracotta accent. A collapsible left sidebar holds a terracotta "New conversation" button, a search field, and date-grouped chat history (Today / Yesterday) with an active-item pill and a user account row. The main column is a single scroll container: a sticky glass top bar with the conversation title in an editorial serif, a centered max-width message thread, and a sticky bottom composer. User turns are right-aligned soft-terracotta cards; assistant turns are left-aligned, frameless, with a serif-italic "Terra" name, editorial paragraphs, a serif-numeral ordered list, a dark warm code block with a filename + Copy header, a check-icon bullet list, and a hover action row. The composer is a rounded card with an auto-grow textarea, an attach button, a model chip ("Terra 1.5 · Editorial"), a "return to send" hint, and a round terracotta send button. Fraunces serif display + Inter body + JetBrains Mono code, warm cream + ink + terracotta only, frameless and responsive (the sidebar collapses to a hamburger on mobile). Reusable for any AI assistant, chatbot, LLM playground, or conversational product.

Source: https://dribbble.com/shots/26274219-AI-Assistant-Sidebar-Interaction

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
