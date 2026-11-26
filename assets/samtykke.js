/* Samtykke til informasjonskapsler + Google Analytics.
   Google Analytics lastes BARE etter at den besøkende har trykket «Godta».
   Lim inn måle-ID-en fra Google Analytics her. Er den tom, vises ingen banner og ingenting lastes. */
(function () {
  var GA_ID = ''; // f.eks. 'G-ABC123XYZ'

  var KEY = 'bv-samtykke', MAX_AGE = 365 * 24 * 3600 * 1000;
  var doc = document;

  function read() {
    try {
      var v = JSON.parse(localStorage.getItem(KEY) || 'null');
      if (v && (v.svar === 'ja' || v.svar === 'nei') && Date.now() - v.tid < MAX_AGE) return v.svar;
    } catch (e) {}
    return null;
  }
  function save(svar) { try { localStorage.setItem(KEY, JSON.stringify({ svar: svar, tid: Date.now() })); } catch (e) {} }

  var loaded = false;
  function loadGA() {
    if (loaded || !GA_ID) return;
    loaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    gtag('consent', 'default', { analytics_storage: 'granted', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' });
    gtag('js', new Date());
    gtag('config', GA_ID, { allow_google_signals: false, allow_ad_personalization_signals: false });
    var s = doc.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA_ID);
    doc.head.appendChild(s);
  }
  function dropGA() {
    if (window.gtag) gtag('consent', 'update', { analytics_storage: 'denied' });
    var host = location.hostname.replace(/^www\./, '');
    doc.cookie.split(';').forEach(function (c) {
      var name = c.split('=')[0].trim();
      if (/^_ga/.test(name)) {
        ['', '; domain=' + host, '; domain=.' + host].forEach(function (d) {
          doc.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + d;
        });
      }
    });
  }

  var banner;
  function close() { if (banner) { banner.remove(); banner = null; } }
  function answer(svar) {
    save(svar);
    if (svar === 'ja') loadGA(); else dropGA();
    close();
    var st = doc.getElementById('samtykkeStatus');
    if (st) st.textContent = svar === 'ja' ? 'Du har godtatt måling.' : 'Du har avslått måling.';
  }
  function show() {
    if (!GA_ID || banner) return;
    banner = doc.createElement('section');
    banner.className = 'consent';
    banner.setAttribute('aria-label', 'Informasjonskapsler');
    banner.innerHTML =
      '<p><b>Får vi måle besøket ditt?</b> Vi vil bruke Google Analytics til å se hvordan siden brukes, så vi kan gjøre den bedre. ' +
      'Det setter informasjonskapsler. Siden virker helt likt om du sier nei. <a href="/personvern.html#informasjonskapsler">Les mer</a></p>' +
      '<div class="consent__btns"><button type="button" class="btn btn--ghost" data-svar="nei">Avslå</button>' +
      '<button type="button" class="btn btn--ghost" data-svar="ja">Godta</button></div>';
    banner.addEventListener('click', function (e) {
      var b = e.target.closest('[data-svar]');
      if (b) answer(b.getAttribute('data-svar'));
    });
    doc.body.appendChild(banner);
  }

  // Lenker/knapper med data-samtykke åpner valget på nytt (bunnen av siden, personvern-siden)
  function wire() {
    doc.querySelectorAll('[data-samtykke]').forEach(function (el) {
      if (!GA_ID) { var li = el.closest('li'); (li || el).hidden = true; return; }
      el.addEventListener('click', function (e) { e.preventDefault(); close(); show(); var b = banner && banner.querySelector('button'); if (b) b.focus(); });
    });
    var st = doc.getElementById('samtykkeStatus'), cur = read();
    if (st) st.textContent = !GA_ID ? 'Vi måler ikke besøk på siden nå.' : cur === 'ja' ? 'Du har godtatt måling.' : cur === 'nei' ? 'Du har avslått måling.' : 'Du har ikke valgt ennå.';
  }

  function start() {
    wire();
    var cur = read();
    if (cur === 'ja') loadGA();
    else if (cur === null) show();
  }
  if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', start); else start();
})();
