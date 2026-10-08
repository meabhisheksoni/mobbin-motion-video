# Mobbin 20s One Take Motion Video

> **Concept 1: The Infinite Flow Filament**
> A 20-second continuous motion graphics product video for [Mobbin](https://mobbin.com/), built using the [`onetake`](https://github.com/feitangyuan/onetake) motion framework. Every beat grows out of the previous one without slideshow cuts or scene dissolves.

## 🎬 Video & Preview

- **Watch Video**: [`mobbin-20s.mp4`](mobbin-20s.mp4) (1080p @ 30fps, 180° shutter blur, 4.1 MB)
- **Contact Sheet**: [`mobbin-20s-stills.png`](mobbin-20s-stills.png)

![Mobbin 20s Contact Sheet](mobbin-20s-stills.png)

---

## 🎨 Creative Concept & Motion Design

- **The Carrier**: A glowing cobalt-blue connector filament (`#3b82f6`) that acts as the camera's spatial track. It unspools from the initial app icon, guides a 3D camera travel across connected user flow screens, weaves through an infinite wall of 600,000+ screens, locks onto a paywall button in the UI inspector, and resolves into the official Mobbin geometric `M` emblem.
- **Palette**: Obsidian & Electric Cobalt (`#0b0c10` void ground, `#f0f3f6` crisp typography, `#3b82f6` / `#60a5fa` neon accents).
- **Rhythm**: High dynamic cadence with 59.6% stillness/holds for visual clarity, contrasting with 552 px/frame shutter-blurred kinetic whip zooms.
- **Audio**: 32 Foley & synthetic events placed in a shared acoustic space via `sfx_palette.py`, mastered to -7.8 dBFS peak.

---

## 📋 Beat Sheet

| Time | Scene | Description | Carrier |
|---|---|---|---|
| **0.00 – 1.20s** | The Icon Hold | Dead-still macro hold on Obsidian ground (`#0b0c10`). | App Icon |
| **1.20 – 2.20s** | The Spark & Sprout | Click ripple; luminous cobalt filament (`#3b82f6`) ignites and unspools. | Glowing Filament |
| **2.20 – 4.80s** | The User Flow | Camera travels along the rail connecting 3 mobile screens (`01 Welcome` → `02 Choose Artists` → `03 Spotify Paywall`). Settle & hold on the Paywall CTA button (3.40–4.80s). | Filament Node on CTA |
| **4.80 – 7.60s** | 600,000+ Wall Dive | Exponential camera pull-back (`1.15x → 0.16x`), revealing a colossal gallery wall of real-world app flows + bold kinetic type (`600,000+ REAL SCREENS`). | Filament S-curve Wave |
| **7.60 – 11.20s** | Macro UI Inspector | Whip camera dive through the glass (`OM.zoomThrough`). Spring-animated `UIK.glowRing` and 4 design token badges (`border-radius`, `#3B82F6`, `padding`). Dead-still hold (9.20–11.20s). | Inspected UI Button |
| **11.20 – 14.50s** | Copy to Figma | Button triggers Figma click. 3D perspective fan of vector mockups + pill: `Copy Screen Sequence to Figma · Vector Auto-Layout`. | Figma Selection Marquee |
| **14.50 – 17.50s** | Staccato Hits | Snappy kinetic cuts with motion blur: `EXPLORE.` → `ANALYZE.` → `SHIP FASTER.` slashed by the laser line. | Diagonal Slash |
| **17.50 – 20.00s** | Brand Anchor | The filament locks into the official geometric **Mobbin `M` emblem** and `MOBBIN` wordmark, with `mobbin.com` tagline and clean reverb decay. | Official Mobbin Lockup |

---

## 🏆 Acceptance Oracle Verification

```text
draft.mp4 — energy map:
  0.0s |                              . . ... .         |
  4.0s |          . ..:..                            ...|
  8.0s |                                       .        |
 12.0s |                              .          ..     |
 16.0s |    ..            .                             |

  PASS  rest       still 0.596 (longest quiet 3.08 s)
  PASS  audio      peak -7.8 dBFS (0 clipped, 65.8% quiet breathing room)
  PASS  continuity carry score 1.00 (flawless carry across all transitions)
  PASS  curves     peak 552 px/frame @ 30 fps, shutter 180°
VERDICT: PASS
```

---

## 🛠 Files

- `comp.html` — The pure HTML composition driven by `window.__seek(t)`
- `motion.js` — The onetake move library (`window.OM`)
- `ui_kit.js` — Rebuilt UI plane and inspection tools (`window.UIK`)
- `look.js` / `look.json` — Obsidian color and typography tokens
- `score.py` — Sound synthesizer score script
- `sfx.wav` — Rendered 48kHz audio track
