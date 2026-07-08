---
title: "Animated List"
slug: "animated-list"
category: "Components"
tags: ["ui component"]
copyCount: 63
tryCount: 2491
author: "Superdesign"
try_url: "https://superdesign.dev/library/animated-list?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
---

# Animated List

A vertical list component with scroll-triggered animations, keyboard navigation, and gradient overflow effects. Features item scaling on scroll and hover.

<img src="preview.mp4" alt="Animated List" width="640">

## Prompt

```text
You are given a task to integrate an existing React component in the codebase

~~~/README.md
# Animated List

A vertical list component with scroll-triggered animations, keyboard navigation, and gradient overflow effects. Features item scaling on scroll and hover.

## Features

- **Scroll Animation**: Items scale up when they enter the viewport and scale down when they exit.
- **Keyboard Navigation**: Use Arrow Up/Down to navigate items, Enter to select.
- **Gradient Overlays**: Fade-out gradients at top and bottom that react to scroll position.
- **Auto-scrolling**: Automatically scrolls to keep the selected item in view during keyboard navigation.

## Usage

```tsx
import { AnimatedList } from '@/sd-components/62fdfafb-13f8-4063-8838-4b0cd1c98e76';

const items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5'];

function MyComponent() {
  return (
    <AnimatedList
      items={items}
      onItemSelect={(item, index) => console.log(item, index)}
      showGradients={true}
      enableArrowNavigation={true}
    />
  );
}
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `items` | `string[]` | `['Item 1'...]` | Array of strings to display in the list. |
| `onItemSelect` | `(item: string, index: number) => void` | - | Callback fired when an item is clicked or selected via Enter key. |
| `showGradients` | `boolean` | `true` | Whether to show the top/bottom fade gradients. |
| `enableArrowNavigation` | `boolean` | `true` | Whether to enable keyboard navigation (Up/Down arrows). |
| `displayScrollbar` | `boolean` | `true` | Whether to show the custom scrollbar. |
| `initialSelectedIndex` | `number` | `-1` | The index of the item selected by default. |
| `className` | `string` | `''` | Additional classes for the container. |
| `itemClassName` | `string` | `''` | Additional classes for individual items. |

## Dependencies

- `framer-motion`: For animations and scroll detection.
- `clsx`, `tailwind-merge`: For class name management.
~~~

~~~/src/App.tsx
import React, { useState } from 'react';
import { AnimatedList } from './Component';

export default function App() {
  const [lastSelected, setLastSelected] = useState<string | null>(null);

  // Generate a longer list of items for better scrolling demonstration
  const items = Array.from({ length: 20 }, (_, i) => `Interactive Item ${i + 1}`);

  return (
    <div className="min-h-screen bg-[#1A1A1B] flex flex-col items-center justify-center p-8 font-sans">
      <div className="w-full max-w-3xl flex flex-col items-center gap-12">
        <div className="text-center space-y-2">
          <h1 className="text-3xl font-medium text-white tracking-tight">Animated List</h1>
          <p className="text-white/60 text-sm max-w-md mx-auto">
            Scroll to trigger scale animations. Use Up/Down arrows to navigate.
          </p>
        </div>

        <div className="relative group">
          {/* Decorative subtle shadow/glow container */}
          <div className="absolute -inset-4 bg-gradient-to-b from-white/5 to-transparent rounded-[32px] blur-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none" />
          
          <div className="relative bg-[#060010] rounded-2xl border border-white/5 shadow-2xl overflow-hidden">
            <AnimatedList
              items={items}
              onItemSelect={(item, index) => {
                console.log('Selected:', item, index);
                setLastSelected(item);
              }}
              showGradients={true}
              enableArrowNavigation={true}
              displayScrollbar={true}
              className="w-[400px]"
            />
          </div>
        </div>

        {lastSelected && (
          <div className="absolute bottom-8 text-white/40 text-xs font-mono animate-fade-in">
            Last selected: <span className="text-white/80">{lastSelected}</span>
          </div>
        )}
      </div>
    </div>
  );
}
~~~

~~~/package.json
{
  "name": "animated-list",
  "version": "1.0.0",
  "description": "A vertical list component with scroll-triggered animations and keyboard navigation",
  "main": "src/Component.tsx",
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "framer-motion": "^10.0.0",
    "lucide-react": "^0.263.1",
    "clsx": "^2.0.0",
    "tailwind-merge": "^2.0.0"
  }
}
~~~

~~~/src/Component.tsx
import React, { useRef, useState, useEffect, useCallback, ReactNode, MouseEventHandler, UIEvent } from 'react';
import { motion, useInView } from 'framer-motion';
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

interface AnimatedItemProps {
  children: ReactNode;
  delay?: number;
  index: number;
  onMouseEnter?: MouseEventHandler<HTMLDivElement>;
  onClick?: MouseEventHandler<HTMLDivElement>;
}

const AnimatedItem: React.FC<AnimatedItemProps> = ({ children, delay = 0, index, onMouseEnter, onClick }) => {
  const ref = useRef<HTMLDivElement>(null);
  const inView = useInView(ref, { amount: 0.5, once: false });
  
  return (
    <motion.div
      ref={ref}
      data-index={index}
      onMouseEnter={onMouseEnter}
      onClick={onClick}
      initial={{ scale: 0.7, opacity: 0 }}
      animate={inView ? { scale: 1, opacity: 1 } : { scale: 0.7, opacity: 0 }}
      transition={{ duration: 0.2, delay }}
      className="mb-4 cursor-pointer"
    >
      {children}
    </motion.div>
  );
};

export interface AnimatedListProps {
  items?: string[];
  onItemSelect?: (item: string, index: number) => void;
  showGradients?: boolean;
  enableArrowNavigation?: boolean;
  className?: string;
  itemClassName?: string;
  displayScrollbar?: boolean;
  initialSelectedIndex?: number;
}

export const AnimatedList: React.FC<AnimatedListProps> = ({
  items = [
    'Item 1',
    'Item 2',
    'Item 3',
    'Item 4',
    'Item 5',
    'Item 6',
    'Item 7',
    'Item 8',
    'Item 9',
    'Item 10',
    'Item 11',
    'Item 12',
    'Item 13',
    'Item 14',
    'Item 15'
  ],
  onItemSelect,
  showGradients = true,
  enableArrowNavigation = true,
  className = '',
  itemClassName = '',
  displayScrollbar = true,
  initialSelectedIndex = -1
}) => {
  const listRef = useRef<HTMLDivElement>(null);
  const [selectedIndex, setSelectedIndex] = useState<number>(initialSelectedIndex);
  const [keyboardNav, setKeyboardNav] = useState<boolean>(false);
  const [topGradientOpacity, setTopGradientOpacity] = useState<number>(0);
  const [bottomGradientOpacity, setBottomGradientOpacity] = useState<number>(1);

  const handleItemMouseEnter = useCallback((index: number) => {
    setSelectedIndex(index);
  }, []);

  const handleItemClick = useCallback(
    (item: string, index: number) => {
      setSelectedIndex(index);
      if (onItemSelect) {
        onItemSelect(item, index);
      }
    },
    [onItemSelect]
  );

  const handleScroll = (e: UIEvent<HTMLDivElement>) => {
    const { scrollTop, scrollHeight, clientHeight } = e.target as HTMLDivElement;
    setTopGradientOpacity(Math.min(scrollTop / 50, 1));
    const bottomDistance = scrollHeight - (scrollTop + clientHeight);
    setBottomGradientOpacity(scrollHeight <= clientHeight ? 0 : Math.min(bottomDistance / 50, 1));
  };

  useEffect(() => {
    if (!enableArrowNavigation) return;
    
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'ArrowDown' || (e.key === 'Tab' && !e.shiftKey)) {
        e.preventDefault();
        setKeyboardNav(true);
        setSelectedIndex(prev => Math.min(prev + 1, items.length - 1));
      } else if (e.key === 'ArrowUp' || (e.key === 'Tab' && e.shiftKey)) {
        e.preventDefault();
        setKeyboardNav(true);
        setSelectedIndex(prev => Math.max(prev - 1, 0));
      } else if (e.key === 'Enter') {
        if (selectedIndex >= 0 && selectedIndex < items.length) {
          e.preventDefault();
          if (onItemSelect) {
            onItemSelect(items[selectedIndex], selectedIndex);
          }
        }
      }
    };
    
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [items, selectedIndex, onItemSelect, enableArrowNavigation]);

  useEffect(() => {
    if (!keyboardNav || selectedIndex < 0 || !listRef.current) return;
    const container = listRef.current;
    // Fixed the selector syntax here
    const selectedItem = container.querySelector(`[data-index="${selectedIndex}"]`) as HTMLElement | null;
    
    if (selectedItem) {
      const extraMargin = 50;
      const containerScrollTop = container.scrollTop;
      const containerHeight = container.clientHeight;
      const itemTop = selectedItem.offsetTop;
      const itemBottom = itemTop + selectedItem.offsetHeight;

      if (itemTop < containerScrollTop + extraMargin) {
        container.scrollTo({ top: itemTop - extraMargin, behavior: 'smooth' });
      } else if (itemBottom > containerScrollTop + containerHeight - extraMargin) {
        container.scrollTo({
          top: itemBottom - containerHeight + extraMargin,
          behavior: 'smooth'
        });
      }
    }
    setKeyboardNav(false);
  }, [selectedIndex, keyboardNav]);

  return (
    <div className={cn("relative w-[500px]", className)}>
      <div
        ref={listRef}
        className={cn(
          "max-h-[400px] overflow-y-auto p-4",
          displayScrollbar
            ? "[&::-webkit-scrollbar]:w-[8px] [&::-webkit-scrollbar-track]:bg-[#060010] [&::-webkit-scrollbar-thumb]:bg-[#222] [&::-webkit-scrollbar-thumb]:rounded-[4px]"
            : "scrollbar-hide"
        )}
        onScroll={handleScroll}
        style={{
          scrollbarWidth: displayScrollbar ? 'thin' : 'none',
          scrollbarColor: '#222 #060010'
        }}
      >
        {items.map((item, index) => (
          <AnimatedItem
            key={index}
            delay={0.1}
            index={index}
            onMouseEnter={() => handleItemMouseEnter(index)}
            onClick={() => handleItemClick(item, index)}
          >
            <div 
              className={cn(
                "p-4 bg-[#111] rounded-lg transition-colors duration-200", 
                selectedIndex === index ? 'bg-[#222]' : '',
                itemClassName
              )}
            >
              <p className="text-white m-0 text-sm font-medium">{item}</p>
            </div>
          </AnimatedItem>
        ))}
      </div>
      {showGradients && (
        <>
          <div
            className="absolute top-0 left-0 right-0 h-[50px] bg-gradient-to-b from-[#060010] to-transparent pointer-events-none transition-opacity duration-300 ease"
            style={{ opacity: topGradientOpacity }}
          ></div>
          <div
            className="absolute bottom-0 left-0 right-0 h-[100px] bg-gradient-to-t from-[#060010] to-transparent pointer-events-none transition-opacity duration-300 ease"
            style={{ opacity: bottomGradientOpacity }}
          ></div>
        </>
      )}
    </div>
  );
};

export default AnimatedList;
~~~

Implementation Guidelines

1. Analyze the component structure, styling, animation implementations
2. Review the component's arguments and state
3. Think through what is the best place to adopt this component/style into the design we are doing
4. Then adopt the component/design to our current system

Help me integrate this into my design
```

**▶ Try it live → [https://superdesign.dev/library/animated-list](https://superdesign.dev/library/animated-list?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library)**

**Use it in your coding agent:** install the [Superdesign skill](https://github.com/superdesigndev/superdesign-skill), then:

```bash
superdesign get-prompts --slugs "animated-list" --json
```

*63 copies · 2,491 tries · ui component*
