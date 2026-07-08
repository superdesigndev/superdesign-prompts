---
title: "Architectural Blueprint"
slug: "architectural-blueprint"
category: "Design Systems & Styles"
tags: ["style"]
copyCount: 373
tryCount: 1746
author: "Jason Zhou"
try_url: "https://superdesign.dev/library/architectural-blueprint?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
---

# Architectural Blueprint

A technical, architectural blueprint style dashboard with grid systems, measurement markers, and drafting aesthetics.

<img src="preview.png" alt="Architectural Blueprint" width="640">

## Prompt

```text
<design-system>

# Design Style: Architectural Blueprint (The "Master Plan" Aesthetic)

## Design Philosophy

**Core Concept: Precision in Progress** This style treats the UI as a technical drawing or a floor plan in the drafting stage. It’s not a finished product; it’s the *logic* behind the product. It’s about measurements, grid math, and the beauty of structural planning.

**Core Tenets:**

1. **The "Cyanotype" Logic**: Traditionally, blueprints are white lines on a deep blue background. This high-contrast, inverted look suggests technical authority.

2. **Measurement Markers**: Every element should have visible "dimension lines" (arrows indicating width/height) or coordinate labels (e.g., `x:140, y:220`).

3. **Drafting Notations**: Use hand-written "redline" notes, circles around "errors," and margin comments to make the UI feel like a living document.

4. **Wireframe Transparency**: Elements are not solid; they are transparent wireframes where you can see the "skeleton" of the layers beneath.

5. **The Master Grid**: A prominent 10px / 50px grid is the foundation. Every element must align strictly to the intersections.

**The Vibe:**

- **Analytical & Calculated**: It feels like an engineering feat.

- **Work-in-Progress**: Suggests the AI is "building" the design in real-time.

- **Structural**: Focuses on the "bones" of the interface.

---

## Design Token System (The DNA)

### Colors (The "Cyanotype" Palette)

- **Background (Blueprint Blue)**: #003366 (Deep, matte technical blue).

- **Lines (Drafting White)**: #FFFFFF at 80% opacity (Clean, sharp lines).

- **Accents (Redline)**: #FF3333 (For "corrections" and critical CTAs).

- **Measurements (Cyan)**: #00FFFF (For coordinates and dimension lines).

### Typography

- **Font Family**: **"Architects Daughter"** (Google Fonts) for notes, or **"Roboto Mono"** for technical data.

- **Style**: Headings are in Block Caps. Labels are tiny, monospaced, and accompanied by a serial number.

### Textures & Patterns

- **Grid**: A repeating CSS background grid of 20px squares.

- **Paper Texture**: A subtle "vellum" or "blueprint paper" grain to give the blue background depth.

---

## Component Stylings

- **Cards**: Defined by thin white outlines with "crosshair" intersections at the corners.

- **Buttons**: Look like technical stamps or "Approved" boxes.

- **Dividers**: Lines with dimension arrows at each end (e.g., `<--- 1200px --->`).

## Animation

- **Drafting Reveal**: Sections "draw" themselves line-by-line using `stroke-dashoffset` animations.

- **Cursor Coordinate**: A small "crosshair" follows the cursor, showing its current X/Y coordinates in real-time.

</design-system>
```

**▶ Try it live → [https://superdesign.dev/library/architectural-blueprint](https://superdesign.dev/library/architectural-blueprint?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library)**

**Use it in your coding agent:** install the [Superdesign skill](https://github.com/superdesigndev/superdesign-skill), then:

```bash
superdesign get-prompts --slugs "architectural-blueprint" --json
```

*373 copies · 1,746 tries · style*
