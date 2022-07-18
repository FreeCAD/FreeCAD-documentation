---
- TutorialInfo   */de
   Topic   *Assembly3, ein Kinematik-Skelett
   Level   *Grundwissen über Assembly3 und Sketcher ist hilfreich
   FCVersion   *0.20 und neuer
   Time   *40 Minuten
   Author   *[FBXL5](User_FBXL5.md)
---

# Tutorial KinematicSkeleton/de





## Einleitung

In dieser Anleitung geht es darum, einen einfachen 2D-Mechanismus zu erstellen und daran 3D-Objekte zu befestigen, hauptsächlich mit den Werkzeugen des externen Arbeitsbereichs <img alt="" src=images/Assembly3_workbench_icon.svg  style="width   *16px;"> [Assembly3](Assembly3_Workbench/de.md).

Diese Anleitung verwendet nicht das Skeleton-Sketch-Prinzip (siehe Assembly3 [Create-Skeleton-Sketch](https   *//github.com/realthunder/FreeCAD_assembly3/wiki/Create-Skeleton-Sketch) auf GitHub).

Stattdessen werden <img alt="" src=images/PartDesign_Body.svg  style="width   *16px;"> [PartDesign Bodies](PartDesign_Body/de.md) (Körper) verwendet, die jeweils nur eine <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [Skizze](Sketcher_Workbench/de.md) enthalten, um einen 2D-Mechanismus aufzubauen, ein **Skizzen-Skelett**.

Die Maße und die Farben wurden von der Anleitung [SolveSpace tutorial](http   *//solvespace.com/linkage.pl) übernommen, auf die sich auch die Assembly3-GitHub-Seite bezieht (siehe oben).

## Skizzen-Skelett 

Dieses sogenannte Skizzen-Skelett besteht aus mehreren einzelnen <img alt="" src=images/PartDesign_Body.svg  style="width   *16px;"> [Körpern](PartDesign_Body/de.md) und einem <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width   *16px;"> [Assembly](Assembly3_CreateAssembly.md)-Container. Um weitere Objekte befestigen zu können, wird jeder Körper in einen eigenen Assembly-Container gepackt.

### 2D-Body-Objekte 

Die Körper (Bodies) und ihre Skizzen, die in diesem Zusammenbau (auch Baugruppe genannt) verwendet werden   *

-   Eine Grundplatte (grün)
-   Eine Kurbel (blau)
-   Zwei bewegliche Scheiben (rot und grau)
-   Vier Verbindungsstangen (weiß, gelb, lila und braun)

<img alt="" src=images/Assembly3_SketchSkeleton-01.png  style="width   *400px;"> 
*Alle acht Skizzen sind unterschiedlich eingefärbt und durch das Verschieben ihrer übergeordneten Körper, manuell positioniert*

Die Form kann von dem tatsächlichen Teil abweichen, aber die Position der Geometrien, die die Gelenke festlegen, müssen genau sein.

### Assembly-Container 

#### Übergeordneter Zusammenbau 

Um die Positionen aller Körper festzusetzen oder zu steuern, braucht man ein <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width   *16px;"> Assembly-Objekt. Das fügt dem Konstruktionsbaum in der [Baumansicht](Tree_view/de.md) einen Ast für den Zusammenbau hinzu.

-   Die Schaltfläche **<img src="images/Assembly_New_Assembly.svg‎‎" width=16px> [Create assembly](Assembly3_CreateAssembly/de.md)** drücken, um einen Zusammenbauast in der [Baumansicht](Tree_view/de.md) zu erstellen.

### Unterbaugruppen

Diese Aktion wiederholt man, um für jeden Körper (Body) ein Assembly-Objekt zu erstellen, in dessen Parts-Container das jeweilige Body-Objekt gezogen wird. Danach setzt man den Körper in seiner Baugruppe fest   *

1.  Das Assembly-Objekt aktivieren (Doppelklick).
2.  Einen Kreis/Bogen auswählen, der zum Body-Objekt gehört.
3.  Die Schaltfläche **<img src="images/Assembly_ConstraintLock.svg‎‎" width=16px> [Create "Locked" constraint](Assembly3_ConstraintLock/de.md)** drücken, um den Körper innerhalb seiner Unterbaugruppe festzusetzen.

Die Kurbelbaugruppe sollte beispielsweise so aussehen   *

<img alt="" src=images/Assembly3_SketchSkeleton-25.png  style="width   *500px;"> 
*Der Unterbaugruppenast der Kurbel in der Baumansicht und die Kurbel mit ihrem festgesetzten Element in der 3D-Ansicht*

#### Konstruktionsbaum

In der Baumansicht werden alle Unterbaugruppenäste in den Parts-Container des übergeordneten Assembly-Objekts gezogen.

<img alt="" src=images/Assembly3_SketchSkeleton-26.png  style="width   *300px;"> 
*Zusammenbauast in der Baumansicht*

Jetzt sind sie bereit, angeordnet zu werden.

### Festgesetzte Grundplatte 

Als Erstes braucht man ein unbewegliches Teil. Um die Grundplatte komplett festzusetzen, würde man normalerweise eine Fläche auswählen, aber in diesem Falle funktioniert es auch mit einem Kreis.

1.  Einen Kreis der Grundplatte auswählen.
2.  Die Schaltfläche **<img src="images/Assembly_ConstraintLock.svg‎‎" width=16px> [Create "Locked" constraint](Assembly3_ConstraintLock.md)** drücken, um die Grundplatte festzusetzen.

<img alt="" src=images/Assembly3_SketchSkeleton-02.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-03.png  style="width   *300px;"> 
*Der ausgewählte Kreis → Die festgesetzte Grundplatte mit dem erzeugten Element-Objekt dessen Element-Koordinatemsystem (EKS) angezeigt wird (grün)*

### Gelenke

For hinge-like joints we select one circle of each sketch and use the <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width   *16px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence.md) constraint. It not only sets both Element\'s XY planes coplanar, but sets their Z axes colinear, too.

1.  Select a circle of each object to connect.
2.  Press the **<img src="images/Assembly_ConstraintCoincidence.svg‎‎" width=16px> [Create "Plane Coincidence" constraint](Assembly3_ConstraintCoincidence.md)** button.

#### Grundplatte - Kurbel 

<img alt="" src=images/Assembly3_SketchSkeleton-04.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-05.png  style="width   *300px;"> 
*Circles on Base and Crank selected → Relocated Crank with the created Element objects and ECSs displayed (green)*

#### Grundplatte - Obere Scheibe 

<img alt="" src=images/Assembly3_SketchSkeleton-06.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-07.png  style="width   *300px;"> 
*Circles on Base and Upper Plate selected → Relocated Upper Plate*

Previously created joints can be identified by their constraint representations (red).

#### Kurbel - Stange 1 

<img alt="" src=images/Assembly3_SketchSkeleton-08.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-09.png  style="width   *300px;"> 
*Circles on Crank and Rod 1 selected → Relocated Rod 1 and tilted Crank*

#### Obere Scheibe - Stange 1 

The last link in this kinematic chain connects two Elements whose Z directions are already defined and a <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width   *16px;"> [Point on line](Assembly3_ConstraintPointOnLine.md) constraint is all we need.

1.  Select a circle of each object to connect.
2.  Press the **<img src="images/Assembly_ConstraintPointOnLine.svg‎‎" width=16px> [Create "PointOnLine" constraint](Assembly3_ConstraintPointOnLine.md)** button.

<img alt="" src=images/Assembly3_SketchSkeleton-10.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-11.png  style="width   *300px;"> 
*Circles on Upper Plate and Rod 1 selected → Relocated Rod 1, and tilted Crank and Upper Plate*

If the 3 joints are colinear (those belonging to Crank and Rod 1), the solver might fail to rearrange the objects. In that case we need to help the solver and tilt one object (e.g. the Crank) manually using the <img alt="" src=images/Assembly_AxialMove.svg  style="width   *16px;"> [Axial move](Assembly3_AxialMove.md) tool.

#### Obere Scheibe - Stange 2 

Another kinematic (sub-)chain starts with <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width   *16px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence.md) constraints.

<img alt="" src=images/Assembly3_SketchSkeleton-12.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-13.png  style="width   *300px;"> 
*Circles on Upper Plate (or Base) and Rod 2 selected → Relocated Rod 2*

#### Stange 2 - Untere Scheibe 

<img alt="" src=images/Assembly3_SketchSkeleton-14.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-15.png  style="width   *300px;"> 
*Circles on Rod 2 and Lower Plate selected → Relocated Lower Plate and tilted Rod 2*

#### Obere Scheibe - Stange 3 

<img alt="" src=images/Assembly3_SketchSkeleton-16.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-17.png  style="width   *300px;"> 
*Circles on Upper Plate and Rod 3 selected → Relocated Rod 3 and rearranged upper kinematic sub-chain*

#### Untere Scheibe - Stange 3 

And this kinematic (sub-)chain ends with a <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width   *16px;"> [Point on line](Assembly3_ConstraintPointOnLine.md) constraint, too.

<img alt="" src=images/Assembly3_SketchSkeleton-18.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-19.png  style="width   *300px;"> 
*Circles on Lower Plate and Rod 3 selected → Relocated Rod 3 and rearranged ukinematic sub-chains*

To connect both kinematic sub-chains we use Rod 4 with a <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width   *16px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence.md) constraint on one end and a <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width   *16px;"> [Point on line](Assembly3_ConstraintPointOnLine.md) constraint on the other.

#### Kurbel - Stange 4 

<img alt="" src=images/Assembly3_SketchSkeleton-20.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-21.png  style="width   *300px;"> 
*Circles on Crank and Rod 4 selected → Relocated Rod 4*

#### Untere Scheibe - Stange 4 

<img alt="" src=images/Assembly3_SketchSkeleton-22.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-23.png  style="width   *300px;"> 
*Circles on Lower Plate and Rod 4 selected → Relocated Rod 4 and final layout of kinematic assembly*

### Antrieb

Since Assembly3 doesn\'t provide any means to control kinematic assemblies, we need external assistance such as this [kinematic controller](Tutorial_KinematicController.md). To use this controller we need to mark one constraint\'s label with the suffix {{Incode|"Driver"}} to make it a driving constraint. It may be separated by a {{Incode|"."}} or {{Incode|"-"}} for clarity, as the controller will only check if the label ends with {{Incode|"Driver"}}.

We therefore change the label of the Base-Crank joint to {{Incode|Base-Crank.Driver}}.

### Fertiges Skelett 

The finished kinematic assembly with deactivated representation of Elements and Constraints should look like this   *

<img alt="" src=images/Assembly3_SketchSkeleton-24.png  style="width   *500px;"> 
*Finished assembly in the [Tree view](Tree_view.md) and the [3D view](3D_view.md)*

<img alt="" src=images/Assembly3_SketchSkeleton-27.gif  style="width   *500px;"> 
*GIF animation made from an image sequence from this [kinematic controller](Tutorial_KinematicController.md)*

## 3D-Geometrie befestigen 

My expectations about attaching a new object to a base object belonging to a kinematic assembly were something like   *

-   Put the new object into the base objects Parts container.
-   Position the new object in relation to the base object.
-   Fix the relative offset and orientation using the Attachment constraint.

But that would have been too easy.

The <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width   *16px;"> [Assembly3 ConstraintAttachment](Assembly3_ConstraintAttachment.md) tool, like any Assembly3 constraint tool, relies on the use of Element objects and their element coordinate systems (ECSs) for positioning tasks.

And so attaching objects is just another way of adding objects to a (sub-)assembly.

Let\'s attach Rod 4-3D to Rod 4 for example   *

The objects have a different orientation and the 3D object should have an offset from the 2D object.

1.  Put the new object into the base objects Parts container.
2.  Select two corresponding circles or arcs.
3.  Press the **<img src="images/Assembly_ConstraintAttachment.svg‎‎" width=16px> [Create "Attachment" constraint](Assembly3_ConstraintAttachment.md)**.

   *   <img alt="" src=images/Assembly3_SketchSkeleton-28.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-29.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-30.png  style="width   *200px;">



*Rod 4 (locked) and Rod 4-3D → Selected arcs → Relocated Rod 4-3D (both ECSs are in the same place with identical orientation)*

It is now plain to see that the <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width   *16px;"> [Assembly3 ConstraintAttachment](Assembly3_ConstraintAttachment.md) tool ignores the offset and orientation between both objects.

However the position is already defined as we wanted and so we only need to adapt the angle manually and define the desired offset   *

-   Set the **Offset, Angle** of the first Element in the Attachment container to match the orientation.
-   Set the **Offset, Position, z** of the same Element to apply an offset.

In case we set the properties of the second Element, the movement of angle and offset would go in the opposite direction.

   *   <img alt="" src=images/Assembly3_SketchSkeleton-30.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-31.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-32.png  style="width   *200px;">



*As attached → Angle adapted → Offset defined*

If there is a 3D object attached to each 2D object, it could look like this   *

<img alt="" src=images/Assembly3_SketchSkeleton-33.gif  style="width   *500px;">

## Hinweise

The section [Attaching 3D geometry](#Attaching_3D_geometry.md) just scratches the surface of extending a sub-assembly, and other constraints or combinations of constraints may be more suitable than the attachment constraint.

It is important to move such a kinematic assembly in tiny steps or the solver will give up and fail. It is almost impossible to use <img alt="" src=images/Assembly_Move.svg‎‎  style="width   *16px;"> [Move part](Assembly3_MovePart.md) or <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width   *16px;"> [Axial move](Assembly3_AxialMove.md) for this task.

The <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width   *16px;"> [Assembly3\_ConstraintCoincidence](Assembly3_ConstraintCoincidence.md) constraint is used to drive the kinematic assembly, its property **Angle** (enabled by the property **Lock Angle**) accepts positive or negative floating point numbers greater than 360 and so could do several full turns.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Tutorial KinematicSkeleton/de
