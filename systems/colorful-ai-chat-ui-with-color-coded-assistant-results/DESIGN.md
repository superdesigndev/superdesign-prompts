# Design System — Colorful AI Chat UI with Color-Coded Assistant Results

> Category: AI Chat  ·  Industry: AI & Tech
> Auto-scaffolded from prompt [`colorful-ai-chat-ui-with-color-coded-assistant-results`](../../prompts/colorful-ai-chat-ui-with-color-coded-assistant-results/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Clean, colorful, product-grade AI-assistant register - the deliberate opposite of the default dark-indigo/violet AI-chat cliche and of a warm editorial serif chat. A WHITE #ffffff canvas with off-white #f8fafc sidebar/washes carries near-black grotesk type (ONE family, light/medium weights only, hierarchy from SIZE) and a SINGLE cobalt-blue #254fad interactive accent (active states, links, the model-chip dot). The personality is the assistant OUTPUT: a color-coded results table whose soft-tint status pills (green fill #e6f4ea + deep-green text #1f7a45; blue #e7eefb / #254fad; amber #fdf0dc / #8a5a12; grey #eef1f6 / #5b6472) and green-up / amber-down momentum make the answer read as real structured data, plus colored source chips and colored initial marks. Shapes are flat with soft shadows, 1px hairline borders (#e6e9ef), and generous radii (12px controls, 16-20px cards, 18px bubbles). The primary action is a flat DARK #181d26 pill (send button, New chat), never a gradient. No neon, no dark app background, no purple/indigo, no bold-black weights - the color comes only from the data pills, chips, and marks, keeping the chrome quiet. Light mode; frameless (a real full-viewport app screen, no browser/device chrome).

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#ffffff`
- `#f8fafc`
- `#254fad`
- `#e6f4ea`
- `#1f7a45`
- `#e7eefb`
- `#fdf0dc`
- `#8a5a12`
- `#eef1f6`
- `#5b6472`
- `#e6e9ef`
- `#181d26`

## 3. Typography

- `Leader`
- `On par`
- `Behind`
- `New entrant`
- `New chat`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a colorful, product-grade AI CHAT / assistant application UI for a 1440-wide desktop in LIGHT MODE, frameless (the app fills the viewport, no browser/device frame). Use a clean WHITE #ffffff main column beside a 268px off-white #f8fafc left sidebar (1px right hairline). Use ONE grotesk typeface (Geist / Neue-Haas-Grotesk feel) for everything at LIGHT/MEDIUM weights ONLY (400/500) and build hierarchy from SIZE: 16px/400 message body and user text, 16px/500 conversation title, 15px/500 assistant name, 14px sidebar items, 12px/500 uppercase muted labels. Confine the interactive accent to a single cobalt blue #254fad; make the primary action a flat DARK #181d26 pill (radius 12px), NEVER a gradient. Put the personality in the ASSISTANT OUTPUT: a white rounded-16 COLOR-CODED results table with soft-tint status pills (green #e6f4ea/#1f7a45 'Leader', blue #e7eefb/#254fad 'On par', amber # …

## 5. Layout

A two-column full-viewport app. LEFT: a 268px off-white sidebar (brand row, a flat dark 'New chat' pill, a search field, date-grouped conversation history with an active pill, a pinned account row). RIGHT: a white main column with a single vertical scroll - a sticky solid top bar (conversation title + model chip + share/more), a centered max-width ~760px message thread (a date separator, a right-aligned user bubble, a frameless assistant turn carrying the color-coded results card + a green-check takeaway list + colored source chips + a hover action row), and a sticky solid bottom composer (textarea + attach/tools + model chip + dark send button + disclaimer). On a narrow viewport the sidebar collapses to a hamburger, the thread goes full-width, and the results table scrolls horizontally inside its card.

## 6. Components

- **Color-coded assistant results table** — The signature: a white rounded card inside an assistant turn that presents structured data with color-coded status pills, so the answer reads as a real database result rather than plain prose.
- **Color-coded status pill** — The small color-coded pill that turns a table cell into structured, scannable status - the DNA borrowed from a no-code-database product and re-used in an assistant answer.
- **Frameless assistant turn** — The assistant message rendered without an outer bubble, so rich content (paragraphs, a table, a list, chips) can breathe - contrasted with the boxed user bubble.
- **Model-selector chip** — A compact pill that names and switches the model/mode, present in both the top bar and the composer - a core signal of an AI-assistant product.
- **Solid sticky composer** — The bottom message-input bar with a solid (not glass) fill so scrolled content never ghosts through it in a full-height view.
- **Conversation-history sidebar** — The left rail of date-grouped past chats with an active pill and an account row - the furniture that makes the screen read instantly as a chat product.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A colorful, product-grade AI chat UI (AI assistant interface) that ditches the default dark-purple AI look for a clean white canvas, ONE grotesk typeface at light/medium weights, near-black ink, and a single cobalt-blue accent. A left sidebar holds a flat dark "New chat" pill, a search field, and date-grouped conversation history (Today / Yesterday) with an active-item pill and an account row. The white main column has a sticky top bar with the conversation title and a model selector, a centered max-width message thread (right-aligned user bubble + a frameless assistant turn), and a sticky bottom composer with a model chip and a round dark send button. The assistant turn's signature is a color-coded results table: COMPANY / SEGMENT / STATUS VS US / MOMENTUM rows with color-coded soft-tint status pills (green Leader, blue On par, amber Behind, grey New entrant) and green-up / amber-down momentum, plus a green-check takeaway list and colored source chips. Reusable for any AI assistant, chatbot, LLM playground, copilot, or conversational data product.

Source: https://www.airtable.com/ (measured colorful product-UI register, transposed to an AI chat screen; corpus DP-409)

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
