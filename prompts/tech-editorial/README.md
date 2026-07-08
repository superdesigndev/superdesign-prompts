---
title: "Tech Editorial"
slug: "tech-editorial"
category: "Landing Pages"
industry: "General"
tags: ["landing page", "style", "page"]
copyCount: 510
tryCount: 1515
author: "Jason Zhou"
try_url: "https://superdesign.dev/library/tech-editorial?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
---

# Tech Editorial

A high-end 'Tech Editorial' aesthetic that merges brutalist precision with classic editorial sophistication. It features a muted, paper-like color palette (#f7f6f2), a structured grid-line system, and a unique pairing of high-contrast Serif (Playfair Display) for display headers and technical Mono (Space Mono) for functional UI. The style is characterized by scroll-triggered text reveals, glassmorphism navigation, and 'scan-line' animations that suggest a sophisticated AI-driven process. Ideal for high-tech SaaS, AI research labs, design agencies, and premium fintech platforms.

<img src="preview.mp4" alt="Tech Editorial" width="640">

## Prompt

```text
{
  "summary": "A sophisticated editorial-style UI featuring a fixed background grid, high-contrast serif typography, and technical monospace accents with a muted forest green primary color.",
  "style": {
    "description": "The design uses a trio of typefaces: Playfair Display (Serif) for headers and emotional impact, Space Grotesk (Sans) for readability, and Space Mono (Mono) for all technical data, labels, and buttons. The color palette is organic and muted: Background (#f7f6f2), Foreground (#1c1c1c), and Primary Accent (#3d7068). Layouts are governed by a strict 4-column vertical guide system and 1px borders. Transitions use a custom 'editorial' cubic-bezier(0.16, 1, 0.3, 1) for a smooth, high-fashion feel.",
    "prompt": "Apply an editorial tech aesthetic using background #f7f6f2 and foreground #1c1c1c. Typography: Headings in 'Playfair Display' (light weight, tight tracking), UI labels and buttons in 'Space Mono' (uppercase, tracking 0.2em-0.3em), and body text in 'Space Grotesk'. Use #3d7068 as the primary accent color for buttons and highlights. Implement 1px borders using #e5e4de. All animations must use cubic-bezier(0.16, 1, 0.3, 1) with a 700ms-1000ms duration. Include a fixed background grid of 40px squares with a radial mask that fades toward the edges."
  },
  "layout_and_structure": {
    "description": "The layout is built on a max-width 7xl container with visible structural vertical dividers. Sections are clearly demarcated by 1px horizontal borders. The navigation is a floating-to-fixed transition element with backdrop blur.",
    "prompts": [
      {
        "part": "Structural Grid",
        "prompt": "Create a fixed background layer with vertical lines at 25%, 50%, and 75% width using 1px #e5e4de. Overlay a 40px square grid pattern with a radial transparency mask (40% center opacity, 0% edge opacity)."
      },
      {
        "part": "Header Navigation",
        "prompt": "A fixed top nav starting with 32px padding-top. On scroll, it transitions to a border-bottom fixed bar with #f7f6f2/80 backdrop-blur. The brand logo is a serif 'SUPERDESIGN' in 20px font-size, flanked by two horizontal bars of varying widths (24px and 32px). Links are 10px uppercase Space Mono with 0.3em tracking."
      },
      {
        "part": "Hero Section",
        "prompt": "Center-aligned hero with a pulse-dot badge. The H1 should be massive (9vw), serif, light weight, and uppercase. Use an italicized secondary color (#B4B4B4) for key words. Primary CTA button should be #3d7068 with a 'Space Mono' label that increases character tracking from 0.2em to 0.4em on hover."
      },
      {
        "part": "Statistics Grid",
        "prompt": "A 3-column grid with 1px #e5e4de dividers. Each cell has 40px padding, a 48px bordered icon box, a large serif number (4xl), and an uppercase mono label. Cells transition to a white background on hover."
      },
      {
        "part": "Text Reveal Section",
        "prompt": "A scroll-interactive section where each word of a large serif paragraph (3xl to 6xl) increases opacity from 0.15 to 1.0 as the user scrolls, creating a 'reading' effect."
      },
      {
        "part": "Interactive Workflow",
        "prompt": "Two-column layout. Left side: Vertical steps (01, 02, 03) in mono. Clicking a step expands a description and reduces the opacity of inactive steps to 0.4. Right side: A sticky card with a grayscale image (60% opacity, multiply blend mode) and a 'scan-line' progress bar using #3b82f6."
      },
      {
        "part": "Use Case Tabs",
        "prompt": "A centered tab switcher with pill-shaped buttons. Content below is a large bordered card (#f7f6f2) featuring a massive 240px ghost icon (5% opacity) in the background and a 3-column benefit grid at the bottom."
      },
      {
        "part": "Contact Form",
        "prompt": "Two-column grid. Left side: Large serif heading 'Request Access'. Right side: Form with inputs that are only bottom-bordered (#e5e4de). Placeholder text in 10px mono. Submit button is full-width with 0.4em letter-spacing and a #3d7068 shadow-drop."
      }
    ]
  },
  "special_ui_components": [
    {
      "component": "Scan-Line Progress Bar",
      "description": "A technical loading indicator used for status updates.",
      "prompt": "Create a 2px height container with #e5e4de background. Inside, a #3b82f6 line that animates from -100% to 100% width/position using a 2s infinite cubic-bezier(0.8, 0, 0.2, 1) 'slide' animation."
    },
    {
      "component": "Animated CTA Button",
      "description": "High-intent button with character-spacing and background-fill transitions.",
      "prompt": "Button with #3d7068 background, #ffffff text, 'Space Mono' font, 10px size, 0.25em tracking. On hover: tracking increases to 0.4em and a white/20% overlay slides up from the bottom (translate-y-full to 0)."
    },
    {
      "component": "Editorial Word Reveal",
      "description": "Scroll-synced typography effect.",
      "prompt": "Split text into individual <span> elements. Set default opacity to 0.15. Using JS IntersectionObserver or scroll listener, map the scroll progress of the container to the index of the spans, setting opacity to 1.0 as they 'activate'."
    }
  ],
  "special_notes": "MUST: Maintain the #f7f6f2 background to avoid a 'clinical' white look. MUST: Use 1px borders instead of shadows for section separation. MUST: Ensure 'Space Mono' is used for all metadata and numeric data. MUST NOT: Use rounded corners larger than 2px. MUST NOT: Use vibrant gradients; stick to solid fills and simple opacity transitions."
}
```

**▶ Try it live → [https://superdesign.dev/library/tech-editorial](https://superdesign.dev/library/tech-editorial?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library)**

**Use it in your coding agent:** install the [Superdesign skill](https://github.com/superdesigndev/superdesign-skill), then:

```bash
superdesign get-prompts --slugs "tech-editorial" --json
```

*510 copies · 1,515 tries · Landing Pages · General · landing page, style, page*
