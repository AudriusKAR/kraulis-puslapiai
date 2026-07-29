# -*- coding: utf-8 -*-
import io, os
from build_cr import (page_cr, anno, OUT_CR, reviews_block, review_lead, REVIEWS,
    G_GAR, G_PRAT, TERITORIJA, img_fig, photo_strip)
from build_v2 import MAIL, TEL, TELH
from build_v2_content import (ic, crumbs, titlebar, chips, cta, btn, faq, process, priespo,
    HERO_SVG, DIVIDER, datasheet, CATPANEL, CLIMATE)
H=("Pradžia","index.html")

# ===================== PAGRINDINIS (revised lead: aiškiau įranga+montavimas+servisas)
home=f'''<section class="hero"><div class="wrap hgrid">
  <div>
    <span class="kick">Įranga · montavimas · servisas · Vilnius</span>
    <h1>Tylu. Šilta.<br><em>Šviežia.</em></h1>
    <p class="lead">Kraulis parduoda vėdinimo, šildymo ir vėsinimo įrangą, ją sumontuoja ir prižiūri. Viena komanda pasirūpina visu keliu — nuo parinkimo iki serviso. Ir padeda net tada, kai įrangą pirkote kitur.</p>
    <div class="doing"><span>{ic("i-shop","ic")}Parduodame</span><span>{ic("i-montavimas","ic")}Montuojame</span><span>{ic("i-remontas","ic")}Prižiūrime ir remontuojame</span></div>
    <div class="acts"><a class="btn btn-primary" href="#" data-todo="eshop-visa">Į e-parduotuvę</a><a class="btn btn-ghost" href="Užklausos forma.html">Užsakyti servisą</a></div>
  </div>
  {HERO_SVG}
</div>
{CATPANEL}
</section>
{DIVIDER}
{process([("Parenkame sprendimą","Pagal patalpas, poreikį ir biudžetą pasiūlome tinkamą įrangą — be perteklinės galios."),
          ("Sumontuojame ir paleidžiame","Sumontuojame, paleidžiame ir sureguliuojame Vilniuje ir apylinkėse."),
          ("Prižiūrime ir remontuojame","Profilaktika, diagnostika ir remontas — kad sistema veiktų ilgai ir taupiai.")],
         kick="Vienose rankose",title="Nuo įrangos parinkimo iki nuolatinės priežiūros",
         sub="Vienas telefonas visiems klausimams. Nesvarbu, ar tik renkatės, ar reikia sutvarkyti turimą sistemą.")}
<section id="paslaugos" style="padding-top:0"><div class="wrap">
  <div class="sh"><div><span class="kick">Paslaugos · kainos „nuo“</span><h2>Servisas visų gamintojų ŠVOK įrangai</h2></div><p>Diagnozuojame, remontuojame ir prižiūrime — net jei įrangą įsigijote ne pas mus.</p></div>
  {datasheet()}
</div></section>
{priespo(h2="Nesakome „viskas gerai“ žodžiais.",
         p="Po rekuperacijos balansavimo pateikiame matavimų ataskaitą su oro srautų reikšmėmis prieš ir po reguliavimo — kiekviename taške. Matote tiksliai, kaip veikia jūsų sistema.")}
{CLIMATE}
{photo_strip(["toshiba","matavimas","olimpia","termovizija"],sub="Servisas, montavimas ir matavimai realiuose objektuose — dirbame su profesionalia „testo“ įranga.")}
{reviews_block(sub="Realūs žmonės, kuriems jau padėjome — remontas, montavimas ir balansavimas. Įsigijote įrangą kitur? Vis tiek liekate su servisu.")}
{cta("Renkate įrangą ar reikia serviso?","Padėsime pasirinkti tinkamą sprendimą, sumontuoti įrangą arba sutvarkyti jau veikiančią sistemą — ir liekame šalia, kai prireiks serviso.",
    [btn("Rinktis įrangą","index.html#kategorijos"),btn("Užsakyti servisą","Užklausos forma.html","ghost cta-ghost")])}'''
page_cr("Pagrindinis.html","Kraulis — ŠVOK įranga ir servisas Vilniuje","Vėdinimo, šildymo ir vėsinimo įranga su montavimu ir servisu Vilniuje. Parduodame, sumontuojame, prižiūrime ir remontuojame — net jei pirkote kitur.",home,"",
    anno("nukreipti į įrangą arba servisą; akcentuoti servisą po pardavimo","visi (renkasi ar turi įrangą)","„Rinktis įrangą“ / „Užsakyti servisą“","kategorijų turinys (Q3–5)"),"index.html")

# ===================== PASLAUGOS
pasl=titlebar("Servisas visų gamintojų ŠVOK įrangai","Diagnozuojame, remontuojame, prižiūrime ir balansuojame — namams ir verslui. Aiškios „nuo“ kainos, garantija darbams. Padedame ir tada, kai įrangą pirkote kitur.",
    kick="Paslaugos",crumb=crumbs(H,("Paslaugos",None)))
pasl+=f'''<section><div class="wrap">{datasheet()}
  <div class="prose" style="margin-top:36px">
    <h2>Kodėl verta pas Kraulis</h2>
    <p>Dirbame su visu ciklu — nuo įrangos parinkimo iki nuolatinės priežiūros. Todėl matome sistemą kaip visumą, o ne pavienį gedimą. Prieš darbus suderiname apimtį ir kainą, o po jų paaiškiname, kaip naudoti, kad problema nesikartotų.</p>
    <h2>Garantijos</h2>
    <p><strong>Darbams — mūsų garantija {G_GAR}</strong> (priklauso nuo darbų pobūdžio). Jei per šį laiką kas nors veikia ne taip dėl mūsų darbo — grįžtame ir sutvarkome. <strong>Įrangai — gamintojo garantija</strong> pagal įstatymus; kai įrangą sumontuoja mūsų kvalifikuoti specialistai, ji <strong>pailgėja {G_PRAT}</strong>.</p>
  </div></div></section>'''
pasl+=priespo()
pasl+=cta("Nežinote, kurios paslaugos reikia?","Aprašykite įrangą ir problemą — patarsime ir suderinsime tolesnį žingsnį.",
    [btn("Užpildyti užklausą","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page_cr("Paslaugos.html","Paslaugos — Kraulis | Remontas, priežiūra, montavimas, balansavimas","ŠVOK servisas Vilniuje: kondicionierių, šilumos siurblių ir rekuperatorių remontas (diagnostika nuo 69 €), priežiūra (nuo 99 €), balansavimas su ataskaita (nuo 149 €), montavimas.",pasl,"paslaugos",
    anno("apžvalga + kelias į konkrečią paslaugą","turintys įrangą / gedimą","„Užpildyti užklausą“","garantija darbams — nuo 3 iki 24 mėn. (patvirtinta); pilnas paslaugų sąrašas (Q6)"),"Paslaugos.html")

# ===================== PASLAUGŲ PUSLAPIAI su technine kompetencija
STEPS=[("Susisiekiate","Paskambinate arba parašote. Aiškų gedimą dažnai įkainojame ar patariame jau telefonu."),
       ("Diagnozuojame ir suderiname","Nustatome tikrąją priežastį ir suderiname darbų apimtį bei kainą prieš tęsdami."),
       ("Sutvarkome ir paaiškiname","Atliekame darbus, patikriname sistemą ir paaiškiname, kaip naudoti, kad gedimas nesikartotų.")]
def svc(fn,h1,lead,price,kick,intro,tikrinam_title,tikrinam,faqs,mt,md,ann_wait,priespo_block=False,rev=None,photos=None):
    tk="".join(f"<li>{s}</li>" for s in tikrinam)
    b=titlebar(h1,lead,kick=kick,crumb=crumbs(H,("Paslaugos","Paslaugos.html"),(h1,None)),meta=price,
        chips=chips([("Skambinti",TELH,ic("i-phone")),("Rašyti",f"mailto:{MAIL}",ic("i-mail")),("Užpildyti užklausą","Užklausos forma.html",ic("i-arrow"))]))
    b+=f'<section><div class="wrap"><div class="prose">{intro}<h2>{tikrinam_title}</h2><ul>{tk}</ul></div></div></section>'
    if photos: b+=photo_strip(photos)
    if priespo_block: b+=priespo()
    if rev: b+=f'<section style="padding-top:0">{review_lead(*rev)}</section>'
    b+=process(STEPS,kick="Kaip dirbame",title="Trys paprasti žingsniai")
    b+=faq(faqs,title="Dažni klausimai",kick="DUK")
    b+=cta("Užsakykite šią paslaugą","Aprašykite įrangą (gamintoją/modelį, jei žinote) ir problemą — grįšime su aiškiu žingsniu ir kaina.",
        [btn("Užpildyti užklausą","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
    page_cr(fn,mt,md,b,"paslaugos",anno("įtikinti dėl paslaugos + užsakyti","turintys šią problemą","„Užpildyti užklausą“",ann_wait),fn)

svc("Paslauga - Kondicionierių remontas.html","Kondicionierių remontas",
  "Nešaldo, nešildo, teka, triukšmauja ar rodo klaidą? Randame priežastį ir sutvarkome. Sieninius (split), multi-split ir kanalinius — visų pagrindinių gamintojų, net jei pirkote kitur.",
  f"Diagnostika nuo 69 € · Darbams — garantija {G_GAR}","Paslauga · Priežiūra ir remontas",
  '<p>Kondicionieriaus problema retai būna atsitiktinė — dažniausiai tai šaltnešio trūkumas, užsiteršęs radiatorius ar filtrai, kondensato nutekėjimo ar automatikos gedimas. Randame tikrąją priežastį, o ne tik pašaliname simptomą.</p>',
  "Ką patikriname ir sutvarkome",
  ["Šaltnešio kiekį ir sistemos sandarumą","Vidinio bloko ir filtrų būklę, kondensato nutekėjimą","Ventiliatorių, kompresorių ir automatikos veikimą","Šaldymo/šildymo galią po remonto"],
  [("Ar remontuojate ne pas jus pirktą kondicionierių?","Taip. Diagnozuojame ir remontuojame visų pagrindinių gamintojų įrangą, nepriklausomai nuo to, kur ją pirkote."),
   ("Kiek kainuoja diagnostika?","Diagnostika — nuo 69 €. Aiškų gedimą dažnai įkainojame dar prieš atvykdami; kitu atveju kainą suderiname prieš darbus."),
   ("Ar suteikiate garantiją darbams?",f"Taip. Darbams suteikiame garantiją — {G_GAR}, priklausomai nuo darbų pobūdžio.")],
  "Kondicionierių remontas Vilniuje — Kraulis | Diagnostika nuo 69 €","Kondicionierių remontas Vilniuje: nešaldo, teka, triukšmauja ar klaidos. Randame priežastį ir sutvarkome. Diagnostika nuo 69 €, darbams garantija.",
  "dažnos problemos (Q20)",photos=["termovizija"])

svc("Paslauga - Šilumos siurblių remontas.html","Šilumos siurblių remontas",
  "Šildo silpnai, augo sąnaudos, apledija lauko blokas ar rodo klaidą? Remontuojame oras–oras, oras–vanduo ir geoterminius šilumos siurblius — kad šiluma nedingtų tada, kai jos labiausiai reikia.",
  f"Diagnostika nuo 69 € · Darbams — garantija {G_GAR}","Paslauga · Priežiūra ir remontas",
  '<p>Šilumos siurblio efektyvumas krenta pamažu, todėl problema dažnai pastebima tik pagal sąskaitą. Patikriname visą grandinę — nuo šaltnešio ir atitirpinimo iki automatikos — ir grąžiname sistemą į projektinį efektyvumą.</p>',
  "Ką patikriname ir sutvarkome",
  ["Šaltnešio kiekį ir sandarumą","Lauko bloko atitirpinimo (defrost) veikimą","Kompresoriaus, ventiliatorių ir siurblio darbą","Automatiką, jutiklius ir šildymo galią po remonto"],
  [("Kokius šilumos siurblius remontuojate?","Oras–oras, oras–vanduo ir geoterminius (žemė–vanduo), visų pagrindinių gamintojų."),
   ("Padėsite su sudėtinga ar sena sistema?","Taip. Į sudėtingas situacijas žiūrime kaip į galimybę rasti praktišką sprendimą — net jei pagalbos negaunate kitur."),
   ("Kiek kainuoja iškvietimas ir diagnostika?","Diagnostika — nuo 69 €. Kainą už darbus suderiname iš anksto.")],
  "Šilumos siurblių remontas Vilniuje — Kraulis | Nuo 69 €","Šilumos siurblių remontas: oras–oras, oras–vanduo ir geoterminiai. Randame priežastį, grąžiname efektyvumą. Diagnostika nuo 69 €, darbams garantija.",
  "dažnos problemos (Q20)",photos=["toshiba"])

svc("Paslauga - Rekuperatorių remontas.html","Rekuperatorių remontas",
  "Silpna trauka, drėgmė, triukšmas ar klaidos? Diagnozuojame ir remontuojame rekuperatorius bei vėdinimo sistemas, kad namuose vėl būtų šviežias oras be nereikalingos drėgmės.",
  f"Diagnostika nuo 69 € · Darbams — garantija {G_GAR}","Paslauga · Priežiūra ir remontas",
  '<p>Dažniausiai kaltininkas — užsiteršę filtrai, ventiliatoriaus ar automatikos gedimas arba netinkamai sureguliuoti srautai. Randame priežastį, o jei sutrikęs oro pasiskirstymas — pasiūlome <a href="Paslauga - Rekuperatorių balansavimas.html">balansavimą su matavimų ataskaita</a>.</p>',
  "Ką patikriname ir sutvarkome",
  ["Filtrų būklę ir šilumokaičio švarą","Ventiliatorių ir automatikos veikimą","Oro srautus ir traukos tolygumą","Drėgmės ir kondensato problemas"],
  [("Kuo skiriasi remontas nuo balansavimo?","Remontas šalina gedimą (pvz., ventiliatoriaus ar automatikos). Balansavimas — oro srautų išmatavimas ir sureguliavimas kiekvienoje patalpoje."),
   ("Ar remontuojate ne jūsų sumontuotą sistemą?","Taip, visų pagrindinių gamintojų rekuperatorius."),
   ("Kaip dažnai reikia keisti filtrus?","Priklauso nuo modelio ir aplinkos; tikslų intervalą pasakome apžiūros metu.")],
  "Rekuperatorių remontas Vilniuje — Kraulis | Nuo 69 €","Rekuperatorių ir vėdinimo sistemų remontas: silpna trauka, drėgmė, triukšmas, klaidos. Diagnostika nuo 69 €, darbams garantija.",
  "dažnos problemos (Q20)",photos=["rekuperatorius"])

svc("Paslauga - Rekuperatorių balansavimas.html","Rekuperatorių balansavimas",
  "Vienur skersvėjis, kitur tvanku? Išmatuojame ir subalansuojame oro srautus kiekviename taške, o rezultatą pateikiame matavimų ataskaita „prieš ir po“. Nustojate spėlioti.",
  "Nuo 149 € · Darbams — garantija","Paslauga · Priežiūra ir remontas",
  '<p>Net geras rekuperatorius veikia prastai, jei srautai nesubalansuoti. Balansavimas — tai tikslus matavimas ir sureguliavimas, po kurio kiekvienoje patalpoje gaunamas projektinis oro kiekis: nei per daug, nei per mažai.</p>',
  "Ką duoda subalansuota sistema",
  ["Tolygus, komfortiškas oras visose patalpose","Mažiau triukšmo ir skersvėjų pojūčio","Efektyvesnis veikimas ir mažesnės sąnaudos","Dokumentuotas įrodymas — matavimų ataskaita „prieš/po“"],
  [("Kas yra oro srautų balansavimas?","Sistemos oro srautų išmatavimas kiekviename difuzoriuje ir sureguliavimas iki projektinių reikšmių."),
   ("Ką gausiu po darbų?","Matavimų ataskaitą su reikšmėmis „prieš ir po“ reguliavimo kiekviename taške."),
   ("Kiek kainuoja balansavimas?","Nuo 149 €. Tiksli kaina priklauso nuo taškų skaičiaus; ją suderiname iš anksto.")],
  "Rekuperatorių balansavimas su ataskaita — Kraulis | Nuo 149 €","Rekuperacijos oro srautų balansavimas Vilniuje: matavimai kiekviename taške ir ataskaita „prieš ir po“. Nuo 149 €, darbams garantija.",
  "realios ataskaitos pavyzdys (Q24 — Audrius turi, tobulina)",priespo_block=True,rev=REVIEWS[0],photos=["matavimas","testo"])

svc("Paslauga - Profilaktinė priežiūra.html","Profilaktinė priežiūra",
  "Gedimo nėra — ir tegul taip lieka. Reguliari priežiūra palaiko galią, mažina netikėtus gedimus ir padeda išsaugoti gamintojo garantiją.",
  "Nuo 99 € · Darbams — garantija","Paslauga · Priežiūra ir remontas",
  '<p>Įranga tarnauja ilgai ir taupiai tada, kai ja nuolat rūpinamasi. Priežiūrą pritaikome pagal įrangos tipą — kondicionierių, šilumos siurblį ar rekuperatorių — ir paaiškiname, kada verta ją kartoti.</p>',
  "Ką apima priežiūra",
  ["Filtrų ir vidinių dalių valymą","Veikimo, galios ir sandarumo patikrą","Susidėvėjimo įvertinimą ir rekomendacijas","Nustatymų peržiūrą taupesniam darbui"],
  [("Kaip dažnai reikia profilaktikos?","Priklauso nuo įrangos tipo ir naudojimo; tinkamą intervalą pasakome pagal jūsų įrangą."),
   ("Kiek kainuoja priežiūra?","Nuo 99 €. Tikslią kainą suderiname pagal įrangą ir darbų apimtį."),
   ("Ar priežiūra padeda išsaugoti garantiją?","Taip — gamintojai garantijos sąlygose dažnai reikalauja periodinės priežiūros.")],
  "Profilaktinė ŠVOK priežiūra Vilniuje — Kraulis | Nuo 99 €","Kondicionierių, šilumos siurblių ir rekuperatorių profilaktinė priežiūra: valymas, patikra, susidėvėjimo įvertinimas. Nuo 99 €.",
  "priminimų formuluotė (Q14); garantijos trukmė (Q9)")

svc("Paslauga - Įrangos montavimas.html","Įrangos montavimas",
  "Sumontuojame ir paleidžiame šilumos siurblius, kondicionierius ir rekuperatorius — nuo sistemos parinkimo iki sureguliavimo. Vienos rankos nuo pradžios iki galo.",
  f"Kaina — pagal sprendimą, suderinama iš anksto · Darbams — garantija {G_GAR}","Paslauga",
  '<p>Tinkamas montavimas svarbus ne tik veikimui — daliai įrangos <strong>gamintojo garantija pailgėja</strong>, kai ją sumontuoja kvalifikuoti specialistai. Turime F-dujų (freono) tvarkymo atestatą — būtiną teisėtam darbui su šaltnešiu. Todėl darbą planuojame nuo teisingo sprendimo parinkimo, o ne nuo skylės sienoje.</p>',
  "Ką apima montavimas",
  ["Sistemos parinkimą pagal patalpas ir biudžetą","Profesionalų montavimą ir prijungimą","Paleidimą ir sureguliavimą","Naudojimo ir priežiūros paaiškinimą"],
  [("Ar galiu pirkti įrangą su montavimu?","Taip. Galime pasiūlyti ir parduoti įrangą kartu su montavimu Vilniaus regione."),
   ("Ar montavimas turi įtakos garantijai?",f"Taip — teigiama prasme. Kai įrangą sumontuoja mūsų kvalifikuoti specialistai, gamintojo garantija pailgėja {G_PRAT}. Kraulis turi reikiamus atestatus, įskaitant F-dujų (freono) tvarkymo."),
   ("Kiek kainuoja montavimas?","Priklauso nuo sistemos ir objekto; kainą suderiname po konsultacijos.")],
  "Įrangos montavimas Vilniuje — Kraulis","Šilumos siurblių, kondicionierių ir rekuperatorių montavimas Vilniuje: parinkimas, montavimas, paleidimas ir sureguliavimas. Montavimo darbams garantija.",
  "gamintojų sąrašas (Q4)",photos=["olimpia","toshiba"])

print("cr service + home + paslaugos done")
