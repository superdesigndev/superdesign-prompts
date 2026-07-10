# Design System — Editorial Serif Receipt Email

> Category: Email & Newsletter  ·  Industry: E-commerce & Retail
> Auto-scaffolded from prompt [`editorial-serif-receipt-email`](../../prompts/editorial-serif-receipt-email/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Quiet-luxury, editorial e-commerce receipt. Warm paper background, near-black ink, muted grey micro-labels, and a single deep-navy accent for the primary button and Total. A condensed all-caps grotesque wordmark and tracked all-caps micro-copy pair with a readable serif for the headline, body, and product names. Thin hairline rules separate the phases; no heavy boxes or fills.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#faf9f6`
- `#eceae4`
- `#1b1b1a`
- `#182338`
- `#9a968e`
- `#e6e3dc`

## 3. Typography

- `Thank you for your order`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design an order-confirmation / receipt email in a centered max-width 600px column on a warm paper surface (#faf9f6) over a soft neutral body (#eceae4). Typography pairs Oswald (condensed, 500-700, UPPERCASE, letter-spacing ~0.13-0.16em) for the wordmark, section labels, buttons, and Total label with Spectral (serif, 400-700, plus an italic) for the headline, body copy, product names, and prices. Palette: ink #1b1b1a text, paper #faf9f6 surface, a single deep navy #182338 for the primary button + emphasis, muted #9a968e for micro-labels, and hairline rules #e6e3dc. Separate each phase (greeting / items / totals / customer info / help / footer) with thin 1px rules. Buttons are rectangular (not pill): primary = solid navy with uppercase Oswald white label; secondary = 1px ink/25 outline. Product thumbnails are 74px rounded-sm tiles with a 1px ink/15 ring + a subtle shadow so they read again …

## 5. Layout

Centered ~600px column, receipt flow: (1) wordmark + order number, (2) serif thank-you headline + greeting + button pair, (3) order summary = ship-status subhead + itemized rows + right-aligned totals, (4) two-column shipping/billing addresses + shipping method, (5) italic help prompt, (6) footer with serif tagline, two link columns, social row, fine print. On mobile the address grid stays 2-up and the dotted price leaders collapse gracefully (price stays right-aligned).

## 6. Components

_REVIEW: no components captured._

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A premium, editorial order-confirmation / receipt email in a centered 600px column: a condensed all-caps wordmark + order number, a serif 'Thank you for your order' headline, a solid-navy primary + outline secondary button pair, then an itemized order summary where each product row uses a thumbnail and a dotted leader line running to a right-aligned price, a subtotal / shipping / big Total block, a two-column shipping + billing address grid, a shipping method line, an italic help prompt, and a link-column footer with a serif tagline. Oswald condensed + Spectral serif, ink on warm paper with a single deep-navy accent. Reusable for any e-commerce receipt or transactional email.

## 9. Anti-patterns

This is a transactional EMAIL layout: a centered ~600px column, no sticky nav. Uses a generic store ('Meridian Supply') and sample order data so the spec ships without bundled assets; swap the wordmark, items, and addresses. The reusable value is the editorial receipt anatomy (dotted-leader line items + right-aligned Total + two-col addresses) and the warm-paper + serif + single-navy system.

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
