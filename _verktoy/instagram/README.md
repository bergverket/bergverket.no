# Instagram for Bergverket (@bergverket.no)

Profil: https://www.instagram.com/bergverket.no/ · bedriftskonto, kategori Webdesigner, e-post hei@bergverket.no, Stavanger.
Toppen av profilen er et banner i tre poster (laget 26.11.2026), og under ligger tre tips-poster (Google, sjekkliste, Shopify vs WooCommerce). Nye poster skyver banneret ned, så legg alltid ut **tre poster om gangen** hvis banneret skal holde seg som en hel rad, eller godta at det forskyves.

## Stil
- Mørk bunn #101315, lys tekst #eceae5, kobber #e57a41 som aksent. Fjell-silhuett nederst, logo oppe til venstre.
- Overskrift i store bokstaver (DIN Condensed i nettleseren, ligner Big Shoulders på nettsiden), liten mono-tekst over.
- Format 1080×1350 (4:5). Velg 4:5 i beskjæringen («Crop» → ikon nede til venstre → 4:5).

## Slik legger du ut fra Chrome
1. Åpne instagram.com (innlogget som bergverket.no) → «+» Create → Post.
2. Lim inn `lag_post.js` med javascript_tool og kjør `await __bvPost({...})`. Bildet tegnes i full kvalitet og legges rett i filfeltet.
3. Velg 4:5 → Next → Next → skriv tekst → Share.
Skjermbilde-opplasting gir for dårlig kvalitet. Ikke bruk det.
4. Instagram laster siden på nytt når du lukker «Post shared», og da forsvinner funksjonen. Lagre den før du lukker: `sessionStorage.setItem('bvPost', __bvPost.toString())`, og hent den etterpå med `window.__bvPost = new Function('return ' + sessionStorage.getItem('bvPost'))()`.
5. Forhåndsvis alltid først med `preview:true` og se på skjermbildet før du laster opp. Overskrift: 2–3 linjer, `size: 170` passer for tre linjer + to linjer brødtekst.

## Ting som bare går i mobilappen
Lenke i bio, feste poster til toppen, stories og høydepunkter. Be Fabian gjøre disse på telefonen.

## Regler for innhold
- Norsk, uformelt, konkret. Ingen priser. Ikke gjett fakta. Ikke «Claude» i tekst eller navn.
- Hver post: én nyttig ting (tips fra en artikkel, en sjekkliste, et case når kunden har sagt ja).
- Pek videre til en artikkel eller tjenesteside på bergverket.no («lenke i bio»).
- 3–6 emneknagger, f.eks. #nettbutikk #shopify #nettside #nettbyrå #stavanger #småbedrift.
- **Publisering krever Fabians ja** i tråden før «Share».
