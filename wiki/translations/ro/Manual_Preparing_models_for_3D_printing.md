# Manual:Preparing models for 3D printing/ro
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

Una dintre principalele utilizări ale FreeCAD este de a produce obiecte în lumea reală. Acestea pot fi proiectate în FreeCAD și apoi materializat în diferite moduri, cum ar fi cele comunicarea altor persoane care le vor construi sau, tot mai des, trimise direct la o [3D printer](https://en.wikipedia.org/wiki/3D_printing) sau la o [CNC mill](https://en.wikipedia.org/wiki/Milling_%28machining%29). Capitolul său vă va arăta cum să vă pregătiți modelele pentru a le trimite la aceste mașini-unelte.


</div>


<div class="mw-translate-fuzzy">

Dacă ați fost prudenți în timpul modelării, cea mai mare parte a dificultăților întâmpinate la imprimarea modelului dvs. în 3D a fost deja evitată. Aceasta implică în principiu:


</div>


<div class="mw-translate-fuzzy">

-   Asigurarea că obiectele dvs sunt **solid**. obiectele din lumea reală sunt solide ( sau cel puțin cochilii), modelul 3D trebuie să fie și solid. Am văzut în capitolele anterioare că FreeCAD vă ajută foarte mult în această privință, și că [PartDesign Workbench](PartDesign_Workbench.md) vă va anunța dacă efectuați o operație care împiedică modelul să rămână solid. Atelierul [Part Workbench](Part_Workbench.md) conține de asemenea uin instrument <img alt="" src=images/Part_CheckGeometry.png  style="width:16px;"> [Check Geometry](Part_CheckGeometry.md) care este util pentru a verifica în continuare posibilele defecte.
-   Asigurați-vă de unitățile de măsură folosite la cotele/ **dimensiunile** obiectului dvs. Un milimetru în desen va fi un milimetru în viața reală. Fiecare cotă/dimensiune are importanță.
-   Controlarea **degradării**. Nicio imprimantă 3D sau sistem de frezare CNC nu poate prelua direct fișierele FreeCAD. Multe dintre ele vor înțelege doar limbajul mașină numit [G-Code](https://en.wikipedia.org/wiki/G-code). Codul G are zeci de dialecte diferite, fiecare mașină sau vânzător de mașini are de obicei propria sa variantă. Conversia modelelor dvs. în G-Code poate fi ușoară și automată, dar o puteți face și manual, cu un control total asupra ieșirii. În orice caz, o anumită pierdere a calității modelului dvs. va apărea în mod inevitabil în timpul procesului. Când printați în 3D, trebuie să vă asigurați întotdeauna că această pierdere de calitate rămâne sub exigențile dvs. minime.


</div>

-   **Confirming the Accuracy of Dimensions**: Precision is critical---what you design in FreeCAD will translate directly to real-world measurements. A millimeter in FreeCAD is a millimeter in the physical object, so each dimension must be carefully considered and verified to ensure accuracy.

-   **Managing Degradation**: It\'s important to remember that no 3D printer or CNC mill can directly process FreeCAD files. These machines use G-Code, a machine language with various dialects depending on the machine or vendor. The process of converting your model into G-Code can often be done automatically through slicer software, but you also have the option to do it manually for greater control. However, during this conversion, some loss of detail or quality is inevitable, particularly when converting the model to a mesh format for printing. You must ensure that this degradation remains within acceptable limits and doesn't affect the functionality or appearance of your final object.

-   **Export Format Compatibility**: For 3D printing, STL is the most commonly used format, but it inherently converts your model into a mesh of triangles, which can result in some loss of detail. It's essential to choose the right resolution when exporting to STL, balancing between detail retention and file size. Similarly, for CNC machining, formats like STEP or IGES are preferable as they maintain the original geometric integrity of the design better than STL. Choosing the right format ensures that the conversion to G-Code remains accurate.

-   **Mesh Analysis and Calibration**: Before exporting your model to a slicer or CNC toolpath generator, it's advisable to run a mesh analysis using FreeCAD's [Mesh Workbench](Mesh_Workbench.md) to detect irregularities, non-manifold edges, or other mesh issues that might complicate the manufacturing process. Additionally, even with a perfect model, make sure your 3D printer or CNC machine is properly calibrated (e.g., for bed leveling, stepper motor settings, or extruder configuration) to avoid quality problems in the final product.

In the following sections, we\'ll assume that you\'ve already taken care of creating solid models with the correct dimensions. Our focus will now shift to managing the conversion process to G-Code, ensuring that your model maintains the necessary quality for 3D printing or CNC machining. By addressing these considerations, you\'ll be better equipped to produce successful physical objects directly from your FreeCAD models.



### Exportarea feliilor 


<div class="mw-translate-fuzzy">

Aceasta este metoda cea mai frecvent utilizată pentru tipărirea 3D. Obiectul 3D este exportat către un alt program (dispozitivul de feliere), care va genera codul G de la obiect, prin împărțirea acestuia în straturi subțiri (de aici numele), care vor reproduce mișcările pe care le va face imprimanta 3D. Deoarece multe dintre aceste imprimante sunt construite acasă, există adesea diferențe mici de la una la alta. Aceste programe oferă de obicei posibilități avansate de configurare care vă permit să adaptați ieșirea exact pentru caracteristicile imprimantei 3D.


</div>


<div class="mw-translate-fuzzy">

De fapt Imprimarea 3D este, totuși, un subiect prea vast pentru acest manual. Dar vom vedea cum să exportați și să utilizați acești sliceri pentru a verifica dacă output-ul este corectă.


</div>

Slicers often include additional insights, such as estimating print time, material usage, and cost based on the filament or resin being used. This allows you to make informed decisions about the printing process and tweak settings for efficiency or material conservation. Although the deeper intricacies of 3D printing---such as machine calibration, material selection, and post-processing---are beyond the scope of this guide, we will focus on how to properly export your FreeCAD model and use slicer software to ensure the output is correct and optimized for your specific printer

 Conversia obiectelor în ochiuri de plase


<div class="mw-translate-fuzzy">

Niciunul dintre sliceri nu va prelua, în acest moment, o geometrie solidă pe măsură ce o producem în FreeCAD. Așa că va trebui să convertim pentru început orice obiect pe care dorim să-l tipărim 3 D într-o plasă [mesh](https://en.wikipedia.org/wiki/Polygon_mesh), pe care se poate deschide feliatorul. Din fericire, transformarea unei rețele într-un solid nu este o operație complicată, dimpotrivă, transformarea unui solid într-o rețea, este foarte simplă. Tot ce trebuie, este să fim atenți, pentru că se va produce degradarea menționată mai sus. Trebuie să verificăm dacă degradarea rămâne în limite acceptabile.


</div>


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


<div class="mw-translate-fuzzy">

![](images/Exercise_meshing_01.jpg )


</div>

-   Let\'s convert the Lego piece we created in the last chapter into an STL mesh. The geometry can be downloaded at the end of said chapter.
-   Open the FreeCAD file containing the Lego piece.
-   Switch to the [Mesh Workbench](Mesh_Workbench.md)
-   Select the Lego brick
-   Select menu **Meshes → Create Mesh from Shape**
-   A task panel will open with several options. Some additional meshing algorithms (Mefisto or Netgen) might not be available, depending on how your version of FreeCAD was compiled. The Standard meshing algorithm will always be present. It offers fewer possibilities than the two others, but is totally sufficient for small objects that fit into the maximum print size of a 3D printer.

![](images/FreeCAD_MeshLego.png )


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


<div class="mw-translate-fuzzy">

Dacă nu dețineți o imprimantă, este de obicei foarte ușor să găsiți servicii comerciale care vă vor tipări și trimite prin poștă. Printre cele celebre sunt [Shapeways](http://www.shapeways.com/) și [Sculpteo](http://www.sculpteo.com/), dar veți găsi, de obicei, alții în orașul dvs. În toate orașele mari, veți găsi astăzi [Fab labs](https://en.wikipedia.org/wiki/Fab_lab), care sunt ateliere echipate cu o gamă de mașini de producție 3D, aproape întotdeauna au cel puțin o imprimantă 3D. Laboratoarele Fab sunt, de obicei, spații comunitare, care vor fi utilizate pentru mașinile lor, contra cost sau gratuit, în funcție de laboratorul Fab, dar vă vor învăța cum să utilizați și să promovați alte activități în jurul producției 3D.


</div>




<div class="mw-translate-fuzzy">

### Utilizare Slic3r 


</div>


<div class="mw-translate-fuzzy">

[Slic3r](http://slic3r.org/) este o aplicație care convertește obiectele STL în cod G care poate fi trimise direct la imprimante 3D. Ca și FreeCAD, acesta este gratuit, open source și rulează pe Windows, Mac OS și Linux. Configurarea corectă a lucrurilor pentru imprimarea 3D este un proces complicat, în care trebuie să aveți o bună cunoaștere a imprimantei dvs. 3D, deci nu este foarte util să generați codul G înainte de a merge la printat (codul dvs G ar putea să nu meargă pe o altă imprimantă), dar este oricum util pentru a verifica dacă fișierul nostru va fi printabil fără probleme.


</div>


<div class="mw-translate-fuzzy">

Acesta este fișierul nostru exportat STL deschis în Slic3r. Prin utilizarea funcției **preview** tab, și deplasând cursorul din dreapta, putem vizualiza calea pe care urmează să o urmeze imprimanta 3D.


</div>

This is our exported STL file opened in PrusaSlicer. By just pressing on the **slice** button, the software divides your model into layers, generates the toolpaths for the 3D printer, and applies the necessary speed and temperature settings. It calculates the infill, support structures, and perimeters, then creates the G-code, which contains detailed instructions for the printer. You can preview the sliced model layer by layer, check estimated print time and filament usage, and finally save or send the G-code to your printer for the actual printing process.


<div class="mw-translate-fuzzy">

![](images/Exercise_meshing_03.jpg )


</div>


<div class="mw-translate-fuzzy">

[Cura](https://ultimaker.com/en/products/cura-software) este o altă aplicație gratuită și open source pentru Windows, Mac și Linux [Ultimaker](https://ultimaker.com). Unii utilizatori FreeCAD au creat un plugin [Cura Workbench](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin) care utilizează Cura intern. Atelierul Curaeste disponibil de la depozitul [FreeCAD addons](https://github.com/FreeCAD/FreeCAD-addons) . Pentru a utiliza Cura Workbench, trebuie să instalați și Cura, care nu este inclusă în atelierul de lucru.


</div>

### Generating G-code 


<div class="mw-translate-fuzzy">

FreeCAD oferă, de asemenea, metode avansate de generare directă a codului G. Acest lucru este mult mai complicat decât utilizarea instrumentelor automate. Acest lucru nu este de obicei necesar atunci când se utilizează imprimante 3D, dar devine foarte important atunci când se lucrează cu frezarea CNC, deoarece mașinile-unelte sunt mult mai complexe.


</div>


<div class="mw-translate-fuzzy">

Generarea traiectoriilor de frezare CNC este un alt subiect care este mult prea vast pentru a fi tratat în acest manual, așa că vom arăta cum să construim un proiect cu Traiectorie simplă, fără a avea grijă de multe detalii ale prelucrării CNC reale.


</div>


<div class="mw-translate-fuzzy">

-   Încarcă fișierul care conține lego-ul nostru [Path Workbench](Path_Workbench.md).
-   Deoarece piesa finală nu mai conține o fațetă de sus dreptunghiulară, ascundeți ultimul picior al piesei lego și arătați primul bloc paralelipipedic pe care l-am făcut, care are o față de sus dreptunghiulară.
-   Selectați fațeta de sus și apăsați butonul <img alt="" src=images/Path_Profile.svg  style="width:16px;"> [Profile](Path_Profile.md) .
-   Set its **Offset** property to 1mm.


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_path_01.jpg )


</div>

-   Load the file containing our Lego piece, and switch to the <img alt="" src=images/Workbench_CAM.svg  style="width:16px;"> [CAM Workbench](CAM_Workbench.md).
-   Press on the <img alt="" src=images/CAM_Job.svg  style="width:16px;"> [Job](CAM_Job.md) button and select our lego piece.
-   Since this section doesn't aim to provide an in-depth tutorial of the CAM Workbench, we will be using the default values. If you would like a more detailed tutorial, please refer to [CAM walk-through](CAM_Walkthrough_for_the_Impatient.md). Keep in mind that in the CAM Workbench, a stock body is automatically created around your object, representing the raw material that will be machined. Right now, this stock body extends 1 mm in all directions from the object.

![](images/FreeCAD_CAM1.png )


<div class="mw-translate-fuzzy">

-   Apoi, să duplicăm această primă buclă de câteva ori, așa că instrumentul va scoate întregul bloc. Selectați calea FaceProfile și apăsați pe butonul<img alt="" src=images/Path_Array.png  style="width:16px;"> [Array](Path_Array.md).
-   Setați proprietățile **Copies** a matricei liniare la 8 , și **Offset** la -2mm in direcția Z, și mutați poziția matricei liniare cu 2 mm în direcția Z, astfel încât tăierea va începe puțin peste bloc și va include și înălțimea bosajelor.


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_path_02.jpg )


</div>

![](images/FreeCAD_CAMtree.png )


<div class="mw-translate-fuzzy">

-   Acum avem o traiectorie de preucrare care, urmată de mașina de frezat, va sculpta un volum dreptunghiular dintr-un bloc de material. Acum trebuie să excavăm spațiul dintre bosaje, pentru a le dezvălui. Ascundeți blocul și arătați din nou piesa finală, pentru a putea face diferența între bosaje.
-   Selectați fața superioară și apăsați butonul <img alt="" src=images/Path_Pocket_Shape.svg  style="width:16px;"> [Pocket Shape](Path_Pocket_Shape.md) . Reglați proprietatea **Offset** la 1mm, și retracția **retraction height** la 20mm. That is the height to where the cutter will travel when switching from one loop to another. Otherwise, the cutter might cut right through one of our dots:Aceasta este înălțimea unde se află freza. În caz contrar, tăietorul ar putea fi trece direct prin unul dintre bosajel noastre:


</div>


<div class="mw-translate-fuzzy">

-   Acum, tot ce a rămas de făcut este să unească aceste două operațiuni într-una singură. Acest lucru se poate face cu o [Path Job](Path_Job.md). Apăsați pe butonul <img alt="" src=images/Path_Job.svg  style="width:16px;"> [Job](Path_Job.md).
-   Definiți proprietatea **Use Placements** a proiectului ca fiind True, deoarece am schimbat poziția matriceelor și dorim ca aceasta să fie luate în considerare în proiect.
-   În vizualizarea arborescentă, glisați și fixați cele două matrice în proiect. Puteți reordona elementele matricii din interiorul proiectului dacă este necesar, făcând dublu clic pe el.
-   Acum, proiectul poate fi exportat la codul G, prin selectarea acestuia, alegeți meniului **File -\> Export**, selectați formatului de cod G și în dialogul pop-up care se va deschide, selectați un postprocesor de script în funcție de aparatul dvs.


</div>


<div class="mw-translate-fuzzy">

Există numeroase aplicații disponibile pentru a simula uzinarea reală, una dintre acestea este de asemenea open source și multiplatformă, ca și FreeCAD, [Camotics](http://camotics.org/).


</div>


<div class="mw-translate-fuzzy">

**Fişiere de descărcat**


</div>


<div class="mw-translate-fuzzy">

-   Fișierul STL generează în acest exercițiu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.stl>
-   fișierul generat pe durata acestui exercițiu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/path.FCStd>
-   Fișierul G-code generat în acest exercițiu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.gcode>


</div>


<div class="mw-translate-fuzzy">

**De citit în plus**


</div>

**Downloads**

-   The STL file generated in this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.stl>
-   The file generated during this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/path.FCStd>
-   The G-code file generated in this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.gcode>

**Read more**


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
⏵ [documentation index](../README.md) > [CAM](Category_CAM.md) > [Mesh](Category_Mesh.md) > [Tutorials](Category_Tutorials.md) > Manual:Preparing models for 3D printing/ro
