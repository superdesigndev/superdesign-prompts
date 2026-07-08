# Design System — Minimalist Checkout

> Category: E-commerce  ·  Industry: E-commerce & Retail
> Auto-scaffolded from prompt [`minimalist-checkout`](../../prompts/minimalist-checkout/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Monochrome and minimalist aesthetic. Typography uses 'General Sans' for headings and 'Satoshi' for body text, creating a clean, modern look. The palette is restricted to #000000 (Black), #FFFFFF (White), and various shades of neutral gray for borders and backgrounds. Inputs are understated with #F9FAFB backgrounds and 1px borders. Animations are subtle, including smooth opacity shifts and a 0.99 scale transform on button clicks.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#000000`
- `#FFFFFF`
- `#F9FAFB`
- `#111827`
- `#6B7280`
- `#E5E7EB`

## 3. Typography

- `General Sans`
- `Satoshi`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a design with a minimalist monochrome palette: Background #FFFFFF, Inputs #F9FAFB, Text #111827, and Accents #000000. Use 'General Sans' for headings (weights 500, 600) and 'Satoshi' for body. Headers should be 20px with tracking-tight. Form labels must be 12px, uppercase, tracking-wide, using #6B7280. Inputs should have a 1px border (#E5E7EB), a 2px border-radius, and 12px 16px padding. Active states use #000000 borders and rings. Inactive sections are styled with 40% opacity and grayscale filters. Buttons are solid black (#000000) with white text, 16px vertical padding, and a 0.99 scale transform on click.

## 5. Layout

Centered single-column layout (max-width 520px) with a vertical flow. The page starts with a clean header, followed by stacked sections for shipping, payment, and review. Inactive steps are visually dimmed to focus user attention. A collapsible order summary is positioned above the final CTA.

## 6. Components

- **Numbered Progress Badge** — A 24px circular indicator used for step navigation.
- **Minimalist Input Field** — Ultra-clean form input with top-aligned labels.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A distraction-free, single-column checkout that removes visual competition and guides users step-by-step. Order summary is minimized or collapsible to keep attention on form completion.

Best suited for
Mobile-first stores, impulse purchases, low-priced items, audiences with short attention spans.

## 9. Anti-patterns

Do not use vibrant colors; stick strictly to the monochrome scale. Ensure all interactive elements have a transition of at least 200ms for border-color and opacity changes. The layout must remain centered and narrow even on wide screens to maintain the focused 'wireframe' feel.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
