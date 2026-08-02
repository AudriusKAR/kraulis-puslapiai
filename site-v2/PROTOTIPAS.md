# site-v2 — HTML prototipo statusas (2026-08-02)

**Neprodukcinis prototipas.** GitHub Pages = staging peržiūra, visi puslapiai `noindex`.
Jokio produkcijos / Verskis / DNS / mokamo resurso / analitikos trackingo.

## Ką šis commit įgyvendina (pagal Codex 8 priėmimo punktus + UX/PM punch-list)

- **Užklausos forma (A1', demonstracinė):** privalomi `Telefonas*` + viena `Paslaugos / poreikio kategorija*`; `Įrangos tipas / Vardas / El. paštas / Žinutė` neprivalomi, o sutikimas lieka privalomas. Pateikimas **neaktyvus** — `mailto` submit pašalintas, forma **nieko nesiunčia** ir **nerodo melagingo „pristatyta"**. Būsenos: validation (klaida ne vien spalva — `aria-invalid` + `err-msg`), error, success(demo). Nuolatinis „demonstracinė versija" ženklas.
- **Kontaktų konfliktas išspręstas:** visur `info@kraulis.lt` → **`audrius@kraulis.lt`** (viešas patvirtintas). Formos gavėjas **nehardkodintas** (forma demo). Pakeista ir generatoriuje (`_generator/build_v2.py` `MAIL`), kad pergeneravus negrįžtų.
- **E-parduotuvės perėjimas:** kol nėra patvirtinto URL, visi e-shop įėjimai yra neaktyvūs elementai su matomu „netrukus" ženklu — tai nėra nuorodos ir jos niekur nenukreipia.
- **Nepatvirtinti verslo faktai:** kainos, teritorija, SLA, garantijos, gamintojai, rekvizitai ir darbo laikas pašalinti iš matomo teksto bei metaduomenų; liko tik nevieši `REIKIA_PATVIRTINIMO` komentarai.
- **Generatoriaus paritetas:** visi pakeitimai įgyvendinti `_generator/` šaltiniuose; pakartotinis abiejų generatorių paleidimas turi palikti švarią darbo kopiją.
- **Paletė:** laikoma esama site-v2 navy `#24303E` (A8, UX rekomendacija). CRM `#0E3A57` = atskira Android kryptis.

## Vidiniai REIKIA_PATVIRTINIMO (Audrius) — nepublikuoti kaip faktų

kainodara · darbų garantija · gamintojų sąrašas · teritorija · SLA · patirtis/atestatai ·
atsiliepimai ir darbų nuotraukos (repo `content-review/img/`, Q23) · rekvizitai · privatumo politika ·
Verskis formos endpointas + e-shop/kategorijų URL.

> Strategas nurodė, kad dalis šių turi 2026-07 Audriaus atsakymus (`CONTENT-QUESTIONS.md`);
> patvirtinus jų galiojimą naujai svetainei, placeholderiai virsta faktais.

## Žinomi likę darbai (follow-up)

- Realios darbų nuotraukos — įdedamos tik po Q23 patvirtinimo (kol kas naudojamos schematinės SVG iliustracijos, ne netikri „įrodymai").
- Gilesnė stratego copy integracija (landing H1, „du keliai", „kodėl Kraulis" pasitikėjimo blokas) — kitas commitas.
