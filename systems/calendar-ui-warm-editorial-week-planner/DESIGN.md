# Design System — Calendar UI: Warm Editorial Week Planner

> Category: Calendar  ·  Industry: General
> Auto-scaffolded from prompt [`calendar-ui-warm-editorial-week-planner`](../../prompts/calendar-ui-warm-editorial-week-planner/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Warm editorial minimalism for productivity software. A cream/ivory canvas (#faf7f2) with warm near-black ink (#1a1714) and warm greys (#8b8178) instead of the usual white + cold grey. Exactly ONE saturated accent, terracotta (#c4623d), used sparingly for the highest-signal elements only: the 'today' marker, the primary 'New event' button, and the live current-time line. Event blocks use a small, restrained, warm-forward palette of four muted families (terracotta / sage / dusty blue / amber) as soft tinted fills with a solid left accent bar and darkened family-colored text, never neon or fully saturated. The signature is a type pairing: a serif DISPLAY face (Fraunces) for the month title, date numerals, and section headers against a clean sans (Inter) for weekday labels, hour ticks, and event text. Hairlines are 1px in warm low-contrast greys; rhythm is generous and calm. The overall feel is a high-end paper planner rendered as software: legible above all, distinctive, and human.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#faf7f2`
- `#1a1714`
- `#8b8178`
- `#c4623d`
- `#7a8a6f`
- `#6f8299`
- `#cf9749`

## 3. Typography

- `New event`
- `My calendars`
- `Up next`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a light calendar/scheduler on a warm IVORY canvas (#faf7f2), NOT white and NOT a cold-blue theme. Text is warm near-black (#1a1714) with warm-grey secondary labels (#8b8178). Use exactly ONE saturated accent, terracotta (#c4623d), and spend it only on the 'today' marker, the primary button, and the current-time line. Color-code events with four MUTED warm families (terracotta, sage #7a8a6f, dusty blue #6f8299, amber #cf9749) as soft tinted blocks with a solid 3px left accent bar and darkened family-colored text; never use neon or saturated fills. Pair a serif display face (Fraunces) for the month title / date numerals / section headers with a sans (Inter) for weekday labels, hour ticks, and event text. Keep 1px warm hairlines, generous spacing, and a calm paper-planner register. Do NOT use indigo/violet/blue, gradients, or centered-everything layouts.

## 5. Layout

A full-viewport desktop app in three regions: (1) a sticky top bar (brand mark + serif month title left; Today + week arrows; a right cluster of Day/Week/Month switcher, search, a terracotta 'New event' button, and an avatar), (2) a fixed 264px left sidebar (mini-month picker, 'My calendars' checklist, 'Up next' agenda), and (3) a main week view sharing a ~58px left hour gutter across three stacked rows: a 7-column day-header row, an all-day row that spans multi-day items, and a scrollable hourly time grid holding absolutely-positioned event blocks. Reflows: at ≤1023px the sidebar hides and the week grid goes full width; at <640px the week grid is replaced by a single-day timeline for today. The top bar is sticky; the time grid scrolls between the header and the viewport edge.

## 6. Components

- **Week time-grid with hour gutter** — The core 7-day scheduling grid: a shared left hour gutter plus seven relative day columns with hour and half-hour hairlines.
- **Duration-scaled event block** — A tinted event block whose height encodes duration, with a solid left accent bar and title + meta.
- **Side-by-side conflict split** — Overlapping events share a time column by splitting horizontally.
- **Terracotta current-time line** — A live 'now' indicator drawn only on today's column.
- **Mini-month picker** — A compact month grid in the sidebar that marks today and highlights the visible week.
- **Calendar-list checklist** — A legend of toggleable calendars, each a color dot + label, that maps to the event colors.
- **All-day spanning row** — A row above the grid for all-day and multi-day items that span across day columns.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A warm editorial take on the calendar UI: an ivory week-planner scheduler with a serif month title, muted color-coded events, and a terracotta "today" marker. The layout is a full 7-day week time-grid (hourly rows, an all-day row, a live current-time line, and side-by-side blocks for conflicts) beside a left sidebar holding a mini-month picker, a "My calendars" color-dot checklist, and an "Up next" agenda. One warm accent (terracotta) over cream, four muted event families (terracotta, sage, dusty blue, amber), and a Fraunces-serif + Inter-sans pairing give it a "paper planner meets modern software" feel. Copy this calendar app design for any scheduler, booking tool, planning dashboard, or agenda view that wants to feel human and premium instead of cold and generic. Responsive: reflows to a single-day timeline on mobile.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
