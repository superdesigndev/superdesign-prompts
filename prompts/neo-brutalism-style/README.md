---
title: "Neo-Brutalism Style"
slug: neo-brutalism-style
tags: ["page", "landing page", "style"]
copyCount: 626
tryCount: 1681
source: https://superdesign.dev/library/neo-brutalism-style
---

# Neo-Brutalism Style

A high-impact Neo-Brutalist design system characterized by 'Acid' aesthetics. It features high-contrast color palettes (off-white, deep black, and neon yellow), heavy-weight typography, and 'hard' UI elements like non-blurred shadows and thick borders. The layout utilizes bento grids, oversized display text, and dynamic marquee components. Suitable for creative agencies, experimental e-commerce, fintech, and portfolio sites looking for a 'loud', digital-first brand identity.

![Neo-Brutalism Style](./preview.png)

## Prompt

```text
{
  "summary": "A bold, high-contrast Neo-Brutalist design system featuring heavy strokes, hard shadows, and an 'Acid' color palette with rhythmic animations and glitch effects.",
  "style": {
    "description": "The style is built on a foundation of Neo-Brutalism. It uses high-contrast pairings: a paper-like background (#F8F4E8), ink-black primary elements (#09090B), and a signature 'Acid' yellow-green (#D2E823) for highlights. Typography pairs the ultra-heavy 'Dela Gothic One' for display headings with the technical 'Space Grotesk' for body text. UI elements feature 2px to 4px solid black borders and 'hard' shadows (offset boxes with 0 blur). Micro-interactions include 'glitch' text animations, floating elements, and a custom mix-blend-difference cursor.",
    "prompt": "Apply a Neo-Brutalist 'Acid' aesthetic. Colors: Background #F8F4E8, Primary/Borders #09090B, Secondary/Accent #D2E823. Typography: Headings in 'Dela Gothic One' (all-caps, tracking-tighter), body text in 'Space Grotesk' (weights 400-700). UI Components: Every card/button must have a 2px solid #09090B border and a hard shadow (e.g., box-shadow: 4px 4px 0px 0px #09090B). Use a global SVG noise overlay at 3% opacity. Animations: Implement a glitch effect on hover for display text (rapid ±2px translations), a continuous marquee for highlights (linear 20s loop), and floating animations (y-axis ±10px) for accent cards. Buttons should translate [2px, 2px] and lose their shadow on click to simulate physical pressing."
  },
  "layout_and_structure": {
    "description": "The layout is structured with modular sections, utilizing bento-style grids and horizontal scrolling containers. It emphasizes vertical hierarchy with sticky navigation and alternating content blocks.",
    "prompts": [
      {
        "part": "Header & Navigation",
        "prompt": "Create a sticky navigation bar at the top with a 16px margin. Design: Background #F8F4E8 at 90% opacity with a heavy backdrop-blur (24px), 2px #09090B border, and 12px border-radius. Include a logo on the left using 'Dela Gothic One' and action buttons on the right. Buttons in the nav should have a 'hard-sm' shadow (2px offset) and transition to a secondary background (#D2E823) on hover."
      },
      {
        "part": "Hero Section",
        "prompt": "A 12-column grid layout. The left side (7 columns) features massive display text (font-size: 8rem, line-height: 0.85) with a glitch-on-hover effect. Include a secondary call-to-action button (20px padding, 2px border, 8px shadow) and a 'sticker' badge (pill-shaped, rotated -2 degrees, #D2E823 background). The right side (5 columns) features a primary image card with a 32px border-radius, #09090B border, and a floating asset card (box-shadow: 8px 8px 0px 0px #09090B) overlapping the main image."
      },
      {
        "part": "Bento Category Grid",
        "prompt": "A grid with varied aspect ratios (e.g., one large 2x2 card and two 1x1 cards). Large cards should have a dark background (#09090B) with high-contrast text and a subtle background image at 40% opacity with 'mix-blend-overlay'. Smaller cards should use 'hard-shadow' effects and radial dot patterns (1px dots every 20px) for texture. Each card must have a hover state that translates it 4px diagonally while removing the shadow."
      },
      {
        "part": "Horizontal Scrolling Product Section",
        "prompt": "A section titled 'NEW DROPS' with an arrow-navigation header. Below, a flex container with 'overflow-x-auto' and hidden scrollbars. Items should be 320px wide cards with square image containers, 2px borders, and 8px hard shadows. Include a 'Sold Out' state using a grayscale filter and 60% opacity on the image."
      },
      {
        "part": "Footer",
        "prompt": "A full-width #09090B background section. Typography should be inverted (text #F8F4E8). Features: A 3-column layout for 'Store', 'Info', and 'Social'. Use a monospaced font for small labels and uppercase tracking-wide for links. Include a newsletter signup with a transparent background, 2px border, and a #D2E823 submit button."
      }
    ]
  },
  "special_ui_components": [
    {
      "component": "Hard-Shadow Button",
      "description": "A tactile button that feels physical when clicked.",
      "prompt": "Background #09090B, Text #D2E823, Padding 16px 32px, Border-radius 12px, Border 2px solid #09090B. Shadow: 4px 4px 0px 0px #09090B. Hover state: TranslateX(2px) TranslateY(2px), Shadow: 0px 0px 0px 0px #09090B. Active state: TranslateY(4px)."
    },
    {
      "component": "Glitch Text",
      "description": "Interactive display text that jitters on hover.",
      "prompt": "Apply to 'Dela Gothic One' fonts. On hover, apply a CSS animation with 5 keyframes over 0.3s. Keyframes move the text: 0% (0,0), 20% (-2px, 2px), 40% (-2px, -2px), 60% (2px, 2px), 80% (2px, -2px), 100% (0,0). Set animation-iteration-count to infinite."
    },
    {
      "component": "Interactive Custom Cursor",
      "description": "A circle cursor that interacts with the background color.",
      "prompt": "Fixed 32px by 32px circle, border-radius 100%. Styling: background-color white, mix-blend-mode: difference. Logic: Follow mouse coordinates with a 0.2 lerp (smooth follow). Scale to 2.5x when hovering over anchor tags or buttons."
    }
  ],
  "special_notes": "MUST maintain the 2px border on all interactive elements. DO NOT use blur on shadows; they must be solid color blocks. MUST use #D2E823 as the primary accent to maintain the 'Acid' feel. DO NOT use rounded corners greater than 32px to keep the 'boxy' Brutalist integrity. Ensure all uppercase text uses 'Dela Gothic One' for consistent branding."
}
```

**▶ Try it live → [https://superdesign.dev/library/neo-brutalism-style](https://superdesign.dev/library/neo-brutalism-style)**

*626 copies · 1,681 tries · tags: page, landing page, style*
