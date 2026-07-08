---
title: "Radiant Prompt Input"
slug: "radiant-prompt-input"
category: "Components"
industry: "General"
tags: ["ui component", "input"]
copyCount: 348
tryCount: 2289
author: "Jason Zhou"
try_url: "https://superdesign.dev/library/radiant-prompt-input?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
---

# Radiant Prompt Input

A high-fidelity, kinetic input interface featuring a mesmerizing, continuously rotating conic gradient border. Designed for next-generation AI interactions, this component elevates simple text entry into a focal point of engagement, blending futuristic aesthetics with organic fluid motion. Ideal for LLM chat interfaces, command palettes, or hero search bars that require a premium, 'magical' feel.

Source: https://codepen.io/una/pen/wBGNWmZ

<img src="preview.png" alt="Radiant Prompt Input" width="640">

## Prompt

```text
You are given a task to integrate an existing React component in the codebase

~~~/README.md
# Radiant Prompt Input

A high-fidelity, kinetic input interface featuring a mesmerizing, continuously rotating conic gradient border. Designed for next-generation AI interactions, this component elevates simple text entry into a focal point of engagement.

## Features

- **Kinetic Gradient Border**: Custom CSS `@property` animation creates a smooth, rotating multi-color gradient.
- **Backdrop Blur**: Organic glassmorphism effect that blends with any background.
- **Fluid Interactions**: Micro-interactions on hover, focus, and submission.
- **Responsive**: Adapts gracefully to mobile and desktop viewports.
- **Production Ready**: Fully typed, accessible, and theme-aware (works in Light/Dark modes).

## Usage

```tsx
import { RadiantPromptInput } from '@/sd-components/d2a7422b-1c93-41e6-a000-e313c7ad67f9';

function MyChatInterface() {
  const handleAsk = (query: string) => {
    console.log("User asked:", query);
  };

  return (
    <div className="w-full max-w-2xl mx-auto mt-20">
      <RadiantPromptInput 
        onSubmit={handleAsk}
        placeholder="Ask Gemini..."
      />
    </div>
  );
}
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `placeholder` | `string` | "Ask anything..." | Text to display when empty |
| `value` | `string` | undefined | Controlled value of the input |
| `onChange` | `(value: string) => void` | undefined | Callback when input changes |
| `onSubmit` | `(value: string) => void` | undefined | Callback when Enter is pressed or arrow clicked |
| `disabled` | `boolean` | false | Disables interactions |
| `className` | `string` | undefined | Additional CSS classes for the wrapper |

## Browser Support

Requires a browser that supports CSS `@property` (Modern Chrome, Edge, Safari, Firefox) for the rotation animation. Fallbacks gracefully to a static gradient in older browsers.
~~~

~~~/src/App.tsx
import React, { useState } from 'react';
import { RadiantPromptInput } from './Component';

export default function App() {
  const [lastSubmitted, setLastSubmitted] = useState<string | null>(null);

  const handleSubmit = (value: string) => {
    setLastSubmitted(value);
    console.log("Submitted:", value);
  };

  return (
    <div className="min-h-screen w-full flex flex-col items-center justify-center bg-background p-4 md:p-8 font-sans transition-colors duration-300">
      
      {/* Background decoration to show off the component's backdrop blur */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-0 left-1/4 w-96 h-96 bg-primary/5 rounded-full blur-[100px]" />
        <div className="absolute bottom-0 right-1/4 w-[500px] h-[500px] bg-accent/5 rounded-full blur-[120px]" />
      </div>

      <div className="relative z-10 w-full max-w-4xl flex flex-col items-center gap-12">
        
        {/* Header Text */}
        <div className="text-center space-y-4">
          <h1 className="text-4xl md:text-6xl font-bold tracking-tight text-transparent bg-clip-text bg-gradient-to-br from-foreground to-muted-foreground/50 pb-2">
            How can I help?
          </h1>
          <p className="text-muted-foreground text-lg md:text-xl font-light max-w-lg mx-auto">
            Experience the fluid interface designed for the next generation of AI.
          </p>
        </div>

        {/* The Component */}
        <div className="w-full px-4">
          <RadiantPromptInput 
            onSubmit={handleSubmit} 
            placeholder="Ask anything..."
          />
        </div>

        {/* Feedback / State Display */}
        <div className="h-12 flex items-center justify-center">
          {lastSubmitted && (
            <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
              <span className="px-4 py-2 rounded-full bg-muted/50 text-sm text-muted-foreground border border-border/50">
                You asked: <span className="text-foreground font-medium">{lastSubmitted}</span>
              </span>
            </div>
          )}
        </div>

        {/* Capabilities Grid (Visual Filler) */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 w-full max-w-3xl opacity-60">
          {[
            { icon: "✨", title: "Creative Writing", desc: "Stories, poems, scripts" },
            { icon: "💻", title: "Code Analysis", desc: "Debug, refactor, optimize" },
            { icon: "🎨", title: "Image Gen", desc: "Logos, art, diagrams" },
          ].map((item, i) => (
            <div key={i} className="p-4 rounded-xl border border-border/40 bg-card/30 hover:bg-card/50 transition-colors text-center">
              <div className="text-2xl mb-2">{item.icon}</div>
              <h3 className="font-medium text-foreground">{item.title}</h3>
              <p className="text-xs text-muted-foreground">{item.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
~~~

~~~/package.json
{
  "name": "radiant-prompt-input",
  "version": "1.0.0",
  "description": "A high-fidelity, kinetic input interface featuring a mesmerizing, continuously rotating conic gradient border.",
  "dependencies": {
    "lucide-react": "^0.300.0",
    "clsx": "^2.0.0",
    "tailwind-merge": "^2.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }
}
~~~

~~~/src/Component.tsx
import React, { useState } from 'react';
import { Plus, Mic, ArrowUp } from 'lucide-react';
import { cn } from './utils'; // We'll implement utility inline or helper
import clsx from 'clsx';
import { twMerge } from 'tailwind-merge';

function cn(...inputs: (string | undefined | null | false)[]) {
  return twMerge(clsx(inputs));
}

export interface RadiantPromptInputProps {
  placeholder?: string;
  value?: string;
  onChange?: (value: string) => void;
  onSubmit?: (value: string) => void;
  className?: string;
  disabled?: boolean;
}

export function RadiantPromptInput({
  placeholder = "Ask anything...",
  value: propValue,
  onChange: propOnChange,
  onSubmit,
  className,
  disabled
}: RadiantPromptInputProps) {
  const [internalValue, setInternalValue] = useState("");
  const isControlled = propValue !== undefined;
  const value = isControlled ? propValue : internalValue;

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!isControlled) {
      setInternalValue(e.target.value);
    }
    propOnChange?.(e.target.value);
  };

  const handleSubmit = () => {
    if (value && !disabled) {
      onSubmit?.(value);
      if (!isControlled) setInternalValue("");
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div className={cn("relative w-full max-w-2xl mx-auto", className)}>
      {/* 
        Custom CSS for the gradient animation using @property which Tailwind doesn't fully support inline yet.
        We use a unique class scope 'radiant-input-wrapper' to avoid conflicts.
      */}
      <style>{`
        @property --rotation {
          syntax: '<angle>';
          inherits: false;
          initial-value: 0deg;
        }
        
        @keyframes rotate-gradient {
          to {
            --rotation: 360deg;
          }
        }

        .radiant-input-wrapper {
          --border-size: 3px;
          --gradient: conic-gradient(
            from var(--rotation) 
            at 50% 50% in oklab, 
            oklch(0.63 0.2 251.22) 27%, 
            oklch(0.67 0.21 25.81) 33%, 
            oklch(0.9 0.19 93.93) 41%, 
            oklch(0.79 0.25 150.49) 49%, 
            oklch(0.63 0.2 251.22) 65%, 
            oklch(0.72 0.21 150.89) 93%, 
            oklch(0.63 0.2 251.22)
          );
          animation: rotate-gradient 5s infinite linear;
        }

        /* The glowing border effect */
        .radiant-input-wrapper::before {
          content: '';
          position: absolute;
          inset: calc(var(--border-size) * -1);
          border-radius: inherit;
          background: var(--gradient);
          z-index: -1;
          filter: blur(8px);
          opacity: 0.6;
        }

        /* The sharp border mask */
        .radiant-input-border {
          position: absolute;
          inset: 0;
          border-radius: inherit;
          padding: var(--border-size);
          background: var(--gradient);
          -webkit-mask: 
            linear-gradient(#fff 0 0) content-box, 
            linear-gradient(#fff 0 0);
          -webkit-mask-composite: xor;
          mask-composite: exclude;
          pointer-events: none;
        }
      `}</style>

      <div className="radiant-input-wrapper relative rounded-full bg-white dark:bg-zinc-900 group transition-all duration-300 hover:shadow-lg hover:shadow-primary/5">
        
        {/* Animated Gradient Border */}
        <div className="radiant-input-border rounded-full" />
        
        {/* Inner Content */}
        <div className="relative z-10 flex items-center gap-2 p-1.5 pl-4 pr-1.5 h-14 md:h-16">
          
          {/* Add Button */}
          <button 
            type="button"
            className="flex items-center justify-center w-8 h-8 md:w-10 md:h-10 rounded-full text-muted-foreground hover:bg-muted/50 hover:text-foreground transition-colors"
            aria-label="Add attachment"
          >
            <Plus size={20} strokeWidth={2} />
          </button>

          {/* Text Input */}
          <input
            type="text"
            value={value}
            onChange={handleChange}
            onKeyDown={handleKeyDown}
            placeholder={placeholder}
            disabled={disabled}
            className="flex-1 bg-transparent border-none outline-none text-foreground placeholder:text-muted-foreground/70 text-base md:text-lg font-light tracking-wide h-full w-full min-w-0"
          />

          {/* Right Actions */}
          <div className="flex items-center gap-1 md:gap-2">
            
            {/* Mic Button */}
            <button 
              type="button"
              className="flex items-center justify-center w-8 h-8 md:w-10 md:h-10 rounded-full text-muted-foreground hover:bg-muted/50 hover:text-foreground transition-colors"
              aria-label="Use microphone"
            >
              <Mic size={20} strokeWidth={2} />
            </button>

            {/* Submit Button */}
            <button
              type="button"
              onClick={handleSubmit}
              disabled={!value || disabled}
              className={cn(
                "flex items-center justify-center w-10 h-10 md:w-12 md:h-12 rounded-full transition-all duration-300",
                value 
                  ? "bg-foreground text-background hover:scale-105 active:scale-95 shadow-md" 
                  : "bg-muted text-muted-foreground cursor-not-allowed opacity-50"
              )}
              aria-label="Send message"
            >
              <ArrowUp size={22} strokeWidth={2.5} />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default RadiantPromptInput;
~~~

Implementation Guidelines

1. Analyze the component structure, styling, animation implementations
2. Review the component's arguments and state
3. Think through what is the best place to adopt this component/style into the design we are doing
4. Then adopt the component/design to our current system

Help me integrate this into my design
```

**▶ Try it live → [https://superdesign.dev/library/radiant-prompt-input](https://superdesign.dev/library/radiant-prompt-input?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library)**

**Use it in your coding agent:** install the [Superdesign skill](https://github.com/superdesigndev/superdesign-skill), then:

```bash
superdesign get-prompts --slugs "radiant-prompt-input" --json
```

*348 copies · 2,289 tries · Components · General · ui component, input*
