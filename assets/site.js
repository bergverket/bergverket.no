(function () {
  var doc = document;

  // Mobilmeny
  var btn = doc.querySelector('.menu-btn'), nav = doc.getElementById('meny');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') !== 'true';
      btn.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('open', open);
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) { btn.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); }
    });
    doc.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) { btn.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); btn.focus(); }
    });
  }

  // Skjul menylenker til seksjoner som er fjernet (f.eks. casen)
  doc.querySelectorAll('[data-needs]').forEach(function (a) {
    if (!doc.getElementById(a.getAttribute('data-needs'))) a.hidden = true;
  });

  // Dybdemåler + aktiv menylenke
  var layers = [].slice.call(doc.querySelectorAll('[data-depth]'));
  var read = doc.getElementById('gaugeRead'), name = doc.getElementById('gaugeName'), rail = doc.getElementById('gaugeRail');
  var links = {};
  doc.querySelectorAll('.nav a[href^="#"]').forEach(function (a) { links[a.getAttribute('href').slice(1)] = a; });
  var maxDepth = layers.length ? +layers[layers.length - 1].dataset.depth : 0;
  var ticking = false;
  function update() {
    ticking = false;
    var y = window.scrollY + window.innerHeight * 0.35, depth = 0, cur = layers[0];
    for (var i = 0; i < layers.length; i++) {
      var top = layers[i].offsetTop, d = +layers[i].dataset.depth;
      if (y >= top) {
        cur = layers[i];
        var next = layers[i + 1];
        if (next) {
          var t = Math.min(1, (y - top) / Math.max(1, next.offsetTop - top));
          depth = d + (+next.dataset.depth - d) * t;
        } else depth = d;
      }
    }
    if (window.innerHeight + window.scrollY >= doc.documentElement.scrollHeight - 2) { depth = maxDepth; cur = layers[layers.length - 1]; }
    if (read) {
      read.textContent = (depth > 0.5 ? '−' : '') + Math.round(depth) + ' m';
      name.textContent = cur.dataset.name;
      rail.style.setProperty('--p', maxDepth ? depth / maxDepth : 0);
    }
    for (var k in links) links[k].removeAttribute('aria-current');
    if (cur && links[cur.id]) links[cur.id].setAttribute('aria-current', 'true');
  }
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(update); } }
  if (layers.length) { window.addEventListener('scroll', onScroll, { passive: true }); window.addEventListener('resize', onScroll); update(); }

  // Glid inn når seksjoner kommer til syne
  var rev = doc.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (ents) {
      ents.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    rev.forEach(function (el) { io.observe(el); });
  } else rev.forEach(function (el) { el.classList.add('in'); });

  // Tall i casen teller opp når de kommer til syne
  var nums = [].slice.call(doc.querySelectorAll('.fact b, .case-facts b')).filter(function (b) { return /^\d+\+?$/.test(b.textContent.trim()); });
  if (nums.length && 'IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var cio = new IntersectionObserver(function (ents) {
      ents.forEach(function (e) {
        if (!e.isIntersecting) return;
        cio.unobserve(e.target);
        var el = e.target, txt = el.textContent.trim(), end = parseInt(txt, 10), plus = /\+$/.test(txt), t0 = null;
        if (end < 10) return;
        function step(t) {
          if (!t0) t0 = t;
          var k = Math.min(1, (t - t0) / 1100), v = Math.round(end * (1 - Math.pow(1 - k, 3)));
          el.textContent = v + (plus ? '+' : '');
          if (k < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    }, { threshold: .6 });
    nums.forEach(function (b) { cio.observe(b); });
  }

  // Kopier e-post
  var copyBtn = doc.getElementById('copyBtn'), msg = doc.getElementById('copyMsg'), mail = doc.getElementById('mail');
  if (copyBtn) copyBtn.addEventListener('click', function () {
    var text = mail.textContent.trim();
    function fallback() {
      var r = doc.createRange(); r.selectNodeContents(mail);
      var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
      msg.textContent = 'Adressen er markert. Kopier den med Cmd+C eller Ctrl+C.';
    }
    try { navigator.clipboard.writeText(text).then(function () { msg.textContent = 'Kopiert.'; copyBtn.textContent = 'Kopiert'; setTimeout(function () { copyBtn.textContent = 'Kopier'; }, 2000); }, fallback); }
    catch (e) { fallback(); }
  });

  // Skjema: lager en ferdig e-post
  var form = doc.getElementById('brief');
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    var err = doc.getElementById('formErr'), bad = null;
    ['f-navn', 'f-om'].forEach(function (id) {
      var el = doc.getElementById(id), empty = !el.value.trim();
      el.setAttribute('aria-invalid', String(empty));
      if (empty && !bad) bad = el;
    });
    if (bad) { err.textContent = 'Fyll inn navn og litt om hva du trenger.'; bad.focus(); return; }
    err.textContent = '';
    var f = form.elements, hva = [].slice.call(form.querySelectorAll('input[name="hva"]:checked')).map(function (c) { return c.value; });
    var subject = 'Prosjekt: ' + (f.firma.value.trim() || f.navn.value.trim());
    var body = [
      'Hei Bergverket!', '',
      f.om.value.trim(), '',
      'Trenger: ' + (hva.join(', ') || 'Usikker'),
      f.side.value.trim() ? 'Nettside i dag: ' + f.side.value.trim() : '',
      '', 'Hilsen ' + f.navn.value.trim() + (f.firma.value.trim() ? ', ' + f.firma.value.trim() : '')
    ].filter(function (l, i, a) { return !(l === '' && a[i - 1] === ''); }).join('\n');
    window.location.href = 'mailto:hei@bergverket.no?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);

    // Reserve hvis e-postprogrammet ikke åpner (vanlig med Gmail i nettleseren)
    var sent = doc.getElementById('sent');
    if (sent) {
      doc.getElementById('gmailLink').href = 'https://mail.google.com/mail/?view=cm&fs=1&to=hei@bergverket.no&su=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      var cb = doc.getElementById('copyBrief'), sm = doc.getElementById('sentMsg');
      cb.onclick = function () {
        var text = 'Til: hei@bergverket.no\nEmne: ' + subject + '\n\n' + body;
        try { navigator.clipboard.writeText(text).then(function () { sm.textContent = 'Kopiert. Lim inn i en ny e-post til hei@bergverket.no.'; }, function () { sm.textContent = 'Fikk ikke kopiert. Skriv til hei@bergverket.no.'; }); }
        catch (e2) { sm.textContent = 'Fikk ikke kopiert. Skriv til hei@bergverket.no.'; }
      };
      setTimeout(function () { sent.hidden = false; }, 600);
    }
  });
})();
