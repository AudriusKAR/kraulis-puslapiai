# -*- coding: utf-8 -*-
import io, os
from urllib.parse import quote
from build_cr import (page_cr, anno, OUT_CR, reviews_block, review_lead, REVIEWS,
    G_GAR, G_PRAT, TERITORIJA, img_fig, photo_strip)
from build_v2 import MAIL, TEL, TELH, CSS
from build_v2_content import ic, crumbs, titlebar, chips, cta, btn, faq
H=("Pradžia","Pagrindinis.html")

# ---- KONTAKTAI (revised: ką parašyti greitesnei pagalbai)
kont=titlebar("Susisiekime","Renkatės įrangą, reikia serviso ar tik norite pasitarti? Skambinkite arba rašykite — patarsime, net jei dar tik svarstote.",
    kick="Kontaktai",crumb=crumbs(H,("Kontaktai",None)))
kont+=f'''<section><div class="wrap"><div class="cards">
  <a class="card" href="{TELH}"><span class="cardic">{ic("i-phone")}</span><h3>Telefonas</h3><p class="price" style="font-size:16px">{TEL}</p><p>Greičiausias kelias — aiškų gedimą dažnai įkainojame telefonu.</p></a>
  <a class="card" href="mailto:{MAIL}"><span class="cardic">{ic("i-mail")}</span><h3>El. paštas</h3><p class="price" style="font-size:15px">{MAIL}</p><p>Bendras svetainės kontaktas.</p></a>
  <div class="card" style="cursor:default"><span class="cardic">{ic("i-prieziura")}</span><h3>Darbo laikas</h3><p class="mono" style="color:var(--navy)">I–V 8.00–17.00</p><p>Servisas — Vilnius ir apie 100 km aplink.</p></div>
</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="layout aside">
  <div class="prose"><h2>Kad padėtume greičiau</h2>
    <p>Kreipdamiesi trumpai nurodykite: <strong>įrangos tipą ir gamintoją/modelį</strong> (jei žinote), <strong>ką pastebite</strong> (nešaldo, triukšmauja, klaida…) ir <strong>adresą</strong>. Tada dažnai galime patarti ar įkainoti dar prieš atvykdami.</p>
    <h2>Kur dirbame</h2>
    <p>Montavimo, priežiūros ir remonto paslaugas teikiame <strong>Vilniuje ir apie 100 km aplink</strong>. E-parduotuvės prekes pristatome <strong>visoje Lietuvoje</strong>.</p>
    <div class="note">Į užklausas paprastai atsakome per 1–2 darbo dienas. Skubūs darbai derinami individualiai.</div>
    {chips([("Skambinti",TELH,ic("i-phone")),("Rašyti el. paštu",f"mailto:{MAIL}",ic("i-mail")),("Užpildyti užklausą","Užklausos forma.html",ic("i-arrow"))])}
  </div>
  <aside class="side"><div class="card" style="cursor:default"><h3>Rekvizitai</h3>
    <p style="font-size:14px;line-height:1.7;color:var(--steel)">Kraulis, MB<br>Įmonės kodas: 307605802<br>Reg. adresas: Naugarduko g. 68-3, 03203 Vilnius<br>Korespondencijai: Žirnių g. 6, 02120 Vilnius<br>Bankas: „Swedbank“<br><span class="mono" style="font-size:13px">LT22 7300 0102 0138 5725</span></p>
  </div></aside>
</div></div></section>'''
kont+=cta("Užsakykite servisą arba konsultaciją","Aprašykite įrangą ir situaciją — grįšime su aiškiu tolesniu žingsniu.",
    [btn("Užpildyti užklausą","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page_cr("Kontaktai.html","Kontaktai — Kraulis | +370 610 24999","Susisiekite su Kraulis: +370 610 24999, info@kraulis.lt. Servisas Vilniuje ir apylinkėse, prekės — visoje Lietuvoje. Ką nurodyti, kad padėtume greičiau.",kont,"kontaktai",
    anno("sumažinti dvejones; duoti kelis kontakto būdus","turintys klausimą / poreikį","„Skambinti“ / „Užpildyti užklausą“","teritorija — SIŪLOMA „Vilnius +100 km“ (iš paslaugos.lt); tikslus spindulys (Q11)"),"Kontaktai.html")

# ---- UŽKLAUSOS FORMA (revised: kas nutiks toliau)
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
uzk=titlebar("Užsakyti servisą arba konsultaciją","Aprašykite įrangą ir situaciją — grįšime su aiškiu tolesniu žingsniu ir kaina. Kuo tiksliau aprašysite, tuo greičiau padėsime.",
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
    <div class="field"><label for="zinute">Žinutė <span class="req">*</span></label><textarea id="zinute" name="zinute" required placeholder="Aprašykite gamintoją/modelį (jei žinote), ką pastebite ir adresą."></textarea><span class="hint">Įrangos modelis, problema ir adresas padeda įkainoti greičiau.</span></div>
    <label class="consent"><input type="checkbox" required> Sutinku, kad mano pateikti duomenys būtų naudojami atsakymui į šią užklausą pateikti.</label>
    <div style="margin-top:18px"><button class="btn btn-primary" type="submit">Paruošti el. laišką</button>
      <p class="hint" style="margin-top:10px">Paspaudus atsidarys <strong>jūsų el. pašto programa</strong> su paruoštu laišku. Nepatogu? Rašykite <a href="mailto:{MAIL}">{MAIL}</a> arba skambinkite <a href="{TELH}">{TEL}</a>.</p></div>
    <p class="form-status" id="formstatus" role="status" aria-live="polite"></p>
    <noscript><p class="note">Formos siuntimui reikalingas JavaScript. Parašykite <a href="mailto:{MAIL}">{MAIL}</a> arba skambinkite <a href="{TELH}">{TEL}</a>.</p></noscript>
  </form>
  <aside class="side"><div class="card" style="cursor:default"><span class="cardic">{ic("i-check")}</span><h3>Kas nutiks toliau</h3><p style="font-size:14.5px;color:var(--steel)">1. Peržiūrime jūsų užklausą.<br>2. Susisiekiame ir, jei reikia, patikslinam.<br>3. Aiškų gedimą įkainojame; kitu atveju suderiname apžiūrą ir kainą prieš darbus.</p>
    <p class="mono" style="font-size:14px;margin-top:8px"><a href="{TELH}" style="text-decoration:none">{TEL}</a></p></div></aside>
</div></div></section>'''
page_cr("Užklausos forma.html","Užklausa — Kraulis | Užsakyti servisą ar konsultaciją","Užsakykite Kraulis ŠVOK servisą ar konsultaciją: užpildykite užklausą arba skambinkite +370 610 24999. Aiškiai paaiškiname, kas nutiks toliau.",uzk,"kontaktai",
    anno("surinkti užklausą su minimaliu trikdžiu","turintys poreikį/gedimą","„Paruošti el. laišką“","kokios info reikia (Q25–26); formos endpointas"),"Užklausos forma.html",extra_head=FORMJS)

# ---- PATARIMAI (revised card hooks)
pat=titlebar("Patarimai ir gidai","Paaiškiname, kaip veikia sistemos ir į ką atsižvelgti renkantis — be žargono ir be spaudimo pirkti. Pradėkite čia, jei renkatės pirmą kartą.",
    kick="Patarimai",crumb=crumbs(H,("Patarimai",None)))
def gcard(h,p,href):
    return f'<a class="card" href="{href}"><span class="cardic">{ic("i-airflow")}</span><h3>{h}</h3><p>{p}</p><span class="more">Skaityti →</span></a>'
pat+=f'''<section><div class="wrap"><div class="cards">
  {gcard("Kaip išsirinkti rekuperatorių","Kokio našumo reikia, centrinė ar sieninė sistema, filtrai ir kodėl svarbu subalansuoti po montavimo.","Patarimas - Kaip išsirinkti rekuperatorių.html")}
  {gcard("Kaip išsirinkti kondicionierių ar šilumos siurblį","Kaip parinkti galią, ką reiškia SEER/SCOP jūsų sąskaitai ir į ką atsižvelgti Lietuvos klimate.","Patarimas - Kaip išsirinkti kondicionierių ar šilumos siurblį.html")}
  {gcard("Dažni klausimai (DUK)","Kainos, aptarnaujama teritorija, garantijos ir kaip užsakyti servisą — trumpi atsakymai.","DUK.html")}
</div></div></section>'''
pat+=cta("Liko klausimų dėl pasirinkimo?","Pasitarkite — padėsime parinkti sprendimą pagal patalpas ir biudžetą, be įpareigojimo pirkti.",
    [btn("Užsakyti konsultaciją","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page_cr("Patarimai.html","Patarimai ir gidai — Kraulis | Kaip išsirinkti ŠVOK įrangą","Kraulis patarimai: kaip išsirinkti rekuperatorių, kondicionierių ar šilumos siurblį, dažni klausimai. Aiškiai, be žargono ir be spaudimo pirkti.",pat,"patarimai",
    anno("edukacija + pagalba renkantis (SEO)","renkasi pirmą kartą","„Užsakyti konsultaciją“",None),"Patarimai.html")

# ---- GIDAS 1 (+ praktiškas checklist)
g1=titlebar("Kaip išsirinkti rekuperatorių","Rekuperacinis vėdinimas tiekia šviežią orą ir šalina panaudotą, o šilumokaityje atgauna didelę dalį šilumos. Štai kaip apsispręsti be žargono.",
    kick="Patarimai · Gidas",crumb=crumbs(H,("Patarimai","Patarimai.html"),("Kaip išsirinkti rekuperatorių",None)))
g1+='''<section><div class="wrap"><div class="prose">
  <h2>Kam iš viso reikia rekuperacijos</h2><p>Sandarūs namai neišvėdina savęs patys. Rekuperatorius pastoviai tiekia šviežią orą ir šalina panaudotą, o šilumokaityje ištraukiamo oro šiluma pašildo įtraukiamą — todėl gaunate šviežią orą be didelių šilumos nuostolių, mažiau drėgmės ir kvapų.</p>
  <h2>1. Reikiamas oro našumas (m³/h)</h2><p>Svarbiausias parametras. Per mažas našumas nevėdins, per didelis — brangesnis ir triukšmingesnis. Poreikis priklauso nuo patalpų ploto, aukščio, žmonių skaičiaus ir paskirties.</p>
  <h2>2. Centrinė ar sieninė sistema</h2><ul><li><strong>Centrinis su ortakiais</strong> — tolygiausias vėdinimas; geriausia numatyti statybų ar renovacijos metu.</li><li><strong>Sieniniai (decentralizuoti)</strong> — be ortakių, paprasčiau įrengti esamame būste.</li></ul>
  <h2>3. Filtrai ir garsas</h2><p>Filtrus turi būti patogu keisti — tai svarbiausia priežiūros dalis. Įrenginį verta montuoti techninėje patalpoje ir subalansuoti, kad veiktų tyliai.</p>
  <div class="note"><strong>Prieš perkant pasitikslinkite:</strong> patalpų plotą ir aukštį, ar yra vieta įrenginiui ir ortakiams, ar planuojama renovacija. Su šiais duomenimis parinksime tinkamą našumą.</div>
  <div class="note"><strong>Svarbu:</strong> net geras rekuperatorius veiks prastai, jei srautai nesubalansuoti. Po montavimo sistemą reikia <a href="Paslauga - Rekuperatorių balansavimas.html">subalansuoti</a> — pateikiame matavimų ataskaitą „prieš/po“.</div>
</div></div></section>'''
g1+=cta("Renkatės rekuperatorių?","Padėsime parinkti našumą ir sistemą pagal jūsų patalpas — ir sumontuoti bei subalansuoti.",
    [btn("Užsakyti konsultaciją","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page_cr("Patarimas - Kaip išsirinkti rekuperatorių.html","Kaip išsirinkti rekuperatorių — Kraulis gidas","Kaip išsirinkti rekuperatorių: oro našumas, centrinė ar sieninė sistema, filtrai, garsas. Praktiškas gidas be žargono.",g1,"patarimai",
    anno("padėti priimti sprendimą (ne tik parduoti)","renkasi pirmą kartą","„Užsakyti konsultaciją“",None),"Patarimas - Kaip išsirinkti rekuperatorių.html")

# ---- GIDAS 2
g2=titlebar("Kaip išsirinkti kondicionierių ar šilumos siurblį","Oras–oras įranga vėsina vasarą ir šildo žiemą. Svarbiausia — parinkti galią ir tipą pagal patalpas ir Lietuvos klimatą.",
    kick="Patarimai · Gidas",crumb=crumbs(H,("Patarimai","Patarimai.html"),("Kaip išsirinkti kondicionierių ar šilumos siurblį",None)))
g2+='''<section><div class="wrap"><div class="prose">
  <h2>1. Galios parinkimas</h2><p>Per maža galia nešildys/nevėsins per ekstremumus, per didelė — brangesnė ir dažniau įsijungs/išsijungs. Galia priklauso nuo ploto, aukščio, langų, izoliacijos ir orientacijos.</p>
  <h2>2. Kuris tipas jums</h2><ul><li><strong>Oras–oras</strong> — šildo ir vėsina orą patalpoje; paprasčiausias, dažniausias sprendimas.</li><li><strong>Oras–vanduo</strong> šilumos siurblys — šildo pastato vandens sistemą (grindinį šildymą, radiatorius), gali ruošti karštą vandenį.</li><li><strong>Geoterminis (žemė–vanduo)</strong> — šilumą ima iš grunto; stabilus efektyvumas ir žiemą, bet reikia gręžinių ar kolektoriaus, todėl planuojamas iš anksto.</li><li><strong>Multi-split</strong> — vienas lauko blokas kelioms patalpoms.</li></ul>
  <h2>3. Ką reiškia SEER ir SCOP jūsų sąskaitai</h2><p>Tai sezoninio efektyvumo rodikliai: <strong>SCOP</strong> — šildymo, <strong>SEER</strong> — vėsinimo. Kuo didesni, tuo mažesnės metinės elektros sąnaudos. Verta žiūrėti ir į energijos klasę.</p>
  <h2>4. Veikimas šaltyje ir triukšmas</h2><p>Jei siurblys bus pagrindinis šildymas, svarbu, iki kokios lauko temperatūros jis efektyviai šildo. Vidinio ir lauko blokų garsas svarbus miegamiesiems ir kaimynystei.</p>
  <div class="note"><strong>Prieš perkant pasitikslinkite:</strong> kiek patalpų ir koks plotas, ar tai pagrindinis, ar papildomas šildymas, kur tiktų lauko blokas. Tada parinksime galią ir tipą.</div>
</div></div></section>'''
g2+=cta("Nežinote, kokios galios reikia?","Parinksime kondicionierių ar šilumos siurblį pagal jūsų patalpas ir biudžetą.",
    [btn("Užsakyti konsultaciją","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page_cr("Patarimas - Kaip išsirinkti kondicionierių ar šilumos siurblį.html","Kaip išsirinkti kondicionierių ar šilumos siurblį — Kraulis gidas","Kaip išsirinkti kondicionierių ar šilumos siurblį: galia, oras–oras ir oras–vanduo, SEER/SCOP, veikimas šaltyje. Praktiškas gidas.",g2,"patarimai",
    anno("padėti priimti sprendimą","renkasi pirmą kartą","„Užsakyti konsultaciją“",None),"Patarimas - Kaip išsirinkti kondicionierių ar šilumos siurblį.html")

# ---- DUK
duk=titlebar("Dažni klausimai","Trumpi atsakymai apie Kraulis paslaugas, kainas, aptarnaujamą teritoriją ir garantijas.",
    kick="DUK",crumb=crumbs(H,("DUK",None)))
duk+=faq([
  ("Ar aptarnaujate ne pas jus pirktą įrangą?","Taip. Diagnozuojame, remontuojame ir prižiūrime visų pagrindinių gamintojų kondicionierius, šilumos siurblius ir rekuperatorius — nesvarbu, kur juos pirkote. Su servisu neliksite vieni."),
  ("Kiek kainuoja diagnostika ir paslaugos?",["Gedimo diagnostika — nuo 69 €. Profilaktinė priežiūra — nuo 99 €. Rekuperacijos balansavimas — nuo 149 €.","Kainos „nuo“; tikslią suderiname prieš darbus."]),
  ("Kur teikiate paslaugas?",f"Montavimą, priežiūrą ir remontą — {TERITORIJA}. E-parduotuvės prekes pristatome visoje Lietuvoje."),
  ("Per kiek laiko atsakote į užklausą?","Į užklausas atsakome per 1–2 darbo dienas. Skubūs darbai derinami individualiai."),
  ("Kokia darbų garantija?",[f"Darbams — garantija {G_GAR}, priklausomai nuo darbų pobūdžio. Jei per šį laiką kas nors veikia ne taip dėl mūsų darbo — grįžtame ir sutvarkome.",f"Įrangai galioja gamintojo garantija pagal įstatymus; kai įrangą sumontuoja mūsų kvalifikuoti specialistai, ji pailgėja {G_PRAT}."]),
  ("Ar turite reikiamus atestatus darbams?","Taip. Kraulis turi visus veiklai reikalingus atestatus, įskaitant F-dujų (freono) tvarkymo ir elektrosaugos. Tai būtina teisėtam ir saugiam darbui su ŠVOK įranga."),
  ("Ar remontuojate geoterminius šilumos siurblius?","Taip. Dirbame su oras–oras, oras–vanduo ir geoterminiais (žemė–vanduo) šilumos siurbliais."),
  ("Kaip dažnai reikia prižiūrėti įrangą?","Priklauso nuo įrangos tipo ir naudojimo. Reguliari priežiūra palaiko galią, mažina netikėtus gedimus ir padeda išsaugoti gamintojo garantiją. Tinkamą intervalą pasakome pagal jūsų įrangą."),
  ("Ar galima kondicionieriumi šildyti žiemą?","Taip — oras–oras įranga šildo ir vėsina. Kiek efektyviai ji šildo esant šalčiui, priklauso nuo modelio; parenkant atsižvelgiame į Lietuvos klimatą."),
  ("Ar dirbate su verslu ir sudėtingomis sistemomis?","Taip — ir namams, ir verslui, įskaitant sudėtingus sprendimus."),
  ("Kaip užsakyti servisą?","Paskambinkite +370 610 24999, parašykite info@kraulis.lt arba užpildykite užklausos formą — patogiausiu jums būdu."),
],title="Klausimai ir atsakymai",kick="DUK")
duk+=cta("Neradote atsakymo?","Paskambinkite arba parašykite — atsakysime ir patarsime.",
    [btn("Užpildyti užklausą","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page_cr("DUK.html","Dažni klausimai (DUK) — Kraulis | Kainos, teritorija, garantijos","Dažni klausimai apie Kraulis ŠVOK paslaugas: kainos (diagnostika nuo 69 €), aptarnaujama teritorija, garantijos, atestatai, kaip užsakyti servisą.",duk,"patarimai",
    anno("pašalinti abejones, atliepti paiešką","turintys klausimų","„Užpildyti užklausą“","klausimai parinkti iš konkurentų DUK + Kraulis faktų — laukia Audriaus peržiūros (Q19)"),"DUK.html")

# ---- APIE MUS (revised: konkretus darbo principas, be išgalvotos istorijos)
apie=titlebar("Įranga, kuri veikia. Ir žmonės, kurie už ją atsako.","Kraulis — šildymo, vėdinimo ir vėsinimo (ŠVOK) komanda iš Vilniaus. Parduodame įrangą, ją sumontuojame ir liekame šalia tada, kai pardavimas jau įvykęs.",
    kick="Apie mus",crumb=crumbs(H,("Apie mus",None)))
apie+=f'''<section><div class="wrap"><div class="prose">
  <p>Mūsų darbo principas paprastas: įranga tarnauja ilgai ir taupiai tada, kai ja nuolat rūpinamasi. Todėl neapsiribojame pardavimu — parenkame, sumontuojame, subalansuojame ir prižiūrime. Kiekvienas įrenginys turi aiškų priežiūros kelią.</p>
  <p><strong>Turite įrangą, bet negaunate reikiamos pagalbos?</strong> Padėsime. Nesvarbu, kur pirkote ir kokia jos istorija — diagnozuojame, remontuojame ir prižiūrime visų pagrindinių gamintojų kondicionierius, šilumos siurblius ir rekuperatorius.</p>
  <h2>Ką darome</h2></div>
  <div class="cards" style="margin-top:20px">
    <a class="card" href="#" data-todo="eshop-visa"><span class="cardic">{ic("i-shop")}</span><h3>Parduodame įrangą</h3><p>Rekuperatoriai, kondicionieriai, šilumos siurbliai ir priedai. Pristatome visoje Lietuvoje.</p></a>
    <a class="card" href="Paslauga - Įrangos montavimas.html"><span class="cardic">{ic("i-montavimas")}</span><h3>Montuojame</h3><p>Nuo sistemos parinkimo iki paleidimo ir sureguliavimo. {TERITORIJA[0].upper()+TERITORIJA[1:]}.</p></a>
    <a class="card" href="Paslaugos.html"><span class="cardic">{ic("i-remontas")}</span><h3>Prižiūrime ir remontuojame</h3><p>Profilaktika, diagnostika ir remontas. Namams ir verslui, įskaitant sudėtingus sprendimus.</p></a>
    <a class="card" href="Paslauga - Rekuperatorių balansavimas.html"><span class="cardic">{ic("i-balans")}</span><h3>Balansuojame</h3><p>Sureguliuojame oro srautus ir pateikiame matavimų ataskaitą „prieš/po“.</p></a>
  </div>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="prose">
  <h2>Kodėl galite pasitikėti</h2>
  <p><strong>8 metų patirtis</strong> ŠVOK srityje ir <strong>5,0 įvertinimas</strong> pagal klientų atsiliepimus. Dirbame ne dėl vienkartinio darbo, o dėl to, kad grįžtumėte ir rekomenduotumėte.</p>
  <ul>
    <li><strong>Visi veiklai reikiami atestatai</strong> — įskaitant F-dujų (freono) tvarkymo ir elektrosaugos. Tai būtina teisėtam ir saugiam darbui su šaltnešiu.</li>
    <li><strong>Atsakomybė po pardavimo</strong> — priežiūra ir remontas, net jei įrangą pirkote kitur. Su servisu neliekate vieni.</li>
    <li><strong>Skaidrumas</strong> — kainą ir apimtį suderiname prieš darbus, o po jų paaiškiname, kaip naudoti, kad problema nesikartotų.</li>
  </ul>
</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="prose">
  <h2>Dirbame su visais</h2><p>Turite namą, butą, įmonę ar sudėtingą sistemą — kreipkitės. Į sudėtingas situacijas žiūrime ne kaip į priežastį jų vengti, o kaip į galimybę rasti geriausią sprendimą.</p>
  <p>Mums svarbu, kad jūsų namuose ar biure tiesiog būtų gera: tylu, šilta, šviežia. Visa inžinerija — mūsų rūpestis.</p>
  <div class="note"><strong>Kraulis — patikima inžinerija ir žmogiškas komfortas.</strong></div>
</div></div></section>'''
apie+=photo_strip(["matavimas","toshiba","trane","rekuperatorius"],sub="Nuo butų iki sudėtingų verslo sistemų — dirbame profesionalia įranga ir atsakome už rezultatą.")
apie+=reviews_block(sub="Realūs klientų atsiliepimai apie mūsų atliktus darbus — remontą, montavimą ir balansavimą.")
apie+=cta("Pasitarkime dėl jūsų sistemos","Renkatės naują įrangą ar reikia pagalbos su turima — parašykite arba paskambinkite.",
    [btn("Užsakyti konsultaciją","Užklausos forma.html"),btn(f"Skambinti {TEL}",TELH,"ghost cta-ghost")])
page_cr("Apie mus.html","Apie mus — Kraulis | ŠVOK įranga ir servisas Vilniuje","Kraulis — ŠVOK komanda iš Vilniaus. 8 m. patirtis, visi reikiami atestatai. Parduodame įrangą, sumontuojame ir prižiūrime; liekame atsakingi po pardavimo.",apie,"apie",
    anno("paaiškinti darbo principą + kelti pasitikėjimą (patirtis, atestatai, atsiliepimai, nuotraukos)","visi","„Užsakyti konsultaciją“","nuotraukos įdėtos — laukia failų į /img (žr. IMG-INSTRUKCIJA)"),"Apie mus.html")

# =========================================================== DASHBOARD (index.html)
PAGES=[
 ("Pagrindinis","Pagrindinis.html","index.html","🟠","Hero + realios darbų nuotraukos + atsiliepimai (5,0) + servisas po pardavimo"),
 ("Paslaugos","Paslaugos.html","Paslaugos.html","🟠","„Kodėl Kraulis“ blokas; garantija nuo 3 iki 24 mėn. + gamintojo pratęsimas"),
 ("Kondicionierių remontas","Paslauga - Kondicionierių remontas.html","Paslauga - Kondicionierių remontas.html","🟠","„Ką patikriname“; termovizijos nuotrauka"),
 ("Šilumos siurblių remontas","Paslauga - Šilumos siurblių remontas.html","Paslauga - Šilumos siurblių remontas.html","🟠","Geoterminiai ĮTRAUKTI (Q7 ✓); Toshiba serviso nuotrauka"),
 ("Rekuperatorių remontas","Paslauga - Rekuperatorių remontas.html","Paslauga - Rekuperatorių remontas.html","🟠","„Ką patikriname“; rekuperatoriaus nuotrauka; nuoroda į balansavimą"),
 ("Rekuperatorių balansavimas","Paslauga - Rekuperatorių balansavimas.html","Paslauga - Rekuperatorių balansavimas.html","🔴","Signature — ataskaita + realus atsiliepimas + „testo“ matavimo nuotraukos"),
 ("Profilaktinė priežiūra","Paslauga - Profilaktinė priežiūra.html","Paslauga - Profilaktinė priežiūra.html","🟠","Aiškesnė nauda; „ką apima“ konkrečiau"),
 ("Įrangos montavimas","Paslauga - Įrangos montavimas.html","Paslauga - Įrangos montavimas.html","🟠","Kvalifikuotas montavimas; garantijos pratęsimas 3–5 m.; nuotraukos"),
 ("Kontaktai","Kontaktai.html","Kontaktai.html","🟠","„Kad padėtume greičiau“; teritorija Vilnius +100 km"),
 ("Užklausos forma","Užklausos forma.html","Užklausos forma.html","🟠","„Kas nutiks toliau“; laukų hint'ai"),
 ("Patarimai","Patarimai.html","Patarimai.html","⚪","Konkretesni kortelių kabliukai"),
 ("Gidas: rekuperatorius","Patarimas - Kaip išsirinkti rekuperatorių.html","Patarimas - Kaip išsirinkti rekuperatorių.html","⚪","Praktiškas „prieš perkant“ checklist"),
 ("Gidas: kondicionierius / šil. siurblys","Patarimas - Kaip išsirinkti kondicionierių ar šilumos siurblį.html","Patarimas - Kaip išsirinkti kondicionierių ar šilumos siurblį.html","⚪","SEER/SCOP → nauda; geoterminiai įtraukti"),
 ("DUK","DUK.html","DUK.html","🟠","Realūs klausimai (konkurentų DUK+faktai); garantija, atestatai, geoterminiai"),
 ("Apie mus","Apie mus.html","Apie mus.html","🟠","8 m. patirtis, atestatai, realūs atsiliepimai; darbo principas"),
]
rows=""
for name,cr,sv,st,chg in PAGES:
    rows+=f'<tr><td>{st}</td><td><b>{name}</b></td><td>{chg}</td><td><a href="{quote(cr)}" target="_blank">Siūloma ↗</a></td><td><a href="../site-v2/{quote(sv)}" target="_blank">Dabartinė ↗</a></td></tr>'
DASH=f'''<!DOCTYPE html><html lang="lt"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kraulis — turinio peržiūra (content-review)</title><meta name="robots" content="noindex">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}
.dash{{max-width:1100px}}
table.rev{{width:100%;border-collapse:collapse;background:var(--white);border:1px solid var(--line);border-radius:14px;overflow:hidden;font-size:14px;margin-top:10px}}
table.rev th,table.rev td{{padding:12px 14px;text-align:left;border-bottom:1px solid var(--line-soft);vertical-align:top}}
table.rev th{{font-family:'IBM Plex Mono',monospace;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--steel);background:var(--paper)}}
table.rev tr:last-child td{{border-bottom:none}}
table.rev a{{font-family:'Archivo',sans-serif;font-weight:700;text-decoration:none;white-space:nowrap}}
.legend{{display:flex;gap:18px;flex-wrap:wrap;font-size:13px;color:var(--steel);margin-top:14px}}
.docs a{{display:inline-block;margin:4px 10px 4px 0;font-family:'Archivo',sans-serif;font-weight:700;text-decoration:none;color:var(--navy);border:1px solid var(--line);border-radius:8px;padding:8px 14px}}
.docs a:hover{{border-color:var(--sky);color:var(--sky-deep)}}
</style></head><body>
<header><div class="wrap hd"><a href="index.html" aria-label="Kraulis">{__import__('build_v2').logo('#24303E')}</a><span class="mono" style="font-size:12px;color:var(--steel)">Turinio peržiūra · content-review</span></div></header>
<section class="titlebar"><div class="wrap"><div class="inner dash">
  <span class="kick">Content review · tik peržiūrai</span>
  <h1>Kraulis turinio peržiūra</h1>
  <p class="lead">Siūlomas 15 puslapių turinys <strong>tuo pačiu final-cba dizainu</strong>. Palyginkite su dabartine site-v2 versija. Kiekvienam siūlomam puslapiui viršuje — anotacijų juosta (tikslas, auditorija, CTA, laukiantys patvirtinimo teiginiai). <strong>Dizainas nekeičiamas; site-v2 neliestas.</strong></p>
</div></div></section>
<section><div class="wrap dash">
  <div class="sh"><div><span class="kick">Audito santrauka</span><h2>Ką keičiu ir kodėl</h2></div></div>
  <div class="prose" style="max-width:820px">
    <ul>
      <li><strong>0 fiktyvių faktų</strong> — kainos, garantijos, teritorija, gamintojai nekeisti.</li>
      <li><strong>Hero ir CTA varijuoti</strong> — nebe ta pati formulė visur; CTA pagal puslapio tikslą (pirkimas / servisas / konsultacija).</li>
      <li><strong>Paslaugų puslapiuose — techninė kompetencija</strong>: pridėta „ką patikriname / sutvarkome".</li>
      <li><strong>Gidai realiai padeda apsispręsti</strong> — pridėti „prieš perkant" patikslinimai, CTA = konsultacija.</li>
      <li><strong>Kontaktai / forma</strong> — paaiškinta, kokios info reikia ir kas nutiks toliau.</li>
      <li><strong>Nenaudota:</strong> „geoterminiai", „1–2 d.d." kaip pažadas pagrindiniuose, jokių atsiliepimų/skaičių.</li>
    </ul>
    <p class="mono" style="font-size:13px;color:var(--steel)">Pilna analizė ir klausimai — dokumentuose:</p>
    <div class="docs">
      <a href="../CONTENT-AUDIT.md">CONTENT-AUDIT.md</a><a href="../CONTENT-QUESTIONS.md">CONTENT-QUESTIONS.md</a><a href="../CONTENT-VOICE.md">CONTENT-VOICE.md</a><a href="../../.agents/product-marketing.md">product-marketing.md</a>
    </div>
  </div>
  <div class="sh" style="margin-top:36px"><div><span class="kick">Visi puslapiai</span><h2>Siūloma vs dabartinė</h2></div></div>
  <table class="rev"><thead><tr><th>Prior.</th><th>Puslapis</th><th>Svarbiausias pakeitimas</th><th>Siūloma</th><th>Dabartinė</th></tr></thead><tbody>{rows}</tbody></table>
  <div class="legend"><span>🔴 kritinis</span><span>🟠 svarbus</span><span>⚪ kosmetinis</span></div>
  <div class="prose" style="max-width:820px;margin-top:30px">
    <h2>Atviri klausimai (svarbiausi)</h2>
    <p>Prieš galutinius tekstus reikia jūsų atsakymų — visų 26 klausimų sąrašas <a href="../CONTENT-QUESTIONS.md">CONTENT-QUESTIONS.md</a>. Svarbiausi: <strong>Q7</strong> (ar geoterminiai?), <strong>Q9</strong> (garantijos trukmė), <strong>Q15–16</strong> (patirtis / sertifikuoti montuotojai), <strong>Q17</strong> („1–2 d.d." formuluotė), <strong>Q19</strong> (realūs klientų klausimai), <strong>Q21</strong> (ką labiausiai akcentuoti), <strong>Q23</strong> (ar bus nuotraukų/atsiliepimų).</p>
    <h2>Pirma tikrinti</h2>
    <p><strong>Pagrindinis</strong>, <strong>Paslaugos + Balansavimas</strong>, <strong>Apie mus</strong> — didžiausias poveikis pasitikėjimui ir konversijai.</p>
  </div>
</div></section>
<footer style="margin-top:0"><div class="wrap"><div class="foot-b" style="border:none"><span>Kraulis, MB · turinio peržiūra (nebus gamyboje)</span><span><a href="../site-v2/index.html" style="color:var(--cloud)">Dabartinė site-v2 →</a></span></div></div></footer>
</body></html>'''
io.open(os.path.join(OUT_CR,"index.html"),"w",encoding="utf-8").write(DASH)
print("cr done. files:", len([f for f in os.listdir(OUT_CR) if f.endswith('.html')]))
