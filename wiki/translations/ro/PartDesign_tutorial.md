# PartDesign tutorial/ro
{{TutorialInfo/ro
|Topic= Sketcher
|Level= Beginner
|Time= 15 minutes
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
|FCVersion=0.16 or above
|Files=
}}

### Introducere

Acest tutorial are rolul de a introduce cititorul în fluxul de lucru de bază al aplicației [PartDesign Workbench](PartDesign_Workbench.md). Cititorul va vedea cum se creează obiecte 3D bazate pe schițe, operații substractive și replicarea unor caracteristici specifice într-un model.

<img alt="" src=images/Sketcher_tutorial_result.png  style="width:480px;">


<div class="mw-translate-fuzzy">

### Cerințe

-   FreeCAD version 0.17 or above
-   The reader has finished the [Basic Sketcher Tutorial](Basic_Sketcher_Tutorial/ro.md)


</div>

### Procedură

#### Crearea de forma geometrice 3D 

Scopul Atelierului **PartDesign Workbench** este de a permite utilizatorului să creeze geometrie în spațiul 3D. Ca atare, este echipat cu instrumente pentru a face uz de schițe și a le converti în obiecte 3D.


<div class="mw-translate-fuzzy">

Pentru a realiza acest lucru, există două instrumente:<img alt="" src=images/PartDesign_Pad.png  style="width:32px;"> _. Alongside their subtractive counterparts (<img alt="" src=images/PartDesign_Pocket.png  style="width:32px;"> _) they make up most of the common actions used by this workbench.


</div>

1.  Switch to the PartDesign Workbench
2.  With the sketch selected in the <img src=images/PartDesign_Body.svg style="width:tree view](tree_view.md), press **[16px"> [PartDesign Body](PartDesign_Body.md)**, choose the default XY-plane, and press **OK**. The sketch should appear now inside the Body.
3.  Select <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Pad](PartDesign_Pad.md)
4.  Set the distance to 5 mm
5.  Select **Ok**


<div class="mw-translate-fuzzy">

Another way to create 3D geometry is with the <img alt="" src=images/PartDesign_Revolution.png  style="width:32px;"> [Revolution](PartDesign_Revolution.md) tool.


</div>

<img alt="" src=images/PartDesign_revolution_exercise.png  style="width:480px;">


<div class="mw-translate-fuzzy">

1.  Create a sketch based on the image above
2.  Select <img alt="" src=images/PartDesign_Revolution.png  style="width:32px;"> [Revolution](PartDesign_Revolution.md)
3.  Set the \"Axis\" to the \"Horizontal Sketch Axis\"
4.  Set the angle to 360°


</div>

#### Caracteristici Subtractve 

Vom începe prin a crea o schiță cu forma pe care dorim să o extragem.


<div class="mw-translate-fuzzy">

1.  Select the top flat face of the \"Revolution\"
2.  Select <img alt="" src=images/Sketcher_NewSketch.png‎‎  style="width:32px;"> [New sketch](Sketcher_NewSketch.md)
3.  Select <img alt="" src=images/Sketcher_External.png  style="width:32px;"> [External Geometry](Sketcher_External.md)
4.  Approach the edge of the pad. An arc should be highlighted
5.  Select the arc. An arc of a different color should appear in the sketch
6.  Create a hexagon centered on the same point as the arc and set the radius of the reference circle to 5 mm


</div>


<div class="mw-translate-fuzzy">


{{Message| '''External Geometry'''
Când a fost creat un element 3D, este posibil să creați referințe la acesta într-o schiță.
# Select <img src="images/Sketcher_External.png" width=32px> [External Geometry](Sketcher_External.md).
# Approach the element that you wish to reference, the edge of a '''Pad''' for example.
# Click on it
# New elements of a different color should appear on the sketch in the location of the feature you wish to reference.}}


</div>

<img alt="" src=images/PartDesign_pocket_exercise.png  style="width:480px;">

Apoi, vom continua să aplicăm funcționalitatea**Pocket**.


<div class="mw-translate-fuzzy">

1.  Select the sketch
2.  Select <img alt="" src=images/PartDesign_Pocket.png  style="width:32px;"> [Pocket](PartDesign_Pocket.md)
3.  Set the distance to **Through all**


</div>

#### Funcționalități ale Modeluluis 

Re apelați profilul extrudat care a fost creat la începutul tutorialului.

1.  Select the top face of the object
2.  Create a new Sketch
3.  Create reference geometry linked to the top arm of the figure
4.  Create a circle constrained to the center of the reference arc
5.  Set its radius to 3 mm
6.  Pocket the sketch through all the workpiece

Instead of creating a circle for each hole in the sketch, we will introduce the concept of **Pattern Features**. These tools operate by replicating a feature in the workpiece that has already been created and that we wish to reproduce in a linear or circular arrangement. We will use a combination of **Linear** and **Polar** pattern features simulatneously to obtain the final workpiece.


<div class="mw-translate-fuzzy">

1.  Select the Pockt feature that we just created in the **Tree View**
2.  Select <img alt="" src=images/PartDesign_MultiTransform.png  style="width:32px;"> [MultiTransform](PartDesign_MultiTransform.md)


</div>

In the Combo View we are now asked to introduce the **Transformations** that we desire. Notice that in the **MultiTransform parameters** menu we see that FreeCAD has identified the Pocket as the **Original feature** and a second box requests us to **Right click it** to introduce the pattern features.

1.  Right click the box
2.  Select **Add Linear Pattern**
3.  Set the **Direction** to **Vertical Sketch Axis**
4.  Set length to 10 mm
5.  Leave occurrences at 2
6.  Click OK
7.  Right click the box again to add a **Polar Pattern**. Notice that the 3D view has now added the linear pattern.
8.  Set occurrences to 5
9.  Click OK twice

După finalizarea acestei sarcini, trebuie să aveți următorul rezultat.

<img alt="" src=images/PartDesign_multitransform_exercise.png  style="width:480px;">

If not, re-edit the MultiTransform operation by double clicking on it in the Tree View. Check both pattern features to detect necessary modifications, such as the **Axis** and if the **Direction** needs to be reversed.

Suntem terminați acum cu fluxul de lucru de bază pentru [PartDesign Workbench](PartDesign_Workbench.md).

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign tutorial/ro
