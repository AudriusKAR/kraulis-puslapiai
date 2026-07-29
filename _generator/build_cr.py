# -*- coding: utf-8 -*-
"""content-review generatorius — SIŪLOMAS turinys final-cba dizaine + anotacijų juosta.
Atskiras nuo site-v2 (nekeičia gamybinio turinio). Išvestis -> puslapiai/content-review/."""
import io, os
from build_v2 import logo, SPRITE, CSS, FOOTER, NAVJS, header, MAIL, TEL, TELH
OUT_CR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "content-review"))
os.makedirs(OUT_CR, exist_ok=True)

ANNO_STYLE = '''<style>
.cr-anno{background:#FFF7E6;border-bottom:1px solid #F0DFB8;color:#5A4A1E;font-family:'IBM Plex Sans',sans-serif}
.cr-anno .wrap{display:flex;flex-wrap:wrap;gap:6px 22px;padding:10px 0;font-size:12.5px;align-items:baseline}
.cr-anno .tag{font-family:'IBM Plex Mono',monospace;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;background:#5A4A1E;color:#FFF7E6;padding:3px 8px;border-radius:5px;white-space:nowrap}
.cr-anno b{color:#3d3212}
.cr-anno .wait{color:#8a5a00}
.cr-bar{background:#1A6E96;color:#fff;font-size:12.5px;text-align:center;padding:7px 12px;font-family:'IBM Plex Mono',monospace;letter-spacing:.04em}
.cr-bar a{color:#CFE0EC}
.cr-revs{padding:56px 0}
.cr-revwrap{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:18px;margin-top:26px}
.rev{background:#fff;border:1px solid #E4EBF1;border-radius:14px;padding:22px 22px 18px;display:flex;flex-direction:column;gap:12px}
.rev .stars{color:#F2A93B;letter-spacing:2px;font-size:15px}
.rev blockquote{margin:0;font-size:15px;line-height:1.6;color:var(--navy)}
.rev figcaption{font-size:13px;color:var(--steel);font-weight:600}
.rev figcaption span{display:block;font-weight:400;font-family:'IBM Plex Mono',monospace;font-size:11.5px;margin-top:2px;letter-spacing:.02em}
.cr-revsrc{font-size:12.5px;color:var(--steel);margin-top:18px}
.rev-lead{background:#fff;border:1px solid #E4EBF1;border-left:3px solid #2E9BD6;border-radius:12px;padding:22px 24px;margin-top:22px}
.rev-lead blockquote{margin:0;font-size:16.5px;line-height:1.6;color:var(--navy);font-weight:500}
.rev-lead .stars{color:#F2A93B;letter-spacing:2px;font-size:15px;margin-bottom:8px}
.rev-lead cite{display:block;margin-top:12px;font-style:normal;font-size:13px;color:var(--steel);font-weight:600}
.cr-gallery{padding:56px 0}
.cr-gwrap{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:24px}
.cr-photo{margin:0;border-radius:14px;overflow:hidden;border:1px solid #E4EBF1;background:#fff}
.cr-photo img{display:block;width:100%;height:230px;object-fit:cover}
.cr-photo figcaption{font-size:12.5px;color:var(--steel);padding:10px 14px;line-height:1.5}
.cr-photo.inline{max-width:560px;margin:24px 0}
.cr-photo.inline img{height:auto;max-height:520px}
</style>'''

# --- Realūs klientų atsiliepimai iš paslaugos.lt profilio (Audrius Karnišauskas | Kraulis).
#     Įvertinimas 5,0 (7 atsiliepimai). Rašyba lengvai sutvarkyta, prasmė nekeista.
# Garantija (Audrius patvirtino 2026-07): darbams — nuo 3 iki 24 mėn. (pagal darbų pobūdį).
G_GAR = "nuo 3 iki 24 mėn."
# Įrangos gamintojo garantijos pratęsimas, kai montuoja kvalifikuoti specialistai:
G_PRAT = "iki gamintojo numatyto termino (dažnai 3, kai kuriais atvejais 5 metai)"
# Aptarnaujama teritorija (iš paslaugos.lt profilio: „Vilnius, +100 km aplink“):
TERITORIJA = "Vilniuje ir apie 100 km aplink"

PASLAUGOS_URL = "https://paslaugos.lt/audrius-karnisauskas--kraulis-av4380"
REVIEWS = [
 ("Tadas Kaminskas","Rekuperatoriaus remontas · 2026-06","Pro meistras — po remonto dar gavau matavimų ataskaitą; nesu matęs, kad kas taip dirbtų Lietuvoje. Rekomenduoju, ačiū Audriau!"),
 ("Danielius Šeštokas","Vėdinimo sistemos remontas · 2026-06","Darbas atliktas greitai, profesionaliai ir preciziškai. Audrius tiksliai sureguliavo oro srautus ir pakonsultavo apie priežiūrą. Name iškart juntamas geresnis oro balansas."),
 ("Diana","Kondicionieriaus remontas · 2026-05","Meistras jau pirmo vizito metu sutvarkė problemą, kurios nepavyko išspręsti jau kurį laiką. Išsami konsultacija ir naudingi patarimai ateičiai. Geriausios rekomendacijos!"),
 ("Juozas","Rekuperatoriaus remontas · 2026-07","Operatyviai sutvarkė rekuperatoriaus problemą. Rekomenduoju."),
 ("Charles M.","Vėdinimo sistemos montavimas · 2026-06","Very professional and human person. He takes time for you and takes care of everything — rare these days. All at a very reasonable price."),
 ("Jolanta","Kondicionieriaus montavimas · 2026-05","Dėkoju už greitą ir kokybišką paslaugą. Viskas puiku, sėkmės darbuose!"),
]

def reviews_block(items=None, title="Ką sako klientai", kick="Atsiliepimai", sub=None, src=True):
    items = items if items is not None else REVIEWS
    cards="".join(f'<figure class="rev"><div class="stars">★★★★★</div><blockquote>{q}</blockquote><figcaption>{who}<span>{meta}</span></figcaption></figure>' for who,meta,q in items)
    srch=(f'<p class="cr-revsrc">Tikri klientų atsiliepimai iš <a href="{PASLAUGOS_URL}" target="_blank" rel="noopener">Paslaugos.lt profilio</a> — įvertinimas 5,0 (7 atsiliepimai).</p>') if src else ''
    s=f'<p>{sub}</p>' if sub else ''
    return f'<section class="cr-revs"><div class="wrap"><div class="sh"><div><span class="kick">{kick}</span><h2>{title}</h2></div>{s}</div><div class="cr-revwrap">{cards}</div>{srch}</div></section>'

# --- Realių darbų nuotraukos (Audrius pateikė 2026-07). Failai dedami į content-review/img/.
#     Kol failo nėra, <img> pasislepia (onerror), puslapis nesulūžta.
PHOTOS = {
 "termovizija":  ("01-termovizija-kondicionierius.jpg","Kondicionieriaus termovizinė nuotrauka — matomas šaldymo pasiskirstymas","Termovizinė patikra: matome, kaip realiai veikia įranga."),
 "olimpia":      ("02-olimpia-lauko-blokas.jpg","Sumontuotas Olimpia Splendid kondicionieriaus lauko blokas ant mūrinės sienos","Tvarkingas lauko bloko montavimas."),
 "rekuperatorius":("03-rekuperatorius.jpg","Rekuperatoriaus įrenginys su prijungtais oro ortakiais","Rekuperacinė vėdinimo sistema."),
 "testo":        ("04-testo-matavimo-iranga.jpg","Profesionali „testo“ oro srauto matavimo įranga","Matuojame profesionalia „testo“ įranga — ne iš akies."),
 "toshiba":      ("05-toshiba-servisas.jpg","Toshiba šilumos siurblio servisas su vakuuminiu siurbliu ir manometrais","Šilumos siurblio servisas su vakuumavimo ir slėgio matavimo įranga."),
 "matavimas":    ("06-oro-srauto-matavimas.jpg","Specialistas matuoja oro srautą prie lubų difuzoriaus","Oro srautų matavimas kiekvienoje patalpoje — balansavimo pagrindas."),
 "trane":        ("07-trane-agregatas.jpg","TRANE pramoninis vandens aušinimo agregatas techninėje patalpoje","Dirbame ir su sudėtingomis verslo sistemomis."),
}

def img_fig(key, cls=""):
    fn,alt,cap = PHOTOS[key]
    c=f'<figcaption>{cap}</figcaption>' if cap else ''
    return (f'<figure class="cr-photo {cls}"><img src="img/{fn}" alt="{alt}" loading="lazy" '
            f'onerror="this.closest(\'figure\').style.display=\'none\'">{c}</figure>')

def photo_strip(keys, title="Iš mūsų darbų", kick="Realūs objektai", sub=None):
    figs="".join(img_fig(k) for k in keys)
    s=f'<p>{sub}</p>' if sub else ''
    return (f'<section class="cr-gallery"><div class="wrap"><div class="sh"><div>'
            f'<span class="kick">{kick}</span><h2>{title}</h2></div>{s}</div>'
            f'<div class="cr-gwrap">{figs}</div></div></section>')

def review_lead(who, meta, quote):
    return f'<div class="wrap"><div class="rev-lead"><div class="stars">★★★★★</div><blockquote>„{quote}"</blockquote><cite>— {who}, {meta} · <a href="{PASLAUGOS_URL}" target="_blank" rel="noopener">Paslaugos.lt</a></cite></div></div>'

def anno(tikslas, auditorija, cta, laukia):
    w = ('<span class="wait"><b>Laukia patvirtinimo:</b> '+laukia+'</span>') if laukia else '<span style="color:#2e7d32"><b>✓</b> nauji teiginiai nelaukia</span>'
    return (f'<div class="cr-anno"><div class="wrap"><span class="tag">Tik peržiūrai</span>'
            f'<span><b>Tikslas:</b> {tikslas}</span><span><b>Auditorija:</b> {auditorija}</span>'
            f'<span><b>CTA:</b> {cta}</span>{w}</div></div>')

def crbar(site_v2_file):
    from urllib.parse import quote
    href = "../site-v2/" + quote(site_v2_file)
    return f'<div class="cr-bar">SIŪLOMO turinio peržiūra (nebus gamyboje) · <a href="index.html">← Visi puslapiai</a> · <a href="{href}">Dabartinis site-v2 →</a></div>'

def page_cr(fn, title, desc, body, active, annotation, site_v2_file, extra_head=""):
    html=f'''<!DOCTYPE html>
<html lang="lt">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[SIŪLOMA] {title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800;900&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style>{ANNO_STYLE}{extra_head}
</head>
<body>
{SPRITE}
{crbar(site_v2_file)}
{annotation}
{header(active)}
<main id="main">
{body}
</main>
{FOOTER}
{NAVJS}
</body>
</html>'''
    with io.open(os.path.join(OUT_CR,fn),"w",encoding="utf-8") as f: f.write(html)
    return fn
print("cr shell ready")
