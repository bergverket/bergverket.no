# Verktøy for bergverket.no (publiseres ikke, Jekyll hopper over mapper med _)

## Lage eller endre undersider
- Tjenestesider: rediger `SIDER` i `lag_sider.py`.
- Artikler: én JSON-fil per artikkel i `artikler/` (felt: path, kort, title, desc, h1, lead, body, faq, dato).
- Kjør `python3 _verktoy/lag_sider.py` fra repo-roten. Den lager sidene, `/artikler/`, `sitemap.xml` og lenkene.
- Legg ny artikkel til i `llms.txt` under «## Artikler».

## Regler for artikler
- Norsk, kort og konkret. Svar på noe kundene faktisk søker etter.
- Ingen priser fra Bergverket. Ikke gjett fakta: skriv bare det som er sikkert, og lenk heller til kilden.
- Ikke «Claude» i tekst om merkevaren. Lenk til minst én tjenesteside og én annen artikkel.
- Ikke slett `googlecc4b3ce880b48861.html` i roten (Google Search Console).
