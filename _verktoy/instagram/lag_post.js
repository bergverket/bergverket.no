// Bergverket – lag Instagram-post (1080x1350) direkte i Instagram-fanen.
// Instagram blokkerer fetch/bilder fra andre domener (CSP), så bildet tegnes på canvas
// i selve instagram.com-fanen og legges i filfeltet med DataTransfer. Full kvalitet, ingen skjermbilder.
//
// Bruk (javascript_tool i instagram.com-fanen, ETTER at «Create»-dialogen er åpnet):
//   1) lim inn hele denne fila, 2) kjør:
//   await __bvPost({kicker:'TIPS', title:[['SLIK BLIR',0],['DU FUNNET',0],['PÅ GOOGLE',1]], body:'Tre gratis grep ...', foot:'BERGVERKET.NO'})
//   title = liste av [tekst, 1 hvis kobberfarget]. Maks ca. 9 tegn per linje i stor skrift.
// Variabler forsvinner når Instagram laster siden på nytt (f.eks. etter «Done»): lim inn igjen.
window.__bvPost = async function ({ kicker = '', title = [], body = '', foot = 'BERGVERKET.NO', size = 200 } = {}) {
  const W = 1080, H = 1350, cv = document.createElement('canvas'); cv.width = W; cv.height = H;
  const x = cv.getContext('2d');
  const BG = '#101315', INK = '#eceae5', ORE = '#e57a41';
  const D = '"DIN Condensed", "Avenir Next Condensed", Impact, sans-serif', M = 'Menlo, monospace', S = '"Helvetica Neue", Helvetica, Arial, sans-serif';
  x.fillStyle = BG; x.fillRect(0, 0, W, H);
  x.fillStyle = '#1c2125'; for (let y = 89; y < H; y += 90) x.fillRect(0, y, W, 1);
  x.save(); x.translate(0, 940);
  x.fillStyle = '#1f2428'; x.fill(new Path2D('M0 410 L0 250 L240 120 L420 220 L640 40 L860 230 L1080 140 L1080 410Z'));
  x.fillStyle = INK; x.fill(new Path2D('M0 410 L0 330 L260 260 L480 320 L760 220 L1080 300 L1080 410Z')); x.restore();
  const t = (s, px, py, font, col, ls) => { x.font = font; x.fillStyle = col; x.letterSpacing = ls || '0px'; x.fillText(s, px, py); x.letterSpacing = '0px'; };
  // logo
  x.save(); x.translate(110, 110); x.scale(90 / 32, 90 / 32);
  x.fillStyle = INK; x.fill(new Path2D('M3.5 26.5 12.5 9.5l4.5 8.3 3.5-5.3 8 14Z'));
  x.fillStyle = BG; x.fill(new Path2D('M11.8 15.2h1.4v7.2h-1.4Z'));
  x.fillStyle = ORE; x.fill(new Path2D('m12.5 20.6 2.6 2.6-2.6 2.6-2.6-2.6Z')); x.restore();
  let y = 280; if (kicker) { t(kicker.toUpperCase(), 110, y, '500 34px ' + M, ORE, '5px'); y += 40; }
  const lh = size * 0.86;
  for (const [s, o] of title) { y += lh; t(s.toUpperCase(), 106, y, 'bold ' + size + 'px ' + D, o ? ORE : INK); }
  if (body) { // ombryt brødtekst
    x.font = '400 42px ' + S; y += 80; let line = '';
    for (const w of body.split(' ')) { const tryL = line ? line + ' ' + w : w; if (x.measureText(tryL).width > 860) { t(line, 110, y, '400 42px ' + S, '#b9bab5'); y += 58; line = w; } else line = tryL; }
    if (line) t(line, 110, y, '400 42px ' + S, '#b9bab5');
  }
  t(foot, 110, 900, '500 34px ' + M, INK, '5px');
  const blob = await new Promise(r => cv.toBlob(r, 'image/jpeg', 0.95));
  const file = new File([blob], 'bergverket-post.jpg', { type: 'image/jpeg' });
  const inp = [...document.querySelectorAll('input[type=file]')].filter(i => /video/.test(i.accept)).pop();
  if (!inp) return 'Fant ikke filfeltet. Åpne «Create» → «Post» først.';
  const dt = new DataTransfer(); dt.items.add(file); inp.files = dt.files; inp.dispatchEvent(new Event('change', { bubbles: true }));
  return 'ok ' + file.size + ' bytes';
};
