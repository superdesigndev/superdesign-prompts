---
title: "Bottom Tab Navigation \u2014 Core App Shell"
slug: "bottom-tab-navigation-core-app-shell"
category: "Mobile Apps"
industry: "General"
tags: ["mobile app", "navigation", "layout"]
copyCount: 1
tryCount: 2356
author: "Shirley Lou"
try_url: "https://superdesign.dev/library/bottom-tab-navigation-core-app-shell?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library"
---

# Bottom Tab Navigation — Core App Shell

A stable bottom tab navigation system where each tab represents a top-level destination with its own navigation stack. The tab bar persists across primary screens, creating a predictable and scalable app shell.

Best Suitable For
Consumer apps, SaaS tools, marketplaces, content platforms, fintech dashboards.

<img src="preview.png" alt="Bottom Tab Navigation — Core App Shell" width="640">

## Prompt

```text
Here is a reference implementation:

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Interactive Wireframe Navigation</title>
  <meta name="description" content="An interactive wireframe for a mobile app with navigation and primary action states.">
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>
  <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
  <link href="https://api.fontshare.com/v2/css?f[]=manrope@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Manrope', sans-serif;
      -webkit-tap-highlight-color: transparent;
    }
    .no-scrollbar::-webkit-scrollbar {
      display: none;
    }
    .no-scrollbar {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }
    [x-cloak] { display: none !important; }
  </style>
</head>
<body x-data="{ activeTab: 'browse', activeFilter: 0, isCreating: false, searchFocused: false }">
  <div class="w-full h-screen flex flex-col bg-white overflow-hidden text-gray-900 relative">
    
    <!-- Safe Area / Header -->
    <header class="pt-14 px-6 pb-4 flex items-center justify-between bg-white/95 backdrop-blur-md z-30 sticky top-0">
      <div class="flex flex-col">
        <div class="h-1 w-8 bg-gray-900 rounded-full mb-1 transition-all duration-300" :class="searchFocused ? 'opacity-0' : 'opacity-100'"></div>
        <h1 class="text-2xl font-extrabold tracking-tight capitalize transition-all" x-text="activeTab">Browse</h1>
      </div>
      <button id="profile-btn" class="h-10 w-10 rounded-full bg-gray-100 border border-gray-200 flex items-center justify-center overflow-hidden hover:bg-gray-200 active:scale-90 transition-all">
        <iconify-icon icon="lucide:user" class="text-gray-400 text-xl"></iconify-icon>
      </button>
    </header>

    <!-- Main Content Area (Scrollable) -->
    <main class="flex-1 overflow-y-auto no-scrollbar px-6 pb-32">
      
      <!-- Search Wireframe -->
      <div class="mt-2 mb-8 relative">
        <div class="h-12 w-full bg-gray-50 border transition-all duration-300 rounded-xl flex items-center px-4 gap-3"
             :class="searchFocused ? 'border-gray-900 ring-4 ring-gray-900/5 bg-white' : 'border-gray-200'">
          <iconify-icon icon="lucide:search" class="transition-colors duration-300" :class="searchFocused ? 'text-gray-900' : 'text-gray-400'"></iconify-icon>
          <input type="text" 
                 @focus="searchFocused = true" 
                 @blur="searchFocused = false" 
                 placeholder="Search everything..."
                 class="w-full bg-transparent border-none focus:ring-0 text-sm font-medium placeholder-gray-400 text-gray-900 outline-none">
        </div>
      </div>

      <!-- Filter Tabs -->
      <div class="flex gap-3 overflow-x-auto pb-6 no-scrollbar">
        <template x-for="(filter, index) in ['Featured', 'Recent', 'Following', 'Saved']">
          <button @click="activeFilter = index" 
                  :class="activeFilter === index ? 'bg-gray-900 text-white' : 'border border-gray-200 text-gray-400 hover:border-gray-300'"
                  class="shrink-0 h-9 px-6 rounded-full flex items-center transition-all active:scale-95">
            <span class="text-xs font-bold tracking-wide" x-text="filter"></span>
          </button>
        </template>
      </div>

      <!-- Masonry Grid Content -->
      <div class="grid grid-cols-2 gap-4">
        <!-- Column 1 -->
        <div class="flex flex-col gap-4">
          <div class="aspect-[4/5] w-full bg-gray-100 rounded-2xl p-4 flex flex-col justify-end border border-transparent hover:border-gray-200 active:scale-[0.98] transition-all cursor-pointer group">
            <div class="h-3 w-3/4 bg-gray-300 rounded-sm mb-2 group-hover:bg-gray-400 transition-colors"></div>
            <div class="h-2 w-1/2 bg-gray-200 rounded-sm"></div>
          </div>
          <div class="aspect-[1/1] w-full bg-gray-100 rounded-2xl p-4 flex flex-col justify-end border border-transparent hover:border-gray-200 active:scale-[0.98] transition-all cursor-pointer group">
            <div class="h-3 w-2/3 bg-gray-300 rounded-sm mb-2 group-hover:bg-gray-400 transition-colors"></div>
            <div class="h-2 w-1/3 bg-gray-200 rounded-sm"></div>
          </div>
        </div>
        
        <!-- Column 2 -->
        <div class="flex flex-col gap-4">
          <div class="aspect-[3/4] w-full bg-gray-100 rounded-2xl p-4 flex flex-col justify-end border border-transparent hover:border-gray-200 active:scale-[0.98] transition-all cursor-pointer group">
            <div class="h-3 w-full bg-gray-300 rounded-sm mb-2 group-hover:bg-gray-400 transition-colors"></div>
            <div class="h-2 w-2/3 bg-gray-200 rounded-sm"></div>
          </div>
          <div class="aspect-[4/5] w-full bg-gray-100 rounded-2xl p-4 flex flex-col justify-end border border-transparent hover:border-gray-200 active:scale-[0.98] transition-all cursor-pointer group">
            <div class="h-3 w-1/2 bg-gray-300 rounded-sm mb-2 group-hover:bg-gray-400 transition-colors"></div>
            <div class="h-2 w-1/2 bg-gray-200 rounded-sm"></div>
          </div>
        </div>
      </div>
    </main>

    <!-- Primary Action Overlay -->
    <div x-show="isCreating" 
         x-cloak
         x-transition:enter="transition ease-out duration-300" 
         x-transition:enter-start="opacity-0" 
         x-transition:enter-end="opacity-100" 
         x-transition:leave="transition ease-in duration-200" 
         x-transition:leave-start="opacity-100" 
         x-transition:leave-end="opacity-0" 
         class="fixed inset-0 z-40 bg-white/80 backdrop-blur-xl flex flex-col items-center justify-center gap-12 p-10">
      <div class="flex flex-col items-center gap-4">
        <h2 class="text-4xl font-extrabold text-gray-900 tracking-tight">Create</h2>
        <p class="text-gray-400 text-center font-medium px-4">Start a new project or capture a quick thought.</p>
      </div>
      <div class="grid grid-cols-2 gap-6 w-full">
        <button class="flex flex-col items-center gap-4 p-6 bg-gray-50 border border-gray-100 rounded-3xl active:scale-95 transition-all">
          <iconify-icon icon="lucide:camera" class="text-3xl text-gray-900"></iconify-icon>
          <span class="text-xs font-bold text-gray-900">Photo</span>
        </button>
        <button class="flex flex-col items-center gap-4 p-6 bg-gray-50 border border-gray-100 rounded-3xl active:scale-95 transition-all">
          <iconify-icon icon="lucide:type" class="text-3xl text-gray-900"></iconify-icon>
          <span class="text-xs font-bold text-gray-900">Post</span>
        </button>
        <button class="flex flex-col items-center gap-4 p-6 bg-gray-50 border border-gray-100 rounded-3xl active:scale-95 transition-all">
          <iconify-icon icon="lucide:mic" class="text-3xl text-gray-900"></iconify-icon>
          <span class="text-xs font-bold text-gray-900">Audio</span>
        </button>
        <button class="flex flex-col items-center gap-4 p-6 bg-gray-50 border border-gray-100 rounded-3xl active:scale-95 transition-all">
          <iconify-icon icon="lucide:link-2" class="text-3xl text-gray-900"></iconify-icon>
          <span class="text-xs font-bold text-gray-900">Link</span>
        </button>
      </div>
      <button @click="isCreating = false" class="mt-8 h-12 px-8 bg-gray-900 text-white rounded-full text-sm font-bold active:scale-95 transition-all shadow-lg shadow-gray-900/10">
        Dismiss
      </button>
    </div>

    <!-- Bottom Navigation Bar -->
    <footer class="absolute bottom-0 w-full pb-[34px] pt-4 px-2 bg-white/95 backdrop-blur-sm border-t border-gray-100 shadow-[0_-10px_30px_rgba(0,0,0,0.03)] z-50">
      <div class="relative flex items-end justify-between px-2">
        
        <!-- Left Group -->
        <div class="flex-1 flex justify-around items-end gap-1">
          <!-- Browse -->
          <button @click="activeTab = 'browse'" id="nav-browse" class="flex flex-col items-center gap-1.5 p-2 w-16 transition-all active:scale-90">
            <iconify-icon :icon="activeTab === 'browse' ? 'lucide:layout-grid' : 'lucide:layout-grid'" 
                          :class="activeTab === 'browse' ? 'text-gray-900' : 'text-gray-300'" 
                          class="text-2xl transition-all"></iconify-icon>
            <span :class="activeTab === 'browse' ? 'text-gray-900 font-bold' : 'text-gray-300 font-medium'" 
                  class="text-[10px] tracking-wide transition-all">Browse</span>
          </button>

          <!-- Profile -->
          <button @click="activeTab = 'profile'" id="nav-profile" class="flex flex-col items-center gap-1.5 p-2 w-16 transition-all active:scale-90">
            <iconify-icon icon="lucide:user" 
                          :class="activeTab === 'profile' ? 'text-gray-900' : 'text-gray-300'" 
                          class="text-2xl transition-all"></iconify-icon>
            <span :class="activeTab === 'profile' ? 'text-gray-900 font-bold' : 'text-gray-300 font-medium'" 
                  class="text-[10px] tracking-wide transition-all">Account</span>
          </button>
        </div>

        <!-- Center Primary Action -->
        <div class="shrink-0 relative -top-6 px-2">
          <button @click="isCreating = !isCreating" 
                  id="btn-create-action" 
                  class="h-[72px] w-[72px] bg-gray-900 rounded-full flex items-center justify-center shadow-2xl shadow-gray-900/30 active:scale-90 transition-all hover:bg-black group border-4 border-white z-50 relative">
             <iconify-icon icon="lucide:plus" 
                           :class="isCreating ? 'rotate-45' : 'rotate-0'"
                           class="text-4xl text-white transition-transform duration-300"></iconify-icon>
             <span class="sr-only">Create New</span>
          </button>
        </div>

        <!-- Right Group -->
        <div class="flex-1 flex justify-around items-end gap-1">
          <!-- Messages -->
          <button @click="activeTab = 'messages'" id="nav-messages" class="flex flex-col items-center gap-1.5 p-2 w-16 transition-all active:scale-90">
            <iconify-icon icon="lucide:message-square" 
                          :class="activeTab === 'messages' ? 'text-gray-900' : 'text-gray-300'" 
                          class="text-2xl transition-all"></iconify-icon>
            <span :class="activeTab === 'messages' ? 'text-gray-900 font-bold' : 'text-gray-300 font-medium'" 
                  class="text-[10px] tracking-wide transition-all">Chat</span>
          </button>

          <!-- Settings -->
          <button @click="activeTab = 'settings'" id="nav-settings" class="flex flex-col items-center gap-1.5 p-2 w-16 transition-all active:scale-90">
            <iconify-icon icon="lucide:settings-2" 
                          :class="activeTab === 'settings' ? 'text-gray-900' : 'text-gray-300'" 
                          class="text-2xl transition-all"></iconify-icon>
            <span :class="activeTab === 'settings' ? 'text-gray-900 font-bold' : 'text-gray-300 font-medium'" 
                  class="text-[10px] tracking-wide transition-all">Settings</span>
          </button>
        </div>

      </div>
    </footer>

  </div>
</body>
</html>
~~~
```

**▶ Try it live → [https://superdesign.dev/library/bottom-tab-navigation-core-app-shell](https://superdesign.dev/library/bottom-tab-navigation-core-app-shell?utm_source=github&utm_medium=prompt-repo&utm_campaign=prompt-library)**

**Use it in your coding agent:** install the [Superdesign skill](https://github.com/superdesigndev/superdesign-skill), then:

```bash
superdesign get-prompts --slugs "bottom-tab-navigation-core-app-shell" --json
```

*1 copies · 2,356 tries · Mobile Apps · General · mobile app, navigation, layout*
