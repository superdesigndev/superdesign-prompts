# Design System — iOS Design System UI: Dark Mode Stocks Watchlist App

> Category: Mobile Apps  ·  Industry: Finance & Crypto
> Auto-scaffolded from prompt [`ios-design-system-dark-stocks-watchlist`](../../prompts/ios-design-system-dark-stocks-watchlist/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

The Apple design system (Human Interface Guidelines) in the DARK appearance, not a stylized theme: true-black systemBackground #000000 as the page, elevated card surfaces #1C1C1E, tertiary fills (search, chips) #2C2C2E, label #FFFFFF, secondaryLabel rgba(235,235,245,0.6), hairline separators #38383A. Market-data semantics carry all the color: gains in dark-mode systemGreen #30D158, losses in systemRed #FF453A, filled as saturated badge rectangles with white text so the numbers are the brightest, most legible elements on screen; systemBlue #0A84FF appears only on small interactive accents (chevron, glyph dots). No purple, no page gradients, no glass; the only gradients are faint sparkline area fades and the duotone news thumbnails. Typography is the SF Pro system stack (-apple-system, 'SF Pro Text', 'SF Pro Display', system-ui) on the HIG ramp: Large Title 34/700, section headers 22/700, row labels 17/600, secondary 13/400, prices in tabular numerals (font-variant-numeric: tabular-nums). Flat, precise, generous 8pt spacing; the restraint and data density are the aesthetic.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#000000`
- `#1C1C1E`
- `#2C2C2E`
- `#FFFFFF`
- `#38383A`
- `#30D158`
- `#FF453A`
- `#0A84FF`

## 3. Typography

- `SF Pro Text`
- `SF Pro Display`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a native iOS dark-mode mobile screen using the Apple design system (Human Interface Guidelines) dark appearance. Page background is true black #000000; elevated cards #1C1C1E; tertiary fills (search fields, chips) #2C2C2E. Text: label #FFFFFF, secondaryLabel rgba(235,235,245,0.6); hairline separators #38383A at 1px. Use the SF Pro system font stack (-apple-system, 'SF Pro Text', 'SF Pro Display', system-ui) with the HIG type ramp: Large Title 34px/700 left-aligned under a gray 20px/700 date line, section headers 22px/700, primary row labels 17px/600, secondary 13px/400, all numerals tabular (font-variant-numeric: tabular-nums). Reserve color for meaning: dark-mode systemGreen #30D158 for gains, systemRed #FF453A for losses, both as saturated filled badges with white text; systemBlue #0A84FF only for small interactive accents. No purple, no page gradients, no emoji, no icon fonts;  …

## 5. Layout

A single-column mobile app screen (430px max width, centered, frameless) with a sticky header group and two content sections. Header: status bar row, date + Large Title with a trailing circular more-button, then a full-width rounded search field, all sticky on black. Section 1, the watchlist: a bold section header row ('My Symbols' + chevron) followed by seven 56px data rows in a strict three-column grid: 38% identity column (symbol over company name), 32% sparkline column, 30% right-aligned numbers column (price stacked over a fixed-width change badge), separated by inset hairlines. Section 2, news: a bold header + gray attribution line, then stacked media-object cards (text left, 88px square thumbnail right) on elevated surfaces with 12px gaps. A home-indicator pill closes the screen. The fixed badge width and tabular numerals keep every row's numbers optically aligned into a scannable column; sparklines share one viewBox scale so slopes compare across rows.

## 6. Components

- **Watchlist row with sparkline and change badge** — The signature row: ticker + company name on the left, a mid-cell trend sparkline, and a right-aligned tabular price stacked over a fixed-width filled percent badge, green for gains and red for losses, so sign, color, and slope always agree.
- **Inline-SVG trend sparkline** — A dependency-free sparkline drawn as inline SVG with an explicit viewBox and a faint area fade under the line; green rising for gainers, red falling for losers.
- **iOS dark large-title header with status bar and search** — The native iOS sticky header: status bar glyphs, a gray date eyebrow over the bold Large Title, a small circular more-button, and a dark rounded search field.
- **News story media-object with duotone thumbnail** — A Top Stories card on an elevated dark surface: headline and source meta on the left, an 88px duotone SVG thumbnail with a subtle chart motif on the right.
- **Home indicator pill** — The iOS home indicator closing the screen.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A native iOS dark mode stocks watchlist screen built to the Apple design system (Human Interface Guidelines dark appearance) on a true black background. A gray date over a bold Stocks large title, a dark search field, then seven My Symbols rows: ticker and company name, an inline SVG sparkline (green rising for gainers, red falling for losers), and a right-aligned tabular price above a fixed-width filled change badge in system green or system red. A Business News section with Top Stories on elevated dark surfaces and a home indicator close the screen. SF Pro, hairline separators, exact iOS dark system colors. Ideal for stocks, crypto, forex and portfolio watchlist screens in finance apps.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
