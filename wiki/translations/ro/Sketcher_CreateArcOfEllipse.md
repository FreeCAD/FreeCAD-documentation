---
 GuiCommand:
   Name: Sketcher CreateArcOfEllipse
   Name/ro: Sketcher arc de elipsă
   Workbenches: Sketcher Workbench/ro
   MenuLocation: Sketch , Geometria schitei , Creaţi un arc de elipsă
   Version: 0.15
   SeeAlso: Sketcher CreateEllipseByCenter/ro, Sketcher CompCreateArc/ro
---

# Sketcher CreateArcOfEllipse/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

Acest instrument desenează un arc de elipsă prin alegerea a patru puncte: centrul, sfârșitul semiaxei majore, punctul de început și punctul final. Când porniți instrumentul, indicatorul mouse-ului se modifică într-o cruce albă cu o pictogramă arc de elipsă roșie. Pe lângă acestea, coordonatele sunt afișate în timp real.


</div>

![](images/Sketcher_CreateArcOfEllipse_Example.png ) 
*Arc of ellipse (white) with internal geometry (dark yellow)*




<div class="mw-translate-fuzzy">

## Utilizare


</div>

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


<div class="mw-translate-fuzzy">

-   Apăsați butonul **[<img src=images/Sketcher_CreateArcOfEllipse.png style="width:24px"> '''arc of ellipse'''**.
-   Primul clic în vizualizarea 3D stabilește centrul de elipsă. Al doilea clic definește prima semiaxă și orientarea elipsei. Al treilea clic stabilește cealaltă semiaxă și începutul arcului. Cel de-al patrulea clic stabilește sfârșitul arcului.
-   După al patrulea clic, arcul de elipsă este creat, împreună cu un ansamblu de geometrie a construcției (cu linii albastre) aliniate la el (semiaxă major, semiaxă minor, două focare). Geometria construcției poate fi ștearsă dacă este necesar și este recreată mai târziu. Vezi [Afișează/Ascunde geometria internă](Sketcher_RestoreInternalAlignmentGeometry/ro.md).
-   Apăsați **ESC** sau click dreapta pe butonul mouse-ului pentru abandonarea funcțiie.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Particularități

-   Axele majore și minore ale elipsei subiadiacente sunt stricte și nu pot fi schimbate prin redimensionare. Elipsa de bază trebuie rotită pentru a schimba axele.
-   Spre deosebire de elipsă care poate fi constrânsă să devină un cerc, arcul de elipsă nu poate fi transformat într-un arc de cerc.
-   Mutarea arcului de elipsă facând click pe margine este aceeași cu deplasarea centrului elipsei.


</div>





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfEllipse/ro
