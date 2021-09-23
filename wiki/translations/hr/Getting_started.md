# Getting started/hr
<div class="mw-translate-fuzzy">


{{docnav/hr
|[Instaliraj na Mac](Install_on_Mac/hr.md)
|[Model Miša](Mouse_Model/hr.md)
}}


</div>


{{TOCright}}

## Predgovor


<div class="mw-translate-fuzzy">

FreeCAD je CAD/CAE [aplikacija parametarskog modeliranja](About_FreeCAD/hr.md).Prvenstveno je napravljen za dizajn mehanike, ali podržava sve druge primjene gdje je potrebno 3D modeliranje objekata sa velikom preciznošću i kontrolom zabilješki modelirnja.


</div>


<div class="mw-translate-fuzzy">

FreeCAD je u razvoju već neko vrijeme i pruža dugačku (i stalno rastuću)listu [Značajke](Feature_list/hr.md). Mogućnosti su ograničene u usporedbi sa komercijalnim rješenjima i možda nisu dovoljno razvijene za korištenje u proizvodnji ali su dovoljne za većinu hobi korisnika i za manje radionice. Ovdje se nalazi brzo rastuća zajednica oduševljenih korisnika koji sudjeluju u razvoju [FreeCAD forum](http://forum.freecadweb.org/index.php) a vi možete pogledati na [primjeri](https://forum.freecadweb.org/viewforum.php?f=24) stranicu gdje će te naći mnoštvo projekata razvijenih sa programom FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Kao svi open-source projekti, FreeCAD projekt nije jednostrano djelo koje vam se servira. On je ovisan o zajednici da bi mogao rasti, dobiti nove funkcije ili ispraviti pogreške u programu. Zato nemojte to zaboraviti dok koristite FreeCAD ; ako vam se sviđa, vi možete direktno utjecati na program i pomoći u razvoju[Pomozite FreeCAD-u](help_FreeCAD/hr.md)!


</div>

See also:

-   [Migrating to FreeCAD from Fusion360](Migrating_to_FreeCAD_from_Fusion360.md)
-   [Tutorials](Tutorials.md)
-   [Video tutorials](Video_tutorials.md)

## Instalacija


<div class="mw-translate-fuzzy">

Prvo preuzmite i instalirajte FreeCAD. Pogledaj [Preuzimanja](Download/hr.md) stranicu za informacije o preuzimanju, trenutnoj verziji programa, i o nadopunama. Za instrukcije [Instalacija](Installing/hr.md) ṡtranicu. Tamo se nalaze paketi za Windowse (.msi), Debian i Ubuntu (.deb), openSUSE (.rmp) i Mac OSX. FreeCAD je dostupan kroz \"package managers\" puno drugih Linux distribucija. Samostalni \[ AppImage/hr\|AppImage\] izvršni program je takođe dostupan za većinu novijih 64-bit Linux sistema. FreeCAD je open-source, vi možete preuzeti \"source code\" [Kompiliranje](Compiling/hr.md) i sastaviti (kompilirati) ga sami.


</div>

## Istraživanje sučelja 

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;"> 
*Standardno FreeCAD sučelje u 0.19.*


</div>


<div class="mw-translate-fuzzy">


**See a full explanation in [Sučelje](Interface/hr.md).**


:   1\. [3D prikaz](3D_view/hr.md), prikazuje stvari u vašem dokumentu
:   2\. [Pregled grananja](tree_view/hr.md), prikazuje hijerarhiju i povijest izrade svih objekata u vašem dokumentu
:   3\. [Uređivač osobina](Property_editor/hr.md), koji omogućava da vidite i promijenite osobine odabranih objekata
:   4\. [Prozor odabira](selection_view/hr.md), ukazuje na odabrane objekte ili pod-elemente objekata (vrhove, rubove, lica).
:   5\. [Izvještaj (ili prozor izlaza)](report_view/hr.md), u kojem FreeCAD ispisuje poruke, upozorenja i greške
:   6\. [Python Konzola](Python_console/hr.md), gdje se ispisuju sve naredbe koje se izvršavaju u FreeCAD-u, i gdje možete upisati Python izvršni kod
:   7\. [status bar](status_bar/hr.md), ovdje se pojavljuju poruke i pomoćni opisi.
:   8\. Područje pomoćnih opisa , gdje su pomoćni opisi usidreni.
:   9\. [Radne ploče](Workbenches/hr.md), gdje odabirete aktivni radni stol
:   10\. [Standardni izbornik](Standard_Menu/hr.md), koji sadrži osnovne operacije programa.


</div>


<div class="mw-translate-fuzzy">

Osnovni koncept FreeCAD sučelja je taj da je podijeljen na [Radne ploče](workbenches/hr.md). Radna ploča je kolekcija alata za specifičnu namjenu, kao rad sa [Moduli mreže](Mesh_Workbench/hr.md), ili crtanje [2D objekti](Draft_Workbench/hr.md), ili [Skiciraj radna površina](Sketcher_Workbench/hr.md). Možete odabrati aktivnu Radnu površinu sa izbornikom (6). Možete prilagoditi [Postavke sučelja](Interface_Customization/hr.md) uključene u Radnu površinu, dodati alate iz druge Radne površine ili osobno kreiranih alata, koje mi zovemo [Makronaredbe](macros/hr.md). Obično se počinje sa Radnim površinama [Oblikovanje Tijela radna površina](PartDesign_Workbench/hr.md) i [Tijelo radna površina](Part_Workbench/hr.md).


</div>


<div class="mw-translate-fuzzy">

Kada otvorite FreeCAD prvi puta otvorit če se Start Centar Ovdje je izgled od verzije 0.18:


</div>

<img alt="" src=images/Start_center_0.18_screenshot.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

Start Centar omogućuje brzi prijelaz na uobičajene radne ploče, otvara uobičajeni dokument ili pregled zadnjih vijesti iz FreeCAD svijeta. Vi možete promijeniti početnu radnu ploču u [Uređivač postavki](Preferences_Editor/hr.md).


</div>

## Navigacija u 3D prostoru 


<div class="mw-translate-fuzzy">

FreeCAD ima na raspolaganju nekoliko različitih [navigacijski načini](Mouse_Model.md) koji mijenjaju način na koji miš koristi za interakciju s objektima u 3D prikazu i samom prikazu. Jedan od njih posebno je izrađen za [touchpads](Mouse_Model_#_Touchpad_Navigation.md), gdje se ne koristi srednja tipka miša. Sljedeća tablica opisuje zadani način rada, nazvan \'\' \'CAD Navigation\' \'\' (trenutni način navigacije možete brzo promijeniti desnim klikom na prazno područje 3D prikaza):


</div>


{{CAD Navigation
|Select_name=Odabir
|Pan_name=Pomakni
|Zoom_name=Zoom
|Rotate_view_name=Zaokreni pogled<br>Prva mogučnost
|Rotate_view_alt_name=Zaokreni pogled<br>Druga mogučnost
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Kliknite sa lijevom tipkom miša na objekt kojeg želite odabrati.

Držeći stisnutom **Ctrl** tipku moguće je odabrati više objekata.
|Pan_text=Držite stisnutu srednju tipku i onda pomjerajte.
|Pan_mode_text=Pan mode: držite **Ctrl** tipku, stisnite desnu tipku miša jednom, zatim pomjerajte. <small>(v0.17)</small> 
|Zoom_text=Koristite točak miša za zumiranje.

Pritiskanjem srednje tipke miša premješta središte rotacije na položaj strelice.
|Zoom_mode_text=Zoom mode: držite **Ctrl** i **Shift** tipke, stisnitipku mišate desnu tipku miša jednom, zatim pomjerajte. <small>(v0.17)</small> 
|Rotate_view_text=Držite stisnutu srednju tipku miša , zatim stisnite i držite lijevu tipku miša i onda pomjerajte.

Mjesto pokazivača kada se pritisne srednja tipka miša određuje središte rotacije. Rotacija djeluje poput okretanja kugle koja se rotira oko njenog središta. Ako su tipke otpuštene prije zaustavljanja pokreta miša, prikaz će se nastaviti [predenje](spinning.md), ako je ovo omogućeno.

Dvostruki pritisak na srednju tipku miša postavlja središte rotacije.
|Rotate_view_mode_text=mod zakretanja: držite **Shift** tipku, stisnite desnu tipku miša jednom, zatim pomjerajte. <small>(v0.17)</small> 
|Rotate_view_alt_text=držite srednju tipku, zatim stisnite i držite desnu tipku miša i onda pomjerajte.

Kod ove metode srednja tipka miša može se otpustiti nakon pritiska desne tipke miša.

Korisnici koji koriste miš desnom rukom mogu naći ovu metodu lakšom od prve.

}}

Vi imate nekoliko pogleda koji su predefinirani (pogled odozgo, pogled sprijeda itd.) koji se nalaze u izborniku pregleda, a imate i brojevne prečice (**1**, **2**, itd\...). Sa klikom na objekt ili prazno područje sa desnom tipkom miša možete dobiti brzi pristup nekim osnovnim operacijama kao postavljanje pogleda, ili položaj objekta u stablu pregleda.

## Prvi koraci sa FreeCAD-om 

Fokus FreeCAD-a vam je omogućiti izradu 3D preciznih 3D modela, strogu kontrolu nad tim modelima (mogućnost vraćanja u povijest modeliranja i izmjenu parametara) i na kraju izradu tih modela (putem 3D ispisa, CNC obrade ili čak gradilišta). Stoga se vrlo razlikuje od nekih drugih 3D aplikacija napravljenih u druge svrhe, poput animacijskog filma ili igranja. Njegova krivulja učenja može biti strma, posebno ako je ovo vaš prvi kontakt s 3D modeliranjem. Ako u nekom trenutku imate poteškoće, nemojte zaboraviti da će vas prijateljska zajednica korisnika na [FreeCAD forumu](http://forum.freecadweb.org/index.php) uspjeti pomoći u bilo kojem trenutku.


<div class="mw-translate-fuzzy">

Radna ploča koju ćete početi koristiti u FreeCAD-u ovisi o vrsti posla koji trebate obaviti: Ako radite na mehaničkim modelima ili općenito nekim objektima manjeg opsega, vjerojatno ćete željeti isprobati [Dizajniranje dijelova radna ploča](PartDesign_Workbench/hr.md). Ako radite u 2D-u, prebacite se na [ Nacrt radna ploča](Draft_Workbench/hr.md) ili na [Skiciraj radna ploča](Sketcher_Workbench/hr.md) ako su vam potrebna ograničenja. Ako želite učiniti BIM, pokrenite [BIM radna ploča](BIM_Workbench/hr.md) ili [Arhitekt radna ploča](Arch_Workbench/hr.md). Ako radite s dizajnom brodova, za vas postoji poseban [Brod radna ploča](Ship_Workbench/hr.md). A ako stižete iz svijeta OpenSCAD, pokušajte [OpenSCAD radna ploča](OpenSCAD_Workbench/hr.md).


</div>


<div class="mw-translate-fuzzy">

Radne ploče možete prebaciti u bilo koje vrijeme i također [Prilagodba sučelja](Interface_Customization/hr.md) svoju omiljenu radnu ploču koristiti za dodavanje alata s drugih radnih ploča.


</div>

## Rad sa radnim pločama Dizajniranje dijelova i Skiciraj 


<div class="mw-translate-fuzzy">

[Dizajniranje dijelova radna ploča](PartDesign_Workbench/hr.md) izrađen je za izgradnju složenih objekata, počevši od jednostavnih oblika, dodajući ili uklanjajući dijelove (zvane \"značajke\"), sve dok ne dođete do vašeg konačnog objekta. Sve značajke koje ste primijenili tijekom postupka modeliranja pohranjuju se u zasebnom prikazu pod nazivom [prikaz stabla](Document_structure/hr.md), koji sadrži i ostale objekte u vašem dokumentu. Objekt PartDesign (Dizajniranje dijelova) možete smatrati dodavanjem operacija, a svaka se primjenjuje na rezultat prethodnog, tvoreći jedan veliki lanac. U prikazu stabla vidite svoj konačni objekt, ali možete ga proširiti i dohvatiti sva prethodna stanja te promijeniti bilo koji njihov parametar, koji automatski ažurira konačni objekt.


</div>


<div class="mw-translate-fuzzy">

Radna ploča PartDesign (Dizajniranje dijelova) uvelike koristi druge radne ploče, [Skiciraj radna ploča](Sketcher_Workbench/hr.md). Skica omogućuje crtanje dvodimenzionalnih oblika koji su definirani primjenom ograničenja na 2D oblik. Na primjer, možete nacrtati pravokutnik i postaviti veličinu stranice primjenjujući ograničenje duljine na jednu od strana. Ta se strana tada više ne može promijeniti (osim ako se ne promijeni ograničenje).


</div>

Ti 2D oblici napravljeni pomoću Skiciraj puno se koriste na radnoj ploči PartDesign-a, na primjer za stvaranje 3D volumena ili za crtanje područja na licima vašeg objekta koja će se nakon toga izdubiti iz glavnog volumena. Ovo je tipičan PartDesign (Dizajniranje dijelova) tijek rada:

1.  Stvori novu skicu
2.  Nacrtaj zatvoreni oblik (budite sigurni da su sve točke spojene)
3.  Zatvori skicu
4.  Izvuci skicu u 3D tijelo pomoću alata (pad) podmetanje
5.  Odaberite jedno lice na tijelu
6.  Stvorite drugu skicu (ovaj put će biti nacrtana na odabranom licu)
7.  Nacrtaj zatvoreni oblik
8.  Zatvori skicu
9.  Na prvom objektu napravite džep iz druge skice

Što vam daje ovakav predmet:

<img alt="" src=images/Partdesign_example.jpg  style="width:1024px;">

U bilo kojem trenutku možete odabrati originalne skice i modificirati ih ili promijeniti parametre ekstruzije padova ili džepnih operacija, što će ažurirati konačni objekt.

## Rad s radnim pločama Nacrt i Arhitekt 


<div class="mw-translate-fuzzy">

[Nacrt](Draft_Workbench/hr.md) i [Arhitekt](Arch_Workbench/hr.md) ponašaju se malo drugačije od ostalih radnih radnih ploča gore, iako slijede ista pravila, koja su zajednička svima FreeCAD-u. Ukratko, dok su Sketcher (Skiciraj) i PartDesign (Dizajniranje dijelova) primarno dizajnirani za pojedinačne komade, Nacrt i Arhitekt su napravljeni da olakšaju vaš rad kada radite s nekoliko jednostavnijih objekata.


</div>


<div class="mw-translate-fuzzy">

[Nacrt radna ploča](Draft_Workbench/hr.md) nudi vam 2D alate pomalo slične onima koje možete pronaći u tradicionalnim 2D CAD aplikacijama, poput [AutoCAD](https://en.wikipedia.org/wiki/AutoCAD). No, 2D nacrt je daleko od dosega FreeCAD-a, nemojte očekivati da će te tamo naći čitav niz alata koje nude ove posvećene aplikacije. Većina alata za nacrte djeluje ne samo u 2D ravnini, već i u cijelom 3D prostoru, a imaju koristi od posebnih pomoćnih sustava kao što su [Označi plohu nacrta](Draft_SelectPlane.md) i [Privuci objekt](Draft_Snap/hr.md).


</div>


<div class="mw-translate-fuzzy">

[Arhitekt](Arch_Workbench/hr.md) dodaje [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) alate FreeCAD, omogućujući vam izgradnju arhitektonskih modela s parametarskim objektima. Arhitekt radna ploča se uvelike oslanja na druge module kao što su Nacrt i Skiciraj. Svi alati za crtanje su također prisutni na Arhitekt radnoj ploči, a većina Arhitekt alata koristi nacrte za pomoćne sustave.


</div>

Tipičan tijek rada s Arch ( Arhitekt) i Drafts (Nacrt)radnim pločama može biti:

1.  Nacrtajte nekoliko linija pomoću alata Nacrtaj liniju
2.  Odaberite svaku liniju i pritisnite Zid alat da na svakom od njih izgradite zid
3.  Pridružite zidove tako da ih odaberete i pritisnete alat Arch Add (Arhitekt Dodaj)
4.  Napravite podni objekt i pomičite zidove u njemu s pogleda na Drvo
5.  Napravite građevinski objekt i pomaknite kat u njemu sa stabla
6.  Stvorite prozor klikom na alat Prozor, odaberite postavku na njenoj ploči, a zatim kliknite lice zida
7.  Dodajte dimenzije prvo postavite radnu ravninu ako je potrebno, a zatim pomoću alata Draft Dimension (dimenzija nacrta)

Što vam daje ovo:

<img alt="" src=images/Arch_workflow_example.jpg  style="width:1024px;">

Više informacija na stranici [Vježbe](Tutorials/hr.md).

## Dodatci, Makronaredbe i Vanjske radne ploče 

Freecad, kao softver otvorenog koda, nudi mogućnost nadopune radnih ploča dodacima.

Princip [Dodatci](Addon/hr.md) temelji se na razvoju dopuna radne površine. Bilo koji korisnik može razviti funkciju za koju smatra da nedostaje za vlastite potrebe ili, u konačnici, za zajednicu. Pomoću foruma korisnik može zatražiti mišljenje, pomoć na forumu. Može dijeliti, ili ne, objekt svog razvoja prema pravilima o autorskim pravima koje treba definirati. Besplatno njoj / njemu. Kako bi se razvio, korisnik ima na raspolaganju [skripti](scripting/hr.md) funkcije.


<div class="mw-translate-fuzzy">

Postoje dvije vrste dodataka:

1.  [Makronaredbe](Macros/hr.md): kratki isječci Python koda koji pružaju novi alat ili funkcionalnost. Makronaredbe obično počinju kao način pojednostavljenja ili automatizacije zadatka crtanja ili uređivanja određenog objekta. Ako se mnogo makronaredbi sakuplja unutar mape, cijeli se direktorij može distribuirati kao nova radna ploča.
2.  [Vanjskie radne ploče](External_workbenches/hr.md): zbirka alata programiranih u Pythonu ili C ++ koji na važan način proširuju FreeCAD. Ako je radna ploča dovoljno razvijena i dobro je dokumentirana, može biti uključena kao jedana od osnovnih radnih ploča u FreeCAD. Pod [ Vanjske radne ploče](External_workbenches/hr.md) naći ćete principe i popis postojeće knjižnice.


</div>

## Skriptiranje

I na kraju, jedna od najmoćnijih značajki FreeCAD-a je [skriptiranje](scripting/hr.md) okruženje. Iz integrirane python konzole (ili iz bilo koje druge vanjske Python skripte) možete dobiti pristup gotovo bilo kojem dijelu FreeCAD-a, stvoriti ili izmijeniti geometriju, modificirati reprezentaciju tih objekata na 3D sceni ili pristupiti i izmijeniti FreeCAD sučelje. Python skripti mogu se koristiti i u [makronaredbe](macros/hr.md), koje pružaju jednostavan način stvaranja prilagođenih naredbi.

## Šta ima novoga 

-   Pogledajte [Bilješke distribucije](Feature_list/hr#Release_notes.md) za detaljnu listu značajki.


<div class="mw-translate-fuzzy">


{{docnav/hr
|[Instaliraj na Mac](Install_on_Mac/hr.md)
|[Model Miša](Mouse_Model/hr.md)
}}


</div>


{{Userdocnavi/hr}}

[Category:User Documentation/hr](Category:User_Documentation/hr.md)

---
[documentation index](../README.md) > Getting started/hr
