// =====================================================================
// FILE: static/app.js
// Bütün frontend məntiqi: Socket.IO klienti + UI helpers + Audio
// =====================================================================
const AVATARS = ['🦁','🐯','🐺','🦊','🐻','🐼','🐸','🦅','🐲','🦄','👑','🎭'];

// ────────────── AUDIO ──────────────
const Audio = (() => {
  let ctx = null;
  const get = () => ctx || (ctx = new (window.AudioContext || window.webkitAudioContext)());
  const beep = (f, d, v = .12, t = 'sine') => {
    try {
      const c = get(), o = c.createOscillator(), g = c.createGain();
      o.connect(g); g.connect(c.destination);
      o.type = t; o.frequency.value = f;
      g.gain.setValueAtTime(v, c.currentTime);
      g.gain.exponentialRampToValueAtTime(.001, c.currentTime + d);
      o.start(); o.stop(c.currentTime + d);
    } catch (e) {}
  };
  return {
    card:      () => { beep(800, .08, .1); setTimeout(() => beep(1000, .06, .08), 80); },
    chip:      () => beep(600, .1, .12, 'triangle'),
    fold:      () => beep(250, .15, .1),
    win:       () => { [0,100,200].forEach...
