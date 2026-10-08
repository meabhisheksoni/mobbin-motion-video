# Mobbin Motion Graphics Videos

High-end product launch and motion graphics showcase videos created for [Mobbin](https://mobbin.com/).

---

## 🌟 Cut 1: 20s Continuous One Take (`onetake-20s/`)

> Built with the [`onetake`](https://github.com/feitangyuan/onetake) motion framework. Every beat grows out of the previous one with zero slide transitions — guided by an unbroken glowing cobalt filament, shutter-blurred camera tracking, and sound scored to frame events.

- **Watch Video**: [**`onetake-20s/mobbin-20s.mp4`**](onetake-20s/mobbin-20s.mp4) (1080p @ 30fps, 4.1 MB)
- **Contact Sheet**: [**`onetake-20s/mobbin-20s-stills.png`**](onetake-20s/mobbin-20s-stills.png)
- **Full Breakdown & Source Code**: See [**`onetake-20s/README.md`**](onetake-20s/README.md)
- **Oracle Continuity Score**: `1.00` (Passed acceptance oracle)

![Mobbin 20s Contact Sheet](onetake-20s/mobbin-20s-stills.png)

---

## 🎬 Cut 2: 24s Meta Muse-Style Product Video (`Hyperframes`)

> Re-architected to faithfully mirror the [Meta Muse launch film](https://x.com/Muse/status/2097399178376671666/video/1) visual aesthetic: luminous high-key white canvas, pillowy floating cards with diffused shadows, conversational chat prompts, floating status pills, kinetic typography with inline badges, an orbiting tools vortex, and a minimal black outro.

- **Watch Video**: [`brag.mp4`](brag.mp4) (1080p @ 30fps, 3.8 MB, 24.0s)
- **Preview Poster**:

![Mobbin Video Poster](brag.jpg)

### Storyboard Breakdown (24s — Muse Choreography)
1. **Scene 1 (0–3.8s): The Emblem & Grid Reveal** — Centered pillowy Mobbin app emblem zooms out into a 24-app matrix grid, followed by kinetic headline: *"Mobbin is A new kind of inspiration"*.
2. **Scene 2 (3.8–8.2s): Search Pill & Conversational Ask** — Floating search bar `+ "What onboarding flows convert best? ↑"` transforms into conversational iOS chat bubbles with top status pill.
3. **Scene 3 (8.2–13.5s): Pillowy App Window & Flow Teardown** — Floating browser window (`mobbin.com/discover`) with top app rows (Duolingo, Revolut, Linear) smoothly transitioning into verified teardown screens with conversion metrics.
4. **Scene 4 (13.5–17.5s): "Done!" & Kinetic Typography** — Bold *"Done!"* title with status pill morphing into *"Design that is always inspiring you"*.
5. **Scene 5 (17.5–21.8s): Orbiting Connected Ecosystem** — Centered pill `Connect Mobbin to your stack` surrounded by an orbiting vortex of tools (Figma, Cursor, Claude, iOS, Android, Linear, Raycast, React).
6. **Scene 6 (21.8–24.0s): Signature Black Outro** — Clean cut to pure black with white rounded app icon and `mobbin.com` call-to-action.

---

## 📦 Repository Structure

- [`onetake-20s/`](onetake-20s/) — **20s One Take motion film**
  - [`mobbin-20s.mp4`](onetake-20s/mobbin-20s.mp4) — Rendered master video file
  - [`mobbin-20s-stills.png`](onetake-20s/mobbin-20s-stills.png) — Contact sheet stills
  - [`comp.html`](onetake-20s/comp.html) — Deterministic composition source
  - [`score.py`](onetake-20s/score.py) & [`sfx.wav`](onetake-20s/sfx.wav) — 32-event audio score
  - [`README.md`](onetake-20s/README.md) — Beat sheet & continuity report
- [`brag.mp4`](brag.mp4) — 24s Hyperframes teaser
- [`composition/`](composition/) — Hyperframes GSAP timeline composition
- [`brag-plan.md`](brag-plan.md) — Creative storyboard and pacing spec
- [`share-copy.txt`](share-copy.txt) — Ready-to-post social media caption
