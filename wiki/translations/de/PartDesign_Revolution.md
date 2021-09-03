---
- GuiCommand:/de
   Name:PartDesign Revolution
   Name/de:PartDesign Drehung
   MenuLocation:PartDesign → Drehung
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
---


</div>

## Beschreibung

Das **Drehung**swerkzeug erstellt einen Festkörper aus der Drehung einer Skizze oder eines 2D Objekts um eine gegebene Achse. ![](images/PartDesign_Revolution_example.svg ) *Oben: Skizze (A) wird um 270 Grad gegen den Uhrzeigersinn um die Achse (B) gedreht; der resultierende Festkörper (C) ist rechts dargestellt.*

## Anwendung

1.  Wählen die Skizze aus, die gedreht werden soll.  v0.17 und höher  Alternativ kann eine Fläche des vorhandenen Festkörpers verwendet werden.
2.  Drücken die **<img src="images/_PartDesign_Revolution.svg" width=24px> '''Drehung'''** Taste.
3.  Lege die Drehungsparameter fest (siehe nächster Abschnitt).
4.  Drücke {{KEY | OK}}.

## Optionen

Bei der Erstellung einer Drehung bietet der **Drehungsparameter** einige Parameter an, die angeben, wie die Skizze gedreht werden soll.

+----------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/partdesign_revolution_parameters-de.png ) | ### Achse                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                        | Diese Option gibt an um welche Achse die Skizze zu rotieren ist.                                                                                                                                                                                                                                                                                                                                        |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                        | -   **Vertikale Skizzenachse**: Wählt die Vertikale Achse der Skizze.                                                                                                                                                                                                                                                                                                                                   |
|                                                                                        | -   **Horizontale Skizzenachse**: Wählt die Horizontale Achse der Skizze.                                                                                                                                                                                                                                                                                                                               |
|                                                                                        | -   **Skizzenachse**: v0.16 und älter wählt eine Konstruktionslinie aus der Skizze. Die erste Konstruktionsline aus der Skizze wird als *Konstruktionslinie 1* bezeichnet.Die Liste enhält weitere *Konstruktionlinie 2..n* soweit in der Skizze vorhanden.                                                                        |
|                                                                                        | -   **Konstruktionslinie n**: v0.17 und danach wählt eine Konstruktionslinie aus der Skizze. Die erste Konstruktionsline aus der Skizze wird als *Konstruktionslinie 1* bezeichnet.Die Liste enhält weitere *Konstruktionlinie 2..n* soweit in der Skizze vorhanden.                                                              |
|                                                                                        | -   **Basis (X/Y/Z) Achse**: v0.17 und danach  selektiert die X, Y oder Z aachse aus dem Usrpung der Form (Body);                                                                                                                                                                                                                 |
|                                                                                        | -   **Referenz auswählen\...**: v0.17 und danach erlaubt die selektion einer Kante der Form oder einer [Bezugslinie](PartDesign_Line/de.md).                                                                                                                                                                              |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                        | ### Winkel                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                        | Dies steuert den Winkel, über den die Rotation zu bilden ist, z. 360 ° wäre eine vollständige, zusammenhängende Rotation. Die Bilder im Abschnitt [ Beispiele](#Beispiele.md) zeigen einige der Möglichkeiten bei der Angabe verschiedener Winkel. Es ist nicht möglich, negative Winkel anzugeben (verwenden Sie stattdessen die Option \'\' \'Umgekehrt\' \'\') oder Winkel größer als 360 °. |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                        | ### Symmetrisch zu Ebene                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                        | Wenn diese Option aktiviert ist, wird die Drehung um die Hälfte des angegebenen Winkels in beide Richtungen von der Skizzierebene aus verlängert.                                                                                                                                                                                                                                                       |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                        | ### Umgekehrt                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                        | Wenn diese Option aktiviert ist, wird die Drehrichtung von Standard im Uhrzeigersinn gegen den Uhrzeigersinn umgekehrt.                                                                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+




## Eigenschaften

Unterhalb wird beschrieben, welche Eigenschaften im Nachhinein änderbar sind. *Basis* und *Achse* sind nicht änderbar.

-    {{PropertyData/de|Winkel}}: Drehwinkel der Rotation. Siehe [Winkel](#Angle.md).

-    {{PropertyData/de|Beschriftung}}: Frei wählbarer Name der Rotation.

-    {{PropertyData/de|Mittelebene}}: true oder false. Siehe [Symmetrisch zu Ebene](#Symmetric_to_plane/de.md).

-    {{PropertyData/de|Umkekehrt}}: true oder false. Siehe [Umgekehrt](#Umgekehrt.md).

-    {{PropertyData/de|Verfeinern}}: v0.17 und höher true oder false. Wenn auf true gesetzt wird die Form von überflüssigen Restkanten bereingt . Siehe [Part Form verfeinern](Part_RefineShape/de.md) für weitere Details.

## Beispiele

![Beispiel Drehung mit einer Konstruktionslinie als Umdrehungsachse: In diesem Bild ist der Winkel 75 °, die Umdrehung ist um die Konstruktionslinie (Skizzenachse 0)](images/PartDesign_Revolution_axis_fromconstructionlines1.jpg ) 

## Hilfreiche Verweise 

Ein [ausführliches Anwendungsbeispiel](http://forum.freecadweb.org/viewtopic.php?f=3&t=3674) im Forum.





{{PartDesign Tools navi

}} 
