# Design System — Enterprise Admin Platform

> Category: Dashboards  ·  Industry: SaaS
> Auto-scaffolded from prompt [`enterprise-admin-platform`](../../prompts/enterprise-admin-platform/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is 'Corporate Professional' with a focus on legibility and scale. It uses the Satoshi font family (weights 400-900) for a neutral but modern feel. The palette relies on Slate 950 (#020617) for dark backgrounds and Blue 600 (#2563eb) for actions. Micro-interactions include 0.8s ease-out fades, 12px backdrop blurs for nav panels, and scale transitions on feature cards. Borders are subtle (#e2e8f0) and layout follows a 40px grid system.

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#020617`
- `#2563eb`
- `#e2e8f0`
- `#151e2e`
- `#ffffff`
- `#f8fafc`
- `#16a34a`
- `#d97706`
- `#dc2626`

## 3. Typography

- `Corporate Professional`
- `Satoshi`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a design with a professional enterprise aesthetic. 
- **Typography**: Use 'Satoshi' sans-serif. Headers should be Bold/ExtraBold with tight tracking (-0.02em). Body text in Slate 500/600 with 1.625 line-height.
- **Colors**: Primary: #2563eb, Deep Slate: #151e2e, Background: #ffffff, Muted BG: #f8fafc. Accents: Success (#16a34a), Warning (#d97706), Error (#dc2626).
- **Borders & Radius**: Border-radius 12px for cards, 8px for buttons. Borders should be 1px solid #e2e8f0.
- **Effects**: Navigation uses a 'glass-panel' effect: background rgba(255, 255, 255, 0.7) with 12px backdrop-filter blur. Hero background uses a 40px x 40px gray grid line pattern.
- **Animations**: Implement 'fadeInUp' (0.8s duration, 20px offset) for section reveals. Use cubic-bezier(0.4, 0, 0.2, 1) for all hover transitions.

## 5. Layout

The layout follows a predictable, top-down enterprise narrative: Navigation -> Hero with Product Visual -> Social Proof -> Core Modules -> Quantifiable Impact (Stats) -> Security Proof -> FAQ -> CTA -> Detailed Footer.

## 6. Components

- **KPI Count-up** — Animated numbers that count from zero to the target value when entering the viewport.
- **Audit Log Table** — High-density information table with status badges.
- **Glass-Morphism Toggle** — Operational switch used for security policy simulations.

## 7. Motion

REVIEW —
- 8s ease-out fades, 12px backdrop blurs for nav panels, and scale transitions on feature cards
- 8s duration, 20px offset) for section reveals
- 2, 1) for all hover transitions

## 8. Voice & Brand

Enterprise Admin Platform is a professional, high-trust landing page design for corporate B2B SaaS, fintech, and infrastructure tools. It features a muted corporate color palette (whites, deep slates, and technical blues), a structured grid-based layout, and a focus on operational control and security. Key elements include a high-fidelity dashboard preview, KPI count-up animations, and a glass-morphism navigation bar. Suitable for enterprise management systems, cybersecurity platforms, and developer infrastructure tools.

## 9. Anti-patterns

MUST: Maintain a strict vertical rhythm with 128px spacing between major sections. MUST: Use only grayscale and primary blue for main UI, reserving colors like green/red strictly for status indicators. MUST NOT: Use rounded corners larger than 12px for structural elements. MUST NOT: Use heavy gradients; keep all surfaces flat or slightly glass-morphic.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
