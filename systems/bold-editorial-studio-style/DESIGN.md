# Design System — Bold Editorial Studio Style

> Category: Design Systems & Styles  ·  Industry: Agency & Studio
> Auto-scaffolded from prompt [`bold-editorial-studio-style`](../../prompts/bold-editorial-studio-style/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is built on 'Inter' typography with extreme weight and size contrasts. It uses a pure black (#000000) and white (#FFFFFF) palette with neutral gray accents (#525252, #737373) for secondary metadata. Motion is central, utilizing smooth cubic-bezier transitions for reveals and a custom 'difference' blend-mode cursor that scales on interaction. Images are primarily grayscale, transitioning to full color on hover to maintain visual discipline.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#000000`
- `#FFFFFF`
- `#525252`
- `#737373`
- `#0A0A0A`

## 3. Typography

- `Inter`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Apply a Bold Editorial Studio Style. 
- **Color Palette**: Primary background #FFFFFF; Primary text #000000; Secondary text #525252; Accents and borders #000000 at 10% opacity; Footer background #0A0A0A with #FFFFFF text.
- **Typography**: Primary Font: 'Inter'. 
  - Headlines: font-weight: 700; letter-spacing: -0.05em; line-height: 0.9.
  - Body: font-weight: 400; letter-spacing: -0.02em; line-height: 1.5.
  - Mono/Metadata: font-family: 'monospace'; font-size: 14px; text-transform: uppercase; letter-spacing: 0.1em.
- **Interactions**: 
  - Custom cursor: 32px circle, border: 1px solid black, background: white, mix-blend-mode: difference. Scale by 2.5x on hover. 
  - Image hover: Grayscale (100%) to Grayscale (0%) transition over 700ms with a 1.05x scale transform.
- **Animations**: 
  - Reveal: Text spans sliding up from translate-y(100%) to (0%) with cubic-bezier(0.16, 1, 0.3, 1) over …

## 5. Layout

The layout follows a spacious, section-based vertical flow. It starts with a massive display hero, followed by a continuous motion marquee, a centered introductory statement, and a balanced two-column project grid. The design concludes with a high-contrast dark footer.

## 6. Components

- **Interactive Difference Cursor** — A custom circular cursor that follows the mouse with smooth interpolation and changes appearance based on the underlying color.
- **Asymmetrical Marquee Cards** — Image containers within the marquee that use non-uniform border-radii to create an organic, editorial feel.

## 7. Motion

REVIEW —
- Motion is central, utilizing smooth cubic-bezier transitions for reveals and a custom 'difference' blend-mode cursor that scales on interaction
- Images are primarily grayscale, transitioning to full color on hover to maintain visual discipline
- 5x on hover
- - Image hover: Grayscale (100%) to Grayscale (0%) transition over 700ms with a 1
- - Marquee: Linear infinite scroll at 30s duration, pausing on container hover

## 8. Voice & Brand

Bold Editorial Studio Style is a high-impact, minimalist design system characterized by massive typography, a strict monochromatic palette, and sophisticated micro-interactions. It features a signature 'editorial' look using ultra-large display fonts (up to 12vw), custom cursor logic, and fluid marquee animations. Ideal for creative agencies, high-end portfolios, fashion brands, and premium fintech products, the system leverages white space and motion to create a premium, curated feel. Key elements include mix-blend-mode navigation, staggered text reveals, and asymmetrical image containers with varied border radii.

## 9. Anti-patterns

MUST: Maintain a strict black-and-white palette; any color should only come from project photography. MUST: Use smooth easing for all hover states (minimum 500ms). MUST: Hide the default browser cursor (`cursor: none` on body). DO NOT: Use borders heavier than 1px. DO NOT: Use standard system easing; stick to cubic-bezier(0.16, 1, 0.3, 1) for a premium feel.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
