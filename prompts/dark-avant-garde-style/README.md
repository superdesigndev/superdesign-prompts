---
title: "Dark Avant-Garde Style"
slug: "dark-avant-garde-style"
category: "Landing Pages"
tags: ["landing page", "page", "style"]
copyCount: 480
tryCount: 2208
author: "Jason Zhou"
try_url: "https://superdesign.dev/library/dark-avant-garde-style?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
---

# Dark Avant-Garde Style

A dark avant-garde design system termed 'Digital Naturalism,' characterized by a sophisticated interplay between deep charcoal surfaces and high-energy acid green accents. Featuring editorial serif typography paired with clean sans-serif UI, the style utilizes Brutalist-inspired elements like serrated edges, skewed 'tab' navigation, and grainy noise overlays. Ideal for high-end design agencies, AI masterclasses, editorial portfolios, and premium fintech brands seeking a bold, technical, yet organic aesthetic.

<img src="preview.png" alt="Dark Avant-Garde Style" width="640">

## Prompt

```text
{
  "summary": "A high-contrast dark-mode design system with an editorial feel, using vibrant lime accents, sophisticated serif headings, and unique geometric cut-outs to create a premium, technical atmosphere.",
  "style": {
    "description": "The style blends 'Digital Naturalism' with brutalist technicality. It uses a core palette of deep charcoal (#0C0A09), warm stone (#E7E5E4), and a signature lime accent (#D4F268). Typography is a dual-system: 'Newsreader' for elegant, light-weight serif headings and 'Instrument Sans' for functional UI and body text. Visuals are treated with a fixed 4% opacity noise overlay to provide texture and organic 'analog' feel to the digital surfaces.",
    "prompt": "### Colors\n- Background: #0C0A09 (Stone Black)\n- Primary Accent: #D4F268 (Acid Lime) - used for highlights, primary buttons, and critical status markers.\n- Secondary Surface: #1C1917 (Warm Charcoal) - used for section backgrounds and cards.\n- Neutral Foreground: #E7E5E4 (Off-white/Stone) - used for primary body text.\n- Borders: rgba(255, 255, 255, 0.1)\n\n### Typography\n- **Serif (Display)**: 'Newsreader', serif. Weights: 200, 300, 400. Use for H1-H3. Use italics frequently for emphasis words within headers. Letter-spacing: -0.02em.\n- **Sans (UI/Body)**: 'Instrument Sans', sans-serif. Weights: 400, 500, 600. Use for body text, labels, and navigation. Size: 18px body, 14px labels.\n- **Mono**: System monospace for technical identifiers (e.g., 'Fig. 1A').\n\n### Effects & Global Styles\n- **Noise Overlay**: Fixed position SVG fractal noise, opacity 0.04, mix-blend-mode: overlay.\n- **Serrated Edges**: Section dividers using radial-gradient masks to create a jagged 'postage-stamp' or 'tear' effect (20px size).\n- **Corner Radii**: 24px (Large) for primary cards, 9999px (Full) for buttons.\n- **Transitions**: 300ms cubic-bezier(0.4, 0, 0.2, 1)."
  },
  "layout_and_structure": {
    "description": "A structured yet dynamic layout featuring a fixed glassmorphism navigation bar, asymmetrical hero sections, and a signature 'bento-tab' layout for content sections.",
    "prompts": [
      {
        "part": "Navigation",
        "prompt": "Fixed top bar. Left: Logo with circular icon. Center: Pill-shaped navigation bar using #E7E5E4/5 background with heavy backdrop-blur (8px). Links have a 300ms transition to #E7E5E4 background with #0C0A09 text. Right: Primary CTA button in #D4F268 with rounded-full shape."
      },
      {
        "part": "Hero Section",
        "prompt": "Two-column grid (5:7 ratio). Left: H1 heading in Serif light weight, using Italics for the accent word. Sub-text in 60% opacity sans-serif. Social proof avatars with 70% opacity grayscale filter. Right: A large abstract image container with a 'rounded-top-arch' (10rem radius) and rectangular bottom. Includes a 'floating' sticky note badge in #D4F268 rotated at 6 degrees."
      },
      {
        "part": "Tabbed Main Content",
        "prompt": "A container with 'Folder' style navigation. Tabs are slightly rotated (-2 to -1 degrees) and overlap the main container. The active tab is larger and uses #D4F268. The content area below is #1C1917 with a serrated top edge. Background features a 40px grid pattern at 3% opacity."
      },
      {
        "part": "Showcase Grid",
        "prompt": "Cards with an aspect ratio of 3:4. Cards are #292524 with images that have a grayscale(100%) filter, becoming full color on hover. Titles are in Serif Italic. One card in the grid should have a vertical offset (Y-axis translation) to break the grid's rigidity."
      }
    ]
  },
  "special_ui_components": [
    {
      "component": "Serrated Edge Divider",
      "description": "A procedural jagged edge used to divide dark sections.",
      "prompt": "Implementation: Use a mask-image with a radial-gradient. `radial-gradient(circle at 10px 0, transparent 0, transparent 5px, black 5px)`. Set `mask-size: 20px 10px` and `mask-repeat: repeat-x`. Apply to a 16px high div placed at the boundary of two sections."
    },
    {
      "component": "Sticky Note CTA",
      "description": "A highlight card that mimics a physical note pinned to the interface.",
      "prompt": "Background: #D4F268. Text: #1C1917. Transform: rotate(2deg). Padding: 40px. Border-radius: 24px. On hover, transform: rotate(0deg) scale(1.02). Use Serif typography for the heading and include a bottom border-top with low opacity for an interactive footer within the card."
    },
    {
      "component": "Catalog Label",
      "description": "Technical metadata label for images.",
      "prompt": "Positioned absolute on images. Semi-transparent black background (40% opacity) with heavy backdrop-blur. Features a top row with 'Fig. No' in 10px monospace and a status dot in #D4F268."
    }
  ],
  "special_notes": "MUST use the noise overlay to prevent the dark colors from appearing flat. MUST NOT use standard pure black (#000000); use the stone-tinted #0C0A09. Headlines MUST use light weights (300 or lower) to maintain the 'Avant-Garde' editorial aesthetic. Icons should be monochrome Lucide-style line icons."
}
```

**▶ Try it live → [https://superdesign.dev/library/dark-avant-garde-style](https://superdesign.dev/library/dark-avant-garde-style?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library)**

**Use it in your coding agent:** install the [Superdesign skill](https://github.com/superdesigndev/superdesign-skill), then:

```bash
superdesign get-prompts --slugs "dark-avant-garde-style" --json
```

*480 copies · 2,208 tries · landing page, page, style*
