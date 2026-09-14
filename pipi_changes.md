# Rub Changes Log

This document tracks custom modifications made to the ai-toolkit codebase.

---

## Change 1: Limit Sample Image Display Width During Training

**Date:** 2025-01-XX  
**Author:** rub  
**Component:** UI - Sample Images Viewer  
**File Modified:** `ui/src/components/SampleImages.tsx`

### Problem
When training with few samples per iteration (e.g., only 2 prompts), the images were displayed at excessive sizes, filling the entire screen width. This made them unnecessarily large and wasted screen space.

**Example:** On a 1920px wide container with 2 samples per row:
- Each image was ~958px wide (too large)
- Images stretched across most of the screen

### Solution
Added a maximum width constraint to the sample grid container, limiting it to **900px** and centering it within the parent.

### Code Change
```diff
// ui/src/components/SampleImages.tsx

- <div className="grid gap-1 pb-1" style={{ gridTemplateColumns: `repeat(${gridCols}, minmax(0, 1fr))` }}>
+ <div 
+   className="grid gap-1 pb-1 mx-auto" 
+   style={{
+     gridTemplateColumns: `repeat(${gridCols}, minmax(0, 1fr))`,
+     maxWidth: '900px', // Limit total row width so images don't get too large
+   }}>
```

### Changes Explained
| Addition | Purpose |
|----------|--------|
| `mx-auto` class | Centers the grid horizontally when it's smaller than the container |
| `maxWidth: '900px'` | Limits total width of the sample row to 900px |

### Result
With the same setup (2 samples per row, wide screen):
- Grid max width = **900px** (centered)
- Each image ≈ **448px** wide (reasonable size)
- Images no longer stretch excessively on wide screens

### Visual Comparison

**Before:** With 2 samples per row on a 1920px screen
```
┌─────────────────────────────────────────────────────┐
│  ████████████████████  ████████████████████         │ ← Each ~958px!
│       Image 1            Image 2                    │    (too big!)
└─────────────────────────────────────────────────────┘
```

**After:** Same setup, but grid is now maxed at 900px and centered
```
┌─────────────────────────────────────────────────────┐
│              ┌─────────┬─────────┐                  │ ← Each ~448px
│              │ Img 1   │ Img 2   │                  │    (reasonable)
│              └─────────┴─────────┘                  │
└─────────────────────────────────────────────────────┘
```

### Tuning Guide
To adjust the maximum width, modify the `maxWidth` value:

| Max Width | Per-Image Width (2 samples) | Use Case |
|-----------|----------------------------|----------|
| 600px | ~298px | Compact view |
| **900px** | **~448px** | **Current/recommended** |
| 1200px | ~598px | Larger previews |

### Per-Row Examples with Current Settings (900px max)

| Samples/Row | Each Image Width | Appearance |
|-------------|------------------|------------|
| 2 | ~448px | Large, detailed view |
| 3 | ~298px | Medium size |
| 4 | ~224px | Thumbnail size |
| 6 | ~149px | Small previews |

### Verification
After rebuilding the UI (`npm run build`), verify by:
1. Starting a training job with few samples (e.g., 2 prompts)
2. Checking that images don't exceed reasonable width on screen
3. Confirming grid is centered when fewer columns are displayed