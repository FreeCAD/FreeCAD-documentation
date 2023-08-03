---
 TutorialInfo:t
   Topic:  Sketcher
   Level:  Base
   Time:  60 minuti
   Author: http://freecadweb.org/wiki/index.php?title=User:Drei Drei e vocx
   FCVersion: 0.19
   Files: https://forum.freecadweb.org/viewtopic.php?f=36&t=43594 Basic Sketcher tutorial updated
---

# Basic Sketcher Tutorial/it







## Introduzione

Questo tutorial ha lo scopo di introdurre il lettore al flusso di lavoro di base dell\'ambiente <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Schizzo](Sketcher_Workbench/it.md).

L\'ambiente[Sketcher ](Sketcher_Workbench/it.md) esiste come modulo autonomo, quindi può essere utilizzato per disegnare oggetti 2D generici (planari). Tuttavia, viene utilizzato principalmente in combinazione con <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/it.md). Uno schizzo chiuso viene normalmente utilizzato per creare una faccia o un profilo da estrudere in un [corpo](PartDesign_Body/it.md) solido con un\'operazione come <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Pad](PartDesign_Pad/it.md) di PartDesign .

Il lettore farà pratica su:

-   Creazione della geometria di costruzione
-   Creazione di geometria reale
-   Applicazione di vincoli geometrici
-   Applicazione di vincoli di riferimento
-   Ottenere un profilo chiuso

Per una descrizione più approfondita dello sketcher, leggere il [Manuale di riferimento per Sketcher](Sketcher_reference/it.md).

![](images/00_Sk01_Sketcher_fully_constrained_final.png ) 
*Risultato finale dello schizzo, con tutta la geometria completamente vincolata, inclusa la geometria di costruzione per il supporto.*



## Setup

1\. Open FreeCAD, create a new empty document with **File → [<img src=images/Std_New.svg style="width:16px"> [New](Std_New.md)**.

:   1.1. Switch to the [Sketcher Workbench](Sketcher_Workbench.md) from the [workbench selector](Std_Workbench.md), or the menu **[View](Std_View_Menu.md) → Workbench → Sketcher**.

Some actions to remember:

-   Press the right mouse button, or press **Esc** in the keyboard once, to deselect the active tool in edit mode.
-   To exit the sketch edit mode, press the **Close** button in the [task panel](task_panel.md), or press **Esc** twice in the keyboard.
-   To enter again edit mode, double click on the sketch in the [tree view](tree_view.md), or select it, and then click on **[<img src=images/Sketcher_EditSketch.svg style="width:16px"> [Edit sketch](Sketcher_EditSketch.md)**.



## Creare uno schizzo 

2\. Click on **<img src="images/Sketcher_NewSketch.svg‎‎" width=16px> [New sketch](Sketcher_NewSketch.md)**.

:   2.1. Choose the sketch orientation, that is, one of the base XY, XZ, or YZ planes. Also choose if you want an inverted orientation, and an offset from the base plane.
:   2.2. We will use the default plane and options.
:   2.3. Click **OK** to start constructing the sketch.

Siamo ora nella modalità di modifica dello schizzo. Al suo interno, è possibile utilizzare la maggior parte degli strumenti di questo ambiente di lavoro.


**Nota:**

la [vista ad albero](tree_view/it.md) passa alla [scheda azioni](task_panel/it.md); in questa interfaccia espandere la sezione **Modifica controlli** e assicurarsi che l\'opzione **Vincoli automatici** sia abilitata. Altre opzioni possono essere modificate inclusa la dimensione della griglia visibile e se si vuole agganciarla; in questo tutorial non ci agganceremo alla griglia e la nasconderemo anche. In altre sezioni della [scheda azioni](task_panel/it.md) si può anche vedere quali elementi geometrici e vincoli sono stati definiti.

<img alt="" src=images/01_Sk01_Sketcher_Task_panel.png  style="width:" height="400px;">



*Upper part of the [task panel](task_panel.md) of the sketcher.*



## La geometria di costruzione 


<div class="mw-translate-fuzzy">

1.  Selezionare <img alt="" src=images/Sketcher_ToggleConstruction.png  style="width:32px;"> [Costruzione](Sketcher_ToggleConstruction/it.md)
2.  Selezionare <img alt="" src=images/Sketcher_Line.png  style="width:32px;"> [Linea da 2 punti](Sketcher_CreateLine/it.md)
3.  Nello schizzo avvicinare il cursore al **punto di origine**, il punto viene evidenziato e vicino al cursore appare questa icona<img alt="" src=images/Constraint_PointOnPoint.png  style="width:32px;">.
4.  Selezionare il punto e tracciare una linea in diagonale con una lunghezza arbitraria.
5.  Ripetere questa procedura fino a creare cinque **linee di costruzione**. Accertarsi che siano disposte a raggera, come nella figura iniziale.
6.  Per uscire dalla modalità di costruzione, è sufficiente cliccare nuovamente su <img alt="" src=images/Sketcher_ToggleConstruction.png  style="width:32px;"> [Costruzione](Sketcher_ToggleConstruction/it.md)


</div>


**Note:**

up to this point the [line tool](Sketcher_CreateLine.md) is still active. This means we can keep clicking on the [3D view](3D_view.md) to draw as many lines as we want. If we wish to exit this tool, we can press the right mouse button, or press **Esc** in the keyboard once. By doing this the pointer won\'t create lines any more, it will just be a pointer allowing us to select the objects we just created. In this pointer mode we can pick and drag the endpoints of each line to adjust its placement.


**Note 2:**

do not press **Esc** a second time as this will exit the sketch edit mode. If you do this, re-enter the edit mode by double clicking on the sketch in the [tree view](tree_view.md).

Take a look at the [task panel](task_panel.md) again. The **Solver messages** section already indicates that the sketch is under-constrained, and it mentions the number of **degrees of freedom**.

Look at the **Constraints** and **Elements** sections to see the new listed constraints and lines. Once your sketches have many elements, it may be difficult to select them in the [3D view](3D_view.md), so you can use these lists to select the object that you wish exactly.

<img alt="" src=images/02_Sk01_Sketcher_construction.png  style="width:" height="400px;">



*Construction lines forming a star shape with its center in the origin.*



## La geometria reale 

La geometria reale deve creare una forma chiusa se deve essere utilizzata come profilo che può essere estruso da strumenti come <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Pad](PartDesign_Pad/it.md) di PartDesign.

Make sure you are not in construction mode by clicking on **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction](Sketcher_ToggleConstruction.md)**, if you have not previously exited this mode.

### Outer arcs 

4\. Create a circle.

:   4.1. Click on **[<img src=images/Sketcher_Circle.svg style="width:16px"> [Create circle](Sketcher_CreateCircle.md)**.
:   4.2. Click on the **origin** of the sketch to position its center point.
:   4.3. Click anywhere in the [3D view](3D_view.md) to set the circumference radius as a distance from the origin. Make it approximately {{Value|8 mm}}. Again the dimension will be fixed later.

5\. Create a series of arcs.

:   5.1. Click on **[<img src=images/Sketcher_Arc.svg style="width:16px"> [Create arc](Sketcher_CreateArc.md)**.
:   5.2. Approach the endpoint of one of the construction lines, and click on it. This will set the center point of the circular arc to be <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [coincident](Sketcher_ConstrainCoincident.md) with this line\'s endpoint.
:   5.3. Click once in the [3D view](3D_view.md) at an arbitrary location to set simultaneously the radius of the arc, and the first endpoint of it. Define an approximate radius of {{Value|8 mm}}.
:   5.4. Move the pointer in an anti-clockwise direction to trace an arc that has its concavity pointing towards the origin of the sketch. Click to set the final endpoint of the arc, defining a circular arc that approximately sweeps {{Value|180°}} or half a circle.
:   5.5. Repeat these steps with each construction line, so that each of them has a circular arc at its tip. We will call these O-arcs for outwards-arcs.

<img alt="" src=images/03_Sk01_Sketcher_outer_arcs.png  style="width:" height="400px;">



*Circular arcs added at the endpoints of the construction lines. Also a central circle.*

### Inner arcs 

6\. Creare un arco tra ogni coppia degli archi O precedenti.

:   6.1. Sempre con lo strumento **[<img src=images/Sketcher_Arc.svg style="width:16px"> [Arco](Sketcher_CreateArc/it.md)** attivo, fare clic da qualche parte tra due archi O ma più lontano dall\'origine dello schizzo, per impostare il punto centrale di un nuovo arco.
:   6.2. Fare clic in un punto vicino al punto finale di un arco O e spostare il puntatore per tracciare un altro arco finendo vicino a un altro punto finale di un arco O diverso, come se si stesse tentando di unire i punti finali. Questa volta la concavità deve puntare lontano dall\'origine.
:   6.3. Ripetere questi passaggi, in modo che ogni coppia di archi O abbia un nuovo arco tra di loro. Chiameremo questi archi a I per archi verso l\'interno.

To summarize, the O-arcs should have their curvature pointing outwards, and their concavity pointing towards the origin of the sketch; the I-arcs should have their curvature pointing inwards, and their concavity pointing away from the same origin.

<img alt="" src=images/04_Sk01_Sketcher_inner_arcs.png  style="width:" height="400px;">



*Circular arcs added between the first set of arcs placed.*

## Constraints

Take a look at the [task panel](task_panel.md) again. Due to the new geometrical elements that we have drawn, the **Solver messages** section indicates even more **degrees of freedom**. A **degree of freedom** (DOF) indicates a possible movement of one element. For example, a point can be moved both in horizontal and vertical directions, so it has two degrees of freedom. A line is defined by two points, therefore in total it has four degrees of freedom. If we fix one of those points, then the entire system has only two degrees of freedom available; if we additionally fix the horizontal movement of the remaining point, we only have one degree of freedom left; and if we also fix the vertical movement of this point, then the last degree of freedom disappears, and the line cannot move from its position any more.

Finora quando abbiamo disegnato linee e curve, lo sketcher ha aggiunto per noi i vincoli automatici, quelli che mantengono le linee legate all\'origine e gli archi O legati alle linee di costruzione. Ma non abbiamo aggiunto altri vincoli espliciti in modo che le forme geometriche possano ancora essere spostate in molte direzioni. **I vincoli sono \"regole\" che ci dicono in quali condizioni un oggetto geometrico può muoversi e di quanto.** Sono usati per eliminare i gradi di libertà in modo che lo schizzo abbia una forma stabile. Se eliminiamo tutti i gradi di libertà, lo schizzo è **completamente vincolato** e ha una forma fissa, ovvero i suoi punti non possono spostarsi affatto. In generale, è una buona idea vincolare completamente gli schizzi perché ciò si riflette in modelli stabili.

There are two principal types of constraints:

-    **Geometric constraints**define characteristics of the shapes without specifying exact dimensions, for example, horizontality, verticality, parallelism, perpendicularity, and tangency.

-    **Datum constraints**define characteristics of the shapes by specifying dimensions, for example, a numeric length or an angle.



## I vincoli geometrici 

### Equal length and radius 


<div class="mw-translate-fuzzy">

1.  Selezionare tutte e cinque le linee di costruzione.
2.  Selezionare <img alt="" src=images/Constraint_EqualLength.png  style="width:32px;"> [Uguale lunghezza](Sketcher_ConstrainEqual/it.md)


</div>


:   7.3. Select all five O-arcs, those centered on an endpoint of a construction line.
:   7.4. Press **[<img src=images/Constraint_EqualLength.svg style="width:16px"> [Equal length](Sketcher_ConstrainEqual.md)**.
:   7.5. Repeat with all I-arcs, those between the O-arcs.
:   
    **Note:**again the constraints are chained. Therefore all O-arcs will have the same radius, and all I-arcs will have the same radius. At this moment, the specific value of these lengths is not fixed. You may use the pointer to drag a point and see how the sketch is updated while respecting the constraints in place.


<div class="mw-translate-fuzzy">

1.  Selezionare la linea di costruzione che è più vicina all\'asse verticale.
2.  Selezionare <img alt="" src=images/Constraint_Vertical.png  style="width:32px;"> [Verticale](Sketcher_ConstrainVertical/it.md)


</div>


**Note:**

as you add constraints, overlay symbols indicating the type of constraint appear over the geometry in the [3D view](3D_view.md). If these symbols obfuscate your view, you can hide them by unchecking the constraint in the [task panel](task_panel.md). Also note that the number of degrees of freedom decreases after adding each constraint.


**Note 2:**

if you wish to temporarily disable the constraint, you may select it and press **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [Toggle active constraint](Sketcher_ToggleActiveConstraint.md)**. When you want to apply it again, press again the same button.

<img alt="" src=images/05a_Sk01_Sketcher_equality_constraints_lines.png  style="width:" height="400px;"> <img alt="" src=images/05b_Sk01_Sketcher_equality_constraints_O-arcs.png  style="width:" height="400px;">

<img alt="" src=images/05c_Sk01_Sketcher_equality_constraints_I-arcs.png  style="width:" height="400px;">



*Sketch with equality constraints applied to the construction lines, and to the two sets of arcs.*

### Tangency


<div class="mw-translate-fuzzy">

1.  Selezionare il punto finale in un arco e il più vicino punto finale di un altro arco.
2.  Selezionare <img alt="" src=images/Constraint_Tangent.png  style="width:32px;"> [Tangente](Sketcher_ConstrainTangent/it.md)
3.  Ripetere l\'operazione per ogni punto finale, fino a quando il profilo viene chiuso.


</div>


**Note:**

applying the tangential constraint very often will move the geometry around in order to produce a smooth connection. You may have to use the pointer to reposition the points a bit before applying the next tangential constraint. Try placing the endpoints in such a way that two arcs aren\'t too far apart, so they can be connected with a short line rather than a long line.


<div class="mw-translate-fuzzy">

A questo punto, il profilo è chiuso e può essere regolato con le dimensioni desiderate.


</div>

<img alt="" src=images/06_Sk01_Sketcher_tangency_constraints.png  style="width:" height="400px;">



*Sketch with tangential constraints applied to the arcs, which closes the shape.*



## I vincoli di dati 

These constraints specify the numerical distances between two points, and angles between two lines.

### Distances and angles 


<div class="mw-translate-fuzzy">

1.  Selezionare la linea di costruzione vincolata verticalmente.
2.  Selezionare <img alt="" src=images/Constraint_VerticalDistance.png  style="width:32px;"> [Lunghezza verticale](Sketcher_ConstrainDistanceY/it.md)
3.  Impostare la lunghezza a 30 mm.


</div>


<div class="mw-translate-fuzzy">

1.  Selezionare la linea di costruzione verticale e la linea più vicina ad essa
2.  Selezionare <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> [Angolo interno](Sketcher_ConstrainAngle/it.md)
3.  Impostare l\'angolo a 72°
4.  Ripetere la stessa procedura per ciascuna coppia di linee adiacenti.


</div>

<img alt="" src=images/07a_Sk01_Sketcher_length_constraint.png  style="width:" height="400px;"> <img alt="" src=images/07b_Sk01_Sketcher_angle_constraint.png  style="width:" height="400px;">



*Sketch with length constraint applied to one vertical construction line (left), and angle constraints to three pairs of construction lines (right).*

### Radius

11\. Regolare la dimensione degli archi.

:   11.1. Selezionare uno degli archi O, centrato sul punto finale di una linea di costruzione.
:   11.2. Premere il pulsante **[<img src=images/Constraint_Radius.svg style="width:16px"> [Raggio](Sketcher_ConstrainRadius/it.md)**.
:   11.3. Impostare il raggio su {{Value|8 mm}}. Poiché tutti gli archi O sono vincolati per avere lo stesso raggio, tutti questi archi regolano le loro dimensioni contemporaneamente.
:   11.4. Selezionare uno degli archi I, tra due archi O.
:   11.5. Premere il pulsante **[<img src=images/Constraint_Radius.svg style="width:16px"> [Raggio](Sketcher_ConstrainRadius/it.md)**.
:   11.6. Impostare il raggio su {{Value|11 mm}}. Poiché tutti gli archi O sono vincolati per avere lo stesso raggio, tutti questi archi regolano le loro dimensioni contemporaneamente.

<img alt="" src=images/08a_Sk01_Sketcher_radius_1_constraint.png  style="width:" height="400px;"> <img alt="" src=images/08b_Sk01_Sketcher_radius_2_constraint.png  style="width:" height="400px;">



*Sketch with radius constraints applied to the outwards arcs (left), and inwards arcs (right).*


:   11.7. Finally, select the circle in the center of the sketch, press **[<img src=images/Constraint_Radius.svg style="width:16px"> [Radius](Sketcher_ConstrainRadius.md)**, and set the value to {{Value|8 mm}}.

Alla fine si dovrebbe ottenere uno schizzo completamente vincolato. Questo può essere confermato dal cambio di colore della geometria reale e dal messaggio che viene mostrato nella [scheda azioni](task_panel/it.md).

<img alt="" src=images/09_Sk01_Sketcher_fully_constrained.png  style="width:" height="400px;">



*Sketch with all geometrical and datum constraints applied.*

## Extrusion

12\. Now that we have a fully constrained sketch, it can be used to create a solid body.

:   12.1. Exit the sketch edit mode by pressing the **Close** button, or pressing **Esc** twice. The sketch should appear in the [tree view](tree_view.md) and the [3D view](3D_view.md).
:   12.2. Switch to the [PartDesign Workbench](PartDesign_Workbench.md).
:   12.3. With the sketch selected in the [tree view](tree_view.md), press **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**, choose the default XY-plane, and press **OK**. The sketch should appear now inside the Body.
:   12.4. Select the sketch, and then press **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad.md)**, choose the default options, and press **OK** to create a solid extrusion.

<img alt="" src=images/09b_Sk01_Sketcher_fully_constrained_clean.png  style="width:" height="400px;"> <img alt="" src=images/10_Sk01_Sketcher_solid_extrusion.png  style="width:" height="400px;">



*Left: fully constrained sketch with only the most important constraints showing. Right: solid extrusion produced with [PartDesign Pad](PartDesign_Pad.md).*

## Additional information 

For a more in depth description of the sketcher, visit the [Sketcher Workbench](Sketcher_Workbench.md) documentation and also read the [Sketcher reference](Sketcher_reference.md).

Constraining a sketch can be done in many different ways. In general, it is recommended to use geometrical constraints first, and minimize the number of datum constraints, as this simplifies the task of the internal constraint solver. To investigate this, repeat this example, now adding the constraints in different order.

-   First constrain the construction lines before drawing the arcs.
-   Or constrain the size of the arcs before making them tangent.
-   Or set the angle of the construction lines before adding more elements.
-   Try using other construction geometry.


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Category_Sketcher.md) > Basic Sketcher Tutorial/it
