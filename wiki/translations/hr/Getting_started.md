# Getting started/hr
## Predgovor

FreeCAD je CAD/CAE [aplikacija parametarskog modeliranja](About_FreeCAD/hr.md).Prvenstveno je napravljen za dizajn mehanike, ali podržava sve druge primjene gdje je potrebno 3D modeliranje objekata sa velikom preciznošću i kontrolom zabilješki modeliranja.

FreeCAD je u razvoju od 2002. godine i nudi veliki popis [features](Feature_list/hr.md). Neke mogućnosti još nedostaju, ali dovoljno je moćan za hobi upotrebu i male radionice. Postoji brzorastuća zajednica korisnika koji sudjeluju na [FreeCAD forumu](http://forum.freecadweb.org/index.php), a možete pronaći [?f=24 mnogo primjera](https://forum.freecadweb.org/viewforum.php) kvalitetnih projekata razvijenih sa FreeCAD-om. Vidi također, [FreeCAD korišten u proizvodnji](FreeCAD_used_in_production.md).

Kao svaki slobodni softver projekt, FreeCAD je ovisan o zajednici da bi mogao rasti, dobiti nove funkcije ili ispraviti pogreške u programu. Zato nemojte to zaboraviti dok koristite FreeCAD ; ako vam se sviđa, i vi možete direktno utjecati na program i pomoći [donate](Donate.md) i [help FreeCAD](Help_FreeCAD.md) učestvovati u razvoju kao npr. pisati dokumentaciju i prevoiti.

See also:

-   [Migrating to FreeCAD from Fusion360](Migrating_to_FreeCAD_from_Fusion360.md)
-   [Which workbench should I choose?](Which_workbench_should_I_choose.md)
-   [Tutorials](Tutorials.md)
-   [Video tutorials](Video_tutorials.md)



## Instalacija


<div class="mw-translate-fuzzy">

Prvo preuzmite i instalirajte FreeCAD. Pogledaj [Preuzimanja](Download/hr.md) stranicu za informacije o preuzimanju, trenutnoj verziji programa, i o nadopunama, i instrukcije [Instalacija](Installing/hr.md) za vaš operacijski sustav ([Windows](Installing_on_Windows/hr.md), [Linux](Installing_on_Linux/hr.md) or [Mac](Installing_on_Mac/hr.md)). Postoje spremni instalacijski paketi za Windows (.msi), Debian i Ubuntu (.deb), openSUSE (.rpm) i Mac OSX. FreeCAD je dostupan od upravitelja paketa mnogih drugih distribucija Linuxa. Dostupna je i samostalna izvršna datoteka [AppImage](AppImage/hr.md) koja će se izvoditi na najnovijim 64-bitnim Linux sustavima. Budući da je FreeCAD otvorenog koda, također možete preuzeti izvorni kod i [kompilirati](Compiling/hr.md) ga sami.


</div>



## Istraživanje sučelja 

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">



*Standardno FreeCAD sučelje*


**pogledaj obašnjenje u [Sučelje](Interface/hr.md).**


:   1\. [glavni pogled](main_view_area.md), koji mogu sadržavati različite prozore s karticama, uglavnom[3D pogled](3D_view/hr.md).
:   2\. [3D pogled](3D_view/hr.md), prikazuje geometrijske objekte u dokumentu
:   3\. [Pregled grananja](tree_view/hr.md), (dio od [combo view](combo_view/hr.md)) prikazuje hijerarhiju i povijest izrade svih objekata u vašem dokumentu; takođe može prikazati [task panel](task_panel/hr.md) za aktivne naredbe..
:   4\. [Uređivač osobina](property_editor/hr.md), (dio od [combo view](combo_view/hr.md))koji omogućava da vidite i promijenite osobine odabranih objekata.
:   5\. [Prozor odabira](selection_view/hr.md), ukazuje na odabrane objekte ili pod-elemente objekata (vrhove, rubove, lica).
:   6\. [Izvještaj](report_view/hr.md) (ili prozor izlaza), u kojem FreeCAD ispisuje poruke, upozorenja i greške
:   7\. [Python Konzola](Python_console/hr.md), gdje se ispisuju sve naredbe koje se izvršavaju u FreeCAD-u, i gdje možete upisati [Python](Python.md) izvršni kod
:   8\. [status bar](status_bar/hr.md), ovdje se pojavljuju poruke i pomoćni opisi.
:   9\. Područje pomoćnih opisa , gdje su pomoćni opisi usidreni.
:   10\. [radno okruženjegdje](Std_Workbench.md) odaberete aktivne[Radne ploče](Workbenches/hr.md).
:   11\. [Standardni izbornik](Standard_Menu/hr.md), koji sadrži osnovne operacije programa.

Osnovni koncept FreeCAD sučelja je taj da je podijeljen na [Radne plovršine](workbenches/hr.md). Radna površina je kolekcija alata za specifičnu namjenu, kao rad sa [Poligonalna mreža radna površina](Mesh_Workbench/hr.md),[Crtanje 2D radna površina](Draft_Workbench/hr.md), ili [Skiciraj radna površina](Sketcher_Workbench/hr.md). Možete odabrati aktivnu Radnu površinu sa izbornikom (6). Možete prilagoditi [Postavke sučelja](Interface_Customization/hr.md) uključene u Radnu površinu, dodati alate iz druge Radne površine ili osobno kreiranih alata, koje mi zovemo [Makronaredbe](macros/hr.md). Obično se počinje sa Radnim površinama [Oblikovanje Tijela radna površina](PartDesign_Workbench/hr.md) i [Jednostavno tijelo radna površina](Part_Workbench/hr.md).


<div class="mw-translate-fuzzy">

Kada otvorite FreeCAD prvi puta otvorit če se Start stranica Ovdje je izgled od verzije 0.18:


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Start_center_0.18_screenshot.jpg  style="width:1024px;">


</div>

Start stranica omogućuje brzi prijelaz na uobičajene radne ploče, otvara uobičajeni dokument ili pregled zadnjih vijesti iz FreeCAD svijeta. Vi možete promijeniti početnu radnu ploču u [Uređivač postavki](Preferences_Editor/hr.md).



## Navigacija u 3D prostoru 


<div class="mw-translate-fuzzy">

FreeCAD ima na raspolaganju nekoliko različitih [navigacijski načini](Mouse_navigation.md) koji mijenjaju način na koji miš koristi za interakciju s objektima u 3D prikazu i samom prikazu. Jedan od njih posebno je izrađen za [touchpads](Mouse_navigation#Touchpad_Navigation.md), gdje se ne koristi srednja tipka miša. Sljedeća tablica opisuje zadani način rada, nazvan *\'CAD Navigation\'* (trenutni način navigacije možete brzo promijeniti desnim klikom na prazno područje 3D prikaza):


</div>

Vi imate nekoliko pogleda koji su predefinirani (pogled odozgo, pogled sprijeda itd.) koji se nalaze u izborniku pregleda, a imate i brojevne prečice (**1**, **2**, itd\...). Sa klikom na objekt ili prazno područje sa desnom tipkom miša možete dobiti brzi pristup nekim osnovnim operacijama kao postavljanje pogleda, ili položaj objekta u stablu pregleda.



## Prvi koraci sa FreeCAD-om 


<div class="mw-translate-fuzzy">

Fokus FreeCAD-a vam je omogućiti izradu 3D preciznih 3D modela, strogu kontrolu nad tim modelima (mogućnost vraćanja u povijest modeliranja i izmjenu parametara) i na kraju izradu tih modela (putem 3D ispisa, CNC obrade ili čak gradilišta). Stoga se vrlo razlikuje od nekih drugih 3D aplikacija napravljenih u druge svrhe, poput animacijskog filma ili igranja. Njegova krivulja učenja može biti strma, posebno ako je ovo vaš prvi kontakt s 3D modeliranjem. Ako u nekom trenutku imate poteškoće, nemojte zaboraviti da će vas prijateljska zajednica korisnika na [FreeCAD forumu](http://forum.freecadweb.org/index.php) uspjeti pomoći u bilo kojem trenutku.


</div>

Radna ploča koju ćete početi koristiti u FreeCAD-u ovisi o vrsti posla koji trebate obaviti: Ako radite na mehaničkim modelima ili općenito nekim objektima manjeg opsega, vjerojatno ćete željeti isprobati [Dizajniranje dijelova radna ploča](PartDesign_Workbench/hr.md). Ako radite u 2D-u, prebacite se na [ Nacrt radna ploča](Draft_Workbench/hr.md) ili na [Skiciraj radna ploča](Sketcher_Workbench/hr.md) ako su vam potrebna ograničenja. Ako želite učiniti BIM, pokrenite [Arhitekt radna ploča](Arch_Workbench/hr.md). Ako radite s dizajnom brodova, za vas postoji poseban [Brod radna ploča](Ship_Workbench/hr.md). A ako stižete iz svijeta OpenSCAD, pokušajte [OpenSCAD radna ploča](OpenSCAD_Workbench/hr.md).

Radne ploče možete prebaciti u bilo koje vrijeme i također [Prilagodba sučelja](Interface_Customization/hr.md) svoju omiljenu radnu ploču koristiti za dodavanje alata s drugih radnih ploča.



## Rad sa radnim pločama Dizajniranje dijelova i Skiciraj 

[Dizajniranje dijelova radna ploča](PartDesign_Workbench/hr.md) izrađen je za izgradnju složenih objekata, počevši od jednostavnih oblika, dodajući ili uklanjajući dijelove (zvane \"značajke\"), sve dok ne dođete do vašeg konačnog objekta. Sve značajke koje ste primijenili tijekom postupka modeliranja pohranjuju se u zasebnom prikazu pod nazivom [Prikaz stabla](Document_structure/hr.md), koji sadrži i ostale objekte u vašem dokumentu. Objekt PartDesign (Dizajniranje dijelova) možete smatrati dodavanjem operacija, a svaka se primjenjuje na rezultat prethodnog, tvoreći jedan veliki lanac. U prikazu stabla vidite svoj konačni objekt, ali možete ga proširiti i dohvatiti sva prethodna stanja te promijeniti bilo koji njihov parametar, koji automatski ažurira konačni objekt.

Radna ploča PartDesign (Dizajniranje dijelova) uvelike koristi druge radne ploče, [Skiciraj radna ploča](Sketcher_Workbench/hr.md). Skica omogućuje crtanje dvodimenzionalnih oblika koji su definirani primjenom ograničenja na 2D oblik. Na primjer, možete nacrtati pravokutnik i postaviti veličinu stranice primjenjujući ograničenje duljine na jednu od strana. Ta se strana tada više ne može promijeniti (osim ako se ne promijeni ograničenje).

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

<img alt="" src=images/Partdesign_example.jpg  style="width:600px;">

U bilo kojem trenutku možete odabrati originalne skice i modificirati ih ili promijeniti parametre ekstruzije padova ili džepnih operacija, što će ažurirati konačni objekt.



## Rad s radnim pločama Nacrt i Arhitekt 

[Nacrt](Draft_Workbench/hr.md) i [Arhitekt](Arch_Workbench/hr.md) ponašaju se malo drugačije od ostalih radnih radnih ploča gore, iako slijede ista pravila, koja su zajednička svima FreeCAD-u. Ukratko, dok su Sketcher (Skiciraj) i PartDesign (Dizajniranje dijelova) primarno dizajnirani za pojedinačne komade, Nacrt i Arhitekt su napravljeni da olakšaju vaš rad kada radite s nekoliko jednostavnijih objekata.

[Nacrt radna ploča](Draft_Workbench/hr.md) nudi vam 2D alate pomalo slične onima koje možete pronaći u tradicionalnim 2D CAD aplikacijama, poput [AutoCAD](https://en.wikipedia.org/wiki/AutoCAD). No, 2D nacrt je daleko od dosega FreeCAD-a, nemojte očekivati da će te tamo naći čitav niz alata koje nude ove posvećene aplikacije. Većina alata za nacrte djeluje ne samo u 2D ravnini, već i u cijelom 3D prostoru, a imaju koristi od posebnih pomoćnih sustava kao što su [Označi plohu nacrta](Draft_SelectPlane.md) i [Privuci objekt](Draft_Snap/hr.md).

[Arhitekt](Arch_Workbench/hr.md) dodaje [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) alate FreeCAD, omogućujući vam izgradnju arhitektonskih modela s parametarskim objektima. Arhitekt radna ploča se uvelike oslanja na druge module kao što su Nacrt i Skiciraj. Svi alati za crtanje su također prisutni na Arhitekt radnoj ploči, a većina Arhitekt alata koristi nacrte za pomoćne sustave.

Tipičan tijek rada s Arch ( Arhitekt) i Drafts (Nacrt)radnim pločama može biti:

1.  Nacrtajte nekoliko linija pomoću alata Nacrtaj liniju
2.  Odaberite svaku liniju i pritisnite Zid alat da na svakom od njih izgradite zid
3.  Pridružite zidove tako da ih odaberete i pritisnete alat Arch Add (Arhitekt Dodaj)
4.  Napravite podni objekt i pomičite zidove u njemu s pogleda na Drvo
5.  Napravite građevinski objekt i pomaknite kat u njemu sa stabla
6.  Stvorite prozor klikom na alat Prozor, odaberite postavku na njenoj ploči, a zatim kliknite lice zida
7.  Dodajte dimenzije prvo postavite radnu ravninu ako je potrebno, a zatim pomoću alata Draft Dimension (dimenzija nacrta)

Što vam daje ovo:

<img alt="" src=images/Arch_workflow_example.jpg  style="width:600px;">

Više informacija na stranici [Vježbe](Tutorials/hr.md).



## Dodatci, Makronaredbe i Vanjske radne ploče 


<div class="mw-translate-fuzzy">

Freecad, kao softver otvorenog koda, nudi mogućnost nadopune radnih ploča dodacima.


</div>

Princip [Dodatci](Addon/hr.md) temelji se na razvoju dopuna radne površine. Bilo koji korisnik može razviti funkciju za koju smatra da nedostaje za vlastite potrebe ili, u konačnici, za zajednicu. Pomoću foruma korisnik može zatražiti mišljenje, pomoć na forumu. Može dijeliti, ili ne, objekt svog razvoja prema pravilima o autorskim pravima koje treba definirati. Besplatno njoj / njemu. Kako bi se razvio, korisnik ima na raspolaganju [skripti](scripting/hr.md) funkcije.

Postoje dvije vrste dodataka:

1.  [Makronaredbe](Macros/hr.md): kratki isječci Python koda koji pružaju novi alat ili funkcionalnost. Makronaredbe obično počinju kao način pojednostavljenja ili automatizacije zadatka crtanja ili uređivanja određenog objekta. Ako se mnogo makronaredbi sakuplja unutar mape, cijeli se direktorij može distribuirati kao nova radna ploča.
2.  [Vanjskie radne ploče](External_workbenches/hr.md): zbirka alata programiranih u Pythonu ili C ++ koji na važan način proširuju FreeCAD. Ako je radna ploča dovoljno razvijena i dobro je dokumentirana, može biti uključena kao jedana od osnovnih radnih ploča u FreeCAD. Pod [ Vanjske radne ploče](External_workbenches/hr.md) naći ćete principe i popis postojeće knjižnice.



## Skriptiranje

I na kraju, jedna od najmoćnijih značajki FreeCAD-a je [skriptiranje](scripting/hr.md) okruženje. Iz integrirane python konzole (ili iz bilo koje druge vanjske Python skripte) možete dobiti pristup gotovo bilo kojem dijelu FreeCAD-a, stvoriti ili izmijeniti geometriju, modificirati reprezentaciju tih objekata na 3D sceni ili pristupiti i izmijeniti FreeCAD sučelje. Python skripti mogu se koristiti i u [makronaredbe](macros/hr.md), koje pružaju jednostavan način stvaranja prilagođenih naredbi.



## Šta ima novoga 

-   Pogledajte [Bilješke distribucije](Feature_list/hr#Release_notes.md) za detaljnu listu značajki.





{{Userdocnavi/hr}}



---
⏵ [documentation index](../README.md) > Getting started/hr
