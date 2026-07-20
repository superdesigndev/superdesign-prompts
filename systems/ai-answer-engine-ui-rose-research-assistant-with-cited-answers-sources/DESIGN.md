# Design System — AI Answer Engine UI (Rose Research Assistant with Cited Answers + Sources)

> Category: AI Chat  ·  Industry: AI & Tech
> Auto-scaffolded from prompt [`ai-answer-engine-ui-rose-research-assistant-with-cited-answers-sources`](../../prompts/ai-answer-engine-ui-rose-research-assistant-with-cited-answers-sources/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Cool, crisp, light-mode product design, deliberately not the dark-violet/indigo AI cliche and not a warm-ivory editorial look. A cool paper canvas (#f5f6f8) with white surfaces (#ffffff), near-black ink (#14161b), muted slate meta text (#5b6472), hairline borders (#e6e8ec), and a subtle neutral fill (#eef0f3). ONE brand accent, rose/raspberry (#e11d48, hover #be123c), used sparingly for the brand glyph, inline citation number chips, links, the active source card (tinted #fff1f3 with a #fbcfd8 border), the active tab underline, and the send button. Three typefaces with clear jobs: Hanken Grotesk (600/700) for the question heading and section labels, Inter for all body and UI, JetBrains Mono for citation numerals, source domains, and URLs. Soft restrained shadows on white cards, rounded-2xl cards, rounded-full chips, hairline dividers, generous whitespace, an editorial rhythm rather than a dense dashboard.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#f5f6f8`
- `#ffffff`
- `#14161b`
- `#5b6472`
- `#e6e8ec`
- `#eef0f3`
- `#e11d48`
- `#be123c`
- `#fff1f3`
- `#fbcfd8`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a cool, crisp, light-mode AI answer engine. Canvas is cool paper #f5f6f8, surfaces white #ffffff, text near-black #14161b, muted slate #5b6472, hairlines #e6e8ec, subtle fill #eef0f3, with ONE accent, rose #e11d48 (hover #be123c), used sparingly for the brand glyph, inline citation number chips, links, the active source card (tinted #fff1f3, border #fbcfd8), the active tab underline, and the send button. Use Hanken Grotesk (600/700) for the question heading and section labels, Inter for all body and UI, and JetBrains Mono for citation numerals, source domains, and URLs. Soft restrained shadows on white cards, rounded-2xl cards, rounded-full chips, hairline dividers, generous whitespace. Keep it light-mode and frameless (the app screen fills the viewport, no browser or device frame). Do NOT use any purple / indigo / violet, do NOT use a dark app background, do NOT use teal or emera …

## 5. Layout

A three-zone frameless app shell: a slim left icon nav rail, a centered max-760px answer column, and a right Sources rail. The answer column is a single vertical read (question, tabs, source-chip strip, cited answer with an in-answer comparison card, related follow-ups, ask composer) so the eye trace is answer-first with citations traceable to the right-rail source cards. Fully responsive: below lg the Sources rail drops out of the row, and on mobile the left rail becomes a top hamburger bar while the Sources content stacks below the answer as its own section; no fixed element overlaps the answer.

## 6. Components

- **Inline citation chips** — Small rose superscript numbered badges embedded directly in the answer sentences (1, 2, 3, 4), in JetBrains Mono, that echo the numbering on the right-rail source cards so a reader can trace any claim to its source. This is the signature copy-worthy primitive of the answer-engine pattern.
- **Source-chip strip** — A horizontal row of small pill chips above the answer, each a favicon square + the site domain in mono + a rose citation number, ending in a '+3' overflow chip. A compact preview of the cited sources.
- **Sources rail with active-source card** — A right rail headed 'Sources 8' listing source cards (favicon + site title + domain.com in mono + a one-line snippet + a citation number badge). The card matching the currently-referenced citation is tinted rose with a rose border; a 'Show all 8 sources' button closes the list.
- **In-answer comparison card** — A clean two/three-column comparison table rendered inside the answer (Feature / RAG / Fine-tuning), so the synthesized answer contains a scannable structured block, not just prose.
- **Related follow-up list** — A RELATED block of four clickable follow-up question rows, each with a leading plus icon (rose on hover) and a trailing chevron, hairline-divided, that suggest next queries.
- **Ask-a-follow-up composer** — A rounded white card at the end of the answer column with an auto-grow input ('Ask a follow-up...'), a paperclip attach, a 'Sonar Pro' model chip (rose dot + caret), and a round rose send button. In normal flow (not fixed) so it never covers the answer.

## 7. Motion

REVIEW —
- ONE brand accent, rose/raspberry (#e11d48, hover #be123c), used sparingly for the brand glyph, inline citation number chips, links, the active source card (tinted #fff1f3 with a #fbcfd8 border), the active tab underline, and the send button
- Canvas is cool paper #f5f6f8, surfaces white #ffffff, text near-black #14161b, muted slate #5b6472, hairlines #e6e8ec, subtle fill #eef0f3, with ONE accent, rose #e11d48 (hover #be123c), used sparingly for the brand glyph, inline citation number chips, links, the active source card (tinted #fff1f3, border #fbcfd8), the active tab underline, and the send button

## 8. Voice & Brand

A clean, light AI answer engine UI, a Perplexity-style research assistant that answers a question with a synthesized, cited answer. Inline numbered citations trace to a Sources rail of source cards, a two-column comparison table sits inside the answer, and Answer/Sources/Images tabs, a source-chip strip, related follow-up questions, and an Ask bar with a model picker round it out. Cool paper canvas, ink text, and one confident rose accent, with Hanken Grotesk + Inter + JetBrains Mono. A slim left icon rail and a right Sources rail frame the answer column; fully responsive (the rail stacks below the answer on mobile). Copy it for any AI search, research assistant, RAG answer surface, or chatbot answer screen.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
