# Part Helix/ro
---
- GuiCommand:/ro   Name:Part Helix   Name/ro:Part Elice   MenuLocation:Part → [Workbenches:[[Part Workbench/ro|Part](Part_CreatePrimitives/ro___Create_Primitives]]_→_Helix.md),  [OpenSCAD](OpenSCAD_Workbench/ro.md)---


</div>


<div class="mw-translate-fuzzy">

## Descriere

Un element primitiv geometric este Elicea care este disponibilă din dialogul Create Primitives în Atelierul de lucru Part.


</div>

The **[<img src=images/Part_Helix.svg style="width:16px"> [Part Helix](Part_Helix.md)** geometric primitive creates a helix shape, defined by a radius, a pitch, and a total height.

A common usage for the helix primitive is for [creating screw threads](Thread_for_Screw_Tutorial.md) in conjunction with a closed profile, and the **<img src="images/Part_Sweep.svg" width=16px> [Sweep](Part_Sweep.md)** operation. This process works essentially the same in the [PartDesign Workbench](PartDesign_Workbench.md) by using the **[<img src=images/PartDesign_AdditivePipe.svg style="width:16px"> [PartDesign Additive pipe](PartDesign_AdditivePipe.md)** tool.


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

The Create Primitives dialogue can be accessed via the [CreatePrimitives](Part_CreatePrimitives.md) icon <img alt="" src=images/Part_CreatePrimitives.png  style="width:32px;"> located in the Part menu or the Part toolbar, in the Part Workbench. A common usage for the Helix is for [threads](Thread_for_Screw_Tutorial.md) in conjunction with the [sweep](Part_Sweep.md) operation.


</div>

![](images/PartHelixPrimitivesOptions_en.png )


<div class="mw-translate-fuzzy">

Sub Windows "Elica"

\|![](images/PartHelixPrimitivesOptions_it.png )

Sub Linux "Helix"

+++
| ![](images/PartHelixPrimitivesOptions_en.png ) | #### Parametrii                                                                                                                                                                                                                                                                      |
|                                                                            |                                                                                                                                                                                                                                                                                      |
|                                                                            | -                                                                                                                                                                                                                                                                     |
|                                                                            |     {{Parameter|Pitch:}}                                                                                                                                                                                                                                                             |
|                                                                            |                                                                                                                                                                                                                                                                                   |
|                                                                            |     Pasul corespunde spațiului dintre două \"întoarceri\" consecutive ale spiralei măsurate de-a lungul axei principale a spiralei.                                                                                                                                                  |
|                                                                            |                                                                                                                                                                                                                                                                                      |
|                                                                            | -                                                                                                                                                                                                                                                                     |
|                                                                            |     {{Parameter|Height:}}                                                                                                                                                                                                                                                            |
|                                                                            |                                                                                                                                                                                                                                                                                   |
|                                                                            |     The height corresponds to the overall height of the helix measured along the main axis of the helix.                                                                                                                                                                             |
|                                                                            |                                                                                                                                                                                                                                                                                      |
|                                                                            | -                                                                                                                                                                                                                                                                     |
|                                                                            |     {{Parameter|Radius:}}                                                                                                                                                                                                                                                            |
|                                                                            |                                                                                                                                                                                                                                                                                   |
|                                                                            |     The radius corresponds to the radius of the circle built by the helix by viewing the helix from the top / bottom.                                                                                                                                                                |
|                                                                            |                                                                                                                                                                                                                                                                                      |
|                                                                            | -                                                                                                                                                                                                                                                                     |
|                                                                            |     {{Parameter|Angle}}                                                                                                                                                                                                                                                              |
|                                                                            |                                                                                                                                                                                                                                                                                   |
|                                                                            |     : Per default the helix is built on a imaginary cylinder. With this option it is possible to build the helix on a imaginay conus. This angle corresponds to the angle of the conus. The value must be comprised between 0 and +90 deg.                                           |
|                                                                            |                                                                                                                                                                                                                                                                                      |
|                                                                            | -                                                                                                                                                                                                                                                                     |
|                                                                            |     {{Parameter|Right-handed or Left-handed:}}                                                                                                                                                                                                                                       |
|                                                                            |                                                                                                                                                                                                                                                                                   |
|                                                                            |     This parameter specifies the [handedness](https://en.wikipedia.org/wiki/Screw_thread) of the helix.                                                                                                                                                                              |
|                                                                            |                                                                                                                                                                                                                                                                                      |
|                                                                            | #### Location                                                                                                                                                                                                                                                                        |
|                                                                            |                                                                                                                                                                                                                                                                                      |
|                                                                            | -                                                                                                                                                                                                                                                                     |
|                                                                            |     {{Parameter|X:}}                                                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                                                                   |
|                                                                            |     The main axis of the helix will be translated along the x axis of the value you indicate in this field.                                                                                                                                                                          |
|                                                                            |                                                                                                                                                                                                                                                                                      |
|                                                                            | -                                                                                                                                                                                                                                                                     |
|                                                                            |     {{Parameter|Y:}}                                                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                                                                   |
|                                                                            |     The main axis of the helix will be translated along the y axis of the value you indicate in this field.                                                                                                                                                                          |
|                                                                            |                                                                                                                                                                                                                                                                                      |
|                                                                            | -                                                                                                                                                                                                                                                                     |
|                                                                            |     {{Parameter|Z:}}                                                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                                                                   |
|                                                                            |     The main axis of the helix will be translated along the z axis of the value you indicate in this field.                                                                                                                                                                          |
|                                                                            |                                                                                                                                                                                                                                                                                      |
|                                                                            | -                                                                                                                                                                                                                                                                     |
|                                                                            |     {{Parameter|Direction:}}                                                                                                                                                                                                                                                         |
|                                                                            |                                                                                                                                                                                                                                                                                   |
|                                                                            |     Per default the main axis of the helix is the z axis. Here you have the possibility to edit the main axis of the helix. If you select the parameter \"user defined\...\" , you will be invited to indicate the main axis of the helix by entering the coordinates of its vector. |
|                                                                            |                                                                                                                                                                                                                                                                                      |
|                                                                            | -                                                                                                                                                                                                                                                                     |
|                                                                            |     {{Parameter|3D View:}}                                                                                                                                                                                                                                                           |
|                                                                            |                                                                                                                                                                                                                                                                                   |
|                                                                            |     vă permite să selectați centrul în vizualizarea 3D                                                                                                                                                                                                                               |
+++


</div>

-    {{Parameter|Pitch:}}The pitch corresponds to the space between two consecutive \"turns\" of the helix measured along the main axis of the helix.

-    {{Parameter|Height:}}The height corresponds to the overall height of the helix measured along the main axis of the helix.

-    {{Parameter|Radius:}}The radius corresponds to the radius of the circle built by the helix by viewing the helix from the top or bottom.

-    {{Parameter|Angle}}: Per default the helix is built on a imaginary cylinder. With this option it is possible to build the helix on a imaginary cone. This angle corresponds to the angle of the cone. The value must be comprised between 0 and +90 deg.

-    {{Parameter|Right-handed or Left-handed:}}This parameter specifies the [handedness](https://en.wikipedia.org/wiki/Screw_thread) of the helix.

#### Location 

-    {{Parameter|X:}}The main axis of the helix will be translated along the x axis of the value you indicate in this field.

-    {{Parameter|Y:}}The main axis of the helix will be translated along the y axis of the value you indicate in this field.

-    {{Parameter|Z:}}The main axis of the helix will be translated along the z axis of the value you indicate in this field.

-    {{Parameter|Direction:}}Per default the main axis of the helix is the z axis. Here you have the possibility to edit the main axis of the helix. If you select the parameter \"user defined\...\" , you will be invited to indicate the main axis of the helix by entering the coordinates of its vector.

-    {{Parameter|3D View:}}allows you select center in the 3D view

## Opțiuni

### Properties

Odată ce ați creat elicea, aveți opțiunea de a modifica parametrii.

+++
| ![](images/PartHelixProperty_en.png ) | The parameters in this menu are similar to those described above.                |
|                                                          | **Base**                                                       |
|                                                          | \* {{Parameter|Placement:}} allows you to move or rotate the helix |
|                                                          |                                                                                  |
|                                                          | -                                                                 |
|                                                          |     {{Parameter|Angle:}}                                                         |
|                                                          |                                                                               |
+++



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Helix/ro
