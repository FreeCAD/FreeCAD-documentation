---
- GuiCommand:
   Name: Sketcher Create Ellipse by center
   Icon: Sketcher_CreateEllipse.png
   Workbenches: [Sketcher](Sketcher_Workbench.md)
   MenuLocation: Sketch - Sketcher geometries - Create ellipse by center
   Version: 0.15
   SeeAlso: [Sketcher Ellipse by 3 Points](Sketcher_CreateEllipseBy3Points.md), [Sketcher Circle](Sketcher_CreateCircle.md), [Sketcher Arc of Ellipse](Sketcher_CreateArcOfEllipse.md)
---

# Sketcher CreateEllipseByCenter/ro


</div>



## Descriere

Acest instrument desenează o elipsă prin alegerea a 3 puncte: centrul, sfârșitul semiaxei majore, semiaxa minoră. Când porniți instrumentul, indicatorul mouse-ului se modifică într-o cruce albă cu o pictogramă ca o elipsă roșie. Pe lângă acestea, coordonatele sunt afișate în timp real.

<img alt="" src=images/Sketcher_EllipseExample1.png‎  style="width:500px;"> 
*The sequence of clicks is indicated by yellow arrows with numbers.<br>
C is the center, a the major diameter, b the minor diameter, F1 and F2 are foci.*




<div class="mw-translate-fuzzy">

## Utilizare


</div>


<div class="mw-translate-fuzzy">

-   Apelați comanda făcând clic pe butonul unei bare de instrumente, selectând elementul de meniu sau utilizând comanda rapidă de la tastatură (trebuie să fie atribuită mai întâi în [Interface Customization](Interface_Customization.md)).
-   Primul clic în vizualizarea 3D stabilește centrul de elipsă. Al doilea clic stabilește prima rază/semiaxă și orientarea elipsei. Al treilea clic stabilește cealaltă rază (distanța de la linia definită de primele două clicuri este a doua rază).
-   După al treilea clic, elipsa este creată, împreună cu un set de geometrie de construcție aliniată la ea (diametrul major, diametrul minor, două focare). Geometria construcției poate fi ștearăs manual dacă nu mai este necesară și este recreată mai târziu. A se vedea [Sketcher Show Hide Internal Geometry](Sketcher_RestoreInternalAlignmentGeometry.md).
-   Apăsând **ESC** sau făcând click pe butonul din dreapta al mouse-lui se părăsește această funcție.


</div>

## Peculiarities


<div class="mw-translate-fuzzy">

## Particularități

-   Axele majore și minore ale elipsei sunt stricte și nu pot fi schimbate prin redimensionarea elipselor. Aceasta este o consecință a parametrizării rezolvitorului utilizat (centrul (x, y), focus1 (x, y) și lungimea razei minore (b)) și același comportament strict ca al OpenCascade. Elipsa trebuie rotită pentru a se schimba axele.
-   Elipsa poate funcționa ca un cerc atunci când semiaxele sale majoră și minoră sunt șterse, iar unul dintre focare este constrâns să coincidă cu centrul. Dar constrângerea razei nu va funcționa pe un astfel de cerc.
-   Deplasarea/Mișcarea elipsei prinsă de margine are același rezulta cu mișcarea elipsei având selectat centrul.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseByCenter/ro
