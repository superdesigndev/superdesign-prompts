---
title: "Masonry Gallery"
slug: "masonry-gallery"
category: "Components"
tags: ["ui component", "animation"]
copyCount: 306
tryCount: 2004
author: "Superdesign"
try_url: "https://superdesign.dev/library/masonry-gallery?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
---

# Masonry Gallery

A high-performance, GSAP-powered Masonry layout component with fluid animations, entrance effects (blur-to-focus, directional stagger), and interactive hover states. Supports responsive column counts and lazy-loading pre-checks.

<img src="preview.mp4" alt="Masonry Gallery" width="640">

## Prompt

```text
You are given a task to integrate an existing React component in the codebase

~~~/README.md
# MasonryGallery

A high-performance, GSAP-powered Masonry layout component designed for cinematic entrances and fluid interactions.

## Dependencies
- react: ^18.2.0
- gsap: ^3.12.5
- lucide-react: ^0.344.0
- clsx: ^2.1.0
- tailwind-merge: ^2.2.1

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `items` | `MasonryItem[]` | Required | Array of items with `id`, `img`, `height`, and optional `url`/`title`. |
| `ease` | `string` | `'power3.out'` | GSAP easing function for animations. |
| `duration` | `number` | `0.6` | Duration of layout update animations. |
| `stagger` | `number` | `0.05` | Delay between consecutive item entry animations. |
| `animateFrom` | `'bottom' \| 'top' \| 'left' \| 'right' \| 'center' \| 'random'` | `'bottom'` | Initial entrance direction. |
| `scaleOnHover` | `boolean` | `true` | Whether to scale items on mouse enter. |
| `hoverScale` | `number` | `0.95` | Scale value applied on hover. |
| `blurToFocus` | `boolean` | `true` | Cinematic blur-to-sharp transition on entrance. |
| `colorShiftOnHover` | `boolean` | `false` | Apply a gradient overlay on hover. |
| `className` | `string` | `undefined` | Container CSS classes. |

## Usage

```tsx
import { MasonryGallery } from '@/sd-components/c249f88a-7efa-478f-8560-cbb667c81f39';

const items = [
  { id: '1', img: 'https://...', height: 400, title: 'Project One' },
  { id: '2', img: 'https://...', height: 250, title: 'Project Two' },
];

export default function GalleryDemo() {
  return (
    <MasonryGallery 
      items={items}
      animateFrom="bottom"
      blurToFocus={true}
      stagger={0.1}
    />
  );
}
```
~~~

~~~/src/App.tsx
import React, { useState } from 'react';
import MasonryGallery, { MasonryItem } from './Component';
import { RefreshCw } from 'lucide-react';

const INITIAL_ITEMS: MasonryItem[] = [
  { id: '1', img: 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&q=80&w=600', height: 400, title: 'Mountain Lake' },
  { id: '2', img: 'https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&q=80&w=600', height: 250, title: 'Alpine Meadow' },
  { id: '3', img: 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&q=80&w=600', height: 600, title: 'Forest Trail' },
  { id: '4', img: 'https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&q=80&w=600', height: 350, title: 'Coastal Cliffs' },
  { id: '5', img: 'https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&q=80&w=600', height: 500, title: 'Desert Dunes' },
  { id: '6', img: 'https://images.unsplash.com/photo-1500673922987-e212871fec22?auto=format&fit=crop&q=80&w=600', height: 300, title: 'Northern Lights' },
  { id: '7', img: 'https://images.unsplash.com/photo-1426604966848-d7adac402bdb?auto=format&fit=crop&q=80&w=600', height: 450, title: 'Rocky Falls' },
  { id: '8', img: 'https://images.unsplash.com/photo-1472214103451-9374bd1c798e?auto=format&fit=crop&q=80&w=600', height: 280, title: 'Green Hills' },
  { id: '9', img: 'https://images.unsplash.com/photo-1518098268026-4e89f1a2cd8e?auto=format&fit=crop&q=80&w=600', height: 550, title: 'Sunrise Peak' },
  { id: '10', img: 'https://images.unsplash.com/photo-1493246507139-91e8bef99c02?auto=format&fit=crop&q=80&w=600', height: 320, title: 'Sunset Valley' },
];

export default function App() {
  const [items, setItems] = useState(INITIAL_ITEMS);
  const [key, setKey] = useState(0);

  const handleRefresh = () => {
    // Shuffle and trigger re-mount for animation demo
    const shuffled = [...INITIAL_ITEMS].sort(() => Math.random() - 0.5);
    setItems(shuffled);
    setKey(prev => prev + 1);
  };

  return (
    <main className="min-h-screen bg-background p-20 flex flex-col items-center">
      <div className="w-full max-w-7xl relative">
        <h1 className="text-foreground text-3xl font-medium tracking-tight mb-12 text-center">
          Masonry Gallery
        </h1>
        
        <MasonryGallery 
          key={key}
          items={items}
          animateFrom="bottom"
          blurToFocus={true}
          stagger={0.08}
          scaleOnHover={true}
          hoverScale={0.96}
          colorShiftOnHover={true}
        />

        <button
          onClick={handleRefresh}
          className="fixed bottom-10 right-10 z-50 p-4 bg-primary text-primary-foreground rounded-full shadow-2xl hover:scale-110 active:scale-95 transition-all group"
          title="Re-animate Gallery"
        >
          <RefreshCw className="w-6 h-6 group-hover:rotate-180 transition-transform duration-500" />
        </button>
      </div>
    </main>
  );
}
~~~

~~~/package.json
{
  "name": "masonry-gallery",
  "description": "A high-performance GSAP-powered Masonry gallery component",
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "gsap": "^3.12.5",
    "lucide-react": "^0.344.0",
    "clsx": "^2.1.0",
    "tailwind-merge": "^2.2.1"
  }
}
~~~

~~~/src/Component.tsx
/**
 * MasonryGallery - A high-performance, GSAP-powered Masonry layout component.
 * Features:
 * - Responsive column mapping
 * - GSAP animations for entry and updates
 * - Blur-to-focus and directional entrance effects
 * - Interactive hover states (scale, color shift)
 * - Automatic image preloading for smooth layout calculations
 */

import React, { useEffect, useLayoutEffect, useMemo, useRef, useState } from 'react';
import { gsap } from 'gsap';
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

/** Utility for Tailwind class merging */
function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

/** Hook to handle media queries for responsive columns */
const useMedia = (queries: string[], values: number[], defaultValue: number): number => {
  const get = () => {
    if (typeof window === 'undefined') return defaultValue;
    const match = queries.findIndex(q => window.matchMedia(q).matches);
    return values[match] !== undefined ? values[match] : defaultValue;
  };

  const [value, setValue] = useState<number>(get);

  useEffect(() => {
    const handler = () => setValue(get);
    queries.forEach(q => window.matchMedia(q).addEventListener('change', handler));
    return () => queries.forEach(q => window.matchMedia(q).removeEventListener('change', handler));
  }, [queries]);

  return value;
};

/** Hook to measure element size via ResizeObserver */
const useMeasure = <T extends HTMLElement>() => {
  const ref = useRef<T | null>(null);
  const [size, setSize] = useState({ width: 0, height: 0 });

  useLayoutEffect(() => {
    if (!ref.current) return;
    const ro = new ResizeObserver(([entry]) => {
      const { width, height } = entry.contentRect;
      setSize({ width, height });
    });
    ro.observe(ref.current);
    return () => ro.disconnect();
  }, []);

  return [ref, size] as const;
};

/** Utility to ensure images are loaded before layout/animation */
const preloadImages = async (urls: string[]): Promise<void> => {
  await Promise.all(
    urls.map(
      src =>
        new Promise<void>(resolve => {
          const img = new Image();
          img.src = src;
          img.onload = img.onerror = () => resolve();
        })
    )
  );
};

export interface MasonryItem {
  id: string;
  img: string;
  url?: string;
  height: number;
  title?: string;
}

interface GridItem extends MasonryItem {
  x: number;
  y: number;
  w: number;
  h: number;
}

export interface MasonryGalleryProps {
  /** Array of items to display in the gallery */
  items: MasonryItem[];
  /** GSAP easing function */
  ease?: string;
  /** Duration of movement animations */
  duration?: number;
  /** Stagger delay between item animations */
  stagger?: number;
  /** Direction from which items enter the screen */
  animateFrom?: 'bottom' | 'top' | 'left' | 'right' | 'center' | 'random';
  /** Whether to scale items down on hover */
  scaleOnHover?: boolean;
  /** Scale factor for hover state */
  hoverScale?: number;
  /** Whether to apply a blur-to-focus entry effect */
  blurToFocus?: boolean;
  /** Whether to show a color overlay on hover */
  colorShiftOnHover?: boolean;
  /** CSS class for the container */
  className?: string;
  /** CSS class for individual item containers */
  itemClassName?: string;
}

export const MasonryGallery: React.FC<MasonryGalleryProps> = ({
  items,
  ease = 'power3.out',
  duration = 0.6,
  stagger = 0.05,
  animateFrom = 'bottom',
  scaleOnHover = true,
  hoverScale = 0.95,
  blurToFocus = true,
  colorShiftOnHover = false,
  className,
  itemClassName
}) => {
  const columns = useMedia(
    ['(min-width: 1500px)', '(min-width: 1000px)', '(min-width: 600px)', '(min-width: 400px)'],
    [5, 4, 3, 2],
    1
  );

  const [containerRef, { width }] = useMeasure<HTMLDivElement>();
  const [imagesReady, setImagesReady] = useState(false);
  const hasMounted = useRef(false);

  // Initial animation calculations
  const getInitialPosition = (item: GridItem) => {
    const containerRect = containerRef.current?.getBoundingClientRect();
    if (!containerRect) return { x: item.x, y: item.y };

    let direction = animateFrom;
    if (animateFrom === 'random') {
      const dirs = ['top', 'bottom', 'left', 'right'];
      direction = dirs[Math.floor(Math.random() * dirs.length)] as any;
    }

    switch (direction) {
      case 'top': return { x: item.x, y: -200 };
      case 'bottom': return { x: item.x, y: window.innerHeight + 200 };
      case 'left': return { x: -200, y: item.y };
      case 'right': return { x: window.innerWidth + 200, y: item.y };
      case 'center': return {
        x: containerRect.width / 2 - item.w / 2,
        y: containerRect.height / 2 - item.h / 2
      };
      default: return { x: item.x, y: item.y + 100 };
    }
  };

  // Preload logic
  useEffect(() => {
    preloadImages(items.map(i => i.img)).then(() => setImagesReady(true));
  }, [items]);

  // Layout calculation
  const { grid, containerHeight } = useMemo(() => {
    if (!width) return { grid: [] as GridItem[], containerHeight: 0 };

    const colHeights = new Array(columns).fill(0);
    const gap = 24; // Increased gap for premium feel
    const totalGaps = (columns - 1) * gap;
    const columnWidth = (width - totalGaps) / columns;

    const gridItems = items.map(child => {
      const col = colHeights.indexOf(Math.min(...colHeights));
      const x = col * (columnWidth + gap);
      const height = (child.height / 400) * columnWidth; // Maintain aspect ratio roughly
      const y = colHeights[col];
      colHeights[col] += height + gap;
      return { ...child, x, y, w: columnWidth, h: height };
    });

    return { grid: gridItems, containerHeight: Math.max(...colHeights) };
  }, [columns, items, width]);

  // Animation logic
  useLayoutEffect(() => {
    if (!imagesReady || !grid.length) return;

    grid.forEach((item, index) => {
      const element = document.querySelector(`[data-key="${item.id}"]`);
      if (!element) return;

      const animProps = { x: item.x, y: item.y, width: item.w, height: item.h };

      if (!hasMounted.current) {
        const start = getInitialPosition(item);
        gsap.fromTo(
          element,
          {
            opacity: 0,
            x: start.x,
            y: start.y,
            width: item.w,
            height: item.h,
            ...(blurToFocus && { filter: 'blur(20px)' })
          },
          {
            opacity: 1,
            ...animProps,
            ...(blurToFocus && { filter: 'blur(0px)' }),
            duration: 1.2,
            ease: 'power3.out',
            delay: index * stagger
          }
        );
      } else {
        gsap.to(element, {
          ...animProps,
          duration,
          ease,
          overwrite: 'auto'
        });
      }
    });

    if (grid.length > 0) hasMounted.current = true;
  }, [grid, imagesReady, stagger, animateFrom, blurToFocus, duration, ease]);

  const handleMouseEnter = (id: string, element: HTMLElement) => {
    if (scaleOnHover) {
      gsap.to(element, {
        scale: hoverScale,
        duration: 0.4,
        ease: 'power2.out'
      });
    }
    if (colorShiftOnHover) {
      const overlay = element.querySelector('.color-overlay');
      if (overlay) gsap.to(overlay, { opacity: 0.3, duration: 0.4 });
    }
  };

  const handleMouseLeave = (id: string, element: HTMLElement) => {
    if (scaleOnHover) {
      gsap.to(element, {
        scale: 1,
        duration: 0.4,
        ease: 'power2.out'
      });
    }
    if (colorShiftOnHover) {
      const overlay = element.querySelector('.color-overlay');
      if (overlay) gsap.to(overlay, { opacity: 0, duration: 0.4 });
    }
  };

  return (
    <div
      ref={containerRef}
      className={cn('relative w-full', className)}
      style={{ height: containerHeight, minHeight: '400px' }}
    >
      {grid.map(item => (
        <div
          key={item.id}
          data-key={item.id}
          className={cn(
            'absolute overflow-hidden cursor-pointer rounded-xl transition-shadow hover:shadow-2xl',
            itemClassName
          )}
          style={{
            willChange: 'transform, width, height, opacity, filter',
            boxShadow: '0 10px 30px -10px rgba(0,0,0,0.1)'
          }}
          onClick={() => item.url && window.open(item.url, '_blank', 'noopener')}
          onMouseEnter={e => handleMouseEnter(item.id, e.currentTarget)}
          onMouseLeave={e => handleMouseLeave(item.id, e.currentTarget)}
        >
          <div
            className="w-full h-full bg-cover bg-center bg-no-repeat"
            style={{ backgroundImage: `url(${item.img})` }}
          >
            {colorShiftOnHover && (
              <div className="color-overlay absolute inset-0 bg-gradient-to-tr from-primary/40 to-accent/40 opacity-0 pointer-events-none transition-opacity" />
            )}
          </div>
          {item.title && (
            <div className="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/60 to-transparent opacity-0 hover:opacity-100 transition-opacity duration-300">
              <p className="text-white text-xs font-medium uppercase tracking-wider">{item.title}</p>
            </div>
          )}
        </div>
      ))}
    </div>
  );
};

export default MasonryGallery;
~~~

Implementation Guidelines

1. Analyze the component structure, styling, animation implementations
2. Review the component's arguments and state
3. Think through what is the best place to adopt this component/style into the design we are doing
4. Then adopt the component/design to our current system

Help me integrate this into my design
```

**▶ Try it live → [https://superdesign.dev/library/masonry-gallery](https://superdesign.dev/library/masonry-gallery?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library)**

**Use it in your coding agent:** install the [Superdesign skill](https://github.com/superdesigndev/superdesign-skill), then:

```bash
superdesign get-prompts --slugs "masonry-gallery" --json
```

*306 copies · 2,004 tries · ui component, animation*
