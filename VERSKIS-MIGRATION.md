# Kraulis site-v2 → Verskis.lt migracijos žemėlapis

Staging: https://audriuskar.github.io/kraulis-puslapiai/site-v2/ (visi puslapiai `noindex`).
Šis dokumentas — ką reikia sutvarkyti prieš keliant į tikrą Verskis.lt. **Verskis.lt URL neišgalvoti** — laukiama realių adresų iš administravimo.

## 1. Nuorodų žemėlapis (placeholder ir sisteminės)

Visos dar neįgyvendintos nuorodos kode pažymėtos `href="#" data-todo="…"` + `aria-disabled` — **jos NEVEIKIA** (paspaudus nieko nedaro, negrąžina į viršų). Statusas: 🔴 laukia Verskis URL.

| Elementas (tekstas) | Kur | data-todo | Reikalingas Verskis.lt URL / laukas | Statusas |
|---|---|---|---|---|
| „E-parduotuvė" (nav) | visi 15 psl. | `shop` | E-parduotuvės pagrindinis puslapis | 🔴 |
| „Į e-parduotuvę" / „Visa e-parduotuvė" / „Elektroninė parduotuvė" | Pagrindinis, Apie mus | `eshop-visa` | E-parduotuvės pagrindinis puslapis | 🔴 |
| „Rekuperatoriai" (kategorija) | Pagrindinis | `cat-rekuperatoriai` | Kategorijos URL (rekuperatoriai) | 🔴 |
| „Kondicionieriai" (kategorija) | Pagrindinis | `cat-kondicionieriai` | Kategorijos URL (kondicionieriai) | 🔴 |
| „Šilumos siurbliai" (kategorija) | Pagrindinis | `cat-silumos-siurbliai` | Kategorijos URL (šilumos siurbliai) | 🔴 |
| „Priedai ir montavimo medžiagos" (kategorija) | Pagrindinis | `cat-priedai` | Kategorijos URL (priedai/medžiagos) | 🔴 |

### Vidinės nuorodos (VEIKIA staging'e — tik slug'ą reikės atnaujinti)
Nav „Paslaugos / Patarimai / Apie mus / Kontaktai", CTA „Užsakyti servisą" → `Užklausos forma.html`, paslaugų datasheet, „Užpildyti užklausą", gidai, DUK — visos rodo į realius site-v2 failus. 🟡 Verskis versijoje pakeisti į galutinius slug'us (žr. 3 dalį).

### Forma
| Elementas | Dabar | Reikia | Statusas |
|---|---|---|---|
| Užklausos forma (`Užklausos forma.html`) | `mailto:info@kraulis.lt` (su `checkValidity` validacija) | Verskis.lt formos endpointas ARBA palikti mailto | 🟡 sprendimas |
| Mygtukas | „Paruošti el. laišką" | Prijungus endpointą — grąžinti į „Siųsti užklausą" | 🟡 |

### Kontaktai (VEIKIA)
Telefonas `tel:+37061024999`, el. paštas `mailto:info@kraulis.lt` — realūs, veikia. 🟢

## 2. Ko reikia iš Verskis.lt administravimo
1. **E-parduotuvės pagrindinis URL** (1 vnt).
2. **4 kategorijų URL:** rekuperatoriai, kondicionieriai, šilumos siurbliai, priedai/montavimo medžiagos.
3. **Formos endpointas** (jei norima ne mailto) — POST laukų pavadinimai.
4. **Sprendimas dėl bendro header/footer šablono** — ar Verskis leidžia vieną bendrą apvalkalą (tada turinys = tik `<main>` fragmentai), ar kiekvienas puslapis savarankiškas.
5. **Realus kraulis.lt URL formatas** (canonical'ams) ir ar puslapiai bus subkataloge, ar šakninėse nuorodose.
6. Patvirtinti, ar sisteminiai puslapiai (krepšelis, atsiskaitymas, paskyra) lieka Verskis dizaino.

## 3. SEO / URL lentelė (rekomenduojami gamybiniai slug'ai)
Staging failų pavadinimai (su tarpais/lietuviškomis raidėmis) gali likti staging'e; gamybiniai URL — trumpi, ASCII, stabilūs. **Canonical — TBD, kol nežinomas kraulis.lt formatas.**

| Staging failas | Rekomenduojamas slug | `<title>` | `<h1>` |
|---|---|---|---|
| index.html | `/` | Kraulis — ŠVOK įranga ir servisas Vilniuje | Tylu. Šilta. Šviežia. |
| Paslaugos.html | `/paslaugos` | Paslaugos — Kraulis | … | Priežiūra, remontas ir balansavimas |
| Paslauga - Kondicionierių remontas.html | `/paslaugos/kondicionieriu-remontas` | Kondicionierių remontas Vilniuje — Kraulis | Kondicionierių remontas |
| Paslauga - Šilumos siurblių remontas.html | `/paslaugos/silumos-siurbliu-remontas` | Šilumos siurblių remontas Vilniuje — Kraulis | Šilumos siurblių remontas |
| Paslauga - Rekuperatorių remontas.html | `/paslaugos/rekuperatoriu-remontas` | Rekuperatorių remontas Vilniuje — Kraulis | Rekuperatorių remontas |
| Paslauga - Rekuperatorių balansavimas.html | `/paslaugos/rekuperatoriu-balansavimas` | Rekuperatorių balansavimas su ataskaita — Kraulis | Rekuperatorių balansavimas |
| Paslauga - Profilaktinė priežiūra.html | `/paslaugos/profilaktine-prieziura` | Profilaktinė ŠVOK priežiūra Vilniuje — Kraulis | Profilaktinė priežiūra |
| Paslauga - Įrangos montavimas.html | `/paslaugos/irangos-montavimas` | Įrangos montavimas Vilniuje — Kraulis | Įrangos montavimas |
| Kontaktai.html | `/kontaktai` | Kontaktai — Kraulis | +370 610 24999 | Susisiekime |
| Užklausos forma.html | `/uzklausa` | Užklausa — Kraulis | Užsakyti servisą arba konsultaciją |
| Patarimai.html | `/patarimai` | Patarimai ir gidai — Kraulis | Patarimai ir gidai |
| Patarimas - Kaip išsirinkti rekuperatorių.html | `/patarimai/kaip-issirinkti-rekuperatoriu` | Kaip išsirinkti rekuperatorių — Kraulis gidas | Kaip išsirinkti rekuperatorių |
| Patarimas - Kaip išsirinkti kondicionierių ar šilumos siurblį.html | `/patarimai/kaip-issirinkti-kondicionieriu-ar-silumos-siurbli` | Kaip išsirinkti kondicionierių ar šilumos siurblį — Kraulis | Kaip išsirinkti kondicionierių ar šilumos siurblį |
| DUK.html | `/duk` | Dažni klausimai (DUK) — Kraulis | Dažni klausimai |
| Apie mus.html | `/apie-mus` | Apie mus — Kraulis | Įranga, kuri veikia. Ir žmonės, kurie už ją atsako. |

Meta description'ai jau įrašyti kiekviename faile (`<meta name="description">`).

## 4. Prieš įjungiant gamyboje (checklist)
- [ ] Pakeisti visus `data-todo` `href="#"` realiais Verskis URL (žr. 1 dalį).
- [ ] Pašalinti `<meta robots noindex>` iš visų 15 puslapių (pažymėta `<!-- TODO -->`).
- [ ] Pridėti `<link rel="canonical">` su tikrais adresais.
- [ ] Prijungti formą (endpointas) arba palikti mailto; jei endpointas — mygtuką grąžinti į „Siųsti užklausą".
- [ ] Vidines nuorodas pakeisti į galutinius slug'us.
- [ ] Nuspręsti dėl bendro header/footer šablono (žr. `_generator/README.md`, „Du eksporto režimai").
- [ ] Pridėti tikras atliktų darbų nuotraukas / atsiliepimus, kai turėsi (dabar sąžiningai nėra).
