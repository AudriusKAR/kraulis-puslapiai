# -*- coding: utf-8 -*-
import os
from build_v2 import page, TEL, TELH, MAIL
from build_v2_content import ic, crumbs, titlebar, chips, cta, btn, faq
H=("Pradžia","index.html")

# ============================ KONTAKTAI
kont=titlebar("Susisiekime","Turite klausimą apie įrangą, montavimą ar servisą? Skambinkite arba rašykite — patarsime, net jei dar tik renkatės.",
    kick="Kontaktai",crumb=crumbs(H,("Kontaktai",None)))
kont+=f'''<section><div class="wrap"><div class="cards">
  <a class="card" href="{TELH}"><span class="cardic">{ic("i-phone")}</span><h3>Telefonas</h3><p class="price" style="font-size:16px">{TEL}</p><p>Dažnai padedame jau telefonu.</p></a>
  <a class="card" href="mailto:{MAIL}"><span class="cardic">{ic("i-mail")}</span><h3>El. paštas</h3><p class="price" style="font-size:15px">{MAIL}</p><p>Bendras svetainės kontaktas.</p></a>
  <div class="card" style="cursor:default"><span class="cardic">{ic("i-prieziura")}</span><h3>Darbo laikas</h3><p class="mono" style="color:var(--navy)">I–V 8.00–17.00</p><p>Servisas — Vilnius ir apylinkės.</p></div>
</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="layout aside">
  <div class="prose"><h2>Kur dirbame?</h2>
    <p>Montavimo, priežiūros ir remonto paslaugas teikiame <strong>Vilniuje ir apylinkėse</strong>. E-parduotuvės prekes pristatome <strong>visoje Lietuvoje</strong>.</p>
    <p>Sugedo įranga ar tiesiog negaunate reikiamos pagalbos? Skambinkite — dažnai padedame jau telefonu, o jei reikia, atvykstame diagnostikai.</p>
    <div class="note">Į užklausas paprastai atsakome per 1–2 darbo dienas. Skubūs darbai derinami individualiai.</div>
    {chips([("Skambinti",TELH,ic("i-phone")),("Rašyti el. paštu",f"mailto:{MAIL}",ic("i-mail")),("Užpildyti užklausą","Užklausos forma.html",ic("i-arrow"))])}
  </div>
  <aside class="side"><div class="card" style="cursor:default"><h3>Rekvizitai</h3>
    <p style="font-size:14px;line-height:1.7;color:var(--steel)">Kraulis, MB<br>Įmonės kodas: 307605802<br>Reg. adresas: Naugarduko g. 68-3, 03203 Vilnius<br>Korespondencijai: Žirnių g. 6, 02120 Vilnius<br>Bankas: „Swedbank“<br><span class="mono" style="font-size:13px">LT22 7300 0102 0138 5725</span></p>
  </div></aside>
</div></div></section>'''
kont+=cta("Užsakykite servisą arba konsultaciją","Aprašykite situaciją ir įrangą — grįšime su aiškiu tolesniu žingsniu.",
    [btn("Užpildyti užklausą","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page("Kontaktai.html","Kontaktai — Kraulis | +370 610 24999","Susisiekite su Kraulis: telefonas +370 610 24999, el. paštas info@kraulis.lt. Servisas Vilniuje ir apylinkėse, prekės — visoje Lietuvoje.",kont,"kontaktai")

# ============================ UŽKLAUSOS FORMA
FORMJS='''<script>
(function(){var f=document.getElementById('uzklausa');if(!f)return;
f.addEventListener('submit',function(e){e.preventDefault();
if(!f.checkValidity()){f.reportValidity();var inv=f.querySelector(':invalid');if(inv)inv.focus();return;}
var g=function(n){var el=f.elements[n];return el?el.value.trim():''};
var subj='Užklausa iš svetainės: '+(g('paslauga')||'ŠVOK')+(g('iranga')?(' · '+g('iranga')):'');
var body=['Vardas: '+g('vardas'),'Telefonas: '+g('telefonas'),'El. paštas: '+g('elpastas'),'Paslauga: '+g('paslauga'),'Įrangos tipas: '+g('iranga'),'','Žinutė:',g('zinute')].join('\\n');
document.getElementById('formstatus').textContent='Atidaroma jūsų el. pašto programa su paruoštu laišku… Jei ji neatsivėrė, parašykite info@kraulis.lt arba paskambinkite +370 610 24999.';
window.location.href='mailto:info@kraulis.lt?subject='+encodeURIComponent(subj)+'&body='+encodeURIComponent(body);});})();
</script>'''
uzk=titlebar("Užsakyti servisą arba konsultaciją","Aprašykite įrangą ir situaciją — grįšime su aiškiu tolesniu žingsniu ir kaina.",
    kick="Užklausa",crumb=crumbs(H,("Užklausa",None)))
uzk+=f'''<section><div class="wrap"><div class="layout aside">
  <form class="form" id="uzklausa" novalidate>
    <div class="grid2">
      <div class="field"><label for="vardas">Vardas <span class="req">*</span></label><input id="vardas" name="vardas" type="text" required autocomplete="name" placeholder="Jūsų vardas"></div>
      <div class="field"><label for="telefonas">Telefonas <span class="req">*</span></label><input id="telefonas" name="telefonas" type="tel" required autocomplete="tel" placeholder="+370 6…"></div>
    </div>
    <div class="field"><label for="elpastas">El. paštas</label><input id="elpastas" name="elpastas" type="email" autocomplete="email" placeholder="vardas@paštas.lt"></div>
    <div class="grid2">
      <div class="field"><label for="paslauga">Paslauga</label><select id="paslauga" name="paslauga"><option value="">Pasirinkite…</option><option>Konsultacija ir įrangos parinkimas</option><option>Įrangos montavimas</option><option>Profilaktinė priežiūra</option><option>Gedimo remontas</option><option>Rekuperatorių balansavimas</option><option>Kita</option></select></div>
      <div class="field"><label for="iranga">Įrangos tipas</label><select id="iranga" name="iranga"><option value="">Pasirinkite…</option><option>Kondicionierius</option><option>Šilumos siurblys</option><option>Rekuperatorius / vėdinimas</option><option>Dar nežinau</option></select></div>
    </div>
    <div class="field"><label for="zinute">Žinutė <span class="req">*</span></label><textarea id="zinute" name="zinute" required placeholder="Trumpai aprašykite įrangą, gamintoją/modelį (jei žinote) ir problemą arba poreikį."></textarea><span class="hint">Kuo tiksliau aprašysite, tuo greičiau padėsime.</span></div>
    <label class="consent"><input type="checkbox" required> Sutinku, kad mano pateikti duomenys būtų naudojami atsakymui į šią užklausą pateikti.</label>
    <div style="margin-top:18px"><button class="btn btn-primary" type="submit">Paruošti el. laišką</button>
      <p class="hint" style="margin-top:10px">Paspaudus atsidarys <strong>jūsų el. pašto programa</strong> su paruoštu laišku. Nepatogu? Rašykite <a href="mailto:{MAIL}">{MAIL}</a> arba skambinkite <a href="{TELH}">{TEL}</a>.</p></div>
    <p class="form-status" id="formstatus" role="status" aria-live="polite"></p>
    <noscript><p class="note">Formos siuntimui reikalingas JavaScript. Parašykite <a href="mailto:{MAIL}">{MAIL}</a> arba skambinkite <a href="{TELH}">{TEL}</a>.</p></noscript>
  </form>
  <aside class="side"><div class="card" style="cursor:default"><span class="cardic">{ic("i-phone")}</span><h3>Greičiau — telefonu</h3><p>Aiškų gedimą dažnai įkainojame ar patariame jau telefonu.</p>
    <p class="mono" style="font-size:15px"><a href="{TELH}" style="text-decoration:none">{TEL}</a></p><p class="mono" style="font-size:13px"><a href="mailto:{MAIL}" style="text-decoration:none">{MAIL}</a></p>
    <p style="font-size:13.5px;color:var(--steel)">I–V 8.00–17.00 · Vilnius ir apylinkės</p></div></aside>
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
  {gcard("Dažni klausimai (DUK)","Kainos, aptarnaujama teritorija, garantijos, kaip užsakyti servisą ir kt.","DUK.html")}
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
  <div class="note"><strong>Svarbu:</strong> net geras rekuperatorius veiks prastai, jei srautai nesubalansuoti. Po montavimo sistemą reikėtų subalansuoti — pateikiame matavimų ataskaitą „prieš/po“.</div>
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
  <div class="note"><strong>Sertifikuotas montavimas:</strong> daliai įrangos gamintojo garantija pailgėja, kai ją sumontuoja sertifikuoti montuotojai.</div>
</div></div></section>'''
g2+=cta("Nežinote, kokios galios reikia?","Parinksime kondicionierių ar šilumos siurblį pagal jūsų patalpas ir biudžetą.",
    [btn("Užsakyti konsultaciją","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page("Patarimas - Kaip išsirinkti kondicionierių ar šilumos siurblį.html","Kaip išsirinkti kondicionierių ar šilumos siurblį — Kraulis gidas","Kaip išsirinkti kondicionierių ar šilumos siurblį: galia, oras–oras ir oras–vanduo, SEER/SCOP, veikimas šaltyje, triukšmas.",g2,"patarimai")

# ============================ DUK
duk=titlebar("Dažni klausimai","Trumpi atsakymai į dažniausius klausimus apie Kraulis paslaugas, kainas ir aptarnaujamą teritoriją.",
    kick="DUK",crumb=crumbs(H,("DUK",None)))
duk+=faq([
  ("Ar aptarnaujate ne pas jus pirktą įrangą?","Taip. Diagnozuojame, remontuojame ir prižiūrime visų pagrindinių gamintojų kondicionierius, šilumos siurblius ir rekuperatorius — nepriklausomai nuo to, kur juos pirkote."),
  ("Kiek kainuoja diagnostika ir paslaugos?",["Gedimo diagnostika — nuo 69 €. Profilaktinė priežiūra — nuo 99 €. Rekuperacijos balansavimas — nuo 149 €.","Kainos skelbiamos „nuo“; tikslią kainą suderiname prieš pradedant darbus."]),
  ("Kur teikiate paslaugas?","Montavimo, priežiūros ir remonto paslaugas teikiame Vilniuje ir apylinkėse. E-parduotuvės prekes pristatome visoje Lietuvoje."),
  ("Per kiek laiko atsakote į užklausą?","Į užklausas paprastai atsakome per 1–2 darbo dienas. Skubūs darbai derinami individualiai."),
  ("Kokia garantija?",["Įrangai galioja gamintojo garantija (trukmė priklauso nuo gamintojo ir modelio). Daliai įrangos ji pailgėja, kai sumontuoja sertifikuoti montuotojai.","Mūsų atliktiems montavimo, remonto ir priežiūros darbams suteikiame garantiją."]),
  ("Ar dirbate su verslu ir sudėtingomis sistemomis?","Taip. Servisą teikiame ir namams, ir verslui, įskaitant sudėtingus sprendimus."),
  ("Kaip užsakyti servisą?","Paskambinkite +370 610 24999, parašykite info@kraulis.lt arba užpildykite užklausos formą."),
  ("Su kokiais gamintojais dirbate?","Montuojame ir prižiūrime patikimų gamintojų įrangą: Mitsubishi Electric, Samsung, Midea, Zehnder, Recom, Airwell, Cooper&Hunter ir kt."),
],title="Klausimai ir atsakymai",kick="DUK")
duk+=cta("Neradote atsakymo?","Paskambinkite arba parašykite — atsakysime ir patarsime.",
    [btn("Užpildyti užklausą","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page("DUK.html","Dažni klausimai (DUK) — Kraulis | Kainos, teritorija, garantijos","Dažni klausimai apie Kraulis ŠVOK paslaugas: kainos (diagnostika nuo 69 €), aptarnaujama teritorija, garantijos, kaip užsakyti servisą.",duk,"patarimai")

# ============================ APIE MUS
apie=titlebar("Įranga, kuri veikia. Ir žmonės, kurie už ją atsako.","„Kraulis“ — šildymo, vėdinimo ir vėsinimo (ŠVOK) komanda iš Vilniaus. Parduodame įrangą, ją sumontuojame, o svarbiausia — liekame šalia ir tada, kai pardavimas jau įvykęs.",
    kick="Apie mus",crumb=crumbs(H,("Apie mus",None)))
apie+=f'''<section><div class="wrap"><div class="prose">
  <p>Mūsų požiūris paprastas: įranga tarnauja ilgai ir taupiai tada, kai ja nuolat rūpinamasi. Todėl kiekvienas mūsų parduotas įrenginys turi aiškų priežiūros kelią. Bėdoje nepaliekame.</p>
  <p><strong>Turite įrangą, bet negaunate reikiamos pagalbos?</strong> Padėsime. Nesvarbu, kokia jūsų rekuperatoriaus, kondicionieriaus ar šilumos siurblio istorija — diagnozuojame, remontuojame ir prižiūrime visų pagrindinių gamintojų įrangą.</p>
  <h2>Ką darome</h2></div>
  <div class="cards" style="margin-top:20px">
    <a class="card" href="#" data-todo="eshop-visa"><!-- TODO: e-parduotuvė --><span class="cardic">{ic("i-shop")}</span><h3>Elektroninė parduotuvė</h3><p>Rekuperatoriai, kondicionieriai, šilumos siurbliai ir priedai. Pristatome visoje Lietuvoje.</p></a>
    <a class="card" href="Paslauga - Įrangos montavimas.html"><span class="cardic">{ic("i-montavimas")}</span><h3>Įrangos montavimas</h3><p>Nuo sistemos parinkimo iki paleidimo ir sureguliavimo. Vilniuje ir apylinkėse.</p></a>
    <a class="card" href="Paslaugos.html"><span class="cardic">{ic("i-remontas")}</span><h3>Priežiūra ir remontas</h3><p>Periodinė profilaktika, gedimų diagnostika ir remonto darbai. Namams ir verslui.</p></a>
    <a class="card" href="Paslauga - Rekuperatorių balansavimas.html"><span class="cardic">{ic("i-balans")}</span><h3>Rekuperacijos balansavimas</h3><p>Išmatuojame ir sureguliuojame oro srautus. Po darbų gaunate matavimų ataskaitą.</p></a>
  </div>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="prose">
  <h2>Dirbame su visais</h2><p>Turite namą, butą, įmonę ar sudėtingą sistemą — kreipkitės. Montuojame ir prižiūrime patikimų gamintojų įrangą: <strong>Mitsubishi Electric, Samsung, Midea, Zehnder, Recom, Airwell, Cooper&amp;Hunter</strong> ir kitų.</p>
  <p>Mums svarbu, kad jūsų namuose ar biure tiesiog būtų gera: tylu, šilta, šviežia. Visa inžinerija — mūsų rūpestis.</p>
  <div class="note"><strong>Kraulis — patikima inžinerija ir žmogiškas komfortas.</strong></div>
</div></div></section>'''
apie+=cta("Pasitarkime dėl jūsų sistemos","Renkatės naują įrangą ar reikia pagalbos su turima — parašykite arba paskambinkite.",
    [btn("Užsakyti servisą","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page("Apie mus.html","Apie mus — Kraulis | ŠVOK įranga ir servisas Vilniuje","Kraulis — šildymo, vėdinimo ir vėsinimo komanda iš Vilniaus. Parduodame įrangą, sumontuojame ir prižiūrime. Servisas namams ir verslui.",apie,"apie")

from build_v2 import OUT as _OUT
print("ALL pages done. Files:", len([f for f in os.listdir(_OUT) if f.endswith('.html')]))
