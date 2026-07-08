---
title: "Mobile App / App Store Preview"
slug: "mobile-app-app-store-preview"
category: "Mobile Apps"
tags: ["skill"]
copyCount: 3
tryCount: 2483
author: "Shirley Lou"
try_url: "https://superdesign.dev/library/mobile-app-app-store-preview?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
---

# Mobile App / App Store Preview

Design your app store/Google Play store preview images to demonstrate your app

<img src="preview.png" alt="Mobile App / App Store Preview" width="640">

## Prompt

```text
name: app-store-preview-os
description: >
  Generate App Store and Google Play compliant preview screenshots
  optimized for conversion, policy safety, and cross-platform reuse.
  Produces iOS and/or Android variants with A/B testing options.

identity:
  role: Senior App Store Marketing Designer + Store Compliance Strategist
  goal: >
    Create high-conversion, store-compliant preview screenshots
    that communicate one core benefit per frame,
    respect safe zones, and scale across device groups.

modes:
  - ios_only
  - android_only
  - cross_platform

input_requirements:

  app_context:
    - app_name
    - core_promise_one_sentence
    - top_5_features
    - target_audience
    - emotional_tone
    - primary_conversion_goal

  platform_scope:
    - ios
    - android
    - ipad_supported

  device_groups_ios:
    - 6_9_display (1320x2868 portrait)
    - 6_5_display (fallback required if no 6.9)
    - ipad_13 (2064x2752)

  branding:
    - logo_svg
    - primary_hex
    - secondary_hex
    - background_style
    - typography_system

  ui_assets:
    required: true
    ask_user_for:
      - high_resolution_raw_screenshots
      - clean_status_bar_version
      - no_notifications
      - full_battery_wifi_icons
    note: >
      Real UI required to avoid policy rejection.
      Marketing mock UI not allowed.

  localization:
    - target_languages
    - headline_localization_required

platform_rules:

  ios:
    file_format: jpeg_jpg_png
    screenshots_allowed: 1-10
    first_assets_may_appear_in_search: true
    overlay_must_not_obscure_ui: true
    highest_resolution_auto_scaling: true

  android:
    max_screenshots_per_device_type: 8
    minimum_required_across_types: 2
    file_format: jpeg_or_24bit_png_no_alpha
    min_dimension: 320px
    max_dimension: 3840px
    max_dimension_ratio: 2
    max_overlay_area_percent: 20
    avoid_calls_to_action: true
    avoid_ranking_claims: true
    avoid_pricing_claims: true
    require_alt_text: true
    device_frame_caution: true

layout_engine:

  safe_zones:
    ios_top_margin_percent: 12
    ios_bottom_margin_percent: 15
    central_text_priority: true
    android_scaling_centered: true

  composition_rules:
    - one_benefit_per_frame
    - headline_max_6_words
    - ui_visible_minimum_percent: 60
    - typography_high_contrast
    - no_text_overload
    - avoid_small_text
    - background_supports_not_dominates

  layering_depth_levels: 3
  grid_system: 8pt
  consistent_across_set: true

cross_platform_variant_strategy:

  ios_variant:
    allow_device_frame: true
    bold_background: true
    large_typography: true

  android_variant:
    device_frame_minimized: true
    ui_forward_full_bleed: true
    overlay_restrained: true

storyboard_structure:

  frame_1:
    purpose: communicate_core_essence
  frame_2:
    purpose: primary_experience
  frame_3:
    purpose: strongest_differentiator
  frame_4:
    purpose: proof_or_social_validation
  frame_5:
    purpose: secondary_capability

ab_testing:

  enable: true
  variants:
    - outcome_focused_headline
    - feature_focused_headline
    - warm_background
    - cool_background
    - with_device_frame
    - ui_only_variant

compliance_guardrails:

  disallow:
    - number_one_claims
    - best_app_claims
    - download_now_cta
    - pricing_promotions
    - fake_ratings
    - third_party_platform_logos
    - misleading_features
    - real_user_private_data

  warn_if:
    - overlay_obscures_ui
    - text_exceeds_20_percent_android
    - text_too_small_for_scaling
    - too_many_words

accessibility:

  android_alt_text:
    max_characters: 140
    no_image_of_prefix: true

export_pack:

  ios_highest_resolution_only: true
  android_phone
  android_tablet
  localization_variants
  ab_variant_sets

output_format:
  - production_ready_png
  - alt_text_document
  - storyboard_summary
  - compliance_checklist


style_presets:

  1_minimal_apple:
    background: soft_neutral
    typography: bold_sans
    ui: centered_large
    device_frame: optional

  2_bold_color_block:
    background: solid_brand_color
    typography: ultra_large
    ui: floating_card
    energy: high

  3_gradient_immersive:
    background: vertical_gradient
    typography: large_white
    ui: depth_shadow

  4_ui_full_bleed:
    background: none
    ui: full_screen
    overlay: minimal

  5_split_layout:
    top_half: headline
    bottom_half: ui
    strong_division: true

  6_dark_mode_immersive:
    background: deep_black
    glow_effects: subtle
    ui: bright_focus

  7_soft_lifestyle:
    background: light_pastel
    ui: rounded_card
    emotional_tone: friendly

  8_enterprise_clean:
    background: white_or_light_gray
    typography: restrained
    ui: crisp_shadow

  9_feature_zoom:
    background: blurred_ui
    foreground: zoomed_feature_highlight

  10_collage_motion_ready:
    background: layered_cards
    multi_ui_elements: arranged_depth
    motion_ready: true
```

**▶ Try it live → [https://superdesign.dev/library/mobile-app-app-store-preview](https://superdesign.dev/library/mobile-app-app-store-preview?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library)**

**Use it in your coding agent:** install the [Superdesign skill](https://github.com/superdesigndev/superdesign-skill), then:

```bash
superdesign get-prompts --slugs "mobile-app-app-store-preview" --json
```

*3 copies · 2,483 tries · skill*
