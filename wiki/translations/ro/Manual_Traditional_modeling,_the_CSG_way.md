# Manual:Traditional modeling, the CSG way/ro
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC}}


<div class="mw-translate-fuzzy">

CSG înseamnă Constructive Solid Geometry [Constructive Solid Geometry](https://en.wikipedia.org/wiki/Constructive_solid_geometry)și descrie maniera cea mai simplă de a lucra cu geometria 3D solidă, care creează obiecte complexe prin adăugarea/eliminarea unor elemente de volum prin utilizarea operațiilor booleene cum ar fi unirea, scăderea sau intersecția solidelor.


</div>


<div class="mw-translate-fuzzy">

FreeCAD poate gestiona multe tipuri de geometrie, dar tipul preferat și mai util de obiecte 3D pe care dorim să-l proiectăm cu FreeCAD, adică obiecte din lumea reală, este fără îndoială , solid,[BREP](https://en.wikipedia.org/wiki/Boundary_representation) geometry, geometria BREP, care în mod principal sprijinită de către atelierul Part [Part Workbench](Part_Workbench.md). Contrar la plasele cu ochiuri poligonale [polygon meshes](https://en.wikipedia.org/wiki/Polygon_mesh), care sunt realizate numai din puncte și triunghiuri, obiectele BREP(B-Rep de la Boundary Representation) au fațetele lor definite de curbe matematice, care permit o precizie absolută, indiferent de scală.


</div>


<div class="mw-translate-fuzzy">

![](images/Mesh_vs_brep.jpg )


</div>


<div class="mw-translate-fuzzy">

Diferența dintre cele două poate fi comparată cu diferența dintre imaginile bitmap și vectori. Ca și în cazul imaginilor bitmap, rețelele poligonale au suprafețele lor curbate împărțite într-o serie de puncte. Dacă o priviți îndeaproape, nu va fi o suprafață curbată, ci o suprafață fațetată. În ambele imagini vectoriale datele B-REP, poziția oricărui punct de pe o curbă nu este stocată în geometrie, ci calculată din voleu, cu precizie exactă.


</div>


<div class="mw-translate-fuzzy">

În FreeCAD, toate geometriile bazate pe BREP sunt tratate de o altă piesă de software open source OpenCasCade, [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology). Interfața principală dintre FreeCAD și kernelul OpenCasCade este Atelierul(Workbench). Majoritatea atelierelor de lucru își construiesc funcționalitatea pe atelierul Part.


</div>

While other workbenches in FreeCAD, such as the Part Design and Surface Workbenches, offer more advanced tools for building and manipulating geometry, they rely on the underlying Part Workbench. Understanding how Part objects work internally and being adept with the basic Part tools is beneficial. Often, these simpler tools can resolve issues that more complex tools may not handle effectively.

![](images/Mesh_vs_brep.jpg )

The difference between the two can be compared to the difference between bitmap and vector images. As with bitmap images, polygon meshes have their curved surfaces divided into a series of points. If you look at it closely or print it very large, you will see not a curved but a faceted surface. In both vector images and BREP data, the position of any point on a curve is not stored in the geometry but calculated on the fly, with exact precision.


<div class="mw-translate-fuzzy">

Pentru a ilustra lucrul Atelierului, vom folosi acest model, folosind doar operațiunile CSG (cu excepția șuruburilor, pentru care vom folosi unul dintre addon-uri și cotele/dimensiunile pe care se vor vedea în următorul capitol):


</div>

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

You can use the Cut tool and other Boolean tools also through \"Combo view\" with <img alt="" src=images/Part_Boolean.svg  style="width:16px;"> [Boolean](Part_Boolean.md). It gives more explicit but longer way to do it.


<div class="mw-translate-fuzzy">

-   Acum, să creăm celelalte trei picioare, duplicând cubul de bază 6 de alte ori. Din moment ce este încă copiat, puteți pur și simplu să inserați (Ctrl + V) de 6 ori. Modificați poziția după cum urmează:
    -   Cube002: x: 0, y: 80cm
    -   Cube003: x: 8mm, y: 79.2cm
    -   Cube004: x: 120cm, y: 0
    -   Cube005: x: 119.2cm, y: 8mm
    -   Cube006: x: 120cm, y: 80cm
    -   Cube007: x: 119.2cm, y: 79.2cm


</div>


<div class="mw-translate-fuzzy">

-   Acum hai să facem celelalte trei secțiuni, selectând mai întâi cubul \"gazdă\", apoi cubul care urmează să fie tăiat. Acum avem patru obiecte tăiate:


</div>

![](images/Exercise_table_03.jpg )


<div class="mw-translate-fuzzy">

S-ar fi putut gândi că, în loc să repetăm cubul de bază de șase ori, am putea să repetăm piciorul complet de trei ori. Acest lucru este complet adevărat, ca întotdeauna în FreeCAD, există multe modalități de a obține același rezultat. Acesta este un lucru prețios de reținut, pentru că putem avansa la obiecte mai complexe, unele operații ar putea să nu dea rezultatul corect și adesea trebuie să încercăm alte căi.


</div>


<div class="mw-translate-fuzzy">

-   Vom face acum găuri pentru șuruburi, folosind aceeași metodă Cut. Deoarece avem nevoie de 8 găuri, câte două în fiecare picior, putem face ca 8 obiecte să fie scăzute. În schimb, să explorăm alte căi și să facem 4 tuburi, care vor fi refolosite de două picioare. Deci, sa creem tuburi folosind cilindri <img alt="" src=images/Part_Cylinder.png  style="width:16px;"> **Cylinder** tool. Din nou, puteți face una și o duplicați ulterior. Dați tuturor cilindrilor o rază de 6 mm. De data aceasta, va trebui să le rotim, ceea ce se face și prin **Placement** property under the Data tab *(**Note:** change the Axis property*before*setting the Angle, or the rotation will not be applied)*:
    -   Cylinder: height: 130cm, angle: 90°, axis: x:0,y:1, position: x:-10mm, y:40mm, z:72cm
    -   Cylinder001: height: 130cm, angle: 90°, axis: x:0,y:1, position: x:-10mm, y:84cm, z:72cm
    -   Cylinder002: height: 90cm, angle: 90°, axis: x:-1,y:0, position: x:40mm, y:-10mm, z:70cm
    -   Cylinder003: height: 90cm, angle: 90°, axis: x:-1,y:0, position: x:124cm, y:-10mm, z:70cm


</div>

![](images/Exercise_table_04.jpg )

Veți observa că cilindrii sunt mai lungi decât este necesar. Acest lucru se datorează tuturor aplicațiilor 3D bazate pe solid, operațiile booleene în FreeCAD sunt uneori suprasensibile față de situațiile față-pe-față și pot eșua. Făcând acest lucru, ne punem în siguranță.


<div class="mw-translate-fuzzy">

-   Acum să facem scăderea. Selectați primul picior, apoi, cu CTRL apăsat, selectați unul dintre tuburile care îl lipesc, apăsați butonul **Cut**. Gaura se va face și cilindrul ascuns. Găsiți-l în arborescență prin extinderea piciorului străpuns.
-   Alegeți un alt picior străpuns de acest cilindru ascuns, apoi repetați procesul, de această dată selectând cilindrul din arborescență cu ajutorul Ctrl +, deoarece este ascuns în vizualizarea 3D (puteți, de asemenea, să îl faceți vizibil și să îl selectați în vizualizarea 3D). Repetați acest lucru pentru celelalte picioare până când fiecare are două găuri:


</div>

![](images/Exercise_table_05.jpg )

După cum puteți vedea, fiecare picior a devenit o lungă serie de operațiuni. Toate acestea rămân parametrice și puteți schimba setările oricând. În FreeCAD, deseori ne referim la această grămadă ca la \"istorie de modelare\"(sau uneori arborescență construcției), deoarece de fapt are toată istoria operațiunilor pe care le-ați făcut.

O altă particularitate a FreeCAD este cea a conceptului de obiect 3D și a conceptului de operare 3D. au tendința a se contopi în unul și același lucru. Cut(secționare) este în același timp operație și obiectul rezultat al acestei operații. În FreeCAD acest lucru este numit \"funcționalitate/caracteristică\", mai degrabă decât obiect sau operație.


<div class="mw-translate-fuzzy">

-   Acum să facem blatul al masă, va fi un simplu bloc de lemn, să o facem cu altă **Box** with length: 126cm, width: 86cm, height: 8cm, position: x: 10mm, y: 10mm, z, 67cm. In the **View** tab, puteți să-i dați o culoare frumoasă maro, de lemn, schimbând proprietatea de culoare **Shape Color** :


</div>

Acum că cele 5 piese ale noastre sunt complete, este un moment potrivit să le oferim nu nume mai potrivit decât \"Cut015\". Dând clic dreapta pe obiectele din vederea arborescentă (or pressing **F2**), le puteți redenumi la ceva mai semnificativ pentru dvs. sau pentru altcineva care va deschide fișierul dvs. mai târziu. Se spune adesea că numirea obiectelor dvs. este mult mai importantă decât modelarea lor.


<div class="mw-translate-fuzzy">

-   Vom plasa acum niște șuruburi. În prezent există un addon extrem de util dezvoltat de un membru al comunității FreeCAD, pe care îl puteți găsi pe[FreeCAD addons](https://github.com/FreeCAD/FreeCAD-addons) repository, numit [Fasteners](https://github.com/shaise/FreeCAD_FastenersWB), care face inserarea șuruburilor foarte ușoară. Instalarea de ateliere suplimentare este ușoară și este descrisă în paginile addons.
-   Odată ce ați instalat Fasteners Workbench și ați repornit FreeCAD, acesta va apărea în lista de biblioteci de lucru și putem trece la acesta. Adăugarea unui șurub la unul dintre găurile noastre se face prin conturul/inelul găurii:


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_table_07.jpg )


</div>


<div class="mw-translate-fuzzy">

-   Apoi, putem apăsa unul dintre șuruburile Fasteners Workbench, de exemplu **EN 1665 Hexagon bolt with flanges, heavy series**. Șurubul va fi plasat și aliniat cu gaura noastră, iar diametrul va fi selectat pentru a se potrivi cu dimensiunea găurii noastre. Uneori, șurubul va fi plasat inversat, pe care îl putem corecta inversând sensul său . De asemenea, putem seta decalajul/offset-ul la 2mm, pentru a respecta aceeași regulă pe care am folosit-o între blatul mesei și picioare:


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_table_08.jpg )


</div>

-   Repetați acest lucru pentru toate găurile, iar masa noastră este completă!


<div class="mw-translate-fuzzy">

**The internal structure of Part objects**


</div>


<div class="mw-translate-fuzzy">

După cum am văzut mai sus, este posibil ca FreeCAD să selecteze nu numai obiecte întregi, ci și părți ale acestora, cum ar fi conturul circular al găurii noastre de șurub. Acesta este un moment bun pentru a avea o privire rapidă asupra modului în care sunt construite obiecte Part în interior. Fiecare atelier de lucru care produce geometria pieselor se va baza pe acestea:


</div>

![](images/Tabble_alternative_complete.png )

**The internal structure of Part objects**

As we saw above, it is possible in FreeCAD to select not only whole objects but parts of them, such as the circular border of our screw hole. This is a good time to have a quick look at how Part objects are constructed internally. Every workbench that produces Part geometry will be based on these:

-   **Vertices**: These are points (usually endpoints) on which all the rest is built. For example, a line has two vertices.
-   **Edges**: the edges are linear geometry like lines, arcs, ellipses or [NURBS](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline) curves. They usually have two vertices, but some special cases have only one (a closed circle for example).
-   **Wires**: A wire is a sequence of edges connected by their endpoints. It can contain edges of any type, and it can be closed or not.
-   **Faces**: Faces can be planar or curved, and can be formed by one closed wire, which forms the border of the face, or more than one, in case the face has holes.
-   **Shells**: Shells are simply a group of faces connected by their edges. It can be open or closed.
-   **Solids**: When a shell is tightly closed, that is, it has no \"leak\", it becomes a solid. Solids carry the notion of inside and outside. Many workbenches rely on this to make sure the objects they produce can be built in the real world.
-   **Compounds**: Compounds are simply aggregates of other shapes, no matter their type, into a single shape.

In the 3D view, you can select individual **vertices**, **edges** or **faces**. Selecting one of these also selects the whole object.

**A note about shared design**


<div class="mw-translate-fuzzy">

S-ar putea să vă uitați la masa de mai sus și să vă gândiți că designul său nu este bun. Strângerea picioarelor cu blatul este probabil prea slabă. S-ar putea să doriți să adăugați bucăți de armare sau pur și simplu aveți alte idei pentru a o face mai bună. Acesta este locul în care partajarea devine interesantă. Puteți descărca fișierul realizat în timpul acestui exercițiu de la linkul de mai jos și îl puteți modifica pentru al face mai bine. Apoi, dacă împărțiți acest fișier îmbunătățit, alții ar putea să o facă chiar mai bine sau să utilizeze masa bine proiectată în proiectele lor. Designul tău ar putea da alte idei altor oameni și poate că ai fi ajutat un pic pentru a face o lume mai bună \...


</div>

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
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Traditional modeling, the CSG way/ro
