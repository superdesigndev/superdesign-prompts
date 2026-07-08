# Design System — Synapse

> Category: Landing Pages  ·  Industry: General
> Auto-scaffolded from prompt [`synapse`](../../prompts/synapse/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style essence relies on a 'Vantablack' foundation with layers of transparency and glowing blurs. Typography pairings utilize 'Instrument Serif' for high-impact headings and 'Inter' for crisp readability. Motion is central, featuring infinite tickers, floating orbs, and subtle bounce animations.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#030303`
- `#8B5CF6`
- `#06B6D4`
- `#10B981`
- `#a78bfa`
- `#ffffff`
- `#22d3ee`

## 3. Typography

- `Vantablack`
- `Instrument Serif`
- `Inter`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

### Visual Theme
- **Base Background:** #030303 (Solid Black).
- **Accent Colors:** Violet (#8B5CF6), Cyan (#06B6D4), Emerald (#10B981 for status).
- **Typography:** 
  - Headings: 'Instrument Serif', Weight: 400-500, Tracking: -0.02em to -0.05em.
  - Body/UI: 'Inter', Weights: 300, 400, 600. 
  - Data/Metrics: 'Inter' or Monospace, Tracking: Widest (0.2em) for labels.
- **Gradients:** 
  - Violet Glow: `rgba(139, 92, 246, 0.4)` blur(40px to 120px).
  - Cyan Glow: `rgba(6, 182, 212, 0.4)` blur(40px to 120px).
  - Text Shimmer: Linear gradient (90deg, #a78bfa 0%, #ffffff 40%, #ffffff 60%, #22d3ee 100%) background-size 200%.
- **Effects:** 
  - Glassmorphism: `rgba(10, 10, 10, 0.7)` with `backdrop-filter: blur(16px)` and `border: 1px solid rgba(255, 255, 255, 0.1)`.
  - Shadows: Violet/Cyan outer glows (`box-shadow: 0 0 20px -10px #8b5cf6`).
- **Animations:** 
  - Floating Orbs: `translate …

## 5. Layout

The layout follows a modular vertical stack with a centered fixed-navigation pill. It transitions from a massive centered hero to a high-density horizontal ticker, then into a grid of feature cards, followed by a dark code integration block.

## 6. Components

- **Shiny Border Button** — A button with a continuously spinning conic gradient border that creates a thin neon line effect.
- **Interactive Feature Card** — Reveal-on-scroll card with floating iconography.

## 7. Motion

REVIEW —
- Motion is central, featuring infinite tickers, floating orbs, and subtle bounce animations

## 8. Voice & Brand

A high-performance 'neural' dark mode design system characterized by deep black backgrounds (#030303), vibrant neon accents in violet (#8B5CF6) and cyan (#06B6D4), and a sophisticated blend of editorial serif typography (Instrument Serif) with functional sans-serif (Inter). The style utilizes glassmorphism, animated mesh gradients, and 'shimmer' text effects to evoke a sense of advanced intelligence, encryption, and institutional-grade technology. Ideal for Fintech, AI, Cybersecurity, and Web3 verticals where speed, security, and technical sophistication are core values.

## 9. Anti-patterns

MUST: Maintain extreme contrast between the black background and white/neon elements. MUST: Use 'Instrument Serif' only for large headings (32px+) or brand elements. MUST: Ensure the 'glass' effects have high blur values (at least 16px) to maintain readability over background orbs. DO NOT: Use standard 0.5s transitions for everything; use `cubic-bezier(0.23, 1, 0.32, 1)` for a more technical, 'snappy' feel. DO NOT: Use pure greys for borders; always use low-opacity white (e.g., `white/5` or `white/10`).

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
