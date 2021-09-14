# FEM CalculiX Cantilever 3D/ro




<div class="mw-translate-fuzzy">


{{TutorialInfo/ro
|Topic= Finite Element Analysis
|Level= Beginner
|Time= 10 minutes
|Author=[http://www.freecadweb.org/wiki/index.php?title=User:Berndhahnebach Bernd]
|FCVersion=0.16.6377 or above
|Files=
}}


</div>

## Introduction


<div class="mw-translate-fuzzy">

### Introducere

Acest exemplu este menit să arate o analiză simplă a elementelor finite (AEF) în FreeCAD [FEM Workbench](FEM_Workbench.md) ar trebui să arate și modul în care rezultatele pot fi vizualizate. Se arată cum se declanșează o AEF și cum se schimbă valoarea de încărcare și direcția de încărcare. Mai mult, deoarece fișierul exemplu este prevăzut pt orice instalare FreeCAD, este ușor să verificați dacă modulul FEM este configurat corect.


</div>

<img alt="" src=images/FEM_example01_pic00.jpg  style="width:700px;">

## Requirements


<div class="mw-translate-fuzzy">

### Cerințe

-   Versiunea FreeCAD = 0.16.6377 sau mai recentă.
-   Acest lucru poate fi verificat în meniul Ajutor -\> despre FreeCAD. Numărul Reviziei trebuie să fie mai mare de 6377
-   Nu este nevoie de software extern pentru încărcarea fișierului exemplu, vizualizarea plasei cu ochiuri și a geometriei, precum și pentru vizualizarea rezultatelor.
-   Pentru reluarea FEA software-ul rezolvitorul CalculiX trebuie să fie instalat pe calculatorul dumneavoastră. Probabil solverul a fost deja instalat împreună cu FreeCAD. Dacă rezolvitorul CalculiX nu este instalat, consultați [FEM Install](FEM_Install.md).


</div>


<div class="mw-translate-fuzzy">

### Configurarea fișierului exemplu 


</div>

### Load Start Workbench 


<div class="mw-translate-fuzzy">

#### Încarcă Atelierul Start Workbench 

-   Start FreeCAD
-   Atelierul Start Workbench trebuie încărcat


</div>

### Load the example file 


<div class="mw-translate-fuzzy">

#### Încărcați fișierul exemplu 

-   Mergeți la proiectele de exemplu și faceți clic pe \"Încărcați un exemplu de analiză MEF\"
-   Dacă din cauza unor operații ulterioare unele geometrii, constrângeri sau rezultate sunt rupte sau șterse doar repetați pașii de mai sus.


</div>

<img alt="" src=images/FEM_example01_pic01.jpg  style="width:700px;">

### Activate the analysis container 


<div class="mw-translate-fuzzy">

#### Activați containerul de analiză 

-   Pentru a lucra cu o analiză, analiza trebuie activată.
-   În vizualizarea copacului, faceți clic dreapta pe<img alt="" src=images/FEM_Analysis.png  style="width:32px;"> MechanicalAnalysis \--\> Activate analysis


</div>

<img alt="" src=images/FEM_example01_pic02.jpg  style="width:700px;">

### Analysis container and its objects 


<div class="mw-translate-fuzzy">

#### Container de analiză și obiectele sale 

-   Dacă analiza este activată, FreeCAD va schimba bancul de lucru curent cu FEM.
-   Există cel puțin cele 5 obiecte necesare pentru a efectua o analiză mecanică statică.
-   [ 32px](Imagine:_FEM_Analysis.png.md) container de analiză

1.  [ 32px](Imagine:_FEM_Solver.png.md) un solver
2.  [ 32px](Imagine:_FEM_Material.png.md) un material
3.  ![ 32px](images/_FEM_FixedConstraint.png ) o constrângere fixă
4.  ![ 32px](images/_FEM_ForceConstraint.png ) o constrângere de forță
5.  [ 32px](Imagine:_FEM_Create.png.md) FEM mesh

-   Deoarece în exemplul de aici sunt incluse rezultatele și există un al șaselea obiect, rezultatele ![ 16px](images/_FEM_ShowResult.png ).


</div>

### Visualizing Results 


<div class="mw-translate-fuzzy">

#### Vizualizarea rezultatelor 

-   Asigurați-vă că analiza este activată.
-   Asigurați-vă că analiza încă conține obiectul rezultat, dacă nu doar reîncărcați fișierul exemplu.
-   Faceți clic pe bara de instrumente icoanițe pe <img alt="" src=images/FEM_ShowResult.png  style="width:16px;"> [Show result](FEM_ResultShow.md)
-   În fereastra task-ului alege z-Displacement. Acesta arată -88.443 mm în direcție z-negativă.
-   Acest lucru are sens, deoarece forța este în direcția negativă, de asemenea.
-   Activați caseta de selectare în afară de glisorul inferior al afișajului de deplasare.
-   Glisorul poate fi folosit pentru a modifica plasa de deformare într-o manieră simplificată.
-   Alegeți dintre diferitele tipuri de rezultate pentru a le vedea în interfața GUI .


</div>

<img alt="" src=images/FEM_example01_pic03.jpg  style="width:400px;">

### Purging Results 


<div class="mw-translate-fuzzy">

#### Rezultate de curățare 

-   Asigurați-vă că analiza este activată.
-   Pentru a elimina rezultatele selectați în bara de instrumente pictogramă <img alt="" src=images/FEM_PurgeResults.png  style="width:32px;"> [Purge results](FEM_ResultsPurge.md)


</div>

### Running the FEA 


<div class="mw-translate-fuzzy">

#### Rularea FEA 

-   În vizualizarea Tree, faceți dublu clic pe obiectul rezolvitor ![ 32px](images/_FEM_Solver.png ).
-   În fereastra de sarcini a obiectului rezolvitor, asigurați-vă că este selectată analiza statică.
-   Faceți clic pe fișierul .inp de scriere în aceeași fereastră de activitate. Urmăriți fereastra de jurnalizare până când se afișează \"scriere completă\".
-   Faceți clic pe Run CalculiX. Deoarece aceasta este o analiză foarte mică, ar trebui să dureze mai puțin de o secundă pentru a rula.
-   În fereastra de text ar trebui să imprimați cu litere verzi \"CalculiX done!\" iar în linia următoare \"seturile de rezultate de încărcare \...\"
-   Ați terminat prima dvs. AEF în FreeCAD dacă nu a fost nici un mesaj de eroare.
-   Faceți clic pe Închidere în fereastra de activități.
-   Trebuie creat un obiect rezultat nou. Știi deja cum să vizualizați rezultatele.
-   Dacă primiți un mesaj de eroare "no solver binary" sau similar atunci când se declanșează analiza, verificați

[ FEM Install](FEM_Install.md).


</div>

<img alt="" src=images/FEM_example01_pic04.jpg  style="width:400px;">

### Running the FEA the fast Way 


<div class="mw-translate-fuzzy">

#### Rularea AEF pe calea rapidă 

-   În vizualizarea arborescentă selectați obiectul Solver ![ 32px](images/_FEM_Solver.png ) al analizei ![ 32px](images/_FEM_Analysis.png ).
-   În bara de instrumente iconițe faceți clic pe <img alt="" src=images/FEM_RunCalculiXccx.png  style="width:32px;"> [Quick Analysis](FEM_SolverRun.md).
-   Fișierul de intrare Calculix va fi scris, CalculiX va fi declanșat și obiectul rezultat ar trebui să fie creat.


</div>

### Changing Load Direction and Load Value 


<div class="mw-translate-fuzzy">

#### Schimbarea direcției de încărcare și a valorii de încărcare 

-   În vizualizarea arborescentă selectați obiectul mesh FEM ![ 32px](images/_FEM_Create.png ) și apăsați tasta spațiu.
-   Vizibilitatea rețelei FEM va fi oprită. Modelul geometric este încă vizibil.
-   În vizualizarea arborescentă faceți dublu clic pe obiectul de constrângere de forță pentru a deschide fereastra de sarcini.
-   În fereastra de sarcini se modifică valoarea de încărcare la 500000000 N = 500 MN (forța în fereastra de sarcină trebuie să fie în N)
-   Faceți clic pe Button Direction.
-   Pe modelul geometric faceți clic pe muchiile lungi în direcția x.

Săgețile roșii ale forței își vor schimba direcția în direcția x. Ele arată în direcția fixă.

-   Deoarece tensiunea ar trebui să fie aplicată casetei, Direcția inversă trebuie să fie declanșată făcând clic pe ea.

Săgețile roșii ale forței își vor schimba direcția.

-   Faceți clic pe OK în fereastra de activități.

<img alt="" src=images/FEM_example01_pic05.jpg  style="width:700px;">

-   Întoarceți vizibilitatea mesei FEM <img alt="" src=images/FEM_Create.png  style="width:32px;"> pe pagină.
-   Acum știți deja cum să declanșați o analiză și cum să vizualizați rezultatele.

Deformarea în direcția x trebuie să fie de 19,05 mm.


</div>

<img alt="" src=images/FEM_example01_pic05.jpg  style="width:700px;">

-   Toggle the [visibility](Std_ToggleVisibility.md) of the FEM mesh <img alt="" src=images/FEM_FEMMesh.svg  style="width:24px;"> \'On\' by selecting it in tree view and pressing the **Space** key.
-   You know how to trigger an analysis and how to visualize results already.
-   The deformation in x-direction should be 19.05 mm.

<img alt="" src=images/FEM_example01_pic06.jpg  style="width:400px;">

## What next? 


<div class="mw-translate-fuzzy">

#### Ce urmează? 

-   Acum că ați terminat cu fluxul de lucru de bază pentru [FEM Module](FEM_Workbench.md).
-   Sunteți pregătit acum să faceți al doilea [FEM tutorial](FEM_tutorial.md).
-   Vom crea consola CalculiX noi înșine și vom compara rezultatele cu teoria grinzii.


</div>


{{Tutorials navi

}} {{FEM Tools navi}} 
