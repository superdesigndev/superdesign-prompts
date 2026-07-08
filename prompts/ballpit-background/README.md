---
title: "Ballpit Background"
slug: ballpit-background
tags: ["animation", "background"]
copyCount: 199
tryCount: 2337
source: https://superdesign.dev/library/ballpit-background
---

# Ballpit Background

A high-performance 3D physics-based background effect with interactive bouncing spheres. Features a custom shader for scattering effects, Three.js instanced rendering for performance, and responsive physics. Inspired by Kevin Levron's creative coding work.

Source: ReactBits

![Ballpit Background](./preview.mp4)

## Prompt

```text
You are given a task to integrate an existing React component in the codebase

~~~/README.md
# BallpitBackground

A high-performance interactive 3D background featuring physics-based spheres that react to gravity, friction, and user pointer movements.

## Features
- **3D Physics**: Real-time sphere-to-sphere and sphere-to-wall collisions.
- **Instanced Rendering**: Optimized for high performance even with hundreds of objects.
- **Interactive**: Spheres follow or react to the user's cursor/touch.
- **Custom Shaders**: Enhanced physical material for subsurface scattering-like visuals.
- **Responsive**: Automatically adjusts physics boundaries to container size.

## Dependencies
- `three`: ^0.170.0
- `gsap`: ^3.12.5
- `lucide-react`: ^0.454.0

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `count` | `number` | `200` | Number of spheres to render. |
| `colors` | `string[]` | `['#ffffff', '#888888', '#444444']` | Array of colors for the spheres. |
| `gravity` | `number` | `0.5` | Strength of the downward pull. |
| `friction` | `number` | `0.9975` | Velocity decay factor (1 = no friction). |
| `wallBounce` | `number` | `0.95` | Energy conservation factor on wall hit. |
| `followCursor` | `boolean` | `true` | Whether a lead sphere should track the pointer. |
| `minSize` | `number` | `0.5` | Minimum radius of spheres. |
| `maxSize` | `number` | `1.0` | Maximum radius of spheres. |
| `lightIntensity` | `number` | `200` | Intensity of the interactive point light. |

## Usage

```tsx
import { BallpitBackground } from '@/sd-components/6f929b17-114f-4ebe-9b32-6443ea884cd2';

function Example() {
  return (
    <div className="h-screen w-full">
      <BallpitBackground 
        count={100}
        gravity={0.3}
        colors={['#ff0000', '#00ff00', '#0000ff']}
      />
    </div>
  );
}
```
~~~

~~~/src/App.tsx
import React, { useState } from 'react';
import { BallpitBackground } from './Component';
import { RefreshCcw } from 'lucide-react';

/**
 * App Demo
 * Showcases the BallpitBackground component in a minimalist environment.
 * Includes a "Reply/Reset" button as requested.
 */
export default function App() {
  const [resetKey, setResetKey] = useState(0);

  const handleReset = () => {
    setResetKey(prev => prev + 1);
  };

  return (
    <div className="relative w-full h-screen bg-[#F9F9F9] flex items-center justify-center p-20">
      {/* Premium Floating Container */}
      <div className="relative w-full h-full bg-white rounded-[40px] overflow-hidden shadow-[0_40px_100px_rgba(0,0,0,0.05)] border-none">
        
        {/* The Background Component */}
        <BallpitBackground 
          key={resetKey}
          count={150}
          colors={['#1A1A1B', '#3B82F6', '#94A3B8']}
          gravity={0.4}
          friction={0.998}
          followCursor={true}
        />

        {/* Minimalist Overlay */}
        <div className="absolute inset-0 pointer-events-none flex flex-col items-center justify-center">
          <h1 className="text-[#1A1A1B] text-4xl font-medium tracking-tight mb-2 opacity-80">
            Ballpit Background
          </h1>
          <p className="text-[#94A3B8] text-sm tracking-wide uppercase font-normal opacity-60">
            3D Physics Interaction
          </p>
        </div>

        {/* Reply/Action Button */}
        <button 
          onClick={handleReset}
          className="absolute bottom-10 right-10 p-4 bg-[#1A1A1B] text-white rounded-full shadow-lg hover:scale-105 transition-transform active:scale-95 flex items-center justify-center group"
          aria-label="Reset Animation"
        >
          <RefreshCcw className="w-5 h-5 group-active:rotate-180 transition-transform duration-500" />
        </button>
      </div>
    </div>
  );
}
~~~

~~~/package.json
{
  "name": "ballpit-background",
  "description": "Interactive 3D physics-based background with bouncing spheres.",
  "dependencies": {
    "three": "^0.170.0",
    "gsap": "^3.12.5",
    "lucide-react": "^0.454.0",
    "framer-motion": "^11.11.11",
    "clsx": "^2.1.1",
    "tailwind-merge": "^2.5.4"
  }
}
~~~

~~~/src/Component.tsx
/**
 * BallpitBackground Component
 * 
 * A high-performance 3D background featuring interactive spheres that react to gravity,
 * friction, and user interaction. Uses Three.js InstancedMesh for rendering efficiency
 * and a custom physical material for advanced lighting effects.
 */

import React, { useRef, useEffect, useMemo } from 'react';
import * as THREE from 'three';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';
import { gsap } from 'gsap';
import { Observer } from 'gsap/Observer';

gsap.registerPlugin(Observer);

// --- Custom Material for Subsurface Scattering-like effect ---
class PhysicalScatteringMaterial extends THREE.MeshPhysicalMaterial {
  uniforms: { [key: string]: { value: any } } = {
    thicknessDistortion: { value: 0.1 },
    thicknessAmbient: { value: 0 },
    thicknessAttenuation: { value: 0.1 },
    thicknessPower: { value: 2 },
    thicknessScale: { value: 10 }
  };

  constructor(params: THREE.MeshPhysicalMaterialParameters) {
    super(params);
    this.defines = { USE_UV: '' };
    this.onBeforeCompile = (shader) => {
      Object.assign(shader.uniforms, this.uniforms);
      shader.fragmentShader = `
        uniform float thicknessPower;
        uniform float thicknessScale;
        uniform float thicknessDistortion;
        uniform float thicknessAmbient;
        uniform float thicknessAttenuation;
        ${shader.fragmentShader}
      `;
      
      shader.fragmentShader = shader.fragmentShader.replace(
        'void main() {',
        `
        void RE_Direct_Scattering(const in IncidentLight directLight, const in vec2 uv, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, inout ReflectedLight reflectedLight) {
          vec3 scatteringHalf = normalize(directLight.direction + (geometryNormal * thicknessDistortion));
          float scatteringDot = pow(saturate(dot(geometryViewDir, -scatteringHalf)), thicknessPower) * thicknessScale;
          #ifdef USE_COLOR
            vec3 scatteringIllu = (scatteringDot + thicknessAmbient) * vColor;
          #else
            vec3 scatteringIllu = (scatteringDot + thicknessAmbient) * diffuse;
          #endif
          reflectedLight.directDiffuse += scatteringIllu * thicknessAttenuation * directLight.color;
        }
        void main() {
        `
      );

      const lightsChunk = THREE.ShaderChunk.lights_fragment_begin.replaceAll(
        'RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );',
        `
          RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
          RE_Direct_Scattering(directLight, vUv, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, reflectedLight);
        `
      );
      shader.fragmentShader = shader.fragmentShader.replace('#include <lights_fragment_begin>', lightsChunk);
    };
  }
}

// --- Physics Engine ---
class PhysicsWorld {
  config: BallpitProps;
  positionData: Float32Array;
  velocityData: Float32Array;
  sizeData: Float32Array;
  center: THREE.Vector3 = new THREE.Vector3();

  constructor(config: BallpitProps) {
    this.config = config;
    const count = config.count || 200;
    this.positionData = new Float32Array(3 * count).fill(0);
    this.velocityData = new Float32Array(3 * count).fill(0);
    this.sizeData = new Float32Array(count).fill(1);
    this.initialize();
  }

  initialize() {
    const count = this.config.count || 200;
    const maxX = this.config.maxX || 5;
    const maxY = this.config.maxY || 5;
    const maxZ = this.config.maxZ || 2;
    const minSize = this.config.minSize || 0.5;
    const maxSize = this.config.maxSize || 1;

    for (let i = 0; i < count; i++) {
      const idx = 3 * i;
      this.positionData[idx] = THREE.MathUtils.randFloatSpread(2 * maxX);
      this.positionData[idx + 1] = THREE.MathUtils.randFloatSpread(2 * maxY);
      this.positionData[idx + 2] = THREE.MathUtils.randFloatSpread(2 * maxZ);
      this.sizeData[i] = THREE.MathUtils.randFloat(minSize, maxSize);
    }
  }

  update(delta: number) {
    const count = this.config.count || 200;
    const gravity = this.config.gravity ?? 0.5;
    const friction = this.config.friction ?? 0.9975;
    const wallBounce = this.config.wallBounce ?? 0.95;
    const maxVelocity = this.config.maxVelocity ?? 0.15;
    const maxX = this.config.maxX || 5;
    const maxY = this.config.maxY || 5;
    const maxZ = this.config.maxZ || 2;
    const followCursor = this.config.followCursor ?? true;

    // First sphere (index 0) is the "follower" if enabled
    let startIdx = 0;
    if (followCursor) {
      startIdx = 1;
      const firstPos = new THREE.Vector3().fromArray(this.positionData, 0);
      firstPos.lerp(this.center, 0.1).toArray(this.positionData, 0);
      new THREE.Vector3(0, 0, 0).toArray(this.velocityData, 0);
    }

    for (let i = startIdx; i < count; i++) {
      const base = 3 * i;
      const pos = new THREE.Vector3().fromArray(this.positionData, base);
      const vel = new THREE.Vector3().fromArray(this.velocityData, base);
      const radius = this.sizeData[i];

      // Gravity & Velocity
      vel.y -= delta * gravity * radius;
      vel.multiplyScalar(friction);
      vel.clampLength(0, maxVelocity);
      pos.add(vel);

      // Collisions with other spheres (simplified)
      for (let j = i + 1; j < count; j++) {
        const otherBase = 3 * j;
        const otherPos = new THREE.Vector3().fromArray(this.positionData, otherBase);
        const diff = new THREE.Vector3().copy(otherPos).sub(pos);
        const dist = diff.length();
        const sumRadius = radius + this.sizeData[j];

        if (dist < sumRadius) {
          const overlap = sumRadius - dist;
          const correction = diff.normalize().multiplyScalar(0.5 * overlap);
          pos.sub(correction);
          otherPos.add(correction);
          
          // Simple impulse transfer
          const relVel = new THREE.Vector3().fromArray(this.velocityData, otherBase).sub(vel);
          const impulse = correction.clone().multiplyScalar(relVel.dot(correction.normalize()));
          vel.add(impulse);
          
          otherPos.toArray(this.positionData, otherBase);
        }
      }

      // Special interaction with follower sphere
      if (followCursor) {
        const followerPos = new THREE.Vector3().fromArray(this.positionData, 0);
        const diff = new THREE.Vector3().copy(followerPos).sub(pos);
        const d = diff.length();
        const sumRadius = radius + this.sizeData[0];
        if (d < sumRadius) {
          const correction = diff.normalize().multiplyScalar(sumRadius - d);
          pos.sub(correction);
          vel.sub(correction.multiplyScalar(0.2));
        }
      }

      // Boundary Collisions
      if (Math.abs(pos.x) + radius > maxX) {
        pos.x = Math.sign(pos.x) * (maxX - radius);
        vel.x *= -wallBounce;
      }
      if (pos.y - radius < -maxY) {
        pos.y = -maxY + radius;
        vel.y *= -wallBounce;
      } else if (gravity === 0 && pos.y + radius > maxY) {
         pos.y = maxY - radius;
         vel.y *= -wallBounce;
      }
      if (Math.abs(pos.z) + radius > maxZ) {
        pos.z = Math.sign(pos.z) * (maxZ - radius);
        vel.z *= -wallBounce;
      }

      pos.toArray(this.positionData, base);
      vel.toArray(this.velocityData, base);
    }
  }
}

// --- Main Component ---
export interface BallpitProps {
  count?: number;
  colors?: string[];
  ambientColor?: string;
  ambientIntensity?: number;
  lightIntensity?: number;
  minSize?: number;
  maxSize?: number;
  gravity?: number;
  friction?: number;
  wallBounce?: number;
  maxVelocity?: number;
  maxX?: number;
  maxY?: number;
  maxZ?: number;
  followCursor?: boolean;
  className?: string;
}

export const BallpitBackground: React.FC<BallpitProps> = ({
  count = 200,
  colors = ['#ffffff', '#888888', '#444444'],
  ambientColor = '#ffffff',
  ambientIntensity = 1,
  lightIntensity = 200,
  minSize = 0.5,
  maxSize = 1,
  gravity = 0.5,
  friction = 0.9975,
  wallBounce = 0.95,
  maxVelocity = 0.15,
  followCursor = true,
  className = ""
}) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  
  useEffect(() => {
    if (!canvasRef.current || !containerRef.current) return;

    const canvas = canvasRef.current;
    const parent = containerRef.current;
    
    // Setup Renderer
    const renderer = new THREE.WebGLRenderer({
      canvas,
      antialias: true,
      alpha: true,
      powerPreference: 'high-performance'
    });
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // Scene & Environment
    const scene = new THREE.Scene();
    const roomEnv = new RoomEnvironment();
    const pmrem = new THREE.PMREMGenerator(renderer);
    const envTexture = pmrem.fromScene(roomEnv).texture;

    // Camera
    const camera = new THREE.PerspectiveCamera(35, 1, 0.1, 1000);
    camera.position.z = 20;

    // Geometry & Material
    const geometry = new THREE.SphereGeometry(1, 32, 32);
    const material = new PhysicalScatteringMaterial({
      envMap: envTexture,
      metalness: 0.5,
      roughness: 0.5,
      clearcoat: 1,
      clearcoatRoughness: 0.15
    });

    // Instanced Mesh
    const imesh = new THREE.InstancedMesh(geometry, material, count);
    scene.add(imesh);

    // Lights
    const ambient = new THREE.AmbientLight(ambientColor, ambientIntensity);
    scene.add(ambient);

    const pointLight = new THREE.PointLight(colors[0], lightIntensity);
    scene.add(pointLight);

    // Physics
    const config = {
      count, minSize, maxSize, gravity, friction, wallBounce, 
      maxVelocity, followCursor, maxX: 5, maxY: 5, maxZ: 2
    };
    const physics = new PhysicsWorld(config);

    // Set Instance Colors
    const threeColors = colors.map(c => new THREE.Color(c));
    for (let i = 0; i < count; i++) {
      const color = threeColors[i % threeColors.length];
      imesh.setColorAt(i, color);
    }
    imesh.instanceColor!.needsUpdate = true;

    // Raycasting for Interaction
    const raycaster = new THREE.Raycaster();
    const plane = new THREE.Plane(new THREE.Vector3(0, 0, 1), 0);
    const intersection = new THREE.Vector3();
    const pointer = new THREE.Vector2();

    const updatePointer = (e: MouseEvent | TouchEvent) => {
      const x = 'touches' in e ? e.touches[0].clientX : e.clientX;
      const y = 'touches' in e ? e.touches[0].clientY : e.clientY;
      const rect = canvas.getBoundingClientRect();
      pointer.x = ((x - rect.left) / rect.width) * 2 - 1;
      pointer.y = -((y - rect.top) / rect.height) * 2 + 1;
      
      raycaster.setFromCamera(pointer, camera);
      raycaster.ray.intersectPlane(plane, intersection);
      physics.center.copy(intersection);
    };

    window.addEventListener('mousemove', updatePointer);
    window.addEventListener('touchstart', updatePointer);
    window.addEventListener('touchmove', updatePointer);

    // Resize Logic
    const resize = () => {
      const w = parent.offsetWidth;
      const h = parent.offsetHeight;
      renderer.setSize(w, h);
      camera.aspect = w / h;
      camera.updateProjectionMatrix();

      // Update World Boundaries
      const fovRad = (camera.fov * Math.PI) / 180;
      const wHeight = 2 * Math.tan(fovRad / 2) * camera.position.z;
      const wWidth = wHeight * camera.aspect;
      physics.config.maxX = wWidth / 2;
      physics.config.maxY = wHeight / 2;
    };
    
    const resizeObserver = new ResizeObserver(resize);
    resizeObserver.observe(parent);
    resize();

    // Animation Loop
    let animationFrameId: number;
    const clock = new THREE.Clock();
    const dummy = new THREE.Object3D();

    const animate = () => {
      const delta = clock.getDelta();
      physics.update(Math.min(delta, 0.1));

      for (let i = 0; i < count; i++) {
        dummy.position.fromArray(physics.positionData, i * 3);
        const s = physics.sizeData[i];
        
        // Hide follower if not needed
        if (i === 0 && !followCursor) {
          dummy.scale.setScalar(0);
        } else {
          dummy.scale.setScalar(s);
        }
        
        dummy.updateMatrix();
        imesh.setMatrixAt(i, dummy.matrix);
        
        if (i === 0) pointLight.position.copy(dummy.position);
      }
      imesh.instanceMatrix.needsUpdate = true;

      renderer.render(scene, camera);
      animationFrameId = requestAnimationFrame(animate);
    };
    animate();

    return () => {
      window.removeEventListener('mousemove', updatePointer);
      window.removeEventListener('touchstart', updatePointer);
      window.removeEventListener('touchmove', updatePointer);
      resizeObserver.disconnect();
      cancelAnimationFrame(animationFrameId);
      renderer.dispose();
      geometry.dispose();
      material.dispose();
      pmrem.dispose();
      roomEnv.dispose();
    };
  }, [count, colors, ambientColor, ambientIntensity, lightIntensity, minSize, maxSize, gravity, friction, wallBounce, maxVelocity, followCursor]);

  return (
    <div ref={containerRef} className={`relative w-full h-full overflow-hidden ${className}`}>
      <canvas ref={canvasRef} className="block w-full h-full outline-none" />
    </div>
  );
};

export default BallpitBackground;
~~~

Implementation Guidelines

1. Analyze the component structure, styling, animation implementations
2. Review the component's arguments and state
3. Think through what is the best place to adopt this component/style into the design we are doing
4. Then adopt the component/design to our current system

Help me integrate this into my design
```

**▶ Try it live → [https://superdesign.dev/library/ballpit-background](https://superdesign.dev/library/ballpit-background)**

*199 copies · 2,337 tries · tags: animation, background*
