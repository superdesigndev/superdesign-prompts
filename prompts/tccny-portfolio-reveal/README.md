---
title: "TCCNY Portfolio Reveal"
slug: "tccny-portfolio-reveal"
category: "Portfolios"
tags: []
copyCount: 33
tryCount: 2456
author: "Superdesign"
try_url: "https://superdesign.dev/library/tccny-portfolio-reveal?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
---

# TCCNY Portfolio Reveal

A high-end, dark-mode portfolio landing page featuring a tech-forward 'Digital Alchemist' aesthetic. Incorporates editorial typography with Space Grotesk and Inter fonts, a pixel-art transition intro, and modern UI elements like infinite marquees and glassmorphism. Perfect for creative agencies, fintech, luxury engineering, or independent developers seeking a brutalist yet polished Brooklyn-style aesthetic.

<img src="preview.png" alt="TCCNY Portfolio Reveal" width="640">

## Prompt

```text
{
  "summary": "A sophisticated single-page portfolio with a deep black theme (#050505), featuring bold geometric typography, high-contrast accent colors (blue, purple, green), and interactive project grids. The UI transitions from a retro pixel-game aesthetic into a clean, modern professional site using scanline overlays and smooth scroll animations.",
  "style": {
    "description": "The style combines retro-tech elements (pixel fonts, scanlines) with high-end modern design (Space Grotesk headers, Inter body text, glassmorphism). It utilizes a monochromatic dark base (#050505) with vibrant gradient accents and subtle 'glow' effects from blurred background containers.",
    "prompt": "Create a design system using a background of #050505 and foreground of #FFFFFF. Typography: Headers in 'Space Grotesk' (Weights: 500, 700, 800) with tight tracking; body text in 'Inter' (Weights: 300, 400). Accent colors: Electric Blue (#3B82F6), Deep Purple (#9333EA), and Signal Green (#22C55E). Include a CRT-style scanline overlay (linear-gradient 50% transparency every 4px). Use glassmorphism for containers: background white/5, border white/10, backdrop-blur(12px). Animations should use cubic-bezier(0.4, 0, 0.2, 1) for smooth transitions."
  },
  "layout_and_structure": {
    "description": "A vertical-scrolling single-page application consisting of a fixed navigation bar, hero section, interactive marquee, asymmetrical project grid, and a split-section services/about layout.",
    "prompts": [
      {
        "part": "Navigation",
        "prompt": "Fixed top bar, height: 80px. Background: #050505 at 80% opacity with backdrop-blur. Left: Logotype in Space Grotesk with a single color dot. Right: Text links (14px, uppercase, tracking-wide) in #9CA3AF. Far right: Pill-shaped CTA button with black text on white background."
      },
      {
        "part": "Hero Section",
        "prompt": "Min-height 100vh. Center-aligned text. Hero tag: Small pill with 'Press Start 2P' font and green dot. Main Heading: Font size 5xl (mobile) to 8xl (desktop), font Space Grotesk, leading-0.95. One word should be a gradient (Blue to Purple). Subtext: Max-width 640px, Inter font, #9CA3AF color. Buttons: Pair a solid white pill-button with an outlined (border-white/20) ghost button."
      },
      {
        "part": "Skills Marquee",
        "prompt": "Full-width container, height: 80px-120px. Background: #0a0a0a. Continuous scrolling text (animate-marquee 20s linear infinite). Text: Space Grotesk, bold, transparent with a gray-to-black gradient stroke, font-size 4xl to 6xl."
      },
      {
        "part": "Project Grid",
        "prompt": "Max-width 1280px. 2-column grid with alternating vertical offsets (top margin 64px on even items). Cards: Aspect ratio 4:3, border-radius 16px, overflow hidden. Hover state: Image scales 1.05x, black overlay appears (60% opacity) with a white circular icon in the center. Card metadata: Title in Space Grotesk 2xl, tech tags as small white/5 border-radius pills."
      },
      {
        "part": "About and Services",
        "prompt": "Split layout (1/3 image, 2/3 text). Image: Grayscale, fixed aspect ratio 1:1, border-radius 16px. Content: Large introductory paragraph (Inter, 20px, light). Services Grid: 2x2 grid of cards with glassmorphism borders. Icons: Use monochrome Lucide-style icons with specific brand colors (Blue, Purple, Green, Pink)."
      },
      {
        "part": "Contact and Footer",
        "prompt": "Contact: Centered text, 7xl heading. CTA Button: Large pill, #2563EB background, shadow-blue-900/50. Footer: 32px height, 12px mono font, #4B5563 color. Two-column layout: copyright left, location right."
      }
    ]
  },
  "special_ui_components": [
    {
      "component": "Interactive Project Card",
      "description": "A card that combines visual depth with clear metadata.",
      "prompt": "Implement a container with 'group' hover classes. The image should have a mix-blend-mode overlay of color (blue/black gradient). On hover, transition an absolute-positioned overlay from opacity 0 to 1. The overlay should contain a centered 64px white circle with an arrow icon. Tech tags below the image should be flex-row with a 8px gap."
    },
    {
      "component": "Infinite Marquee",
      "description": "A non-stop horizontal text scroller for dynamic branding.",
      "prompt": "Create a wrapper with 'overflow-hidden'. Inside, two identical divs with 'flex whitespace-nowrap' and an animation 'marquee 20s linear infinite'. Text should be set to 'text-transparent' with 'bg-clip-text' using a gradient from #1f2937 to #4b5563."
    }
  ],
  "special_notes": "MUST: Maintain the #050505 background for deep blacks. DO NOT: Use standard 12px grid gutters; use 32px-64px for a premium feel. MUST: Use the iris-wipe (clip-path: circle) for page transitions. MUST: Keep font-weight of Space Grotesk heavy for headings to contrast the light Inter body text."
}
```

**▶ Try it live → [https://superdesign.dev/library/tccny-portfolio-reveal](https://superdesign.dev/library/tccny-portfolio-reveal?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library)**

**Use it in your coding agent:** install the [Superdesign skill](https://github.com/superdesigndev/superdesign-skill), then:

```bash
superdesign get-prompts --slugs "tccny-portfolio-reveal" --json
```

*33 copies · 2,456 tries · *
