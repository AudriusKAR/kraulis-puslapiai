# Kraulis site-v2 — puslapių generatorius (vienintelis tiesos šaltinis)

Visi 15 `../site-v2/*.html` puslapių **generuojami** iš šių šablonų. **Nekeisk `site-v2/*.html` rankomis** — pakeitimai bus prarasti kitą kartą pergeneruojant. Taisyk šablonus čia ir pergeneruok.

## Struktūra
| Failas | Ką laiko |
|---|---|
| `build_v2.py` | Bendras **shell**: header + navigacija (JS su focus valdymu), footer, SVG sprite, `page()` wrapper. Čia `MAIL`, `TEL`, `NAV`. |
| `v2_css.txt` | **Visa CSS dizaino sistema** (final-cba light-first). Vienas failas. |
| `build_v2_content.py` | **Komponentai / helperiai**: titlebar, crumbs, chips, cta, faq, process, priešpo, datasheet, kategorijų panelė, mikroklimato juosta, hero SVG, skirtukas. |
| `build_v2_pages.py` | Pagrindinis, Paslaugos, 6 paslaugų puslapiai (turinys). |
| `build_v2_pages2.py` | Kontaktai, Užklausos forma, Patarimai, 2 gidai, DUK, Apie mus. |

## Pergeneruoti visus puslapius
- Windows: dukart spustelėk **`PERGENERUOTI.bat`**
- arba: `cd _generator && python build_v2_pages.py && python build_v2_pages2.py`
Išvestis visada perrašo `../site-v2/*.html`.

## Kaip pakeisti…
- **Bendrą header/navigaciją** → `build_v2.py`, funkcija `header()` ir sąrašas `NAV`.
- **Footerį** → `build_v2.py`, kintamasis `FOOTER`.
- **CSS toką ar spalvą** → `v2_css.txt`, `:root{ --navy: … }` (visi puslapiai atsinaujina po pergeneravimo).
- **Bendrą el. paštą / telefoną** → `build_v2.py`, `MAIL` / `TEL`.
- **Ikoną** → `build_v2.py`, `SPRITE` (SVG `<symbol id="i-…">`).
- **Puslapio turinį** → atitinkamas `build_v2_pages*.py`.

## Ar sugeneruoti failai nepaseno?
Po bet kokio šablono keitimo **būtina pergeneruoti** ir padaryti Git commit. Patikra:
```
cd _generator && python build_v2_pages.py && python build_v2_pages2.py
cd .. && git status --short site-v2   # jei rodo pakeitimų — buvo nesutapimas, commitink
```
Jei `git status` po pergeneravimo švarus — `site-v2/` atitinka šablonus.

## Du eksporto režimai (žr. VERSKIS-MIGRATION.md)
- **A (dabar): savarankiški HTML** — kiekvienas puslapis su įdėta CSS+sprite. Tinka Verskis.lt turinio laukams ir GitHub Pages staging.
- **B (ateičiai): bendras šablonas + turinio fragmentai** — kai bus aišku, kaip Verskis.lt leidžia bendrą header/footer/CSS. Tada `build_v2.py` `page()` galima perjungti į „fragmento" režimą (tik `<main>` turinys), o bendrą apvalkalą kelti į Verskis šabloną. Neįgyvendinta, kol nepatvirtinta Verskis prieiga.
