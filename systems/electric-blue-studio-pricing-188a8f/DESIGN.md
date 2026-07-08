# Design System — Electric-Blue Studio Pricing

> Category: Pricing Pages  ·  Industry: Dev Tools
> Auto-scaffolded from prompt [`electric-blue-studio-pricing-188a8f`](../../prompts/electric-blue-studio-pricing-188a8f/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Electric, high-contrast dark dev-tool aesthetic: near-black ink canvas, one saturated electric-blue accent used surgically for CTAs, glows, knobs and checkmarks, and a typographic system that pairs a tight geometric grotesk for display with an all-caps tracked monospace for labels/metadata. Subtle dotted grain texture and a blue glow shadow give it a 'terminal meets premium product' feel.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#08090c`
- `#0e1016`
- `#13161f`
- `#21242f`
- `#2563ff`
- `#4d7bff`
- `#163fb0`
- `#bcd1ff`
- `#4a5168`

## 3. Typography

- `Space Grotesk`
- `JetBrains Mono`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Dark, electric, terminal-grade SaaS aesthetic. Palette: background ink #08090c (near-black), panel #0e1016, card surfaces #13161f, hairline borders/dividers #21242f (very low-contrast lines). Single accent: electric blue elec #2563ff (CTAs, knobs, focus glow), bright variant elecbright #4d7bff (hover, checkmarks, small accents), deep variant elecdeep #163fb0 (filled accent panel), and an icy tint ice #bcd1ff for soft highlights. Text is white at graded opacities: headlines pure white, body white/55, muted labels white/40-45, micro-print white/30-35. Typography: 'Space Grotesk' (weights 400-700) for all display and UI copy, set very tight (letter-spacing -0.04em, line-height ~0.9 on the giant headline); 'JetBrains Mono' (400-700) for ALL small labels, eyebrows, price-billing notes, nav items, footer links, and badges, always uppercase with wide tracking (0.1em-0.28em). Signature 'outline- …

## 5. Layout

Frameless, single-column responsive web page (max content width 1280px, padded 20-32px) that flows top to bottom: sticky translucent nav, a centered hero headline + sub, a two-column pricing grid (primary plan card | accent panel + add-on power-ups) that collapses to one column on mobile, a fine-print tax note with an FAQ jump pill, a social-proof strip, a two-column FAQ accordion, and a footer. The pricing card grid is the visual + functional centerpiece. Cards reflow from the 2-column (1fr + fixed 360px) desktop layout down to a single stacked column on small screens; the feature checklist inside the card goes 2-col to 1-col.

## 6. Components

- **Outline / ghost statement headline** — The second line of each big heading is rendered as transparent-fill outlined type (only a hairline stroke), creating a layered solid-white-over-ghost-blue-grey effect that defines the page's typographic personality.
- **Monthly/annual billing toggle with price flip** — A custom rounded-full switch that toggles the plan card between monthly and annual, sliding an electric knob and swapping both the giant price number and the mono billing-period sub-line; annual is the default-on state and shows a 'SAVE 25%' badge.
- **Add-on power-up toggles** — Three optional feature switches that let users compose extra capacity on top of the single base plan — the interactive expression of the 'one plan + power-ups' pricing model.
- **Rotated accent panel** — A solid electric-deep-blue panel tilted a couple degrees to break the grid, reinforcing the single-plan value prop with a big '842 PROMPTS UNLOCKED' stat.
- **elec-glow accent treatment** — A reusable electric-blue glow (subtle ring + large soft drop shadow) applied to all primary interactive/branded elements to give them a charged, light-emitting quality.
- **Native details FAQ accordion** — Lightweight, JS-free expand/collapse FAQ using native details/summary with a custom rotating plus-to-x icon.

## 7. Motion

REVIEW —
- Single accent: electric blue elec #2563ff (CTAs, knobs, focus glow), bright variant elecbright #4d7bff (hover, checkmarks, small accents), deep variant elecdeep #163fb0 (filled accent panel), and an icy tint ice #bcd1ff for soft highlights

## 8. Voice & Brand

A frameless, near-black dev-tool SaaS pricing page with one electric-blue accent, oversized outlined-type headline, and a single-plan card (monthly/annual toggle + optional power-up add-ons) instead of a tier wall.

## 9. Anti-patterns

Frameless, fully responsive web page (no device chrome): content is centered in a max-w-1280px container with 20-32px side padding, and the pricing grid sits in a max-w-940px well. Layout reflows gracefully — the pricing grid goes from 2 columns (1fr + 360px) to a single stacked column, the in-card feature checklist goes 2-col -> 1-col, nav links and the annual 'SIGN IN' link hide on mobile, and the fine-print + FAQ-jump row stacks and centers. The nav is sticky with a translucent blurred background. The defining structural choice is a SINGLE-PLAN pricing model (one card with a monthly/annual toggle) augmented by optional add-on power-up toggles, deliberately rejecting the usual 3-tier comparison wall — copy throughout ('ONE PLAN. NO TIERS.', 'WHY ONE PLAN') reinforces this. Built with Tailwind (CDN config defining the custom color tokens), Iconify Phosphor (ph:*) icons, and Google Fonts Space Grotesk + JetBrains Mono. Brand voice in supporting copy stays warm and human ('ping us and we'll sort it together'). No em-dashes used in customer-facing copy.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
