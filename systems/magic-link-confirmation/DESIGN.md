# Design System — Magic Link Confirmation

> Category: Auth & Login  ·  Industry: General
> Auto-scaffolded from prompt [`magic-link-confirmation`](../../prompts/magic-link-confirmation/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is defined by its 'calm minimal' approach. It uses the Switzer typeface for a modern geometric feel, a neutral Slate-based color palette (#0F172A for headings, #64748B for body text), and subtle depth through soft shadows and rounded corners (24px for cards). Animations are smooth, utilizing cubic-bezier curves for organic motion.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#0F172A`
- `#64748B`
- `#FFFFFF`
- `#F8FAFC`
- `#10B981`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a minimalist light-theme UI using the Switzer font family. Color Palette: Background #FFFFFF with a subtle top-to-bottom gradient from #F8FAFC to transparent; Headings and Primary text #0F172A; Body text #64748B; Accents #10B981 (Emerald). Typography: Heading 1 at 24px font-size, font-weight 600, tight tracking; Body text at 15px, leading-relaxed; Secondary text at 12px-14px. Components should have high border-radius (rounded-xl 12px and rounded-3xl 24px). Use extremely soft shadows: shadow-[0_8px_30px_rgb(0,0,0,0.04)]. Implementation includes a fadeInUp animation (0.8s, cubic-bezier(0.16, 1, 0.3, 1)) and a gentle 5px floating animation for central icons.

## 5. Layout

A single-column, vertically centered layout designed for mobile screens, structured into a fixed header, a flexible centered content area, and a bottom-aligned footer.

## 6. Components

- **Animated Resend Button** — A secondary CTA button with a rotating icon on hover.
- **Floating Icon Container** — A central visual element that uses a slow floating animation to create a 'calm' vibe.

## 7. Motion

REVIEW —
- Animations are smooth, utilizing cubic-bezier curves for organic motion

## 8. Voice & Brand

A centered, message-driven layout designed to reassure users after initiating email-based authentication. Minimal actions and generous whitespace create a calm, waiting-state experience.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
