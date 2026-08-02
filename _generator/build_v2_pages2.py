# -*- coding: utf-8 -*-
import os
from build_v2 import page, TEL, TELH, MAIL
from build_v2_content import ic, crumbs, titlebar, chips, cta, btn, faq
H=("Pradžia","index.html")

# ============================ KONTAKTAI
kont=titlebar("Susisiekime","Turite klausimą apie įrangą, montavimą ar servisą? Skambinkite arba rašykite — patarsime, net jei dar tik renkatės.",
    kick="Kontaktai",crumb=crumbs(H,("Kontaktai",None)))
kont+=f'''<section><div class="wrap"><div class="cards">
  <a class="card" href="{TELH}"><span class="cardic">{ic("i-phone")}</span><h3>Telefonas</h3><p class="price" style="font-size:16px">{TEL}</p><p>Skambinkite bendruoju numeriu.</p></a>
  <a class="card" href="mailto:{MAIL}"><span class="cardic">{ic("i-mail")}</span><h3>El. paštas</h3><p class="price" style="font-size:15px">{MAIL}</p><p>Bendras svetainės kontaktas.</p></a>
</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="layout">
  <div class="prose"><h2>Kaip pradėti?</h2>
    <p>Trumpai aprašykite įrangą, pastebėtą problemą arba planuojamą sprendimą. Jei nežinote techninių detalių, pakanka telefono numerio ir poreikio kategorijos.</p>
    <div class="note">Aptarnavimo teritorija, darbo laikas ir atsakymo terminai bus paskelbti tik patvirtinus galutinę informaciją.</div>
    <!-- REIKIA_PATVIRTINIMO: teritorija, darbo laikas, SLA ir juridiniai rekvizitai -->
    {chips([("Skambinti",TELH,ic("i-phone")),("Rašyti el. paštu",f"mailto:{MAIL}",ic("i-mail")),("Užpildyti užklausą","Užklausos forma.html",ic("i-arrow"))])}
  </div>
</div></div></section>'''
kont+=cta("Susisiekite dėl serviso arba konsultacijos","Aprašykite situaciją ir įrangą arba paskambinkite bendruoju numeriu.",
    [btn("Užpildyti užklausą","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page("Kontaktai.html","Kontaktai — Kraulis | +370 610 24999",f"Susisiekite su Kraulis telefonu {TEL} arba el. paštu {MAIL}. Taip pat galite peržiūrėti demonstracinę užklausos formą.",kont,"kontaktai")

# ============================ UŽKLAUSOS FORMA
FORMJS='''<script>
document.addEventListener('DOMContentLoaded',function(){var f=document.getElementById('uzklausa');if(!f)return;
var status=document.getElementById('formstatus');
function clearErrors(){Array.prototype.forEach.call(f.querySelectorAll('.field.err'),function(el){el.classList.remove('err');});
Array.prototype.forEach.call(f.querySelectorAll('[aria-invalid]'),function(el){el.removeAttribute('aria-invalid');});}
function showErrors(){Array.prototype.forEach.call(f.elements,function(el){if(el.willValidate&&!el.checkValidity()){var fld=el.closest&&el.closest('.field');if(fld)fld.classList.add('err');el.setAttribute('aria-invalid','true');}});}
f.addEventListener('submit',function(e){e.preventDefault();clearErrors();
if(!f.checkValidity()){showErrors();var inv=f.querySelector(':invalid');if(inv)inv.focus();
status.className='form-status err';status.textContent='Patikrinkite pažymėtus laukus — reikia telefono numerio, paslaugos kategorijos ir sutikimo.';return;}
status.className='form-status demo';
status.textContent='Ačiū! Tai demonstracinė forma — užklausa dar nesiunčiama. Susisiekite telefonu arba el. paštu.';
if(status.focus)status.focus();});
f.addEventListener('input',function(e){var el=e.target,fld=el.closest&&el.closest('.field.err');if(fld&&el.checkValidity()){fld.classList.remove('err');el.removeAttribute('aria-invalid');}});
f.addEventListener('change',function(e){var el=e.target,fld=el.closest&&el.closest('.field.err');if(fld&&el.checkValidity()){fld.classList.remove('err');el.removeAttribute('aria-invalid');}});
});
</script>'''
uzk=titlebar("Serviso arba konsultacijos užklausos demonstracija","Pasirinkite poreikio kategoriją ir peržiūrėkite būsimos formos veikimą. Ši versija duomenų dar nesiunčia.",
    kick="Užklausa",crumb=crumbs(H,("Užklausa",None)))
uzk+=f'''<section><div class="wrap"><div class="layout aside">
  <form class="form" id="uzklausa" novalidate>
    <p class="demo-badge" role="note">{ic("i-mail")} Demonstracinė versija — <strong>užklausos pateikimas dar neaktyvus</strong>. Kol kas skambinkite arba rašykite tiesiogiai.</p>
    <div class="field"><label for="telefonas">Telefonas <span class="req" aria-hidden="true">*</span></label>
      <input id="telefonas" name="telefonas" type="tel" required autocomplete="tel" inputmode="tel" placeholder="+370 6…" aria-describedby="telefonas-err">
      <span class="err-msg" id="telefonas-err">{ic("i-phone")} Įveskite telefono numerį, kad būtų galima susisiekti.</span></div>
    <div class="field"><label for="paslauga">Paslaugos / poreikio kategorija <span class="req" aria-hidden="true">*</span></label>
      <select id="paslauga" name="paslauga" required aria-describedby="paslauga-err"><option value="">Pasirinkite…</option><option>Konsultacija ir įrangos parinkimas</option><option>Įrangos montavimas</option><option>Profilaktinė priežiūra</option><option>Gedimo remontas</option><option>Rekuperatorių balansavimas</option><option>Kita</option></select>
      <span class="err-msg" id="paslauga-err">{ic("i-arrow")} Pasirinkite geriausiai tinkamą poreikio kategoriją.</span></div>
    <div class="grid2">
      <div class="field"><label for="iranga">Įrangos tipas</label><select id="iranga" name="iranga"><option value="">Pasirinkite…</option><option>Kondicionierius</option><option>Šilumos siurblys</option><option>Rekuperatorius / vėdinimas</option><option>Dar nežinau</option></select></div>
    </div>
    <fieldset class="opt"><legend>Papildoma informacija (nebūtina)</legend>
      <div class="grid2">
        <div class="field"><label for="vardas">Vardas</label><input id="vardas" name="vardas" type="text" autocomplete="name" placeholder="Jūsų vardas"></div>
        <div class="field"><label for="elpastas">El. paštas</label><input id="elpastas" name="elpastas" type="email" autocomplete="email" placeholder="vardas@paštas.lt"></div>
      </div>
      <div class="field"><label for="zinute">Žinutė</label><textarea id="zinute" name="zinute" placeholder="Trumpai aprašykite įrangą, gamintoją/modelį (jei žinote) ir problemą arba poreikį."></textarea><span class="hint">Papildoma informacija padės greičiau suprasti situaciją.</span></div>
    </fieldset>
    <label class="consent"><input type="checkbox" id="consent" required> Sutinku, kad mano pateikti duomenys būtų naudojami atsakymui į šią užklausą pateikti. <span class="req" aria-hidden="true">*</span></label>
    <div style="margin-top:18px"><button class="btn btn-primary" type="submit">Peržiūrėti demo būseną</button>
      <p class="hint" style="margin-top:10px">Prototipe pateikimas neaktyvus. Rašykite <a href="mailto:{MAIL}">{MAIL}</a> arba skambinkite <a href="{TELH}">{TEL}</a>.</p></div>
    <p class="form-status" id="formstatus" role="status" aria-live="polite" tabindex="-1"></p>
    <noscript><p class="note">Formos demonstracijai reikalingas JavaScript. Rašykite <a href="mailto:{MAIL}">{MAIL}</a> arba skambinkite <a href="{TELH}">{TEL}</a>.</p></noscript>
  </form>
  <aside class="side"><div class="card" style="cursor:default"><span class="cardic">{ic("i-phone")}</span><h3>Susisiekite telefonu</h3><p>Kol demonstracinė forma neaktyvi, skambinkite bendruoju numeriu.</p>
    <p class="mono" style="font-size:15px"><a href="{TELH}" style="text-decoration:none">{TEL}</a></p><p class="mono" style="font-size:13px"><a href="mailto:{MAIL}" style="text-decoration:none">{MAIL}</a></p>
    <!-- REIKIA_PATVIRTINIMO: darbo laikas ir aptarnavimo teritorija --></div></aside>
</div></div></section>'''
page("Užklausos forma.html","Užklausa — Kraulis | Užsakyti servisą ar konsultaciją","Užsakykite Kraulis ŠVOK servisą ar konsultaciją: užpildykite užklausą arba skambinkite +370 610 24999.",uzk,"kontaktai",extra_head=FORMJS)

# ============================ PATARIMAI
pat=titlebar("Patarimai ir gidai","Paaiškiname, kaip veikia sistemos ir ką verta žinoti renkantis — be žargono. Renkatės pirmą kartą ar tik įsigilinate — pradėkite čia.",
    kick="Patarimai",crumb=crumbs(H,("Patarimai",None)))
def gcard(h,p,href):
    return f'<a class="card" href="{href}"><span class="cardic">{ic("i-airflow")}</span><h3>{h}</h3><p>{p}</p><span class="more">Skaityti →</span></a>'
pat+=f'''<section><div class="wrap"><div class="cards">
  {gcard("Kaip išsirinkti rekuperatorių","Kas yra rekuperacija, kokio našumo reikia, centrinė ar decentralizuota sistema, filtrai ir montavimas.","Patarimas - Kaip išsirinkti rekuperatorių.html")}
  {gcard("Kaip išsirinkti kondicionierių ar šilumos siurblį","Galios parinkimas, oras–oras ir oras–vanduo, SEER/SCOP, veikimas šaltyje, triukšmas ir valdymas.","Patarimas - Kaip išsirinkti kondicionierių ar šilumos siurblį.html")}
  {gcard("Dažni klausimai (DUK)","Kaip pasirinkti užklausos kategoriją, kokią informaciją pateikti ir kaip susisiekti.","DUK.html")}
</div></div></section>'''
pat+=cta("Liko klausimų dėl pasirinkimo?","Pasitarkite su mumis — padėsime parinkti sprendimą pagal patalpas ir biudžetą.",
    [btn("Užsakyti konsultaciją","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page("Patarimai.html","Patarimai ir gidai — Kraulis | Kaip išsirinkti ŠVOK įrangą","Kraulis patarimai: kaip išsirinkti rekuperatorių, kondicionierių ar šilumos siurblį, dažni klausimai. Aiškiai ir be žargono.",pat,"patarimai")

# ---- Gidas 1
g1=titlebar("Kaip išsirinkti rekuperatorių","Rekuperacinis vėdinimas tiekia šviežią orą ir šalina panaudotą, o šilumokaityje atgauna didelę dalį šilumos. Į ką verta atsižvelgti renkantis.",
    kick="Patarimai · Gidas",crumb=crumbs(H,("Patarimai","Patarimai.html"),("Kaip išsirinkti rekuperatorių",None)))
g1+='''<section><div class="wrap"><div class="prose">
  <h2>Kas yra rekuperacija ir kam jos reikia</h2><p>Rekuperatorius pastoviai tiekia šviežią orą ir šalina panaudotą, o šilumokaityje ištraukiamo oro šiluma pašildo įtraukiamą. Taip gaunamas šviežias oras be didelių šilumos nuostolių, mažiau drėgmės ir kvapų.</p>
  <h2>1. Reikiamas oro našumas</h2><p>Svarbiausias parametras — kiek oro (m³/h) įrenginys paduoda. Poreikis priklauso nuo patalpų ploto, aukščio, žmonių skaičiaus ir paskirties. Tikslų poreikį geriausia įvertinti pagal projektą arba konsultuojantis.</p>
  <h2>2. Centrinė ar decentralizuota sistema</h2><ul><li><strong>Centrinis rekuperatorius su ortakiais</strong> — vienas įrenginys aptarnauja visą būstą; tolygiausias vėdinimas.</li><li><strong>Decentralizuoti (sieniniai) rekuperatoriai</strong> — be ortakių, paprasčiau įrengti esamame būste.</li></ul>
  <h2>3. Šilumokaičio tipas ir filtrai</h2><p>Nuo šilumokaičio priklauso, kiek šilumos atgaunama ir ar perduodama drėgmė. Filtrai apsaugo įrenginį ir orą — svarbu, kad juos būtų patogu keisti.</p>
  <h2>4. Garsas ir montavimo vieta</h2><p>Įrenginį verta montuoti techninėje patalpoje. Gerai suprojektuota ir <a href="Paslauga - Rekuperatorių balansavimas.html">subalansuota</a> sistema veikia tyliai ir tolygiai.</p>
  <div class="note"><strong>Svarbu:</strong> sistemos veikimas priklauso ir nuo tinkamo oro srautų sureguliavimo. Konkreti darbų bei matavimų apimtis derinama individualiai.</div>
</div></div></section>'''
g1+=cta("Renkatės rekuperatorių?","Padėsime parinkti našumą ir sistemą pagal jūsų patalpas — ir sumontuoti bei subalansuoti.",
    [btn("Užsakyti konsultaciją","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page("Patarimas - Kaip išsirinkti rekuperatorių.html","Kaip išsirinkti rekuperatorių — Kraulis gidas","Kaip išsirinkti rekuperatorių: oro našumas, centrinė ar decentralizuota sistema, šilumokaitis, filtrai, garsas ir montavimas.",g1,"patarimai")

# ---- Gidas 2
g2=titlebar("Kaip išsirinkti kondicionierių ar šilumos siurblį","Oras–oras kondicionierius ir šilumos siurblys vėsina vasarą ir šildo žiemą. Svarbiausia — teisingai parinkti galią ir tipą pagal patalpas ir Lietuvos klimatą.",
    kick="Patarimai · Gidas",crumb=crumbs(H,("Patarimai","Patarimai.html"),("Kaip išsirinkti kondicionierių ar šilumos siurblį",None)))
g2+='''<section><div class="wrap"><div class="prose">
  <h2>1. Galios parinkimas</h2><p>Per maža galia neužtikrins komforto, per didelė — brangesnė ir dažniau įsijungs/išsijungs. Reikiama galia priklauso nuo ploto, aukščio, langų, izoliacijos ir orientacijos. Tikslų poreikį geriausia įvertinti individualiai.</p>
  <h2>2. Sistemos tipas</h2><ul><li><strong>Oras–oras</strong> — šildo ir vėsina orą patalpoje; dažniausias sprendimas.</li><li><strong>Oras–vanduo</strong> šilumos siurblys — šildo vandens sistemą (grindinį šildymą, radiatorius) ir gali ruošti karštą vandenį.</li><li><strong>Multi-split</strong> — vienas lauko blokas aptarnauja kelis vidinius blokus.</li></ul>
  <h2>3. Efektyvumas: SEER ir SCOP</h2><p><strong>SEER</strong> rodo sezoninį vėsinimo, <strong>SCOP</strong> — šildymo efektyvumą. Kuo didesni, tuo mažesnės metinės sąnaudos. Verta žiūrėti ir į energijos klasę.</p>
  <h2>4. Veikimas šaltyje, triukšmas ir valdymas</h2><p>Lietuvos klimatui svarbu, iki kokios lauko temperatūros įrenginys efektyviai šildo. Vidinio ir lauko blokų garso lygis svarbus miegamiesiems. Daugelis modelių valdomi programėle (Wi-Fi).</p>
  <div class="note"><strong>Montavimo sąlygos:</strong> prieš pasirenkant įrangą verta patikrinti gamintojo dokumentaciją ir montavimo reikalavimus konkrečiam modeliui.</div>
  <!-- REIKIA_PATVIRTINIMO: sertifikatai ir garantijos sąlygos -->
</div></div></section>'''
g2+=cta("Nežinote, kokios galios reikia?","Parinksime kondicionierių ar šilumos siurblį pagal jūsų patalpas ir biudžetą.",
    [btn("Užsakyti konsultaciją","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page("Patarimas - Kaip išsirinkti kondicionierių ar šilumos siurblį.html","Kaip išsirinkti kondicionierių ar šilumos siurblį — Kraulis gidas","Kaip išsirinkti kondicionierių ar šilumos siurblį: galia, oras–oras ir oras–vanduo, SEER/SCOP, veikimas šaltyje, triukšmas.",g2,"patarimai")

# ============================ DUK
duk=titlebar("Dažni klausimai","Trumpi atsakymai apie demonstracinę užklausos formą, poreikio kategorijas ir susisiekimą.",
    kick="DUK",crumb=crumbs(H,("DUK",None)))
duk+=faq([
  ("Kokią informaciją pateikti užklausoje?","Pakanka telefono numerio ir poreikio kategorijos. Įrangos tipą, modelį bei situacijos aprašymą galima pridėti kaip neprivalomą informaciją."),
  ("Ar demonstracinė forma išsiunčia užklausą?","Ne. Ši prototipo forma tik parodo laukus ir jų būsenas. Kol pateikimas neaktyvus, susisiekite telefonu arba el. paštu."),
  ("Kaip pasirinkti poreikio kategoriją?","Pasirinkite artimiausią variantą: konsultaciją, montavimą, priežiūrą, remontą, balansavimą arba „Kita“. Tikslų poreikį galima patikslinti pokalbio metu."),
  ("Ką rašyti, jei nežinau įrangos modelio?","Modelis nėra privalomas. Trumpai aprašykite, ko reikia arba ką pastebėjote, o technines detales galėsite pateikti vėliau."),
  ("Kaip susisiekti, kol forma neaktyvi?",f"Skambinkite {TEL} arba rašykite {MAIL}. Kontaktų puslapyje pateiktos tiesioginės nuorodos."),
  ("Kur rasti paslaugų aprašymus?","Paslaugų puslapyje pateiktos montavimo, priežiūros, remonto ir balansavimo kryptys. Galite pasirinkti artimiausią pagal savo situaciją."),
],title="Klausimai ir atsakymai",kick="DUK")
duk+='''<!-- REIKIA_PATVIRTINIMO: kainos, teritorija, SLA, garantijos ir gamintojų sąrašas -->'''
duk+=cta("Neradote atsakymo?","Paskambinkite arba parašykite — atsakysime ir patarsime.",
    [btn("Užpildyti užklausą","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page("DUK.html","Dažni klausimai (DUK) — Kraulis | Užklausa ir kontaktai","Dažni klausimai apie Kraulis svetainės demonstracinę užklausos formą, poreikio kategorijas ir susisiekimą.",duk,"patarimai")

# ============================ APIE MUS
apie=titlebar("ŠVOK sprendimai vienoje aiškioje svetainėje","Šiame prototipe pristatomos įrangos parinkimo, montavimo, priežiūros, remonto ir vėdinimo sistemų balansavimo paslaugų kryptys.",
    kick="Apie mus",crumb=crumbs(H,("Apie mus",None)))
apie+=f'''<section><div class="wrap"><div class="prose">
  <p>Svetainės aprašomoji dalis padeda pasirinkti poreikio kryptį ir pereiti į kontaktą. E. parduotuvė numatyta kaip gretima tos pačios svetainės dalis, tačiau šiame prototipe ji dar neaktyvi.</p>
  <p><strong>Nežinote, nuo ko pradėti?</strong> Pasirinkite artimiausią paslaugos kategoriją arba susisiekite bendruoju telefonu ir el. paštu.</p>
  <h2>Ką darome</h2></div>
  <div class="cards" style="margin-top:20px">
    <span class="card disabled-link" aria-disabled="true"><span class="cardic">{ic("i-shop")}</span><h3>Elektroninė parduotuvė <small>netrukus</small></h3><p>Numatyta kaip gretima svetainės dalis. Galutinė nuoroda dar derinama.</p></span>
    <a class="card" href="Paslauga - Įrangos montavimas.html"><span class="cardic">{ic("i-montavimas")}</span><h3>Įrangos montavimas</h3><p>Sistemos parinkimo, montavimo, paleidimo ir sureguliavimo kryptis.</p></a>
    <a class="card" href="Paslaugos.html"><span class="cardic">{ic("i-remontas")}</span><h3>Priežiūra ir remontas</h3><p>Periodinė profilaktika, gedimų diagnostika ir remonto darbai. Namams ir verslui.</p></a>
    <a class="card" href="Paslauga - Rekuperatorių balansavimas.html"><span class="cardic">{ic("i-balans")}</span><h3>Rekuperacijos balansavimas</h3><p>Oro srautų matavimo ir sureguliavimo paslaugos kryptis.</p></a>
  </div>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="prose">
  <h2>Aiškus kelias pagal poreikį</h2><p>Paslaugų aprašymuose atskiriamos montavimo, priežiūros, remonto ir balansavimo kryptys. Užklausos demonstracijoje galima pasirinkti artimiausią kategoriją.</p>
  <!-- REIKIA_PATVIRTINIMO: gamintojai, sertifikatai, garantijos, teritorija, patirtis ir pozicionavimo pažadai -->
</div></div></section>'''
apie+=cta("Pasitarkime dėl jūsų sistemos","Renkatės naują įrangą ar reikia pagalbos su turima — parašykite arba paskambinkite.",
    [btn("Užsakyti servisą","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page("Apie mus.html","Apie svetainės paslaugų kryptis — Kraulis","Kraulis svetainės prototipe pristatomos įrangos parinkimo, montavimo, priežiūros, remonto ir balansavimo paslaugų kryptys.",apie,"apie")

from build_v2 import OUT as _OUT
print("ALL pages done. Files:", len([f for f in os.listdir(_OUT) if f.endswith('.html')]))
