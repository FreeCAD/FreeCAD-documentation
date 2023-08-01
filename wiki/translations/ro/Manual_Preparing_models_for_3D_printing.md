# Manual:Preparing models for 3D printing/ro
{{Manual:TOC/ro}}

Una dintre principalele utilizări ale FreeCAD este de a produce obiecte în lumea reală. Acestea pot fi proiectate în FreeCAD și apoi materializat în diferite moduri, cum ar fi cele comunicarea altor persoane care le vor construi sau, tot mai des, trimise direct la o [3D printer](https://en.wikipedia.org/wiki/3D_printing) sau la o [CNC mill](https://en.wikipedia.org/wiki/Milling_%28machining%29). Capitolul său vă va arăta cum să vă pregătiți modelele pentru a le trimite la aceste mașini-unelte.

Dacă ați fost prudenți în timpul modelării, cea mai mare parte a dificultăților întâmpinate la imprimarea modelului dvs. în 3D a fost deja evitată. Aceasta implică în principiu:


<div class="mw-translate-fuzzy">

-   Asigurarea că obiectele dvs sunt **solid**. obiectele din lumea reală sunt solide ( sau cel puțin cochilii), modelul 3D trebuie să fie și solid. Am văzut în capitolele anterioare că FreeCAD vă ajută foarte mult în această privință, și că [PartDesign Workbench](PartDesign_Workbench.md) vă va anunța dacă efectuați o operație care împiedică modelul să rămână solid. Atelierul [Part Workbench](Part_Workbench.md) conține de asemenea uin instrument <img alt="" src=images/Part_CheckGeometry.png  style="width:16px;"> [Check Geometry](Part_CheckGeometry.md) care este util pentru a verifica în continuare posibilele defecte.
-   Asigurați-vă de unitățile de măsură folosite la cotele/ **dimensiunile** obiectului dvs. Un milimetru în desen va fi un milimetru în viața reală. Fiecare cotă/dimensiune are importanță.
-   Controlarea **degradării**. Nicio imprimantă 3D sau sistem de frezare CNC nu poate prelua direct fișierele FreeCAD. Multe dintre ele vor înțelege doar limbajul mașină numit [G-Code](https://en.wikipedia.org/wiki/G-code). Codul G are zeci de dialecte diferite, fiecare mașină sau vânzător de mașini are de obicei propria sa variantă. Conversia modelelor dvs. în G-Code poate fi ușoară și automată, dar o puteți face și manual, cu un control total asupra ieșirii. În orice caz, o anumită pierdere a calității modelului dvs. va apărea în mod inevitabil în timpul procesului. Când printați în 3D, trebuie să vă asigurați întotdeauna că această pierdere de calitate rămâne sub exigențile dvs. minime.


</div>

Mai jos, vom presupune că sunt îndeplinite primele două criterii și că până acum puteți produce obiecte solide cu dimensiuni corecte. Vom vedea acum cum să abordăm al treilea punct.

### Exportarea feliilor 

Aceasta este metoda cea mai frecvent utilizată pentru tipărirea 3D. Obiectul 3D este exportat către un alt program (dispozitivul de feliere), care va genera codul G de la obiect, prin împărțirea acestuia în straturi subțiri (de aici numele), care vor reproduce mișcările pe care le va face imprimanta 3D. Deoarece multe dintre aceste imprimante sunt construite acasă, există adesea diferențe mici de la una la alta. Aceste programe oferă de obicei posibilități avansate de configurare care vă permit să adaptați ieșirea exact pentru caracteristicile imprimantei 3D.

De fapt Imprimarea 3D este, totuși, un subiect prea vast pentru acest manual. Dar vom vedea cum să exportați și să utilizați acești sliceri pentru a verifica dacă output-ul este corectă.

Conversia obiectelor în ochiuri de plase

Niciunul dintre sliceri nu va prelua, în acest moment, o geometrie solidă pe măsură ce o producem în FreeCAD. Așa că va trebui să convertim pentru început orice obiect pe care dorim să-l tipărim 3 D într-o plasă [mesh](https://en.wikipedia.org/wiki/Polygon_mesh), pe care se poate deschide feliatorul. Din fericire, transformarea unei rețele într-un solid nu este o operație complicată, dimpotrivă, transformarea unui solid într-o rețea, este foarte simplă. Tot ce trebuie, este să fim atenți, pentru că se va produce degradarea menționată mai sus. Trebuie să verificăm dacă degradarea rămâne în limite acceptabile.


<div class="mw-translate-fuzzy">

Toate manipulările cu plase, în FreeCAD, sunt realizate de un alt atelier de lucru specific [Mesh Workbench](Mesh_Workbench.md). Ace3st atelier conține, în plus față de cele mai importante instrumente care fac conversia între obeicte Part și obeicte Mesh, mai multe utilitare sunt menite să analizeze și să repare ochiurile. Deși lucrul cu ochiurile nu este în centrul FreeCAD, atunci când lucrați cu modelarea 3D, adesea trebuie să vă ocupați cu obiecte tip plasă, deoarece utilizarea lor este foarte răspândită printre alte aplicații. Acest atelier de lucru vă permite să le gestionați pe deplin în FreeCAD.


</div>


<div class="mw-translate-fuzzy">

-   Să transformăm unul dintre obiectele pe care le modelam în capitolele anterioare, cum ar fi piesa lego (care poate fi descărcată de la sfârșitul capitolului precedent).
-   Deschideți fișierul FreeCAD care conține piesa Lego.
-   comutați pe atelierul [Mesh Workbench](Mesh_Workbench.md)
-   Selectați piesa lego
-   Selectați meniul **Meshes -\> Create Mesh from Shape**
-   Se deschide un panou de sarcini cu mai multe opțiuni. Unii algoritmi suplimentari de plasă (Mefisto sau Netgen) pot să nu fie disponibili, în funcție de modul în care a fost compilată versiunea FreeCAD. Algoritmul standard al plaselor va fi întotdeauna prezent. Acesta oferă mai puține posibilități decât celelalte două, dar este suficient pentru obiecte mai mici decât dimensiunea maximă de imprimare a unei imprimante 3D.


</div>

![](images/Exercise_meshing_01.jpg )


<div class="mw-translate-fuzzy">

-   Selectați plasa/rețeaua de discretizare **Standard** și lăsați valoarea deviației la valoarea implicită de **0.10**. Apăsați **Ok**.
-   Se va crea un obiect de plasă, exact peste obiectul nostru solid. Pentru a compara cele două, puteți ascunde solidul sau să mutați unul dintre obiecte în raport cu celălalt.
-   Schimbați proprietatea **View -\> Display Mode** o noiului obiect plasă în **Flat Lines**, pentru a vedea cum a apărut triangularea.
-   Dacă nu sunteți fericit și credeți că rezultatul este prea grosier, puteți repeta operația, scăzând valoarea deviației. În exemplul de mai jos, rețeaua stângă a folosit valoarea implicită de**0.10**, while the right one uses **0.01**:


</div>

![](images/Exercise_meshing_02.jpg )

În cele mai multe cazuri, însă, valorile implicite vor da un rezultat satisfăcător.


<div class="mw-translate-fuzzy">

-   Acum putem exporta plasa noastră într-un format tip medh, ca de exemplu [STL](https://en.wikipedia.org/wiki/STL_%28file_format%29), care este în prezent cel mai utilizat format în imprimarea 3D, folosind meniul**File -\> Export** și alegerea formatului de fișier STL.


</div>

Dacă nu dețineți o imprimantă, este de obicei foarte ușor să găsiți servicii comerciale care vă vor tipări și trimite prin poștă. Printre cele celebre sunt [Shapeways](http://www.shapeways.com/) și [Sculpteo](http://www.sculpteo.com/), dar veți găsi, de obicei, alții în orașul dvs. În toate orașele mari, veți găsi astăzi [Fab labs](https://en.wikipedia.org/wiki/Fab_lab), care sunt ateliere echipate cu o gamă de mașini de producție 3D, aproape întotdeauna au cel puțin o imprimantă 3D. Laboratoarele Fab sunt, de obicei, spații comunitare, care vor fi utilizate pentru mașinile lor, contra cost sau gratuit, în funcție de laboratorul Fab, dar vă vor învăța cum să utilizați și să promovați alte activități în jurul producției 3D.

### Utilizare Slic3r 

[Slic3r](http://slic3r.org/) este o aplicație care convertește obiectele STL în cod G care poate fi trimise direct la imprimante 3D. Ca și FreeCAD, acesta este gratuit, open source și rulează pe Windows, Mac OS și Linux. Configurarea corectă a lucrurilor pentru imprimarea 3D este un proces complicat, în care trebuie să aveți o bună cunoaștere a imprimantei dvs. 3D, deci nu este foarte util să generați codul G înainte de a merge la printat (codul dvs G ar putea să nu meargă pe o altă imprimantă), dar este oricum util pentru a verifica dacă fișierul nostru va fi printabil fără probleme.

Acesta este fișierul nostru exportat STL deschis în Slic3r. Prin utilizarea funcției **preview** tab, și deplasând cursorul din dreapta, putem vizualiza calea pe care urmează să o urmeze imprimanta 3D.

![](images/Exercise_meshing_03.jpg )


<div class="mw-translate-fuzzy">

### Utilizarea addon Cura 

Atenție: addon Cura nu este deocamdată funcțional pentru FreeCAD 0.17!


</div>

[Cura](https://ultimaker.com/en/products/cura-software) este o altă aplicație gratuită și open source pentru Windows, Mac și Linux [Ultimaker](https://ultimaker.com). Unii utilizatori FreeCAD au creat un plugin [Cura Workbench](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin) care utilizează Cura intern. Atelierul Curaeste disponibil de la depozitul [FreeCAD addons](https://github.com/FreeCAD/FreeCAD-addons) . Pentru a utiliza Cura Workbench, trebuie să instalați și Cura, care nu este inclusă în atelierul de lucru.

Odată ce ați instalat atât Cura, cât și atelierul Cura, le veți putea utiliza pentru a produce fișierul cu cod G direct de la obiecte Part, fără a fi nevoie să le convertiți în ochiuri de plasă și fără a fi nevoie să deschideți o aplicație externă. Producerea altui fișier G-cod din caramida Lego, folosind de data aceasta Atelierul Cura Workbench , se derulează după cum urmează:


<div class="mw-translate-fuzzy">

-   Încărcați fișierul care conține caramida Lego (poate fi descărcat de la sfârșitul capitolului precedent)
-   Mergeți în atelierul [Cura Workbench](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   Configurați spațiul de lucru al imprimantei și selectați meniul **3D printing -\> Create a 3D printer definition**. Din moment ce nu vom imprima in mod real, vom folosi parametrii asa cum sunt. Geometria spațiului de imprimare și spațiul disponibil vor fi afișate în vizualizarea 3D.
-   Deplasați caramida Lego într-o locație potrivită, cum ar fi centrul patului de imprimare. Rețineți că obiectele PartDesign nu pot fi mutate direct, deci trebuie să mutați prima schiță (primul dreptunghi) sau să mutați (și imprimați) o copie, care poate fi făcută cu instrumentul [Part -\> Create Simple Copy](Part_SimpleCopy.md). copia poate fi mutată, de exemplu cu <img alt="" src=images/Draft_Move.png  style="width:16px;"> [Draft -\> Move](Draft_Move.md).
-   Selectați obiectul de printat, și selectați meniul **3D printing -\> Slice with Cura Engine**.
-   În panoul de activități care se va deschide, asigurați-vă că calea către executabilul Cura este definită corect. Din moment ce nu vom imprima cu adevărat, putem lăsa toate celelalte opțiuni așa cum sunt.Apăsați **Ok**. Două fișiere for fi generate în același director ca fișierul dvs FreeCAD, un fișier STL și un fișier G-code.


</div>

![](images/Exercise_meshing_05.jpg )

-   Codul G generat poate fi, de asemenea, reimportat în FreeCAD (utilizând postprocesorul slic3r ) pentru verificare.


<div class="mw-translate-fuzzy">

### Generarea codulului G-code 

 Atenție:Această secțiune a fost făcută pentru FreeCAD 0.16. Au fost făcute schimbări semnificative în crearea căii. Consultați documentația [Path workbench](Path_Workbench.md) in general sau tutorialul ca [path walk-through](Path_Walkthrough_for_the_Impatient.md)!


</div>

FreeCAD oferă, de asemenea, metode avansate de generare directă a codului G. Acest lucru este mult mai complicat decât utilizarea instrumentelor automate. Acest lucru nu este de obicei necesar atunci când se utilizează imprimante 3D, dar devine foarte important atunci când se lucrează cu frezarea CNC, deoarece mașinile-unelte sunt mult mai complexe.

Generarea de cale G-code în FreeCAD se face cu [Path Workbench](Path_Workbench.md). Dispune de instrumente care generează traiectorii complete de mașină și altele care pot fi doar părți dintr-un proiect G-code, care poate fi apoi asamblat pentru a forma o întreagă operație de frezare.

Generarea traiectoriilor de frezare CNC este un alt subiect care este mult prea vast pentru a fi tratat în acest manual, așa că vom arăta cum să construim un proiect cu Traiectorie simplă, fără a avea grijă de multe detalii ale prelucrării CNC reale.


<div class="mw-translate-fuzzy">

-   Încarcă fișierul care conține lego-ul nostru [Path Workbench](Path_Workbench.md).
-   Deoarece piesa finală nu mai conține o fațetă de sus dreptunghiulară, ascundeți ultimul picior al piesei lego și arătați primul bloc paralelipipedic pe care l-am făcut, care are o față de sus dreptunghiulară.
-   Selectați fațeta de sus și apăsați butonul <img alt="" src=images/Path_Profile.svg  style="width:16px;"> [Profile](Path_Profile.md) .
-   Set its **Offset** property to 1mm.


</div>

![](images/Exercise_path_01.jpg )


<div class="mw-translate-fuzzy">

-   Apoi, să duplicăm această primă buclă de câteva ori, așa că instrumentul va scoate întregul bloc. Selectați calea FaceProfile și apăsați pe butonul<img alt="" src=images/Path_Array.png  style="width:16px;"> [Array](Path_Array.md).
-   Setați proprietățile **Copies** a matricei liniare la 8 , și **Offset** la -2mm in direcția Z, și mutați poziția matricei liniare cu 2 mm în direcția Z, astfel încât tăierea va începe puțin peste bloc și va include și înălțimea bosajelor.


</div>

![](images/Exercise_path_02.jpg )


<div class="mw-translate-fuzzy">

-   Acum avem o traiectorie de preucrare care, urmată de mașina de frezat, va sculpta un volum dreptunghiular dintr-un bloc de material. Acum trebuie să excavăm spațiul dintre bosaje, pentru a le dezvălui. Ascundeți blocul și arătați din nou piesa finală, pentru a putea face diferența între bosaje.
-   Selectați fața superioară și apăsați butonul <img alt="" src=images/Path_Pocket_Shape.svg  style="width:16px;"> [Pocket Shape](Path_Pocket_Shape.md) . Reglați proprietatea **Offset** la 1mm, și retracția **retraction height** la 20mm. That is the height to where the cutter will travel when switching from one loop to another. Otherwise, the cutter might cut right through one of our dots:Aceasta este înălțimea unde se află freza. În caz contrar, tăietorul ar putea fi trece direct prin unul dintre bosajel noastre:


</div>

![](images/Exercise_path_03.jpg )


<div class="mw-translate-fuzzy">

-   Încă o dată faceți o matrice. Selectați obiectul FacePocket, și apăsați butonul <img alt="" src=images/Path_Array.png  style="width:16px;"> [Array](Path_Array.md). reglați numărul *Copies**la 1 și**offset*\' la -2mm in direcția Z . Deplasați poziționarea matricei cu 2 mm în direcția Z. Cele două operațiuni se fac acum:


</div>

![](images/Exercise_path_04.jpg )


<div class="mw-translate-fuzzy">

-   Acum, tot ce a rămas de făcut este să unească aceste două operațiuni într-una singură. Acest lucru se poate face cu o [Path Job](Path_Job.md). Apăsați pe butonul <img alt="" src=images/Path_Job.svg  style="width:16px;"> [Job](Path_Job.md).
-   Definiți proprietatea **Use Placements** a proiectului ca fiind True, deoarece am schimbat poziția matriceelor și dorim ca aceasta să fie luate în considerare în proiect.
-   În vizualizarea arborescentă, glisați și fixați cele două matrice în proiect. Puteți reordona elementele matricii din interiorul proiectului dacă este necesar, făcând dublu clic pe el.
-   Acum, proiectul poate fi exportat la codul G, prin selectarea acestuia, alegeți meniului **File -\> Export**, selectați formatului de cod G și în dialogul pop-up care se va deschide, selectați un postprocesor de script în funcție de aparatul dvs.


</div>

Există numeroase aplicații disponibile pentru a simula uzinarea reală, una dintre acestea este de asemenea open source și multiplatformă, ca și FreeCAD, [Camotics](http://camotics.org/).

**Fişiere de descărcat**

-   Fișierul STL generează în acest exercițiu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.stl>
-   fișierul generat pe durata acestui exercițiu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/path.FCStd>
-   Fișierul G-code generat în acest exercițiu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.gcode>

**De citit în plus**


<div class="mw-translate-fuzzy">

-   [The Mesh Workbench](Mesh_Workbench.md)
-   [The STL file format](https://en.wikipedia.org/wiki/STL_%28file_format%29)
-   [Slic3r](http://slic3r.org/)
-   [Cura](https://ultimaker.com/en/products/cura-software)
-   [The Cura Workbench](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   [The Path Workbench](Path_Workbench.md)
-   [Camotics](http://camotics.org/)


</div>

### Videos

-   [How To Use FreeCAD For 3D Printing \| Using The Realthunder Branch](https://www.youtube.com/playlist?list=PL6Fiih6ItYsWCE20KtUJYpiDPrCA2rVpN) A video playlist by Maker Tales about how to use FreeCAD for 3D printing.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Category_Path.md) > [Mesh](Category_Mesh.md) > [Tutorials](Category_Tutorials.md) > Manual:Preparing models for 3D printing/ro
