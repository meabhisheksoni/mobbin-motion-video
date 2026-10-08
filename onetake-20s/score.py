#!/usr/bin/env python3
# onetake · Mobbin 20s Sound Score · The Infinite Flow Filament
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "scripts"))
from sfx_palette import Score, air, glass, wood, sub, bubble, wobble, pan_of
import numpy as np

rng = np.random.default_rng(42)
s = Score(dur=20.0, T60=1.2)
place = s.place

# ── Scene 1: Opening & Tap (0.00 - 2.20s) ──
place(glass(440, 1.4, 0.5), 0.20, 0.12, 0.0, 0.5)

# Tap at 1.20s
place(wood(240, 0.08), 1.20, 0.35, 0.0, 0.2)
place(sub(75, 0.45), 1.20, 0.30, 0.0, 0.25)

# Filament ignites and sprouts at 1.30s
place(air(0.65, 280, 2600, 1.4, 0.35), 1.28, 0.32, -0.2, 0.4, pan_to=0.3)

# ── Scene 2: The Flow Sequence (2.20 - 4.80s) ──
# Screen 1 lands
place(bubble(440, 0.22), 2.18, 0.28, pan_of(580), 0.3)
place(air(0.35, 1200, 300, 1.2), 2.20, 0.18, pan_of(580), 0.3)

# Screen 2 lands
place(bubble(520, 0.22), 2.68, 0.28, pan_of(960), 0.3)
place(air(0.35, 1400, 350, 1.2), 2.70, 0.18, pan_of(960), 0.3)

# Screen 3 lands (Paywall hero)
place(sub(58, 0.8), 3.30, 0.38, pan_of(1340), 0.35)
place(glass(659, 1.2, 0.6), 3.32, 0.22, pan_of(1340), 0.5)

# ── Scene 3: Colossal Wall Pullback (4.80 - 7.60s) ──
# Deep exponential dive out
place(air(0.85, 160, 3200, 1.5, 0.45), 4.80, 0.42, 0.1, 0.45, pan_to=-0.2)
place(sub(48, 1.0), 4.85, 0.40, 0.0, 0.4)

# "600,000+ screens" harmonic chime
place(glass(1046, 1.5, 0.5), 5.30, 0.20, -0.15, 0.6)
place(glass(1318, 1.5, 0.4), 5.32, 0.16, 0.15, 0.6)

# ── Scene 4: Macro UI Inspector (7.60 - 11.20s) ──
# Whip into inspector
place(air(0.55, 3000, 350, 1.5, 0.3), 7.60, 0.38, 0.2, 0.4, pan_to=-0.1)
place(wobble(160, 0.5), 7.90, 0.30, 0.0, 0.3)

# Token badges staggered clicks (micro precision)
place(wood(320, 0.06), 8.00, 0.22, -0.3, 0.15)
place(wood(360, 0.06), 8.14, 0.22, 0.3, 0.15)
place(wood(400, 0.06), 8.28, 0.22, -0.2, 0.15)
place(wood(440, 0.06), 8.42, 0.22, 0.2, 0.15)

# ── Scene 5: Figma Export (11.20 - 14.50s) ──
# Figma click
place(wood(280, 0.08), 11.22, 0.32, 0.0, 0.2)
place(wood(340, 0.07), 11.28, 0.24, 0.0, 0.2)
# Fan out whoosh
place(air(0.45, 600, 2400, 1.3), 11.45, 0.28, -0.2, 0.35, pan_to=0.2)

# ── Scene 6: Staccato Hits (14.50 - 17.50s) ──
# Hit 1: EXPLORE
place(sub(72, 0.45), 14.50, 0.42, -0.15, 0.25)
place(air(0.28, 350, 2800, 1.4), 14.50, 0.35, -0.2, 0.3)

# Hit 2: ANALYZE
place(sub(68, 0.45), 15.40, 0.44, 0.15, 0.25)
place(air(0.28, 450, 3000, 1.4), 15.40, 0.36, 0.2, 0.3)

# Hit 3: SHIP FASTER
place(sub(62, 0.50), 16.30, 0.48, 0.0, 0.25)
place(air(0.32, 550, 3200, 1.4), 16.30, 0.38, 0.0, 0.3)

# ── Scene 7: Brand Anchor Lockup (17.40 - 20.00s) ──
# Deep sub impact
place(sub(46, 1.4), 17.40, 0.58, 0.0, 0.45)
# Pure resonant glass tone
place(glass(523, 2.0, 0.65), 17.42, 0.26, 0.0, 0.65)
place(glass(1046, 2.0, 0.45), 17.45, 0.16, 0.0, 0.65)

out_wav = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sfx.wav")
s.write(out_wav)
print(f"wrote {out_wav}")
