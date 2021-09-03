---
- GuiCommand:/ro
   Name:Sketcher CreateArcOfEllipse
   Name/ro:Sketcher arc de elipsă
   Workbenches:[Sketcher](Sketcher_Workbench/ro.md)
   MenuLocation:Sketch → Geometria schitei → Creaţi un arc de elipsă
   Version:0.15
   SeeAlso:[Sketcher elipsă cu centru](Sketcher_CreateEllipseByCenter/ro.md), [Sketcher Arc cu centru](Sketcher_CompCreateArc/ro.md)
---


</div>

## Descriere

Acest instrument desenează un arc de elipsă prin alegerea a patru puncte: centrul, sfârșitul semiaxei majore, punctul de început și punctul final. Când porniți instrumentul, indicatorul mouse-ului se modifică într-o cruce albă cu o pictogramă arc de elipsă roșie. Pe lângă acestea, coordonatele sunt afișate în timp real.

<img alt="" src=images/Sketcher_ArcOfEllipseExample1.png‎  style="width:500px;"> 
*The sequence of clicks is indicated by yellow arrows with numbers. C is the center, a - major diameter, b - minor diameter, F1, F2 are foci.*


<div class="mw-translate-fuzzy">

## Utilizare


</div>


<div class="mw-translate-fuzzy">

-   Apăsați butonul **<img src=images/Sketcher_CreateArcOfEllipse.png style="width:24px"> '''arc of ellipse'''**.
-   Primul clic în vizualizarea 3D stabilește centrul de elipsă. Al doilea clic definește prima semiaxă și orientarea elipsei. Al treilea clic stabilește cealaltă semiaxă și începutul arcului. Cel de-al patrulea clic stabilește sfârșitul arcului.
-   După al patrulea clic, arcul de elipsă este creat, împreună cu un ansamblu de geometrie a construcției (cu linii albastre) aliniate la el (semiaxă major, semiaxă minor, două focare). Geometria construcției poate fi ștearsă dacă este necesar și este recreată mai târziu. Vezi [Constrânge alinierea internă](Sketcher_ConstrainInternalAlignment/ro.md) și [Afișează/Ascunde geometria internă](Sketcher_RestoreInternalAlignmentGeometry/ro.md).
-   Apăsați **ESC** sau click dreapta pe butonul mouse-ului pentru abandonarea funcțiie.


</div>

## Particularități

-   Axele majore și minore ale elipsei subiadiacente sunt stricte și nu pot fi schimbate prin redimensionare. Elipsa de bază trebuie rotită pentru a schimba axele.
-   Spre deosebire de elipsă care poate fi constrânsă să devină un cerc, arcul de elipsă nu poate fi transformat într-un arc de cerc.
-   Mutarea arcului de elipsă facând click pe margine este aceeași cu deplasarea centrului elipsei.





{{Sketcher Tools navi

}}  
