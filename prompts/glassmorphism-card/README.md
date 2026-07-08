---
title: "Glassmorphism card"
slug: "glassmorphism-card"
category: "Design Systems & Styles"
industry: "General"
tags: ["landing page", "page", "style"]
copyCount: 1250
tryCount: 1895
author: "Jason Zhou"
try_url: "https://superdesign.dev/library/glassmorphism-card?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
---

# Glassmorphism card

A premium, high-tech glassmorphism design system characterized by deep translucent layers, dark-to-light transitions, and editorial typography. Featuring a 'Superdesign' aesthetic, it utilizes heavy background blurs, grain textures, and emerald accents. This style is ideal for SaaS, AI platforms, fintech, and high-end design agencies requiring a sophisticated, futuristic feel with bento-grid layouts and fluid animations.

<img src="preview.mp4" alt="Glassmorphism card" width="640">

## Prompt

```text
{
  "summary": "A sophisticated design system centered on glassmorphism, depth-focused layouts, and a monochrome palette with vibrant emerald highlights. It transitions from a dark, immersive hero section to a clean, structured light-mode feature set.",
  "style": {
    "description": "The style relies on the Inter font family for a clean, modern look. It features two primary modes: a high-contrast dark mode using deep blacks (#000000) and translucent glass layers, and a light mode using soft zinc grays (#F4F4F5). Animations are smooth, utilizing cubic-bezier curves for entry and hover states. Key visual elements include 20px-blur glass containers and a subtle grain overlay.",
    "prompt": "### Visual Foundations\n- **Color Palette:** Primary Dark (#000000), Light Background (#F4F4F5), Zinc Accent (#18181B), Emerald Highlight (#34D399), Subtle Border (rgba(255, 255, 255, 0.1)).\n- **Typography:** Font: 'Inter', sans-serif. \n  - Headings: font-weight 500-700, tracking -0.05em, leading 1.05.\n  - Body: font-weight 300-400, color: Zinc-500 (#71717A).\n  - Labels: font-weight 700, size 10px, tracking 0.2em, uppercase.\n- **Glassmorphism:** \n  - `background: rgba(255, 255, 255, 0.05)`\n  - `backdrop-filter: blur(12px)`\n  - `border: 1px solid rgba(255, 255, 255, 0.1)`\n- **Grain Overlay:** Use a noise SVG as a fixed overlay at 15% opacity to add texture to dark sections.\n- **Corner Radius:** Standardize large containers at `2.5rem (40px)` and internal cards at `1rem (16px)` to `1.5rem (24px)`.\n- **Animations:** \n  - Entry: `fade-in-up` (TranslateY: 20px to 0, Opacity: 0 to 1) using `cubic-bezier(0.16, 1, 0.3, 1)` over 0.8s.\n  - Hover: Scaling effects (105%) and background color transitions (300ms duration)."
  },
  "layout_and_structure": {
    "description": "The layout is built within a max-width 1600px container. It uses a tiered structure: an immersive full-height hero section with absolute-positioned glass elements, followed by a grid-based feature section, a dark 'productivity' block, and a bento-grid pricing layout.",
    "prompts": [
      {
        "part": "Navigation",
        "prompt": "Floating glass navbar. Features a blur of 20px, rounded-full shape, and 1.5px padding. Links use `text-white/80` with a hover state of `bg-white/10` and rounded-full background."
      },
      {
        "part": "Hero Section",
        "prompt": "Height 92vh, rounded corners (2.5rem). Background consists of a high-resolution abstract image at 60% opacity with a gradient overlay from `zinc-950/40` to `zinc-950/90`. Includes a massive background text ('CREATE') at 22vw with 3% opacity and a blur filter. Content is split between a left-aligned typography block and a right-aligned vertical stack of glass stats cards."
      },
      {
        "part": "Feature Grid",
        "prompt": "Two-column layout. Left column: Sticky header with 4xl-5xl typography and a 2x3 grid of icon+label pairs. Right column: Large display card with a 105% hover-scale image and an internal floating glass 'System Analysis' component showing progress bars and status indicators."
      },
      {
        "part": "Dark Productivity Block",
        "prompt": "Full-width section with #18181B background. Features a grayscale grid lineart overlay. Layout: 2-column. Left: List of numbered steps (01, 02) in rounded-2xl boxes. Right: 3D-transformed mock-up window (rotated 3 degrees) with internal glass-morphic code snippets and a 'bounce' animated status tag at the bottom-right."
      },
      {
        "part": "Pricing Bento Grid",
        "prompt": "3-column grid of cards. Each card: White background, 2rem radius, thin zinc-100 border. Top half: 64px height image with a gradient-to-black bottom overlay. Bottom half: Padding 1.5rem, secondary text for features, and a full-width action button."
      }
    ]
  },
  "special_ui_components": [
    {
      "component": "Interactive Action Button",
      "description": "A pill-shaped button with a nested circular icon container.",
      "prompt": "Base: `bg-white`, `rounded-full`, `pl-6 pr-2 py-2`. Text: `font-medium`, `text-zinc-900`. Inner Icon: `w-10 h-10`, `bg-zinc-900`, `rounded-full`, containing a white icon. Interaction: Entire button scales to 105% on hover, inner icon background shifts to `bg-zinc-700`."
    },
    {
      "component": "Glass Stat Card",
      "description": "A high-transparency card used for metrics within dark sections.",
      "prompt": "Dimensions: Width 72px (approx), Padding 1.25rem. Style: `background: rgba(255, 255, 255, 0.05)`, `backdrop-filter: blur(12px)`, `border: 1px solid rgba(255, 255, 255, 0.1)`. Elements: Large metric (text-3xl) and secondary description (text-white/60, size sm)."
    }
  ],
  "special_notes": "MUST: Maintain the 2.5rem corner radius for all major section wrappers to ensure visual rhythm. MUST: Use 'grainy-gradients' noise textures on dark backgrounds to prevent banding and add 'analog' depth. MUST: Ensure all glass elements have a 1px white border with 10% opacity for edge definition. DO NOT: Use flat colors for dark backgrounds; always apply a subtle bottom-heavy gradient."
}
```

**▶ Try it live → [https://superdesign.dev/library/glassmorphism-card](https://superdesign.dev/library/glassmorphism-card?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library)**

**Use it in your coding agent:** install the [Superdesign skill](https://github.com/superdesigndev/superdesign-skill), then:

```bash
superdesign get-prompts --slugs "glassmorphism-card" --json
```

*1,250 copies · 1,895 tries · Design Systems & Styles · General · landing page, page, style*
