# Manual:Traditional modeling, the CSG way/ro
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC/ro}}

CSG înseamnă Constructive Solid Geometry [Constructive Solid Geometry](https://en.wikipedia.org/wiki/Constructive_solid_geometry)și descrie maniera cea mai simplă de a lucra cu geometria 3D solidă, care creează obiecte complexe prin adăugarea/eliminarea unor elemente de volum prin utilizarea operațiilor booleene cum ar fi unirea, scăderea sau intersecția solidelor.


<div class="mw-translate-fuzzy">

FreeCAD poate gestiona multe tipuri de geometrie, dar tipul preferat și mai util de obiecte 3D pe care dorim să-l proiectăm cu FreeCAD, adică obiecte din lumea reală, este fără îndoială , solid,[BREP](https://en.wikipedia.org/wiki/Boundary_representation) geometry, geometria BREP, care în mod principal sprijinită de către atelierul Part [Part Workbench](Part_Workbench.md). Contrar la plasele cu ochiuri poligonale [polygon meshes](https://en.wikipedia.org/wiki/Polygon_mesh), care sunt realizate numai din puncte și triunghiuri, obiectele BREP(B-Rep de la Boundary Representation) au fațetele lor definite de curbe matematice, care permit o precizie absolută, indiferent de scală.


</div>

![](images/Mesh_vs_brep.jpg )

Diferența dintre cele două poate fi comparată cu diferența dintre imaginile bitmap și vectori. Ca și în cazul imaginilor bitmap, rețelele poligonale au suprafețele lor curbate împărțite într-o serie de puncte. Dacă o priviți îndeaproape, nu va fi o suprafață curbată, ci o suprafață fațetată. În ambele imagini vectoriale datele B-REP, poziția oricărui punct de pe o curbă nu este stocată în geometrie, ci calculată din voleu, cu precizie exactă.

În FreeCAD, toate geometriile bazate pe BREP sunt tratate de o altă piesă de software open source OpenCasCade, [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology). Interfața principală dintre FreeCAD și kernelul OpenCasCade este Atelierul(Workbench). Majoritatea atelierelor de lucru își construiesc funcționalitatea pe atelierul Part.

Deși alte benzi de lucru oferă adesea instrumente mai avansate pentru a construi și manipula geometria, deoarece acestea manipulează obiecte Part, este foarte util să știm cum funcționează aceste obiecte intern și să poată folosi instrumentele Part deoarece, fiind mai simple, pot foarte des să vă ajute să ocoliți problemele instrumentelor mai inteligente care nu reușesc a rezolva corect aceleași probleme.

Pentru a ilustra lucrul Atelierului, vom folosi acest model, folosind doar operațiunile CSG (cu excepția șuruburilor, pentru care vom folosi unul dintre addon-uri și cotele/dimensiunile pe care se vor vedea în următorul capitol):

![](images/Exercise_table_complete.jpg )


<div class="mw-translate-fuzzy">

hai să cream un nou document (**Ctrl+N** or menu File -\> New Document), comuntați pe Part Workbench și începeți cu primul picior:


</div>

Now we can switch to the Part Workbench and start to create our first table leg.


<div class="mw-translate-fuzzy">

-   Apăsați butonul <img alt="" src=images/Part_Box.png  style="width:16px;"> 
**Cube**
-   Selectați Cube, apoi definiți următoarele proprietăți (în tabul **Data** ):
    -   Lungime: 80mm (or 8cm, or 0.8m, FreeCAD works in any unit)
    -   Lîțime: 80mm
    -   Înălțime: 75cm
-   Duplicați Cube apăsând **Ctrl+C** apoi **Ctrl+V** (sau meniul Edit -\> Copy și Paste)
-   Selectați noul obiect denumit Cube001 care a fost creat
-   Schimbați poziția sa editând proprietățile Placement:
    -   Poziție x: 8mm
    -   Poziție y: 8mm


</div>

Ar trebui să obțineți două cuburi(paralelipipede) distanțate la 8 mm pe axa x și 8 mm pe axa Y:

![](images/Exercise_table_01.jpg )


<div class="mw-translate-fuzzy">

-   Acum puteți extrage unul din celălalt: Selectați-l pe **first** , acesta este unul, care va sta **stay**, apoi , cu tasta CTRL apăsată, selectați pe celălalt the**other** , care va extras/scăzut **subtracted** (ordinea este importantă ) apoi apăsați butonul <img alt="" src=images/Part_Cut.png  style="width:16px;"> **Cut** :


</div>

![](images/Exercise_table_02.jpg )

Observați că obiectul nou creat, numit \"Cut\", conține în continuare cele două cuburi(de fapt paralelipipede) pe care le-am folosit ca operanzi. De fapt, cele două cuburi sunt încă în document, au fost ascunse și grupate sub obiectul Cut din vizualizarea arborescentă. Puteți să le selectați prin extinderea săgeții la obiectul Cut și, dacă doriți, să le readuceți din nou vizibile făcând clic pe ele sau schimbând oricare dintre proprietățile acestora.

You can use Cut -tool and other Boolean tools also through \"Combo view\" with <img alt="" src=images/Part_Boolean.svg  style="width:16px;"> [Boolean](Part_Boolean.md). It gives more explicit but longer way to do it.

-   Acum, să creăm celelalte trei picioare, duplicând cubul de bază 6 de alte ori. Din moment ce este încă copiat, puteți pur și simplu să inserați (Ctrl + V) de 6 ori. Modificați poziția după cum urmează:
    -   Cube002: x: 0, y: 80cm
    -   Cube003: x: 8mm, y: 79.2cm
    -   Cube004: x: 120cm, y: 0
    -   Cube005: x: 119.2cm, y: 8mm
    -   Cube006: x: 120cm, y: 80cm
    -   Cube007: x: 119.2cm, y: 79.2cm

-   Acum hai să facem celelalte trei secțiuni, selectând mai întâi cubul \"gazdă\", apoi cubul care urmează să fie tăiat. Acum avem patru obiecte tăiate:

![](images/Exercise_table_03.jpg )

S-ar fi putut gândi că, în loc să repetăm cubul de bază de șase ori, am putea să repetăm piciorul complet de trei ori. Acest lucru este complet adevărat, ca întotdeauna în FreeCAD, există multe modalități de a obține același rezultat. Acesta este un lucru prețios de reținut, pentru că putem avansa la obiecte mai complexe, unele operații ar putea să nu dea rezultatul corect și adesea trebuie să încercăm alte căi.


<div class="mw-translate-fuzzy">

-   Vom face acum găuri pentru șuruburi, folosind aceeași metodă Cut. Deoarece avem nevoie de 8 găuri, câte două în fiecare picior, putem face ca 8 obiecte să fie scăzute. În schimb, să explorăm alte căi și să facem 4 tuburi, care vor fi refolosite de două picioare. Deci, sa creem tuburi folosind cilindri <img alt="" src=images/Part_Cylinder.png  style="width:16px;"> **Cylinder** tool. Din nou, puteți face una și o duplicați ulterior. Dați tuturor cilindrilor o rază de 6 mm. De data aceasta, va trebui să le rotim, ceea ce se face și prin **Placement** property under the Data tab *(**Note:** change the Axis property*before*setting the Angle, or the rotation will not be applied)*:
    -   Cylinder: height: 130cm, angle: 90°, axis: x:0,y:1, position: x:-10mm, y:40mm, z:72cm
    -   Cylinder001: height: 130cm, angle: 90°, axis: x:0,y:1, position: x:-10mm, y:84cm, z:72cm
    -   Cylinder002: height: 90cm, angle: 90°, axis: x:-1,y:0, position: x:40mm, y:-10mm, z:70cm
    -   Cylinder003: height: 90cm, angle: 90°, axis: x:-1,y:0, position: x:124cm, y:-10mm, z:70cm


</div>

![](images/Exercise_table_04.jpg )

Veți observa că cilindrii sunt mai lungi decât este necesar. Acest lucru se datorează tuturor aplicațiilor 3D bazate pe solid, operațiile booleene în FreeCAD sunt uneori suprasensibile față de situațiile față-pe-față și pot eșua. Făcând acest lucru, ne punem în siguranță.

-   Acum să facem scăderea. Selectați primul picior, apoi, cu CTRL apăsat, selectați unul dintre tuburile care îl lipesc, apăsați butonul **Cut**. Gaura se va face și cilindrul ascuns. Găsiți-l în arborescență prin extinderea piciorului străpuns.
-   Alegeți un alt picior străpuns de acest cilindru ascuns, apoi repetați procesul, de această dată selectând cilindrul din arborescență cu ajutorul Ctrl +, deoarece este ascuns în vizualizarea 3D (puteți, de asemenea, să îl faceți vizibil și să îl selectați în vizualizarea 3D). Repetați acest lucru pentru celelalte picioare până când fiecare are două găuri:

![](images/Exercise_table_05.jpg )

După cum puteți vedea, fiecare picior a devenit o lungă serie de operațiuni. Toate acestea rămân parametrice și puteți schimba setările oricând. În FreeCAD, deseori ne referim la această grămadă ca la \"istorie de modelare\"(sau uneori arborescență construcției), deoarece de fapt are toată istoria operațiunilor pe care le-ați făcut.

O altă particularitate a FreeCAD este cea a conceptului de obiect 3D și a conceptului de operare 3D. au tendința a se contopi în unul și același lucru. Cut(secționare) este în același timp operație și obiectul rezultat al acestei operații. În FreeCAD acest lucru este numit \"funcționalitate/caracteristică\", mai degrabă decât obiect sau operație.

-   Acum să facem blatul al masă, va fi un simplu bloc de lemn, să o facem cu altă **Box** with length: 126cm, width: 86cm, height: 8cm, position: x: 10mm, y: 10mm, z, 67cm. In the **View** tab, puteți să-i dați o culoare frumoasă maro, de lemn, schimbând proprietatea de culoare **Shape Color** :

![](images/Exercise_table_06.jpg )

Observați că, deși picioarele au o grosime de 8 mm, le plasăm la 10 mm distanță, lăsând 2 mm între ele. Acest lucru nu este necesar, desigur, nu se va întâmpla cu masa reală, dar este un lucru obișnuit de făcut în acele fel de modele \"asamblate\", îi ajută pe oameni care privesc la Model să înțeleagă că acestea sunt piese separate, care vor trebui atașate manual mai târziu.

Acum că cele 5 piese ale noastre sunt complete, este un moment potrivit să le oferim nu nume mai potrivit decât \"Cut015\". Dând clic dreapta pe obiectele din vederea arborescentă (or pressing **F2**), le puteți redenumi la ceva mai semnificativ pentru dvs. sau pentru altcineva care va deschide fișierul dvs. mai târziu. Se spune adesea că numirea obiectelor dvs. este mult mai importantă decât modelarea lor.


<div class="mw-translate-fuzzy">

-   Vom plasa acum niște șuruburi. În prezent există un addon extrem de util dezvoltat de un membru al comunității FreeCAD, pe care îl puteți găsi pe[FreeCAD addons](https://github.com/FreeCAD/FreeCAD-addons) repository, numit [Fasteners](https://github.com/shaise/FreeCAD_FastenersWB), care face inserarea șuruburilor foarte ușoară. Instalarea de ateliere suplimentare este ușoară și este descrisă în paginile addons.
-   Odată ce ați instalat Fasteners Workbench și ați repornit FreeCAD, acesta va apărea în lista de biblioteci de lucru și putem trece la acesta. Adăugarea unui șurub la unul dintre găurile noastre se face prin conturul/inelul găurii:


</div>

![](images/Exercise_table_07.jpg )

-   Apoi, putem apăsa unul dintre șuruburile Fasteners Workbench, de exemplu **EN 1665 Hexagon bolt with flanges, heavy series**. Șurubul va fi plasat și aliniat cu gaura noastră, iar diametrul va fi selectat pentru a se potrivi cu dimensiunea găurii noastre. Uneori, șurubul va fi plasat inversat, pe care îl putem corecta inversând sensul său . De asemenea, putem seta decalajul/offset-ul la 2mm, pentru a respecta aceeași regulă pe care am folosit-o între blatul mesei și picioare:

![](images/Exercise_table_08.jpg )

-   Repetați acest lucru pentru toate găurile, iar masa noastră este completă!

**The internal structure of Part objects**

După cum am văzut mai sus, este posibil ca FreeCAD să selecteze nu numai obiecte întregi, ci și părți ale acestora, cum ar fi conturul circular al găurii noastre de șurub. Acesta este un moment bun pentru a avea o privire rapidă asupra modului în care sunt construite obiecte Part în interior. Fiecare atelier de lucru care produce geometria pieselor se va baza pe acestea:

-   **Vertices**: Acestea sunt puncte (usually endpoints) pe care se construiește restul. De exemplu, o linie are două vortexuri/vârfuri.
-   **Edges**: muchiile sunt forme geometrice liniare ca linii, arcuri, elipse sau curbe B-spline [NURBS](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline) De obicei, acestea au două vârfuri, dar în unele cazuri speciale au doar unul (de exemplu, un cerc închis).
-   **Wires**: O polilinie este o secvență de muchii conectae la punctele lor de capăt. Pot conține muchii de orice tip, și pot fi deschise sau închise.
-   **Faces**: Fațetele pot fi plane sau curbe și pot fi formate de o polilinie inchisă, care formează marginile unei fațete, sau a multora în cazul în care fațeta are găuri.
-   **Shells**: Cochilie este un simplu grup de fațete conectaea prin muchiile lor. Poate fi deschis sau închis.
-   **Solids**: Atunci când o cochilie este închisă bine, adică nu are \"scurgeri\", devine solid. Solidul poartă noțiunea de interior și exterior. Multe ateliere de lucru se bazează pe acest lucru pentru a se asigura că obiectele pe care le produc pot fi construite în lumea reală.
-   **Compounds**: Compușii sunt pur și simplu agregate de alte forme, indiferent de tipul lor, într-o singură formă.

În vizualizarea 3D, puteți selecta **vertices**, **edges** or **faces**. individuale. Selectarea unuia dintre acestea selectează de asemenea întregul obiect.

**A note about shared design**

S-ar putea să vă uitați la masa de mai sus și să vă gândiți că designul său nu este bun. Strângerea picioarelor cu blatul este probabil prea slabă. S-ar putea să doriți să adăugați bucăți de armare sau pur și simplu aveți alte idei pentru a o face mai bună. Acesta este locul în care partajarea devine interesantă. Puteți descărca fișierul realizat în timpul acestui exercițiu de la linkul de mai jos și îl puteți modifica pentru al face mai bine. Apoi, dacă împărțiți acest fișier îmbunătățit, alții ar putea să o facă chiar mai bine sau să utilizeze masa bine proiectată în proiectele lor. Designul tău ar putea da alte idei altor oameni și poate că ai fi ajutat un pic pentru a face o lume mai bună \...

**Downloads**

-   Fișierul produs în acest exercițiu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/table.FCStd>

**De citit în plus**


<div class="mw-translate-fuzzy">

-   [The Part Workbench](Part_Workbench.md)
-   [The FreeCAD addons repository](https://github.com/FreeCAD/FreeCAD-addons)
-   [The Fasteners Workbench](https://github.com/shaise/FreeCAD_FastenersWB)


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Traditional modeling, the CSG way/ro
