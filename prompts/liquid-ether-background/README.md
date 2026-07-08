---
title: "Liquid Ether Background"
slug: liquid-ether-background
tags: ["background", "animation"]
copyCount: 444
tryCount: 1725
source: https://superdesign.dev/library/liquid-ether-background
---

# Liquid Ether Background

A production-grade showcase for the LiquidEther fluid simulation background effect. Features a minimalist, premium layout that emphasizes the motion and fluid dynamics of the WebGL-based ether effect.

![Liquid Ether Background](./preview.mp4)

## Prompt

```text
You are given a task to integrate an existing React component in the codebase

~~~/README.md
# LiquidEther

A production-grade WebGL fluid simulation component for React, built with Three.js. It provides a highly performant, interactive "liquid ether" background effect with smooth mouse interactions and an intelligent auto-demo driver.

## Features
- **Real-time Fluid Dynamics**: Navier-Stokes based simulation optimized for WebGL.
- **BFECC Support**: Back-and-Forth Error Compensation and Correction for high-fidelity fluid details.
- **Interactive**: Responds to mouse and touch movements with momentum.
- **Auto-Driver**: Seamlessly transitions between user control and automated movement.
- **Customizable**: Control colors, viscosity, resolution, and interaction force.
- **Performance Optimized**: Uses `HalfFloatType` on iOS and handles visibility/resizing efficiently.

## Dependencies
- `three`: ^0.170.0
- `react`: ^18.0.0
- `lucide-react`: ^0.454.0

## Component Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `colors` | `string[]` | `['#5227FF', '#FF9FFC', '#B19EEF']` | Array of hex strings for the simulation palette. |
| `mouseForce` | `number` | `20` | Force multiplier for mouse movement. |
| `cursorSize` | `number` | `100` | Interaction radius in pixels. |
| `resolution` | `number` | `0.5` | Simulation resolution scale (0.1 to 1.0). |
| `isViscous` | `boolean` | `false` | Enable viscosity simulation. |
| `viscous` | `number` | `30` | Viscosity coefficient. |
| `autoDemo` | `boolean` | `true` | Enable auto-movement when idle. |
| `autoSpeed` | `number` | `0.5` | Speed of the auto-demo driver. |

## Usage Example

```tsx
import { LiquidEther } from '@/sd-components/36039875-1e54-4edb-8860-9609381fb61c';

function MyComponent() {
  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <LiquidEther 
        colors={['#000000', '#3b82f6', '#ffffff']}
        mouseForce={25}
        autoDemo={true}
      />
    </div>
  );
}
```
~~~

~~~/src/App.tsx
/**
 * LiquidEther Showcase Demo
 * Displays a full-screen interactive fluid simulation using the LiquidEther component.
 * Follows the 'Minimalist Showcase' style guide.
 */

import React from 'react';
import { LiquidEther } from './Component';
import { RefreshCcw } from 'lucide-react';

export default function App() {
  const [key, setKey] = React.useState(0);

  const handleRefresh = () => {
    setKey(prev => prev + 1);
  };

  return (
    <div className="relative w-full h-screen bg-background overflow-hidden flex flex-col items-center justify-center p-20 lg:p-40">
      {/* Premium Floating Container */}
      <div className="relative w-full max-w-5xl h-full bg-card rounded-3xl overflow-hidden shadow-[0_40px_80px_-20px_rgba(0,0,0,0.05)] border border-border/50 group">
        
        {/* The Component Itself */}
        <div className="absolute inset-0 z-0">
          <LiquidEther
            key={key}
            colors={['#5227FF', '#FF9FFC', '#B19EEF']}
            mouseForce={25}
            cursorSize={120}
            autoDemo={true}
            autoSpeed={0.6}
            autoIntensity={2.5}
            resolution={0.6}
            BFECC={true}
          />
        </div>

        {/* Minimalist Overlay UI */}
        <div className="absolute inset-0 z-10 p-12 pointer-events-none flex flex-col justify-between">
          <div className="space-y-2">
            <h1 className="text-4xl font-semibold tracking-tight text-foreground/90 font-sans">
              Liquid Ether
            </h1>
            <p className="text-muted-foreground font-medium text-sm tracking-widest uppercase">
              Fluid Dynamics Simulation
            </p>
          </div>

          <div className="flex justify-end pointer-events-auto">
            <button
              onClick={handleRefresh}
              className="flex items-center gap-2 px-6 py-3 bg-primary text-primary-foreground rounded-full text-sm font-semibold tracking-tight hover:scale-105 transition-all duration-300 shadow-lg active:scale-95"
            >
              <RefreshCcw className="w-4 h-4" />
              Reply Animation
            </button>
          </div>
        </div>
      </div>

      {/* Atmospheric Background Noise/Grain (Optional but adds premium feel) */}
      <div className="absolute inset-0 pointer-events-none opacity-[0.03] mix-blend-overlay bg-[url('https://grainy-gradients.vercel.app/noise.svg')]" />
    </div>
  );
}
~~~

~~~/package.json
{
  "name": "liquid-ether-showcase",
  "description": "Premium fluid simulation showcase component",
  "dependencies": {
    "three": "^0.170.0",
    "@types/three": "^0.170.0",
    "lucide-react": "^0.454.0",
    "framer-motion": "^11.11.17"
  }
}
~~~

~~~/src/Component.tsx
/**
 * LiquidEther Component
 * A high-performance WebGL fluid simulation component using Three.js.
 * Features:
 * - Real-time fluid dynamics
 * - Mouse interaction and auto-demo driver
 * - Custom color palettes
 * - Responsive sizing and intersection observation for performance
 */

import React, { useEffect, useRef } from 'react';
import * as THREE from 'three';

export interface LiquidEtherProps {
  /** Force multiplier for mouse movement */
  mouseForce?: number;
  /** Radius of the interaction cursor in pixels */
  cursorSize?: number;
  /** Whether to enable viscosity simulation */
  isViscous?: boolean;
  /** Viscosity coefficient */
  viscous?: number;
  /** Number of iterations for viscosity calculation */
  iterationsViscous?: number;
  /** Number of iterations for Poisson pressure calculation */
  iterationsPoisson?: number;
  /** Time step for simulation */
  dt?: number;
  /** Back-and-Forth Error Compensation and Correction for sharper details */
  BFECC?: boolean;
  /** Simulation resolution (0.0 to 1.0) */
  resolution?: number;
  /** Whether the fluid bounces off edges */
  isBounce?: boolean;
  /** Array of hex color strings for the palette */
  colors?: string[];
  /** Custom styles for the container */
  style?: React.CSSProperties;
  /** Custom class name for the container */
  className?: string;
  /** Enable automatic movement when no user interaction */
  autoDemo?: boolean;
  /** Speed of the auto-demo driver */
  autoSpeed?: number;
  /** Intensity multiplier for auto-demo driver forces */
  autoIntensity?: number;
  /** Duration of transition when user takes over control (seconds) */
  takeoverDuration?: number;
  /** Delay before auto-demo resumes after last interaction (ms) */
  autoResumeDelay?: number;
  /** Duration of the ramp-up when auto-demo starts (seconds) */
  autoRampDuration?: number;
}

interface SimOptions {
  iterations_poisson: number;
  iterations_viscous: number;
  mouse_force: number;
  resolution: number;
  cursor_size: number;
  viscous: number;
  isBounce: boolean;
  dt: number;
  isViscous: boolean;
  BFECC: boolean;
}

interface LiquidEtherWebGL {
  output?: { simulation?: { options: SimOptions; resize: () => void } };
  autoDriver?: {
    enabled: boolean;
    speed: number;
    resumeDelay: number;
    rampDurationMs: number;
    mouse?: { autoIntensity: number; takeoverDuration: number };
    forceStop: () => void;
  };
  resize: () => void;
  start: () => void;
  pause: () => void;
  dispose: () => void;
}

const defaultColors = ['#5227FF', '#FF9FFC', '#B19EEF'];

export function LiquidEther({
  mouseForce = 20,
  cursorSize = 100,
  isViscous = false,
  viscous = 30,
  iterationsViscous = 32,
  iterationsPoisson = 32,
  dt = 0.014,
  BFECC = true,
  resolution = 0.5,
  isBounce = false,
  colors = defaultColors,
  style = {},
  className = '',
  autoDemo = true,
  autoSpeed = 0.5,
  autoIntensity = 2.2,
  takeoverDuration = 0.25,
  autoResumeDelay = 1000,
  autoRampDuration = 0.6
}: LiquidEtherProps): React.ReactElement {
  const mountRef = useRef<HTMLDivElement | null>(null);
  const webglRef = useRef<LiquidEtherWebGL | null>(null);
  const resizeObserverRef = useRef<ResizeObserver | null>(null);
  const rafRef = useRef<number | null>(null);
  const intersectionObserverRef = useRef<IntersectionObserver | null>(null);
  const isVisibleRef = useRef<boolean>(true);
  const resizeRafRef = useRef<number | null>(null);

  useEffect(() => {
    if (!mountRef.current) return;

    function makePaletteTexture(stops: string[]): THREE.DataTexture {
      let arr: string[];
      if (Array.isArray(stops) && stops.length > 0) {
        arr = stops.length === 1 ? [stops[0], stops[0]] : stops;
      } else {
        arr = ['#ffffff', '#ffffff'];
      }
      const w = arr.length;
      const data = new Uint8Array(w * 4);
      for (let i = 0; i < w; i++) {
        const c = new THREE.Color(arr[i]);
        data[i * 4 + 0] = Math.round(c.r * 255);
        data[i * 4 + 1] = Math.round(c.g * 255);
        data[i * 4 + 2] = Math.round(c.b * 255);
        data[i * 4 + 3] = 255;
      }
      const tex = new THREE.DataTexture(data, w, 1, THREE.RGBAFormat);
      tex.magFilter = THREE.LinearFilter;
      tex.minFilter = THREE.LinearFilter;
      tex.wrapS = THREE.ClampToEdgeWrapping;
      tex.wrapT = THREE.ClampToEdgeWrapping;
      tex.generateMipmaps = false;
      tex.needsUpdate = true;
      return tex;
    }

    const paletteTex = makePaletteTexture(colors);
    const bgVec4 = new THREE.Vector4(0, 0, 0, 0);

    class CommonClass {
      width = 0;
      height = 0;
      aspect = 1;
      pixelRatio = 1;
      isMobile = false;
      breakpoint = 768;
      fboWidth: number | null = null;
      fboHeight: number | null = null;
      time = 0;
      delta = 0;
      container: HTMLElement | null = null;
      renderer: THREE.WebGLRenderer | null = null;
      clock: THREE.Clock | null = null;

      init(container: HTMLElement) {
        this.container = container;
        this.pixelRatio = Math.min(window.devicePixelRatio || 1, 2);
        this.resize();
        this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        this.renderer.autoClear = false;
        this.renderer.setClearColor(new THREE.Color(0x000000), 0);
        this.renderer.setPixelRatio(this.pixelRatio);
        this.renderer.setSize(this.width, this.height);
        const el = this.renderer.domElement;
        el.style.width = '100%';
        el.style.height = '100%';
        el.style.display = 'block';
        this.clock = new THREE.Clock();
        this.clock.start();
      }

      resize() {
        if (!this.container) return;
        const rect = this.container.getBoundingClientRect();
        this.width = Math.max(1, Math.floor(rect.width));
        this.height = Math.max(1, Math.floor(rect.height));
        this.aspect = this.width / this.height;
        if (this.renderer) this.renderer.setSize(this.width, this.height, false);
      }

      update() {
        if (!this.clock) return;
        this.delta = this.clock.getDelta();
        this.time += this.delta;
      }
    }

    const Common = new CommonClass();

    class MouseClass {
      mouseMoved = false;
      coords = new THREE.Vector2();
      coords_old = new THREE.Vector2();
      diff = new THREE.Vector2();
      timer: number | null = null;
      container: HTMLElement | null = null;
      docTarget: Document | null = null;
      listenerTarget: Window | null = null;
      isHoverInside = false;
      hasUserControl = false;
      isAutoActive = false;
      autoIntensity = 2.0;
      takeoverActive = false;
      takeoverStartTime = 0;
      takeoverDuration = 0.25;
      takeoverFrom = new THREE.Vector2();
      takeoverTo = new THREE.Vector2();
      onInteract: (() => void) | null = null;

      private _onMouseMove = this.onDocumentMouseMove.bind(this);
      private _onTouchStart = this.onDocumentTouchStart.bind(this);
      private _onTouchMove = this.onDocumentTouchMove.bind(this);
      private _onTouchEnd = this.onTouchEnd.bind(this);
      private _onDocumentLeave = this.onDocumentLeave.bind(this);

      init(container: HTMLElement) {
        this.container = container;
        this.docTarget = container.ownerDocument || null;
        const defaultView = this.docTarget?.defaultView || (typeof window !== 'undefined' ? window : null);
        if (!defaultView) return;
        this.listenerTarget = defaultView;
        this.listenerTarget.addEventListener('mousemove', this._onMouseMove);
        this.listenerTarget.addEventListener('touchstart', this._onTouchStart, { passive: true });
        this.listenerTarget.addEventListener('touchmove', this._onTouchMove, { passive: true });
        this.listenerTarget.addEventListener('touchend', this._onTouchEnd);
        this.docTarget?.addEventListener('mouseleave', this._onDocumentLeave);
      }

      dispose() {
        if (this.listenerTarget) {
          this.listenerTarget.removeEventListener('mousemove', this._onMouseMove);
          this.listenerTarget.removeEventListener('touchstart', this._onTouchStart);
          this.listenerTarget.removeEventListener('touchmove', this._onTouchMove);
          this.listenerTarget.removeEventListener('touchend', this._onTouchEnd);
        }
        if (this.docTarget) {
          this.docTarget.removeEventListener('mouseleave', this._onDocumentLeave);
        }
        this.listenerTarget = null;
        this.docTarget = null;
        this.container = null;
      }

      private isPointInside(clientX: number, clientY: number) {
        if (!this.container) return false;
        const rect = this.container.getBoundingClientRect();
        return clientX >= rect.left && clientX <= rect.right && clientY >= rect.top && clientY <= rect.bottom;
      }

      private updateHoverState(clientX: number, clientY: number) {
        this.isHoverInside = this.isPointInside(clientX, clientY);
        return this.isHoverInside;
      }

      setCoords(x: number, y: number) {
        if (!this.container) return;
        if (this.timer) window.clearTimeout(this.timer);
        const rect = this.container.getBoundingClientRect();
        if (rect.width === 0 || rect.height === 0) return;
        const nx = (x - rect.left) / rect.width;
        const ny = (y - rect.top) / rect.height;
        this.coords.set(nx * 2 - 1, -(ny * 2 - 1));
        this.mouseMoved = true;
        this.timer = window.setTimeout(() => {
          this.mouseMoved = false;
        }, 100);
      }

      setNormalized(nx: number, ny: number) {
        this.coords.set(nx, ny);
        this.mouseMoved = true;
      }

      onDocumentMouseMove(event: MouseEvent) {
        if (!this.updateHoverState(event.clientX, event.clientY)) return;
        if (this.onInteract) this.onInteract();
        if (this.isAutoActive && !this.hasUserControl && !this.takeoverActive) {
          if (!this.container) return;
          const rect = this.container.getBoundingClientRect();
          const nx = (event.clientX - rect.left) / rect.width;
          const ny = (event.clientY - rect.top) / rect.height;
          this.takeoverFrom.copy(this.coords);
          this.takeoverTo.set(nx * 2 - 1, -(ny * 2 - 1));
          this.takeoverStartTime = performance.now();
          this.takeoverActive = true;
          this.hasUserControl = true;
          this.isAutoActive = false;
          return;
        }
        this.setCoords(event.clientX, event.clientY);
        this.hasUserControl = true;
      }

      onDocumentTouchStart(event: TouchEvent) {
        if (event.touches.length !== 1) return;
        const t = event.touches[0];
        if (!this.updateHoverState(t.clientX, t.clientY)) return;
        if (this.onInteract) this.onInteract();
        this.setCoords(t.clientX, t.clientY);
        this.hasUserControl = true;
      }

      onDocumentTouchMove(event: TouchEvent) {
        if (event.touches.length !== 1) return;
        const t = event.touches[0];
        if (!this.updateHoverState(t.clientX, t.clientY)) return;
        if (this.onInteract) this.onInteract();
        this.setCoords(t.clientX, t.clientY);
      }

      onTouchEnd() { this.isHoverInside = false; }
      onDocumentLeave() { this.isHoverInside = false; }

      update() {
        if (this.takeoverActive) {
          const t = (performance.now() - this.takeoverStartTime) / (this.takeoverDuration * 1000);
          if (t >= 1) {
            this.takeoverActive = false;
            this.coords.copy(this.takeoverTo);
            this.coords_old.copy(this.coords);
            this.diff.set(0, 0);
          } else {
            const k = t * t * (3 - 2 * t);
            this.coords.copy(this.takeoverFrom).lerp(this.takeoverTo, k);
          }
        }
        this.diff.subVectors(this.coords, this.coords_old);
        this.coords_old.copy(this.coords);
        if (this.coords_old.x === 0 && this.coords_old.y === 0) this.diff.set(0, 0);
        if (this.isAutoActive && !this.takeoverActive) this.diff.multiplyScalar(this.autoIntensity);
      }
    }

    const Mouse = new MouseClass();

    class AutoDriver {
      mouse: MouseClass;
      manager: WebGLManager;
      enabled: boolean;
      speed: number;
      resumeDelay: number;
      rampDurationMs: number;
      active = false;
      current = new THREE.Vector2(0, 0);
      target = new THREE.Vector2();
      lastTime = performance.now();
      activationTime = 0;
      margin = 0.2;
      private _tmpDir = new THREE.Vector2();

      constructor(mouse: MouseClass, manager: WebGLManager, opts: any) {
        this.mouse = mouse;
        this.manager = manager;
        this.enabled = opts.enabled;
        this.speed = opts.speed;
        this.resumeDelay = opts.resumeDelay || 3000;
        this.rampDurationMs = (opts.rampDuration || 0) * 1000;
        this.pickNewTarget();
      }

      pickNewTarget() {
        const r = Math.random;
        this.target.set((r() * 2 - 1) * (1 - this.margin), (r() * 2 - 1) * (1 - this.margin));
      }

      forceStop() {
        this.active = false;
        this.mouse.isAutoActive = false;
      }

      update() {
        if (!this.enabled) return;
        const now = performance.now();
        const idle = now - this.manager.lastUserInteraction;
        if (idle < this.resumeDelay || this.mouse.isHoverInside) {
          if (this.active) this.forceStop();
          return;
        }
        if (!this.active) {
          this.active = true;
          this.current.copy(this.mouse.coords);
          this.lastTime = now;
          this.activationTime = now;
        }
        if (!this.active) return;
        this.mouse.isAutoActive = true;
        let dtSec = (now - this.lastTime) / 1000;
        this.lastTime = now;
        if (dtSec > 0.2) dtSec = 0.016;
        const dir = this._tmpDir.subVectors(this.target, this.current);
        const dist = dir.length();
        if (dist < 0.01) {
          this.pickNewTarget();
          return;
        }
        dir.normalize();
        let ramp = 1;
        if (this.rampDurationMs > 0) {
          const t = Math.min(1, (now - this.activationTime) / this.rampDurationMs);
          ramp = t * t * (3 - 2 * t);
        }
        const step = this.speed * dtSec * ramp;
        const move = Math.min(step, dist);
        this.current.addScaledVector(dir, move);
        this.mouse.setNormalized(this.current.x, this.current.y);
      }
    }

    const face_vert = `
      attribute vec3 position;
      uniform vec2 px;
      uniform vec2 boundarySpace;
      varying vec2 uv;
      precision highp float;
      void main(){
        vec3 pos = position;
        vec2 scale = 1.0 - boundarySpace * 2.0;
        pos.xy = pos.xy * scale;
        uv = vec2(0.5)+(pos.xy)*0.5;
        gl_Position = vec4(pos, 1.0);
      }
    `;

    const line_vert = `
      attribute vec3 position;
      uniform vec2 px;
      precision highp float;
      varying vec2 uv;
      void main(){
        vec3 pos = position;
        uv = 0.5 + pos.xy * 0.5;
        vec2 n = sign(pos.xy);
        pos.xy = abs(pos.xy) - px * 1.0;
        pos.xy *= n;
        gl_Position = vec4(pos, 1.0);
      }
    `;

    const mouse_vert = `
      precision highp float;
      attribute vec3 position;
      attribute vec2 uv;
      uniform vec2 center;
      uniform vec2 scale;
      uniform vec2 px;
      varying vec2 vUv;
      void main(){
        vec2 pos = position.xy * scale * 2.0 * px + center;
        vUv = uv;
        gl_Position = vec4(pos, 0.0, 1.0);
      }
    `;

    const advection_frag = `
      precision highp float;
      uniform sampler2D velocity;
      uniform float dt;
      uniform bool isBFECC;
      uniform vec2 fboSize;
      uniform vec2 px;
      varying vec2 uv;
      void main(){
        vec2 ratio = max(fboSize.x, fboSize.y) / fboSize;
        if(isBFECC == false){
          vec2 vel = texture2D(velocity, uv).xy;
          vec2 uv2 = uv - vel * dt * ratio;
          vec2 newVel = texture2D(velocity, uv2).xy;
          gl_FragColor = vec4(newVel, 0.0, 0.0);
        } else {
          vec2 spot_new = uv;
          vec2 vel_old = texture2D(velocity, uv).xy;
          vec2 spot_old = spot_new - vel_old * dt * ratio;
          vec2 vel_new1 = texture2D(velocity, spot_old).xy;
          vec2 spot_new2 = spot_old + vel_new1 * dt * ratio;
          vec2 error = spot_new2 - spot_new;
          vec2 spot_new3 = spot_new - error / 2.0;
          vec2 vel_2 = texture2D(velocity, spot_new3).xy;
          vec2 spot_old2 = spot_new3 - vel_2 * dt * ratio;
          vec2 newVel2 = texture2D(velocity, spot_old2).xy; 
          gl_FragColor = vec4(newVel2, 0.0, 0.0);
        }
      }
    `;

    const color_frag = `
      precision highp float;
      uniform sampler2D velocity;
      uniform sampler2D palette;
      uniform vec4 bgColor;
      varying vec2 uv;
      void main(){
        vec2 vel = texture2D(velocity, uv).xy;
        float lenv = clamp(length(vel), 0.0, 1.0);
        vec3 c = texture2D(palette, vec2(lenv, 0.5)).rgb;
        vec3 outRGB = mix(bgColor.rgb, c, lenv);
        float outA = mix(bgColor.a, 1.0, lenv);
        gl_FragColor = vec4(outRGB, outA);
      }
    `;

    const divergence_frag = `
      precision highp float;
      uniform sampler2D velocity;
      uniform float dt;
      uniform vec2 px;
      varying vec2 uv;
      void main(){
        float x0 = texture2D(velocity, uv-vec2(px.x, 0.0)).x;
        float x1 = texture2D(velocity, uv+vec2(px.x, 0.0)).x;
        float y0 = texture2D(velocity, uv-vec2(0.0, px.y)).y;
        float y1 = texture2D(velocity, uv+vec2(0.0, px.y)).y;
        float divergence = (x1 - x0 + y1 - y0) / 2.0;
        gl_FragColor = vec4(divergence / dt);
      }
    `;

    const externalForce_frag = `
      precision highp float;
      uniform vec2 force;
      uniform vec2 center;
      uniform vec2 scale;
      uniform vec2 px;
      varying vec2 vUv;
      void main(){
        vec2 circle = (vUv - 0.5) * 2.0;
        float d = 1.0 - min(length(circle), 1.0);
        d *= d;
        gl_FragColor = vec4(force * d, 0.0, 1.0);
      }
    `;

    const poisson_frag = `
      precision highp float;
      uniform sampler2D pressure;
      uniform sampler2D divergence;
      uniform vec2 px;
      varying vec2 uv;
      void main(){
        float p0 = texture2D(pressure, uv + vec2(px.x * 2.0, 0.0)).r;
        float p1 = texture2D(pressure, uv - vec2(px.x * 2.0, 0.0)).r;
        float p2 = texture2D(pressure, uv + vec2(0.0, px.y * 2.0)).r;
        float p3 = texture2D(pressure, uv - vec2(0.0, px.y * 2.0)).r;
        float div = texture2D(divergence, uv).r;
        float newP = (p0 + p1 + p2 + p3) / 4.0 - div;
        gl_FragColor = vec4(newP);
      }
    `;

    const pressure_frag = `
      precision highp float;
      uniform sampler2D pressure;
      uniform sampler2D velocity;
      uniform vec2 px;
      uniform float dt;
      varying vec2 uv;
      void main(){
        float step = 1.0;
        float p0 = texture2D(pressure, uv + vec2(px.x * step, 0.0)).r;
        float p1 = texture2D(pressure, uv - vec2(px.x * step, 0.0)).r;
        float p2 = texture2D(pressure, uv + vec2(0.0, px.y * step)).r;
        float p3 = texture2D(pressure, uv - vec2(0.0, px.y * step)).r;
        vec2 v = texture2D(velocity, uv).xy;
        vec2 gradP = vec2(p0 - p1, p2 - p3) * 0.5;
        v = v - gradP * dt;
        gl_FragColor = vec4(v, 0.0, 1.0);
      }
    `;

    const viscous_frag = `
      precision highp float;
      uniform sampler2D velocity;
      uniform sampler2D velocity_new;
      uniform float v;
      uniform vec2 px;
      uniform float dt;
      varying vec2 uv;
      void main(){
        vec2 old = texture2D(velocity, uv).xy;
        vec2 new0 = texture2D(velocity_new, uv + vec2(px.x * 2.0, 0.0)).xy;
        vec2 new1 = texture2D(velocity_new, uv - vec2(px.x * 2.0, 0.0)).xy;
        vec2 new2 = texture2D(velocity_new, uv + vec2(0.0, px.y * 2.0)).xy;
        vec2 new3 = texture2D(velocity_new, uv - vec2(0.0, px.y * 2.0)).xy;
        vec2 newv = 4.0 * old + v * dt * (new0 + new1 + new2 + new3);
        newv /= 4.0 * (1.0 + v * dt);
        gl_FragColor = vec4(newv, 0.0, 0.0);
      }
    `;

    type Uniforms = Record<string, { value: any }>;
    class ShaderPass {
      props: any;
      uniforms?: Uniforms;
      scene: THREE.Scene | null = null;
      camera: THREE.Camera | null = null;
      material: THREE.RawShaderMaterial | null = null;
      geometry: THREE.BufferGeometry | null = null;
      plane: THREE.Mesh | null = null;
      constructor(props: any) {
        this.props = props || {};
        this.uniforms = this.props.material?.uniforms;
      }
      init() {
        this.scene = new THREE.Scene();
        this.camera = new THREE.Camera();
        if (this.uniforms) {
          this.material = new THREE.RawShaderMaterial(this.props.material);
          this.geometry = new THREE.PlaneGeometry(2, 2);
          this.plane = new THREE.Mesh(this.geometry, this.material);
          this.scene.add(this.plane);
        }
      }
      update() {
        if (!Common.renderer || !this.scene || !this.camera) return;
        Common.renderer.setRenderTarget(this.props.output || null);
        Common.renderer.render(this.scene, this.camera);
        Common.renderer.setRenderTarget(null);
      }
    }

    class Advection extends ShaderPass {
      line!: THREE.LineSegments;
      constructor(simProps: any) {
        super({
          material: {
            vertexShader: face_vert,
            fragmentShader: advection_frag,
            uniforms: {
              boundarySpace: { value: simProps.cellScale },
              px: { value: simProps.cellScale },
              fboSize: { value: simProps.fboSize },
              velocity: { value: simProps.src.texture },
              dt: { value: simProps.dt },
              isBFECC: { value: true }
            }
          },
          output: simProps.dst
        });
        this.init();
      }
      init() {
        super.init();
        this.createBoundary();
      }
      createBoundary() {
        const boundaryG = new THREE.BufferGeometry();
        const vertices = new Float32Array([-1,-1,0, -1,1,0, -1,1,0, 1,1,0, 1,1,0, 1,-1,0, 1,-1,0, -1,-1,0]);
        boundaryG.setAttribute('position', new THREE.BufferAttribute(vertices, 3));
        const boundaryM = new THREE.RawShaderMaterial({
          vertexShader: line_vert,
          fragmentShader: advection_frag,
          uniforms: this.uniforms!
        });
        this.line = new THREE.LineSegments(boundaryG, boundaryM);
        this.scene!.add(this.line);
      }
      update(args: any) {
        const { dt, isBounce, BFECC } = args;
        if (!this.uniforms) return;
        this.uniforms.dt.value = dt;
        this.line.visible = isBounce;
        this.uniforms.isBFECC.value = BFECC;
        super.update();
      }
    }

    class ExternalForce extends ShaderPass {
      mouse!: THREE.Mesh;
      constructor(simProps: any) {
        super({ output: simProps.dst });
        this.init(simProps);
      }
      init(simProps: any) {
        super.init();
        const mouseG = new THREE.PlaneGeometry(1, 1);
        const mouseM = new THREE.RawShaderMaterial({
          vertexShader: mouse_vert,
          fragmentShader: externalForce_frag,
          blending: THREE.AdditiveBlending,
          depthWrite: false,
          uniforms: {
            px: { value: simProps.cellScale },
            force: { value: new THREE.Vector2(0, 0) },
            center: { value: new THREE.Vector2(0, 0) },
            scale: { value: new THREE.Vector2(simProps.cursor_size, simProps.cursor_size) }
          }
        });
        this.mouse = new THREE.Mesh(mouseG, mouseM);
        this.scene!.add(this.mouse);
      }
      update(args: any) {
        const { mouse_force, cellScale, cursor_size } = args;
        const uniforms = (this.mouse.material as THREE.RawShaderMaterial).uniforms;
        uniforms.force.value.set((Mouse.diff.x / 2) * mouse_force, (Mouse.diff.y / 2) * mouse_force);
        uniforms.center.value.set(Mouse.coords.x, Mouse.coords.y);
        uniforms.scale.value.set(cursor_size, cursor_size);
        super.update();
      }
    }

    class Viscous extends ShaderPass {
      constructor(simProps: any) {
        super({
          material: {
            vertexShader: face_vert,
            fragmentShader: viscous_frag,
            uniforms: {
              boundarySpace: { value: simProps.boundarySpace },
              velocity: { value: simProps.src.texture },
              velocity_new: { value: simProps.dst_.texture },
              v: { value: simProps.viscous },
              px: { value: simProps.cellScale },
              dt: { value: simProps.dt }
            }
          },
          output: simProps.dst,
          output0: simProps.dst_,
          output1: simProps.dst
        });
        this.init();
      }
      update(args: any) {
        const { iterations, dt } = args;
        for (let i = 0; i < iterations; i++) {
          const fbo_in = i % 2 === 0 ? this.props.output0 : this.props.output1;
          const fbo_out = i % 2 === 0 ? this.props.output1 : this.props.output0;
          this.uniforms!.velocity_new.value = fbo_in.texture;
          this.props.output = fbo_out;
          this.uniforms!.dt.value = dt;
          super.update();
        }
        return iterations % 2 === 0 ? this.props.output0 : this.props.output1;
      }
    }

    class Divergence extends ShaderPass {
      constructor(simProps: any) {
        super({
          material: {
            vertexShader: face_vert,
            fragmentShader: divergence_frag,
            uniforms: {
              boundarySpace: { value: simProps.boundarySpace },
              velocity: { value: simProps.src.texture },
              px: { value: simProps.cellScale },
              dt: { value: simProps.dt }
            }
          },
          output: simProps.dst
        });
        this.init();
      }
      update(args: any) {
        if (this.uniforms) this.uniforms.velocity.value = args.vel.texture;
        super.update();
      }
    }

    class Poisson extends ShaderPass {
      constructor(simProps: any) {
        super({
          material: {
            vertexShader: face_vert,
            fragmentShader: poisson_frag,
            uniforms: {
              boundarySpace: { value: simProps.boundarySpace },
              pressure: { value: simProps.dst_.texture },
              divergence: { value: simProps.src.texture },
              px: { value: simProps.cellScale }
            }
          },
          output: simProps.dst,
          output0: simProps.dst_,
          output1: simProps.dst
        });
        this.init();
      }
      update(args: any) {
        const { iterations } = args;
        for (let i = 0; i < iterations; i++) {
          const p_in = i % 2 === 0 ? this.props.output0 : this.props.output1;
          const p_out = i % 2 === 0 ? this.props.output1 : this.props.output0;
          this.uniforms!.pressure.value = p_in.texture;
          this.props.output = p_out;
          super.update();
        }
        return iterations % 2 === 0 ? this.props.output0 : this.props.output1;
      }
    }

    class Pressure extends ShaderPass {
      constructor(simProps: any) {
        super({
          material: {
            vertexShader: face_vert,
            fragmentShader: pressure_frag,
            uniforms: {
              boundarySpace: { value: simProps.boundarySpace },
              pressure: { value: simProps.src_p.texture },
              velocity: { value: simProps.src_v.texture },
              px: { value: simProps.cellScale },
              dt: { value: simProps.dt }
            }
          },
          output: simProps.dst
        });
        this.init();
      }
      update(args: any) {
        this.uniforms!.velocity.value = args.vel.texture;
        this.uniforms!.pressure.value = args.pressure.texture;
        super.update();
      }
    }

    class Simulation {
      options: SimOptions;
      fbos: Record<string, THREE.WebGLRenderTarget | null> = {
        vel_0: null, vel_1: null, vel_viscous0: null, vel_viscous1: null,
        div: null, pressure_0: null, pressure_1: null
      };
      fboSize = new THREE.Vector2();
      cellScale = new THREE.Vector2();
      boundarySpace = new THREE.Vector2();
      advection!: Advection; externalForce!: ExternalForce; viscous!: Viscous;
      divergence!: Divergence; poisson!: Poisson; pressure!: Pressure;

      constructor(options?: Partial<SimOptions>) {
        this.options = {
          iterations_poisson: 32, iterations_viscous: 32, mouse_force: 20,
          resolution: 0.5, cursor_size: 100, viscous: 30, isBounce: false,
          dt: 0.014, isViscous: false, BFECC: true, ...options
        };
        this.init();
      }
      init() { this.calcSize(); this.createAllFBO(); this.createShaderPass(); }
      getFloatType() { return /(iPad|iPhone|iPod)/i.test(navigator.userAgent) ? THREE.HalfFloatType : THREE.FloatType; }
      createAllFBO() {
        const type = this.getFloatType();
        const opts = { type, depthBuffer: false, stencilBuffer: false, minFilter: THREE.LinearFilter, magFilter: THREE.LinearFilter, wrapS: THREE.ClampToEdgeWrapping, wrapT: THREE.ClampToEdgeWrapping };
        for (const key in this.fbos) this.fbos[key] = new THREE.WebGLRenderTarget(this.fboSize.x, this.fboSize.y, opts);
      }
      createShaderPass() {
        this.advection = new Advection({ cellScale: this.cellScale, fboSize: this.fboSize, dt: this.options.dt, src: this.fbos.vel_0, dst: this.fbos.vel_1 });
        this.externalForce = new ExternalForce({ cellScale: this.cellScale, cursor_size: this.options.cursor_size, dst: this.fbos.vel_1 });
        this.viscous = new Viscous({ cellScale: this.cellScale, boundarySpace: this.boundarySpace, viscous: this.options.viscous, src: this.fbos.vel_1, dst: this.fbos.vel_viscous1, dst_: this.fbos.vel_viscous0, dt: this.options.dt });
        this.divergence = new Divergence({ cellScale: this.cellScale, boundarySpace: this.boundarySpace, src: this.fbos.vel_viscous0, dst: this.fbos.div, dt: this.options.dt });
        this.poisson = new Poisson({ cellScale: this.cellScale, boundarySpace: this.boundarySpace, src: this.fbos.div, dst: this.fbos.pressure_1, dst_: this.fbos.pressure_0 });
        this.pressure = new Pressure({ cellScale: this.cellScale, boundarySpace: this.boundarySpace, src_p: this.fbos.pressure_0, src_v: this.fbos.vel_viscous0, dst: this.fbos.vel_0, dt: this.options.dt });
      }
      calcSize() {
        const w = Math.max(1, Math.round(this.options.resolution * Common.width));
        const h = Math.max(1, Math.round(this.options.resolution * Common.height));
        this.cellScale.set(1 / w, 1 / h); this.fboSize.set(w, h);
      }
      resize() { this.calcSize(); for (const key in this.fbos) this.fbos[key]!.setSize(this.fboSize.x, this.fboSize.y); }
      update() {
        this.boundarySpace.copy(this.options.isBounce ? new THREE.Vector2(0,0) : this.cellScale);
        this.advection.update({ dt: this.options.dt, isBounce: this.options.isBounce, BFECC: this.options.BFECC });
        this.externalForce.update({ cursor_size: this.options.cursor_size, mouse_force: this.options.mouse_force, cellScale: this.cellScale });
        let vel = this.fbos.vel_1;
        if (this.options.isViscous) vel = this.viscous.update({ iterations: this.options.iterations_viscous, dt: this.options.dt });
        this.divergence.update({ vel });
        const pressure = this.poisson.update({ iterations: this.options.iterations_poisson });
        this.pressure.update({ vel, pressure });
      }
    }

    class Output {
      simulation: Simulation; scene: THREE.Scene; camera: THREE.Camera; output: THREE.Mesh;
      constructor() {
        this.simulation = new Simulation();
        this.scene = new THREE.Scene(); this.camera = new THREE.Camera();
        this.output = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), new THREE.RawShaderMaterial({
          vertexShader: face_vert, fragmentShader: color_frag, transparent: true, depthWrite: false,
          uniforms: { velocity: { value: this.simulation.fbos.vel_0!.texture }, boundarySpace: { value: new THREE.Vector2() }, palette: { value: paletteTex }, bgColor: { value: bgVec4 } }
        }));
        this.scene.add(this.output);
      }
      resize() { this.simulation.resize(); }
      render() { if (Common.renderer) { Common.renderer.setRenderTarget(null); Common.renderer.render(this.scene, this.camera); } }
      update() { this.simulation.update(); this.render(); }
    }

    class WebGLManager implements LiquidEtherWebGL {
      props: any; output!: Output; autoDriver?: AutoDriver; lastUserInteraction = performance.now(); running = false;
      private _loop = this.loop.bind(this); private _resize = this.resize.bind(this); private _onVisibility?: () => void;
      constructor(props: any) {
        this.props = props; Common.init(props.$wrapper); Mouse.init(props.$wrapper);
        Mouse.autoIntensity = props.autoIntensity; Mouse.takeoverDuration = props.takeoverDuration;
        Mouse.onInteract = () => { this.lastUserInteraction = performance.now(); if (this.autoDriver) this.autoDriver.forceStop(); };
        this.autoDriver = new AutoDriver(Mouse, this as any, { enabled: props.autoDemo, speed: props.autoSpeed, resumeDelay: props.autoResumeDelay, rampDuration: props.autoRampDuration });
        this.init(); window.addEventListener('resize', this._resize);
        this._onVisibility = () => { if (document.hidden) this.pause(); else if (isVisibleRef.current) this.start(); };
        document.addEventListener('visibilitychange', this._onVisibility);
      }
      init() { if (Common.renderer) { this.props.$wrapper.prepend(Common.renderer.domElement); this.output = new Output(); } }
      resize() { Common.resize(); this.output.resize(); }
      render() { if (this.autoDriver) this.autoDriver.update(); Mouse.update(); Common.update(); this.output.update(); }
      loop() { if (this.running) { this.render(); rafRef.current = requestAnimationFrame(this._loop); } }
      start() { if (!this.running) { this.running = true; this._loop(); } }
      pause() { this.running = false; if (rafRef.current) cancelAnimationFrame(rafRef.current); rafRef.current = null; }
      dispose() {
        window.removeEventListener('resize', this._resize); if (this._onVisibility) document.removeEventListener('visibilitychange', this._onVisibility);
        Mouse.dispose(); if (Common.renderer) { const canvas = Common.renderer.domElement; if (canvas.parentNode) canvas.parentNode.removeChild(canvas); Common.renderer.dispose(); }
      }
    }

    const webgl = new WebGLManager({ $wrapper: mountRef.current, autoDemo, autoSpeed, autoIntensity, takeoverDuration, autoResumeDelay, autoRampDuration });
    webglRef.current = webgl;
    webgl.start();

    const io = new IntersectionObserver(entries => {
      const isVisible = entries[0].isIntersecting;
      isVisibleRef.current = isVisible;
      if (webglRef.current) isVisible && !document.hidden ? webglRef.current.start() : webglRef.current.pause();
    }, { threshold: 0.1 });
    io.observe(mountRef.current);
    intersectionObserverRef.current = io;

    const ro = new ResizeObserver(() => {
      if (resizeRafRef.current) cancelAnimationFrame(resizeRafRef.current);
      resizeRafRef.current = requestAnimationFrame(() => webglRef.current?.resize());
    });
    ro.observe(mountRef.current);
    resizeObserverRef.current = ro;

    return () => {
      if (rafRef.current) cancelAnimationFrame(rafRef.current);
      resizeObserverRef.current?.disconnect();
      intersectionObserverRef.current?.disconnect();
      webglRef.current?.dispose();
      webglRef.current = null;
    };
  }, [colors, autoDemo, autoSpeed, autoIntensity, takeoverDuration, autoResumeDelay, autoRampDuration]);

  return (
    <div
      ref={mountRef}
      className={`w-full h-full relative overflow-hidden pointer-events-none touch-none ${className}`}
      style={style}
    />
  );
}

export default LiquidEther;
~~~

Implementation Guidelines

1. Analyze the component structure, styling, animation implementations
2. Review the component's arguments and state
3. Think through what is the best place to adopt this component/style into the design we are doing
4. Then adopt the component/design to our current system

Help me integrate this into my design
```

**▶ Try it live → [https://superdesign.dev/library/liquid-ether-background](https://superdesign.dev/library/liquid-ether-background)**

*444 copies · 1,725 tries · tags: background, animation*
