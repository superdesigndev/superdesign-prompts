---
title: "Red sun"
slug: red-sun
tags: ["landing page", "page", "style"]
copyCount: 513
tryCount: 1616
source: https://superdesign.dev/library/red-sun
---

# Red sun

A sophisticated editorial-style design system named 'Red Sun', characterized by a high-contrast 'Coral and Ink' color palette. This style blends 'Instrument Serif' for high-impact typography with 'Manrope' for technical precision. Features include bento-grid layouts, glassmorphism navigation, scroll-triggered animations with subtle rotations, and soft ambient background blurs. Ideal for premium SaaS, creative agencies, AI product design tools, and fintech platforms looking for a balance between warmth and authority.

![Red sun](./preview.mp4)

## Prompt

```text
{
  "summary": "The Red Sun system uses a bold coral primary color against a deep ink-blue foundation to create a modern, editorial aesthetic. It relies on large-scale serif typography, generous white space, and smooth, non-linear animations (cubic-bezier) to convey a sense of premium craftsmanship and technological speed.",
  "style": {
    "description": "The style is defined by its high-contrast color duo: Coral (#EF4623) and Ink (#2D3B42). Typography follows an editorial hierarchy: 'Instrument Serif' for expressive, large-scale headlines (italicized for emphasis) and 'Manrope' (weights 300-700) for functional UI elements and body copy. UI elements use large corner radii (rounded-3xl to rounded-[3rem]) and subtle depth through 'Soft Peach' (#FDF1EE) background accents and soft blurs.",
    "prompt": "Apply a 'Coral and Ink' editorial style. Primary color: #EF4623 (Coral); Secondary color: #2D3B42 (Ink); Background Accent: #FDF1EE (Soft Peach). Typography: Use 'Instrument Serif' for headings (sizes 60px to 160px, tracking-tight) and 'Manrope' for body (18px, leading-relaxed). For animations, use a custom cubic-bezier(0.16, 1, 0.3, 1) curve for 'fade-up' effects that include a starting 2-degree rotation. Navigation must be a glassmorphism header (backdrop-blur 12px, white/80 opacity). Buttons should have a 30px corner radius and include a shadow-lg shadow-primary/20. Use ambient background blurs (#EF4623 at 10% opacity) with 100px-120px blur radii to create depth."
  },
  "layout_and_structure": {
    "description": "An asymmetrical, modular structure using a mix of full-width hero sections and bento-grid feature areas. Content is revealed via scroll-triggered transitions.",
    "prompts": [
      {
        "part": "Navigation",
        "prompt": "Fixed top navigation. Left: Logo mark (square #EF4623 container with 3-degree rotation). Center/Right: Text links in Manrope (text-sm, font-semibold, #2D3B42 80% opacity). Right CTA: Pill-shaped button (#EF4623, white text, uppercase text-xs). On scroll, apply a background: rgba(255, 255, 255, 0.8) with 12px backdrop-blur and a subtle bottom border."
      },
      {
        "part": "Hero Section",
        "prompt": "Centered layout with high-impact serif typography. Top element: Small pill badge with #FDF1EE background and 'sparkles' icon. Heading: Two-line layout using Instrument Serif at 10rem (mobile 4rem), with the second line italicized and colored #EF4623. Subtext: Max-width 2xl, Manrope text-lg, #2D3B42/70. CTAs: Primary pill button with shadow-2xl; Secondary ghost button with 2px border-ink/10. Background: Large ambient blur circles at top-right and bottom-left."
      },
      {
        "part": "Value Proposition (Bento)",
        "prompt": "Two-column grid. Left: Text-heavy with large Serif H2 and vertical feature list using 56px rounded-2xl icon containers. Right: A 'UI Simulator' component—a dark-themed browser window (#2D3B42) containing a simplified white interface mockup with abstract skeleton loaders and a 'Code Generated' status bar at the bottom."
      },
      {
        "part": "Features Grid",
        "prompt": "Three-column bento grid. Cards use 3rem (48px) border radius. Card Style 1 (Large): Spans 2 columns, white background, #2D3B42 border/5, features a large background icon at 5% opacity. Card Style 2 (Dark): Solid #2D3B42 background, white text, #EF4623 accent icons. Card Style 3 (Standard): White background, vertical layout, accent icon shifts color on hover."
      },
      {
        "part": "Call to Action",
        "prompt": "Full-width section with a 4rem (64px) rounded container in solid #EF4623. Background pattern: subtle white dot grid (opacity 20%, 30px spacing). Heading: Serif text at 8rem. Buttons: High-contrast white background button with #EF4623 text. Include a trust-bar footer with small uppercase tracking-widest text."
      },
      {
        "part": "Footer",
        "prompt": "Deep Ink (#2D3B42) background. 5-column grid. Column 1: Logo and social icons in circular white/10 borders. Columns 2-4: Product/Resource/Company links with H4 serif headers. Bottom bar: 1px top border (white/5), horizontal list of legal links, copyright text."
      }
    ]
  },
  "special_ui_components": [
    {
      "component": "Animated UI Simulator",
      "description": "A floating mockup window representing a software interface.",
      "prompt": "Create a card with #2D3B42 background and 40px radius. Inside, place a white container with rounded-3xl corners. Top bar: 3 colored 'window' dots and a skeleton address bar. Content: 3 vertical sections—a thin skeleton header, a 2-column grid with one peach and one grey block, and a bottom text block. Footer: A glassmorphism blur bar with a green check-circle icon and two 'code tags' (dark rectangles with mono text)."
    },
    {
      "component": "The 'Rotating Logo' Brand Mark",
      "description": "A simple but dynamic logo mark.",
      "prompt": "A 36px square container using #EF4623. Apply a 3-degree rotation by default. Inside, place a single white uppercase letter in Instrument Serif, Bold, Italic. On hover, the container should rotate to 12 degrees with a 300ms transition."
    }
  ],
  "special_notes": "MUST: Use 'Instrument Serif' specifically for emphasis and large headers to maintain the editorial feel. MUST: Use the cubic-bezier(0.16, 1, 0.3, 1) curve for all entry animations. MUST: Use large corner radii (min 24px) for all containers. DO NOT: Use standard blue or green for primary actions; stick strictly to #EF4623. DO NOT: Use sharp 90-degree corners on any primary UI containers."
}
```

**▶ Try it live → [https://superdesign.dev/library/red-sun](https://superdesign.dev/library/red-sun)**

*513 copies · 1,616 tries · tags: landing page, page, style*
