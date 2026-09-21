import json

with open('/Users/kumaran/Downloads/backgammon/game_data.json') as f:
    game_data = json.load(f)

json_str = json.dumps(game_data)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Backgammon Match Replay & Animation - Table #917860648</title>
<script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
<style>
  :root {{
    --bg-dark: #090d16;
    --card-bg: #131d2e;
    --border-color: #23354d;
    --cameron-color: #f59e0b;
    --cameron-accent: #fbbf24;
    --george-color: #10b981;
    --george-accent: #34d399;
  }}

  body {{
    background-color: var(--bg-dark);
    color: #e2e8f0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    margin: 0;
    padding: 0;
    min-height: 100vh;
  }}

  /* Custom scrollbars */
  ::-webkit-scrollbar {{
    width: 6px;
    height: 6px;
  }}
  ::-webkit-scrollbar-track {{
    background: #0f172a;
  }}
  ::-webkit-scrollbar-thumb {{
    background: #334155;
    border-radius: 4px;
  }}
  ::-webkit-scrollbar-thumb:hover {{
    background: #475569;
  }}

  /* Checkers & Board Styling */
  .board-container {{
    position: relative;
    width: 100%;
    max-width: 1060px;
    margin: 0 auto;
    user-select: none;
  }}

  .checker-flying {{
    position: absolute;
    pointer-events: none;
    z-index: 50;
    transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1);
  }}

  .hit-ripple {{
    position: absolute;
    border-radius: 50%;
    border: 3px solid #ef4444;
    animation: ripple 0.6s ease-out forwards;
    pointer-events: none;
    z-index: 60;
  }}

  @keyframes ripple {{
    0% {{
      transform: scale(0.6);
      opacity: 1;
    }}
    100% {{
      transform: scale(2.2);
      opacity: 0;
    }}
  }}

  /* 3D Dice styling */
  .dice-face {{
    width: 38px;
    height: 38px;
    background: linear-gradient(135deg, #ffffff, #e2e8f0);
    border-radius: 8px;
    box-shadow: inset 0 1px 2px rgba(255,255,255,0.8), 0 4px 8px rgba(0,0,0,0.4), 0 1px 2px rgba(0,0,0,0.2);
    display: inline-grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(3, 1fr);
    padding: 5px;
    box-sizing: border-box;
    position: relative;
    border: 1px solid #cbd5e1;
    transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
  }}
  .dice-pip {{
    width: 6px;
    height: 6px;
    background: #1e293b;
    border-radius: 50%;
    margin: auto;
    box-shadow: inset 0 1px 1px rgba(0,0,0,0.6);
  }}
  .dice-face.cameron-dice {{
    background: linear-gradient(135deg, #fef3c7, #fde68a);
    border-color: #f59e0b;
  }}
  .dice-face.cameron-dice .dice-pip {{
    background: #92400e;
  }}
  .dice-face.george-dice {{
    background: linear-gradient(135deg, #d1fae5, #a7f3d0);
    border-color: #10b981;
  }}
  .dice-face.george-dice .dice-pip {{
    background: #065f46;
  }}

  /* Custom Range Slider */
  input[type=range] {{
    -webkit-appearance: none;
    background: #1e293b;
    border-radius: 9999px;
    height: 8px;
    outline: none;
    border: 1px solid #334155;
  }}
  input[type=range]::-webkit-slider-thumb {{
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #38bdf8;
    cursor: pointer;
    box-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
    border: 2px solid #ffffff;
    transition: transform 0.1s;
  }}
  input[type=range]::-webkit-slider-thumb:hover {{
    transform: scale(1.2);
  }}

  /* Pulse highlight on points */
  @keyframes pointGlow {{
    0%, 100% {{ opacity: 0.3; }}
    50% {{ opacity: 0.8; }}
  }}
  .point-active-glow {{
    animation: pointGlow 1.2s infinite ease-in-out;
  }}

  /* Badge animations */
  .badge-pop {{
    animation: badgePop 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  }}
  @keyframes badgePop {{
    0% {{ transform: scale(0.7); opacity: 0; }}
    100% {{ transform: scale(1); opacity: 1; }}
  }}
</style>
</head>
<body class="p-3 sm:p-5">

<div class="max-w-[1280px] mx-auto space-y-4">

  <!-- Top Header & Match Status -->
  <header class="bg-[#131d2e] border border-[#23354d] rounded-2xl p-4 sm:p-5 shadow-xl flex flex-wrap items-center justify-between gap-4">
    <div>
      <div class="flex items-center gap-2">
        <span class="text-2xl">🎲</span>
        <h1 class="text-xl sm:text-2xl font-bold bg-gradient-to-r from-amber-400 via-sky-400 to-emerald-400 bg-clip-text text-transparent">
          Backgammon Replay & Animation
        </h1>
        <span class="bg-sky-500/20 text-sky-300 border border-sky-500/40 text-xs px-2.5 py-0.5 rounded-full font-semibold">Interactive</span>
      </div>
      <p class="text-xs sm:text-sm text-slate-400 mt-1 flex items-center gap-3">
        <span>Table #<strong class="text-slate-200">917860648</strong></span>
        <span>•</span>
        <span>Match Progression: <strong class="text-amber-400">59%</strong></span>
        <span>•</span>
        <span>Game Length: <strong class="text-slate-200">27 Moves</strong></span>
      </p>
    </div>

    <!-- Quick Actions / Toggles -->
    <div class="flex items-center flex-wrap gap-2 sm:gap-3">
      <button id="soundToggleBtn" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-medium text-slate-200 transition" title="Toggle audio sound effects">
        <span id="soundIcon">🔊</span> <span id="soundLabel">Sound ON</span>
      </button>

      <button id="perspectiveToggleBtn" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-medium text-slate-200 transition" title="Switch board perspective">
        <span>🔄</span> <span id="perspectiveLabel">Cameron View (1-24)</span>
      </button>

      <button id="logToggleBtn" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-sky-900/40 hover:bg-sky-900/60 border border-sky-700/50 text-xs font-medium text-sky-300 transition">
        <span>📜</span> <span id="logToggleLabel">Hide Log</span>
      </button>
    </div>
  </header>

  <!-- Player Cards & Pip Race Bar -->
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <!-- Cameron Whale Card -->
    <div id="cameronCard" class="bg-[#131d2e] border-2 border-amber-500/30 rounded-2xl p-4 transition-all duration-300 relative overflow-hidden shadow-lg">
      <div class="absolute -right-8 -top-8 w-24 h-24 bg-amber-500/10 rounded-full blur-xl pointer-events-none"></div>
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-amber-600 to-amber-400 flex items-center justify-center text-slate-950 font-bold shadow-md shadow-amber-500/20">
            CW
          </div>
          <div>
            <div class="flex items-center gap-2">
              <h3 class="font-bold text-base sm:text-lg text-amber-400">cameronwhale</h3>
              <span id="cameronTurnBadge" class="hidden text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded-full bg-amber-500 text-slate-950">Active Turn</span>
            </div>
            <div class="text-xs text-slate-400 flex items-center gap-2">
              <span>Home: <strong class="text-slate-300">1–6</strong></span>
              <span>•</span>
              <span>Bar: <strong id="cameronBarCount" class="text-amber-400">0</strong></span>
              <span>•</span>
              <span>Off: <strong id="cameronOffCount" class="text-slate-300">0</strong></span>
            </div>
          </div>
        </div>
        <div class="text-right">
          <div class="text-xs uppercase tracking-wider text-slate-400 font-medium">Pip Count</div>
          <div class="flex items-baseline justify-end gap-1.5">
            <span id="cameronPipCount" class="text-2xl sm:text-3xl font-extrabold text-amber-400">167</span>
            <span id="cameronPipDiff" class="text-xs font-semibold text-slate-400">Tied</span>
          </div>
        </div>
      </div>
      <!-- Pip progress comparison line -->
      <div class="mt-3 w-full bg-slate-800/80 rounded-full h-2 overflow-hidden">
        <div id="cameronPipBar" class="bg-gradient-to-r from-amber-600 to-amber-400 h-full rounded-full transition-all duration-300" style="width: 50%"></div>
      </div>
    </div>

    <!-- George Card -->
    <div id="georgeCard" class="bg-[#131d2e] border-2 border-emerald-500/30 rounded-2xl p-4 transition-all duration-300 relative overflow-hidden shadow-lg">
      <div class="absolute -right-8 -top-8 w-24 h-24 bg-emerald-500/10 rounded-full blur-xl pointer-events-none"></div>
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-emerald-600 to-emerald-400 flex items-center justify-center text-slate-950 font-bold shadow-md shadow-emerald-500/20">
            -G
          </div>
          <div>
            <div class="flex items-center gap-2">
              <h3 class="font-bold text-base sm:text-lg text-emerald-400">-George</h3>
              <span id="georgeTurnBadge" class="hidden text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded-full bg-emerald-500 text-slate-950">Active Turn</span>
            </div>
            <div class="text-xs text-slate-400 flex items-center gap-2">
              <span>Home: <strong class="text-slate-300">19–24 (G: 1-6)</strong></span>
              <span>•</span>
              <span>Bar: <strong id="georgeBarCount" class="text-emerald-400">0</strong></span>
              <span>•</span>
              <span>Off: <strong id="georgeOffCount" class="text-slate-300">0</strong></span>
            </div>
          </div>
        </div>
        <div class="text-right">
          <div class="text-xs uppercase tracking-wider text-slate-400 font-medium">Pip Count</div>
          <div class="flex items-baseline justify-end gap-1.5">
            <span id="georgePipCount" class="text-2xl sm:text-3xl font-extrabold text-emerald-400">167</span>
            <span id="georgePipDiff" class="text-xs font-semibold text-slate-400">Tied</span>
          </div>
        </div>
      </div>
      <!-- Pip progress comparison line -->
      <div class="mt-3 w-full bg-slate-800/80 rounded-full h-2 overflow-hidden">
        <div id="georgePipBar" class="bg-gradient-to-r from-emerald-600 to-emerald-400 h-full rounded-full transition-all duration-300" style="width: 50%"></div>
      </div>
    </div>
  </div>

  <!-- Main Board Area & Log Split View -->
  <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">

    <!-- Backgammon Board & Controls -->
    <div id="boardCol" class="lg:col-span-8 transition-all duration-300 space-y-4">

      <!-- Current Turn Highlight Banner -->
      <div class="bg-[#131d2e] border border-[#23354d] rounded-2xl p-4 shadow-md flex flex-wrap items-center justify-between gap-3">
        <div class="flex items-center gap-3">
          <div class="flex flex-col">
            <span id="moveNumLabel" class="text-xs font-bold text-sky-400 uppercase tracking-widest">Move 1 of 27</span>
            <span id="submoveStepLabel" class="text-[11px] text-slate-400">Step 1 of 2</span>
          </div>
          <div class="h-8 w-px bg-slate-700 hidden sm:block"></div>
          <div id="diceContainer" class="flex items-center gap-1.5">
            <!-- Dynamic Dice rendered here -->
          </div>
        </div>

        <!-- Move description and Badges -->
        <div class="flex items-center gap-2 flex-wrap">
          <div id="moveNotation" class="font-mono text-sm sm:text-base font-semibold bg-slate-900/80 border border-slate-700 px-3 py-1 rounded-lg text-slate-100">
            6 ➡ 3 , 8 ➡ 3
          </div>
          <div id="badgeContainer" class="flex items-center gap-1.5">
            <!-- Dynamic badges (Double!, Hit!) -->
          </div>
          <span id="moveTimestamp" class="text-xs text-slate-400 ml-1">9/19/2026 07:41 AM</span>
        </div>
      </div>

      <!-- Graphical Board SVG Container -->
      <div class="board-container rounded-2xl overflow-hidden shadow-2xl border-4 border-[#3a2012] bg-[#1a0e08]">
        <svg id="boardSvg" viewBox="0 0 1020 660" class="w-full h-auto block select-none">
          <defs>
            <!-- Board Wood Texture & Gradients -->
            <linearGradient id="frameGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#452312" />
              <stop offset="40%" stop-color="#2a150a" />
              <stop offset="100%" stop-color="#190c05" />
            </linearGradient>

            <linearGradient id="woodBevel" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#6e3a1f" />
              <stop offset="100%" stop-color="#1f0e06" />
            </linearGradient>

            <linearGradient id="feltGrad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#172230" />
              <stop offset="50%" stop-color="#0f1724" />
              <stop offset="100%" stop-color="#131c29" />
            </linearGradient>

            <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#1f0e06" />
              <stop offset="50%" stop-color="#3d1e10" />
              <stop offset="100%" stop-color="#1f0e06" />
            </linearGradient>

            <!-- Point Colors -->
            <linearGradient id="pointDarkTop" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#831843" />
              <stop offset="100%" stop-color="#be185d" />
            </linearGradient>
            <linearGradient id="pointDarkBottom" x1="0%" y1="100%" x2="0%" y2="0%">
              <stop offset="0%" stop-color="#831843" />
              <stop offset="100%" stop-color="#be185d" />
            </linearGradient>

            <linearGradient id="pointLightTop" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#d97706" />
              <stop offset="100%" stop-color="#fef08a" />
            </linearGradient>
            <linearGradient id="pointLightBottom" x1="0%" y1="100%" x2="0%" y2="0%">
              <stop offset="0%" stop-color="#d97706" />
              <stop offset="100%" stop-color="#fef08a" />
            </linearGradient>

            <!-- Active Point Highlight -->
            <filter id="glowFilter" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="6" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>

            <!-- Drop Shadows -->
            <filter id="checkerShadow" x="-30%" y="-30%" width="160%" height="160%">
              <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000000" flood-opacity="0.6" />
            </filter>
            
            <filter id="pointShadow" x="-10%" y="-10%" width="120%" height="120%">
              <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.4" />
            </filter>

            <!-- Checker Marble Gradients -->
            <!-- Cameron (Amber Gold) -->
            <radialGradient id="cameronCheckerGrad" cx="35%" cy="30%" r="70%">
              <stop offset="0%" stop-color="#fef08a" />
              <stop offset="35%" stop-color="#f59e0b" />
              <stop offset="85%" stop-color="#b45309" />
              <stop offset="100%" stop-color="#78350f" />
            </radialGradient>

            <!-- George (Emerald Jade) -->
            <radialGradient id="georgeCheckerGrad" cx="35%" cy="30%" r="70%">
              <stop offset="0%" stop-color="#a7f3d0" />
              <stop offset="35%" stop-color="#10b981" />
              <stop offset="85%" stop-color="#047857" />
              <stop offset="100%" stop-color="#064e3b" />
            </radialGradient>

            <!-- Hinges & Brackets -->
            <linearGradient id="brassGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#fef08a" />
              <stop offset="50%" stop-color="#ca8a04" />
              <stop offset="100%" stop-color="#713f12" />
            </linearGradient>
          </defs>

          <!-- Outer Wooden Border -->
          <rect x="0" y="0" width="1020" height="660" rx="14" fill="url(#frameGrad)" />
          <rect x="12" y="12" width="996" height="636" rx="8" fill="none" stroke="url(#woodBevel)" stroke-width="6" />

          <!-- Corner Brass Brackets -->
          <g fill="url(#brassGrad)">
            <path d="M 12 40 L 40 12 L 12 12 Z" />
            <path d="M 1008 40 L 980 12 L 1008 12 Z" />
            <path d="M 12 620 L 40 648 L 12 648 Z" />
            <path d="M 1008 620 L 980 648 L 1008 648 Z" />
          </g>

          <!-- Left Board Felt (Outer Board) -->
          <rect x="36" y="32" width="418" height="596" rx="4" fill="url(#feltGrad)" />
          <rect x="36" y="32" width="418" height="596" rx="4" fill="none" stroke="#000000" stroke-opacity="0.4" stroke-width="2" />

          <!-- Center Bar (Wood / Leather) -->
          <rect x="454" y="32" width="54" height="596" fill="url(#barGrad)" />
          <line x1="454" y1="32" x2="454" y2="628" stroke="#000000" stroke-opacity="0.6" stroke-width="2" />
          <line x1="508" y1="32" x2="508" y2="628" stroke="#000000" stroke-opacity="0.6" stroke-width="2" />

          <!-- Center Bar Hinges -->
          <rect x="466" y="160" width="30" height="14" rx="2" fill="url(#brassGrad)" />
          <circle cx="473" cy="167" r="2" fill="#451a03" />
          <circle cx="489" cy="167" r="2" fill="#451a03" />

          <rect x="466" y="486" width="30" height="14" rx="2" fill="url(#brassGrad)" />
          <circle cx="473" cy="493" r="2" fill="#451a03" />
          <circle cx="489" cy="493" r="2" fill="#451a03" />

          <!-- Center Bar Label -->
          <text x="481" y="335" fill="#ca8a04" font-size="11" font-weight="bold" letter-spacing="4" text-anchor="middle" transform="rotate(-90 481 335)" opacity="0.6">THE BAR</text>

          <!-- Right Board Felt (Home Board) -->
          <rect x="508" y="32" width="418" height="596" rx="4" fill="url(#feltGrad)" />
          <rect x="508" y="32" width="418" height="596" rx="4" fill="none" stroke="#000000" stroke-opacity="0.4" stroke-width="2" />

          <!-- Side Bear-Off Tray (Far Right) -->
          <rect x="934" y="32" width="52" height="596" rx="4" fill="#0d141e" />
          <rect x="934" y="32" width="52" height="596" rx="4" fill="none" stroke="#2a150a" stroke-width="3" />
          <line x1="934" y1="330" x2="986" y2="330" stroke="#2a150a" stroke-width="2" />
          <text x="960" y="180" fill="#64748b" font-size="10" font-weight="bold" letter-spacing="3" text-anchor="middle" transform="rotate(90 960 180)">BEAR OFF</text>
          <text x="960" y="480" fill="#64748b" font-size="10" font-weight="bold" letter-spacing="3" text-anchor="middle" transform="rotate(90 960 480)">BEAR OFF</text>

          <!-- Point Triangles Group -->
          <g id="pointsGroup"></g>

          <!-- Active Highlights Group -->
          <g id="highlightsGroup"></g>

          <!-- Point Numbers Group -->
          <g id="pointLabelsGroup"></g>

          <!-- Checkers Group -->
          <g id="checkersGroup"></g>

          <!-- Animated Flying Checkers Layer -->
          <g id="animLayer"></g>
        </svg>
      </div>

      <!-- Playback Controls Bar -->
      <div class="bg-[#131d2e] border border-[#23354d] rounded-2xl p-4 shadow-xl space-y-3">
        <!-- Controls Buttons & Speed -->
        <div class="flex flex-wrap items-center justify-between gap-3">
          <div class="flex items-center gap-1 sm:gap-2">
            <button id="firstBtn" class="p-2 sm:px-3 sm:py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs sm:text-sm font-semibold transition" title="Go to First Move (Start)">
              ⏮ First
            </button>
            <button id="prevTurnBtn" class="p-2 sm:px-3 sm:py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs sm:text-sm font-semibold transition" title="Previous Turn">
              ◀◀ Turn
            </button>
            <button id="prevStepBtn" class="p-2 sm:px-3 sm:py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs sm:text-sm font-semibold transition" title="Previous Sub-step">
              ◂ Step
            </button>

            <!-- Play / Pause Primary Button -->
            <button id="playBtn" class="px-4 sm:px-6 py-2 rounded-xl bg-gradient-to-r from-sky-500 to-blue-600 hover:from-sky-400 hover:to-blue-500 text-slate-950 font-bold text-sm sm:text-base shadow-lg shadow-sky-500/25 transition transform active:scale-95 flex items-center gap-2">
              <span id="playIcon">▶</span> <span id="playText">Play</span>
            </button>

            <button id="nextStepBtn" class="p-2 sm:px-3 sm:py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs sm:text-sm font-semibold transition" title="Next Sub-step">
              Step ▸
            </button>
            <button id="nextTurnBtn" class="p-2 sm:px-3 sm:py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs sm:text-sm font-semibold transition" title="Next Turn">
              Turn ▶▶
            </button>
            <button id="lastBtn" class="p-2 sm:px-3 sm:py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs sm:text-sm font-semibold transition" title="Go to Last Move">
              Last ⏭
            </button>
          </div>

          <!-- Speed Selectors -->
          <div class="flex items-center gap-1.5 bg-slate-900 border border-slate-800 p-1 rounded-xl text-xs font-semibold">
            <span class="text-slate-400 px-1 text-[11px]">Speed:</span>
            <button class="speed-btn px-2 py-1 rounded-lg text-slate-300 hover:text-white" data-speed="0.5">0.5x</button>
            <button class="speed-btn px-2 py-1 rounded-lg bg-sky-500 text-slate-950 font-bold" data-speed="1">1x</button>
            <button class="speed-btn px-2 py-1 rounded-lg text-slate-300 hover:text-white" data-speed="1.5">1.5x</button>
            <button class="speed-btn px-2 py-1 rounded-lg text-slate-300 hover:text-white" data-speed="2">2x</button>
            <button class="speed-btn px-2 py-1 rounded-lg text-slate-300 hover:text-white" data-speed="3">3x</button>
          </div>
        </div>

        <!-- Scrubber Range Slider -->
        <div class="space-y-1 pt-1">
          <div class="flex items-center justify-between text-xs text-slate-400">
            <span>Start (Move 0)</span>
            <span id="sliderPositionLabel" class="text-sky-400 font-bold">Move 1 / 27</span>
            <span>Final Move (27)</span>
          </div>
          <div class="relative flex items-center">
            <input type="range" id="moveSlider" min="0" max="27" value="1" class="w-full">
          </div>
          <!-- Hit & Double Indicator dots below slider -->
          <div id="sliderTimelineMarkers" class="relative w-full h-3"></div>
        </div>

        <!-- Hotkey hints -->
        <div class="text-[11px] text-slate-500 text-center sm:text-left flex flex-wrap gap-3 pt-1 border-t border-slate-800/80">
          <span><kbd class="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-300">Space</kbd> Play / Pause</span>
          <span><kbd class="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-300">←</kbd> <kbd class="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-300">→</kbd> Step submove</span>
          <span><kbd class="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-300">↑</kbd> <kbd class="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-300">↓</kbd> Jump turn</span>
          <span><kbd class="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-300">M</kbd> Mute/Unmute</span>
        </div>
      </div>
    </div>

    <!-- Move Log & Transcript Sidebar -->
    <div id="logCol" class="lg:col-span-4 bg-[#131d2e] border border-[#23354d] rounded-2xl p-4 shadow-xl flex flex-col h-[650px] lg:h-auto">
      <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div class="flex items-center gap-2">
          <span class="text-base">📋</span>
          <h3 class="font-bold text-slate-200">Match Transcript</h3>
          <span class="bg-slate-800 text-slate-400 text-xs px-2 py-0.5 rounded-full font-mono">27</span>
        </div>
        <div class="flex items-center gap-1 text-xs">
          <button id="filterAllBtn" class="px-2 py-0.5 rounded bg-sky-500/20 text-sky-400 font-semibold border border-sky-500/30">All</button>
          <button id="filterHitsBtn" class="px-2 py-0.5 rounded bg-slate-800 text-slate-400 hover:text-slate-200">Hits Only</button>
        </div>
      </div>

      <!-- Scrollable list of moves -->
      <div id="movesListContainer" class="flex-1 overflow-y-auto divide-y divide-slate-800/80 pr-1 mt-2 space-y-1">
        <!-- Rows populated dynamically -->
      </div>
    </div>

  </div>

  <!-- Legend & Rule Explanations footer -->
  <footer class="bg-[#131d2e] border border-[#23354d] rounded-2xl p-4 text-xs text-slate-400 flex flex-wrap items-center justify-between gap-4">
    <div class="flex items-center flex-wrap gap-4">
      <div class="flex items-center gap-2">
        <span class="w-3.5 h-3.5 rounded-full bg-amber-500 border border-amber-300 inline-block shadow"></span>
        <span><strong>cameronwhale:</strong> Moves counter-clockwise (24 ➡ 1 into Home Board)</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="w-3.5 h-3.5 rounded-full bg-emerald-500 border border-emerald-300 inline-block shadow"></span>
        <span><strong>-George:</strong> Moves clockwise (1 ➡ 24 into Home Board)</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="bg-red-500 text-white font-bold px-1.5 py-0.2 rounded text-[10px]">HIT</span>
        <span>Checker sent to The Bar</span>
      </div>
    </div>
    <div class="text-slate-500">
      Antigravity Backgammon Engine • Complete Match Visualizer
    </div>
  </footer>

</div>

<!-- Audio Synthesizer & Game Engine Script -->
<script>
const GAME_DATA = {json_str};

// Board Coordinate Configuration
// 1020 x 660 viewBox
const CFG = {{
  leftStart: 42,
  rightStart: 514,
  colWidth: 68.33,
  barX: 481, // center of bar
  barWidth: 54,
  trayX: 960, // center of bearoff tray
  checkerRadius: 24,
  topBaseY: 34,
  bottomBaseY: 626,
  triangleHeight: 236,
  stackStep: 42
}};

// Audio Synthesizer (Zero external dependencies)
let audioCtx = null;
let soundEnabled = true;

function getAudioCtx() {{
  if (!audioCtx) {{
    const AC = window.AudioContext || window.webkitAudioContext;
    if (AC) audioCtx = new AC();
  }}
  if (audioCtx && audioCtx.state === 'suspended') {{
    audioCtx.resume();
  }}
  return audioCtx;
}}

function playClack() {{
  if (!soundEnabled) return;
  try {{
    const ctx = getAudioCtx();
    if (!ctx) return;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(160, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(35, ctx.currentTime + 0.05);
    gain.gain.setValueAtTime(0.35, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.05);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.06);
  }} catch(e) {{}}
}}

function playDiceRoll() {{
  if (!soundEnabled) return;
  try {{
    const ctx = getAudioCtx();
    if (!ctx) return;
    for (let i = 0; i < 3; i++) {{
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      const t = ctx.currentTime + i * 0.04;
      osc.frequency.setValueAtTime(320 + Math.random() * 260, t);
      gain.gain.setValueAtTime(0.12, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.035);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(t);
      osc.stop(t + 0.04);
    }}
  }} catch(e) {{}}
}}

function playHitSound() {{
  if (!soundEnabled) return;
  try {{
    const ctx = getAudioCtx();
    if (!ctx) return;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(300, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(700, ctx.currentTime + 0.12);
    gain.gain.setValueAtTime(0.3, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.14);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.15);
  }} catch(e) {{}}
}}

// Game State Management
let currentTurnIndex = 1; // 1 to 27, 0 = start
let currentSubmoveIndex = -1; // -1 means show full turn state, 0..k-1 means show specific submove
let isPlaying = false;
let playTimer = null;
let playSpeed = 1.0;
let perspective = 'cameron'; // 'cameron' or 'george'
let filterHitsOnly = false;
let activeAnimId = null;

// Helpers to get point (X, Y)
function getPointGeometry(p) {{
  let colIndex = 0;
  let isTop = (p >= 13);
  let isRight = (p <= 6 || p >= 19);

  if (p >= 1 && p <= 6) {{
    colIndex = 6 - p;
  }} else if (p >= 7 && p <= 12) {{
    colIndex = 12 - p;
  }} else if (p >= 13 && p <= 18) {{
    colIndex = p - 13;
  }} else if (p >= 19 && p <= 24) {{
    colIndex = p - 19;
  }}

  const baseX = isRight ? CFG.rightStart : CFG.leftStart;
  const centerX = baseX + colIndex * CFG.colWidth + CFG.colWidth / 2;
  const leftX = baseX + colIndex * CFG.colWidth;
  const rightX = leftX + CFG.colWidth;

  return {{
    point: p,
    isTop: isTop,
    isRight: isRight,
    centerX: centerX,
    leftX: leftX,
    rightX: rightX,
    baseY: isTop ? CFG.topBaseY : CFG.bottomBaseY,
    tipY: isTop ? (CFG.topBaseY + CFG.triangleHeight) : (CFG.bottomBaseY - CFG.triangleHeight)
  }};
}}

// Get position for checker at index `k` on point `p`
function getCheckerPosition(p, k, totalCount) {{
  if (p === 'bar_c') {{
    return {{
      x: CFG.barX,
      y: 420 + k * 32
    }};
  }}
  if (p === 'bar_g') {{
    return {{
      x: CFG.barX,
      y: 240 - k * 32
    }};
  }}
  if (p === 'off_c') {{
    return {{
      x: CFG.trayX,
      y: 560 - k * 18
    }};
  }}
  if (p === 'off_g') {{
    return {{
      x: CFG.trayX,
      y: 100 + k * 18
    }};
  }}

  const geom = getPointGeometry(p);
  const step = totalCount > 5 ? Math.min(38, (CFG.triangleHeight - 35) / totalCount) : CFG.stackStep;

  if (geom.isTop) {{
    return {{
      x: geom.centerX,
      y: CFG.topBaseY + 28 + k * step
    }};
  }} else {{
    return {{
      x: geom.centerX,
      y: CFG.bottomBaseY - 28 - k * step
    }};
  }}
}}

// Build Static Board Points & Triangles
function buildBoardSvg() {{
  const pointsGroup = document.getElementById('pointsGroup');
  const labelsGroup = document.getElementById('pointLabelsGroup');
  pointsGroup.innerHTML = '';
  labelsGroup.innerHTML = '';

  for (let p = 1; p <= 24; p++) {{
    const g = getPointGeometry(p);

    const isDark = (p % 2 === 1);
    const fillUrl = g.isTop 
      ? (isDark ? 'url(#pointDarkTop)' : 'url(#pointLightTop)')
      : (isDark ? 'url(#pointDarkBottom)' : 'url(#pointLightBottom)');

    const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    poly.setAttribute('points', `${{g.leftX}},${{g.baseY}} ${{g.rightX}},${{g.baseY}} ${{g.centerX}},${{g.tipY}}`);
    poly.setAttribute('fill', fillUrl);
    poly.setAttribute('filter', 'url(#pointShadow)');
    poly.setAttribute('id', `point-poly-${{p}}`);
    pointsGroup.appendChild(poly);

    const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    text.setAttribute('x', g.centerX);
    text.setAttribute('y', g.isTop ? (g.baseY - 7) : (g.baseY + 18));
    text.setAttribute('text-anchor', 'middle');
    text.setAttribute('font-size', '12');
    text.setAttribute('font-weight', 'bold');
    text.setAttribute('fill', '#94a3b8');
    text.setAttribute('id', `point-label-${{p}}`);
    labelsGroup.appendChild(text);
  }}
}}

// Update Point Labels based on perspective
function updatePointLabels() {{
  for (let p = 1; p <= 24; p++) {{
    const label = document.getElementById(`point-label-${{p}}`);
    if (!label) continue;
    if (perspective === 'cameron') {{
      label.textContent = p;
    }} else {{
      label.textContent = (25 - p);
    }}
  }}
  document.getElementById('perspectiveLabel').textContent = 
    perspective === 'cameron' ? 'Cameron View (1-24)' : 'George View (1-24)';
}}

// Render current board checkers
function renderCheckers(state, activeHighlightFrom = null, activeHighlightTo = null) {{
  if (!state) return;
  const checkersGroup = document.getElementById('checkersGroup');
  const highlightsGroup = document.getElementById('highlightsGroup');
  checkersGroup.innerHTML = '';
  highlightsGroup.innerHTML = '';

  // Render point highlights if any
  [activeHighlightFrom, activeHighlightTo].forEach((pt, idx) => {{
    if (typeof pt === 'number' && pt >= 1 && pt <= 24) {{
      const g = getPointGeometry(pt);
      const glowPoly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
      glowPoly.setAttribute('points', `${{g.leftX}},${{g.baseY}} ${{g.rightX}},${{g.baseY}} ${{g.centerX}},${{g.tipY}}`);
      glowPoly.setAttribute('fill', idx === 0 ? 'rgba(56, 189, 248, 0.4)' : 'rgba(245, 158, 11, 0.4)');
      glowPoly.setAttribute('stroke', idx === 0 ? '#38bdf8' : '#f59e0b');
      glowPoly.setAttribute('stroke-width', '3');
      glowPoly.setAttribute('filter', 'url(#glowFilter)');
      glowPoly.setAttribute('class', 'point-active-glow');
      highlightsGroup.appendChild(glowPoly);
    }}
  }});

  // Render Checkers on Points 1..24
  for (let p = 1; p <= 24; p++) {{
    const camCount = (state.cameron_board && (state.cameron_board[p] ?? state.cameron_board[String(p)])) || 0;
    const geoCount = (state.george_board && (state.george_board[p] ?? state.george_board[String(p)])) || 0;
    const count = Math.max(camCount, geoCount);
    const player = camCount > 0 ? 'cameron' : (geoCount > 0 ? 'george' : null);

    if (count > 0 && player) {{
      for (let k = 0; k < count; k++) {{
        const pos = getCheckerPosition(p, k, count);
        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('cx', pos.x);
        circle.setAttribute('cy', pos.y);
        circle.setAttribute('r', CFG.checkerRadius);
        circle.setAttribute('fill', player === 'cameron' ? 'url(#cameronCheckerGrad)' : 'url(#georgeCheckerGrad)');
        circle.setAttribute('stroke', player === 'cameron' ? '#fbbf24' : '#34d399');
        circle.setAttribute('stroke-width', '1.5');
        circle.setAttribute('filter', 'url(#checkerShadow)');
        checkersGroup.appendChild(circle);

        const ring = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        ring.setAttribute('cx', pos.x);
        ring.setAttribute('cy', pos.y);
        ring.setAttribute('r', CFG.checkerRadius - 7);
        ring.setAttribute('fill', 'none');
        ring.setAttribute('stroke', player === 'cameron' ? 'rgba(254, 240, 138, 0.4)' : 'rgba(167, 243, 208, 0.4)');
        ring.setAttribute('stroke-width', '1.5');
        checkersGroup.appendChild(ring);

        if (k === count - 1 && count >= 5) {{
          const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          txt.setAttribute('x', pos.x);
          txt.setAttribute('y', pos.y + 5);
          txt.setAttribute('text-anchor', 'middle');
          txt.setAttribute('font-size', '14');
          txt.setAttribute('font-weight', 'bold');
          txt.setAttribute('fill', '#ffffff');
          txt.setAttribute('filter', 'drop-shadow(0 1px 2px rgba(0,0,0,0.8))');
          txt.textContent = count;
          checkersGroup.appendChild(txt);
        }}
      }}
    }}
  }}

  // Render Cameron Checkers on Bar
  const camBar = state.cameron_bar || 0;
  if (camBar > 0) {{
    for (let k = 0; k < camBar; k++) {{
      const pos = getCheckerPosition('bar_c', k, camBar);
      const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      circle.setAttribute('cx', pos.x);
      circle.setAttribute('cy', pos.y);
      circle.setAttribute('r', CFG.checkerRadius);
      circle.setAttribute('fill', 'url(#cameronCheckerGrad)');
      circle.setAttribute('stroke', '#ef4444');
      circle.setAttribute('stroke-width', '2');
      circle.setAttribute('filter', 'url(#checkerShadow)');
      checkersGroup.appendChild(circle);

      const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      txt.setAttribute('x', pos.x);
      txt.setAttribute('y', pos.y + 4);
      txt.setAttribute('text-anchor', 'middle');
      txt.setAttribute('font-size', '11');
      txt.setAttribute('font-weight', 'bold');
      txt.setAttribute('fill', '#ffffff');
      txt.textContent = 'BAR';
      checkersGroup.appendChild(txt);
    }}
  }}

  // Render George Checkers on Bar
  const geoBar = state.george_bar || 0;
  if (geoBar > 0) {{
    for (let k = 0; k < geoBar; k++) {{
      const pos = getCheckerPosition('bar_g', k, geoBar);
      const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      circle.setAttribute('cx', pos.x);
      circle.setAttribute('cy', pos.y);
      circle.setAttribute('r', CFG.checkerRadius);
      circle.setAttribute('fill', 'url(#georgeCheckerGrad)');
      circle.setAttribute('stroke', '#ef4444');
      circle.setAttribute('stroke-width', '2');
      circle.setAttribute('filter', 'url(#checkerShadow)');
      checkersGroup.appendChild(circle);

      const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      txt.setAttribute('x', pos.x);
      txt.setAttribute('y', pos.y + 4);
      txt.setAttribute('text-anchor', 'middle');
      txt.setAttribute('font-size', '11');
      txt.setAttribute('font-weight', 'bold');
      txt.setAttribute('fill', '#ffffff');
      txt.textContent = 'BAR';
      checkersGroup.appendChild(txt);
    }}
  }}
}}

// Generate HTML for 3D Dice Face
function createDiceElement(val, player) {{
  const div = document.createElement('div');
  div.className = `dice-face ${{player === 'cameronwhale' ? 'cameron-dice' : 'george-dice'}}`;
  div.title = `Rolled ${{val}}`;

  const pipMap = {{
    1: [4],
    2: [0, 8],
    3: [0, 4, 8],
    4: [0, 2, 6, 8],
    5: [0, 2, 4, 6, 8],
    6: [0, 2, 3, 5, 6, 8]
  }};

  const pips = pipMap[val] || [4];
  for (let i = 0; i < 9; i++) {{
    const cell = document.createElement('div');
    if (pips.includes(i)) {{
      const dot = document.createElement('div');
      dot.className = 'dice-pip';
      cell.appendChild(dot);
    }}
    div.appendChild(cell);
  }}
  return div;
}}

// Update Top Info & Cards
function updateInfo(turnIdx, subIdx = -1) {{
  const turn = GAME_DATA.turns[turnIdx - 1];
  const state = (turnIdx === 0) 
    ? GAME_DATA.initial_state 
    : (subIdx >= 0 ? turn.submoves[subIdx].state_after : turn.state_after);

  if (!state) return;

  // Update Move Count Label
  document.getElementById('moveNumLabel').textContent = 
    turnIdx === 0 ? 'Initial Board Position' : `Move ${{turnIdx}} of ${{GAME_DATA.turns.length}}`;

  if (turnIdx === 0) {{
    document.getElementById('submoveStepLabel').textContent = 'Match Start';
    document.getElementById('moveNotation').textContent = 'Initial Setup';
    document.getElementById('diceContainer').innerHTML = '';
    document.getElementById('badgeContainer').innerHTML = '';
    document.getElementById('moveTimestamp').textContent = 'Ready';
    document.getElementById('cameronTurnBadge').classList.add('hidden');
    document.getElementById('georgeTurnBadge').classList.add('hidden');
  }} else {{
    const totalSubs = turn.submoves.length;
    if (subIdx >= 0) {{
      document.getElementById('submoveStepLabel').textContent = `Checker Step ${{subIdx + 1}} of ${{totalSubs}}`;
      document.getElementById('moveNotation').textContent = turn.submoves[subIdx].text;
    }} else {{
      document.getElementById('submoveStepLabel').textContent = `${{totalSubs}} checker movements`;
      document.getElementById('moveNotation').textContent = turn.desc;
    }}

    const diceCont = document.getElementById('diceContainer');
    diceCont.innerHTML = '';
    turn.dice.forEach(d => {{
      diceCont.appendChild(createDiceElement(d, turn.player));
    }});

    const badgeCont = document.getElementById('badgeContainer');
    let bHtml = '';
    if (turn.is_double) {{
      bHtml += '<span class="bg-purple-600/90 text-white font-bold text-xs px-2.5 py-1 rounded-md shadow badge-pop">Double!</span> ';
    }}
    if (turn.has_hit) {{
      bHtml += '<span class="bg-red-600/90 text-white font-bold text-xs px-2.5 py-1 rounded-md shadow badge-pop">Checker Hit!</span>';
    }}
    badgeCont.innerHTML = bHtml;

    document.getElementById('moveTimestamp').textContent = turn.time;

    if (turn.player === 'cameronwhale') {{
      document.getElementById('cameronCard').classList.add('border-amber-500', 'ring-2', 'ring-amber-400/50');
      document.getElementById('georgeCard').classList.remove('border-emerald-500', 'ring-2', 'ring-emerald-400/50');
      document.getElementById('cameronTurnBadge').classList.remove('hidden');
      document.getElementById('georgeTurnBadge').classList.add('hidden');
    }} else {{
      document.getElementById('georgeCard').classList.add('border-emerald-500', 'ring-2', 'ring-emerald-400/50');
      document.getElementById('cameronCard').classList.remove('border-amber-500', 'ring-2', 'ring-amber-400/50');
      document.getElementById('georgeTurnBadge').classList.remove('hidden');
      document.getElementById('cameronTurnBadge').classList.add('hidden');
    }}
  }}

  // Player Stats Update
  document.getElementById('cameronPipCount').textContent = state.cameron_pips;
  document.getElementById('georgePipCount').textContent = state.george_pips;
  document.getElementById('cameronBarCount').textContent = state.cameron_bar;
  document.getElementById('georgeBarCount').textContent = state.george_bar;
  document.getElementById('cameronOffCount').textContent = state.cameron_off;
  document.getElementById('georgeOffCount').textContent = state.george_off;

  const diff = state.cameron_pips - state.george_pips;
  const camDiffEl = document.getElementById('cameronPipDiff');
  const geoDiffEl = document.getElementById('georgePipDiff');

  if (diff < 0) {{
    camDiffEl.textContent = `Lead by ${{-diff}}`;
    camDiffEl.className = 'text-xs font-bold text-amber-400';
    geoDiffEl.textContent = `Behind ${{-diff}}`;
    geoDiffEl.className = 'text-xs font-semibold text-slate-500';
  }} else if (diff > 0) {{
    camDiffEl.textContent = `Behind ${{diff}}`;
    camDiffEl.className = 'text-xs font-semibold text-slate-500';
    geoDiffEl.textContent = `Lead by ${{diff}}`;
    geoDiffEl.className = 'text-xs font-bold text-emerald-400';
  }} else {{
    camDiffEl.textContent = 'Tied';
    camDiffEl.className = 'text-xs font-semibold text-slate-400';
    geoDiffEl.textContent = 'Tied';
    geoDiffEl.className = 'text-xs font-semibold text-slate-400';
  }}

  const totalPips = state.cameron_pips + state.george_pips;
  if (totalPips > 0) {{
    const camPct = Math.round((1 - (state.cameron_pips / 334)) * 100);
    const geoPct = Math.round((1 - (state.george_pips / 334)) * 100);
    document.getElementById('cameronPipBar').style.width = `${{camPct}}%`;
    document.getElementById('georgePipBar').style.width = `${{geoPct}}%`;
  }}

  document.getElementById('moveSlider').value = turnIdx;
  document.getElementById('sliderPositionLabel').textContent = `Move ${{turnIdx}} / ${{GAME_DATA.turns.length}}`;

  document.getElementById('prevTurnBtn').disabled = (turnIdx === 0 && subIdx <= 0);
  document.getElementById('firstBtn').disabled = (turnIdx === 0 && subIdx <= 0);
  document.getElementById('nextTurnBtn').disabled = (turnIdx === GAME_DATA.turns.length && subIdx === -1);
  document.getElementById('lastBtn').disabled = (turnIdx === GAME_DATA.turns.length && subIdx === -1);

  highlightTranscriptRow(turnIdx);
}}

function highlightTranscriptRow(idx) {{
  document.querySelectorAll('.transcript-row').forEach(row => {{
    row.classList.remove('bg-sky-950/60', 'border-sky-500/80', 'ring-1', 'ring-sky-500');
  }});
  if (idx > 0) {{
    const activeRow = document.getElementById(`row-move-${{idx}}`);
    if (activeRow) {{
      activeRow.classList.add('bg-sky-950/60', 'border-sky-500/80', 'ring-1', 'ring-sky-500');
      
      // When in play mode: completely ignore position of current step and keep window at the top
      if (!isPlaying) {{
        const container = document.getElementById('movesListContainer');
        if (container) {{
          const rowOffset = activeRow.offsetTop;
          const containerH = container.clientHeight;
          const rowH = activeRow.clientHeight;
          // Scroll ONLY the internal container, never the browser window
          container.scrollTo({{
            top: rowOffset - (containerH / 2) + (rowH / 2),
            behavior: 'smooth'
          }});
        }}
      }}
    }}
  }}
}}

// Animate a Single Submove
function animateSubmove(submove, onComplete) {{
  if (activeAnimId) {{
    cancelAnimationFrame(activeAnimId);
    activeAnimId = null;
  }}

  const animLayer = document.getElementById('animLayer');
  animLayer.innerHTML = '';

  const stateBefore = submove.state_before;
  const stateAfter = submove.state_after;
  const fromAbs = submove.from_abs;
  const toAbs = submove.to_abs;
  const turnObj = GAME_DATA.turns[currentTurnIndex - 1];
  const player = (turnObj && turnObj.player === 'cameronwhale') ? 'cameron' : 'george';

  // Lift moving checker from origin during flight
  const boardDuringFlight = JSON.parse(JSON.stringify(stateBefore));
  if (typeof fromAbs === 'number') {{
    const k = String(fromAbs);
    if (player === 'cameron' && boardDuringFlight.cameron_board[k] > 0) boardDuringFlight.cameron_board[k]--;
    else if (player === 'george' && boardDuringFlight.george_board[k] > 0) boardDuringFlight.george_board[k]--;
  }} else if (fromAbs === 'bar_c' && boardDuringFlight.cameron_bar > 0) {{
    boardDuringFlight.cameron_bar--;
  }} else if (fromAbs === 'bar_g' && boardDuringFlight.george_bar > 0) {{
    boardDuringFlight.george_bar--;
  }}
  renderCheckers(boardDuringFlight, fromAbs, toAbs);

  // Source Coordinates
  let countAtFrom = 1;
  if (typeof fromAbs === 'number') {{
    const k = String(fromAbs);
    countAtFrom = (player === 'cameron' ? stateBefore.cameron_board[k] : stateBefore.george_board[k]) || 1;
  }}
  const startPos = getCheckerPosition(fromAbs, countAtFrom - 1, countAtFrom);

  // Target Coordinates
  let countAtTo = 0;
  if (typeof toAbs === 'number') {{
    const k = String(toAbs);
    countAtTo = (player === 'cameron' ? stateBefore.cameron_board[k] : stateBefore.george_board[k]) || 0;
  }}
  const endPos = getCheckerPosition(toAbs, countAtTo, countAtTo + 1);

  // Create Animated Checker SVG Element
  const flyingCircle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  flyingCircle.setAttribute('cx', startPos.x);
  flyingCircle.setAttribute('cy', startPos.y);
  flyingCircle.setAttribute('r', CFG.checkerRadius);
  flyingCircle.setAttribute('fill', player === 'cameron' ? 'url(#cameronCheckerGrad)' : 'url(#georgeCheckerGrad)');
  flyingCircle.setAttribute('stroke', '#ffffff');
  flyingCircle.setAttribute('stroke-width', '2.5');
  flyingCircle.setAttribute('filter', 'url(#checkerShadow)');
  animLayer.appendChild(flyingCircle);

  // Inner ring
  const ring = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  ring.setAttribute('cx', startPos.x);
  ring.setAttribute('cy', startPos.y);
  ring.setAttribute('r', CFG.checkerRadius - 7);
  ring.setAttribute('fill', 'none');
  ring.setAttribute('stroke', 'rgba(255, 255, 255, 0.6)');
  ring.setAttribute('stroke-width', '1.5');
  animLayer.appendChild(ring);

  const duration = Math.max(180, 420 / playSpeed);
  const startTime = performance.now();

  function stepAnim(now) {{
    const elapsed = now - startTime;
    const progress = Math.min(1, elapsed / duration);
    const ease = progress < 0.5 
      ? 4 * progress * progress * progress 
      : 1 - Math.pow(-2 * progress + 2, 3) / 2;

    const curX = startPos.x + (endPos.x - startPos.x) * ease;
    const archY = Math.sin(progress * Math.PI) * -65;
    const curY = startPos.y + (endPos.y - startPos.y) * ease + archY;

    flyingCircle.setAttribute('cx', curX);
    flyingCircle.setAttribute('cy', curY);
    ring.setAttribute('cx', curX);
    ring.setAttribute('cy', curY);

    if (progress < 1) {{
      activeAnimId = requestAnimationFrame(stepAnim);
    }} else {{
      activeAnimId = null;
      animLayer.innerHTML = '';
      playClack();

      if (submove.hit) {{
        playHitSound();
        const hitShock = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        hitShock.setAttribute('cx', endPos.x);
        hitShock.setAttribute('cy', endPos.y);
        hitShock.setAttribute('r', CFG.checkerRadius + 4);
        hitShock.setAttribute('fill', 'none');
        hitShock.setAttribute('stroke', '#ef4444');
        hitShock.setAttribute('stroke-width', '4');
        hitShock.setAttribute('class', 'point-active-glow');
        animLayer.appendChild(hitShock);

        setTimeout(() => {{
          if (!activeAnimId) animLayer.innerHTML = '';
        }}, 300);
      }}

      // Render the true resulting state
      renderCheckers(stateAfter, fromAbs, toAbs);
      if (onComplete) onComplete();
    }}
  }}

  activeAnimId = requestAnimationFrame(stepAnim);
}}

// Jump to a specific Turn
function goToTurn(turnIdx, animate = false, onComplete = null) {{
  if (activeAnimId) {{
    cancelAnimationFrame(activeAnimId);
    activeAnimId = null;
  }}
  const animLayer = document.getElementById('animLayer');
  if (animLayer) animLayer.innerHTML = '';

  if (turnIdx < 0) turnIdx = 0;
  if (turnIdx > GAME_DATA.turns.length) turnIdx = GAME_DATA.turns.length;

  currentTurnIndex = turnIdx;
  currentSubmoveIndex = -1;

  if (turnIdx === 0) {{
    renderCheckers(GAME_DATA.initial_state);
    updateInfo(0);
    if (onComplete) onComplete();
    return;
  }}

  const turn = GAME_DATA.turns[turnIdx - 1];

  if (!animate) {{
    renderCheckers(turn.state_after);
    updateInfo(turnIdx);
    if (onComplete) onComplete();
  }} else {{
    // Animate turn's submoves in sequence
    playDiceRoll();
    let subI = 0;
    function nextSub() {{
      if (!isPlaying && onComplete) {{
        // If playback was stopped during turn
        renderCheckers(turn.state_after);
        updateInfo(turnIdx);
        return;
      }}

      if (subI < turn.submoves.length) {{
        currentSubmoveIndex = subI;
        updateInfo(turnIdx, subI);
        animateSubmove(turn.submoves[subI], () => {{
          subI++;
          if (subI < turn.submoves.length) {{
            setTimeout(nextSub, 180 / playSpeed);
          }} else {{
            currentSubmoveIndex = -1;
            updateInfo(turnIdx);
            if (onComplete) onComplete();
          }}
        }});
      }} else {{
        currentSubmoveIndex = -1;
        updateInfo(turnIdx);
        if (onComplete) onComplete();
      }}
    }}
    nextSub();
  }}
}}

// Step forward 1 submove
function stepForward() {{
  stopPlay();

  if (currentTurnIndex === 0) {{
    currentTurnIndex = 1;
    currentSubmoveIndex = 0;
    const turn = GAME_DATA.turns[0];
    playDiceRoll();
    animateSubmove(turn.submoves[0], () => {{
      updateInfo(1, 0);
    }});
    return;
  }}

  const turn = GAME_DATA.turns[currentTurnIndex - 1];
  if (currentSubmoveIndex < turn.submoves.length - 1) {{
    currentSubmoveIndex++;
    animateSubmove(turn.submoves[currentSubmoveIndex], () => {{
      updateInfo(currentTurnIndex, currentSubmoveIndex);
    }});
  }} else {{
    if (currentTurnIndex < GAME_DATA.turns.length) {{
      currentTurnIndex++;
      currentSubmoveIndex = 0;
      const nextTurn = GAME_DATA.turns[currentTurnIndex - 1];
      playDiceRoll();
      animateSubmove(nextTurn.submoves[0], () => {{
        updateInfo(currentTurnIndex, 0);
      }});
    }}
  }}
}}

// Step backward 1 submove
function stepBackward() {{
  stopPlay();

  if (currentTurnIndex === 0) return;

  const turn = GAME_DATA.turns[currentTurnIndex - 1];

  if (currentSubmoveIndex > 0) {{
    currentSubmoveIndex--;
    renderCheckers(turn.submoves[currentSubmoveIndex].state_after);
    updateInfo(currentTurnIndex, currentSubmoveIndex);
  }} else if (currentSubmoveIndex === 0) {{
    renderCheckers(turn.submoves[0].state_before);
    currentSubmoveIndex = -1;
    currentTurnIndex--;
    updateInfo(currentTurnIndex);
  }} else {{
    // currentSubmoveIndex was -1
    if (turn.submoves.length > 1) {{
      currentSubmoveIndex = turn.submoves.length - 2;
      renderCheckers(turn.submoves[currentSubmoveIndex].state_after);
      updateInfo(currentTurnIndex, currentSubmoveIndex);
    }} else {{
      currentTurnIndex--;
      if (currentTurnIndex === 0) {{
        goToTurn(0, false);
      }} else {{
        const prevTurn = GAME_DATA.turns[currentTurnIndex - 1];
        renderCheckers(prevTurn.state_after);
        updateInfo(currentTurnIndex);
      }}
    }}
  }}
}}

// Auto-Play Continuous Slideshow
function startPlay() {{
  if (isPlaying) return;
  isPlaying = true;

  // Keep window at the top during play mode
  window.scrollTo({{ top: 0, behavior: 'smooth' }});

  document.getElementById('playText').textContent = 'Pause';
  document.getElementById('playIcon').textContent = '⏸';
  document.getElementById('playBtn').classList.replace('from-sky-500', 'from-amber-500');
  document.getElementById('playBtn').classList.replace('to-blue-600', 'to-orange-600');

  // If already at final move, rewind to start
  if (currentTurnIndex >= GAME_DATA.turns.length) {{
    goToTurn(0, false);
  }}

  function advanceNextTurn() {{
    if (!isPlaying) return;
    if (currentTurnIndex < GAME_DATA.turns.length) {{
      goToTurn(currentTurnIndex + 1, true, () => {{
        if (!isPlaying) return;
        const pauseBetweenTurns = Math.max(450, 1000 / playSpeed);
        playTimer = setTimeout(advanceNextTurn, pauseBetweenTurns);
      }});
    }} else {{
      stopPlay();
    }}
  }}

  advanceNextTurn();
}}

function stopPlay() {{
  isPlaying = false;
  if (playTimer) {{
    clearTimeout(playTimer);
    playTimer = null;
  }}
  document.getElementById('playText').textContent = 'Play';
  document.getElementById('playIcon').textContent = '▶';
  document.getElementById('playBtn').classList.replace('from-amber-500', 'from-sky-500');
  document.getElementById('playBtn').classList.replace('to-orange-600', 'to-blue-600');
}}

// Build Timeline Markers along the slider
function buildTimelineMarkers() {{
  const container = document.getElementById('sliderTimelineMarkers');
  container.innerHTML = '';
  const total = GAME_DATA.turns.length;

  GAME_DATA.turns.forEach((t, i) => {{
    const pct = ((i + 1) / total) * 100;
    if (t.is_double || t.has_hit) {{
      const dot = document.createElement('span');
      dot.style.left = `${{pct}}%`;
      dot.className = `absolute -top-1 w-2 h-2 -ml-1 rounded-full cursor-pointer pointer-events-auto ${{t.has_hit ? 'bg-red-500 ring-2 ring-red-400/40' : 'bg-purple-500 ring-2 ring-purple-400/40'}}`;
      dot.title = `Move ${{i+1}}: ${{t.is_double ? 'Double' : ''}} ${{t.has_hit ? 'Checker Hit!' : ''}}`;
      dot.onclick = () => {{
        stopPlay();
        goToTurn(i + 1, false);
      }};
      container.appendChild(dot);
    }}
  }});
}}

// Populate Transcript Sidebar
function buildTranscriptList() {{
  const container = document.getElementById('movesListContainer');
  container.innerHTML = '';

  GAME_DATA.turns.forEach((t, i) => {{
    const moveIdx = i + 1;
    const isCameron = t.player === 'cameronwhale';

    const row = document.createElement('div');
    row.id = `row-move-${{moveIdx}}`;
    row.className = `transcript-row p-2.5 rounded-xl border border-slate-800 hover:border-slate-700 cursor-pointer transition flex items-center justify-between gap-2 text-xs ${{t.has_hit ? 'border-red-900/40 bg-red-950/10' : 'bg-slate-900/40'}}`;
    if (filterHitsOnly && !t.has_hit) {{
      row.style.display = 'none';
    }}

    row.onclick = () => {{
      stopPlay();
      goToTurn(moveIdx, false);
    }};

    row.innerHTML = `
      <div class="flex items-center gap-2">
        <span class="font-mono text-slate-500 font-bold w-5 text-right">${{moveIdx}}</span>
        <span class="w-2.5 h-2.5 rounded-full ${{isCameron ? 'bg-amber-400' : 'bg-emerald-400'}}"></span>
        <div class="flex flex-col">
          <span class="font-semibold ${{isCameron ? 'text-amber-400' : 'text-emerald-400'}}">${{isCameron ? 'cameronwhale' : '-George'}}</span>
          <span class="font-mono text-slate-300 text-[11px]">${{t.desc}}</span>
        </div>
      </div>
      <div class="flex items-center gap-1.5 flex-shrink-0">
        ${{t.is_double ? '<span class="bg-purple-900/60 text-purple-300 border border-purple-700/50 text-[10px] px-1.5 py-0.5 rounded font-bold">2x</span>' : ''}}
        ${{t.has_hit ? '<span class="bg-red-900/80 text-red-300 border border-red-700/60 text-[10px] px-1.5 py-0.5 rounded font-bold">HIT</span>' : ''}}
        <span class="font-mono text-slate-400 text-[11px]">${{t.state_after.cameron_pips}} / ${{t.state_after.george_pips}}</span>
      </div>
    `;

    container.appendChild(row);
  }});
}}

// Initialize Event Listeners
function initEvents() {{
  document.getElementById('playBtn').onclick = () => {{
    if (isPlaying) stopPlay();
    else startPlay();
  }};

  document.getElementById('nextTurnBtn').onclick = () => {{
    stopPlay();
    goToTurn(currentTurnIndex + 1, false);
  }};

  document.getElementById('prevTurnBtn').onclick = () => {{
    stopPlay();
    goToTurn(currentTurnIndex - 1, false);
  }};

  document.getElementById('nextStepBtn').onclick = () => {{
    stepForward();
  }};

  document.getElementById('prevStepBtn').onclick = () => {{
    stepBackward();
  }};

  document.getElementById('firstBtn').onclick = () => {{
    stopPlay();
    goToTurn(0, false);
  }};

  document.getElementById('lastBtn').onclick = () => {{
    stopPlay();
    goToTurn(GAME_DATA.turns.length, false);
  }};

  document.getElementById('moveSlider').oninput = (e) => {{
    stopPlay();
    goToTurn(parseInt(e.target.value), false);
  }};

  // Speed buttons
  document.querySelectorAll('.speed-btn').forEach(btn => {{
    btn.onclick = () => {{
      document.querySelectorAll('.speed-btn').forEach(b => {{
        b.classList.remove('bg-sky-500', 'text-slate-950', 'font-bold');
        b.classList.add('text-slate-300');
      }});
      btn.classList.add('bg-sky-500', 'text-slate-950', 'font-bold');
      btn.classList.remove('text-slate-300');
      playSpeed = parseFloat(btn.dataset.speed);
    }};
  }});

  // Sound toggle
  document.getElementById('soundToggleBtn').onclick = () => {{
    soundEnabled = !soundEnabled;
    document.getElementById('soundIcon').textContent = soundEnabled ? '🔊' : '🔇';
    document.getElementById('soundLabel').textContent = soundEnabled ? 'Sound ON' : 'Sound OFF';
    if (soundEnabled) playClack();
  }};

  // Perspective toggle
  document.getElementById('perspectiveToggleBtn').onclick = () => {{
    perspective = perspective === 'cameron' ? 'george' : 'cameron';
    updatePointLabels();
  }};

  // Filter Hits Only
  document.getElementById('filterHitsBtn').onclick = () => {{
    filterHitsOnly = true;
    document.getElementById('filterHitsBtn').className = 'px-2 py-0.5 rounded bg-red-500/20 text-red-400 font-semibold border border-red-500/30';
    document.getElementById('filterAllBtn').className = 'px-2 py-0.5 rounded bg-slate-800 text-slate-400 hover:text-slate-200';
    buildTranscriptList();
  }};
  document.getElementById('filterAllBtn').onclick = () => {{
    filterHitsOnly = false;
    document.getElementById('filterAllBtn').className = 'px-2 py-0.5 rounded bg-sky-500/20 text-sky-400 font-semibold border border-sky-500/30';
    document.getElementById('filterHitsBtn').className = 'px-2 py-0.5 rounded bg-slate-800 text-slate-400 hover:text-slate-200';
    buildTranscriptList();
  }};

  // Hide / Show Transcript
  document.getElementById('logToggleBtn').onclick = () => {{
    const logCol = document.getElementById('logCol');
    const boardCol = document.getElementById('boardCol');
    const label = document.getElementById('logToggleLabel');
    if (logCol.classList.contains('hidden')) {{
      logCol.classList.remove('hidden');
      boardCol.className = 'lg:col-span-8 transition-all duration-300 space-y-4';
      label.textContent = 'Hide Log';
    }} else {{
      logCol.classList.add('hidden');
      boardCol.className = 'lg:col-span-12 transition-all duration-300 space-y-4';
      label.textContent = 'Show Log';
    }}
  }};

  // Keyboard Shortcuts
  window.addEventListener('keydown', (e) => {{
    if (e.target.tagName === 'INPUT') return;
    if (e.code === 'Space') {{
      e.preventDefault();
      document.getElementById('playBtn').click();
    }} else if (e.code === 'ArrowRight') {{
      e.preventDefault();
      stepForward();
    }} else if (e.code === 'ArrowLeft') {{
      e.preventDefault();
      stepBackward();
    }} else if (e.code === 'ArrowDown') {{
      e.preventDefault();
      stopPlay();
      goToTurn(currentTurnIndex + 1, false);
    }} else if (e.code === 'ArrowUp') {{
      e.preventDefault();
      stopPlay();
      goToTurn(currentTurnIndex - 1, false);
    }} else if (e.code === 'Home') {{
      e.preventDefault();
      stopPlay();
      goToTurn(0, false);
    }} else if (e.code === 'End') {{
      e.preventDefault();
      stopPlay();
      goToTurn(GAME_DATA.turns.length, false);
    }} else if (e.key === 'm' || e.key === 'M') {{
      document.getElementById('soundToggleBtn').click();
    }}
  }});
}}

// Initialize Application
window.addEventListener('DOMContentLoaded', () => {{
  buildBoardSvg();
  updatePointLabels();
  buildTimelineMarkers();
  buildTranscriptList();
  initEvents();

  // Load Move 1
  goToTurn(1, false);
}});
</script>
</body>
</html>
'''

with open('/Users/kumaran/Downloads/backgammon/index.html', 'w') as f:
    f.write(html_content)

print('Successfully rebuilt index.html!')
