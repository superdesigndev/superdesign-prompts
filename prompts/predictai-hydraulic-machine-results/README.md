---
title: "PredictAI - Hydraulic Machine Results"
slug: "predictai-hydraulic-machine-results"
category: "Design Systems & Styles"
tags: []
copyCount: 17
tryCount: 2477
author: "Superdesign"
try_url: "https://superdesign.dev/library/predictai-hydraulic-machine-results?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
---

# PredictAI - Hydraulic Machine Results

A high-contrast, bold editorial style dashboard designed for industrial analytics and predictive AI monitoring. Features a sophisticated dark/light mode system with a minimalist color palette emphasizing teal (#1DB584) and deep blue (#0070C0). The layout uses a structured 12-column bento-grid approach with heavy emphasis on typography contrast, combining sans-serif Inter for headlines with JetBrains Mono for technical metadata. Ideal for SaaS platforms, fintech, IoT monitoring, and high-end technical interfaces that require both clarity and an editorial aesthetic. Includes unique micro-interactions like a mix-blend-mode custom cursor and staggered reveal animations.

<img src="preview.png" alt="PredictAI - Hydraulic Machine Results" width="640">

## Prompt

```text
{
  "summary": "PredictAI is a technical dashboard design that blends industrial data visualization with bold editorial aesthetics. It utilizes extreme typographic weight variations, a 12-column responsive grid, and smooth, high-end motion design to deliver complex information clearly. The interface relies on subtle 1px borders, generous 40px rounded corners, and a specific palette of teal and blue against monochrome backgrounds.",
  "style": {
    "description": "Editorial-meets-technical style with high-contrast typography, monochrome base colors with vibrant functional accents, and smooth cubic-bezier motion. Key fonts are Inter (Bold for titles, Regular for body) and JetBrains Mono (for technical data). Main colors are Pure Black (#000000), White (#FFFFFF), Health Teal (#1DB584), and Accent Blue (#0070C0).",
    "prompt": "Apply a 'Bold Editorial' design system. Backgrounds: #FBFBFB (Light) / #0A0A0A (Dark). Primary Text: #000000 (Light) / #FFFFFF (Dark). Accent 1 (Health/Success): #1DB584. Accent 2 (Action/Confidence): #0070C0. Borders: 1px solid with 5% (Light) to 10% (Dark) opacity. Typography: Primary font 'Inter', headings use weight 700 with letter-spacing -0.05em; Metadata font 'JetBrains Mono', weight 400, uppercase, letter-spacing 0.2em. Border radius: 40px for primary cards, 16px for secondary elements. Animation Easing: cubic-bezier(0.16, 1, 0.3, 1). Interactive Cursor: 32px circle, 1px border, mix-blend-mode: difference, scaling 2.5x on hover. All card transitions: 500ms duration."
  },
  "layout_and_structure": {
    "description": "The page uses a fixed navigation header and a main 12-column grid divided into three primary segments (4-4-4) on desktop, collapsing to a single column on mobile.",
    "prompts": [
      {
        "part": "Navigation",
        "prompt": "Fixed header with 'mix-blend-difference' mode. Left: Bold lowercase logo. Right: Navigation links using metadata font style (JetBrains Mono, 10px, uppercase, 0.2em tracking) with '01 / Label' numbering format. Far right: Theme toggle icon and a 'plus' menu button."
      },
      {
        "part": "Metric Column (Left)",
        "prompt": "4-column wide section. Top card: Status indicator featuring a large 60px bold uppercase heading (e.g., 'STABLE'), a small 8px green dot indicator, and a rounded pill-badge for severity. Bottom card: Detailed confidence metrics featuring a large SVG circular progress ring (stroke-width 6px, stroke-linecap round) and horizontal data bars for probability and risk scores."
      },
      {
        "part": "Narrative Column (Center)",
        "prompt": "4-column wide section. Top card: Tall diagnostic summary with 24px medium weight text and high leading (relaxed). Includes a 'System Message' sub-section separated by a 1px border-top, using 18px italic text. Bottom card: Action recommendation card with a distinctive icon in a 56px rounded-square container (bg: #0070C0) and 24px bold title."
      },
      {
        "part": "Technical Column (Right)",
        "prompt": "4-column wide section containing three cards. Card 1: Failure analysis with a 'Decision Path' flow showing technical steps as small 9px bold badges connected by chevron icons. Card 2: 2x2 grid of 'Key Sensors' showing large 24px bold values and 8px metadata labels. Card 3: 'Model Breakdown' with stacked horizontal progress bars (2px height) and percentage labels."
      }
    ]
  },
  "special_ui_components": [
    {
      "component": "Circular Confidence Ring",
      "description": "Animated SVG progress indicator for confidence scores.",
      "prompt": "Create an SVG circle with 112px center, 90px radius. Background circle stroke: opacity 5%. Foreground progress stroke: #0070C0, stroke-width 6px, stroke-linecap: round. Use stroke-dasharray based on 2 * PI * R (approx 565.48) and animate stroke-dashoffset on load with 2s duration."
    },
    {
      "component": "Interactive Metadata Badges",
      "description": "Small technical tags for status and categorical labels.",
      "prompt": "Font: JetBrains Mono, Size: 9px, Weight: 700, Case: Uppercase, Tracking: 0.2em. Background: 5% opacity of accent color. Padding: 6px 16px. Radius: 8px. Border: 1px solid 10% opacity."
    },
    {
      "component": "Mix-Blend Custom Cursor",
      "description": "Cursor that reacts to the color of elements it moves over.",
      "prompt": "Circle div 32px x 32px, border-radius 50%, border 1px solid #FFFFFF, background transparent. CSS properties: pointer-events: none, position: fixed, z-index: 9999, mix-blend-mode: difference. On hovering links/cards: transition transform 0.5s cubic-bezier(0.16, 1, 0.3, 1) to scale(2.5)."
    }
  ],
  "special_notes": "MUST: Hide the default OS cursor and use the custom circle cursor. MUST: Implement staggered entrance animations for cards with 100ms intervals. MUST: Use 'mix-blend-mode: difference' for the navigation and cursor. MUST NOT: Use heavy shadows; instead, use 1px borders and subtle color shifts for depth. MUST NOT: Exceed 10% opacity on card borders to maintain the 'editorial' cleanliness."
}
```

**▶ Try it live → [https://superdesign.dev/library/predictai-hydraulic-machine-results](https://superdesign.dev/library/predictai-hydraulic-machine-results?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library)**

**Use it in your coding agent:** install the [Superdesign skill](https://github.com/superdesigndev/superdesign-skill), then:

```bash
superdesign get-prompts --slugs "predictai-hydraulic-machine-results" --json
```

*17 copies · 2,477 tries · *
