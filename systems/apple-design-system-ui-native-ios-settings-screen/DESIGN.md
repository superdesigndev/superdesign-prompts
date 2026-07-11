# Design System — Apple Design System UI: Native iOS Settings Screen

> Category: Mobile Apps  ·  Industry: General
> Auto-scaffolded from prompt [`apple-design-system-ui-native-ios-settings-screen`](../../prompts/apple-design-system-ui-native-ios-settings-screen/). Fields marked
> `REVIEW` were best-effort extracted and should be verified.

## 1. Visual Theme & Atmosphere

Clean, flat, precise Apple system UI in the light appearance — this is the iOS design language, not a stylized theme. Uses the exact iOS system color tokens: systemBackground #FFFFFF for cells, grouped background #F2F2F7 for the page, label #000000, secondaryLabel #3C3C43 at 60%, hairline separator #C6C6C8, and the accent hues systemBlue #007AFF, systemGreen #34C759, systemRed #FF3B30, systemOrange #FF9500, systemIndigo #5856D6, systemPink #FF2D55 for the icon tiles. Typography is the SF Pro system stack (-apple-system, 'SF Pro Text', 'SF Pro Display', system-ui) on a HIG type ramp: Large Title 34/700, cell label 17/400, value/secondary 13-17 in gray, profile name 20/600. Structure comes from the inset grouped list: white rounded-10 groups on the gray page, 16px page margins, ~44px rows, hairline separators inset to start after the icon tile. Real native controls: 51x31 pill toggles (gray track off, green track on, white knob with a soft shadow) and thin #C7C7CC disclosure chevrons. Zero AI-slop tells: no purple/indigo page gradient, no centered-everything, no emoji, no lorem, no heavy drop shadows; the only gradient is the small avatar fill. Generous 8pt spacing grid.

## 2. Color Palette & Roles

Colors used in this style (the prompt has their exact roles):

- `#FFFFFF`
- `#F2F2F7`
- `#000000`
- `#3C3C43`
- `#C6C6C8`
- `#007AFF`
- `#34C759`
- `#FF3B30`
- `#FF9500`
- `#5856D6`
- `#FF2D55`
- `#C7C7CC`

## 3. Typography

- `SF Pro Text`
- `SF Pro Display`
- `Settings`
- `HomeNet`
- `Dark`

## 4. Spacing, Radius & Effects

_REVIEW — extracted from the source style prompt:_

Design a native iOS 17 mobile screen in a 390px-wide column using the Apple design system (Human Interface Guidelines) in the light appearance. Use the SF Pro system font stack (-apple-system, 'SF Pro Text', 'SF Pro Display', system-ui). Page background is the grouped background #F2F2F7; cells are white #FFFFFF inside rounded-10 inset groups with 16px page margins. Text: label #000000, secondaryLabel #3C3C43 at 60%. Type ramp: Large Title 34px/700 left-aligned, cell labels 17px/400, secondary 13-15px. Build the inset grouped list as the hero pattern: ~44px rows, hairline #C6C6C8 separators inset to START AFTER a leading 29x29 rounded-7 colored icon tile that holds a white SF-Symbol-style glyph. Use the exact iOS system accent colors for the tiles (systemBlue #007AFF, green #34C759, red #FF3B30, orange #FF9500, indigo #5856D6, pink #FF2D55). Add real native controls: 51x31 pill toggles (g …

## 5. Layout

A single vertical mobile scroll at 390px: (1) status bar, (2) Large Title 'Settings' + rounded search field, (3) inset profile card, (4) connectivity group (Airplane Mode toggle, Wi-Fi/Bluetooth/Cellular), (5) system group (Notifications, Sounds & Haptics, Focus, Screen Time), (6) general group (General, Display & Brightness, Privacy & Security, Battery) + a gray footer note, (7) a standalone Low Power Mode toggle row, (8) home-indicator pill. Everything is fully visible in one screenshot; nothing is behind a fixed element.

## 6. Components

- **Inset grouped list** — The hero pattern of the Apple design system on iOS.
- **Colored icon tile** — The iconic iOS Settings category glyph tile.
- **Native pill toggle** — The iOS switch control.
- **Disclosure row (value + chevron)** — A tappable row that drills into a subscreen.
- **Profile card cell** — The account header row unique to iOS Settings.
- **Large Title + search field** — The iOS navigation header in its expanded state.

## 7. Motion

_REVIEW: none captured._

## 8. Voice & Brand

A native iOS 17 Settings screen built to the Apple design system (Human Interface Guidelines). It opens on a large 34px bold "Settings" title, a rounded system-gray search field, and an inset profile card (circular gradient avatar with initials, name, "Apple Account, iCloud, and more" subtitle, disclosure chevron). Below are three inset grouped lists on a #F2F2F7 background: connectivity (Airplane Mode with a pill toggle, Wi-Fi "HomeNet", Bluetooth "On", Cellular), system (Notifications, Sounds & Haptics, Focus, Screen Time), and general (General, Display & Brightness "Dark", Privacy & Security, Battery). Each category row carries a 29px rounded-square colored icon tile with a white SF-Symbol-style glyph, a 17px label, and either a native toggle, a gray value detail, or a thin disclosure chevron; separators are hairlines inset after the tile. Uses the exact iOS system colors (systemBlue #007AFF, green #34C759, red #FF3B30, orange #FF9500, indigo #5856D6, pink #FF2D55) and the SF Pro system font. Reusable for any iOS settings, account, or preferences screen.

## 9. Anti-patterns

_REVIEW: none captured._

---
*Recombine this system with any [page-type](../../page-types/) to generate a new artifact in this style.*
