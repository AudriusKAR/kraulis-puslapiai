# -*- coding: utf-8 -*-
import os
from build_v2 import page, logo, OUT, TEL, TELH, MAIL

def ic(name,cls="ic",style=""):
    st=f' style="{style}"' if style else ''
    return f'<svg class="{cls}"{st} viewBox="0 0 24 24"><use href="#{name}"/></svg>'
def crumbs(*p):
    return '<div class="crumbs">'+' / '.join((f'<a href="{h}">{t}</a>' if h else f'<span>{t}</span>') for t,h in p)+'</div>'
def titlebar(h1,lead,kick=None,crumb=None,meta=None,chips=None):
    k=f'<span class="kick">{kick}</span>' if kick else ''
    m=f'<p class="meta">{meta}</p>' if meta else ''
    c=chips or ''
    return f'<section class="titlebar"><div class="wrap"><div class="inner">{crumb or ""}{k}<h1>{h1}</h1><p class="lead">{lead}</p>{m}{c}</div></div></section>'
def chips(items):
    return '<div class="chips">'+''.join(f'<a class="chip" href="{h}">{i}{t}</a>' for t,h,i in items)+'</div>'
def cta(h2,p,acts):
    a=''.join(acts)
    return f'<section><div class="wrap"><div class="cta"><div><h2>{h2}</h2><p>{p}</p></div><div class="cta-acts">{a}</div></div></div></section>'
def btn(txt,href,kind="primary",arrow=False):
    ar=ic('i-arrow','ic',"width:16px;height:16px") if arrow else ''
    return f'<a class="btn btn-{kind}" href="{href}">{txt}{ar}</a>'
def faq(items,title=None,kick="DUK"):
    rows=""
    for q,a in items:
        aa="".join(f"<p>{x}</p>" for x in (a if isinstance(a,(list,tuple)) else [a]))
        rows+=f'<details><summary>{q}</summary><div class="a">{aa}</div></details>'
    head=f'<div class="sh"><div><span class="kick">{kick}</span><h2>{title}</h2></div></div>' if title else ''
    return f'<section><div class="wrap">{head}<div class="faq">{rows}</div></div></section>'
def process(steps,kick="Kaip dirbame",title="Trys žingsniai",sub=None):
    s=""
    for i,(h,p) in enumerate(steps,1):
        s+=f'<div class="pstep"><span class="pn">0{i}</span><div class="pstep-content"><h3>{h}</h3><p>{p}</p></div></div>'
    sp=f'<p>{sub}</p>' if sub else ''
    return f'<section><div class="wrap"><div class="sh"><div><span class="kick">{kick}</span><h2>{title}</h2></div>{sp}</div><div class="process">{s}</div></div></section>'
def priespo(kick="Balansavimo pavyzdys",h2="Oro srautų matavimo ir reguliavimo kryptis",
            p="Pavyzdinė diagrama paaiškina, kaip lyginami oro srautai prieš ir po reguliavimo. Tai iliustracija, o ne konkretaus objekto matavimo duomenys.",
            link=("Apie balansavimą","Paslauga - Rekuperatorių balansavimas.html")):
    return f'''<section><div class="wrap"><div class="sig">
  <div class="txt"><span class="kick">{kick}</span><h2>{h2}</h2><p>{p}</p>{btn(link[0],link[1],"primary",True)}</div>
  <div class="fig" role="img" aria-label="Oro srautų pavyzdys prieš ir po balansavimo">
    <div class="fh"><span>Oro srautas · m³/h</span><span>Pavyzdys</span></div>
    <div class="brow"><span class="rl">Miegamasis</span><div class="bar"><i class="b" style="width:42%"><b>42</b></i></div></div>
    <div class="brow"><span class="rl"></span><div class="bar"><i class="a" style="width:72%"><b>72</b></i></div></div>
    <div class="brow"><span class="rl">Svetainė</span><div class="bar"><i class="b" style="width:88%"><b>88</b></i></div></div>
    <div class="brow"><span class="rl"></span><div class="bar"><i class="a" style="width:70%"><b>70</b></i></div></div>
    <div class="leg"><span>▪ Prieš</span><span><em>▪ Po reguliavimo</em></span></div>
  </div></div></div></section>'''

HERO_SVG='''<div class="instr" aria-hidden="true"><svg viewBox="0 0 440 380" fill="none" width="100%">
  <circle cx="288" cy="150" r="140" stroke="#DCE4EB"/><circle cx="288" cy="150" r="100" stroke="#E7EEF4"/>
  <path class="draw" style="--l:420" d="M118 176 L238 70 L358 176" stroke="#24303E" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path class="draw d2" style="--l:520" d="M150 162 L150 288 L326 288 L326 162" stroke="#24303E" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path class="draw d3" style="--l:200" d="M238 162 L238 288 M150 226 L326 226" stroke="#DCE4EB" stroke-width="1.5"/>
  <rect x="205" y="120" width="66" height="30" rx="3" stroke="#24303E" stroke-width="2"/><path d="M238 120 v30" stroke="#DCE4EB" stroke-width="1.2"/>
  <path class="flow" d="M60 214 C130 214 150 135 205 135" stroke="#2E9BD6" stroke-width="2.5" stroke-linecap="round"/><path d="M205 135 l-9 -5 M205 135 l-8 6" stroke="#2E9BD6" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <path class="flow" style="animation-delay:.7s" d="M271 135 C330 135 350 214 410 214" stroke="#5D6B74" stroke-width="2" stroke-linecap="round"/><path d="M410 214 l-9 -5 M410 214 l-9 5" stroke="#5D6B74" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="360" y="250" width="46" height="38" rx="3" stroke="#24303E" stroke-width="2"/><circle cx="383" cy="269" r="9" stroke="#24303E" stroke-width="1.6"/><path d="M383 262v14M377 266l12 6" stroke="#24303E" stroke-width="1.2"/>
  <line x1="150" y1="316" x2="326" y2="316" stroke="#DCE4EB"/><line x1="150" y1="312" x2="150" y2="320" stroke="#5D6B74"/><line x1="238" y1="312" x2="238" y2="320" stroke="#5D6B74"/><line x1="326" y1="312" x2="326" y2="320" stroke="#5D6B74"/>
  <circle cx="238" cy="135" r="3" fill="#2E9BD6"/><text x="150" y="334" font-family="IBM Plex Mono" font-size="9.5" fill="#5D6B74">rekuperacija · srautas · matavimas</text>
</svg></div>'''
DIVIDER='<div class="divide"><svg viewBox="0 0 180 38" fill="none"><path d="M0 19 C50 19 55 8 90 8 C125 8 130 19 180 19" stroke="#DCE4EB" stroke-width="1"/><circle cx="90" cy="8" r="2.5" fill="#2E9BD6"/></svg></div>'

# service datasheet rows (reused)
def datasheet():
    rows=[("i-remontas","Remontas","Gedimo požymiai, diagnostikos eiga ir galimi tolesni veiksmai.","Paslaugos.html"),
          ("i-balans","Rekuperatorių balansavimas","Oro srautų matavimo ir reguliavimo paslaugos apžvalga.","Paslauga - Rekuperatorių balansavimas.html"),
          ("i-prieziura","Profilaktinė priežiūra","Patikros, valymo ir susidėvėjimo įvertinimo eiga.","Paslauga - Profilaktinė priežiūra.html"),
          ("i-montavimas","Įrangos montavimas","Parinkimo, montavimo, paleidimo ir sureguliavimo eiga.","Paslauga - Įrangos montavimas.html")]
    r=""
    for icn,h,p,href in rows:
        r+=f'<a class="srow" href="{href}"><span class="sic">{ic(icn)}</span><h3>{h}</h3><p>{p}</p><span class="rt">{ic("i-arrow","ic ar","width:20px;height:20px")}</span></a>'
    return f'<div class="svc-wrap">{r}</div>'

CATPANEL=f'''<div class="wrap cats" id="kategorijos">
  <div class="hd2"><span class="t">E-parduotuvės kategorijų vieta</span><span class="disabled-link" aria-disabled="true">E-parduotuvė netrukus</span></div>
  <div class="catgrid">
    <span class="cat cat-disabled"><span class="cic">{ic("i-rekup")}</span><b>Rekuperatoriai</b><span>Kategorijos peržiūros vieta</span><span class="go">Netrukus</span></span>
    <span class="cat cat-disabled"><span class="cic">{ic("i-kond")}</span><b>Kondicionieriai</b><span>Kategorijos peržiūros vieta</span><span class="go">Netrukus</span></span>
    <span class="cat cat-disabled"><span class="cic">{ic("i-shiluma")}</span><b>Šilumos siurbliai</b><span>Kategorijos peržiūros vieta</span><span class="go">Netrukus</span></span>
    <span class="cat cat-disabled"><span class="cic">{ic("i-priedai")}</span><b>Priedai ir montavimo medžiagos</b><span>Kategorijos peržiūros vieta</span><span class="go">Netrukus</span></span>
  </div></div>'''

CLIMATE=f'''<section style="padding-top:0"><div class="wrap"><div class="sh"><div><span class="kick">Sistemos vertinimo kryptys</span><h2>Keturi mikroklimato parametrai</h2></div></div>
  <div class="climate">
    <div class="cl">{ic("i-airflow")}<div><b>Oro srautas</b><span>Šviežias, tolygiai paskirstytas</span></div></div>
    <div class="cl">{ic("i-temp")}<div><b>Temperatūra</b><span>Šiluma tada, kai reikia</span></div></div>
    <div class="cl">{ic("i-cooling")}<div><b>Vėsinimas</b><span>Vėsu per karščius, tyliai</span></div></div>
    <div class="cl">{ic("i-energy")}<div><b>Efektyvumas</b><span>Vertinamas pagal sistemos duomenis</span></div></div>
  </div></div></section>'''

FINAL_CTA=cta("Renkate įrangą ar reikia serviso?","Padėsime pasirinkti tinkamą sprendimą, sumontuoti įrangą arba sutvarkyti jau veikiančią sistemą.",
    [btn("Rinktis įrangą","index.html#kategorijos"),btn("Užsakyti servisą","Užklausos forma.html","ghost cta-ghost")])

# ---- Realios darbų nuotraukos (content-review/img -> site-v2/img). Alt tekstai patvirtinti
# (strategas + IMG-INSTRUKCIJA), be išgalvotų vietų/klientų/tech parametrų. Matmenys tikri.
IMG={
 '01':('01-termovizija-kondicionierius.jpg','Termovizinė kondicionieriaus patikra — matomas šaldymo pasiskirstymas',501,512),
 '02':('02-olimpia-lauko-blokas.jpg','Sumontuotas Olimpia Splendid kondicionieriaus lauko blokas',1600,901),
 '03':('03-rekuperatorius.jpg','Sumontuotas rekuperatorius su ortakiais',1600,2842),
 '04':('04-testo-matavimo-iranga.jpg','„testo" oro srauto matavimo įranga',1600,901),
 '05':('05-toshiba-servisas.jpg','Toshiba šilumos siurblio servisas',1600,901),
 '06':('06-oro-srauto-matavimas.jpg','Oro srauto matavimas balansuojant vėdinimą',1600,2842),
 '07':('07-trane-agregatas.jpg','TRANE vėdinimo agregatas techninėje patalpoje',1600,900),
}
def photo(key,caption=None,cls=""):
    fn,alt,w,h=IMG[key]
    cap=f'<figcaption>{caption}</figcaption>' if caption else ''
    extra=(" "+cls) if cls else ""
    return (f'<figure class="photo{extra}">'
            f'<img src="img/{fn}" alt="{alt}" width="{w}" height="{h}" loading="lazy" '
            f'onerror="this.closest(&#39;figure&#39;).style.display=&#39;none&#39;">{cap}</figure>')
def gallery(keys,captions=None,kick="Mūsų darbai",title="Realūs mūsų darbai",sub="Nuotraukos iš tikrų Kraulis darbų."):
    caps=captions or {}
    cells="".join(photo(k,caps.get(k),"thermal" if k=="01" else "") for k in keys)
    return (f'<section class="gallery"><div class="wrap"><div class="sh"><div>'
            f'<span class="kick">{kick}</span><h2>{title}</h2></div><p>{sub}</p></div>'
            f'<div class="gwrap">{cells}</div></div></section>')

# ---- Social proof: 6 realios verbatim citatos (content-review) + realus agregatas.
# 7-os citatos NĖRA -> nekurta (Audrius/PM). Charles M. — anglų k. (lang="en").
PASLAUGOS_LT='https://paslaugos.lt/audrius-karnisauskas--kraulis-av4380'
REVIEWS=[
 ("Pro meistras — po remonto dar gavau matavimų ataskaitą; nesu matęs, kad kas taip dirbtų Lietuvoje. Rekomenduoju, ačiū Audriau!","Tadas Kaminskas","Rekuperatoriaus remontas · 2026-06",None),
 ("Darbas atliktas greitai, profesionaliai ir preciziškai. Audrius tiksliai sureguliavo oro srautus ir pakonsultavo apie priežiūrą. Name iškart juntamas geresnis oro balansas.","Danielius Šeštokas","Vėdinimo sistemos remontas · 2026-06",None),
 ("Meistras jau pirmo vizito metu sutvarkė problemą, kurios nepavyko išspręsti jau kurį laiką. Išsami konsultacija ir naudingi patarimai ateičiai. Geriausios rekomendacijos!","Diana","Kondicionieriaus remontas · 2026-05",None),
 ("Operatyviai sutvarkė rekuperatoriaus problemą. Rekomenduoju.","Juozas","Rekuperatoriaus remontas · 2026-07",None),
 ("Very professional and human person. He takes time for you and takes care of everything — rare these days. All at a very reasonable price.","Charles M.","Vėdinimo sistemos montavimas · 2026-06","en"),
 ("Dėkoju už greitą ir kokybišką paslaugą. Viskas puiku, sėkmės darbuose!","Jolanta","Kondicionieriaus montavimas · 2026-05",None),
]
def reviews():
    cards=""
    for quote,name,meta,lang in REVIEWS:
        lg=f' lang="{lang}"' if lang else ''
        cards+=(f'<figure class="rev"><div class="stars" aria-hidden="true">★★★★★</div>'
                f'<blockquote{lg}>„{quote}"</blockquote>'
                f'<figcaption>{name}<span>{meta}</span></figcaption></figure>')
    return (f'<section class="revs"><div class="wrap"><div class="sh"><div>'
            f'<span class="kick">Ką sako klientai</span><h2>Tikri klientų atsiliepimai</h2></div>'
            f'<p class="rating"><span class="stars" aria-hidden="true">★★★★★</span> <strong>5,0</strong> · 7 atsiliepimai</p></div>'
            f'<div class="revwrap">{cards}</div>'
            f'<p class="revsrc">Tikri klientų atsiliepimai iš <a href="{PASLAUGOS_LT}" target="_blank" rel="noopener noreferrer">Paslaugos.lt profilio</a> — 5,0 (7 atsiliepimai).</p>'
            f'</div></section>')

def why():
    items=[
      ("Neliekate be serviso","Sumontuojame ir liekame šalia — prižiūrime bei remontuojame, kad įranga tarnautų ilgai."),
      ("Dirbame su visų pagrindinių gamintojų įranga","Diagnozuojame ir remontuojame net tada, kai įrangą pirkote kitur."),
      ("Kvalifikacija, kuri svarbi","Ilgametė patirtis; atestuoti darbui su freonu (F-dujos) ir elektra. Kvalifikuotas montavimas gali pailginti gamintojo garantiją, tačiau terminas priklauso nuo konkretaus gamintojo ir modelio."),
      ("Aiškumas nuo pradžios","Prieš darbus aiškiai suderiname apimtį, eigą ir tolesnius žingsnius."),
    ]
    cells="".join(f'<div class="why-item"><span class="cic">{ic("i-prieziura")}</span><b>{h}</b><p>{p}</p></div>' for h,p in items)
    return (f'<section style="padding-top:0"><div class="wrap"><div class="sh"><div><span class="kick">Kodėl Kraulis</span>'
            f'<h2>Servisas, kuris nedingsta po pardavimo</h2></div></div>'
            f'<div class="whygrid">{cells}</div></div></section>')

print("helpers ready")
