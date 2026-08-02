# -*- coding: utf-8 -*-
from build_v2 import page, TEL, TELH, MAIL
from build_v2_content import (ic, crumbs, titlebar, chips, cta, btn, faq, process, priespo,
    HERO_SVG, DIVIDER, datasheet, CATPANEL, CLIMATE, FINAL_CTA)
import os

HOME_CRUMB=("Pradžia","index.html")

# ============================ PAGRINDINIS
home_body=f'''<section class="hero"><div class="wrap hgrid">
  <div>
    <span class="kick">ŠVOK įranga ir paslaugos</span>
    <h1>Tylu. Šilta.<br><em>Šviežia.</em></h1>
    <p class="lead">Informacija apie vėdinimo, šildymo ir vėsinimo įrangą, montavimą, priežiūrą ir remontą — vienoje aiškioje vietoje.</p>
    <div class="doing"><span>{ic("i-shop","ic")}E-parduotuvė</span><span>{ic("i-montavimas","ic")}Montavimas</span><span>{ic("i-remontas","ic")}Remontas ir priežiūra</span></div>
    <div class="acts"><span class="btn btn-primary" aria-disabled="true">E-parduotuvė netrukus</span>{btn("Užsakyti servisą","Užklausos forma.html","ghost")}</div>
  </div>
  {HERO_SVG}
</div>
{CATPANEL}
</section>
{DIVIDER}
{process([("Aptariame poreikį","Surinkus pagrindinę informaciją aiškėja tinkamiausias kitas žingsnis."),
          ("Suderiname darbų eigą","Prieš darbus aptariama apimtis ir reikalinga informacija."),
          ("Patikriname rezultatą","Baigus darbus įvertinamas sistemos veikimas ir tolesnė priežiūra.")],
         kick="Paslaugų eiga",title="Aiški kelionė nuo klausimo iki sprendimo",
         sub="Vienas kontaktas įrangos, montavimo, priežiūros ir remonto klausimams.")}
<section id="paslaugos" style="padding-top:0"><div class="wrap">
  <div class="sh"><div><span class="kick">Paslaugos</span><h2>Priežiūra, remontas ir balansavimas</h2></div><p>Pasirinkite aktualią paslaugos kryptį arba pateikite bendrą užklausą.</p></div>
  {datasheet()}
</div></section>
{priespo()}
{CLIMATE}
{FINAL_CTA}'''
page("index.html","Kraulis — ŠVOK įranga, montavimas ir servisas","Vėdinimo, šildymo ir vėsinimo įrangos, montavimo, priežiūros ir remonto informacija bei užklausos.",home_body,"")  # homepage: jokio false aria-current (logo = pradžia)

# ============================ PASLAUGOS (indeksas)
pasl_body=titlebar("Priežiūra, remontas ir balansavimas","Pasirinkite paslaugos kryptį pagal įrangą ir pastebėtą problemą. Jei abejojate, pradėkite nuo bendros užklausos.",
    kick="Paslaugos",crumb=crumbs(HOME_CRUMB,("Paslaugos",None)))
pasl_body+=f'''<section><div class="wrap">{datasheet()}
  <div class="prose" style="margin-top:36px">
    <h2>Ką pateikti užklausoje</h2>
    <p>Nurodykite įrangos tipą, modelį, pastebėtus simptomus ir kada problema prasidėjo. Nuotraukas ar papildomą informaciją galima pateikti vėliau, kai bus suderintas kontaktas.</p>
    <!-- REIKIA_PATVIRTINIMO: garantijų politika, gamintojai ir paslaugų aprėptis -->
  </div></div></section>'''
pasl_body+=priespo()
pasl_body+=cta("Nežinote, kurios paslaugos reikia?","Aprašykite situaciją ir įrangą — patarsime ir suderinsime tolesnį žingsnį.",
    [btn("Užsakyti servisą","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page("Paslaugos.html","Paslaugos — Kraulis | Priežiūra, remontas, montavimas, balansavimas","ŠVOK paslaugų apžvalga: kondicionierių, šilumos siurblių ir rekuperatorių remontas, balansavimas, profilaktinė priežiūra ir montavimas.",pasl_body,"paslaugos")

# ============================ PASLAUGŲ PUSLAPIAI (helper)
STEPS=[("Susisiekiate","Pateikiate telefono numerį, paslaugos kategoriją ir turimą informaciją."),
       ("Įvertinama situacija","Pagal pateiktus duomenis nustatomas tinkamiausias tolesnis žingsnis."),
       ("Suderinama eiga","Darbų apimtis ir sąlygos aptariamos prieš pradedant.")]
def service_page(fn,h1,lead,price,kick,signs_title,signs,body_html,faqs,mt,md):
    sl="".join(f"<li>{s}</li>" for s in signs)
    b=titlebar(h1,lead,kick=kick,crumb=crumbs(HOME_CRUMB,("Paslaugos","Paslaugos.html"),(h1,None)),meta=price,
        chips=chips([("Skambinti",TELH,ic("i-phone")),("Rašyti",f"mailto:{MAIL}",ic("i-mail")),("Užpildyti užklausą","Užklausos forma.html",ic("i-arrow"))]))
    b+=f'<section><div class="wrap"><div class="prose"><h2>{signs_title}</h2><ul>{sl}</ul>{body_html}</div></div></section>'
    b+=process(STEPS,kick="Kaip dirbame",title="Trys paprasti žingsniai")
    b+=faq(faqs,title="Dažni klausimai",kick="DUK")
    b+=cta("Pateikite paslaugos užklausą","Nurodykite kontaktą ir pasirinkite poreikio kategoriją. Papildomą informaciją galėsite pateikti iškart arba vėliau.",
        [btn("Užsakyti servisą","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
    page(fn,mt,md,b,"paslaugos")

service_page("Paslauga - Kondicionierių remontas.html","Kondicionierių remontas",
  "Nešaldo, nešildo, teka, triukšmauja ar skleidžia kvapą? Šie požymiai padeda aprašyti situaciją ir pasirinkti tinkamą diagnostikos kryptį.",
  "Pirmas žingsnis — situacijos įvertinimas","Paslauga · Priežiūra ir remontas","Kada verta kreiptis",
  ["Kondicionierius nešaldo arba nešildo taip, kaip anksčiau","Iš vidinio bloko laša arba teka vanduo","Atsirado triukšmas, vibracija ar nemalonus kvapas","Rodomas klaidos kodas ar mirksi indikatoriai"],
  '''<h2>Ką verta pateikti diagnostikai</h2><p>Nurodykite kondicionieriaus tipą, modelį, rodomą klaidą ir pastebėtus simptomus. Ši informacija padeda tiksliau įvertinti galimą tolesnį veiksmą.</p>
  <!-- REIKIA_PATVIRTINIMO: aptarnaujami gamintojai ir garantijų politika -->
  <div class="note"><strong>Svarbu:</strong> reguliari filtrų ir vidinio bloko priežiūra padeda išvengti dalies gedimų. Žr. <a href="Paslauga - Profilaktinė priežiūra.html">profilaktinę priežiūrą</a>.</div>''',
  [("Kokią informaciją pateikti?","Įrangos tipą, modelį, klaidos kodą ir trumpą simptomų aprašymą."),
   ("Ar galima pridėti nuotraukų?","Papildomą informaciją ir nuotraukas galima pateikti suderinus kontaktą."),
   ("Nuo ko pradedama?","Nuo situacijos aprašymo ir tinkamo diagnostikos žingsnio parinkimo.")],
  "Kondicionierių remontas — Kraulis","Kondicionierių remonto paslaugos informacija: dažniausi požymiai, diagnostikos eiga ir užklausos pateikimas.")

service_page("Paslauga - Šilumos siurblių remontas.html","Šilumos siurblių remontas",
  "Remontuojame šilumos siurblius: oras–oras ir oras–vanduo. Kad šiluma nedingtų tada, kai jos labiausiai reikia.",
  "Pirmas žingsnis — situacijos įvertinimas","Paslauga · Priežiūra ir remontas","Kada verta kreiptis",
  ["Sistema nebešildo arba šildo silpnai","Smarkiai išaugo elektros sąnaudos","Lauko blokas apledija ir neatsileidžia","Rodomi klaidų kodai arba sistema stabdosi"],
  '''<h2>Ką apima remontas</h2><p>Nustatome priežastį, suderiname darbų apimtį bei kainą, pašaliname gedimą ir patikriname sistemą po remonto. Dirbame su <strong>oras–oras ir oras–vanduo</strong> šilumos siurbliais.</p>
  <div class="note"><strong>Naudinga informacija:</strong> užklausoje nurodykite, ar sistema yra oras–oras, ar oras–vanduo, ir pateikite rodomą klaidos kodą.</div><!-- REIKIA_PATVIRTINIMO: gamintojai ir garantijų politika -->''',
  [("Kokią informaciją pateikti?","Nurodykite sistemos tipą, modelį, klaidos kodą ir pastebėtus simptomus."),
   ("Ar galite padėti su sudėtinga sistema?","Taip. Į sudėtingas situacijas žiūrime kaip į galimybę rasti praktišką sprendimą."),
   ("Nuo ko pradedama?","Nuo pateiktos informacijos įvertinimo ir tolesnio diagnostikos žingsnio parinkimo.")],
  "Šilumos siurblių remontas — Kraulis","Šilumos siurblių remonto paslaugos informacija: oras–oras ir oras–vanduo sistemų požymiai bei užklausos eiga.")

service_page("Paslauga - Rekuperatorių remontas.html","Rekuperatorių remontas",
  "Triukšmas, drėgmė, silpna trauka ar klaidos pranešimai — diagnozuojame ir remontuojame rekuperatorius bei vėdinimo sistemas, kad oras namuose vėl būtų šviežias.",
  "Pirmas žingsnis — situacijos įvertinimas","Paslauga · Priežiūra ir remontas","Kada verta kreiptis",
  ["Sumažėjo oro trauka arba vėdinimas jaučiasi silpnas","Padidėjo drėgmė, rasoja langai","Girdimas triukšmas ar vibracija iš įrenginio","Rodomi klaidos pranešimai arba užsiteršę filtrai"],
  '''<h2>Ką apima remontas</h2><p>Diagnozuojame rekuperatoriaus ir vėdinimo sistemos gedimą, pašaliname priežastį ir patikriname veikimą. Dažnai problemą lemia užsiteršę filtrai, ventiliatoriaus ar automatikos gedimas.</p>
  <div class="note">Jei sutrikęs oro pasiskirstymas, peržiūrėkite <a href="Paslauga - Rekuperatorių balansavimas.html">oro srautų balansavimo</a> paslaugos kryptį.</div>''',
  [("Kuo skiriasi remontas nuo balansavimo?","Remontas šalina gedimą; balansavimas — oro srautų išmatavimas ir sureguliavimas kiekvienoje patalpoje."),
   ("Kokią informaciją pateikti?","Nurodykite rekuperatoriaus modelį, klaidos kodą ir pastebėtus simptomus."),
   ("Kaip dažnai reikia keisti filtrus?","Priklauso nuo modelio ir aplinkos; tikslų intervalą pasakome apžiūros metu.")],
  "Rekuperatorių remontas — Kraulis","Rekuperatorių ir vėdinimo sistemų remonto informacija: triukšmas, drėgmė, silpna trauka ir klaidų požymiai.")

service_page("Paslauga - Rekuperatorių balansavimas.html","Rekuperatorių balansavimas",
  "Oro srautų matavimo ir reguliavimo paslaugos apžvalga: kada ji aktuali, kokios informacijos reikia ir kaip gali atrodyti darbų eiga.",
  "Pirmas žingsnis — situacijos įvertinimas","Paslauga · Priežiūra ir remontas","Kada verta vertinti srautus",
  ["Vienose patalpose per stipri trauka, kitose — beveik nėra","Naujai sumontuota sistema dar nebuvo subalansuota","Jaučiamas triukšmas dėl per didelių srautų","Norite dokumentuoto įrodymo, kad sistema veikia kaip suprojektuota"],
  '''<h2>Kaip vertinami oro srautai</h2><p>Balansavimo metu oro srautai matuojami difuzoriuose ir grotelėse, lyginami su turimomis projektinėmis reikšmėmis ir pagal jas reguliuojami.</p>
  <div class="note"><strong>Prieš užklausą:</strong> jei turite vėdinimo projektą ar ankstesnių matavimų duomenis, nurodykite tai papildomoje informacijoje.</div><!-- REIKIA_PATVIRTINIMO: ataskaitos sudėtis ir įteikimas klientui -->
  <h2>Ką duoda subalansuota sistema</h2><ul><li>Tolygus, komfortiškas oras visose patalpose</li><li>Mažesnis triukšmas ir skersvėjų pojūtis</li><li>Efektyvesnis veikimas ir mažesnės sąnaudos</li><li>Dokumentuotas sistemos veikimo įrodymas</li></ul>''',
  [("Kas yra oro srautų balansavimas?","Sistemos oro srautų matavimas ir reguliavimas pagal turimus projektinius poreikius."),
   ("Ką verta turėti prieš užklausą?","Vėdinimo projektą, įrangos modelį ir pastebėtų problemų aprašymą, jei šią informaciją turite."),
   ("Nuo ko pradedama?","Nuo sistemos ir turimos dokumentacijos įvertinimo.")],
  "Rekuperatorių balansavimas — Kraulis","Rekuperacijos oro srautų balansavimo informacija: matavimai, reguliavimo eiga ir užklausai reikalingi duomenys.")

service_page("Paslauga - Profilaktinė priežiūra.html","Profilaktinė priežiūra",
  "Gedimo nėra — ir tegul taip lieka. Patikriname veikimą, išvalome, įvertiname susidėvėjimą ir patariame, kaip naudoti, kad įranga tarnautų ilgiau ir taupiau.",
  "Pirmas žingsnis — situacijos įvertinimas","Paslauga · Priežiūra ir remontas","Kodėl verta prižiūrėti reguliariai",
  ["Patikrinama įrangos būklė ir veikimas","Anksčiau pastebimi susidėvėjimo požymiai","Valomi priežiūros reikalaujantys elementai","Aptariami tolesni priežiūros veiksmai"],
  '''<h2>Ką apima priežiūra</h2><p>Atvykstame, patikriname veikimą, išvalome, įvertiname susidėvėjimą ir patariame, kaip naudoti įrangą, kad ji tarnautų ilgiau ir taupiau. Priežiūrą pritaikome pagal įrangos tipą.</p>
  <div class="note"><strong>Gamintojo instrukcija:</strong> konkretų priežiūros intervalą ir veiksmus verta tikrinti pagal įrangos modelio dokumentaciją.</div><!-- REIKIA_PATVIRTINIMO: garantijų politika -->''',
  [("Kaip dažnai reikia profilaktikos?","Priklauso nuo įrangos tipo ir naudojimo; tinkamą intervalą pasakome pagal jūsų įrangą."),
   ("Kokią informaciją pateikti?","Įrangos tipą, modelį ir kada paskutinį kartą buvo atlikta priežiūra, jei žinote."),
   ("Nuo ko pradedama?","Nuo įrangos ir jos naudojimo aplinkybių įvertinimo.")],
  "Profilaktinė ŠVOK priežiūra — Kraulis","Kondicionierių, šilumos siurblių ir rekuperatorių profilaktinės priežiūros informacija: patikra, valymas ir būklės įvertinimas.")

service_page("Paslauga - Įrangos montavimas.html","Įrangos montavimas",
  "Sumontuojame ir paleidžiame šilumos siurblius, kondicionierius ir rekuperatorius — nuo sistemos parinkimo iki sureguliavimo. Vienos rankos nuo pradžios iki galo.",
  "Pirmas žingsnis — poreikio įvertinimas","Paslauga","Ką apima montavimo procesas",
  ["Poreikio ir patalpų informacijos surinkimas","Montavimo ir prijungimo darbų kryptis","Paleidimo ir sureguliavimo etapas","Naudojimo informacijos perdavimas"],
  '''<h2>Kokią įrangą montuojame</h2><ul><li>Šilumos siurbliai — oras–oras ir oras–vanduo</li><li>Kondicionieriai — sieniniai (split), multi-split, kanaliniai</li><li>Rekuperatoriai ir vėdinimo sistemos</li></ul>
  <p>Konkreti įranga, montavimo galimybės ir darbų apimtis vertinamos pagal patalpas, esamą sistemą ir pasirinktą sprendimą.</p>
  <div class="note"><strong>Prieš užklausą:</strong> jei turite patalpų planą, įrangos modelį ar projekto informaciją, nurodykite tai papildomame lauke.</div><!-- REIKIA_PATVIRTINIMO: gamintojai, sertifikatai ir garantijų politika -->''',
  [("Kokią informaciją pateikti?","Patalpų tipą, turimą projektą ar planą ir dominančios įrangos tipą, jei jau žinote."),
   ("Kas aptariama prieš montavimą?","Sistemos tipas, montavimo vieta, darbų apimtis ir reikalingas pasirengimas."),
   ("Nuo ko pradedama?","Nuo poreikio ir turimos techninės informacijos įvertinimo.")],
  "Įrangos montavimas — Kraulis","Šilumos siurblių, kondicionierių ir rekuperatorių montavimo proceso informacija: parinkimas, montavimas, paleidimas ir sureguliavimas.")

print("service pages done")
