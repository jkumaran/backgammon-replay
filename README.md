# 🎲 Backgammon Match Replay & Animation

An interactive graphical Backgammon Match Replay and Animation viewer for **Table #917860648** (between **`cameronwhale`** and **`-George`**).

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/jkumaran/backgammon-replay)

---

## 🌟 Live Demo & Deployment

- **Live on Render**: [https://backgammon-replay.onrender.com](https://backgammon-replay.onrender.com)
- **Live on GitHub Pages**: [https://jkumaran.github.io/backgammon-replay/](https://jkumaran.github.io/backgammon-replay/)


---

## ✨ Features

- **Authentic Wooden Backgammon Board**:
  - Precision 24-point layout with mahogany wood cabinet frame and brass corner accents.
  - Alternating burgundy and amber pips with drop shadows.
  - Dedicated central **Bar** for hit checkers and **Bear-off trays** for borne-off checkers.
  - 3D tactile marble checkers for both players:
    - **`cameronwhale`**: Radiant Amber Gold (`#f59e0b`).
    - **`-George`**: Emerald Jade (`#10b981`).
  - Dynamic count badges for stacks of 5+ checkers.
- **Smooth Animations & Physics**:
  - Arched 3D flight trajectories when checkers move between points.
  - Expanding red shockwave impact animation when blots get hit.
- **Dynamic Race & Pip Tracking**:
  - Live pip count updates at every turn and sub-step (starts at standard 167 pips).
  - Pip difference lead indicator and race progress bars.
- **3D Animated Dice**:
  - Visual 3D dice faces showing exact rolls (e.g. ⚂ ⚂ ⚂ ⚂ for double 3s or ⚄ ⚂ for 5-3).
- **Interactive Move Log**:
  - Full match transcript of all 27 moves with timestamp, roll, and hit indicators.
  - Click any move to immediately jump to that board state.
- **Built-in Audio Synthesizer**:
  - Procedural sound effects via Web Audio API (dice rattle, checker clacks, hit chime) with no external audio files required.
- **Customizable Controls**:
  - Turn-by-turn and checker-by-checker sub-step navigation.
  - Auto-play slideshow with speeds from `0.5x` to `3x`.
  - Perspective toggle (Cameron 1–24 or George 1–24).
  - Keyboard shortcuts (`Space`, `←`, `→`, `↑`, `↓`, `Home`, `End`, `M`).

---

## 🛠️ Local Development

Simply open `index.html` in any modern web browser:

```bash
open index.html
```

Or run a local HTTP server:

```bash
python3 -m http.server 8000
```
Then visit `http://localhost:8000`.

---

## 📄 License

MIT
