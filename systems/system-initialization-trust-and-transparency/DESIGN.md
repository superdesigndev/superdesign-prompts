# Design System — System Initialization - Trust & Transparency

> Category: Onboarding  ·  Industry: AI & Tech
> Auto-scaffolded from prompt [`system-initialization-trust-and-transparency`](../../prompts/system-initialization-trust-and-transparency/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is 'Industrial Editorial' - a blend of elegant serif headings, clean sans-serif body text, and monospaced technical labels. The palette is a warm neutral (Stone) with high-contrast dark text and a warm Amber accent for active states. Micro-interactions include smooth vertical expansion for details and pulse animations for live status indicators. A subtle noise texture layer is applied across the background for an organic, paper-like feel.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#FAFAF9`
- `#44403C`
- `#1C1917`
- `#57534E`
- `#E7E5E4`
- `#F59E0B`

## 3. Typography

- `Industrial Editorial`
- `DM Serif Display`
- `Inter`
- `JetBrains Mono`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a design with a background of #FAFAF9 (Stone-50) and a subtle 0.03 opacity noise texture. Typography: use 'DM Serif Display' for main headings (max-width 2xl, size 4xl to 6xl, leading-tight) with selective italics for emphasis; use 'Inter' for body text (size 1rem, weight 400, color #44403C); use 'JetBrains Mono' for all technical labels and metadata (uppercase, tracking-widest, size 0.75rem). Colors: Primary text #1C1917, secondary text #57534E, border #E7E5E4. Accent: #F59E0B (Amber-500). Animation: Details elements must use a 'sweep' animation (opacity 0 to 1, translate -10px to 0px over 0.3s). Hover states for interactive cards should transition border-color and background subtly over 150ms.

## 5. Layout

The layout follows a modular, section-based grid. Each major configuration topic is a section spanning the full width, divided into a 5-column guidance area (left) and a 7-column evidence/transparency area (right). A sticky bottom bar provides a persistent primary action.

## 6. Components

- **Custom Decision Radio** — A high-fidelity radio button replacement for decision-making.
- **Technical Architecture Details** — Expandable accordion for deep-dive technical verification.

## 7. Motion

REVIEW —
- Hover states for interactive cards should transition border-color and background subtly over 150ms

## 8. Voice & Brand

A high-trust, technical briefing design system for AI onboarding and system initialization. Featuring an editorial typography approach with a warm, neutral color palette (Stone and Amber), it utilizes a two-column grid to balance user configuration with technical evidence. Ideal for fintech, cybersecurity, AI safety, or enterprise SaaS where transparency, data privacy, and ethical alignment are core product values. The layout emphasizes vertical rhythm, semantic depth, and clear decision-making through structured guidance and live-updating evidence cards.

## 9. Anti-patterns

MUST: Maintain strict vertical alignment between the configuration options on the left and their corresponding evidence on the right. MUST: Use 'JetBrains Mono' for any text related to system IDs, technical specs, or data. MUST NOT: Use vibrant or 'friendly' marketing colors (like neon blues or rounded pill buttons); stick to the industrial/briefing aesthetic. MUST: Use the custom radio indicator (16px circle with a dot that only appears when the parent input is checked).

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
