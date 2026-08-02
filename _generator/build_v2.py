# -*- coding: utf-8 -*-
"""Kraulis site-v2 — visi puslapiai final-cba dizaino sistemoje (light, C+B+A).
Bendras shell (header+nav+footer+CSS+SVG sprite) -> savarankiški HTML failai Verskis.lt."""
import io, os
# Generatorius gyvena puslapiai/_generator/ ; išvestis -> puslapiai/site-v2/
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "site-v2"))
os.makedirs(OUT, exist_ok=True)
TEL='+370 610 24999'; TELH='tel:+37061024999'; MAIL='audrius@kraulis.lt'  # viešas patvirtintas kontaktas (PM/Codex 2026-08-02)
# Prototipo HTML generuojamas tik iš _generator/ šaltinių. Nevykdyti rankinių
# pataisų site-v2/ kataloge, nes kitas generavimas jas perrašys.

def logo(color, cls="logo"):
    M=('<path fill-rule="evenodd" fill="{c}" d="M175,31 L26,180 L57,180 L57,302 L293,302 L293,180 L324,180 Z M175,72 L81,166 L81,275 L269,275 L269,166 Z"/>'
       '<path fill="{c}" d="M151,149 L133,177 L145,177 L145,243 L157,243 L157,177 L169,177 Z"/>'
       '<path fill="{c}" d="M199,243 L181,215 L193,215 L193,149 L205,149 L205,215 L217,215 Z"/>'
       '<g transform="translate(53.416,350.152) scale(0.02358,-0.02358)"><path fill="{c}" d="M152 1466H605V912L1080 1466H1682L1148 913L1706 0H1148L839 603L605 358V0H152ZM1862 0V1466H2617Q2827 1466 2938.0 1430.0Q3049 1394 3117.0 1296.5Q3185 1199 3185 1059Q3185 937 3133.0 848.5Q3081 760 2990 705Q2932 670 2831 647Q2912 620 2949 593Q2974 575 3021.5 516.0Q3069 457 3085 425L3304 0H2792L2550 448Q2504 535 2468 561Q2419 595 2357 595H2317V0ZM2317 872H2508Q2539 872 2628 892Q2673 901 2701.5 938.0Q2730 975 2730 1023Q2730 1094 2685.0 1132.0Q2640 1170 2516 1170H2317ZM4351 242H3835L3764 0H3301L3852 1466H4346L4897 0H4423ZM4256 559 4094 1086 3933 559ZM5996 1466H6448V592Q6448 462 6407.5 346.5Q6367 231 6280.5 144.5Q6194 58 6099 23Q5967 -26 5782 -26Q5675 -26 5548.5 -11.0Q5422 4 5337.0 48.5Q5252 93 5181.5 175.0Q5111 257 5085 344Q5043 484 5043 592V1466H5495V571Q5495 451 5561.5 383.5Q5628 316 5746 316Q5863 316 5929.5 382.5Q5996 449 5996 571ZM6748 1466H7201V361H7908V0H6748ZM8132 1466H8586V0H8132ZM8832 485 9263 512Q9277 407 9320 352Q9390 263 9520 263Q9617 263 9669.5 308.5Q9722 354 9722 414Q9722 471 9672 516Q9622 561 9440 601Q9142 668 9015 779Q8887 890 8887 1062Q8887 1175 8952.5 1275.5Q9018 1376 9149.5 1433.5Q9281 1491 9510 1491Q9791 1491 9938.5 1386.5Q10086 1282 10114 1054L9687 1029Q9670 1128 9615.5 1173.0Q9561 1218 9465 1218Q9386 1218 9346.0 1184.5Q9306 1151 9306 1103Q9306 1068 9339 1040Q9371 1011 9491 986Q9788 922 9916.5 856.5Q10045 791 10103.5 694.0Q10162 597 10162 477Q10162 336 10084.0 217.0Q10006 98 9866.0 36.5Q9726 -25 9513 -25Q9139 -25 8995.0 119.0Q8851 263 8832 485Z"/></g>')
    return '<svg class="%s" viewBox="14 19 322 343.7654345654346" role="img" aria-label="Kraulis">%s</svg>'%(cls,M.format(c=color))

SPRITE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>
<symbol id="i-rekup" viewBox="0 0 24 24"><rect x="3.5" y="6.5" width="17" height="11" rx="1.5"/><path d="M12 6.5v11"/><path d="M6 10c2 0 3 1.6 5.6 1.6M6 14c2 0 3-1.6 5.6-1.6"/><path d="M18 10c-2 0-3 1.6-5.6 1.6M18 14c-2 0-3-1.6-5.6-1.6"/></symbol>
<symbol id="i-kond" viewBox="0 0 24 24"><rect x="3" y="6" width="18" height="6.5" rx="1.6"/><path d="M6 9h9"/><path d="M7 16c0 1.4-1 2-1 2.6M12 16c0 1.8-1.2 2.5-1.2 3.2M17 16c0 1.4-1 2-1 2.6"/></symbol>
<symbol id="i-shiluma" viewBox="0 0 24 24"><rect x="3" y="5.5" width="12" height="13" rx="1.6"/><circle cx="9" cy="12" r="3.1"/><path d="M9 9.6v4.8M7.2 10.5l3.6 3M10.8 10.5l-3.6 3"/><path d="M18 8.5c1.4 1.2 1.4 3 0 4.2M20.5 7c1.9 1.8 1.9 4.6 0 6.4"/></symbol>
<symbol id="i-priedai" viewBox="0 0 24 24"><path d="M12 3.2l8 4.1v9.4L12 20.8l-8-4.1V7.3z"/><path d="M4 7.3l8 4.1 8-4.1M12 11.4v9.4"/></symbol>
<symbol id="i-remontas" viewBox="0 0 24 24"><path d="M15 7a4 4 0 0 1-5.2 5.2L5.5 16.5a2.5 2.5 0 0 0 3.5 3.5l4.3-4.3A4 4 0 0 1 18.5 10.5l-2.8 2.8-2.8-.7-.7-2.8z"/></symbol>
<symbol id="i-balans" viewBox="0 0 24 24"><path d="M20 14a8 8 0 1 0-16 0"/><path d="M12 14l4-3.2"/><circle cx="12" cy="14" r="1.4" fill="currentColor" stroke="none"/><path d="M4 18h16"/></symbol>
<symbol id="i-prieziura" viewBox="0 0 24 24"><path d="M12 3l7 3v5c0 5-3 8-7 10-4-2-7-5-7-10V6z"/><path d="M9 12l2 2 4-4"/></symbol>
<symbol id="i-montavimas" viewBox="0 0 24 24"><rect x="3.5" y="5" width="17" height="8" rx="1.6"/><path d="M7 9h7"/><path d="M8 17v2.5M16 17v2.5M12 13v6.5"/></symbol>
<symbol id="i-airflow" viewBox="0 0 24 24"><path d="M3 8h11a3 3 0 1 0-3-3"/><path d="M3 12h16a3 3 0 1 1-3 3"/><path d="M3 16h8a3 3 0 1 1-3 3"/></symbol>
<symbol id="i-temp" viewBox="0 0 24 24"><path d="M14 13.5V6a2 2 0 0 0-4 0v7.5a4 4 0 1 0 4 0z"/><path d="M12 15.5v-6"/><circle cx="12" cy="16.5" r="1.4" fill="currentColor" stroke="none"/></symbol>
<symbol id="i-cooling" viewBox="0 0 24 24"><path d="M12 3v18M4.5 7.5l15 9M19.5 7.5l-15 9"/><path d="M9.5 4.2 12 6l2.5-1.8M9.5 19.8 12 18l2.5 1.8M4.8 10.6l.3 3-2.6 1.5M19.2 10.6l-.3 3 2.6 1.5M4.8 13.4l-2.3-1.5.3-3M19.2 13.4l2.3-1.5-.3-3"/></symbol>
<symbol id="i-energy" viewBox="0 0 24 24"><path d="M20 12a8 8 0 1 1-4.2-7"/><path d="M12 12l3.5-4"/><path d="M12 4v3M18.5 6.5l-1.6 1.6"/><circle cx="12" cy="12" r="1.3" fill="currentColor" stroke="none"/></symbol>
<symbol id="i-shop" viewBox="0 0 24 24"><path d="M5 8h14l-1 10H6z"/><path d="M8.5 8V6.5a3.5 3.5 0 0 1 7 0V8"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M5 4h4l2 5-3 2a12 12 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M4 7l8 6 8-6"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M12 7v5l3.5 2"/></symbol>
<symbol id="i-map" viewBox="0 0 24 24"><path d="M12 21s6-5.5 6-11a6 6 0 1 0-12 0c0 5.5 6 11 6 11z"/><circle cx="12" cy="10" r="2"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
<symbol id="i-fb" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9.2"/><path d="M14.5 8.2h-1.3a1.8 1.8 0 0 0-1.8 1.8V19"/><path d="M9.7 12.2h4.6"/></symbol>
<symbol id="i-ig" viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="4.6"/><circle cx="12" cy="12" r="3.6"/><circle cx="16.6" cy="7.4" r="0.7"/></symbol>
</defs></svg>'''

# CSS bendrai visiems puslapiams (final-cba + turinio komponentai)
CSS = open(os.path.join(os.path.dirname(__file__),'v2_css.txt'),encoding='utf-8').read()

NAV=[("E-parduotuvė",None,"shop"),("Įranga","index.html#kategorijos","iranga"),("Paslaugos","Paslaugos.html","paslaugos"),
     ("Patarimai","Patarimai.html","patarimai"),("Apie mus","Apie mus.html","apie"),("Kontaktai","Kontaktai.html","kontaktai")]

def header(active,home="index.html"):
    def navitem(t,h,k):
        if h is None:
            return f'<span class="nav-disabled" aria-disabled="true">{t}<small>netrukus</small></span>'
        current=' aria-current="page"' if k==active else ''
        return f'<a href="{h}"{current}>{t}</a>'
    links="".join(navitem(t,h,k) for t,h,k in NAV)
    return f'''<a class="skip" href="#main">Pereiti prie turinio</a>
<header><div class="wrap hd">
  <a href="{home}" aria-label="Kraulis pradžia">{logo('#24303E')}</a>
  <nav class="main" id="mainnav" aria-label="Pagrindinė navigacija">{links}<a class="navcta" href="Užklausos forma.html">Užsakyti servisą</a></nav>
  <div class="hd-right"><a class="hd-tel" href="{TELH}">{TEL}</a>
    <button class="burger" type="button" aria-expanded="false" aria-controls="mainnav" aria-label="Atverti meniu"><svg class="ic" style="width:22px;height:22px" viewBox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
    <a class="btn btn-primary" href="Užklausos forma.html">Užsakyti servisą</a></div>
</div></header>'''

# Socialiniai tinklai — PATVIRTINTA (iš kraulis.lt live, 2026-08-02). Tik paprastos
# nuorodos: jokių FB/IG embed, SDK, pikselių, feed widget ar sekėjų skaičių (Codex/Audrius).
FB_URL='https://www.facebook.com/KraulisMB/'; IG_URL='https://www.instagram.com/kraulismb/'
def social_links(cls="social"):
    return (f'<div class="{cls}">'
            f'<a href="{FB_URL}" target="_blank" rel="noopener noreferrer" aria-label="Kraulis Facebook"><svg class="ic" viewBox="0 0 24 24"><use href="#i-fb"/></svg></a>'
            f'<a href="{IG_URL}" target="_blank" rel="noopener noreferrer" aria-label="Kraulis Instagram"><svg class="ic" viewBox="0 0 24 24"><use href="#i-ig"/></svg></a>'
            '</div>')

FOOTER=f'''<footer><div class="wrap">
  <div class="foot">
    <div>{logo('#FBFCFD')}<p>Šildymo, vėdinimo ir vėsinimo įranga su servisu, kuris nedingsta po pardavimo.</p>
      <h4 style="margin-top:16px">Sekite mus</h4>{social_links()}</div>
    <div><h4>Paslaugos</h4><a href="Paslauga - Rekuperatorių balansavimas.html">Balansavimas</a><a href="Paslauga - Profilaktinė priežiūra.html">Priežiūra</a><a href="Paslaugos.html">Remontas</a><a href="Paslauga - Įrangos montavimas.html">Montavimas</a></div>
    <div><h4>Informacija</h4><a href="Patarimai.html">Patarimai</a><a href="DUK.html">Dažni klausimai</a><a href="Apie mus.html">Apie mus</a><a href="Kontaktai.html">Kontaktai</a></div>
    <div><h4>Kontaktai</h4><p class="mono"><a href="{TELH}">{TEL}</a></p><p class="mono"><a href="mailto:{MAIL}">{MAIL}</a></p><p>Atsakome per 1–2 darbo dienas</p><p>Paslaugos: Vilnius ir ~100 km spinduliu</p></div>
  </div>
  <div class="foot-b"><span>Kraulis, MB</span><span>© 2026 Kraulis, MB</span></div>
</div></footer>'''

NAVJS='''<script>
(function(){var b=document.querySelector('.burger'),n=document.getElementById('mainnav');if(!b||!n)return;
var mq=window.matchMedia('(max-width:860px)');function isOpen(){return n.classList.contains('open')}
function set(o){n.classList.toggle('open',o);b.setAttribute('aria-expanded',o?'true':'false');b.setAttribute('aria-label',o?'Užverti meniu':'Atverti meniu');if(o){var f=n.querySelector('a');if(f)f.focus()}}
b.addEventListener('click',function(){set(!isOpen())});
n.addEventListener('click',function(e){if(e.target.closest('a'))set(false)});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&isOpen()){set(false);b.focus()}});
document.addEventListener('click',function(e){if(isOpen()&&!n.contains(e.target)&&!b.contains(e.target))set(false)});
if(mq.addEventListener)mq.addEventListener('change',function(){if(!mq.matches)set(false)});
})();
</script>'''

def page(fn,title,desc,body,active,extra_head=""):
    html=f'''<!DOCTYPE html>
<html lang="lt">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex"><!-- TODO: gamybinėje Verskis.lt versijoje pašalinti noindex -->
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800;900&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style>{extra_head}
</head>
<body>
{SPRITE}
{header(active)}
<main id="main">
{body}
</main>
{FOOTER}
{NAVJS}
</body>
</html>'''
    with io.open(os.path.join(OUT,fn),"w",encoding="utf-8") as f: f.write(html)
    return fn

print("shell ready")
