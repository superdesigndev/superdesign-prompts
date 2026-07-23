# Design System — Skeuomorphism Smart Home App: Dark Brushed-Metal Control Panel

> Category: Mobile Apps  ·  Industry: Smart Home
> Auto-scaffolded from prompt [`skeuomorphism-smart-home-app-ui-dark-brushed-metal-control-panel-with-thermostat-dial`](../../prompts/skeuomorphism-smart-home-app-ui-dark-brushed-metal-control-panel-with-thermostat-dial/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Dark tactile skeuomorphism (neo-skeuomorphism), NOT flat, NOT neumorphism-on-light. Ground is dark cool brushed graphite: base #16181c, control plates a linear-gradient #23262e to #191c22, hairline top-light #3a3f49. Ink is bright off-white #eef2f6 for load-bearing numerals and labels, muted #9aa3ad for secondary. Exactly two accents: a cool ice-blue #7fd8ff powered-on glow (active toggles, active devices, dimmer fill), and a warm heat arc amber #ffb24d to orange #ff7a2f used ONLY on the thermostat. Type: Space Grotesk for display and numerals, Inter for body, JetBrains Mono for small setpoint / energy / status readouts. Every surface uses a consistent shadow language so the metal reads as real: RAISED plate = inset 1px top highlight rgba(255,255,255,0.10) + inset bottom shadow rgba(0,0,0,0.55) + outer drop shadow 0 8px 20px rgba(0,0,0,0.5); DEBOSSED track / well = the reverse (inset dark top, faint light bottom); a brushed-metal sheen is a very low-opacity repeating-linear-gradient overlay; a lit control adds a colored box-shadow bloom plus a brighter inner face so ON reads as actual light. All effects are pure CSS and SVG, no JavaScript needed for the visible frame, so every state is frozen and the render is faithful.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#16181c`
- `#23262e`
- `#191c22`
- `#3a3f49`
- `#eef2f6`
- `#9aa3ad`
- `#7fd8ff`
- `#ffb24d`
- `#ff7a2f`

## 3. Typography

_REVIEW: no font families captured._

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

_none captured_

## 5. Layout

_REVIEW_

## 6. Components

- **Brushed-metal thermostat dial (hero)** — The load-bearing focal control: a large circular metal dial with a knurled rim, an SVG heat gauge, and a bright temperature numeral that dominates the screen.
- **Rocker toggle (raised thumb in a debossed track)** — The repeated on/off control across the device grid; the single clearest signal of value contrast.
- **Debossed dimmer slider** — A tactile brightness control on the Lights card that shows a filled ice-blue level.
- **3D pushable scene buttons** — A row of tactile preset buttons where one is shown physically pressed and lit.
- **Metal tab bar with raised center voice FAB** — The bottom navigation, pinned to the bottom of the page, anchored by a glowing center microphone button.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A dark tactile skeuomorphism mobile app home screen for smart-home / IoT control. On a brushed-graphite wall, every control is a raised, top-lit dark-metal plate: a large brushed-metal thermostat dial with a knurled rim, a glowing amber heat arc and a big bright temperature readout; a pressed-metal room switch; a row of 3D pushable scene buttons; and a six-card device grid with real rocker toggles that light ice-blue when a device is on, plus a dimmer slider. A metal tab bar carries a raised center voice button. Two accents only, a cool ice-blue powered-on glow and one warm amber heat arc, on a dark ground so every control keeps real value contrast and nothing washes out. Reusable for any smart-home, IoT, or connected-device app.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
