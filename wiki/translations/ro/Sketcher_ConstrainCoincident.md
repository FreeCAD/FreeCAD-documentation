---
- GuiCommand:/ro
   Name:Sketcher ConstrainCoincident
   Icon:Constraint_PointOnPoint.svg
   Workbenches:[Sketcher](Sketcher_Workbench/ro.md)
   Shortcut:C
   MenuLocation:Sketch → Sketcher constraints → Constrain coincident
   SeeAlso:[Constrain Lock](Sketcher_ConstrainLock/ro.md), [Constrain Point onto Object](Sketcher_ConstrainPointOnObject/ro.md)
---

# Sketcher ConstrainCoincident/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Creați o constrângere de coincidență asupra elementului selectat


</div>

Acest instrument de constrângere ia două puncte ca argument pentru a face ca cele două puncte să *coincident*. (Însemnând să le faceți să devină ca un singur punct).

În termeni practici, acest instrument de constrângere este util atunci când există o ruptură într-un profil, de exemplu - unde două linii se termină aproape una de alta și trebuie să fie unite - o constrângere de coincidență asupra punctelor lor finale va închide spațiul.

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

După cum sa menționat mai sus, acest instrument are două argumente - ambele sunt puncte.

1.  În primul rând este necesar să evidențiem două puncte distincte. (Rețineți că acest lucru nu va funcționa dacă, de exemplu, doriți să selectați punctul inițial și cel final din aceeași linie).
2.  Evidențiarea unui element de desen este realizată prin mutarea mouse-ului peste element și făcând clic pe butonul stânga al mouse-ului.
3.  Un element selectat își va schimba culoarea în verde.
4.  Următoarele elemente pot fi evidențiate prin repetarea procedurilor de mai sus. NOTĂ: Nu este necesar să țineți apăsată o tastă specială, cum ar fi Ctrl, pentru a selecta mai multe elemente dintr-un desen.
5.  Odată ce ați selectat două puncte, faceți clic stânga pe \'PointOnPoint\' <img alt="" src=images/Constraint_PointOnPoint.png  style="width:32px;"> constrângerea va face ca cele două puncte să devină *coincident* și să fie înlocuite de un singur punct.


</div>


<div class="mw-translate-fuzzy">

NOTĂ: Pentru a face două puncte coincide, FreeCAD trebuie să se mute în mod necesar unul sau ambele puncte originale.


</div>

## Alternatives to Coincident constraint 

The two constrained items of a [Coincident](Sketcher_ConstrainCoincident.md) constraint must be start point or end point vertices, or center points of arcs, circles or ellipses. Some combinations which are not possible with a coincident constraint can be emulated using other constraints:

-   The <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [Symmetric](Sketcher_ConstrainSymmetric.md) constraint can be used to place a start point, end point or center point on the midpoint of a straight line.
-   A midpoint-to-midpoint placement of two straight lines can be achieved by creating a new <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:24px;"> [Point](Sketcher_CreatePoint.md) and using two <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [Symmetric](Sketcher_ConstrainSymmetric.md) constraints so that it lies on the midpoint of both lines.
-   A vertex can be constrained to lie along an edge using a <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;">[PointOnObject](Sketcher_ConstrainPointOnObject.md) constraint. Note that with this constraint, the point can lie anywhere on the full extension of a segment or curve (i.e. also before the start point or beyond the end point).
-   A collinear placement of two straight lines can be obtained by applying a <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> [Tangent](Sketcher_ConstrainTangent.md) constraint to them, or by combining a <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [PointOnObject](Sketcher_ConstrainPointOnObject.md) constraint and a <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> [Parallel](Sketcher_ConstrainParallel.md) constraint.
-   Two edges can be made identical by using two <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincident](Sketcher_ConstrainCoincident.md) constraints, one for each pair of extremities.
-   Two circles can be made identical by using a <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincident](Sketcher_ConstrainCoincident.md) constraint to merge the centers, and applying an <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> [Equal](Sketcher_ConstrainEqual.md) constraint to their edges. For arcs, this will ensure both arcs are part of the same circle, while allowing them to have different start and end points.


<div class="mw-translate-fuzzy">

### General scripting 

Constrângerea poate fi creată din macrocomenzi și din consola Python folosind următoarea comandă:


</div>

The constraint can be created from [macros](Macros.md) and from the [Python](Python.md) console by using the following command:


```pythonSketch.addConstraint(Sketcher.Constraint('Coincident',LineFixed,PointOfLineFixed,LineMoving,PointOfLineMoving)) 
```


<div class="mw-translate-fuzzy">

unde :

-   Sketch este un obiect sketch
-   LineFixed este numărul liniei care nu se mișcă prin aplicarea constrângerii
-   PointOfLineFixed este numărul liniei liniei Fixed care trebuie să îndeplinească constrângerea
-   LineMoving este numărul liniei care se va deplasa prin aplicarea constrângerii
-   PointOfLineMoving este numărul liniei este LineMoving, care trebuie să îndeplinească constrângerea


</div>

As the names `LineFixed` and `LineMoving` indicate, if both constrained vertices are free to move in any direction, the first one (first to be selected in the Gui) will remain fixed and the other one will move. In the presence of existing constraints, however, both edges may move.

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `LineFixed`, `PointOfLineFixed`, `LineMoving` and `PointOfLineMoving`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">


</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincident/ro
