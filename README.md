<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, interactive-widget=resizes-content">
<title>SethCyanide</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { height: 100%; overflow: hidden; background: #000; }

/* ── THEME VARIABLES (set by JS at load) ── */
:root {
  --bg:        #000000;
  --primary:   #7dd9ff;
  --bright:    #ccf2ff;
  --dim:       #336677;
  --border:    #2a6a8a;
  --glow:      rgba(125,217,255,0.35);
  --err:       #ff6b6b;
  --ink:       #000000;
  --outline:   #000000;
}

.fo-wrap { width:100%; height:100dvh; background:#000; display:flex; align-items:center; justify-content:center; overflow:hidden; }

.fo-screen {
  width:100%; height:100%;
  background: var(--bg);
  display:flex; flex-direction:column;
  padding:24px 28px 16px;
  position:relative; overflow:hidden;
  font-family:'Share Tech Mono','Courier New',monospace;
  color: var(--primary);
  transition: background 0.3s;
}

.scanlines {
  position:absolute; inset:0; pointer-events:none; z-index:10;
  background: repeating-linear-gradient(to bottom, transparent 0px, transparent 2px, rgba(0,0,0,0.18) 2px, rgba(0,0,0,0.18) 4px);
}
.vignette {
  position:absolute; inset:0; pointer-events:none; z-index:11;
  background: radial-gradient(ellipse at center, transparent 45%, rgba(0,0,0,0.7) 100%);
}
.vhs-glitch { position:absolute; inset:0; pointer-events:none; z-index:12; animation:vhs-noise 6s infinite; opacity:0; }
@keyframes vhs-noise {
  0%,89%,100%{opacity:0}
  90%{opacity:1;background:linear-gradient(transparent 60%,var(--glow) 60%,transparent 62%);transform:translateX(-3px)}
  91%{opacity:1;background:linear-gradient(transparent 30%,var(--glow) 30%,transparent 32%);transform:translateX(3px)}
  92%{opacity:1;background:linear-gradient(transparent 75%,var(--glow) 75%,transparent 77%);transform:translateX(-2px)}
  93%{opacity:0;transform:translateX(0)}
}
.vhs-rgb {
  position:absolute; inset:0; pointer-events:none; z-index:9;
  background:repeating-linear-gradient(90deg,var(--glow) 0px,transparent 1px,transparent 3px);
  opacity:0.05;
}

/* ── GLITTER / SHIMMER SYSTEM ── */

/* Diagonal screen shimmer sweep — smooth holographic card tilt effect */
.shimmer-sweep {
  position:absolute; inset:0; pointer-events:none; z-index:8; overflow:hidden;
}
.shimmer-sweep::after {
  content:'';
  position:absolute;
  top:-100%; left:-60%;
  width:30%; height:300%;
  background: linear-gradient(
    to right,
    transparent 0%,
    rgba(255,255,255,0.03) 30%,
    rgba(255,255,255,0.07) 50%,
    rgba(255,255,255,0.03) 70%,
    transparent 100%
  );
  transform: skewX(-15deg) translateX(-100%);
  animation: shimmer-slide 10s ease-in-out infinite;
}
@keyframes shimmer-slide {
  0%   { transform: skewX(-15deg) translateX(-100%); opacity:0; }
  5%   { opacity:1; }
  45%  { opacity:1; }
  55%  { transform: skewX(-15deg) translateX(500%); opacity:0; }
  100% { transform: skewX(-15deg) translateX(500%); opacity:0; }
}

/* Sparkle particle canvas — sits above everything except overlays */
#glitterCanvas {
  position:absolute; inset:0; pointer-events:none; z-index:13;
  width:100%; height:100%;
}

/* Title prismatic shimmer — subtle rainbow sheen that slides across */
.fo-title {
  font-size:clamp(18px,4vw,26px); letter-spacing:8px;
  color:var(--bright);
  text-shadow:0 0 10px var(--glow),0 0 28px var(--glow);
  text-transform:uppercase;
  position:relative;
  overflow:hidden;
}
.fo-title::after {
  content:'';
  position:absolute; inset:0;
  background: linear-gradient(
    105deg,
    transparent 20%,
    rgba(255,255,255,0.0) 35%,
    rgba(255,255,255,0.18) 45%,
    rgba(255,255,255,0.0) 55%,
    transparent 70%
  );
  background-size:300% 100%;
  animation: title-shine 5s ease-in-out infinite;
  pointer-events:none;
}
@keyframes title-shine {
  0%   { background-position:150% 0; }
  50%  { background-position:-50% 0; }
  100% { background-position:150% 0; }
}

/* Cursor gets a prismatic glint pulse on top of blink */
.cursor-block {
  display:inline-block; width:9px; height:13px;
  background:var(--primary);
  box-shadow:0 0 8px var(--glow), 0 0 2px #fff;
  vertical-align:middle;
  animation:blink 1.1s step-end infinite, cursor-glint 4s ease-in-out infinite;
}
@keyframes cursor-glint {
  0%,100% { box-shadow:0 0 8px var(--glow), 0 0 2px #fff; }
  40%     { box-shadow:0 0 14px var(--glow), 0 0 6px #fff, 0 0 2px rgba(255,255,255,0.9); }
  50%     { box-shadow:0 0 18px var(--glow), 0 0 10px #fff, 0 0 4px rgba(255,220,255,0.9); }
  60%     { box-shadow:0 0 14px var(--glow), 0 0 6px #fff, 0 0 2px rgba(255,255,255,0.9); }
}

/* Border lines get a slow glimmer pulse */
.fo-header {
  text-align:center; padding-bottom:12px; margin-bottom:12px;
  border-bottom:1px solid var(--border);
  flex-shrink:0; z-index:5; position:relative;
  animation:flicker 9s infinite, border-glimmer 6s ease-in-out infinite;
}
@keyframes flicker { 0%,93%,100%{opacity:1} 94%{opacity:0.6} 95%{opacity:1} 97%{opacity:0.4} 98%{opacity:1} }
@keyframes border-glimmer {
  0%,100% { border-bottom-color:var(--border); }
  50%     { border-bottom-color:var(--bright); box-shadow:0 1px 6px var(--glow); }
}
.fo-input-area { flex-shrink:0; border-top:1px solid var(--border); padding-top:10px; position:relative; z-index:5; padding-bottom:env(safe-area-inset-bottom,0px); animation:border-glimmer-top 7s ease-in-out infinite; }
@keyframes border-glimmer-top {
  0%,100% { border-top-color:var(--border); }
  50%     { border-top-color:var(--bright); box-shadow:0 -1px 6px var(--glow); }
}

.fo-subtitle { font-size:clamp(9px,1.4vw,11px); letter-spacing:4px; color:var(--dim); margin-top:4px; text-transform:uppercase; }


.fo-output { flex:1; overflow-y:auto; font-size:clamp(11px,1.8vw,13px); line-height:1.8; white-space:pre-wrap; word-break:break-word; color:var(--primary); text-shadow:0 0 4px var(--glow); padding-bottom:8px; -webkit-overflow-scrolling:touch; position:relative; z-index:5; scrollbar-width:none; }
.fo-output::-webkit-scrollbar { display:none; }
.fo-output .err  { color:var(--err); text-shadow:0 0 5px rgba(255,107,107,0.5); }
.fo-output .ok   { color:var(--bright); text-shadow:0 0 8px var(--glow); }
.fo-output .hdr  { color:var(--bright); text-shadow:0 0 8px var(--glow); }
.fo-output .dim  { color:var(--bright); text-shadow:-1px -1px 0 var(--outline),1px -1px 0 var(--outline),-1px 1px 0 var(--outline),1px 1px 0 var(--outline); }
.fo-output .info { color:var(--primary); }
.fo-output .pwr  { color:var(--dim); font-size:10px; }
.fo-output .warn { color:var(--bright); text-shadow:0 0 5px var(--glow); }

.fo-prompt-row  { display:flex; align-items:center; font-size:clamp(11px,1.8vw,13px); color:var(--primary); text-shadow:0 0 4px var(--glow); }
.fo-prompt-label { white-space:nowrap; flex-shrink:0; }
.fake-input-wrap { position:relative; flex:1; height:18px; }
.typed-text { position:absolute; top:0; left:0; white-space:pre; pointer-events:none; line-height:18px; font-family:'Share Tech Mono','Courier New',monospace; font-size:clamp(11px,1.8vw,13px); color:var(--primary); text-shadow:0 0 4px var(--glow); }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
#real-input { position:absolute; top:0; left:0; width:100%; height:100%; background:transparent; border:none; outline:none; padding:0; font-family:'Share Tech Mono','Courier New',monospace; font-size:16px; color:transparent; caret-color:transparent; }

.fo-footer { display:flex; justify-content:space-between; font-size:9px; letter-spacing:2px; margin-top:8px; text-transform:uppercase; position:relative; z-index:5; color:var(--bright); text-shadow:-1px -1px 0 var(--outline),1px -1px 0 var(--outline),-1px 1px 0 var(--outline),1px 1px 0 var(--outline); }

/* ── SHARED OVERLAY BASE ── */
.sc-overlay {
  position:absolute; inset:0;
  background:var(--bg);
  display:none; flex-direction:column;
  font-family:'Share Tech Mono','Courier New',monospace;
}
.sc-overlay.active { display:flex; }
.sc-overlay-top {
  display:flex; justify-content:space-between; align-items:center;
  border-bottom:1px solid var(--border);
  padding:14px 20px 10px;
  color:var(--bright); text-shadow:0 0 8px var(--glow);
  font-size:clamp(10px,1.8vw,12px); letter-spacing:2px;
  flex-shrink:0;
}
.sc-close-btn {
  cursor:pointer; border:1px solid var(--border); color:var(--primary);
  background:transparent; padding:4px 12px;
  font-family:inherit; font-size:inherit; letter-spacing:2px;
  -webkit-tap-highlight-color:transparent;
}
.sc-close-btn:active { background:var(--primary); color:var(--ink); }

/* ── HACKING MINIGAME ── */
.hack-overlay { padding:20px 24px; z-index:20; }
.hack-top { display:flex; justify-content:space-between; align-items:baseline; border-bottom:1px solid var(--border); padding-bottom:8px; margin-bottom:10px; color:var(--bright); text-shadow:0 0 8px var(--glow); font-size:clamp(11px,2vw,13px); letter-spacing:2px; flex-shrink:0; }
.hack-attempts { display:flex; gap:6px; }
.hack-attempt-dot { width:10px; height:14px; background:var(--primary); box-shadow:0 0 6px var(--glow); }
.hack-attempt-dot.used { background:var(--border); box-shadow:none; opacity:0.3; }
.hack-body { display:flex; gap:16px; flex:1; min-height:0; }
.hack-col { flex:1; overflow-y:auto; font-size:clamp(10px,1.6vw,12.5px); line-height:1.9; color:var(--primary); scrollbar-width:none; }
.hack-col::-webkit-scrollbar { display:none; }
.hack-line { display:flex; gap:10px; white-space:nowrap; align-items:center; width:100%; }
.hack-addr { color:var(--bright); flex-shrink:0; text-shadow:-1px -1px 0 var(--outline),1px -1px 0 var(--outline),-1px 1px 0 var(--outline),1px 1px 0 var(--outline); }
.hack-bytes { display:flex; gap:4px; flex-wrap:nowrap; white-space:nowrap; flex:1; justify-content:space-between; }
.hack-tok { cursor:pointer; padding:0 2px; border-radius:2px; color:var(--primary); text-shadow:0 0 4px var(--glow); -webkit-tap-highlight-color:transparent; user-select:none; }
.hack-tok.candidate { color:var(--bright); text-shadow:0 0 8px var(--glow); font-weight:bold; }
.hack-tok:active,.hack-tok.touched { background:var(--primary); color:var(--ink); text-shadow:none; }
.hack-tok.bracket { color:var(--bright); opacity:0.7; }
.hack-tok.bracket:active { background:var(--primary); color:var(--ink); opacity:1; }
.hack-feed { margin-top:10px; border-top:1px solid var(--border); padding-top:8px; font-size:clamp(10px,1.6vw,12px); color:var(--primary); min-height:40px; max-height:70px; overflow-y:auto; flex-shrink:0; scrollbar-width:none; }
.hack-feed::-webkit-scrollbar { display:none; }
.hack-feed .ok   { color:var(--bright); }
.hack-feed .err  { color:var(--err); }
.hack-feed .warn { color:var(--bright); opacity:0.8; }
.hack-history { margin-top:8px; border-top:1px solid var(--border); padding-top:6px; font-size:clamp(10px,1.6vw,12px); flex-shrink:0; display:flex; flex-direction:column; gap:3px; }
.hack-history-row { display:flex; justify-content:space-between; color:var(--primary); text-shadow:0 0 4px var(--glow); }
.hack-history-row .hh-match { color:var(--bright); }
.hack-hint { font-size:10px; color:var(--bright); text-shadow:-1px -1px 0 var(--outline),1px -1px 0 var(--outline),-1px 1px 0 var(--outline),1px 1px 0 var(--outline); text-align:center; margin-top:8px; letter-spacing:1px; flex-shrink:0; }

/* ── REFLEX MINIGAME ── */
.reflex-overlay { z-index:22; align-items:center; justify-content:center; gap:18px; padding:24px; text-align:center; }
.reflex-top { display:flex; justify-content:space-between; width:100%; max-width:360px; color:var(--bright); text-shadow:0 0 8px var(--glow); font-size:clamp(11px,2vw,13px); letter-spacing:2px; }
.reflex-instructions { color:var(--primary); font-size:clamp(11px,2vw,13px); letter-spacing:1px; max-width:320px; }
.reflex-track { position:relative; width:100%; max-width:360px; height:28px; background:rgba(0,0,0,0.5); border:1px solid var(--border); border-radius:4px; overflow:hidden; }
.reflex-zone { position:absolute; top:0; bottom:0; background:var(--primary); opacity:0.4; }
.reflex-bar { position:absolute; top:0; bottom:0; width:4px; background:#fff; box-shadow:0 0 8px #fff; left:0; }
.reflex-button { font-family:inherit; font-size:clamp(16px,4vw,20px); letter-spacing:4px; padding:16px 48px; background:var(--primary); color:var(--ink); border:none; border-radius:6px; cursor:pointer; box-shadow:0 0 20px var(--glow); -webkit-tap-highlight-color:transparent; user-select:none; font-weight:bold; }
.reflex-button:active { transform:scale(0.96); }
.reflex-result { min-height:20px; font-size:clamp(11px,2vw,13px); letter-spacing:1px; color:var(--bright); }
.reflex-result.win  { text-shadow:0 0 8px var(--glow); }
.reflex-result.lose { color:var(--err); }

/* ── MUSIC PLAYER ── */
.music-overlay { z-index:23; }

.music-body {
  flex:1; display:flex; flex-direction:column;
  min-height:0; position:relative;
}

/* Visualizer canvas */
#milkCanvas {
  position:absolute; inset:0; width:100%; height:100%;
  display:none;
}
#milkCanvas.active { display:block; }

/* Track list */
.music-tracklist {
  flex:1; overflow-y:auto; padding:8px 20px;
  scrollbar-width:none; position:relative; z-index:2;
}
.music-tracklist::-webkit-scrollbar { display:none; }
.music-track {
  display:flex; align-items:center; gap:12px;
  padding:10px 8px; border-bottom:1px solid var(--border);
  cursor:pointer; font-size:clamp(11px,1.8vw,13px);
  color:var(--primary); letter-spacing:1px;
  -webkit-tap-highlight-color:transparent;
  user-select:none;
}
.music-track:active,.music-track.playing { color:var(--bright); background:rgba(255,255,255,0.05); }
.music-track.playing { text-shadow:0 0 8px var(--glow); }
.music-track-num { color:var(--dim); width:22px; flex-shrink:0; }
.music-track-info { flex:1; min-width:0; }
.music-track-title { white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.music-track-artist { font-size:10px; color:var(--dim); margin-top:2px; letter-spacing:1px; }
.music-track-dur { color:var(--dim); font-size:11px; flex-shrink:0; }

/* Player controls */
.music-controls {
  flex-shrink:0; padding:12px 20px 8px;
  border-top:1px solid var(--border);
  display:flex; flex-direction:column; gap:10px;
  position:relative; z-index:2;
  background:var(--bg);
}
.music-now-playing { font-size:clamp(10px,1.8vw,12px); color:var(--bright); text-shadow:0 0 6px var(--glow); letter-spacing:1px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.music-progress-wrap { position:relative; height:6px; background:rgba(255,255,255,0.1); border-radius:3px; cursor:pointer; -webkit-tap-highlight-color:transparent; }
.music-progress-bar { height:100%; background:var(--primary); border-radius:3px; width:0%; box-shadow:0 0 6px var(--glow); pointer-events:none; }
.music-btn-row { display:flex; align-items:center; gap:16px; }
.music-btn {
  font-family:inherit; font-size:clamp(11px,2vw,13px); letter-spacing:2px;
  padding:7px 14px; background:transparent; border:1px solid var(--border);
  color:var(--primary); cursor:pointer; -webkit-tap-highlight-color:transparent;
}
.music-btn:active,.music-btn.active-btn { background:var(--primary); color:var(--ink); }
.music-time { font-size:11px; color:var(--dim); margin-left:auto; letter-spacing:1px; }
.music-vol-wrap { display:flex; align-items:center; gap:10px; font-size:11px; color:var(--dim); letter-spacing:1px; }
.music-vol { -webkit-appearance:none; appearance:none; flex:1; height:4px; background:rgba(255,255,255,0.1); border-radius:2px; outline:none; cursor:pointer; }
.music-vol::-webkit-slider-thumb { -webkit-appearance:none; width:14px; height:14px; border-radius:50%; background:var(--primary); box-shadow:0 0 6px var(--glow); }

/* ── EMULATOR OVERLAY ── */
.emu-overlay { z-index:25; }
#emuContainer { flex:1; min-height:0; background:#000; position:relative; }
.emu-loading { position:absolute; inset:0; display:flex; align-items:center; justify-content:center; color:var(--primary); font-family:'Share Tech Mono','Courier New',monospace; font-size:13px; letter-spacing:2px; text-shadow:0 0 6px var(--glow); }

</style>
</head>
<body>

<div class="fo-wrap">
  <div class="fo-screen" id="terminal">
    <div class="scanlines"></div>
    <div class="vignette"></div>
    <div class="vhs-glitch"></div>
    <div class="vhs-rgb"></div>
    <div class="shimmer-sweep"></div>
    <canvas id="glitterCanvas"></canvas>

    <div class="fo-header">
      <div class="fo-title">SethCyanide</div>
      <div class="fo-subtitle">Terminal Access System &mdash; v1.0</div>
    </div>

    <div class="fo-output" id="out"><span class="hdr">SethCyanide Terminal [Version 1.0]
<span class="pwr">$POWERED_BY$</span>
(C)Copyright SethCyanide. All rights reserved.</span>

<span class="info">Type HELP for available commands.</span>

</div>

    <div class="fo-input-area">
      <div class="fo-prompt-row">
        <span class="fo-prompt-label">C:\SETHCYANIDE&gt;&nbsp;</span>
        <div class="fake-input-wrap">
          <input id="real-input" type="text" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" autofocus aria-label="Command input" />
          <div class="typed-text"><span id="typed"></span><span class="cursor-block"></span></div>
        </div>
      </div>
      <div class="fo-footer">
        <span>SethCyanide.do.am</span>
        <span id="fo-time">--:--:--</span>
      </div>
    </div>

    <!-- HACKING MINIGAME -->
    <div class="sc-overlay hack-overlay" id="hackOverlay">
      <div class="hack-top">
        <span>SECURITY OVERRIDE // SETHCYANIDE</span>
        <div class="hack-attempts" id="hackAttempts"></div>
      </div>
      <div class="hack-body">
        <div class="hack-col" id="hackColA"></div>
        <div class="hack-col" id="hackColB"></div>
      </div>
      <div class="hack-history" id="hackHistory"></div>
      <div class="hack-feed" id="hackFeed"></div>
      <div class="hack-hint">TAP A WORD OR A [BRACKET PAIR] TO GUESS</div>
    </div>

    <!-- REFLEX MINIGAME -->
    <div class="sc-overlay reflex-overlay" id="reflexOverlay">
      <div class="reflex-top">
        <span id="reflexLabel">SYNC TEST</span>
        <span id="reflexRound">ROUND 1/3</span>
      </div>
      <div class="reflex-instructions" id="reflexInstructions">TAP WHEN THE BAR HITS THE ZONE</div>
      <div class="reflex-track">
        <div class="reflex-zone" id="reflexZone"></div>
        <div class="reflex-bar" id="reflexBar"></div>
      </div>
      <button class="reflex-button" id="reflexButton">TAP</button>
      <div class="reflex-result" id="reflexResult">&nbsp;</div>
    </div>

    <!-- MUSIC PLAYER -->
    <div class="sc-overlay music-overlay" id="musicOverlay">
      <div class="sc-overlay-top">
        <span>SETHCYANIDE // MEDIA MODULE</span>
        <div style="display:flex;gap:8px;">
          <button class="sc-close-btn" id="vizToggleBtn">VISUALIZER</button>
          <button class="sc-close-btn" id="musicClose">CLOSE</button>
        </div>
      </div>
      <div class="music-body">
        <canvas id="milkCanvas"></canvas>
        <div class="music-tracklist" id="musicTracklist"></div>
      </div>
      <div class="music-controls">
        <div class="music-now-playing" id="nowPlaying">-- SELECT A TRACK --</div>
        <div class="music-progress-wrap" id="progressWrap">
          <div class="music-progress-bar" id="progressBar"></div>
        </div>
        <div class="music-btn-row">
          <button class="music-btn" id="prevBtn">&#9664;&#9664;</button>
          <button class="music-btn" id="playBtn">&#9654;</button>
          <button class="music-btn" id="nextBtn">&#9654;&#9654;</button>
          <button class="music-btn" id="shuffleBtn">&#8645;</button>
          <span class="music-time" id="musicTime">0:00 / 0:00</span>
        </div>
        <div class="music-vol-wrap">
          <span>VOL</span>
          <input class="music-vol" type="range" id="volSlider" min="0" max="1" step="0.01" value="0.8">
        </div>
      </div>
    </div>

    <!-- EMULATOR -->
    <div class="sc-overlay emu-overlay" id="emuOverlay">
      <div class="sc-overlay-top">
        <span>SETHCYANIDE // GB MODULE</span>
        <button class="sc-close-btn" id="emuClose">CLOSE</button>
      </div>
      <div id="emuContainer">
        <div class="emu-loading" id="emuLoading">LOADING CARTRIDGE...</div>
      </div>
    </div>

  </div>
</div>

<!-- <popup> --><!-- </popup> -->

<script>
/* ═══════════════════════════════════════════
   THEME SYSTEM — picks one at random on load
   ═══════════════════════════════════════════ */
const THEMES = {
  hotpink: {
    '--bg':      '#0d0008',
    '--primary': '#ff69b4',
    '--bright':  '#ffb3d9',
    '--dim':     '#7a2a50',
    '--border':  '#a03060',
    '--glow':    'rgba(255,105,180,0.35)',
    '--err':     '#ff4444',
    '--ink':     '#0d0008',
    '--outline': '#0d0008',
  },
  mossy: {
    '--bg':      '#060e06',
    '--primary': '#6dbf7e',
    '--bright':  '#b3f0bf',
    '--dim':     '#2e5c36',
    '--border':  '#3a7a4a',
    '--glow':    'rgba(109,191,126,0.35)',
    '--err':     '#ff8d6b',
    '--ink':     '#060e06',
    '--outline': '#060e06',
  },
  babyblue: {
    '--bg':      '#01010f',
    '--primary': '#7dd9ff',
    '--bright':  '#ccf2ff',
    '--dim':     '#2a5a7a',
    '--border':  '#2a6a8a',
    '--glow':    'rgba(125,217,255,0.35)',
    '--err':     '#ff6b6b',
    '--ink':     '#01010f',
    '--outline': '#01010f',
  },
  noir: {
    '--bg':      '#0a0a0a',
    '--primary': '#c8c8c8',
    '--bright':  '#ffffff',
    '--dim':     '#555555',
    '--border':  '#666666',
    '--glow':    'rgba(200,200,200,0.25)',
    '--err':     '#ff4444',
    '--ink':     '#0a0a0a',
    '--outline': '#0a0a0a',
  },
};

const themeKeys = Object.keys(THEMES);
const chosenTheme = THEMES[themeKeys[Math.floor(Math.random() * themeKeys.length)]];
const root = document.documentElement;
Object.entries(chosenTheme).forEach(([k, v]) => root.style.setProperty(k, v));

/* ═══════════════════════════════════════
   PAGE CONFIG
   ═══════════════════════════════════════ */
const pages = {
  home:    { label: 'Home',    url: '/' },
  contact: { label: 'Contact', url: '/contact' },
};

const secrets = {
  override: { label: 'Override Access', url: '/secretpage', failUrl: '/' },
  vault:    { label: 'The Vault',        url: '/vault',       failUrl: '/' },
};

const gameCommand = {
  cmd:     'cartridge',
  core:    'gambatte',
  romUrl:  'https://your-ucoz-domain.com/files/your-game.gb'
};

const reflexGames = {
  syncup: { cmd: 'syncup', label: 'SYNC TEST', rounds: 3, unlockUrl: null },
};

const musicCmd = 'music';
/* ── Update these URLs after uploading to ucoz file manager ── */
const tracks = [
  { title: 'Track One',    artist: 'SethCyanide', url: 'https://your-ucoz-domain.com/files/track01.mp3' },
  { title: 'Track Two',    artist: 'SethCyanide', url: 'https://your-ucoz-domain.com/files/track02.mp3' },
  { title: 'Track Three',  artist: 'SethCyanide', url: 'https://your-ucoz-domain.com/files/track03.mp3' },
  { title: 'Track Four',   artist: 'SethCyanide', url: 'https://your-ucoz-domain.com/files/track04.mp3' },
  { title: 'Track Five',   artist: 'SethCyanide', url: 'https://your-ucoz-domain.com/files/track05.mp3' },
  { title: 'Track Six',    artist: 'SethCyanide', url: 'https://your-ucoz-domain.com/files/track06.mp3' },
  { title: 'Track Seven',  artist: 'SethCyanide', url: 'https://your-ucoz-domain.com/files/track07.mp3' },
  { title: 'Track Eight',  artist: 'SethCyanide', url: 'https://your-ucoz-domain.com/files/track08.mp3' },
  { title: 'Track Nine',   artist: 'SethCyanide', url: 'https://your-ucoz-domain.com/files/track09.mp3' },
  { title: 'Track Ten',    artist: 'SethCyanide', url: 'https://your-ucoz-domain.com/files/track10.mp3' },
];

/* ═══════════════════════════════════════
   TERMINAL CORE
   ═══════════════════════════════════════ */
const out   = document.getElementById('out');
const typed = document.getElementById('typed');
const input = document.getElementById('real-input');
const clock = document.getElementById('fo-time');

function updateClock() {
  const n = new Date();
  clock.textContent = String(n.getHours()).padStart(2,'0')+':'+String(n.getMinutes()).padStart(2,'0')+':'+String(n.getSeconds()).padStart(2,'0');
}
updateClock(); setInterval(updateClock, 1000);

document.getElementById('terminal').addEventListener('click', () => {
  if (document.querySelector('.sc-overlay.active')) return;
  input.focus();
});
input.addEventListener('input', () => { typed.textContent = input.value; });

input.addEventListener('keydown', e => {
  if (e.key !== 'Enter') return;
  const raw = input.value;
  const cmd = raw.trim().toLowerCase();
  append('<span class="dim">C:\\SETHCYANIDE&gt;</span> ' + raw);
  input.value = ''; typed.textContent = '';
  if (!cmd) return;

  if (cmd === 'help' || cmd === 'help /?') {
    append('<span class="hdr">Available commands:</span>');
    Object.entries(pages).forEach(([k,v]) => append('  '+k.toUpperCase().padEnd(12)+'- Go to '+v.label));
    append('  MUSIC       - Open music player');
    append('  HELP        - Show this list');
    append('  CLS         - Clear screen');
    append('  VER         - Version info');
    append('  DIR         - List pages');
    Object.values(reflexGames).forEach(g => append('  '+g.cmd.toUpperCase().padEnd(12)+'- '+g.label+' (minigame)'));
    return;
  }
  if (cmd === 'cls') { out.innerHTML = ''; return; }
  if (cmd === 'ver') {
    append('<span class="hdr">SethCyanide Terminal [Version 1.0]</span>');
    append('<span class="dim">sethcyanide.do.am - Terminal Navigation v1.0</span>');
    return;
  }
  if (cmd === 'dir') {
    append('<span class="hdr"> Volume in drive C has no label.\n Directory of C:\\SETHCYANIDE</span>\n');
    Object.entries(pages).forEach(([k]) => append('01/01/99  12:00AM    &lt;PAGE&gt;    '+k.toUpperCase()));
    append('<span class="dim">       '+Object.keys(pages).length+' page(s)</span>');
    return;
  }
  if (pages[cmd]) {
    append('<span class="warn">Navigating to: '+pages[cmd].label+'</span>');
    setTimeout(() => { window.location.href = pages[cmd].url; }, 500);
    return;
  }
  if (secrets[cmd]) {
    append('<span class="warn">Initiating security override...</span>');
    setTimeout(() => startHack(secrets[cmd]), 400); return;
  }
  if (cmd === gameCommand.cmd) {
    append('<span class="warn">Loading cartridge module...</span>');
    setTimeout(() => startEmulator(), 400); return;
  }
  const reflexMatch = Object.values(reflexGames).find(g => g.cmd === cmd);
  if (reflexMatch) {
    append('<span class="warn">Calibrating sync protocol...</span>');
    setTimeout(() => startReflex(reflexMatch), 400); return;
  }
  if (cmd === musicCmd) {
    append('<span class="warn">Opening media module...</span>');
    setTimeout(() => openMusicPlayer(), 400); return;
  }
  append('<span class="err">\''+raw+'\' is not recognized as an internal\nor external command, operable program or batch file.</span>');
});

function append(html) {
  out.innerHTML += html + '\n';
  out.scrollTop = out.scrollHeight;
}

/* ═══════════════════════════════════════
   HACKING MINIGAME
   ═══════════════════════════════════════ */
const WORDLIST = ['REACTOR','STATIC','VECTOR','CIPHER','BUNKER','SENTRY','MODULE','ENGINE','SIGNAL','FUSION','HOLLOW','BREACH','RADIUS','SYSTEM','ANCHOR','MATRIX','BEACON','SHADOW'];
const BRACKET_PAIRS = ['()','[]','{}','<>'];
const JUNK = '!@#$%^&*_-+=~|;:,.?/\\'.split('');
let hackState = null;

function randInt(n) { return Math.floor(Math.random()*n); }

function sameLetterCount(a,b) {
  let s=0; for(let i=0;i<a.length;i++) if(a[i]===b[i]) s++; return s;
}

function buildHackPool(wordLen) {
  const pool=[...new Set(WORDLIST.filter(w=>w.length===wordLen))];
  for(let attempt=0;attempt<30;attempt++){
    const shuffled=[...pool].sort(()=>Math.random()-0.5).slice(0,8);
    if(shuffled.length<4) continue;
    const answer=shuffled[randInt(shuffled.length)];
    const ambiguous=shuffled.filter((w,i)=>w!==answer&&sameLetterCount(w,answer)===wordLen).length;
    if(ambiguous===0) return {candidates:shuffled,answer};
  }
  const fallback=[...pool].sort(()=>Math.random()-0.5).slice(0,8);
  return {candidates:fallback,answer:fallback[0]};
}

function startHack(target) {
  const {candidates,answer}=buildHackPool(6);
  hackState={target,answer,candidates,attemptsLeft:4,locked:false,history:[]};
  document.getElementById('hackOverlay').classList.add('active');
  document.getElementById('hackFeed').innerHTML='';
  document.getElementById('hackHistory').innerHTML='';
  renderAttempts();
  feed('<span class="warn">SETHCYANIDE TERMLINK PROTOCOL</span>');
  feed('ENTER PASSWORD NOW');
  renderHackGrid();
}

function renderAttempts(){
  const wrap=document.getElementById('hackAttempts');
  wrap.innerHTML='';
  for(let i=0;i<4;i++){
    const d=document.createElement('div');
    d.className='hack-attempt-dot'+(i>=hackState.attemptsLeft?' used':'');
    wrap.appendChild(d);
  }
}

function feed(html){
  const f=document.getElementById('hackFeed');
  const p=document.createElement('div');
  p.innerHTML=html; f.appendChild(p); f.scrollTop=f.scrollHeight;
}

function addrLabel(i){ return '0x'+(0xF000+i*8).toString(16).toUpperCase(); }

function genJunk(len){
  let s='',i=0;
  while(i<len){
    if(Math.random()<0.12&&i<len-1){s+=BRACKET_PAIRS[randInt(BRACKET_PAIRS.length)];i+=2;}
    else{s+=JUNK[randInt(JUNK.length)];i++;}
  }
  return s.slice(0,len);
}

function renderHackGrid(){
  const colA=document.getElementById('hackColA');
  const colB=document.getElementById('hackColB');
  colA.innerHTML=''; colB.innerHTML='';
  const colWidth=colA.clientWidth||200,colHeight=colA.clientHeight||300;
  const lineLen=Math.max(10,Math.min(20,Math.floor((colWidth-60-30)/9.5)));
  const totalLines=Math.max(8,Math.min(20,Math.floor(colHeight/24)));
  const placements=[];
  hackState.candidates.forEach(w=>{
    let tries=0;
    while(tries<20){
      const line=randInt(totalLines),col=randInt(2),startPos=randInt(lineLen-w.length);
      const overlap=placements.some(p=>p.line===line&&p.col===col&&!(startPos+w.length<=p.start||startPos>=p.start+p.len));
      if(!overlap){placements.push({word:w,line,col,start:startPos,len:w.length});break;}
      tries++;
    }
  });
  for(let l=0;l<totalLines;l++){
    [0,1].forEach(ci=>{
      const lineWords=placements.filter(p=>p.line===l&&p.col===ci).sort((a,b)=>a.start-b.start);
      let cursor=0;
      const rowEl=document.createElement('div'); rowEl.className='hack-line';
      const addr=document.createElement('span'); addr.className='hack-addr'; addr.textContent=addrLabel(l+ci*totalLines); rowEl.appendChild(addr);
      const bytesEl=document.createElement('span'); bytesEl.className='hack-bytes';
      function pushJunk(len){
        const str=genJunk(len); let i=0;
        while(i<str.length){
          if(Math.random()<0.12&&i<str.length-1){
            const pair=BRACKET_PAIRS[randInt(BRACKET_PAIRS.length)];
            const span=document.createElement('span'); span.className='hack-tok bracket'; span.textContent=pair; span.dataset.value=pair;
            bytesEl.appendChild(span); i+=2;
          } else {
            const span=document.createElement('span'); span.className='hack-tok'; span.textContent=str[i]; bytesEl.appendChild(span); i++;
          }
        }
      }
      lineWords.forEach(w=>{
        const gap=w.start-cursor; if(gap>0) pushJunk(gap);
        const span=document.createElement('span'); span.className='hack-tok candidate'; span.textContent=w.word; span.dataset.value=w.word;
        bytesEl.appendChild(span); cursor=w.start+w.len;
      });
      if(cursor<lineLen) pushJunk(lineLen-cursor);
      rowEl.appendChild(bytesEl);
      (ci===0?colA:colB).appendChild(rowEl);
    });
  }
  document.querySelectorAll('.hack-tok.candidate').forEach(el=>el.addEventListener('click',()=>guessWord(el)));
  document.querySelectorAll('.hack-tok.bracket').forEach(el=>el.addEventListener('click',()=>useBracket(el)));
}

function useBracket(el){
  if(hackState.locked) return;
  el.classList.add('touched');
  if(Math.random()<0.5){
    hackState.attemptsLeft=Math.min(4,hackState.attemptsLeft+1);
    feed('<span class="ok">DUD REMOVED. ATTEMPT RESTORED.</span>');
  } else {
    const wrong=hackState.candidates.filter(w=>w!==hackState.answer);
    if(wrong.length>1){
      const rem=wrong[randInt(wrong.length)];
      hackState.candidates=hackState.candidates.filter(w=>w!==rem);
      feed('<span class="warn">DUD REMOVED: '+rem+'</span>');
      renderHackGrid();
    } else { feed('<span class="warn">NO EFFECT.</span>'); }
  }
  renderAttempts(); setTimeout(()=>el.classList.remove('touched'),200);
}

function renderHistory(){
  const wrap=document.getElementById('hackHistory'); wrap.innerHTML='';
  hackState.history.forEach(h=>{
    const row=document.createElement('div'); row.className='hack-history-row';
    row.innerHTML='<span>'+h.word+'</span><span class="hh-match">'+h.same+'/'+h.word.length+'</span>';
    wrap.appendChild(row);
  });
}

function guessWord(el){
  if(hackState.locked) return;
  const word=(el.dataset.value||'').trim().toUpperCase();
  const answer=(hackState.answer||'').trim().toUpperCase();
  feed('&gt; '+word);
  if(word===answer){
    hackState.locked=true;
    feed('<span class="ok">ACCESS GRANTED</span>');
    el.classList.add('touched');
    setTimeout(()=>{ window.location.href=hackState.target.url; },700);
    return;
  }
  hackState.attemptsLeft--;
  const same=sameLetterCount(word,answer);
  hackState.history.push({word,same}); renderHistory();
  feed('<span class="err">ENTRY DENIED</span> &mdash; <span class="warn">'+same+'/'+word.length+' CORRECT</span>');
  renderAttempts();
  if(hackState.attemptsLeft<=0){
    hackState.locked=true;
    feed('<span class="err">TERMINAL LOCKED</span>');
    feed('<span class="dim">REDIRECTING...</span>');
    setTimeout(()=>{ window.location.href=hackState.target.failUrl||'/'; },1200);
  }
}

window.addEventListener('resize',()=>{
  if(hackState&&document.getElementById('hackOverlay').classList.contains('active')&&!hackState.locked) renderHackGrid();
});

/* ═══════════════════════════════════════
   REFLEX MINIGAME
   ═══════════════════════════════════════ */
let reflexState=null, reflexAnimFrame=null;
const reflexOverlay   = document.getElementById('reflexOverlay');
const reflexLabel     = document.getElementById('reflexLabel');
const reflexRoundEl   = document.getElementById('reflexRound');
const reflexInstr     = document.getElementById('reflexInstructions');
const reflexTrack     = document.querySelector('.reflex-track');
const reflexZone      = document.getElementById('reflexZone');
const reflexBarEl     = document.getElementById('reflexBar');
const reflexButton    = document.getElementById('reflexButton');
const reflexResult    = document.getElementById('reflexResult');

function startReflex(config){
  reflexState={config,round:1,totalRounds:config.rounds,hits:0,direction:1,position:0,speed:1.6,zoneStart:0,zoneWidth:0,locked:false,awaitingTap:true};
  reflexLabel.textContent=config.label;
  reflexOverlay.classList.add('active');
  reflexResult.textContent='\u00A0'; reflexResult.className='reflex-result';
  setupReflexRound();
}

function setupReflexRound(){
  const tw=reflexTrack.clientWidth||320;
  const zw=Math.max(40,tw*(0.22-reflexState.round*0.02));
  const zs=20+Math.random()*Math.max(10,tw-zw-40);
  reflexState.zoneStart=zs; reflexState.zoneWidth=zw;
  reflexState.position=0; reflexState.direction=1;
  reflexState.speed=1.8+reflexState.round*0.6; reflexState.awaitingTap=true;
  reflexZone.style.left=zs+'px'; reflexZone.style.width=zw+'px';
  reflexRoundEl.textContent='ROUND '+reflexState.round+'/'+reflexState.totalRounds;
  reflexInstr.textContent='TAP WHEN THE BAR HITS THE ZONE';
  cancelAnimationFrame(reflexAnimFrame); reflexAnimLoop();
}

function reflexAnimLoop(){
  if(!reflexState||reflexState.locked) return;
  const tw=reflexTrack.clientWidth||320;
  reflexState.position+=reflexState.direction*reflexState.speed;
  if(reflexState.position>=tw-4){reflexState.position=tw-4;reflexState.direction=-1;}
  if(reflexState.position<=0){reflexState.position=0;reflexState.direction=1;}
  reflexBarEl.style.left=reflexState.position+'px';
  reflexAnimFrame=requestAnimationFrame(reflexAnimLoop);
}

reflexButton.addEventListener('click',()=>{
  if(!reflexState||reflexState.locked||!reflexState.awaitingTap) return;
  reflexState.awaitingTap=false;
  const inZone=reflexState.position>=reflexState.zoneStart&&reflexState.position<=(reflexState.zoneStart+reflexState.zoneWidth);
  if(inZone){
    reflexState.hits++;
    if(reflexState.hits>=reflexState.totalRounds){ reflexWin(); }
    else {
      reflexResult.textContent='NICE! ROUND '+reflexState.hits+' CLEAR';
      reflexResult.className='reflex-result win'; reflexState.round++;
      setTimeout(()=>setupReflexRound(),600);
    }
  } else { reflexLose(); }
});

function reflexWin(){
  reflexState.locked=true; cancelAnimationFrame(reflexAnimFrame);
  reflexResult.textContent='SYNC COMPLETE'; reflexResult.className='reflex-result win';
  reflexInstr.textContent='ACCESS GRANTED';
  setTimeout(()=>{
    if(reflexState.config.unlockUrl){ window.location.href=reflexState.config.unlockUrl; }
    else { reflexOverlay.classList.remove('active'); append('<span class="ok">Sync test passed.</span>'); input.focus(); }
  },1200);
}

function reflexLose(){
  reflexState.locked=true; cancelAnimationFrame(reflexAnimFrame);
  reflexResult.textContent='MISSED IT'; reflexResult.className='reflex-result lose';
  reflexInstr.textContent='SYNC FAILED';
  setTimeout(()=>{ reflexOverlay.classList.remove('active'); append('<span class="err">Sync test failed.</span>'); input.focus(); },1200);
}

window.addEventListener('resize',()=>{
  if(reflexState&&!reflexState.locked&&reflexOverlay.classList.contains('active')) setupReflexRound();
});

/* ═══════════════════════════════════════
   MUSIC PLAYER + BUTTERCHURN VISUALIZER
   ═══════════════════════════════════════ */
const musicOverlay  = document.getElementById('musicOverlay');
const musicClose    = document.getElementById('musicClose');
const vizToggleBtn  = document.getElementById('vizToggleBtn');
const tracklistEl   = document.getElementById('musicTracklist');
const nowPlayingEl  = document.getElementById('nowPlaying');
const progressBar   = document.getElementById('progressBar');
const progressWrap  = document.getElementById('progressWrap');
const musicTimeEl   = document.getElementById('musicTime');
const playBtn       = document.getElementById('playBtn');
const prevBtn       = document.getElementById('prevBtn');
const nextBtn       = document.getElementById('nextBtn');
const shuffleBtn    = document.getElementById('shuffleBtn');
const volSlider     = document.getElementById('volSlider');
const milkCanvas    = document.getElementById('milkCanvas');

let audioEl = null, audioCtx = null, analyser = null, sourceNode = null;
let currentTrack = -1, isShuffling = false, vizActive = false;
let butterchurn = null, milkRenderer = null, milkAnimFrame = null;
let butterchurnLoaded = false;

function fmt(s){ const m=Math.floor(s/60),sec=Math.floor(s%60); return m+':'+(sec<10?'0':'')+sec; }

function buildTracklist(){
  tracklistEl.innerHTML='';
  tracks.forEach((t,i)=>{
    const row=document.createElement('div'); row.className='music-track'; row.dataset.idx=i;
    row.innerHTML=`<span class="music-track-num">${String(i+1).padStart(2,'0')}</span>
      <div class="music-track-info">
        <div class="music-track-title">${t.title}</div>
        <div class="music-track-artist">${t.artist}</div>
      </div>
      <span class="music-track-dur" id="dur-${i}">-:--</span>`;
    row.addEventListener('click',()=>playTrack(i));
    tracklistEl.appendChild(row);
  });
}

function openMusicPlayer(){
  musicOverlay.classList.add('active');
  if(!tracklistEl.children.length) buildTracklist();
}

musicClose.addEventListener('click',()=>{
  musicOverlay.classList.remove('active');
  stopViz();
  input.focus();
});

/* Audio init */
function initAudio(){
  if(!audioCtx){
    audioCtx=new(window.AudioContext||window.webkitAudioContext)();
    analyser=audioCtx.createAnalyser();
    analyser.fftSize=2048;
    analyser.connect(audioCtx.destination);
  }
}

function playTrack(idx){
  initAudio();
  if(audioEl){ audioEl.pause(); audioEl.src=''; }
  currentTrack=idx;
  document.querySelectorAll('.music-track').forEach(r=>r.classList.remove('playing'));
  const row=document.querySelector('.music-track[data-idx="'+idx+'"]');
  if(row){ row.classList.add('playing'); row.scrollIntoView({block:'nearest'}); }
  audioEl=new Audio(tracks[idx].url);
  audioEl.volume=parseFloat(volSlider.value);
  audioEl.crossOrigin='anonymous';
  if(sourceNode){ try{sourceNode.disconnect();}catch(e){} }
  sourceNode=audioCtx.createMediaElementSource(audioEl);
  sourceNode.connect(analyser);
  audioEl.play().catch(()=>{});
  nowPlayingEl.textContent=tracks[idx].title+' — '+tracks[idx].artist;
  playBtn.innerHTML='&#9646;&#9646;';
  audioEl.addEventListener('timeupdate',updateProgress);
  audioEl.addEventListener('ended',()=>{ playTrack((currentTrack+1)%tracks.length); });
  audioEl.addEventListener('loadedmetadata',()=>{
    const dur=document.getElementById('dur-'+idx);
    if(dur) dur.textContent=fmt(audioEl.duration);
  });
}

function updateProgress(){
  if(!audioEl||!audioEl.duration) return;
  const pct=(audioEl.currentTime/audioEl.duration)*100;
  progressBar.style.width=pct+'%';
  musicTimeEl.textContent=fmt(audioEl.currentTime)+' / '+fmt(audioEl.duration);
}

playBtn.addEventListener('click',()=>{
  if(!audioEl){if(tracks.length) playTrack(0); return;}
  if(audioEl.paused){ audioEl.play(); playBtn.innerHTML='&#9646;&#9646;'; }
  else { audioEl.pause(); playBtn.innerHTML='&#9654;'; }
});
prevBtn.addEventListener('click',()=>{ playTrack(((currentTrack-1)+tracks.length)%tracks.length); });
nextBtn.addEventListener('click',()=>{
  if(isShuffling) playTrack(Math.floor(Math.random()*tracks.length));
  else playTrack((currentTrack+1)%tracks.length);
});
shuffleBtn.addEventListener('click',()=>{
  isShuffling=!isShuffling;
  shuffleBtn.classList.toggle('active-btn',isShuffling);
});
volSlider.addEventListener('input',()=>{ if(audioEl) audioEl.volume=parseFloat(volSlider.value); });
progressWrap.addEventListener('click',e=>{
  if(!audioEl||!audioEl.duration) return;
  const rect=progressWrap.getBoundingClientRect();
  audioEl.currentTime=((e.clientX-rect.left)/rect.width)*audioEl.duration;
});

/* Butterchurn / MilkDrop */
function loadButterchurn(cb){
  if(butterchurnLoaded){cb();return;}
  const s1=document.createElement('script');
  s1.src='https://cdn.jsdelivr.net/npm/butterchurn@2.6.7/lib/butterchurn.min.js';
  s1.onload=()=>{
    const s2=document.createElement('script');
    s2.src='https://cdn.jsdelivr.net/npm/butterchurn-presets@2.4.7/lib/butterchurnPresets.min.js';
    s2.onload=()=>{ butterchurnLoaded=true; cb(); };
    document.head.appendChild(s2);
  };
  document.head.appendChild(s1);
}

function startViz(){
  if(!analyser){ nowPlayingEl.textContent='PLAY A TRACK FIRST'; return; }
  loadButterchurn(()=>{
    milkCanvas.classList.add('active');
    milkCanvas.width=milkCanvas.clientWidth;
    milkCanvas.height=milkCanvas.clientHeight;
    milkRenderer=window.butterchurn.default.createRenderer(audioCtx,milkCanvas,{width:milkCanvas.width,height:milkCanvas.height});
    const presets=window.butterchurnPresets.getPresets();
    const presetKeys=Object.keys(presets);
    milkRenderer.loadPreset(presets[presetKeys[Math.floor(Math.random()*presetKeys.length)]],0.0);
    milkRenderer.connectAudio(analyser);
    let presetTimer=setInterval(()=>{
      const k=presetKeys[Math.floor(Math.random()*presetKeys.length)];
      milkRenderer.loadPreset(presets[k],2.7);
    },15000);
    milkCanvas._presetTimer=presetTimer;
    vizActive=true;
    function renderMilk(){
      if(!vizActive){return;}
      milkRenderer.render();
      milkAnimFrame=requestAnimationFrame(renderMilk);
    }
    renderMilk();
  });
}

function stopViz(){
  vizActive=false;
  cancelAnimationFrame(milkAnimFrame);
  milkCanvas.classList.remove('active');
  if(milkCanvas._presetTimer) clearInterval(milkCanvas._presetTimer);
}

vizToggleBtn.addEventListener('click',()=>{
  if(vizActive){ stopViz(); vizToggleBtn.textContent='VISUALIZER'; }
  else { startViz(); vizToggleBtn.textContent='TRACKLIST'; }
});

window.addEventListener('resize',()=>{
  if(vizActive&&milkRenderer){
    milkCanvas.width=milkCanvas.clientWidth;
    milkCanvas.height=milkCanvas.clientHeight;
    milkRenderer.setRendererSize(milkCanvas.width,milkCanvas.height);
  }
});

/* ═══════════════════════════════════════
   EMULATOR
   ═══════════════════════════════════════ */
let emuStarted=false;
document.getElementById('emuClose').addEventListener('click',()=>{
  document.getElementById('emuOverlay').classList.remove('active'); input.focus();
});
function startEmulator(){
  document.getElementById('emuOverlay').classList.add('active');
  if(emuStarted) return; emuStarted=true;
  window.EJS_player='#emuContainer'; window.EJS_core=gameCommand.core;
  window.EJS_gameUrl=gameCommand.romUrl;
  window.EJS_pathtodata='https://cdn.jsdelivr.net/npm/emulatorjs@latest/data/';
  window.EJS_startOnLoaded=true; window.EJS_backgroundColor='#000000';
  window.EJS_onGameStart=function(){ const l=document.getElementById('emuLoading'); if(l) l.remove(); };
  const s=document.createElement('script');
  s.src='https://cdn.jsdelivr.net/npm/emulatorjs@latest/data/loader.js';
  document.body.appendChild(s);
}
/* ═══════════════════════════════════════
   GLITTER PARTICLE SYSTEM
   ═══════════════════════════════════════ */
(function(){
  const canvas = document.getElementById('glitterCanvas');
  const ctx = canvas.getContext('2d');
  let W, H, particles = [];

  /* Pull the current primary color from CSS variables for theme-aware sparkles */
  function getPrimaryRGB(){
    const v = getComputedStyle(document.documentElement).getPropertyValue('--primary').trim();
    const m = v.match(/^#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i);
    if(m) return [parseInt(m[1],16), parseInt(m[2],16), parseInt(m[3],16)];
    return [255,255,255];
  }

  function resize(){
    W = canvas.width  = canvas.offsetWidth;
    H = canvas.height = canvas.offsetHeight;
  }
  window.addEventListener('resize', resize);
  resize();

  /* Particle types: tiny dot, 4-point star, small cross */
  function randomShape(){ return ['dot','star','cross'][Math.floor(Math.random()*3)]; }

  function spawn(){
    const [r,g,b] = getPrimaryRGB();
    /* Mix between pure white, theme primary, and a near-white tint for variety */
    const toss = Math.random();
    let cr,cg,cb;
    if(toss < 0.4){       cr=255;cg=255;cb=255; }           /* white sparkle */
    else if(toss < 0.75){ cr=r;cg=g;cb=b; }                /* theme color   */
    else {                cr=Math.round((r+255)/2);cg=Math.round((g+255)/2);cb=Math.round((b+255)/2); } /* pastel mix */

    return {
      x:  Math.random() * W,
      y:  Math.random() * H,
      size: 0.5 + Math.random() * 1.8,
      alpha: 0,
      alphaDir: 1,
      alphaSpeed: 0.008 + Math.random() * 0.018,
      maxAlpha: 0.25 + Math.random() * 0.35,
      vx: (Math.random() - 0.5) * 0.12,
      vy: (Math.random() - 0.5) * 0.12,
      shape: randomShape(),
      r:cr, g:cg, b:cb,
      rotation: Math.random() * Math.PI * 2,
      rotSpeed: (Math.random() - 0.5) * 0.02,
    };
  }

  /* Seed initial particles spread across the whole screen */
  const PARTICLE_COUNT = 55;
  for(let i=0;i<PARTICLE_COUNT;i++){
    const p = spawn();
    p.alpha = Math.random() * p.maxAlpha; /* start at random phase */
    particles.push(p);
  }

  function drawStar(ctx, x, y, size){
    ctx.beginPath();
    for(let i=0;i<4;i++){
      const a = (Math.PI/2)*i;
      ctx.moveTo(x, y);
      ctx.lineTo(x + Math.cos(a)*size*2, y + Math.sin(a)*size*2);
    }
    ctx.stroke();
  }

  function drawCross(ctx, x, y, size){
    ctx.beginPath();
    ctx.moveTo(x - size*1.5, y); ctx.lineTo(x + size*1.5, y);
    ctx.moveTo(x, y - size*1.5); ctx.lineTo(x, y + size*1.5);
    ctx.stroke();
  }

  function tick(){
    ctx.clearRect(0,0,W,H);
    particles.forEach(p => {
      p.x += p.vx; p.y += p.vy;
      p.rotation += p.rotSpeed;
      p.alpha += p.alphaDir * p.alphaSpeed;

      if(p.alpha >= p.maxAlpha){ p.alpha = p.maxAlpha; p.alphaDir = -1; }
      if(p.alpha <= 0){
        /* respawn at new position when fully faded */
        Object.assign(p, spawn());
        p.alpha = 0; p.alphaDir = 1;
      }

      /* wrap edges */
      if(p.x < -4) p.x = W+4;
      if(p.x > W+4) p.x = -4;
      if(p.y < -4) p.y = H+4;
      if(p.y > H+4) p.y = -4;

      ctx.save();
      ctx.globalAlpha = p.alpha;
      ctx.strokeStyle = `rgb(${p.r},${p.g},${p.b})`;
      ctx.fillStyle   = `rgb(${p.r},${p.g},${p.b})`;
      ctx.lineWidth   = p.size * 0.6;
      ctx.translate(p.x, p.y);
      ctx.rotate(p.rotation);

      if(p.shape === 'dot'){
        ctx.beginPath();
        ctx.arc(0,0,p.size,0,Math.PI*2);
        ctx.fill();
      } else if(p.shape === 'star'){
        drawStar(ctx,0,0,p.size);
      } else {
        drawCross(ctx,0,0,p.size);
      }
      ctx.restore();
    });
    requestAnimationFrame(tick);
  }
  tick();
})();
</script>
</body>
</html>
