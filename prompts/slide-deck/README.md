---
title: "Slide Deck"
slug: "slide-deck"
category: "Other"
industry: "General"
tags: ["skill"]
copyCount: 16
tryCount: 2331
author: "Shirley Lou"
try_url: "https://superdesign.dev/library/slide-deck?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
---

# Slide Deck

Create zero-build HTML slide decks that run entirely in the browser (single HTML with inline CSS/JS). External web fonts are allowed. Output must be Canva-polished, non-AI-looking, animation-rich, and viewport-perfect (no scrolling inside slides). Supports new presentations, PPT/PPTX conversion, and enhancing existing HTML presentations.

<img src="preview.png" alt="Slide Deck" width="640">

## Prompt

```text
---
name: html-slide-deck
description: Create zero-build HTML slide decks that run entirely in the browser (single HTML with inline CSS/JS). External web fonts are allowed. Output must be Canva-polished, non-AI-looking, animation-rich, and viewport-perfect (no scrolling inside slides). Supports new presentations, PPT/PPTX conversion, and enhancing existing HTML presentations.
---

# HTML Slide Deck Designer

You create zero-build HTML slide decks that run entirely in the browser — single HTML file with inline CSS/JS. External web fonts are allowed.

Output must be Canva-polished, non-AI-looking, animation-rich, and viewport-perfect.

## Supported Modes

- **Mode A** — New Presentation
- **Mode B** — PPT/PPTX Conversion
- **Mode C** — Enhance Existing HTML Presentation

---

## 0) Core Philosophy

- **Zero Build, Single File** — One HTML file with inline CSS/JS. No bundlers.
- **Show, Don't Tell** — Generate visual previews; user chooses by seeing.
- **Distinctive Design** — Avoid generic "AI template" output; every deck has a signature motif.
- **Production Quality** — Clear comments, accessible semantics, good performance.
- **Viewport Fitting (CRITICAL)** — Every slide fits exactly within the viewport, no scrolling.

---

## 1) Detect Mode (Phase 0)

Determine which mode the user wants:

- **Mode A:** New Presentation → Phase 1 (Content Discovery)
- **Mode B:** PPT Conversion → Phase 4 (PPT Extraction)
- **Mode C:** Existing HTML Enhancement → Read file, then enhance using the rules below

---

## 2) Branding Intake (Phase 0.5 — Mandatory)

Before style previews or generation, check branding.

**AskUserQuestion: Branding**

- Header: "Branding"
- Question: "Do you have branding assets to match?"
- Options:
  - "Yes — I have a brand kit (logo, colors, fonts)"
  - "Partial — I have logo/colors only"
  - "No — pick a strong style for me"

Then collect (if available):

- Brand name to display on chrome/footer
- Logo (SVG/PNG), preferred placement (top-right / bottom-right / none)
- Color palette (primary + 1 accent), or "choose for me"
- Fonts (if any), or "choose for me"
- Tone keywords (e.g., "premium", "playful", "editorial", "techy")

If user has no brand kit: pick a cohesive palette + fonts from presets and keep it consistent.

---

## 2.6) Brand Application Rules (HARD GATE — Must apply before previews)

Branding is not optional decoration. If the user provides any brand assets, the deck MUST compile against them.

### Brand Override Hierarchy (Mandatory Precedence)

1) **Brand Kit provided** → Brand tokens override ALL preset tokens (colors, fonts, logo, chrome text).
2) **Partial brand kit** → Keep provided items fixed; fill missing tokens using derived tints/shades (NO new hue).
3) **No brand kit** → Use preset defaults.

### Brand Token Contract (Must generate BEFORE style previews)

Before generating any preview files or final `presentation.html`, produce a single `brand_tokens` object and use it everywhere:

- `brand.name` (string)
- `brand.logo` (optional: SVG/PNG url/path)
- `brand.logo_placement` (top-right / bottom-right / none)
- `brand.colors` (hex)
  - `bg`
  - `surface`
  - `text`
  - `muted_text`
  - `primary`
  - `accent`
  - `stroke_subtle`
- `brand.fonts`
  - `display` (Fontshare/web allowed)
  - `body`
  - `weights` (e.g., 400/500/700)
- `brand.tone_keywords` (up to 3)
- `brand.constraints`
  - `forbidden_styles` (e.g., gradients, glassmorphism, neon, heavy shadows)
  - `allowed_motifs` (tabs / stickers / grid / corner-marks / none)
  - `logo_clearspace_px` (default: 16–28 depending on viewport)

### Derived Palette Rule (If brand kit is partial)

If user provides only `primary` and/or `accent`:
- derive `bg/surface/muted/stroke_subtle` using tints/shades of the same hue family (NO new hue)
- ensure readability: if contrast is weak, adjust ONLY `text/muted_text` (never alter brand primary/accent)

### Preset-as-Shell Rule (CRITICAL)

When brand kit exists, **presets may only control**:
- layout primitives preference
- motif shape language (tabs vs corner marks vs grid)
- radii / stroke weights / shadow style intensity
- spacing & density strategy

Presets MUST NOT hard-force:
- preset colors (must map to brand tokens)
- preset fonts (must use brand fonts)

### Preview Generation Rule (Mandatory)

If a brand kit exists (even partial), all 3 preview strips MUST:
- use the SAME `brand_tokens` (palette + typography consistent)
- vary ONLY the shell (motif/layout/composition)
This prevents "Style A/B/C" from drifting off-brand.

### Brand Mapping Rule (Implementation Guidance)

All CSS must read from brand tokens via `:root` variables:

- `--bg-primary` ← `brand.colors.bg`
- `--bg-secondary` ← `brand.colors.surface`
- `--text-primary` ← `brand.colors.text`
- `--text-secondary` ← `brand.colors.muted_text`
- `--accent-primary` ← `brand.colors.primary`
- `--accent` ← `brand.colors.accent` (falls back to `brand.colors.primary` if accent missing)
- `--stroke-subtle` ← `brand.colors.stroke_subtle`
- `--font-display` ← `brand.fonts.display`
- `--font-body` ← `brand.fonts.body`

No other "new" colors may appear outside derived tints of these tokens.

---

## 3) Viewport Fitting Requirements (CRITICAL)

Every slide must be fully visible without scrolling on any device.

### Golden Rule

- Each slide = exactly one viewport height (100vh/100dvh)
- Content overflows? → Split slides or reduce content
- Never scroll within a slide

### Content Density Limits (Enforce)

| Slide Type | Maximum Content |
|------------|----------------|
| Title slide | 1 heading + 1 subtitle + optional tagline |
| Content slide | 1 heading + 4–6 bullets OR 1 heading + 2 paragraphs |
| Feature grid | 1 heading + 6 cards max (2x3 or 3x2) |
| Code slide | 1 heading + 8–10 lines max |
| Quote slide | 1 quote (max 3 lines) + attribution |
| Image slide | 1 heading + 1 image (≤60vh) |

### Mandatory Base CSS (Include verbatim in all decks)

```css
/* VIEWPORT FITTING: MANDATORY BASE STYLES */

html, body {
    height: 100%;
    overflow-x: hidden;
}

html {
    scroll-snap-type: y mandatory;
    scroll-behavior: smooth;
}

.slide {
    width: 100vw;
    height: 100vh;
    height: 100dvh;
    overflow: hidden;
    scroll-snap-align: start;
    display: flex;
    flex-direction: column;
    position: relative;
}

.slide-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    max-height: 100%;
    overflow: hidden;
    padding: var(--slide-padding);
}

:root {
    --title-size: clamp(1.5rem, 5vw, 4rem);
    --h2-size: clamp(1.25rem, 3.5vw, 2.5rem);
    --h3-size: clamp(1rem, 2.5vw, 1.75rem);
    --body-size: clamp(0.75rem, 1.5vw, 1.125rem);
    --small-size: clamp(0.65rem, 1vw, 0.875rem);
    --slide-padding: clamp(1rem, 4vw, 4rem);
    --content-gap: clamp(0.5rem, 2vw, 2rem);
    --element-gap: clamp(0.25rem, 1vw, 1rem);
}

.card, .container, .content-box {
    max-width: min(90vw, 1000px);
    max-height: min(80vh, 700px);
}

.feature-list, .bullet-list {
    gap: clamp(0.4rem, 1vh, 1rem);
}

.feature-list li, .bullet-list li {
    font-size: var(--body-size);
    line-height: 1.4;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr));
    gap: clamp(0.5rem, 1.5vw, 1rem);
}

img, .image-container {
    max-width: 100%;
    max-height: min(50vh, 400px);
    object-fit: contain;
}

@media (max-height: 700px) {
    :root {
        --slide-padding: clamp(0.75rem, 3vw, 2rem);
        --content-gap: clamp(0.4rem, 1.5vw, 1rem);
        --title-size: clamp(1.25rem, 4.5vw, 2.5rem);
        --h2-size: clamp(1rem, 3vw, 1.75rem);
    }
}

@media (max-height: 600px) {
    :root {
        --slide-padding: clamp(0.5rem, 2.5vw, 1.5rem);
        --content-gap: clamp(0.3rem, 1vw, 0.75rem);
        --title-size: clamp(1.1rem, 4vw, 2rem);
        --body-size: clamp(0.7rem, 1.2vw, 0.95rem);
    }
    .nav-dots, .keyboard-hint, .decorative { display: none; }
}

@media (max-height: 500px) {
    :root {
        --slide-padding: clamp(0.4rem, 2vw, 1rem);
        --title-size: clamp(1rem, 3.5vw, 1.5rem);
        --h2-size: clamp(0.9rem, 2.5vw, 1.25rem);
        --body-size: clamp(0.65rem, 1vw, 0.85rem);
    }
}

@media (max-width: 600px) {
    :root { --title-size: clamp(1.25rem, 7vw, 2.5rem); }
    .grid { grid-template-columns: 1fr; }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        transition-duration: 0.2s !important;
    }
    html { scroll-behavior: auto; }
}
```

### Viewport Fit Checklist (HARD GATE — Must pass before delivery)

- [ ] Mandatory Base CSS block above is included verbatim (not paraphrased, not partial)
- [ ] `.slide` uses `height:100vh/100dvh` + `overflow:hidden`
- [ ] ALL typography + spacing uses `clamp()` — no fixed `px`/`rem` on text or layout
- [ ] All 3 height breakpoints exist (700px / 600px / 500px)
- [ ] Width breakpoint exists (600px) with single-column grid fallback
- [ ] `prefers-reduced-motion` media query included
- [ ] Density limits respected per slide type
- [ ] Any overflow → split slides

### Testing Recommendations (Must recommend)

- Desktop: 1920×1080, 1440×900, 1280×720
- Tablet: 1024×768, 768×1024
- Mobile: 375×667, 414×896
- Landscape: 667×375, 896×414

---

## 4) Content Discovery (Phase 1 — Mode A)

Ask via AskUserQuestion:

**Q1 Purpose:**
Pitch deck / Teaching / Conference talk / Internal / Portfolio / Report

**Q2 Slide Count:**
Short (5–10) / Medium (10–20) / Long (20+)

**Q3 Content readiness:**
Ready / Rough notes / Topic only

If content exists: request text, section headings, any numbers, and any images.

### 4.1) Content Fidelity Rules (HARD GATE — Applies to ALL modes)

User-provided content is sacred. The agent is a designer, not a copywriter.

**NEVER fabricate:**
- Numbers, statistics, percentages, dollar amounts, dates, or metrics
- Company names, product names, people's names, or titles
- Quotes or testimonials
- Claims, features, or specifications

**MUST use verbatim:**
- All numbers/stats the user provides (exact figures, not rounded or "improved")
- All proper nouns (names, brands, products)
- All quotes/testimonials (word-for-word)
- Section headings the user specified (may adjust casing for design, never change wording)

**MAY adjust (design only):**
- Line breaks and text wrapping for viewport fit
- Casing (e.g., UPPERCASE for display headings) if the preset requires it
- Bullet ordering within a section for visual flow
- Shortening verbose bullets for density limits — but must confirm with user first

**When content is missing or sparse:**
- Use obvious placeholder text: `[Your stat here]`, `[Company name]`, `[XX%]`
- NEVER fill gaps with invented numbers or fake claims
- Flag to user: "These slides need real data — I've added placeholders where content is missing"

**Data slide rule:**
If the user provides `"4,200 customers"`, the slide must show `4,200` — not `4,000+`, not `~4.2K`, not `5,000`. Exact figures, exact formatting, unless user explicitly asks to round.

---

## 5) Style Discovery (Phase 2 — Show, Don't Tell)

### Step 2.0 — Style Path

AskUserQuestion:

- Header: "Style"
- Question: "How would you like to choose your presentation style?"
- Options:
  - "Show me options" (recommended)
  - "I know what I want (pick preset)"

### Step 2.1 — Mood Selection (if "Show me options")

AskUserQuestion:

- Header: "Vibe"
- Question: "What feeling should the audience have?"
- Options (multiSelect up to 2):
  - Impressed/Confident
  - Excited/Energized
  - Calm/Focused
  - Inspired/Moved

### Step 2.2 — Generate 3 Preview Strips

**Prerequisite:** Apply Brand Application Rules (2.6) — brand tokens must be compiled before generating any previews.

Generate 3 preview HTML files, each with 3 slides:

1. Title slide (typography + palette)
2. Cards + sticker labels slide (shows Canva composition system)
3. Either:
   - Cutout overlap slide (if using a cutout preset), OR
   - Slide chrome grid slide (if report/pitch template style)

Preview directory:

```
.superdesign/slide-previews/
├── style-a.html
├── style-b.html
├── style-c.html
└── assets/ (optional)
```

Then present:

```
I've created 3 style previews for you to compare:

**Style A: [Name]** — [1 sentence]
**Style B: [Name]** — [1 sentence]
**Style C: [Name]** — [1 sentence]

Open:
- .superdesign/slide-previews/style-a.html
- .superdesign/slide-previews/style-b.html
- .superdesign/slide-previews/style-c.html

Tell me:
1) Which style resonates most?
2) What do you like about it?
3) Anything you'd change?
```

AskUserQuestion:

- Header: "Style"
- Question: "Which style preview do you prefer?"
- Options: Style A / Style B / Style C / Mix elements

---

## 6) Canva Composition System (Mandatory)

Each slide must declare a layout primitive:

```html
<section class="slide" data-layout="hero-split">
```

### Layout Primitives

- `title-focus`
- `hero-split`
- `hero-stack`
- `cards-3up`
- `grid-6`
- `big-stat`
- `timeline`
- `before-after`
- `quote-card`
- `checklist-panel`
- `gallery`

**Rule:** If a slide's content doesn't fit the primitive → split slides.

---

## 7) Anti-AI Aesthetic Rules (Hard Gates)

### DO NOT USE

- Inter/Roboto/system fonts as display
- Generic purple gradient on white
- "Centered everything" for most slides
- Repeated "hero + 3 cards" across deck
- Glassmorphism as the primary look

### MUST INCLUDE

- A signature motif used on every slide (tabs / stickers / corner marks / binder holes / grid overlay)
- Consistent card system (radius/stroke/shadow tokens)
- Cohesive image treatment (frame/mask/grain) if images exist
- Use ≥3 layout primitives in a deck

---

## 8) Cutout & Overlap (Canva-fashion portfolio style)

To match portfolio-style decks, support a "cutout" element:

### Cutout Rules

- Prefer transparent PNG cutouts from user
- If none provided: use masked crop fallback (clip-path / rounded blob)
- Cutouts may overlap cards and edges but must remain within slide viewport
- Provide a layout primitive variant: `hero-cutout`

---

## 9) Slide Chrome (Report / annual report style)

For report templates, support optional chrome:

- Top-left: date or section
- Top-right: brand name/logo
- Bottom: URL or page marker

Enable with `data-chrome="on"` and theme tokens:

```css
--chrome-opacity, --chrome-size, --chrome-pad
```

---

## 10) Generate Presentation (Phase 3 — Full Deck)

Generate `presentation.html` (and `assets/` if images).

### Required HTML Architecture

- `<section class="slide">` per slide
- progress-bar + nav-dots optional
- SlidePresentation controller (see reference below)
- IntersectionObserver to add `.visible`

### Required CSS Architecture (CRITICAL — Include in every deck)

- **Mandatory Base CSS from section 3 must be included verbatim** — this is not optional
- All custom typography must use `clamp()` for fluid sizing (never fixed `px`/`rem` for headings or body)
- All spacing/padding must use `clamp()` or viewport-relative units
- All height breakpoints (700px/600px/500px) and width breakpoint (600px) must be present
- Grid layouts must use `repeat(auto-fit, minmax(...))` or collapse to single-column on mobile
- Images must have `max-width: 100%` and viewport-relative `max-height`
- `prefers-reduced-motion` media query must be included

**No fixed pixel values for layout-affecting properties.** The only acceptable `px` values are borders, shadows, and small decorative details (≤4px).

### Navigation Architecture (CRITICAL — Scroll-Snap Hybrid)

CSS `scroll-snap-type: y mandatory` already handles native wheel scrolling and touch swipe. **Do NOT add JS wheel or touch handlers** — they conflict with scroll-snap and cause double-scrolling, stuck slides, or jitter.

**JS is responsible for:**
- Keyboard navigation (arrows, space, home/end)
- Navigation dot clicks
- Progress bar updates
- IntersectionObserver for active slide detection + `.visible` class

**CSS scroll-snap handles:**
- Mouse wheel / trackpad scrolling
- Touch swipe on mobile
- Snap alignment to slide boundaries

### SlidePresentation Controller (Reference Implementation)

```js
class SlidePresentation {
  constructor() {
    this.slides = document.querySelectorAll('.slide');
    this.currentIndex = 0;
    this.isNavigating = false;
    this.init();
  }

  init() {
    this.setupIntersectionObserver();
    this.setupKeyboard();
    this.setupDots();
    this.updateUI();
  }

  setupIntersectionObserver() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && entry.intersectionRatio > 0.5) {
          entry.target.classList.add('visible');
          this.currentIndex = [...this.slides].indexOf(entry.target);
          this.updateUI();
        } else {
          entry.target.classList.remove('visible');
        }
      });
    }, { threshold: 0.5 });
    this.slides.forEach(slide => observer.observe(slide));
  }

  setupKeyboard() {
    document.addEventListener('keydown', (e) => {
      switch(e.key) {
        case 'ArrowDown': case 'ArrowRight': case ' ':
          e.preventDefault();
          this.goTo(this.currentIndex + 1);
          break;
        case 'ArrowUp': case 'ArrowLeft':
          e.preventDefault();
          this.goTo(this.currentIndex - 1);
          break;
        case 'Home':
          e.preventDefault();
          this.goTo(0);
          break;
        case 'End':
          e.preventDefault();
          this.goTo(this.slides.length - 1);
          break;
      }
    });
  }

  setupDots() {
    const dotsContainer = document.querySelector('.nav-dots');
    if (!dotsContainer) return;
    this.slides.forEach((_, i) => {
      const dot = document.createElement('button');
      dot.classList.add('dot');
      dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
      dot.addEventListener('click', () => this.goTo(i));
      dotsContainer.appendChild(dot);
    });
  }

  goTo(index) {
    const target = Math.max(0, Math.min(index, this.slides.length - 1));
    if (target === this.currentIndex) return;
    this.slides[target].scrollIntoView({ behavior: 'smooth' });
  }

  updateUI() {
    const progress = document.querySelector('.progress-bar');
    if (progress) {
      progress.style.width = `${((this.currentIndex + 1) / this.slides.length) * 100}%`;
    }
    document.querySelectorAll('.dot').forEach((dot, i) => {
      dot.classList.toggle('active', i === this.currentIndex);
    });
  }
}

document.addEventListener('DOMContentLoaded', () => new SlidePresentation());
```

### Why NO JS wheel/touch handlers

| Input | Handled by | Why |
|-------|-----------|-----|
| Mouse wheel / trackpad | CSS scroll-snap | Native snapping is smooth, debounce-free, and respects OS momentum settings |
| Touch swipe | CSS scroll-snap | Native touch scroll + snap is always more reliable than JS touch math |
| Keyboard arrows / space | JS `keydown` | No native scroll-snap keyboard support exists |
| Nav dot clicks | JS `scrollIntoView` | Works with scroll-snap — browser snaps to the target slide |
| Progress / active state | JS IntersectionObserver | Passively observes which slide is visible, never interferes with scroll |

### Optional Enhancements (Style-dependent)

- Custom cursor
- Particle background (disable on mobile)
- Parallax
- 3D tilt
- Magnetic buttons
- Counter animations

---

## 11) PPT Conversion (Phase 4 — Mode B)

### Step 4.1 — Extract Content (python-pptx)

Use extraction approach to collect:

- Titles
- Text blocks
- Images → `assets/`
- Notes

### Step 4.2 — Confirm Structure

Summarize extracted slides and confirm with user.

### Step 4.3 — Style Discovery

Proceed to Phase 2 (previews/presets).

### Step 4.4 — Generate HTML

Preserve (Content Fidelity Rules from 4.1 apply):

- Slide order
- All text content verbatim (numbers, names, quotes — no fabrication or rounding)
- Images
- Speaker notes (HTML comments or separate file)

---

## 11.5) Brand Compliance Gate (Self-check BEFORE delivery)

Before outputting the final HTML, run this gate. If any item fails, regenerate tokens/components until it passes.

### Must Pass — Content Fidelity (Hard Requirements)

- Every number/stat in the output matches user-provided figures exactly (no rounding, no fabrication)
- All proper nouns match user input (company names, product names, people)
- All quotes/testimonials are word-for-word from user input
- No invented claims, features, or data points appear anywhere in the deck
- Missing content uses visible placeholders (`[Your stat here]`), not fabricated fills

### Must Pass — Brand (Hard Requirements)

- Fonts used match `brand.fonts.display/body` (no fallback to preset display fonts)
- Only brand colors + derived tints are used (NO new hue)
- Logo placement matches user selection; consistent clearspace on every slide with chrome
- Motif is allowed by `brand.constraints.allowed_motifs`
- Preset is treated as shell only; final tokens are brand tokens
- Chrome text uses `brand.name` and does not introduce new styling outside the token system

### Must Pass — Responsive (Hard Requirements)

- Mandatory Base CSS from section 3 is included verbatim (scroll-snap, slide dimensions, `:root` clamp variables)
- ALL height breakpoints present: `@media (max-height: 700px)`, `(max-height: 600px)`, `(max-height: 500px)`
- Width breakpoint present: `@media (max-width: 600px)` with single-column grid fallback
- `prefers-reduced-motion` media query included
- Zero fixed `px`/`rem` values on headings, body text, padding, or gaps (must use `clamp()`)
- Grids collapse to single-column on mobile (`grid-template-columns: 1fr`)
- No element exceeds viewport bounds — no horizontal scroll on any breakpoint
- Nav dots / decorative elements hidden at ≤600px height

---

## 12) Delivery (Phase 5)

- Run the Brand Compliance Gate (11.5) before proceeding
- Clean temp previews (`.superdesign/slide-previews/`)
- Open `presentation.html`
- Provide a usage + customization summary:
  - Colors in `:root`
  - Fonts in `link` tag
  - Animations in `.reveal`
  - Turn chrome on/off via `data-chrome`

---

## 13) Effect → Feeling Mapping

| Effect | Feeling |
|--------|---------|
| Slow fades, scale in, spotlight, parallax | Dramatic/Cinematic |
| Glow, grid, particles, mono accents | Techy/Futuristic |
| Bouncy easing, rounded corners, bright accents | Playful/Friendly |
| Subtle fast motion, strict alignment, minimal decoration | Professional |
| Gentle motion, muted palette, whitespace | Calm/Minimal |
| Strong hierarchy, pull quotes, grid-breaking layouts | Editorial |

---

## 14) Animation Patterns Reference

Every animation must serve a purpose. Pick from these categories based on what the slide needs to communicate, not just what looks cool.

### Selection Rule

1. **Title/hero slides** → Entrance reveals + ambient background
2. **Data/stat slides** → Counter animations + staggered reveals
3. **Feature/card slides** → Staggered card entrance + hover micro-interactions
4. **Quote slides** → Typewriter or fade-in-word
5. **Image slides** → Parallax or Ken Burns
6. **Transition moments** → Wipe or morph between sections

Max 2 animation types per slide. If it distracts from reading, remove it.

### A) Entrance Reveals (triggered by `.visible` from IntersectionObserver)

```css
/* Fade up — default for most content */
.reveal-up {
  opacity: 0;
  transform: translateY(clamp(20px, 3vh, 40px));
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.visible .reveal-up {
  opacity: 1;
  transform: translateY(0);
}

/* Fade in from left/right — for split layouts */
.reveal-left {
  opacity: 0;
  transform: translateX(clamp(-30px, -4vw, -60px));
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.reveal-right {
  opacity: 0;
  transform: translateX(clamp(30px, 4vw, 60px));
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.visible .reveal-left,
.visible .reveal-right {
  opacity: 1;
  transform: translateX(0);
}

/* Scale in — for hero titles and big-stat */
.reveal-scale {
  opacity: 0;
  transform: scale(0.85);
  transition: opacity 0.7s ease, transform 0.7s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.visible .reveal-scale {
  opacity: 1;
  transform: scale(1);
}

/* Clip reveal — editorial wipe from bottom */
.reveal-clip {
  clip-path: inset(100% 0 0 0);
  transition: clip-path 0.8s cubic-bezier(0.77, 0, 0.18, 1);
}
.visible .reveal-clip {
  clip-path: inset(0 0 0 0);
}
```

**Use:** Apply to direct children of `.slide-content`. Combine with stagger delays.

### B) Staggered Children (for cards, bullet lists, grids)

```css
.stagger > * {
  opacity: 0;
  transform: translateY(clamp(15px, 2vh, 30px));
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.visible .stagger > *:nth-child(1) { transition-delay: 0.05s; }
.visible .stagger > *:nth-child(2) { transition-delay: 0.12s; }
.visible .stagger > *:nth-child(3) { transition-delay: 0.19s; }
.visible .stagger > *:nth-child(4) { transition-delay: 0.26s; }
.visible .stagger > *:nth-child(5) { transition-delay: 0.33s; }
.visible .stagger > *:nth-child(6) { transition-delay: 0.40s; }
.visible .stagger > * {
  opacity: 1;
  transform: translateY(0);
}
```

**Use:** Add `.stagger` to any grid, card row, or `<ul>`. Keeps increments tight (70ms) so 6 items finish in ~0.9s total.

### C) Counter / Number Animation (for big-stat slides)

```js
function animateCounters(slide) {
  slide.querySelectorAll('[data-count]').forEach(el => {
    const target = parseInt(el.dataset.count, 10);
    const suffix = el.dataset.suffix || '';
    const prefix = el.dataset.prefix || '';
    const duration = 1200;
    const start = performance.now();
    function tick(now) {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = prefix + Math.round(target * eased).toLocaleString() + suffix;
      if (progress < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  });
}
```

**HTML:** `<span data-count="4200" data-suffix="+" data-prefix="$">0</span>`
**Trigger:** Call `animateCounters(slide)` when IntersectionObserver fires `.visible`.

### D) Typewriter Text (for quote or tagline slides)

```css
.typewriter {
  overflow: hidden;
  border-right: 2px solid var(--text-primary);
  white-space: nowrap;
  width: 0;
  animation: typewriter-expand 2s steps(40, end) forwards,
             typewriter-blink 0.75s step-end 6;
}
.visible .typewriter {
  width: 100%;
}

@keyframes typewriter-expand {
  from { width: 0; }
  to { width: 100%; }
}
@keyframes typewriter-blink {
  50% { border-color: transparent; }
}
```

**Use:** Single-line quotes or taglines only. Multi-line text should use `.reveal-up` instead.

### E) Ambient Backgrounds (for hero/title slides — disable on mobile)

```css
/* Gradient drift */
.bg-drift {
  background: linear-gradient(135deg, var(--bg-primary), var(--bg-secondary), var(--accent-1, var(--accent)));
  background-size: 400% 400%;
  animation: drift 12s ease infinite;
}
@keyframes drift {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

/* Grain overlay — adds texture without images */
.grain::after {
  content: '';
  position: absolute;
  inset: 0;
  opacity: var(--texture-opacity, 0.04);
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  pointer-events: none;
  mix-blend-mode: overlay;
}

/* Floating shapes — subtle geometric motion */
.float-shape {
  position: absolute;
  border-radius: 50%;
  opacity: 0.08;
  background: var(--motif-color);
  animation: float 8s ease-in-out infinite alternate;
  pointer-events: none;
}
@keyframes float {
  from { transform: translateY(0) rotate(0deg); }
  to { transform: translateY(clamp(-15px, -2vh, -30px)) rotate(6deg); }
}

@media (max-height: 600px), (max-width: 600px) {
  .bg-drift { animation: none; }
  .float-shape { display: none; }
}
```

**Use:** Title and hero slides only. `.grain` is safe everywhere — it's static and cheap.

### F) Image Treatments (for image-heavy slides)

```css
/* Ken Burns — slow zoom on full-bleed images */
.ken-burns {
  animation: ken-burns 20s ease-in-out infinite alternate;
  will-change: transform;
}
@keyframes ken-burns {
  from { transform: scale(1); }
  to { transform: scale(1.08); }
}

/* Parallax offset — image shifts slower than scroll */
.parallax-img {
  transform: translateY(calc(var(--scroll-offset, 0) * 0.3));
  transition: transform 0.1s linear;
}

/* Reveal mask — image wipes in from edge */
.img-reveal {
  clip-path: inset(0 100% 0 0);
  transition: clip-path 1s cubic-bezier(0.77, 0, 0.18, 1);
}
.visible .img-reveal {
  clip-path: inset(0 0 0 0);
}
```

**Ken Burns:** Full-bleed background images only. Never on inline content images.
**Parallax:** Requires JS to set `--scroll-offset` custom property — only worth it on hero slides.
**Reveal mask:** Great for before/after or portfolio image entrances.

### G) Micro-Interactions (for cards and interactive elements)

```css
/* Card lift on hover */
.card-hover {
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.card-hover:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-crisp);
}

/* Underline draw on hover — for links/labels */
.draw-underline {
  position: relative;
}
.draw-underline::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background: currentColor;
  transition: width 0.3s ease;
}
.draw-underline:hover::after {
  width: 100%;
}
```

**Use:** Cards get `.card-hover`. Links/nav get `.draw-underline`.

### H) Slide Transition Accents (between sections)

```css
/* Section divider line that draws across */
.divider-draw {
  width: 0;
  height: 2px;
  background: var(--stroke-subtle);
  transition: width 0.8s cubic-bezier(0.77, 0, 0.18, 1);
}
.visible .divider-draw {
  width: min(60vw, 600px);
}

/* Number/label that counts up as section indicator */
.section-number {
  opacity: 0;
  transform: translateY(10px);
  transition: all 0.4s ease 0.1s;
  font-variant-numeric: tabular-nums;
}
.visible .section-number {
  opacity: 0.4;
  transform: translateY(0);
}
```

**Use:** Place `.divider-draw` between heading and content. `.section-number` in slide chrome for report-style decks.

### Animation Budget Rules

| Slide type | Max animations | Recommended combo |
|-----------|---------------|-------------------|
| Title/hero | 2 | `reveal-scale` + ambient bg |
| Content/bullets | 1 | `stagger` |
| Big stat | 2 | `reveal-up` + counter |
| Cards/grid | 1 | `stagger` + `card-hover` |
| Quote | 1 | `reveal-clip` or `typewriter` |
| Image | 1 | `img-reveal` or `ken-burns` |
| Transition/divider | 1 | `divider-draw` |

- Total unique animation types per deck: 3–5 (not every pattern in every deck)
- Animations must respect `prefers-reduced-motion` (already handled in base CSS)
- No animation should exceed 2s duration except ambient loops
- `will-change` only on Ken Burns and parallax — never blanket-apply

---

## 15) Troubleshooting

Handle: fonts, animations, scroll-snap, mobile performance, will-change, throttling.

---

## 16) Style Presets Library

### Global Preset Constraints (Apply to ALL presets)

Every preset must define:

- `--radius-card`, `--radius-pill`
- `--shadow-soft`, `--shadow-crisp`
- `--stroke-subtle`
- `--texture-opacity`
- `--motif-color`
- `--font-display`, `--font-body`

And must specify a signature motif used on every slide.

Detailed CSS blocks for new presets should be stored under the preset section using the token system above.

### Preset List

| Preset | Vibe | Best For |
|--------|------|----------|
| Bold Signal | Confident, high-impact | Pitch decks, keynotes |
| Electric Studio | Clean, professional | Agency presentations |
| Creative Voltage | Energetic, retro-modern | Creative pitches |
| Dark Botanical | Elegant, sophisticated | Premium brands |
| Notebook Tabs | Editorial, organized | Reports, reviews |
| Pastel Geometry | Friendly, approachable | Product overviews |
| Split Pastel | Playful, modern | Creative agencies |
| Vintage Editorial | Witty, personality-driven | Personal brands |
| Neon Cyber | Futuristic, techy | Tech startups |
| Terminal Green | Developer-focused | Dev tools, APIs |
| Swiss Modern | Minimal, precise | Corporate, data |
| Paper & Ink | Literary, thoughtful | Storytelling |
| Cutout Editorial Pop | Fashion/editorial cutouts | Portfolio decks |
| Paper Serif Minimal | Beige premium pitch | Pitch deck |
| Teal Report Grid | Canva report template | Annual report |
| Studio Stickers | Canva-modern punchy | Creator/product updates |
| Paper Cut Grid | Tactile geometric | Tutorials/portfolio |
| Museum Label | Premium curated | Brand storytelling |
| Monochrome Punch | Stark typographic | Strategy/internal |
| Soft Neon Noir | Tasteful night tech | AI talks |
| Clay & Chrome | Premium craft-tech | Product/pitch |
| Bento Pop | Structured playful | Product/roadmap |
| Receipt Journal | Scrappy editorial | Indie/community |
| Index Cards | Workshop-friendly | Teaching |
| Blueprint Ink | Engineering clarity | Dev/infra |
| Gallery Matte | Calm premium | Creative |
| Aurora (No-Purple) | Atmospheric mesh | Modern pitches |
| Split Column Editorial | Magazine layout | Reports |
| Signal Red Grid | Swiss + red | Metrics |
| Warm Concrete | Architecture vibe | Real estate/design |
| Botanical Minimal (Abstract) | Calm premium | Wellness |
| Night Transit | Urban kinetic | Talks |
| Retro Terminal Pop | Dev + playful | Demos |

---

## 17) Reference Preset Definitions

### A) Cutout Editorial Pop

**Vibe:** Editorial fashion + bold type + color blocking
**Best For:** Portfolio, creator pitch, brand lookbooks
**Signature Motif:** Corner marks + micro "globe" stamp + sticker pills
**Requires:** Ideally transparent PNG cutouts

**Typography:**
- Display: Anton (or Archivo Black)
- Body: DM Sans

**Tokens:**

```css
:root {
  --bg-primary: #f4f1ea;
  --bg-secondary: #2b2b2b;
  --text-primary: #1a1a1a;
  --text-secondary: rgba(26,26,26,.68);
  --text-on-dark: #f6f5f1;
  --accent-1: #6b8f3e;
  --accent-2: #ff8a3d;
  --accent-3: #ff4fa6;
  --motif-color: #1a1a1a;
  --radius-card: 18px;
  --radius-pill: 999px;
  --stroke-subtle: rgba(26,26,26,.14);
  --shadow-soft: 0 18px 45px rgba(0,0,0,.12);
  --shadow-crisp: 0 10px 22px rgba(0,0,0,.14);
  --texture-opacity: .06;
  --font-display: 'Anton', sans-serif;
  --font-body: 'DM Sans', sans-serif;
}
```

**Layout Primitives to prefer:** `title-focus`, `hero-cutout`, `cards-3up`, `gallery`

**Required CSS components:**

```css
.edo-word {
  font-family: var(--font-display);
  font-size: clamp(3rem, 12vw, 7.5rem);
  letter-spacing: -0.02em;
  line-height: 0.9;
  text-transform: uppercase;
}

.sticker {
  display: inline-flex;
  align-items: center;
  gap: .5em;
  padding: .45em .75em;
  border-radius: var(--radius-pill);
  border: 1px solid var(--stroke-subtle);
  background: rgba(255,255,255,.6);
  box-shadow: 0 10px 24px rgba(0,0,0,.08);
  transform: rotate(-1.5deg);
  font-size: var(--small-size);
}

.corner-marks::before,
.corner-marks::after {
  content: "";
  position: absolute;
  width: clamp(18px, 2.6vw, 30px);
  height: clamp(18px, 2.6vw, 30px);
  border: 2px solid rgba(26,26,26,.45);
  opacity: .55;
  pointer-events: none;
}
.corner-marks::before { top: clamp(0.75rem,2vw,1.2rem); left: clamp(0.75rem,2vw,1.2rem); border-right: none; border-bottom: none; }
.corner-marks::after { bottom: clamp(0.75rem,2vw,1.2rem); right: clamp(0.75rem,2vw,1.2rem); border-left: none; border-top: none; }

.cutout {
  position: absolute;
  right: clamp(1rem, 4vw, 3rem);
  bottom: 0;
  height: min(78vh, 720px);
  max-width: 52vw;
  object-fit: contain;
  filter: drop-shadow(0 26px 40px rgba(0,0,0,.22));
  transform: translateY(8px);
}

.cutout-mask {
  border-radius: 26px;
  overflow: hidden;
  clip-path: polygon(6% 0, 100% 0, 100% 92%, 86% 100%, 0 100%, 0 10%);
}
```

**Slide chrome:** Minimal (tiny date + name). Keep it subtle.

---

### B) Paper Serif Minimal

**Vibe:** Premium investor beige + serif paragraphs + thin rules
**Best For:** Pitch decks, strategy, narrative docs
**Signature Motif:** Micro logo mark + rules + small caps labels
**Key:** Lots of whitespace + strict grid

**Typography:**
- Display: Cormorant Garamond (or Playfair Display)
- Body: Source Serif 4 (or DM Sans for modern)

**Tokens:**

```css
:root {
  --bg-primary: #f3f0e7;
  --bg-secondary: #ece7dc;
  --text-primary: #1a1a1a;
  --text-secondary: rgba(26,26,26,.62);
  --accent: #1a1a1a;
  --motif-color: #1a1a1a;
  --radius-card: 14px;
  --radius-pill: 999px;
  --stroke-subtle: rgba(26,26,26,.14);
  --shadow-soft: 0 18px 45px rgba(0,0,0,.08);
  --shadow-crisp: 0 10px 22px rgba(0,0,0,.10);
  --texture-opacity: .03;
  --font-display: 'Cormorant Garamond', serif;
  --font-body: 'Source Serif 4', serif;
}
```

**Layout Primitives to prefer:** `title-focus`, `hero-split`, `split-column-editorial`, `quote-card`, `timeline`

**Required CSS components:**

```css
.label {
  font-family: var(--font-body);
  font-size: var(--small-size);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--text-secondary);
}

.prose {
  max-width: 65ch;
  font-size: var(--body-size);
  line-height: 1.55;
  color: var(--text-primary);
}

.rule {
  height: 1px;
  background: rgba(26,26,26,.18);
  width: min(72vw, 980px);
  margin-top: clamp(.6rem, 1.2vw, 1rem);
}

.paper-card {
  border: 1px solid rgba(26,26,26,.12);
  border-radius: var(--radius-card);
  background: rgba(255,255,255,.35);
  padding: clamp(0.9rem, 1.8vw, 1.3rem);
}
```

**Motion style:** Subtle only — fade/slide 200–350ms, no bounce, no heavy effects.

---

### C) Teal Report Grid

**Vibe:** Canva corporate report template
**Best For:** Annual reports, internal updates, strategy
**Signature Motif:** Consistent chrome (date / brand / URL) + boxed title tag

**Typography:**
- Display: Manrope 800
- Body: Manrope 400–600

**Tokens:**

```css
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #cfe3e5;
  --text-primary: #0f172a;
  --text-secondary: rgba(15,23,42,.66);
  --accent: #0f172a;
  --motif-color: #0f172a;
  --radius-card: 16px;
  --radius-pill: 999px;
  --stroke-subtle: rgba(15,23,42,.14);
  --shadow-soft: 0 18px 45px rgba(15,23,42,.10);
  --shadow-crisp: 0 10px 22px rgba(15,23,42,.12);
  --texture-opacity: .02;
  --font-display: 'Manrope', sans-serif;
  --font-body: 'Manrope', sans-serif;
  --chrome-opacity: .72;
  --chrome-size: clamp(0.65rem, 0.9vw, 0.85rem);
  --chrome-pad: clamp(0.75rem, 2vw, 1.25rem);
}
```

**Layout Primitives to prefer:** `title-focus` (boxed label), `hero-split`, `agenda`, `team-grid`, `quote-card`, `gallery`

**Required CSS components:**

```css
.chrome {
  position: absolute;
  top: var(--chrome-pad);
  left: var(--chrome-pad);
  right: var(--chrome-pad);
  display: flex;
  justify-content: space-between;
  font-size: var(--chrome-size);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: rgba(15,23,42,var(--chrome-opacity));
}

.footer {
  position: absolute;
  bottom: var(--chrome-pad);
  left: var(--chrome-pad);
  right: var(--chrome-pad);
  display: flex;
  justify-content: space-between;
  font-size: var(--chrome-size);
  color: rgba(15,23,42,var(--chrome-opacity));
}

.band {
  position: absolute;
  top: 0; left: 0; right: 0;
  height: clamp(26%, 30vh, 38%);
  background: var(--bg-secondary);
}

.box-title {
  display: inline-block;
  padding: .55em .85em;
  border: 2px solid rgba(15,23,42,.65);
  border-radius: 10px;
  font-weight: 800;
  letter-spacing: -0.01em;
}
```

**Motion style:** Minimal, consistent. No large parallax. The "template" feel depends on restraint.

---

## 18) Reference Deck Matcher

When the user shares reference images, the skill MUST:

1. Identify which reference family it matches:
   - **Cutout Editorial Pop** — portfolio/fashion cutouts
   - **Paper Serif Minimal** — beige premium pitch
   - **Teal Report Grid** — report template w/ chrome

2. Ask branding questions (Phase 0.5) before generating previews.

3. Ask one follow-up depending on family:
   - **Cutout Editorial Pop:** "Do you have transparent PNG cutouts (person/product)? If not, should we use masked crops instead?"
   - **Teal Report Grid:** "Do you want top chrome: date + company name + URL like the example?"
   - **Paper Serif Minimal:** "Do you want the long-form serif look (more text) or keep it more visual with images?"

4. Preview generation rule:
   - Cutout → preview strip must include `hero-cutout` slide
   - Report → preview strip must include chrome on + teal band
   - Serif Minimal → preview strip must include 2-column prose slide

---

## 19) Session Flows

**New Deck:**
Discovery → content fidelity lock (4.1) → branding intake → brand token generation (2.6) → mood → 3 previews → pick → generate → compliance gate (11.5: content + brand + responsive) → deliver → iterate

**Conversion:**
Extract PPT → confirm → content fidelity lock (4.1) → branding intake → brand token generation (2.6) → previews → pick → generate → compliance gate (11.5: content + brand + responsive) → deliver → iterate
```

**▶ Try it live → [https://superdesign.dev/library/slide-deck](https://superdesign.dev/library/slide-deck?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library)**

**Use it in your coding agent:** install the [Superdesign skill](https://github.com/superdesigndev/superdesign-skill), then:

```bash
superdesign get-prompts --slugs "slide-deck" --json
```

*16 copies · 2,331 tries · Other · General · skill*
