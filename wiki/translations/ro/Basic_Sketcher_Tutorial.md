# Basic Sketcher Tutorial/ro
<div class="mw-translate-fuzzy">


{{TutorialInfo/ro
|Topic= Sketcher
|Level= Beginner
|Time= 10 minutes
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
|FCVersion=0.16 or above
|Files=
}}


</div>


<div class="mw-translate-fuzzy">

### Introducere

Acest tutorial are rolul de a introduce cititorul în fluxul de lucru de bază al aplicației [Sketcher Workbench](Sketcher_Workbench.md). Vom crea o schiță similară celei prezentate mai jos.


</div>

This tutorial is meant to introduce the reader to the basic workflow of the <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md).


<div class="mw-translate-fuzzy">

Atelierul de lucru Sketcher există ca modul independent, dar este accesibil și din cadrul [PartDesign Workbench](PartDesign_Workbench.md) atunci când este necesar să creați un **profil**.


</div>

The reader will practice:

-   Creating construction geometry
-   Creating real geometry
-   Applying geometric constraints
-   Applying datum constraints
-   Obtaining a closed profile

For a more in depth description of the sketcher, read the [Sketcher reference](Sketcher_reference.md).

![](images/00_Sk01_Sketcher_fully_constrained_final.png )


<div class="mw-translate-fuzzy">

<img alt="" src=images/Sketcher_tutorial_result.png  style="width:480px;">


</div>


<div class="mw-translate-fuzzy">

### Cerințe

-   Versiunea FreeCAD 0.16 sau mai recentă


</div>

1\. Open FreeCAD, create a new empty document with **File → <img src=images/Std_New.svg style="width:16px"> [New](Std_New.md)**.

:   1.1. Switch to the [Sketcher Workbench](Sketcher_Workbench.md) from the [workbench selector](Std_Workbench.md), or the menu **[View](Std_View_Menu.md) → Workbench → Sketcher**.

Some actions to remember:

-   Press the right mouse button, or press **Esc** in the keyboard once, to deselect the active tool in edit mode.
-   To exit the sketch edit mode, press the **Close** button in the [task panel](task_panel.md), or press **Esc** twice in the keyboard.
-   To enter again edit mode, double click on the sketch in the <img src=images/Sketcher_EditSketch.svg style="width:tree view](tree_view.md), or select it, and then click on **[16px"> [Edit sketch](Sketcher_EditSketch.md)**.


<div class="mw-translate-fuzzy">

### Procedură

#### Crearea unei Sketch 

1.  Creați un nou document
2.  Comutați la Sketcher Workbench utilizând meniul contextual **drop-down menu** sau făcând click pe **View menu \> Workbench \> Sketcher**.
3.  Selectați <img alt="" src=images/Sketcher_NewSketch.png‎‎  style="width:32px;"> [New sketch](Sketcher_NewSketch.md)
4.  Ar trebui să vedeți un dialog care vă solicită să alegeți orientarea schiței și să oferiți o compensare. Nu vom folosi offset și vom folosi planul implicit
5.  Faceți clic pe OK și putem începe să construim schița


</div>

2\. Click on **<img src="images/Sketcher_NewSketch.svg‎‎" width=16px> [New sketch](Sketcher_NewSketch.md)**.

:   2.1. Choose the sketch orientation, that is, one of the base XY, XZ, or YZ planes. Also choose if you want an inverted orientation, and an offset from the base plane.
:   2.2. We will use the default plane and options.
:   2.3. Click **OK** to start constructing the sketch.


<div class="mw-translate-fuzzy">

Suntem acum în mediul Sketcher. În cadrul acestuia, putem folosi majoritatea instrumentelor disponibile în acest atelier de lucru.


</div>


<div class="mw-translate-fuzzy">

In the **Combo View**, expand the option **Edit controls** and make sure **Autoconstraints** are enabled.


</div>

<img alt="" src=images/01_Sk01_Sketcher_Task_panel.png  style="width:" height="400px;">


*Upper part of the [task panel](task_panel.md) of the sketcher.*


<div class="mw-translate-fuzzy">

#### Creating geometry 

##### Sketcher construction geometry 

Construction geometry is used as guides for the creation of complex profiles. To access it, we need to enable \'\'\'Construction mode \'\'\'.


</div>


<div class="mw-translate-fuzzy">

1.  Selectați <img alt="" src=images/Sketcher_ToggleConstruction.png  style="width:32px;"> [Construction Mode](Sketcher_ToggleConstruction.md)
2.  Select <img alt="" src=images/Sketcher_Line.png  style="width:32px;"> [Line by 2 point](Sketcher_CreateLine.md)
3.  Apropiați **origin point** din schiță, punctul ar trebui să evidențieze lângă cursorul această pictogramă <img alt="" src=images/Constraint_PointOnPoint.png  style="width:32px;"> va apărea.
4.  Selectați punctul și extindeți linia în diagonală până la o lungime arbitrară.
5.  Repetați această procedură până când creați cinci linii de **construction**. Asigurați-vă că păstrați-le pe toate diagonale.
6.  Pentru a ieși din modul construcție, doar faceți click din nou pe <img alt="" src=images/Sketcher_ToggleConstruction.png  style="width:32px;"> [Construction Mode](Sketcher_ToggleConstruction.md)


</div>


**Note:**

up to this point the [line tool](Sketcher_CreateLine.md) is still active. This means we can keep clicking on the [3D view](3D_view.md) to draw as many lines as we want. If we wish to exit this tool, we can press the right mouse button, or press **Esc** in the keyboard once. By doing this the pointer won\'t create lines any more, it will just be a pointer allowing us to select the objects we just created. In this pointer mode we can pick and drag the endpoints of each line to adjust its placement.


**Note 2:**

do not press **Esc** a second time as this will exit the sketch edit mode. If you do this, re-enter the edit mode by double clicking on the sketch in the [tree view](tree_view.md).

Take a look at the [task panel](task_panel.md) again. The **Solver messages** section already indicates that the sketch is under-constrained, and it mentions the number of **degrees of freedom**.

Look at the **Constraints** and **Elements** sections to see the new listed constraints and lines. Once your sketches have many elements, it may be difficult to select them in the [3D view](3D_view.md), so you can use these lists to select the object that you wish exactly.

<img alt="" src=images/02_Sk01_Sketcher_construction.png  style="width:" height="400px;">


*Construction lines forming a star shape with its center in the origin.*


<div class="mw-translate-fuzzy">

##### Geometria Sketcher 

Geometria Sketcher este folosită pentru a crea profilurile închise necesare pentru a efectua operații 3D în Atelierul**PartDesign** .

1.  Selectați <img alt="" src=images/Sketcher_Circle.png  style="width:32px;"> [Circle](Sketcher_CreateCircle.md)
2.  Poziționați **centerpoint** acestuia pe oringinea sketch.
3.  Extindeți circumferința cu o lungime arbitrară.


</div>


<div class="mw-translate-fuzzy">

1.  Selectați <img alt="" src=images/Sketcher_Arc.png  style="width:32px;"> [Arc](Sketcher_CreateArc.md)
2.  Apropiați **endpoint** de una de liniile de construcție.
3.  Definiți **centerpoint** arcului de cerc pentru a **coincide** cu punctul de capăt.
4.  Selectați o locație arbitrară a cursorului dvs pentru a fi definit ca începutul arcului , făcând click o dată.
5.  Extindeți arcul de cerc în mod arbitar, asigurându-vă că circumferința se deschide spre exterior (spațiul gol se îndreaptă spre cercul pe care l-ați creat mai devreme).
6.  Repetați acești pași pentru fiecare linie de construcție.


</div>

Make sure you are not in construction mode by clicking on **<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction](Sketcher_ToggleConstruction.md)**, if you have not previously exited this mode.

### Outer arcs 

4\. Create a circle.

:   4.1. Click on **<img src=images/Sketcher_Circle.svg style="width:16px"> [Create circle](Sketcher_CreateCircle.md)**.
:   4.2. Click on the **origin** of the sketch to position its center point.
:   4.3. Click anywhere in the [3D view](3D_view.md) to set the circumference radius as a distance from the origin. Make it approximately {{Value|8 mm}}. Again the dimension will be fixed later.

5\. Create a series of arcs.

:   5.1. Click on **<img src=images/Sketcher_Arc.svg style="width:16px"> [Create arc](Sketcher_CreateArc.md)**.
:   5.2. Approach the endpoint of one of the construction lines, and click on it. This will set the center point of the circular arc to be <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [coincident](Sketcher_ConstrainCoincident.md) with this line\'s endpoint.
:   5.3. Click once in the [3D view](3D_view.md) at an arbitrary location to set simultaneously the radius of the arc, and the first endpoint of it. Define an approximate radius of {{Value|8 mm}}.
:   5.4. Move the pointer in an anti-clockwise direction to trace an arc that has its concavity pointing towards the origin of the sketch. Click to set the final endpoint of the arc, defining a circular arc that approximately sweeps {{Value|180°}} or half a circle.
:   5.5. Repeat these steps with each construction line, so that each of them has a circular arc at its tip. We will call these O-arcs for outwards-arcs.

<img alt="" src=images/03_Sk01_Sketcher_outer_arcs.png  style="width:" height="400px;">


*Circular arcs added at the endpoints of the construction lines. Also a central circle.*

### Inner arcs 


<div class="mw-translate-fuzzy">

1.  Creați un arc între fiecare pereche de arce anterioare, cu circumferința lor îndreptată către cerc.


</div>

To summarize, the O-arcs should have their curvature pointing outwards, and their concavity pointing towards the origin of the sketch; the I-arcs should have their curvature pointing inwards, and their concavity pointing away from the same origin.

<img alt="" src=images/04_Sk01_Sketcher_inner_arcs.png  style="width:" height="400px;">


*Circular arcs added between the first set of arcs placed.*

## Constraints

Take a look at the [task panel](task_panel.md) again. Due to the new geometrical elements that we have drawn, the **Solver messages** section indicates even more **degrees of freedom**. A **degree of freedom** (DOF) indicates a possible movement of one element. For example, a point can be moved both in horizontal and vertical directions, so it has two degrees of freedom. A line is defined by two points, therefore in total it has four degrees of freedom. If we fix one of those points, then the entire system has only two degrees of freedom available; if we additionally fix the horizontal movement of the remaining point, we only have one degree of freedom left; and if we also fix the vertical movement of this point, then the last degree of freedom disappears, and the line cannot move from its position any more.


<div class="mw-translate-fuzzy">

#### Constrângeri

Constrângerile sunt folosite pentru a reduce **Degrees of Freedom** a punctelor și curbelor din schiță.


</div>

There are two principal types of constraints:

-    **Geometric constraints**define characteristics of the shapes without specifying exact dimensions, for example, horizontality, verticality, parallelism, perpendicularity, and tangency.

-    **Datum constraints**define characteristics of the shapes by specifying dimensions, for example, a numeric length or an angle.


<div class="mw-translate-fuzzy">

##### Constrângeri Geometrice 

Ele sunt folosite pentru a stabili relațiile dintre puncte și curbe fără a utiliza dimensiuni.


</div>

### Equal length and radius 


<div class="mw-translate-fuzzy">

1.  Selectați toate cele cinci linii de construcție.
2.  Selectați <img alt="" src=images/Constraint_EqualLength.png  style="width:32px;"> [Equal Length](Sketcher_ConstrainEqual.md)


</div>


:   7.3. Select all five O-arcs, those centered on an endpoint of a construction line.
:   7.4. Press **<img src=images/Constraint_EqualLength.svg style="width:16px"> [Equal length](Sketcher_ConstrainEqual.md)**.
:   7.5. Repeat with all I-arcs, those between the O-arcs.
:   
    **Note:**again the constraints are chained. Therefore all O-arcs will have the same radius, and all I-arcs will have the same radius. At this moment, the specific value of these lengths is not fixed. You may use the pointer to drag a point and see how the sketch is updated while respecting the constraints in place.


<div class="mw-translate-fuzzy">

1.  Selectați linia de construcție care este închisă pe axa verticală .
2.  Selectați <img alt="" src=images/Constraint_Vertical.png  style="width:32px;"> [Vertical](‎Sketcher_ConstrainVertical.md)


</div>


**Note:**

as you add constraints, overlay symbols indicating the type of constraint appear over the geometry in the [3D view](3D_view.md). If these symbols obfuscate your view, you can hide them by unchecking the constraint in the [task panel](task_panel.md). Also note that the number of degrees of freedom decreases after adding each constraint.


**Note 2:**

if you wish to temporarily disable the constraint, you may select it and press **<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [Toggle active constraint](Sketcher_ToggleActiveConstraint.md)**. When you want to apply it again, press again the same button.

<img alt="" src=images/05a_Sk01_Sketcher_equality_constraints_lines.png  style="width:" height="400px;"> <img alt="" src=images/05b_Sk01_Sketcher_equality_constraints_O-arcs.png  style="width:" height="400px;">

<img alt="" src=images/05c_Sk01_Sketcher_equality_constraints_I-arcs.png  style="width:" height="400px;">


*Sketch with equality constraints applied to the construction lines, and to the two sets of arcs.*

### Tangency


<div class="mw-translate-fuzzy">

1.  Selectați punctul de capăt al arcului de cer și punctul de capăt cel mai apropiat de el.
2.  Selectați <img alt="" src=images/Constraint_Tangent.png  style="width:32px;"> [Tangent](Sketcher_ConstrainTangent.md)
3.  Repetați pentru fiecare punct de capăt, până se închide profilul creat.


</div>


**Note:**

applying the tangential constraint very often will move the geometry around in order to produce a smooth connection. You may have to use the pointer to reposition the points a bit before applying the next tangential constraint. Try placing the endpoints in such a way that two arcs aren\'t too far apart, so they can be connected with a short line rather than a long line.


<div class="mw-translate-fuzzy">

Până la acest pas, am creat un profil închis, care poate fi ajustat cu dimensiunile dorite.


</div>

<img alt="" src=images/06_Sk01_Sketcher_tangency_constraints.png  style="width:" height="400px;">


*Sketch with tangential constraints applied to the arcs, which closes the shape.*


<div class="mw-translate-fuzzy">

##### Constrângeri de Referință 

Acestea sunt folosite pentru a specifica distanța dintre punctele dintr-o anumită direcție și dimensiunile curbelor.


</div>

These constraints specify the numerical distances between two points, and angles between two lines.

### Distances and angles 


<div class="mw-translate-fuzzy">

1.  Selectați constrângerea verticală pentru linia de construit.
2.  Selectați <img alt="" src=images/Constraint_VerticalDistance.png  style="width:32px;"> [Vertical Distance](Sketcher_ConstrainDistanceY.md)
3.  Definiți lungimea la 30 mm.


</div>


<div class="mw-translate-fuzzy">

1.  Selectați linia verticală de construcție și linia cea mai apropiată de aceasta
2.  Selectați <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> [Internal Angle](Sketcher_ConstrainAngle.md)
3.  Definiți unghiul la 72°
4.  Repetați aceeași procedură pentru fiecare pereche de linii adiacente.


</div>

<img alt="" src=images/07a_Sk01_Sketcher_length_constraint.png  style="width:" height="400px;"> <img alt="" src=images/07b_Sk01_Sketcher_angle_constraint.png  style="width:" height="400px;">


*Sketch with length constraint applied to one vertical construction line (left), and angle constraints to three pairs of construction lines (right).*

### Radius


<div class="mw-translate-fuzzy">

1.  Selectați unul dintre arcele de cerc centrate pe puctul de capăt al liniei.
2.  Selectați <img alt="" src=images/Constraint_Radius.png  style="width:32px;"> [Radius](Sketcher_ConstrainRadius.md)
3.  Definiți raza la 8 mm.
4.  Faceți același lucru pentru un arc de cerc necentrat pe un punct de capăt. Definiți raza la 11 mm.
5.  Modificați raza cercului de centru la 10 mm.


</div>

<img alt="" src=images/08a_Sk01_Sketcher_radius_1_constraint.png  style="width:" height="400px;"> <img alt="" src=images/08b_Sk01_Sketcher_radius_2_constraint.png  style="width:" height="400px;">


*Sketch with radius constraints applied to the outwards arcs (left), and inwards arcs (right).*


:   11.7. Finally, select the circle in the center of the sketch, press **<img src=images/Constraint_Radius.svg style="width:16px"> [Radius](Sketcher_ConstrainRadius.md)**, and set the value to {{Value|8 mm}}.


<div class="mw-translate-fuzzy">

Ar trebui să finalizați cu o schiță complet constrânsă. Aceasta poate fi confirmată prin observarea modificării culorii tuturor curbelor.


</div>

<img alt="" src=images/09_Sk01_Sketcher_fully_constrained.png  style="width:" height="400px;">


*Sketch with all geometrical and datum constraints applied.*

## Extrusion

12\. Now that we have a fully constrained sketch, it can be used to create a solid body.

:   12.1. Exit the sketch edit mode by pressing the **Close** button, or pressing **Esc** twice. The sketch should appear in the [tree view](tree_view.md) and the [3D view](3D_view.md).
:   12.2. Switch to the [PartDesign Workbench](PartDesign_Workbench.md).
:   12.3. With the sketch selected in the <img src=images/PartDesign_Body.svg style="width:tree view](tree_view.md), press **[16px"> [PartDesign Body](PartDesign_Body.md)**, choose the default XY-plane, and press **OK**. The sketch should appear now inside the Body.
:   12.4. Select the sketch, and then press **<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad.md)**, choose the default options, and press **OK** to create a solid extrusion.

<img alt="" src=images/09b_Sk01_Sketcher_fully_constrained_clean.png  style="width:" height="400px;"> <img alt="" src=images/10_Sk01_Sketcher_solid_extrusion.png  style="width:" height="400px;">


*Left: fully constrained sketch with only the most important constraints showing. Right: solid extrusion produced with [PartDesign Pad](PartDesign_Pad.md).*

## Additional information 

For a more in depth description of the sketcher, visit the [Sketcher Workbench](Sketcher_Workbench.md) documentation and also read the [Sketcher reference](Sketcher_reference.md).

Constraining a sketch can be done in many different ways. In general, it is recommended to use geometrical constraints first, and minimize the number of datum constraints, as this simplifies the task of the internal constraint solver. To investigate this, repeat this example, now adding the constraints in different order.

-   First constrain the construction lines before drawing the arcs.
-   Or constrain the size of the arcs before making them tangent.
-   Or set the angle of the construction lines before adding more elements.
-   Try using other construction geometry.


{{Tutorials navi

}} {{Sketcher Tools navi}} 

_

---
[documentation index](../README.md) > Basic Sketcher Tutorial/ro
