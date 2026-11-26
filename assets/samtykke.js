/* Samtykke til informasjonskapsler: Google Analytics (statistikk) og Meta-pikselen (markedsføring).
   Ingenting lastes før den besøkende har valgt. Tre like store knapper: Avslå, Bare statistikk, Godta alt.
   GA_ID / META_PIXEL_ID: lim inn ID-ene her. Er META_PIXEL_ID tom, vises bare Avslå/Godta for statistikk.
   Hendelser: window.bvMal('Lead') / bvMal('Contact') sender til begge, men bare hvis samtykket dekker det. */
(function () {
  var GA_ID = 'G-NTHLWEHQT3';
  var META_PIXEL_ID = '1836795680873219';

  var KEY = 'bv-samtykke', MAX_AGE = 365 * 24 * 3600 * 1000;
  var doc = document;
  var harMeta = !!META_PIXEL_ID;

  // svar: 'alt' (statistikk + markedsføring), 'stat' (bare statistikk), 'nei'.
  // Gamle valg fra før Meta kom inn: 'ja' = bare statistikk, og vi spør på nytt om markedsføring.
  function read() {
    try {
      var v = JSON.parse(localStorage.getItem(KEY) || 'null');
      if (!v || Date.now() - v.tid >= MAX_AGE) return null;
      if (v.svar === 'ja') return 'stat-gammel';
      if (v.svar === 'alt' || v.svar === 'stat' || v.svar === 'nei') return v.svar;
    } catch (e) {}
    return null;
  }
  function save(svar) { try { localStorage.setItem(KEY, JSON.stringify({ svar: svar, tid: Date.now() })); } catch (e) {} }

  var gaLoaded = false, metaLoaded = false;
  function loadGA() {
    if (gaLoaded || !GA_ID) return;
    gaLoaded = true;
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
  function loadMeta() {
    if (metaLoaded || !harMeta) return;
    metaLoaded = true;
    /* Metas standardkode for pikselen */
    !function (f, b, e, v, n, t, s) {
      if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
      if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = [];
      t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
    }(window, doc, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
    fbq('consent', 'grant');
    fbq('init', META_PIXEL_ID);
    fbq('track', 'PageView');
  }
  function clearCookies(re) {
    var host = location.hostname.replace(/^www\./, '');
    doc.cookie.split(';').forEach(function (c) {
      var name = c.split('=')[0].trim();
      if (re.test(name)) {
        ['', '; domain=' + host, '; domain=.' + host].forEach(function (d) {
          doc.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + d;
        });
      }
    });
  }
  function dropGA() {
    if (window.gtag) gtag('consent', 'update', { analytics_storage: 'denied' });
    clearCookies(/^_ga/);
  }
  function dropMeta() {
    if (window.fbq) fbq('consent', 'revoke');
    clearCookies(/^_fb[pc]$/);
  }
  function apply(svar) {
    if (svar === 'alt' || svar === 'stat' || svar === 'stat-gammel') loadGA(); else dropGA();
    if (svar === 'alt') loadMeta(); else dropMeta();
  }

  // Hendelser fra siden (skjema, e-postlenker). Sendes bare til det som er godtatt og lastet.
  var GA_NAVN = { Lead: 'generate_lead', Contact: 'contact' };
  window.bvMal = function (navn, data) {
    if (gaLoaded && window.gtag) gtag('event', GA_NAVN[navn] || navn, data || {});
    if (metaLoaded && window.fbq) fbq('track', navn, data || {});
  };

  function statusTekst(cur) {
    if (!GA_ID && !harMeta) return 'Vi måler ikke besøk på siden nå.';
    if (cur === 'alt') return harMeta ? 'Du har godtatt statistikk og markedsføring.' : 'Du har godtatt måling.';
    if (cur === 'stat' || cur === 'stat-gammel') return harMeta ? 'Du har godtatt bare statistikk.' : 'Du har godtatt måling.';
    if (cur === 'nei') return 'Du har avslått alt.';
    return 'Du har ikke valgt ennå.';
  }

  var banner;
  function close() { if (banner) { banner.remove(); banner = null; } }
  function answer(svar) {
    save(svar);
    apply(svar);
    close();
    var st = doc.getElementById('samtykkeStatus');
    if (st) st.textContent = statusTekst(svar);
  }
  function show() {
    if ((!GA_ID && !harMeta) || banner) return;
    banner = doc.createElement('section');
    banner.className = 'consent';
    banner.setAttribute('aria-label', 'Informasjonskapsler');
    banner.innerHTML = harMeta
      ? '<p><b>Får vi måle besøket ditt?</b> Statistikk (Google Analytics) viser oss hvordan siden brukes. ' +
        'Markedsføring (Meta-pikselen) lar oss vise annonser på Facebook og Instagram til folk som har vært her. ' +
        'Begge setter informasjonskapsler. Siden virker helt likt om du sier nei. <a href="/personvern.html#informasjonskapsler">Les mer</a></p>' +
        '<div class="consent__btns consent__btns--3"><button type="button" class="btn btn--ghost" data-svar="nei">Avslå</button>' +
        '<button type="button" class="btn btn--ghost" data-svar="stat">Bare statistikk</button>' +
        '<button type="button" class="btn btn--ghost" data-svar="alt">Godta alt</button></div>'
      : '<p><b>Får vi måle besøket ditt?</b> Vi vil bruke Google Analytics til å se hvordan siden brukes, så vi kan gjøre den bedre. ' +
        'Det setter informasjonskapsler. Siden virker helt likt om du sier nei. <a href="/personvern.html#informasjonskapsler">Les mer</a></p>' +
        '<div class="consent__btns"><button type="button" class="btn btn--ghost" data-svar="nei">Avslå</button>' +
        '<button type="button" class="btn btn--ghost" data-svar="alt">Godta</button></div>';
    banner.addEventListener('click', function (e) {
      var b = e.target.closest('[data-svar]');
      if (b) answer(b.getAttribute('data-svar'));
    });
    doc.body.appendChild(banner);
  }

  // Lenker/knapper med data-samtykke åpner valget på nytt (bunnen av siden, personvern-siden)
  function wire() {
    doc.querySelectorAll('[data-samtykke]').forEach(function (el) {
      if (!GA_ID && !harMeta) { var li = el.closest('li'); (li || el).hidden = true; return; }
      el.addEventListener('click', function (e) { e.preventDefault(); close(); show(); var b = banner && banner.querySelector('button'); if (b) b.focus(); });
    });
    var st = doc.getElementById('samtykkeStatus');
    if (st) st.textContent = statusTekst(read());
    // Klikk på e-postlenker teller som «Contact»
    doc.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('a[href^="mailto:"]');
      if (a) window.bvMal('Contact', { metode: 'e-post' });
    });
  }

  function start() {
    wire();
    var cur = read();
    if (cur) apply(cur);
    if (cur === null || (cur === 'stat-gammel' && harMeta)) show();
  }
  if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', start); else start();
})();
