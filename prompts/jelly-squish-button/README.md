---
title: "Jelly Squish Button"
slug: jelly-squish-button
tags: ["animation", "ui component", "button"]
copyCount: 368
tryCount: 2377
source: https://superdesign.dev/library/jelly-squish-button
---

# Jelly Squish Button

A high-fidelity interactive 3D jelly simulation that responds to vertical dragging and mouse movement. Uses GSAP for physics-based animation and optimized image sequencing. Perfect for playful hero sections or interactive showcases.

Source: https://codepen.io/cerpow/pen/LEZYxqM

![Jelly Squish Button](./preview.mp4)

## Prompt

```text
You are given a task to integrate an existing React component in the codebase

~~~/README.md
# JellySqueeze Component

A high-fidelity interactive 3D jelly simulation that responds to vertical dragging and mouse movement. Uses GSAP for physics-based animation and optimized image sequencing.

## Features

- **Physics-based Interaction**: Drag the jelly vertically to see it squeeze and bounce back with realistic inertia.
- **Image Sequence Animation**: Uses a sequence of 215 high-quality images to create a 3D effect without WebGL.
- **Mouse Follow Mode**: Optional mode where the jelly squeeze follows the mouse cursor position.
- **Responsive**: Automatically adjusts to canvas size and device pixel ratio.
- **Loading State**: Built-in loader while preloading the image sequence.

## Usage

```tsx
import { JellySqueeze } from '@/sd-components/781928a0-2180-4e75-bf1c-17eac7236428';

function MyPage() {
  return (
    <div className="h-screen w-full">
      <JellySqueeze 
        title="Squeeze Me!" 
        showControls={true} 
      />
    </div>
  );
}
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `showControls` | `boolean` | `true` | Whether to show the bottom "Follow mouse" checkbox control. |
| `className` | `string` | `undefined` | Additional CSS classes for the container. |
| `title` | `string` | `"Drag vertically to squeeze"` | The text displayed above the jelly. |

## Dependencies

- `gsap`: For Draggable interaction and animation smoothing.
- `lucide-react`: For UI icons.
~~~

~~~/src/App.tsx
import React from 'react';
import { JellySqueeze } from './Component';

export default function App() {
  return (
    <div className="w-full h-screen">
      <JellySqueeze />
    </div>
  );
}
~~~

~~~/package.json
{
  "name": "jelly-squeeze",
  "description": "Interactive jelly squeeze component",
  "dependencies": {
    "gsap": "^3.12.5",
    "lucide-react": "^0.344.0",
    "clsx": "^2.1.0",
    "tailwind-merge": "^2.2.1",
    "react-router-dom": "^6.22.0"
  }
}
~~~

~~~/src/lib/utils.ts
import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
~~~

~~~/src/Component.tsx
import React, { useEffect, useRef, useState, useLayoutEffect } from "react";
import gsap from "gsap";
import { Draggable } from "gsap/Draggable";
import { Check } from "lucide-react";
import { cn } from "./lib/utils";

// Register GSAP plugin
if (typeof window !== "undefined") {
  gsap.registerPlugin(Draggable);
}

interface JellySqueezeProps {
  /**
   * Whether to show the bottom controls
   * @default true
   */
  showControls?: boolean;
  /**
   * Background color class
   * @default "bg-[#b1b3c0]"
   */
  className?: string;
  /**
   * Title text to display above the jelly
   * @default "Drag vertically to squeeze"
   */
  title?: string;
}

export function JellySqueeze({ 
  showControls = true, 
  className,
  title = "Drag vertically to squeeze" 
}: JellySqueezeProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const dragTriggerRef = useRef<HTMLDivElement>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [followMouse, setFollowMouse] = useState(false);
  const [imagesLoaded, setImagesLoaded] = useState(0);

  // Animation refs to persist across renders
  const animState = useRef({
    totalFrames: 215,
    startFrame: 70,
    images: [] as HTMLImageElement[],
    currentFrame: -1,
    dragFrame: 70, // Start at startFrame
    displayFrame: 70, // Start at startFrame
    dragSensitivity: 5.2,
    smoothing: 0.11,
    startTime: 0,
    rafId: 0,
    isMounted: false
  });

  // Preload images
  useEffect(() => {
    animState.current.isMounted = true;
    const totalFrames = animState.current.totalFrames;
    let loaded = 0;
    const images: HTMLImageElement[] = [];

    const loadImages = async () => {
      console.log(`Loading ${totalFrames} images...`);
      
      // Batch load slightly to not freeze UI but load fast
      for (let i = 0; i < totalFrames; i++) {
        if (!animState.current.isMounted) return;
        
        const img = new Image();
        img.src = `https://cerpow.github.io/cerpow-img/jelly/jelly_${i
          .toString()
          .padStart(5, "0")}.jpg`;
        
        img.onload = () => {
          loaded++;
          setImagesLoaded(prev => prev + 1);
          if (loaded === totalFrames) {
            setIsLoading(false);
          }
        };
        img.onerror = () => {
          // Handle error or skip
          loaded++; 
          setImagesLoaded(prev => prev + 1);
          if (loaded === totalFrames) setIsLoading(false);
        };
        
        images[i] = img;
      }
      
      animState.current.images = images;
    };

    loadImages();

    return () => {
      animState.current.isMounted = false;
      cancelAnimationFrame(animState.current.rafId);
    };
  }, []);

  // Initialize Canvas & GSAP
  useLayoutEffect(() => {
    if (isLoading || !canvasRef.current || !dragTriggerRef.current) return;

    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    const state = animState.current;
    
    // Initial GSAP setup
    gsap.set(canvas, { y: state.startFrame / state.dragSensitivity });

    // Helper to clamp frame
    const resetWithinBounds = (frame: number) => {
      return Math.max(0, Math.min(state.totalFrames - 1, Math.floor(frame)));
    };

    // Canvas sizing
    const setCanvasSize = () => {
      if (!canvas) return;
      const ratio = window.devicePixelRatio || 1;
      const width = canvas.clientWidth;
      const height = width * (3 / 4); // Force 4:3
      
      canvas.width = width * ratio;
      canvas.height = height * ratio;
      canvas.style.height = `${height}px`;
      
      if (ctx) {
        ctx.scale(ratio, ratio);
        ctx.imageSmoothingEnabled = true;
        ctx.imageSmoothingQuality = "medium";
      }
      
      state.currentFrame = -1; // Force redraw
    };

    setCanvasSize();
    window.addEventListener("resize", setCanvasSize);

    // Draggable setup
    const draggable = Draggable.create(canvas, {
      trigger: dragTriggerRef.current,
      type: "y",
      inertia: true,
      bounds: { minY: 0, maxY: (state.totalFrames - 1) / state.dragSensitivity },
      allowNativeTouchScrolling: false, // Changed to false for better mobile control
      dragResistance: 0.5, // Averaged from original code
      edgeResistance: 1,
      minDuration: 0.4,
      onDrag: function() {
        state.dragFrame = this.y * state.dragSensitivity;
      },
      onThrowUpdate: function() {
        state.dragFrame = this.y * state.dragSensitivity;
      }
    })[0];

    // Animation Loop
    state.startTime = Date.now();
    const animate = () => {
      if (!state.isMounted) return;
      
      const now = Date.now();
      const dt = (now - state.startTime) / 1000;
      state.startTime = now;

      // Dampening logic from original
      const dampening = 1.0 - Math.exp(-state.smoothing * 60 * dt);
      state.displayFrame += (state.dragFrame - state.displayFrame) * dampening;

      const newFrame = resetWithinBounds(state.displayFrame);

      if (newFrame !== state.currentFrame && state.images[newFrame]?.complete && ctx) {
        ctx.clearRect(0, 0, canvas.clientWidth, canvas.clientHeight);
        ctx.drawImage(
          state.images[newFrame],
          0,
          0,
          canvas.clientWidth,
          canvas.clientHeight
        );
        state.currentFrame = newFrame;
      }

      state.rafId = requestAnimationFrame(animate);
    };

    // Start animation
    animate();

    // Mouse move handler for "Follow Mouse" mode
    const handleMouseMove = (e: MouseEvent) => {
      if (followMouse) {
        const normalizedY = e.clientY / window.innerHeight;
        state.dragFrame = normalizedY * (state.totalFrames - 1);
      }
    };
    
    if (followMouse) {
      window.addEventListener("mousemove", handleMouseMove);
    }

    // Toggle Draggable based on followMouse
    if (followMouse) {
      draggable.disable();
    } else {
      draggable.enable();
      // Sync draggable to current frame when re-enabling
      gsap.set(canvas, { y: state.displayFrame / state.dragSensitivity });
      draggable.update();
    }

    return () => {
      window.removeEventListener("resize", setCanvasSize);
      window.removeEventListener("mousemove", handleMouseMove);
      cancelAnimationFrame(state.rafId);
      draggable.kill();
    };
  }, [isLoading, followMouse]);

  // Styling helpers
  const progressPercentage = Math.round((imagesLoaded / animState.current.totalFrames) * 100);

  return (
    <div 
      ref={containerRef}
      className={cn(
        "relative flex flex-col items-center justify-center w-full min-h-screen overflow-hidden select-none",
        "bg-[#b1b3c0] text-[#464e60]", // Default theme from original
        className
      )}
    >
      {/* Header */}
      <div className="absolute top-[10%] z-20 text-center pointer-events-none transition-opacity duration-700"
           style={{ opacity: isLoading ? 0 : 1 }}>
        <h1 className="text-[17px] font-medium tracking-tight">
          {title}
        </h1>
      </div>

      {/* Canvas Container */}
      <div className="relative w-full max-w-[640px] min-w-[380px] aspect-[4/3] z-10">
        <canvas
          ref={canvasRef}
          className={cn(
            "w-full h-full rounded-[clamp(22px,6vw,42px)] transition-opacity duration-1000 ease-out",
            isLoading ? "opacity-0 scale-90" : "opacity-100 scale-100"
          )}
          style={{ transform: "scale3d(1, 1, 1)" }} // Start scale
        />
        
        {/* Invisible Drag Trigger */}
        <div 
          ref={dragTriggerRef}
          className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-[49%] w-[56%] h-[52%] rounded-full cursor-grab active:cursor-grabbing z-20"
          aria-label="Drag to squeeze"
        />
      </div>

      {/* Loading State */}
      <div 
        className={cn(
          "absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[90%] max-w-[150px] h-[2px] bg-white/20 transition-all duration-500",
          !isLoading && "opacity-0 invisible"
        )}
      >
        <div className="h-full bg-white animate-loader w-1/4" />
      </div>

      {/* Bottom Controls */}
      {showControls && (
        <div 
          className={cn(
            "absolute bottom-8 w-full flex justify-center gap-4 z-20 transition-opacity duration-1000 delay-300",
            isLoading ? "opacity-0" : "opacity-100"
          )}
        >
          <div className="flex items-center gap-2">
            <label className="flex items-center gap-2 cursor-pointer text-[17px] font-medium group">
              <input 
                type="checkbox" 
                className="peer sr-only"
                checked={followMouse}
                onChange={(e) => setFollowMouse(e.target.checked)}
              />
              <div className="w-5 h-5 border-[1.5px] border-[#464e60] rounded flex items-center justify-center transition-colors peer-checked:bg-[#464e60]">
                <Check className="w-3.5 h-3.5 text-white opacity-0 peer-checked:opacity-100" strokeWidth={3} />
              </div>
              <span>Follow mouse</span>
            </label>
          </div>
        </div>
      )}

      {/* Inline Styles for Custom Loader Animation if needed, using Tailwind animate-loader instead
          We need to add custom animation to tailwind config or use style tag
      */}
      <style>{`
        @keyframes loader {
          0% { opacity: 0; transform: translateX(0%); }
          50% { opacity: 1; }
          100% { opacity: 0; transform: translateX(300%); }
        }
        .animate-loader {
          animation: loader 1.3s infinite alternate ease-in-out;
        }
      `}</style>
    </div>
  );
}

// Helper for clsx/tailwind-merge
// You might need to create this file or just inline it if strict no-new-files rule
// But I'll assume standard utils exist or I should create them. 
// Actually, standard is usually just use clsx/twMerge inline if I can't create utils.
// I'll assume I can import from @/lib/utils if it exists, but since project is empty, I'll inline a simple version or just standard class strings if simpler.
// Wait, I am writing Component.tsx, I should use the one from imports or define it. 
// I'll remove the import and inline `cn` for safety as it is a new project.
~~~

Implementation Guidelines

1. Analyze the component structure, styling, animation implementations
2. Review the component's arguments and state
3. Think through what is the best place to adopt this component/style into the design we are doing
4. Then adopt the component/design to our current system

Help me integrate this into my design
```

**▶ Try it live → [https://superdesign.dev/library/jelly-squish-button](https://superdesign.dev/library/jelly-squish-button)**

*368 copies · 2,377 tries · tags: animation, ui component, button*
