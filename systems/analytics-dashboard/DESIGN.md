# Design System — Analytics dashboard

> Category: Dashboards  ·  Industry: General
> Auto-scaffolded from prompt [`analytics-dashboard`](../../prompts/analytics-dashboard/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The style is 'Modern Professional Enterprise'. It uses a light gray background (#F8F9FA) to make white cards (#FFFFFF) pop. Typography pairs Inter (Sans) for UI controls with JetBrains Mono (Monospace) for technical logs. Key colors include Brand Blue (#3B82F6), Success Green (#22C55E), and Warning Amber (#F59E0B). UI elements feature 8px corner radii, 1px borders (#E9ECEF), and soft 'card' shadows (0 1px 3px 0 rgba(0,0,0,0.1)).

## 2. Color Palette & Roles

REVIEW — role assignment is a guess; verify against the preview.

- `#F8F9FA`
- `#FFFFFF`
- `#3B82F6`
- `#22C55E`
- `#F59E0B`
- `#E9ECEF`
- `#2563EB`
- `#212529`
- `#868E96`
- `#10B981`
- `#EF4444`

## 3. Typography

- `Modern Professional Enterprise`
- `Inter`
- `JetBrains Mono`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Create a professional SaaS dashboard style. 

**Colors:** 
- Background: #F8F9FA
- Surface/Cards: #FFFFFF
- Primary: #3B82F6 (Hover: #2563EB)
- Text: #212529 (Secondary: #868E96)
- Border: #E9ECEF
- Status: Success (#10B981), Warning (#F59E0B), Danger (#EF4444)

**Typography:**
- UI Font: 'Inter', sans-serif; weights 400 (regular), 500 (medium), 600 (semibold).
- Data/Log Font: 'JetBrains Mono', monospace; weight 400.
- Headings: 14px Semibold tracking-tight.
- Body: 13px Regular.
- Technical Logs: 12px Mono.

**Effects:**
- Border Radius: 8px (standard), 6px (buttons/inputs).
- Shadows: 'card' (0 1px 3px rgba(0,0,0,0.1)), 'input' (0 1px 2px rgba(0,0,0,0.05)).
- Transitions: 200ms ease-in-out for hover states.
- Chart Grids: Dash-array 4, Color #E9ECEF.

## 5. Layout

A responsive two-column layout with a fixed-width left sidebar (256px) and a fluid main content area. Content is structured into a global header, high-level metrics grid, split chart/panel area, and a data table/event stream footer.

## 6. Components

- **Grouped Bar Chart** — Double-column vertical bar chart for comparison
- **Analytics Donut Chart** — Minimalist donut chart with centered summary
- **Segmented Control** — Time range selection toggle

## 7. Motion

REVIEW —
- - Primary: #3B82F6 (Hover: #2563EB)
- - Transitions: 200ms ease-in-out for hover states

## 8. Voice & Brand

Professional SaaS analytics dashboard design featuring a clean, enterprise-grade aesthetic. Utilizing a refined blue brand palette (#3B82F6), high-contrast gray scales, and dual-font pairing (Inter for UI, JetBrains Mono for data logs). The layout employs a classic sidebar-and-main-content structure with bento-style metric cards, interactive grouped bar charts, and technical event streams. Ideal for fintech, developer tools, cloud infrastructure monitoring, and complex data-driven enterprise platforms.

## 9. Anti-patterns

Must maintain consistent spacing (24px gutter between cards). Must use Lucide-style line icons. Must ensure charts have a 'dashed line' background grid at regular Y-intervals. Do not use overly rounded 'pill' corners for cards—keep them at 8px for a professional feel.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
