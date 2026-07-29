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
</style>'''

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
