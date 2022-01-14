# Part Helix/de
---
- GuiCommand:/de   Name:Part Helix   Name/de:Part Helix   MenuLocation:Formteil → [Workbenches:[[Part_Workbench/de|Part](Part_CreatePrimitives/de___Grundkörper_erstellen...]] → Helix.md), [OpenSCAD](OpenSCAD_Workbench/de.md)---


</div>


<div class="mw-translate-fuzzy">

## Beschreibung

Ein Helix-Grundkörper ist im **Grundkörper erstellen**-Dialog im Part-Arbeitsbereich verfügbar.


</div>

The **[<img src=images/Part_Helix.svg style="width:16px"> [Part Helix](Part_Helix.md)** geometric primitive creates a helix shape, defined by a radius, a pitch, and a total height.

A common usage for the helix primitive is for [creating screw threads](Thread_for_Screw_Tutorial.md) in conjunction with a closed profile, and the **<img src="images/Part_Sweep.svg" width=16px> [Sweep](Part_Sweep.md)** operation. This process works essentially the same in the [PartDesign Workbench](PartDesign_Workbench.md) by using the **[<img src=images/PartDesign_AdditivePipe.svg style="width:16px"> [PartDesign Additive pipe](PartDesign_AdditivePipe.md)** tool.


<div class="mw-translate-fuzzy">

## Anwendung


</div>


<div class="mw-translate-fuzzy">

Der \'Geometrische Grundkörper\'-Dialog kann über **Formteil** → **<img src="images/Part_CreatePrimitives.png" width=32px> Grundkörper erstellen...** aus der Menüleiste oder über <img alt="" src=images/Part_CreatePrimitives.png  style="width:32px;"> aus der Part-Werkzeugleiste im Part-Arbeitsbereich ausgewählt werden. Eine übliche Verwendung für die Helix ist für [Gewinde](Thread_for_Screw_Tutorial/de.md) in Verbindung mit der [Sweep](Part_Sweep/de.md)-Operation.


</div>

![](images/PartHelixPrimitivesOptions_en.png )


<div class="mw-translate-fuzzy">

+----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/PartHelixPrimitivesOptions_en.png ) | #### Parameter                                                                                                                                                                                              |
|                                                                            |                                                                                                                                                                                                             |
|                                                                            | -                                                                                                                                                                                            |
|                                                                            |     {{Parameter|Steigung:}}                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                          |
|                                                                            |     Die Steigung entspricht dem Platz zwischen zwei aufeinanderfolgenden \"Umdrehungen\" der Helix gemessen an der Hauptachse der Helix.                                                                    |
|                                                                            |                                                                                                                                                                                                             |
|                                                                            | -                                                                                                                                                                                            |
|                                                                            |     {{Parameter|Höhe:}}                                                                                                                                                                                     |
|                                                                            |                                                                                                                                                                                                          |
|                                                                            |     Die Höhe entspricht der gesamten Höhe der Helix an der Hauptachse.                                                                                                                                      |
|                                                                            |                                                                                                                                                                                                             |
|                                                                            | -                                                                                                                                                                                            |
|                                                                            |     {{Parameter|Radius:}}                                                                                                                                                                                   |
|                                                                            |                                                                                                                                                                                                          |
|                                                                            |     Der Radius entspricht dem durch die Helix erzeugten Radius gesehen von der Spitze/dem Boden aus.                                                                                                        |
|                                                                            |                                                                                                                                                                                                             |
|                                                                            | -                                                                                                                                                                                            |
|                                                                            |     {{Parameter|Winkel}}                                                                                                                                                                                    |
|                                                                            |                                                                                                                                                                                                          |
|                                                                            |     : Als Vorgabewert wird die Helix auf einem imaginären Zylinger erstellt (0°). Mit dieser Option ist es möglich, die Helix auf einem Kegel zu erstellen. Der Winkel muss zwischen 0 und +90 Grad liegen. |
|                                                                            |                                                                                                                                                                                                             |
|                                                                            | -                                                                                                                                                                                            |
|                                                                            |     {{Parameter|Koordinatensystem:}}                                                                                                                                                                        |
|                                                                            |                                                                                                                                                                                                          |
|                                                                            |     Dieser Parameter gibt die [Drehrichtung](https://de.wikipedia.org/wiki/Gewinde#Drehrichtung_des_Gewindes) (Rechtdrehend/Linksdrehend) der Helix an.                                                     |
|                                                                            |                                                                                                                                                                                                             |
|                                                                            | #### Lage                                                                                                                                                                                                   |
|                                                                            |                                                                                                                                                                                                             |
|                                                                            | -                                                                                                                                                                                            |
|                                                                            |     {{Parameter|X:}}                                                                                                                                                                                        |
|                                                                            |                                                                                                                                                                                                          |
|                                                                            |     Der Abstand der Hauptachse der Helix vom Ursprung entlang der X-Achse.                                                                                                                                  |
|                                                                            |                                                                                                                                                                                                             |
|                                                                            | -                                                                                                                                                                                            |
|                                                                            |     {{Parameter|Y:}}                                                                                                                                                                                        |
|                                                                            |                                                                                                                                                                                                          |
|                                                                            |     Der Abstand der Hauptachse der Helix vom Ursprung entlang der Y-Achse.                                                                                                                                  |
|                                                                            |                                                                                                                                                                                                             |
|                                                                            | -                                                                                                                                                                                            |
|                                                                            |     {{Parameter|Z:}}                                                                                                                                                                                        |
|                                                                            |                                                                                                                                                                                                          |
|                                                                            |     Der Abstand der Hauptachse der Helix vom Ursprung entlang der Z-Achse.                                                                                                                                  |
|                                                                            |                                                                                                                                                                                                             |
|                                                                            | -                                                                                                                                                                                            |
|                                                                            |     {{Parameter|Richtung:}}                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                          |
|                                                                            |     Als Standardwert zeigt die Hauptachse der Helix in die Z-Richtung. Hier lässt sich die Richtung ändern. Bei der Angabe \"Benutzerdefiniert\...\" lässt sich die Richtung durch einen Vektor angeben.    |
|                                                                            |                                                                                                                                                                                                             |
|                                                                            | -                                                                                                                                                                                            |
|                                                                            |     {{Parameter|3D-Ansicht:}}                                                                                                                                                                               |
|                                                                            |                                                                                                                                                                                                          |
|                                                                            |     gibt das Zentrum der 3D-Ansicht an                                                                                                                                                                      |
+----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


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

## Optionen

### Eigenschaften

Sobald die Helix erstellt ist, lassen sich die Parameter ändern.

+----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ![](images/PartHelixProperty_en.png ) | Die Parameter in diesem Menü entsprechen den oben beschriebenen.                          |
|                                                          | **Base**                                                                |
|                                                          | \* {{Parameter|Placement:}} Erlaubt die Verschiebung oder Drehung der Helix |
|                                                          |                                                                                           |
|                                                          | -                                                                          |
|                                                          |     {{Parameter|Winkel:}}                                                                 |
|                                                          |                                                                                        |
+----------------------------------------------------------+-------------------------------------------------------------------------------------------+

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Helix/de
