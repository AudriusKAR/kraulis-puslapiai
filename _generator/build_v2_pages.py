# -*- coding: utf-8 -*-
from build_v2 import page, TEL, TELH, MAIL
from build_v2_content import (ic, crumbs, titlebar, chips, cta, btn, faq, process, priespo,
    HERO_SVG, DIVIDER, datasheet, CATPANEL, CLIMATE, FINAL_CTA)
import os

HOME_CRUMB=("Pradžia","index.html")

# ============================ PAGRINDINIS
home_body=f'''<section class="hero"><div class="wrap hgrid">
  <div>
    <span class="kick">ŠVOK inžinerija · Vilnius</span>
    <h1>Tylu. Šilta.<br><em>Šviežia.</em></h1>
    <p class="lead">Vėdinimo, šildymo ir vėsinimo įranga su servisu, kuris lieka ir po pardavimo. Išsirinkite — sumontuosime, subalansuosime ir prižiūrėsime.</p>
    <div class="doing"><span>{ic("i-shop","ic")}Parduodame</span><span>{ic("i-montavimas","ic")}Montuojame</span><span>{ic("i-remontas","ic")}Remontuojame ir prižiūrime</span></div>
    <div class="acts"><a class="btn btn-primary" href="#" data-todo="eshop-visa"><!-- TODO: e-parduotuvės nuoroda -->Į e-parduotuvę</a>{btn("Užsakyti servisą","Užklausos forma.html","ghost")}</div>
  </div>
  {HERO_SVG}
</div>
{CATPANEL}
</section>
{DIVIDER}
{process([("Parenkame sprendimą","Įvertiname patalpas, poreikį ir biudžetą, pasiūlome tinkamą įrangą."),
          ("Sumontuojame ir paleidžiame","Profesionalus montavimas, paleidimas ir sureguliavimas Vilniuje ir apylinkėse."),
          ("Prižiūrime ir remontuojame","Profilaktika, diagnostika ir remontas — kad sistema tarnautų ilgai.")],
         kick="Kaip dirbame",title="Vienose rankose — nuo parinkimo iki priežiūros",
         sub="Vienas telefonas visiems klausimams. Ir padedame net tada, kai įrangą pirkote kitur.")}
<section id="paslaugos" style="padding-top:0"><div class="wrap">
  <div class="sh"><div><span class="kick">Paslaugos · kainos „nuo“</span><h2>Priežiūra, remontas ir balansavimas</h2></div><p>Visų pagrindinių gamintojų įranga. Net jei įsigijote ne pas mus.</p></div>
  {datasheet()}
</div></section>
{priespo()}
{CLIMATE}
{FINAL_CTA}'''
page("index.html","Kraulis — ŠVOK įranga ir servisas Vilniuje","Vėdinimo, šildymo ir vėsinimo įranga su servisu, kuris lieka ir po pardavimo. Parduodame, montuojame, prižiūrime ir remontuojame. Vilnius ir apylinkės.",home_body,"")  # homepage: jokio false aria-current (logo = pradžia)

# ============================ PASLAUGOS (indeksas)
pasl_body=titlebar("Priežiūra, remontas ir balansavimas","Diagnozuojame, remontuojame ir sureguliuojame visų pagrindinių gamintojų įrangą — net jei ją įsigijote ne pas mus. Servisas namams ir verslui.",
    kick="Paslaugos",crumb=crumbs(HOME_CRUMB,("Paslaugos",None)))
pasl_body+=f'''<section><div class="wrap">{datasheet()}
  <div class="prose" style="margin-top:36px">
    <h2>Garantijos</h2>
    <p><strong>Įrangai — gamintojo garantija.</strong> Jos trukmė priklauso nuo gamintojo ir modelio. Daliai įrangos ji pailgėja, kai sumontuoja sertifikuoti montuotojai.</p>
    <p><strong>Darbams — mūsų garantija.</strong> Montavimo, remonto ir priežiūros darbams suteikiame garantiją. Jei po mūsų darbų kas nors veikia ne taip — grįžtame ir sutvarkome.</p>
  </div></div></section>'''
pasl_body+=priespo()
pasl_body+=cta("Nežinote, kurios paslaugos reikia?","Aprašykite situaciją ir įrangą — patarsime ir suderinsime tolesnį žingsnį.",
    [btn("Užsakyti servisą","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page("Paslaugos.html","Paslaugos — Kraulis | Priežiūra, remontas, montavimas, balansavimas","ŠVOK paslaugos Vilniuje: kondicionierių, šilumos siurblių ir rekuperatorių remontas, balansavimas su ataskaita, profilaktinė priežiūra, montavimas. Darbams garantija.",pasl_body,"paslaugos")

# ============================ PASLAUGŲ PUSLAPIAI (helper)
STEPS=[("Susisiekiate","Paskambinate arba parašote — grįšime su aiškiu tolesniu žingsniu. Aiškų gedimą dažnai įkainojame telefonu."),
       ("Diagnozuojame ir suderiname","Nustatome priežastį ir suderiname darbų apimtį bei kainą prieš tęsiant."),
       ("Sutvarkome ir paaiškiname","Atliekame darbus, patikriname sistemą ir paaiškiname, kaip naudoti, kad gedimai nesikartotų.")]
def service_page(fn,h1,lead,price,kick,signs_title,signs,body_html,faqs,mt,md):
    sl="".join(f"<li>{s}</li>" for s in signs)
    b=titlebar(h1,lead,kick=kick,crumb=crumbs(HOME_CRUMB,("Paslaugos","Paslaugos.html"),(h1,None)),meta=price,
        chips=chips([("Skambinti",TELH,ic("i-phone")),("Rašyti",f"mailto:{MAIL}",ic("i-mail")),("Užpildyti užklausą","Užklausos forma.html",ic("i-arrow"))]))
    b+=f'<section><div class="wrap"><div class="prose"><h2>{signs_title}</h2><ul>{sl}</ul>{body_html}</div></div></section>'
    b+=process(STEPS,kick="Kaip dirbame",title="Trys paprasti žingsniai")
    b+=faq(faqs,title="Dažni klausimai",kick="DUK")
    b+=cta("Užsakykite šią paslaugą","Aprašykite įrangą ir problemą — grįšime su aiškiu tolesniu žingsniu ir kaina.",
        [btn("Užsakyti servisą","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
    page(fn,mt,md,b,"paslaugos")

service_page("Paslauga - Kondicionierių remontas.html","Kondicionierių remontas",
  "Nešaldo, nešildo, teka, triukšmauja ar skleidžia kvapą? Surandame priežastį ir sutvarkome — visų pagrindinių gamintojų įrangą, net jei ją įsigijote ne pas mus.",
  "Diagnostika nuo 69 € · Darbams — garantija","Paslauga · Priežiūra ir remontas","Kada verta kreiptis",
  ["Kondicionierius nešaldo arba nešildo taip, kaip anksčiau","Iš vidinio bloko laša arba teka vanduo","Atsirado triukšmas, vibracija ar nemalonus kvapas","Rodomas klaidos kodas ar mirksi indikatoriai"],
  '''<h2>Ką apima remontas</h2><p>Diagnozuojame gedimą, suderiname darbų apimtį ir kainą, pašaliname priežastį ir <strong>patikriname sistemą po remonto</strong>. Remontuojame sieninius (split), multi-split ir kanalinius kondicionierius: <strong>Mitsubishi Electric, Samsung, Midea, Airwell, Cooper&amp;Hunter</strong> ir kt.</p>
  <div class="note"><strong>Svarbu:</strong> reguliari filtrų ir vidinio bloko priežiūra padeda išvengti dalies gedimų. Žr. <a href="Paslauga - Profilaktinė priežiūra.html">profilaktinę priežiūrą</a>.</div>''',
  [("Ar remontuojate ne pas jus pirktą kondicionierių?","Taip. Diagnozuojame ir remontuojame visų pagrindinių gamintojų įrangą, nepriklausomai nuo to, kur ją pirkote."),
   ("Kiek kainuoja diagnostika?","Diagnostika — nuo 69 €. Kainą už darbus suderiname prieš pradedant."),
   ("Ar suteikiate garantiją darbams?","Taip, atliktiems remonto darbams suteikiame garantiją.")],
  "Kondicionierių remontas Vilniuje — Kraulis | Diagnostika nuo 69 €","Kondicionierių remontas Vilniuje: nešaldo, teka, triukšmauja ar klaidos. Visų gamintojų įranga. Diagnostika nuo 69 €, darbams garantija.")

service_page("Paslauga - Šilumos siurblių remontas.html","Šilumos siurblių remontas",
  "Remontuojame šilumos siurblius: oras–oras ir oras–vanduo. Kad šiluma nedingtų tada, kai jos labiausiai reikia.",
  "Diagnostika nuo 69 € · Darbams — garantija","Paslauga · Priežiūra ir remontas","Kada verta kreiptis",
  ["Sistema nebešildo arba šildo silpnai","Smarkiai išaugo elektros sąnaudos","Lauko blokas apledija ir neatsileidžia","Rodomi klaidų kodai arba sistema stabdosi"],
  '''<h2>Ką apima remontas</h2><p>Nustatome priežastį, suderiname darbų apimtį bei kainą, pašaliname gedimą ir patikriname sistemą po remonto. Dirbame su <strong>oras–oras ir oras–vanduo</strong> šilumos siurbliais.</p>
  <div class="note"><strong>Garantija ir priežiūra:</strong> gamintojų garantijos sąlygose dažnai numatyta periodinė priežiūra. Reguliari <a href="Paslauga - Profilaktinė priežiūra.html">profilaktika</a> padeda ją išsaugoti.</div>''',
  [("Kokius šilumos siurblius remontuojate?","Oras–oras ir oras–vanduo, visų pagrindinių gamintojų."),
   ("Ar galite padėti su sudėtinga sistema?","Taip. Į sudėtingas situacijas žiūrime kaip į galimybę rasti praktišką sprendimą."),
   ("Kiek kainuoja diagnostika?","Nuo 69 €. Kainą suderiname prieš pradedant darbus.")],
  "Šilumos siurblių remontas Vilniuje — Kraulis | Nuo 69 €","Šilumos siurblių remontas: oras–oras ir oras–vanduo. Diagnostika nuo 69 €, darbams garantija. Vilnius ir apylinkės.")

service_page("Paslauga - Rekuperatorių remontas.html","Rekuperatorių remontas",
  "Triukšmas, drėgmė, silpna trauka ar klaidos pranešimai — diagnozuojame ir remontuojame rekuperatorius bei vėdinimo sistemas, kad oras namuose vėl būtų šviežias.",
  "Diagnostika nuo 69 € · Darbams — garantija","Paslauga · Priežiūra ir remontas","Kada verta kreiptis",
  ["Sumažėjo oro trauka arba vėdinimas jaučiasi silpnas","Padidėjo drėgmė, rasoja langai","Girdimas triukšmas ar vibracija iš įrenginio","Rodomi klaidos pranešimai arba užsiteršę filtrai"],
  '''<h2>Ką apima remontas</h2><p>Diagnozuojame rekuperatoriaus ir vėdinimo sistemos gedimą, pašaliname priežastį ir patikriname veikimą. Dažnai problemą lemia užsiteršę filtrai, ventiliatoriaus ar automatikos gedimas.</p>
  <div class="note">Jei sutrikęs oro pasiskirstymas — gali prireikti <a href="Paslauga - Rekuperatorių balansavimas.html">oro srautų balansavimo</a> su ataskaita „prieš/po“.</div>''',
  [("Kuo skiriasi remontas nuo balansavimo?","Remontas šalina gedimą; balansavimas — oro srautų išmatavimas ir sureguliavimas kiekvienoje patalpoje."),
   ("Ar remontuojate ne jūsų sumontuotą sistemą?","Taip, visų pagrindinių gamintojų rekuperatorius."),
   ("Kaip dažnai reikia keisti filtrus?","Priklauso nuo modelio ir aplinkos; tikslų intervalą pasakome apžiūros metu.")],
  "Rekuperatorių remontas Vilniuje — Kraulis | Nuo 69 €","Rekuperatorių ir vėdinimo sistemų remontas: triukšmas, drėgmė, silpna trauka, klaidos. Diagnostika nuo 69 €, darbams garantija.")

service_page("Paslauga - Rekuperatorių balansavimas.html","Rekuperatorių balansavimas",
  "Išmatuojame ir subalansuojame oro padavimo bei ištraukimo srautus kiekviename patalpos taške. Po darbų gaunate matavimų ataskaitą „prieš ir po“.",
  "Nuo 149 € · Darbams — garantija","Paslauga · Priežiūra ir remontas","Kada verta balansuoti",
  ["Vienose patalpose per stipri trauka, kitose — beveik nėra","Naujai sumontuota sistema dar nebuvo subalansuota","Jaučiamas triukšmas dėl per didelių srautų","Norite dokumentuoto įrodymo, kad sistema veikia kaip suprojektuota"],
  '''<h2>Kaip vyksta balansavimas</h2><p>Išmatuojame oro srautus kiekviename difuzoriuje bei grotelėse, palyginame su projektinėmis reikšmėmis ir sureguliuojame taip, kad kiekvienoje patalpoje būtų tinkamas oro kiekis.</p>
  <div class="note"><strong>Skaidrumas, kurį matote:</strong> po balansavimo gaunate matavimų ataskaitą su reikšmėmis „prieš ir po“ kiekviename taške.</div>
  <h2>Ką duoda subalansuota sistema</h2><ul><li>Tolygus, komfortiškas oras visose patalpose</li><li>Mažesnis triukšmas ir skersvėjų pojūtis</li><li>Efektyvesnis veikimas ir mažesnės sąnaudos</li><li>Dokumentuotas sistemos veikimo įrodymas</li></ul>''',
  [("Kas yra oro srautų balansavimas?","Sistemos oro srautų išmatavimas ir sureguliavimas, kad kiekvienoje patalpoje būtų projektuotas oro kiekis."),
   ("Ką gausiu po darbų?","Matavimų ataskaitą su reikšmėmis „prieš ir po“ reguliavimo kiekviename taške."),
   ("Kiek kainuoja balansavimas?","Nuo 149 €. Tiksli kaina priklauso nuo taškų skaičiaus; ją suderiname iš anksto.")],
  "Rekuperatorių balansavimas su ataskaita — Kraulis | Nuo 149 €","Rekuperacijos oro srautų balansavimas Vilniuje: matavimai kiekviename taške ir ataskaita „prieš ir po“. Nuo 149 €, darbams garantija.")

service_page("Paslauga - Profilaktinė priežiūra.html","Profilaktinė priežiūra",
  "Gedimo nėra — ir tegul taip lieka. Patikriname veikimą, išvalome, įvertiname susidėvėjimą ir patariame, kaip naudoti, kad įranga tarnautų ilgiau ir taupiau.",
  "Nuo 99 € · Darbams — garantija","Paslauga · Priežiūra ir remontas","Kodėl verta prižiūrėti reguliariai",
  ["Palaikoma šaldymo/šildymo galia ir efektyvumas","Mažesnė gedimų tikimybė ir netikėtos išlaidos","Švaresnis oras ir mažiau kvapų","Padeda išsaugoti gamintojo garantiją"],
  '''<h2>Ką apima priežiūra</h2><p>Atvykstame, patikriname veikimą, išvalome, įvertiname susidėvėjimą ir patariame, kaip naudoti įrangą, kad ji tarnautų ilgiau ir taupiau. Priežiūrą pritaikome pagal įrangos tipą.</p>
  <div class="note"><strong>Gamintojo garantija:</strong> jos sąlygose dažnai numatyta periodinė priežiūra — reguliari profilaktika padeda garantiją išsaugoti.</div>''',
  [("Kaip dažnai reikia profilaktikos?","Priklauso nuo įrangos tipo ir naudojimo; tinkamą intervalą pasakome pagal jūsų įrangą."),
   ("Kiek kainuoja priežiūra?","Nuo 99 €. Tikslią kainą suderiname pagal įrangą ir darbų apimtį."),
   ("Ar prižiūrite ne pas jus pirktą įrangą?","Taip, visų pagrindinių gamintojų.")],
  "Profilaktinė ŠVOK priežiūra Vilniuje — Kraulis | Nuo 99 €","Kondicionierių, šilumos siurblių ir rekuperatorių profilaktinė priežiūra: patikra, valymas, susidėvėjimo įvertinimas. Nuo 99 €.")

service_page("Paslauga - Įrangos montavimas.html","Įrangos montavimas",
  "Sumontuojame ir paleidžiame šilumos siurblius, kondicionierius ir rekuperatorius — nuo sistemos parinkimo iki sureguliavimo. Vienos rankos nuo pradžios iki galo.",
  "Kaina — pagal sprendimą, suderinama iš anksto · Darbams — garantija","Paslauga","Ką apima montavimas",
  ["Sistema parenkama pagal patalpas ir biudžetą","Profesionalus montavimas ir prijungimas","Paleidimas ir sureguliavimas","Paaiškiname naudojimą ir priežiūrą"],
  '''<h2>Kokią įrangą montuojame</h2><ul><li>Šilumos siurbliai — oras–oras ir oras–vanduo</li><li>Kondicionieriai — sieniniai (split), multi-split, kanaliniai</li><li>Rekuperatoriai ir vėdinimo sistemos</li></ul>
  <p>Dirbame su patikimų gamintojų įranga: <strong>Mitsubishi Electric, Samsung, Midea, Zehnder, Recom, Airwell, Cooper&amp;Hunter</strong> ir kt. Galime pasiūlyti ir parduoti įrangą su montavimu.</p>
  <div class="note"><strong>Sertifikuotas montavimas:</strong> daliai įrangos gamintojo garantija pailgėja, kai ją sumontuoja sertifikuoti montuotojai.</div>''',
  [("Ar galiu pirkti įrangą su montavimu?","Taip. Galime pasiūlyti ir parduoti įrangą kartu su montavimu Vilniaus regione."),
   ("Ar montavimas turi įtakos garantijai?","Daliai įrangos gamintojo garantija pailgėja, kai ją sumontuoja sertifikuoti montuotojai."),
   ("Kiek kainuoja montavimas?","Kaina priklauso nuo sistemos ir objekto; ją suderiname iš anksto po konsultacijos.")],
  "Įrangos montavimas Vilniuje — Kraulis","Šilumos siurblių, kondicionierių ir rekuperatorių montavimas Vilniuje: parinkimas, montavimas, paleidimas ir sureguliavimas. Darbams garantija.")

print("service pages done")
