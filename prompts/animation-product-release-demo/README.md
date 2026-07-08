---
title: "Animation / Product Release Demo"
slug: "animation-product-release-demo"
category: "Animations & Backgrounds"
tags: ["skill", "animation"]
copyCount: 171
tryCount: 2180
author: "Superdesign"
try_url: "https://superdesign.dev/library/animation-product-release-demo?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
---

# Animation / Product Release Demo

Use this to deliver product launch animation based on real UI

<img src="preview.mp4" alt="Animation / Product Release Demo" width="640">

## Prompt

```text
I want you to help me plan and outline a highly detailed, scene-by-scene implementation plan for a UI interaction or video animation.
---
## Step 1 Discovery Phase (MANDATORY)
Before generating the final plan, you must first act in a Discovery Phase.
If attached design draft make sure you read the current UI & design for context
Ask me 4–5 clarifying questions to understand my exact intent.
Your questions should avoid any technical aspect, we always use CSS keyframes, video triggered by automated timeline, play in loop, the style should always follow existing UI if given;
Including question to ask & confirm user journey (by proposing a few ones)
Focus your question only on non-obvious question to align with user on the scene
—

## Step 2 Animation plan
Once I answer your questions, you will output the Animation Implementation Plan with an unpinned note node using the strict structure, vocabulary, and rules below. After plan created, use askQuestion tool to collect user’s feedback on plan, proposed answer including ‘Looks good, lets build’ 
---
### 1️⃣ Scene Breakdown Structure
Break the animation down into clear, numbered scenes.
For each scene, provide:
#### Scene Name & Duration
Example:
Scene 1 — Tab Expansion (2s)
#### Initial State
What is visible, hidden, or positioned off-screen before movement starts?
#### Action & Easing
What happens, and how does it feel?
Example: Spring-animated scale up

#### Technical Implementation Details
Specific CSS properties, SVG transforms, or timeline coordinates.
---
### 2️⃣ Standardized Motion Vocabulary
Use precise motion design terminology to avoid ambiguity.
#### Camera / View
- Zoom In / Out → scale() transforms
- Pan → translateX / translateY
- Perspective Shift → rotateX / rotateY
#### Transitions
- Crossfade → opacity swapping
- Morph → border-radius or SVG path shifts
- Staggered Reveal → delayed list items
#### Physics / Easing
- Spring → overshoot and settle
- Ease-in-out → smooth acceleration/deceleration
- Linear → constant speed
#### Effects
- Shimmer → background-position animation
- Pulse → continuous subtle scaling
## Step 3 Implementation
After user confirm the plan, start creating a design draft to implement the animation with html keyframe, auto reply;

---
# Strict Rules & Anti-Patterns (CRITICAL)
LLMs frequently make spatial and performance mistakes.
You MUST adhere to the following rules:
---
## Rule 1 — Zoom in/out, transition for main elements
Zoom in/out for the core part of UI elements deliver best quality
For each scene, think about what is the epic center, and which part we should zoom in/out to create awesome effect
You can even hide some part of UI to have some transition animation when introducing new features
—
## Rule 2 — Resolve Coordinates From the Shared Origin
- Never derive an animation coordinate from a single CSS value in isolation.
- Always trace the full ancestor chain back to the animation container, summing every offset, margin, and padding along the path.
—
## Rule 3 — The “Anchored Cursor” Mandate
If a cursor interacts with an element that is zooming, moving, or scaling:
- The cursor's transform coordinates MUST be mathematically relative to the target’s new position.
- Do NOT use the original absolute DOM position.
- Pin the cursor to the target’s bounding box.
- Avoid “clicking empty air.”
---
# Example plan
~~~
[scene1] Showing the exact prompt input, but hide inspire mode option initially, zoom in 3x focus on mode switch UI
[scene2] The mode switch expand and Inspire mode pop up, with some poping animation
[scene3] A mouse showup and clicked Inspire mode, and then prompt input show a different UI & color to indicate mode change
[scene4] zoom out, and inspiration design showup at the top (just use skeleton)
~~~
—
Notes:
For Step 2 Animation plan, must be unpinned notes

Now please help me plan and generate animation for below:
```

**▶ Try it live → [https://superdesign.dev/library/animation-product-release-demo](https://superdesign.dev/library/animation-product-release-demo?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library)**

**Use it in your coding agent:** install the [Superdesign skill](https://github.com/superdesigndev/superdesign-skill), then:

```bash
superdesign get-prompts --slugs "animation-product-release-demo" --json
```

*171 copies · 2,180 tries · skill, animation*
