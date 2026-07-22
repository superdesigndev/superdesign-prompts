# Design System — Dark Editorial Wall of Love Testimonial Section (Forest + Gold)

> Category: Testimonials  ·  Industry: SaaS
> Auto-scaffolded from prompt [`dark-editorial-wall-of-love-testimonial-section`](../../prompts/dark-editorial-wall-of-love-testimonial-section/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

A calm, premium, quiet-luxury DARK editorial aesthetic for a social-proof surface, the opposite of a busy or default-indigo testimonials block. A deep FOREST-GREEN #0e1c17 ground with lifted panels (#14261f) and quote cards (#15281f) carries warm cream ink #f2ede1 (used at opacity steps for hierarchy), cool sage-grey muted #a9b5ab, and faint gold-tinted + neutral hairlines. The single saturated element is a champagne/brass GOLD accent (#c9a35b fill, #d9bd83 light, #a8823f deep), deliberately muted and luxe rather than the bright amber a testimonials block usually reaches for, held to exactly where social proof lives: the five-star glyphs, the review-source badges (G2 / Product Hunt), the eyebrow and the one headline payoff word, the 'Start free' buttons, the stat units, and the oversized quotation-mark. Everything else is strictly cream + sage + forest, so the gold reads as 'ratings' and never as decoration. Type carries hierarchy from FAMILY CONTRAST, size, and weight rather than color: a characterful DISPLAY SERIF (Fraunces) for the section headline and the spotlight quote is the deliberate taste move (a real designer reaches for an editorial serif; an AI defaults to Inter-only), with a grotesk sans (Inter) for quote body, names, roles, badges, and buttons. The shape language is soft and modern: rounded-2xl cards with a faint gold-tinted hairline ring, rounded-full real-photo avatars, and small pill badges, with depth built from one lifted panel step and hairlines only (no heavy drop shadow on the dark ground). The signature is the WALL itself: a masonry of varying-height cards in mixed treatments (plain star / gold-ruled featured / native tweet / G2 / Product Hunt) so the grid reads as a real, heterogeneous stream of proof rather than a uniform template, anchored by one oversized spotlight quote. No gradient anywhere, no second accent hue, no glow: dark, credible, warm-but-restrained, conversion-first.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#0e1c17`
- `#14261f`
- `#15281f`
- `#f2ede1`
- `#a9b5ab`
- `#c9a35b`
- `#d9bd83`
- `#a8823f`

## 3. Typography

- `Start free`
- `Verified review`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a premium DARK, editorial 'quiet-luxury' WALL OF LOVE / testimonials social-proof SECTION for a desktop SaaS marketing page on a deep FOREST-GREEN #0e1c17 ground with lifted panels (#14261f) and quote cards (#15281f), making ONE champagne/brass GOLD accent (#c9a35b fill, #d9bd83 light, #a8823f deep) the entire chroma against warm cream ink (#f2ede1 at opacity steps), cool sage-grey muted (#a9b5ab), and faint gold-tinted + neutral hairlines. Build a two-typeface system where hierarchy comes from FAMILY CONTRAST + size + weight: a characterful DISPLAY SERIF (Fraunces) for the section headline (~52px / 500-600 / tight leading) and the spotlight quote (~30px) is the anti-slop signal (do NOT set everything in Inter), with a grotesk sans (Inter) for the quote body, names, roles, badges, buttons, and stat labels. Confine the gold to exactly where social proof lives: the five-star glyphs, …

## 5. Layout

A real framed page read top to bottom inside a max-w-7xl column with px-6 gutters: a glass sticky nav, a centered header block (eyebrow + Fraunces headline + subhead + rating pill), a monochrome logo strip, THE WALL (a columns-1 md:columns-2 lg:columns-3 masonry of 12 break-inside-avoid quote cards in mixed treatments), a full-width spotlight quote band, a four-up stat band with vertical hairline dividers, a closing CTA card, and a slim footer. It reflows cleanly: the masonry steps 3 -> 2 -> 1 column, the nav hides its center links behind the wordmark + 'Start free', the rating cluster and stat band and logo strip wrap, the CTA buttons stack, and there is no horizontal overflow at 390px.

## 6. Components

- **Heterogeneous quote-card masonry** — The centerpiece: a CSS-columns masonry of 12 varying-height quote cards in five mixed treatments so no two read alike and the grid reads as a real, heterogeneous stream of proof rather than a uniform template.
- **Native X / tweet review card** — A quote card styled as a real X post, so the wall mixes formal reviews with authentic social chatter.
- **Review-source badge card (G2 / Product Hunt)** — Quote cards led by a verified-source pill, the credibility signal that closes the 'is this real' gap.
- **Rating summary cluster** — The at-a-glance trust anchor under the headline: a compact pill that fuses faces, stars, and the aggregate score.
- **Oversized spotlight quote band** — A full-width feature quote that breaks the masonry rhythm and gives the section one hero testimonial.
- **Four-up stat band with hairline dividers** — The aggregate proof numbers, set in the display serif so they read as a confident editorial statement.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A premium DARK, editorial "wall of love" testimonials / social-proof SECTION for a SaaS marketing page. A deep forest-green ground with warm cream text and ONE champagne-gold accent (no gradient) carries a Fraunces serif headline ("Praise that ships itself.") over a rating summary cluster (stacked avatars + five gold stars + "4.9 / 5 from 3,000+ reviews") and a monochrome logo trust strip. The centerpiece is a responsive MASONRY wall of quote cards of varying height that mixes plain star cards, gold-ruled featured cards, native X / tweet cards, and review-source badge cards (G2 "Verified review", Product Hunt "#1 Product of the Day"), each with a real avatar + name + role. A full-width SPOTLIGHT quote (an oversized quotation-mark + a big Fraunces quote), a four-up stat band, and a closing CTA finish it. Gold lives only in the stars, badges, buttons, and stat units; everything structural stays forest-green and cream. Reusable for any SaaS, indie, or agency site that wants a credible, remixable dark social-proof section with real faces, star ratings, and source badges.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
