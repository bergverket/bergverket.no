# Lager undersider for bergverket.no. Kjør fra repo-roten: python3 _verktoy/lag_sider.py
# Tjenestesider står i SIDER under. Artikler er egne JSON-filer i _verktoy/artikler/ (en fil per artikkel),
# med feltene path, kort, title, desc, h1, lead, body (HTML), faq ([[spm, svar], ...]) og dato (ÅÅÅÅ-MM-DD).
# Ny artikkel: legg til en JSON-fil og kjør skriptet. Det lager også /artikler/, sitemap.xml og lenker i footeren.
import json, os, sys, html, glob

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HER = os.path.dirname(os.path.abspath(__file__))
BASE = "https://bergverket.no"
DATO = "2026-11-26"
LOGO = '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M1.5 28.5 12 8.5l5.2 9.6 4-6.1 9.3 16.5Z" fill="currentColor"/><path d="M11.2 15h1.6v8.6h-1.6Z" fill="#101315"/><path d="m12 21.3 3 3-3 3-3-3Z" fill="#e57a41"/></svg>'

TJENESTER = [
    ("/nettbutikk-shopify/", "Nettbutikk i Shopify"),
    ("/nettside/", "Nettside for bedrifter"),
    ("/automatisering/", "Automatisering med AI-agenter"),
    ("/nettbyra-stavanger/", "Nettbyrå i Stavanger"),
]

SIDER = [
 {
  "path": "/nettbutikk-shopify/",
  "kort": "Nettbutikk i Shopify",
  "title": "Nettbutikk i Shopify · Bergverket nettbyrå",
  "desc": "Vi lager nettbutikker i Shopify for små bedrifter i hele Norge: design, vareimport, Vipps og kort, frakt og vilkår på norsk. Første prat er uforpliktende.",
  "eyebrow": "Tjeneste",
  "h1": "Nettbutikk i Shopify",
  "lead": "Vi bygger nettbutikken din i Shopify, klar til å ta imot ordre fra dag én. Du får én kontakt hele veien, og du eier alt når vi er ferdige.",
  "service": "Nettbutikk i Shopify",
  "body": """
<h2>Dette får du</h2>
<ul class="ticks">
<li>Oppsett av Shopify, tema og design som passer merkevaren din</li>
<li>Import av varer fra regneark, bilder eller kassesystemet du har i dag</li>
<li>Betaling med kort og norske løsninger som Vipps, koblet og testet</li>
<li>Frakt, salgsbetingelser, angrerett og e-poster til kundene på norsk</li>
<li>SEO på kategorier og produkter, så butikken kan bli funnet i Google</li>
<li>Google, Facebook og Instagram koblet til butikken, med måling av salg</li>
<li>Opplæring, så du kan legge inn varer og håndtere ordre selv</li>
</ul>

<h2>Hvorfor Shopify?</h2>
<p>Shopify tar seg av servere, sikkerhet, oppdateringer og betaling. Du betaler et fast månedsbeløp til Shopify og slipper å tenke på drift. Det er enkelt å bruke fra mobilen, og det fungerer med norske betalings- og fraktløsninger.</p>
<p>Har du en butikk på en annen plattform i dag, kan vi flytte varene over. Har du allerede Shopify, kan vi forbedre det du har.</p>

<h2>Slik foregår det</h2>
<ol>
<li><strong>Første prat.</strong> Vi ser på hva du selger og til hvem. Du får et tilbud med pris og plan.</li>
<li><strong>Plan og innhold.</strong> Vi samler varer, bilder, tekster og logo.</li>
<li><strong>Bygging.</strong> Vi setter opp butikken, og du kan klikke rundt og teste underveis.</li>
<li><strong>Åpning.</strong> Vi tester kjøp, frakt og e-poster, og lærer deg å drive butikken.</li>
<li><strong>Drift (valgfritt).</strong> AI-agenter og vi holder butikken ved like etter åpning.</li>
</ol>

<h2>Eksempel: On the Record</h2>
<p>Platesjappa On the Record i Trondheim ville selge brukte plater på nett ved siden av butikken. Vi bygde nettbutikken i Shopify fra bunnen, med eget tema, over 200 plater lagt inn fra bilder og regneark, og kortbetaling, frakt og vilkår på norsk. Butikken åpner 2. desember 2026.</p>
""",
  "faq": [
   ("Hvor lang tid tar det å lage en nettbutikk?", "Det kommer an på hvor mange varer du har og hvor klart innholdet er. Du får en tidsplan sammen med tilbudet etter første prat."),
   ("Hvem eier nettbutikken?", "Du. Shopify-kontoen, domenet og alle kundene står i ditt navn. Vi får tilgang som medarbeidere, og du kan ta den fra oss når du vil."),
   ("Kan jeg legge inn varer selv etterpå?", "Ja. Du får opplæring, og Shopify er laget for at du skal kunne gjøre det fra mobilen. Vil du heller slippe, kan agentene våre legge inn nye varer fra bilder."),
   ("Lager dere nettbutikker for hele Norge?", "Ja. Vi holder til i Stavanger, men jobber digitalt med bedrifter i hele landet."),
  ],
 },
 {
  "path": "/nettside/",
  "kort": "Nettside",
  "title": "Ny nettside for bedriften · Bergverket nettbyrå",
  "desc": "Rask, mobilvennlig nettside som er lett å finne i Google og får folk til å ta kontakt. For små bedrifter i hele Norge. Bergverket, nettbyrå i Stavanger.",
  "eyebrow": "Tjeneste",
  "h1": "Nettside for bedriften din",
  "lead": "En rask og ryddig nettside som viser hvem du er, hva du tilbyr og hvordan folk tar kontakt. Bygget for mobil og for Google fra første linje.",
  "service": "Nettside",
  "body": """
<h2>Dette får du</h2>
<ul class="ticks">
<li>Design som passer bedriften, bygget for mobil først</li>
<li>Korte tekster som sier det viktigste, skrevet sammen med deg</li>
<li>Kontaktskjema, kart, åpningstider og det kundene dine leter etter</li>
<li>Teknisk SEO: titler, beskrivelser, sitemap og strukturerte data for Google</li>
<li>Rask lasting og god tilgjengelighet, også for skjermlesere</li>
<li>Måling av besøk med samtykke, så du ser hva som virker</li>
<li>Domene og e-post satt opp, eller flyttet fra der du har det i dag</li>
</ul>

<h2>Lett å finne i Google</h2>
<p>En nettside hjelper bare hvis folk finner den. Vi setter opp Google Search Console, Google-bedriftsprofilen og strukturerte data, så Google forstår hvem du er, hva du gjør og hvor du holder til. Vi skriver tekstene slik at de svarer på det kundene faktisk søker etter.</p>

<h2>Nettside eller nettbutikk?</h2>
<p>Skal du selge varer direkte på nett, trenger du en <a href="/nettbutikk-shopify/">nettbutikk</a>. Skal folk finne deg, lese om tjenestene og ta kontakt, holder det med en nettside. Er du usikker, finner vi ut av det i første prat.</p>
""",
  "faq": [
   ("Kan jeg oppdatere nettsiden selv?", "Ja. Vi lager den slik at du kan endre tekst og bilder selv, eller sende oss en melding så gjør vi det."),
   ("Kan dere flytte en nettside jeg har fra før?", "Ja. Vi kan bygge en ny side og flytte domenet og innholdet, uten at du mister plasseringen i Google."),
   ("Hva koster en nettside?", "Det kommer an på hvor mange sider og funksjoner du trenger. Etter første prat får du et tilbud med pris og plan."),
  ],
 },
 {
  "path": "/automatisering/",
  "kort": "Automatisering",
  "title": "AI-agenter og automatisering for nettbutikk · Bergverket",
  "desc": "AI-agenter som skriver produkttekster, legger inn varer, sjekker butikken og sender ukesrapport. Et menneske godkjenner alt. Bergverket, nettbyrå i Stavanger.",
  "eyebrow": "Tjeneste",
  "h1": "Agenter som tar de faste oppgavene",
  "lead": "Hver kunde får egne AI-agenter som kjenner butikken og gjør det som ellers blir liggende: tekster, varer, sjekker og rapporter. Vi følger med og tar avgjørelsene.",
  "service": "Automatisering med AI-agenter",
  "body": """
<h2>Hva agentene kan gjøre</h2>
<ul class="ticks">
<li>Skrive produkttekster og SEO-titler fra bilder og stikkord</li>
<li>Legge inn nye varer fra bilder eller regneark, klare til godkjenning</li>
<li>Sjekke butikken for varer uten bilde, tomme kategorier og døde lenker</li>
<li>Varsle om lav beholdning</li>
<li>Sende ukesrapport med salg, besøk og mest solgte varer</li>
<li>Lage utkast til nyhetsbrev og innlegg i sosiale medier</li>
</ul>

<h2>Et menneske sier alltid ja</h2>
<p>Agentene publiserer eller sender ingenting på egen hånd. De lager utkast og lister, og du eller vi godkjenner før noe går ut. Agentene kan skrus av og på når du vil.</p>

<h2>Hvorfor det lønner seg</h2>
<p>Små bedrifter har sjelden tid til å skrive tekster til hver vare eller sjekke butikken hver uke. Med agenter blir det gjort fast, ikke bare når noen husker det. Det gir mer igjen for pengene enn å betale timepris for det samme arbeidet.</p>
<p>Vi brukte agenter da vi la inn over 200 plater i nettbutikken til On the Record i Trondheim: tekst, kategori og SEO ble laget fra bilder, og så sjekket vi alt før det ble publisert.</p>
""",
  "faq": [
   ("Hva er en AI-agent?", "Et program som bruker kunstig intelligens til å gjøre en bestemt oppgave, for eksempel å skrive produkttekster eller sjekke butikken for feil. Hos oss er agentene satt opp for akkurat din butikk."),
   ("Fungerer det med butikken jeg har i dag?", "Agentene er laget for Shopify. Har du en annen plattform, ser vi på hva som er mulig i første prat."),
   ("Blir tekstene like for alle?", "Nei. Agentene får en beskrivelse av tonen din og varene dine, og vi går over tekstene før de publiseres."),
  ],
 },
 {
  "path": "/nettbyra-stavanger/",
  "kort": "Nettbyrå i Stavanger",
  "title": "Nettbyrå i Stavanger · Nettbutikk og nettside · Bergverket",
  "desc": "Bergverket er et nettbyrå i Stavanger som lager nettbutikker i Shopify og nettsider for små bedrifter i Stavanger, Sandnes og resten av Rogaland.",
  "eyebrow": "Stavanger",
  "h1": "Nettbyrå i Stavanger",
  "lead": "Vi er to gründere i Stavanger som lager nettbutikker i Shopify og nettsider for små bedrifter. Holder du til i Stavanger-området, kan vi gjerne møtes over en kaffe.",
  "service": "Nettbutikk og nettside i Stavanger",
  "body": """
<h2>Hva vi lager</h2>
<ul class="ticks">
<li><a href="/nettbutikk-shopify/">Nettbutikk i Shopify</a>: klar til å selge, med Vipps, kort, frakt og vilkår på norsk</li>
<li><a href="/nettside/">Nettside</a>: rask, mobilvennlig og lett å finne i Google</li>
<li><a href="/automatisering/">Automatisering med AI-agenter</a>: produkttekster, vareimport og ukesrapporter</li>
<li>Synlighet: Google-bedriftsprofil, Search Console, Facebook og Instagram koblet til butikken</li>
</ul>

<h2>For bedrifter i Stavanger og Rogaland</h2>
<p>Vi lager nettbutikker og nettsider for butikker, håndverkere, frisører, kafeer og andre små bedrifter i Stavanger, Sandnes og resten av Rogaland, og for bedrifter i hele Norge. Du snakker med de samme to folka fra første prat til butikken eller nettsiden er oppe.</p>

<h2>Hvem vi er</h2>
<p>Bergverket er startet av Fabian Berg og Viktor Mellberg. Fabian studerer innovasjon, markedsføring og ledelse ved NLA Høgskolen, og Viktor studerer ved Universitetet i Stavanger. Vi driver byrået ved siden av studiene, med god tid til hver kunde. <a href="/#oss">Les mer om oss</a>.</p>
""",
  "faq": [
   ("Kan vi møtes i Stavanger?", "Ja. Holder du til i Stavanger-området, møtes vi gjerne. Ellers tar vi første prat på video eller telefon."),
   ("Jobber dere bare med bedrifter i Stavanger?", "Nei. Vi jobber digitalt med bedrifter i hele Norge. Vår første nettbutikk laget vi for en platesjappe i Trondheim."),
   ("Hva koster det?", "Det kommer an på hva du trenger. Etter første prat får du et tilbud med pris og plan, og vi starter ikke før du har sagt ja."),
  ],
 }

]

ART_SIDER = []
for f in glob.glob(os.path.join(HER, "artikler", "*.json")):
    a = json.load(open(f, encoding="utf-8"))
    a["article"] = True
    a["eyebrow"] = "Artikkel"
    ART_SIDER.append(a)
# Case-sider (bare med kundens ja). Trond sa ja til On the Record-caset 2026-11-25.
CASES = [
 {
  "path": "/arbeid/on-the-record/",
  "kort": "On the Record",
  "title": "Case: nettbutikk for platesjappa On the Record · Bergverket",
  "desc": "Slik bygde vi nettbutikken i Shopify for platesjappa On the Record i Trondheim: eget tema, over 200 brukte plater lagt inn fra bilder, kasse og butikk i samme system.",
  "eyebrow": "Case · Nettbutikk i Shopify",
  "h1": "On the Record",
  "lead": "Platesjappa On the Record i Trondheim ville selge brukte plater på nett, ved siden av butikken. Vi bygde nettbutikken i Shopify fra bunnen, og den åpner 2. desember 2026.",
  "body": """
<div class="case-facts">
  <div><b>200+</b><span>plater lagt inn</span></div>
  <div><b>2.12</b><span>åpningsdag 2026</span></div>
  <div><b>1</b><span>lager for butikk og nett</span></div>
</div>
<h2>Utgangspunktet</h2>
<p>On the Record selger brukte CD-er og LP-er i Trondheim. Hver plate er ofte den eneste i sitt slag, så alt må legges inn én og én, med riktig artist, tittel, format og stand. Det tar lang tid å gjøre for hånd, og det er derfor mange sjapper aldri kommer seg på nett.</p>
<h2>Det vi gjorde</h2>
<ul class="ticks">
<li>Satte opp Shopify med et eget tema i sjappas stil</li>
<li>La inn lageret i bunker fra bilder og regneark. Agenter skrev produkttekstene, og vi så over før de ble publisert</li>
<li>Koblet kassen i butikken til Shopify, så salg i sjappa og på nett havner i samme system</li>
<li>Satte opp kortbetaling, frakt, salgsbetingelser og e-poster på norsk</li>
<li>Koblet måling av salg og besøk, så Trond ser hva som selger</li>
</ul>
<h2>Slik gikk vareimporten</h2>
<ol>
<li><strong>Bunker.</strong> Platene kom inn i bunker, med bilder og opplysninger fra sjappa.</li>
<li><strong>Agenter.</strong> Agenter laget produkttekst, kategori og søkeord for hver plate.</li>
<li><strong>Kontroll.</strong> Vi gikk gjennom alt før platene ble satt som aktive i butikken.</li>
</ol>
<p>Over 200 plater kom inn på denne måten før åpning. Det samme oppsettet bruker vi når nye bunker kommer.</p>
<h2>Hva betyr det for deg?</h2>
<p>Har du mange varer, eller varer som ikke finnes i en ferdig produktliste, er det her vi sparer deg mest tid. Les mer om <a href="/nettbutikk-shopify/">nettbutikk i Shopify</a> og <a href="/automatisering/">automatisering med AI-agenter</a>.</p>
""",
 },
]
SIDER = SIDER + CASES
ART_SIDER.sort(key=lambda a: a["dato"], reverse=True)
ARTIKLER = [(a["path"], a["kort"]) for a in ART_SIDER]
SIDER = SIDER + ART_SIDER

def esc(s): return html.escape(s, quote=True)

def related(current):
    items = [(p, t) for p, t in TJENESTER + ARTIKLER[:4] + [("/artikler/", "Alle artikler")] if p != current]
    cards = "\n".join(f'<li><a href="{p}"><span class="rel__k">{"Artikkel" if p.startswith("/artikler/") and p != "/artikler/" else "Les mer"}</span>{esc(t)}</a></li>' for p, t in items[:6])
    return f'''<nav class="related light-2" aria-label="Mer fra Bergverket">
  <div class="wrap">
    <h2>Mer fra Bergverket</h2>
    <ul class="rel">
{cards}
    </ul>
  </div>
</nav>'''

def footer():
    tj = "\n".join(f'          <li><a href="{p}">{esc(t)}</a></li>' for p, t in TJENESTER + [("/artikler/", "Artikler")])
    return f'''<footer class="foot">
  <div class="wrap">
    <div class="grid">
      <div>
        <a class="mark" href="/">
          {LOGO.replace('#101315', '#0a0c0e')}
          Bergverket
        </a>
        <p>Nettbyrå i Stavanger for nettbutikker i Shopify, nettsider og automatisering med AI-agenter. For bedrifter i hele Norge. To berg, ett verk.</p>
      </div>
      <div>
        <h2 class="foot-h">Tjenester</h2>
        <ul>
{tj}
        </ul>
      </div>
      <div>
        <h2 class="foot-h">Kontakt</h2>
        <ul>
          <li><a href="/#kontakt">Start et prosjekt</a></li>
          <li><a href="mailto:hei@bergverket.no">hei@bergverket.no</a></li>
          <li><a href="https://www.instagram.com/bergverket.no/" rel="me noopener">Instagram</a></li>
          <li><a href="/personvern.html">Personvern</a></li>
          <li><button type="button" class="linkbtn" data-samtykke>Informasjonskapsler</button></li>
        </ul>
      </div>
    </div>
    <div class="base">
      <span>© 2026 Bergverket</span>
      <span><a href="/">bergverket.no</a></span>
    </div>
  </div>
</footer>'''

def header():
    return f'''<header class="top">
  <div class="wrap">
    <a class="mark" href="/" aria-label="Bergverket, til forsiden">
      {LOGO}
      Bergverket
    </a>
    <a class="btn btn--ore top-cta" href="/#kontakt">Kontakt</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="meny"><span aria-hidden="true"></span>Meny</button>
    <nav class="nav" id="meny" aria-label="Hovedmeny">
      <a href="/#tjenester">Tjenester</a>
      <a href="/arbeid/on-the-record/">Arbeid</a>
      <a href="/artikler/">Artikler</a>
      <a href="/#oss">Om oss</a>
      <a class="btn btn--ore" href="/#kontakt">Start et prosjekt</a>
    </nav>
  </div>
</header>'''

def hero_link(s):
    if s.get("article"):
        return '<a class="btn btn--ghost" href="/artikler/">Flere artikler</a>'
    if s["path"].startswith("/arbeid/"):
        return '<a class="btn btn--ghost" href="/#tjenester">Se hva vi lager</a>'
    return '<a class="btn btn--ghost" href="/arbeid/on-the-record/">Se et eksempel</a>'

def cta_link(s):
    if s["path"].startswith("/arbeid/"):
        return '<a class="btn btn--ghost" href="/#tjenester">Se hva vi lager</a>'
    return '<a class="btn btn--ghost" href="/arbeid/on-the-record/">Se On the Record-caset</a>'

def aside_links(current):
    cur = ' aria-current="page"'
    return "\n".join(f'          <li><a href="{p}"{cur if p == current else ""}>{esc(t)}</a></li>' for p, t in TJENESTER)

def page(s):
    dato = s.get("dato", DATO)
    url = BASE + s["path"]
    crumbs = [("Bergverket", BASE + "/"), (s["kort"], url)]
    if s.get("article"):
        crumbs = [("Bergverket", BASE + "/"), ("Artikler", BASE + "/artikler/"), (s["kort"], url)]
    elif s["path"].startswith("/arbeid/"):
        crumbs = [("Bergverket", BASE + "/"), ("Arbeid", BASE + "/#arbeid"), (s["kort"], url)]
    graph = [
        {"@type": "WebPage" if not s.get("article") else "Article", "@id": url + "#side", "url": url,
         ("name" if not s.get("article") else "headline"): s["h1"], "description": s["desc"], "inLanguage": "nb-NO",
         "isPartOf": {"@id": BASE + "/#website"}, "dateModified": dato,
         **({"datePublished": dato, "author": {"@id": BASE + "/#org"}, "publisher": {"@id": BASE + "/#org"}, "image": BASE + "/assets/og.jpg"} if s.get("article") else {"about": {"@id": BASE + "/#org"}})},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]},
    ]
    if s.get("service"):
        graph.append({"@type": "Service", "name": s["service"], "description": s["desc"], "url": url,
                      "provider": {"@id": BASE + "/#org"},
                      "areaServed": [{"@type": "Country", "name": "Norge"}, {"@type": "City", "name": "Stavanger"}]})
    if s.get("faq"):
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    crumb_html = " <span aria-hidden=\"true\">/</span> ".join(
        f'<a href="{u.replace(BASE, "") or "/"}">{esc(n)}</a>' if i < len(crumbs) - 1 else f'<span aria-current="page">{esc(n)}</span>'
        for i, (n, u) in enumerate(crumbs))
    faq_html = ""
    if s.get("faq"):
        faq_html = '<h2>Spørsmål</h2>\n<div class="faq">\n' + "\n".join(
            f'<details><summary>{esc(q)}</summary><div class="a"><p>{esc(a)}</p></div></details>' for q, a in s["faq"]) + "\n</div>"
    og_type = "article" if s.get("article") else "website"
    return f'''<!doctype html>
<html lang="nb">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(s["title"])}</title>
<meta name="description" content="{esc(s["desc"])}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#101315">
<meta name="color-scheme" content="light dark">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="nb_NO">
<meta property="og:site_name" content="Bergverket">
<meta property="og:title" content="{esc(s["h1"])} · Bergverket">
<meta property="og:description" content="{esc(s["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/big-shoulders.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/plex-sans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<a class="skip" href="#innhold">Hopp til innholdet</a>
{header()}
<main id="innhold">
<section class="sub-hero dark">
  <div class="wrap">
    <nav class="crumbs" aria-label="Brødsmuler">{crumb_html}</nav>
    <div class="depth">{esc(s["eyebrow"])}</div>
    <h1>{esc(s["h1"])}</h1>
    <p class="lead">{esc(s["lead"])}</p>{(chr(10) + '    <p class="updated">Publisert ' + dato + "</p>") if s.get("article") else ""}
    <div class="ctas">
      <a class="btn btn--ore" href="/#kontakt">Start et prosjekt <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 10h11M11 5l5 5-5 5"/></svg></a>
      {hero_link(s)}
    </div>
  </div>
</section>
<div class="sub light">
  <div class="wrap sub__grid">
    <article class="prose">
{s["body"].strip()}
{faq_html}
    </article>
    <aside class="sub__aside" aria-label="Kontakt">
      <div class="aside-card">
        <div class="depth">Snakk med oss</div>
        <p>Fortell kort hva du vil få til, så svarer Fabian eller Viktor. Første prat er uforpliktende.</p>
        <a class="btn btn--ore" href="/#kontakt">Start et prosjekt</a>
        <a class="aside-mail" href="mailto:hei@bergverket.no">hei@bergverket.no</a>
      </div>
      <div class="aside-card aside-card--plain">
        <div class="depth">Tjenester</div>
        <ul>
{aside_links(s["path"])}
        </ul>
      </div>
    </aside>
  </div>
</div>
<section class="sub-cta dark">
  <div class="wrap">
    <h2>Har du noe vi skal <em>grave i?</em></h2>
    <p>To folk, én kontakt, og du eier alt når vi er ferdige.</p>
    <div class="ctas">
      <a class="btn btn--ore" href="/#kontakt">Start et prosjekt</a>
      {cta_link(s)}
    </div>
  </div>
</section>
</main>
{related(s["path"])}
{footer()}
<script src="/assets/site.js" defer></script>
<script src="/assets/samtykke.js" defer></script>
</body>
</html>
'''

def artikler_index():
    lis = "\n".join(f'<li><a href="{a["path"]}">{esc(a["h1"])}</a><br>{esc(a["desc"])}</li>' for a in ART_SIDER)
    s = {"path": "/artikler/", "kort": "Artikler", "title": "Artikler om nettbutikk og nettside · Bergverket",
         "desc": "Korte, ærlige artikler om nettbutikk i Shopify, nettsider, Google og automatisering for små bedrifter.",
         "eyebrow": "Artikler", "h1": "Artikler", "lead": "Korte svar på det folk lurer på før de lager nettbutikk eller nettside.",
         "body": f'<ul class="ticks">\n{lis}\n</ul>'}
    return page(s)

for s in SIDER:
    d = os.path.join(ROOT, s["path"].strip("/"))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(page(s))
os.makedirs(os.path.join(ROOT, "artikler"), exist_ok=True)
open(os.path.join(ROOT, "artikler", "index.html"), "w", encoding="utf-8").write(artikler_index())

# Siste artikler på forsiden (mellom ARTIKLER-START og ARTIKLER-SLUTT i index.html)
def forside_artikler():
    kort = "\n".join(f'          <li><a href="{a["path"]}"><span class="rel__k">Artikkel</span>{esc(a["h1"])}</a></li>' for a in ART_SIDER[:3])
    return f'''      <div class="home-art reveal">
        <div class="home-art__head"><h3>Les mer i artiklene</h3><a href="/artikler/">Alle artikler →</a></div>
        <ul class="rel">
{kort}
        </ul>
      </div>
'''
idx = os.path.join(ROOT, "index.html")
forside = open(idx, encoding="utf-8").read()
a, b = "<!-- ARTIKLER-START (lages av _verktoy/lag_sider.py) -->\n", "      <!-- ARTIKLER-SLUTT -->"
if a in forside and b in forside:
    forside = forside[:forside.index(a) + len(a)] + forside_artikler() + forside[forside.index(b):]
    open(idx, "w", encoding="utf-8").write(forside)

urls = [("/", DATO), ("/personvern.html", DATO)] + [(p, DATO) for p, _ in TJENESTER] + [(c["path"], DATO) for c in CASES] + [("/artikler/", max([DATO] + [a["dato"] for a in ART_SIDER]))] + [(a["path"], a["dato"]) for a in ART_SIDER]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{BASE}{u}</loc><lastmod>{d}</lastmod></url>\n" for u, d in urls) + "</urlset>\n"
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(sm)
print("ok", len(SIDER) + 1, "sider")
