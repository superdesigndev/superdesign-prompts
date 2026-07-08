---
title: "Gradient Blinds Background"
slug: gradient-blinds-background
tags: ["animation", "background"]
copyCount: 255
tryCount: 2215
source: https://superdesign.dev/library/gradient-blinds-background
---

# Gradient Blinds Background

A premium, minimalist showcase of the GradientBlinds background effect. Features a smooth, reactive blind-like gradient animation with spotlight effects and mouse interaction.

Source: ReactBits

![Gradient Blinds Background](./preview.mp4)

## Prompt

```text
You are given a task to integrate an existing React component in the codebase

~~~/README.md
# GradientBlinds Showcase

A premium, high-performance background effect featuring dynamic "blinds" or stripes overlaying a reactive gradient. Built with OGL (WebGL) for smooth performance and interactive spotlighting.

## Dependencies

- `ogl`: ^0.0.116
- `lucide-react`: ^0.454.0
- `react`: ^18.0.0
- `react-dom`: ^18.0.0

## Component Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` | `undefined` | Additional CSS classes for the container |
| `dpr` | `number` | `window.devicePixelRatio` | Device Pixel Ratio for rendering |
| `paused` | `boolean` | `false` | Pause the animation loop |
| `gradientColors` | `string[]` | `['#FF9FFC', '#5227FF']` | Array of hex colors for the gradient (max 8) |
| `angle` | `number` | `0` | Rotation angle of the blinds in degrees |
| `noise` | `number` | `0.3` | Amount of film grain/noise texture |
| `blindCount` | `number` | `16` | Number of blind stripes |
| `blindMinWidth` | `number` | `60` | Minimum width of blinds before scaling down |
| `mouseDampening` | `number` | `0.15` | Smoothing factor for mouse tracking (0 for instant) |
| `mirrorGradient` | `boolean` | `false` | Mirror the gradient across the center |
| `spotlightRadius` | `number` | `0.5` | Size of the interactive spotlight |
| `spotlightSoftness` | `number` | `1.0` | Falloff softness of the spotlight |
| `spotlightOpacity` | `number` | `1.0` | Intensity of the spotlight effect |
| `distortAmount` | `number` | `0` | Wave distortion amount |
| `shineDirection` | `'left' \| 'right'` | `'left'` | Direction of the blind highlight |
| `mixBlendMode` | `string` | `'lighten'` | CSS mix-blend-mode for the container |

## Usage Example

```tsx
import { GradientBlinds } from '@/sd-components/78335fea-2bdb-453f-a435-1adadc815c1c';

function MySection() {
  return (
    <div className="relative w-full h-[600px]">
      <GradientBlinds
        gradientColors={['#FF9FFC', '#5227FF']}
        angle={-15}
        blindCount={24}
        spotlightRadius={0.7}
      />
      <div className="relative z-10 p-20">
        <h1 className="text-6xl font-bold text-white">Interactive Visuals</h1>
      </div>
    </div>
  );
}
```
~~~

~~~/src/App.tsx
import React from 'react';
import { GradientBlinds } from './Component';
import { RefreshCcw } from 'lucide-react';

/**
 * App.tsx
 * 
 * Minimalist Showcase for the GradientBlinds component.
 * Follows the 'Minimalist Showcase' style guide:
 * - Clean background
 * - Ample whitespace
 * - Floating premium feel
 * - Monochrome base with a single accent
 */

export default function App() {
  const [key, setKey] = React.useState(0);

  return (
    <div className="min-h-screen bg-[#F9F9F9] flex flex-col items-center justify-center p-20 select-none">
      {/* Container with soft shadow for premium feel */}
      <div className="relative w-full max-w-5xl aspect-video rounded-3xl overflow-hidden bg-[#1A1A1B] shadow-[0_40px_80px_-15px_rgba(0,0,0,0.1)] border border-white/5">
        
        {/* The Animated Component */}
        <GradientBlinds
          key={key}
          gradientColors={['#FF9FFC', '#5227FF']}
          angle={-15}
          noise={0.2}
          blindCount={20}
          blindMinWidth={40}
          spotlightRadius={0.6}
          spotlightSoftness={0.8}
          spotlightOpacity={0.9}
          mouseDampening={0.12}
          distortAmount={2}
          shineDirection="left"
          mixBlendMode="lighten"
        />

        {/* Floating Label - Top Left */}
        <div className="absolute top-8 left-8 z-10">
          <h1 className="text-white text-2xl font-medium tracking-tight">
            Gradient Blinds
          </h1>
          <p className="text-white/40 text-sm mt-1 uppercase tracking-widest font-medium">
            Atmospheric Motion
          </p>
        </div>

        {/* Reply/Reset Button - Bottom Right */}
        <div className="absolute bottom-8 right-8 z-10">
          <button
            onClick={() => setKey(prev => prev + 1)}
            className="flex items-center gap-2 px-6 py-3 bg-white/10 hover:bg-white/20 backdrop-blur-md border border-white/10 rounded-full text-white text-sm font-medium transition-all active:scale-95 group"
          >
            <RefreshCcw className="w-4 h-4 group-hover:rotate-180 transition-transform duration-500" />
            <span>Reset Effect</span>
          </button>
        </div>
      </div>

      {/* Subtle background detail */}
      <div className="fixed inset-0 pointer-events-none opacity-[0.03] z-[-1]">
        <div className="absolute inset-0 bg-[radial-gradient(#000_1px,transparent_1px)] [background-size:24px_24px]" />
      </div>
    </div>
  );
}
~~~

~~~/package.json
{
  "name": "gradient-blinds-showcase",
  "description": "Premium WebGL background effect with interactive blinds and gradients.",
  "dependencies": {
    "ogl": "^0.0.116",
    "lucide-react": "^0.454.0"
  }
}
~~~

~~~/src/Component.tsx
/**
 * GradientBlinds Component
 * 
 * A high-performance background effect using OGL for WebGL rendering.
 * Features a "blinds" or "stripe" effect overlaying a dynamic gradient.
 * Reactive to mouse movement with spotlight effects and noise textures.
 */

import React, { useEffect, useRef } from 'react';
import { Renderer, Program, Mesh, Triangle } from 'ogl';

export interface GradientBlindsProps {
  className?: string;
  dpr?: number;
  paused?: boolean;
  gradientColors?: string[];
  angle?: number;
  noise?: number;
  blindCount?: number;
  blindMinWidth?: number;
  mouseDampening?: number;
  mirrorGradient?: boolean;
  spotlightRadius?: number;
  spotlightSoftness?: number;
  spotlightOpacity?: number;
  distortAmount?: number;
  shineDirection?: 'left' | 'right';
  mixBlendMode?: string;
}

const MAX_COLORS = 8;

const hexToRGB = (hex: string): [number, number, number] => {
  const c = hex.replace('#', '').padEnd(6, '0');
  const r = parseInt(c.slice(0, 2), 16) / 255;
  const g = parseInt(c.slice(2, 4), 16) / 255;
  const b = parseInt(c.slice(4, 6), 16) / 255;
  return [r, g, b];
};

const prepStops = (stops?: string[]) => {
  const base = (stops && stops.length ? stops : ['#FF9FFC', '#5227FF']).slice(0, MAX_COLORS);
  if (base.length === 1) base.push(base[0]);
  while (base.length < MAX_COLORS) base.push(base[base.length - 1]);
  const arr: [number, number, number][] = [];
  for (let i = 0; i < MAX_COLORS; i++) arr.push(hexToRGB(base[i]));
  const count = Math.max(2, Math.min(MAX_COLORS, stops?.length ?? 2));
  return { arr, count };
};

export function GradientBlinds({
  className,
  dpr,
  paused = false,
  gradientColors,
  angle = 0,
  noise = 0.3,
  blindCount = 16,
  blindMinWidth = 60,
  mouseDampening = 0.15,
  mirrorGradient = false,
  spotlightRadius = 0.5,
  spotlightSoftness = 1,
  spotlightOpacity = 1,
  distortAmount = 0,
  shineDirection = 'left',
  mixBlendMode = 'lighten'
}: GradientBlindsProps) {
  const containerRef = useRef<HTMLDivElement | null>(null);
  const rafRef = useRef<number | null>(null);
  const programRef = useRef<Program | null>(null);
  const meshRef = useRef<Mesh<Triangle> | null>(null);
  const geometryRef = useRef<Triangle | null>(null);
  const rendererRef = useRef<Renderer | null>(null);
  const mouseTargetRef = useRef<[number, number]>([0, 0]);
  const lastTimeRef = useRef<number>(0);
  const firstResizeRef = useRef<boolean>(true);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    const renderer = new Renderer({
      dpr: dpr ?? (typeof window !== 'undefined' ? window.devicePixelRatio || 1 : 1),
      alpha: true,
      antialias: true
    });
    rendererRef.current = renderer;
    const gl = renderer.gl;
    const canvas = gl.canvas as HTMLCanvasElement;
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.display = 'block';
    container.appendChild(canvas);

    const vertex = `
attribute vec2 position;
attribute vec2 uv;
varying vec2 vUv;
void main() {
  vUv = uv;
  gl_Position = vec4(position, 0.0, 1.0);
}
`;

    const fragment = `
#ifdef GL_ES
precision mediump float;
#endif
uniform vec3  iResolution;
uniform vec2  iMouse;
uniform float iTime;
uniform float uAngle;
uniform float uNoise;
uniform float uBlindCount;
uniform float uSpotlightRadius;
uniform float uSpotlightSoftness;
uniform float uSpotlightOpacity;
uniform float uMirror;
uniform float uDistort;
uniform float uShineFlip;
uniform vec3  uColor0;
uniform vec3  uColor1;
uniform vec3  uColor2;
uniform vec3  uColor3;
uniform vec3  uColor4;
uniform vec3  uColor5;
uniform vec3  uColor6;
uniform vec3  uColor7;
uniform int   uColorCount;
varying vec2 vUv;

float rand(vec2 co){
  return fract(sin(dot(co, vec2(12.9898,78.233))) * 43758.5453);
}

vec2 rotate2D(vec2 p, float a){
  float c = cos(a);
  float s = sin(a);
  return mat2(c, -s, s, c) * p;
}

vec3 getGradientColor(float t){
  float tt = clamp(t, 0.0, 1.0);
  int count = uColorCount;
  if (count < 2) count = 2;
  float scaled = tt * float(count - 1);
  float seg = floor(scaled);
  float f = fract(scaled);
  if (seg < 1.0) return mix(uColor0, uColor1, f);
  if (seg < 2.0 && count > 2) return mix(uColor1, uColor2, f);
  if (seg < 3.0 && count > 3) return mix(uColor2, uColor3, f);
  if (seg < 4.0 && count > 4) return mix(uColor3, uColor4, f);
  if (seg < 5.0 && count > 5) return mix(uColor4, uColor5, f);
  if (seg < 6.0 && count > 6) return mix(uColor5, uColor6, f);
  if (seg < 7.0 && count > 7) return mix(uColor6, uColor7, f);
  if (count > 7) return uColor7;
  if (count > 6) return uColor6;
  if (count > 5) return uColor5;
  if (count > 4) return uColor4;
  if (count > 3) return uColor3;
  if (count > 2) return uColor2;
  return uColor1;
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    vec2 uv0 = fragCoord.xy / iResolution.xy;
    float aspect = iResolution.x / iResolution.y;
    vec2 p = uv0 * 2.0 - 1.0;
    p.x *= aspect;
    vec2 pr = rotate2D(p, uAngle);
    pr.x /= aspect;
    vec2 uv = pr * 0.5 + 0.5;
    
    vec2 uvMod = uv;
    if (uDistort > 0.0) {
      float a = uvMod.y * 6.0;
      float b = uvMod.x * 6.0;
      float w = 0.01 * uDistort;
      uvMod.x += sin(a) * w;
      uvMod.y += cos(b) * w;
    }

    float t = uvMod.x;
    if (uMirror > 0.5) {
      t = 1.0 - abs(1.0 - 2.0 * fract(t));
    }
    
    vec3 base = getGradientColor(t);
    vec2 offset = vec2(iMouse.x/iResolution.x, iMouse.y/iResolution.y);
    float d = length(uv0 - offset);
    float r = max(uSpotlightRadius, 1e-4);
    float dn = d / r;
    float spot = (1.0 - 2.0 * pow(dn, uSpotlightSoftness)) * uSpotlightOpacity;
    vec3 cir = vec3(spot);
    
    float stripe = fract(uvMod.x * max(uBlindCount, 1.0));
    if (uShineFlip > 0.5) stripe = 1.0 - stripe;
    vec3 ran = vec3(stripe);
    vec3 col = cir + base - ran;
    col += (rand(gl_FragCoord.xy + iTime) - 0.5) * uNoise;
    fragColor = vec4(col, 1.0);
}

void main() {
    vec4 color;
    mainImage(color, vUv * iResolution.xy);
    gl_FragColor = color;
}
`;

    const { arr: colorArr, count: colorCount } = prepStops(gradientColors);

    const uniforms: any = {
      iResolution: {
        value: [gl.drawingBufferWidth, gl.drawingBufferHeight, 1]
      },
      iMouse: { value: [0, 0] },
      iTime: { value: 0 },
      uAngle: { value: (angle * Math.PI) / 180 },
      uNoise: { value: noise },
      uBlindCount: { value: Math.max(1, blindCount) },
      uSpotlightRadius: { value: spotlightRadius },
      uSpotlightSoftness: { value: spotlightSoftness },
      uSpotlightOpacity: { value: spotlightOpacity },
      uMirror: { value: mirrorGradient ? 1 : 0 },
      uDistort: { value: distortAmount },
      uShineFlip: { value: shineDirection === 'right' ? 1 : 0 },
      uColor0: { value: colorArr[0] },
      uColor1: { value: colorArr[1] },
      uColor2: { value: colorArr[2] },
      uColor3: { value: colorArr[3] },
      uColor4: { value: colorArr[4] },
      uColor5: { value: colorArr[5] },
      uColor6: { value: colorArr[6] },
      uColor7: { value: colorArr[7] },
      uColorCount: { value: colorCount }
    };

    const program = new Program(gl, {
      vertex,
      fragment,
      uniforms
    });
    programRef.current = program;

    const geometry = new Triangle(gl);
    geometryRef.current = geometry;

    const mesh = new Mesh(gl, { geometry, program });
    meshRef.current = mesh;

    const resize = () => {
      const rect = container.getBoundingClientRect();
      renderer.setSize(rect.width, rect.height);
      uniforms.iResolution.value = [gl.drawingBufferWidth, gl.drawingBufferHeight, 1];
      
      if (blindMinWidth && blindMinWidth > 0) {
        const maxByMinWidth = Math.max(1, Math.floor(rect.width / blindMinWidth));
        const effective = blindCount ? Math.min(blindCount, maxByMinWidth) : maxByMinWidth;
        uniforms.uBlindCount.value = Math.max(1, effective);
      } else {
        uniforms.uBlindCount.value = Math.max(1, blindCount);
      }

      if (firstResizeRef.current) {
        firstResizeRef.current = false;
        const cx = gl.drawingBufferWidth / 2;
        const cy = gl.drawingBufferHeight / 2;
        uniforms.iMouse.value = [cx, cy];
        mouseTargetRef.current = [cx, cy];
      }
    };

    resize();
    const ro = new ResizeObserver(resize);
    ro.observe(container);

    const onPointerMove = (e: PointerEvent) => {
      const rect = canvas.getBoundingClientRect();
      const scale = (renderer as any).dpr || 1;
      const x = (e.clientX - rect.left) * scale;
      const y = (rect.height - (e.clientY - rect.top)) * scale;
      mouseTargetRef.current = [x, y];
      if (mouseDampening <= 0) {
        uniforms.iMouse.value = [x, y];
      }
    };

    canvas.addEventListener('pointermove', onPointerMove);

    const loop = (t: number) => {
      rafRef.current = requestAnimationFrame(loop);
      uniforms.iTime.value = t * 0.001;

      if (mouseDampening > 0) {
        if (!lastTimeRef.current) lastTimeRef.current = t;
        const dt = (t - lastTimeRef.current) / 1000;
        lastTimeRef.current = t;
        const tau = Math.max(1e-4, mouseDampening);
        let factor = 1 - Math.exp(-dt / tau);
        if (factor > 1) factor = 1;
        const target = mouseTargetRef.current;
        const cur = uniforms.iMouse.value;
        cur[0] += (target[0] - cur[0]) * factor;
        cur[1] += (target[1] - cur[1]) * factor;
      } else {
        lastTimeRef.current = t;
      }

      if (!paused && programRef.current && meshRef.current) {
        try {
          renderer.render({ scene: meshRef.current });
        } catch (e) {
          console.error(e);
        }
      }
    };

    rafRef.current = requestAnimationFrame(loop);

    return () => {
      if (rafRef.current) cancelAnimationFrame(rafRef.current);
      canvas.removeEventListener('pointermove', onPointerMove);
      ro.disconnect();
      if (canvas.parentElement === container) {
        container.removeChild(canvas);
      }
      
      const callIfFn = (obj: any, key: string) => {
        if (obj && typeof obj[key] === 'function') {
          obj[key]();
        }
      };
      
      callIfFn(programRef.current, 'remove');
      callIfFn(geometryRef.current, 'remove');
      callIfFn(meshRef.current, 'remove');
      // renderer.destroy() is not always standard in all versions of OGL
      programRef.current = null;
      geometryRef.current = null;
      meshRef.current = null;
      rendererRef.current = null;
    };
  }, [
    dpr,
    paused,
    gradientColors,
    angle,
    noise,
    blindCount,
    blindMinWidth,
    mouseDampening,
    mirrorGradient,
    spotlightRadius,
    spotlightSoftness,
    spotlightOpacity,
    distortAmount,
    shineDirection
  ]);

  return (
    <div
      ref={containerRef}
      className={`w-full h-full overflow-hidden relative ${className}`}
      style={{
        ...(mixBlendMode && {
          mixBlendMode: mixBlendMode as React.CSSProperties['mixBlendMode']
        })
      }}
    />
  );
}

export default GradientBlinds;
~~~

Implementation Guidelines

1. Analyze the component structure, styling, animation implementations
2. Review the component's arguments and state
3. Think through what is the best place to adopt this component/style into the design we are doing
4. Then adopt the component/design to our current system

Help me integrate this into my design
```

**▶ Try it live → [https://superdesign.dev/library/gradient-blinds-background](https://superdesign.dev/library/gradient-blinds-background)**

*255 copies · 2,215 tries · tags: animation, background*
