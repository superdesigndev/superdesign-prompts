# Design System — Palette — Social-first friendly sign-up

> Category: Auth & Login  ·  Industry: SaaS
> Auto-scaffolded from prompt [`palette-social-first-friendly-sign-up`](../../prompts/palette-social-first-friendly-sign-up/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Warm, friendly, approachable indie-maker SaaS aesthetic on a soft cream canvas with a coral primary accent and a teal secondary accent, set in Poppins. Rounded, pillowy surfaces (rounded-2xl inputs/buttons, rounded-4xl = 2rem cards), hairline cream borders, soft layered shadows with a coral-tinted glow under the hero card, decorative blurred coral/teal blobs and a faint two-color radial grain behind the hero, and playful touches (a hand-drawn SVG underline, a 5-star rating, gradient avatar chips). High polish, high warmth, low noise.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#fdf9f3`
- `#ffffff`
- `#ff7a59`
- `#c8431f`
- `#b83a16`
- `#2bb6a3`
- `#1fa18f`
- `#16776a`
- `#23201d`
- `#736c63`
- `#efe6d8`

## 3. Typography

- `From prompt to UI in one breath`
- `Create account`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Warm, friendly indie-maker SaaS sign-up + landing screen. Background canvas cream #fdf9f3; cards/surfaces white #ffffff. Typeface: Poppins (weights 400/500/600/700/800) from Google Fonts, antialiased, with sans fallback ui-sans-serif, system-ui, sans-serif. Two accent hues: a coral primary scale (DEFAULT #ff7a59, 600 #c8431f, 700 #b83a16) and a teal secondary scale (DEFAULT #2bb6a3, 600 #1fa18f, 700 #16776a). Neutrals: ink (headings/body strong) #23201d, muted (secondary text) #736c63, line (hairline borders) #efe6d8. Custom radius token 4xl = 2rem (the signup card and how-it-works cards), with rounded-2xl (16px) on inputs/buttons and rounded-full pills. Three named shadows: soft = 0 1px 2px rgba(35,32,29,.04), 0 12px 30px -12px rgba(35,32,29,.16); card = 0 2px 4px rgba(35,32,29,.04), 0 24px 60px -22px rgba(255,122,89,.28) (a coral-tinted glow under the signup card); btn = 0 8px 20px -8p …

## 5. Layout

A full-width sticky blurred nav, then a full-bleed hero section that is a two-column grid (left product pitch, right signup card) over decorative blobs + grain, then a logo marquee strip, a three-step 'how it works' section, a dark gradient CTA band, and a light footer. Everything is centered in a mx-auto max-w-6xl px-6 container. Below lg the hero stacks to one column, the nav center links and 'Log in' link hide, the social buttons stay full-width stacked, and the how-it-works / footer rows reflow to single column.

## 6. Components

_REVIEW: no components captured._

## 7. Motion

REVIEW —
- Smooth, low-key motion: a 26s horizontal logo marquee and a 6s vertical float on one CTA blob

## 8. Voice & Brand

A warm, social-first sign-up screen on a cream canvas: a two-column hero+signup landing with a friendly product pitch on the left (hand-drawn underline, teal-check benefits, a 5-star social-proof cluster) and a white rounded card on the right that leads with three full-width stacked social-auth buttons (Google, GitHub, Apple) above an 'or sign up with email' divider and a single email field with a coral 'Create account' CTA. Coral + teal accents, Poppins, a sticky blurred nav, a logo marquee, a three-step how-it-works, and a dark gradient CTA band.

## 9. Anti-patterns

Built on the Tailwind CDN with a custom theme.extend: fontFamily.sans = ['Poppins','ui-sans-serif','system-ui','sans-serif'] (Poppins weights 400;500;600;700;800 from Google Fonts); colors cream #fdf9f3, card #ffffff, coral {DEFAULT #ff7a59, 600 #c8431f, 700 #b83a16}, teal {DEFAULT #2bb6a3, 600 #1fa18f, 700 #16776a}, ink #23201d, muted #736c63, line #efe6d8; borderRadius.4xl = 2rem; three named shadows soft / card / btn (card = a coral-tinted glow 0 24px 60px -22px rgba(255,122,89,.28), btn = 0 8px 20px -8px rgba(255,122,89,.55)). CSS: html scroll-behavior smooth; .grain = two soft radial gradients (coral at 12% 18%, teal at 88% 8%); .focus-ring:focus-within = box-shadow 0 0 0 4px rgba(255,122,89,.18) + border #ff7a59; .marquee = translateX 0 -> -50% over 26s linear infinite; .float = a 6s ease-in-out translateY ±10px loop. Icons via Iconify (Phosphor 'ph:*' for UI glyphs, mdi:github / mdi:apple / mdi:twitter / mdi:discord, and an inline multi-color Google logo SVG). Coral is the primary action color, teal is the secondary/affirmation color, on a warm cream ground. The reusable prompt-library value is the SOCIAL-FIRST signup card pattern (SSO buttons leading above an OR divider and a single email field) wrapped in a friendly warm-SaaS landing (sticky nav, two-column hero with social proof, logo marquee, three-step how-it-works, dark CTA band, footer). Original prompt-library product for the placeholder brand 'Palette', faithfully reproducing the build HTML; the real reference is the 21st.dev / Tailark 'Login 1' social-first auth component (https://21st.dev/community/components/meschacirung/login-1/sign-up), re-skinned from a neutral shadcn palette to this cream/coral/teal Poppins system and re-providered to Google/GitHub/Apple. Responsive: nav center links hide below md, the 'Log in' nav link below sm, the hero stacks to one column below lg, the social buttons stay full-width stacked, no overflow at 390px.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
