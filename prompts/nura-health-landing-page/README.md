---
title: "Nura Health Landing Page"
slug: nura-health-landing-page
tags: []
copyCount: 73
tryCount: 2494
source: https://superdesign.dev/library/nura-health-landing-page
---

# Nura Health Landing Page

A high-end clinical boutique aesthetic for premium health and biotech verticals. This design system, titled Nura Health, leverages a deep charcoal dark mode with organic earth-tone accents in moss green and terracotta clay. It features sophisticated scroll-driven animations including sticky stacking cards, split-text reveals, and glassmorphic navigation. Suitable for longevity SaaS, wellness clinics, medical telemetry platforms, and high-end organic skincare brands. Key visual identifiers include editorial typography using Cabinet Grotesk, a global noise texture overlay for a tactile feel, and interactive GSAP-powered micro-interactions.

## Prompt

```text
{
  "summary": "A modern, minimal, and organic clinical landing page designed for premium health SaaS. It utilizes a dark charcoal base with moss green and clay accents, featuring a floating glassmorphic navbar, a hero section with staggered headline reveals, and a unique sticky-stacking protocol section where cards blur and scale as they are overlapped.",
  "style": {
    "description": "The style blends high-tech precision with organic textures. Typography uses Cabinet Grotesk for bold, editorial headers and Satoshi for clean, readable body text. The palette is dominated by Charcoal (#0a0a0b), Moss Green (#4a5d23), and Clay (#c86b51). A global SVG noise texture is applied at 4% opacity to create a sophisticated, non-digital paper feel. Animations are smooth and deliberate, using GSAP for scroll-triggered transforms and state transitions.",
    "prompt": "Create a design with a 'Clinical Boutique' aesthetic. **Colors:** Background: #0a0a0b; Cards: #121214; Borders: #ffffff0d (5% white); Accents: Moss Green (#4a5d23), Clay (#c86b51). **Typography:** Headers in Cabinet Grotesk (800 weight), body in Satoshi (400-500 weight). Hero font size: 8xl (96px) with 1.05 line-height. **Effects:** Apply a global grain texture overlay using a fractal noise SVG at 0.04 opacity. Use glassmorphism for the navbar with a backdrop-blur starting at 4px and increasing to 12px on scroll. **Animations:** Use GSAP 'power4.out' curves for entrance animations. Implement split-text reveals for section headings where words slide up from overflow-hidden containers."
  },
  "layout_and_structure": {
    "description": "A responsive desktop-first layout consisting of a fixed floating navbar, an immersive hero with a background image overlay, an interactive feature grid, a parallax philosophy statement, and a vertical stacking protocol sequence.",
    "prompts": [
      {
        "part": "Floating Navbar",
        "prompt": "Design a fixed navbar positioned 24px from the top, centered, with a width of 95% maxing at 1280px. Shape: rounded-full. Background: #121214 at 20% opacity with 4px backdrop-blur. On scroll, transition background to 80% opacity and 12px blur. Include a circular logo on the left, centered navigation links, and a pill-shaped 'Request Access' button with a subtle 1px border."
      },
      {
        "part": "Hero Section",
        "prompt": "Full-height (min-h-screen) section. Background: Dark forest image (30% opacity) with a vertical gradient transition from charcoal-950/80 to charcoal-950. Content: A top-aligned badge 'System Online' with a pulsing green dot. Headline: Three lines of large text (96px) with staggered entry animation. CTA: Primary button (solid white) and secondary button (outlined white/20) with rounded-full shapes. Include a bottom-centered vertical line scroll indicator."
      },
      {
        "part": "Intelligence Architecture Grid",
        "prompt": "3-column grid of cards (height: 450px). Cards: #121214 background, rounded-3xl, 1px white/5 border. Card 1: 'Diagnostics Shuffler' featuring three stacked internal cards that fan out on hover. Card 2: 'Telemetry Typewriter' with a black console-style box and a JavaScript-driven typewriter effect for code/data. Card 3: 'Biometric Mapping' with an interactive radial glow (moss green) that follows the cursor movements."
      },
      {
        "part": "Sticky Stacking Protocols",
        "prompt": "A sequence of large cards (min-h-400px) that stack vertically. Use 'position: sticky; top: 128px;'. As a new card scrolls over the previous one, the card underneath must scale down to 0.94, fade to 0.4 opacity, and apply an 8px blur filter using ScrollTrigger. Each card includes a large background 'Step Number' (e.g., 01, 02) at 3% white opacity."
      },
      {
        "part": "Pricing Grid",
        "prompt": "Three-tier pricing layout. The middle tier must be 'elevated' using 'scale: 1.05' and a 2px border of Clay (#c86b51). Background for active tier: #121215 with a subtle 40px clay glow shadow. Toggle button: pill-shaped container with white/10 active state background."
      },
      {
        "part": "System Health Footer",
        "prompt": "Deep charcoal background (#0a0a0b) with a top 1px border. 4-column layout for links. Bottom row includes a copyright notice and a 'System Operational' status indicator featuring a pulsing emerald green dot (#10b981) inside a pill-shaped badge."
      }
    ]
  },
  "special_ui_components": [
    {
      "component": "Interactive Hover Glow Card",
      "description": "A card that tracks mouse position to render a localized radial gradient glow.",
      "prompt": "Create a card component with a hidden radial-gradient background: 'radial-gradient(circle at var(--mouse-x) var(--mouse-y), rgba(74, 93, 35, 0.15) 0%, transparent 50%)'. Use JS to update CSS variables --mouse-x and --mouse-y on 'mousemove'. The glow should only become visible (opacity 1) when the mouse enters the card's bounding box."
    },
    {
      "component": "Card Shuffler Visual",
      "description": "A deck-of-cards animation for illustrating data layers.",
      "prompt": "Place three cards inside a container with 'perspective: 1000px'. On parent hover, Card 1 (bottom) translates -20px X and -10px Y with a -4deg rotation. Card 2 (middle) translates 20px X and 10px Y with 4deg rotation. Card 0 (top) scales to 1.05. Use a 500ms ease-out transition for all properties."
    }
  ],
  "special_notes": "Must-dos: Maintain a strict dark-mode contrast ratio; Use a specific noise texture overlay across the entire 'app-wrapper' to prevent flat digital gradients. Must-nots: Avoid bright white backgrounds or saturated neon colors; Do not use sharp corners (all UI elements should have a radius of at least 12px or be fully rounded)."
}
```

**▶ Try it live → [https://superdesign.dev/library/nura-health-landing-page](https://superdesign.dev/library/nura-health-landing-page)**

*73 copies · 2,494 tries · tags: *
