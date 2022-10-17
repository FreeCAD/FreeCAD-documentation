---
- GuiCommand   */ro
   Name   *Part Loft
   Name/ro   *Part Loft
   MenuLocation   *Part → Loft...
|
   Workbenches   *[Part](Part_Workbench/ro.md)
   SeeAlso   *[Part Sweep](Part_Sweep/ro.md)
---

# Part Loft/ro


</div>

## Overview


<div class="mw-translate-fuzzy">

## Prezentare generală 

Instrumentul Loft din Atelierul (Part Workbench) este utilizat pentru a crea o fațetă, o cochilie sau o formă solidă (corp) plecând de la două sau mai multe profiluri. Profilele pot fi un punct (vertex), o linie (margine), o polilinie sau o fațetă. Muchiile și poliliniile pot fi deschise sau închise. Există mai multe limitări și complicații [limitations and complications](Part_Loft#limitations_and_complications.md) , vezi mai jos, însă profilurile pot proveni de la primitivele geometrice din Atelierul Part/Piese, de la funcționalitățile Aelierului Draft Workbench și de la Atelierul Sketch.


</div>


<div class="mw-translate-fuzzy">

Instrumentul Loft are trei parametrii, \"Ruled\",\"Solid\" and \"Closed\" fiecare având câte o valoare sau \"true\" ori \"false\".


</div>


<div class="mw-translate-fuzzy">

Dacă \"Solid\" are valoarea \"true\" FreeCAD creează un solid dacă profilele sunt forme geometrice închise, dacă valorea este \"false\" FreeCAD creează o fațetă sau (dacă are mi mult de o fațetă) o cochilie dacă este un profil închis sau deschis.


</div>


<div class="mw-translate-fuzzy">

Dacă este true\" , \"Ruled\" FreeCAD creează o fațetă, fațetele sau solidele din suprafețele riglate. [Ruled surface page on Wikipedia.](http   *//en.wikipedia.org/wiki/Ruled_surface)


</div>

FreeCAD încearcă să atașeze ultimul profil la primul profil pentru a crea o figură închisă.


<div class="mw-translate-fuzzy">

Pentru mai multe informații supra modului cum profilele sunt legate împreună , referiți-vă la pagina [Part Loft Technical Details](Part_Loft_Technical_Details.md) .


</div>


<div class="mw-translate-fuzzy">

![centre\|Part_Loft. From three profiles which are two Part_Circles and one Part_Ellipse. Parameters are Solid \"True\" and Ruled \"True\"](images/Part_Loft_solid_ruled_from3profiles_example_FreeCAD_0_13.jpg )


</div>

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as profiles and paths. <small>(v0.20)</small> 

## Limitations and complications 


<div class="mw-translate-fuzzy">

## Limitări și complicații 

-   Un vertex sau un punct
    -   vârful sau punctul pot fi utilizate numai ca primul și / sau ultimul profil din lista de profiluri.
        -   De examplu
            -   you cannot loft from a circle to a point, to an ellipse.
            -   However you could Loft from a point to a circle to an ellipse to another point.
-   Open or closed geometry profiles can not be mixed in one single Loft
    -   In one Loft, all profiles (lines wires etc.) must be either open or closed.
        -   De examplu
            -   FreeCAD can not Loft between one Part Circle and one default Part Line.
-   Draft Workbench features
    -   Draft Workbench features can be directly used as a profile in FreeCAD 0.14 or later.
        -   For example the following Draft features can be used as profiles in a Part Loft
            -   Draft Polygon.
            -   Draft Point, Line, wire,
            -   Draft B-spline, Bezier Curve
            -   Draft Circle, Ellipse, Rectangle
-   Schițe PartDesign Sketches
    -   The profile may be created with a sketch. However only a valid sketch will be shown in the list to be available for selection.
    -   The sketch must contain only one open or closed wire or line (can be multiple lines, if those lines are all connected as they are then a single wire)
-   Atelierul Part Workbench
    -   the profile can be a valid Part geometric primitive which can be created with the [Part CreatePrimitives](Part_CreatePrimitives.md) tool
        -   De examplu următoarele primiteve geometrice Part pot fi un profil valid
            -   Punct (Vertex), Linie (Edge)
            -   Elice, Spirală
            -   Cerc, Elipsă
            -   Poligon Regulat
            -   Plan (Fațetă)


</div>


<div class="mw-translate-fuzzy">

-   Closed Lofts
    -   Rezultatele loft-urilor închise pot fi neașteptate - mansarda/loft ul poate dezvolta răsuciri sau deformări. Lofting-ul este foarte sensibil la Plasamentul profilurilor și la complexitatea curbelor necesare pentru conectarea Vârfurilor corespunzătoare în toate profilurile.


</div>

## An example Loft 


<div class="mw-translate-fuzzy">

## Un exemplu de Loft 

Instrumentul Loft este în Atelierul Part Workbench, meniul Part -\> Loft\... sau via iconița din bara de instrumente.


</div>

![](images/Part_Loft_Ikon_Ballon_Hilfe.png )


<div class="mw-translate-fuzzy">

In the \"Tasks\" will be two lists   * \"node / wire\" and \"free form\".


</div>

![](images/Part_Loft_Liste3.png )


<div class="mw-translate-fuzzy">

### Selecția elementelor 

In the \"node / wire\" the available items are displayed. Two elements must be selected one after the first in this list.


</div>

![](images/Part_Loft_Liste_Auswahl_3b.png )


<div class="mw-translate-fuzzy">

Thereafter, with the blue arrow that item is added to the list of \"free form\".


</div>

![](images/Part_Loft_Liste_Auswahl_3c.png )

The selected items must be of the same type.


<div class="mw-translate-fuzzy">

Tip   * the active / selected items in the list are displayed in the 3D area as active / selected.


</div>

### Command complete 


<div class="mw-translate-fuzzy">

### Comanda completă 

Dacă sunt selectate ambele elemente, comanda poate fi completată cu \"OK\".


</div>

![](images/Part_Loft_Liste_Auswahl_3d.png )

### Result


<div class="mw-translate-fuzzy">

## Rezultat

Din liniile închise obținem suprafețe care ar putea fi luate ca un aspect superficial pentru solide.


</div>

![](images/Part_Loft_geschlossen.png )


<div class="mw-translate-fuzzy">

Dacă într-adevăr trebuie să creați un solid, utilizați butonul \"Create Solid\" sau după ce ați creat comutatorul Loft în tab-ul **properties** **data** și setați comutatorul \"Solid\" la True.


</div>

Procedura este aceeași cu cea descrisă mai sus cu polilinii deschise.

### Changing the selection of sections 

If you want to change the selection of the sections after creation of the loft, you can select the field Sections in the Data tab and click the occuring ellipsis button. The list of all selectable sections occurs, the current selection is highlighted. You can remove or add additional sections.

The sequence of sections depends on the sequence of clicks in the list. If you want to make substantial changes it is recommended to first deselect all and then start selection in the right order.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft/ro
