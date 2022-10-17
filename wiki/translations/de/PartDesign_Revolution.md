---
- GuiCommand   */de
   Name   *PartDesign Revolution
   Name/de   *PartDesign Drehteil
   MenuLocation   *Part Design → Objekte hinzufügen → Drehteil
   Workbenches   *[PartDesign](PartDesign_Workbench/de.md)
   SeeAlso   *[PartDesign Nut](PartDesign_Groove/de.md)
---

# PartDesign Revolution/de

## Beschreibung

Das Werkzeug **Drehkörper** erstellt einenVolumenkörper durch Rotation einer Skizze oder eines 2D-Objekts um eine gegebene Achse.

![](images/PartDesign_Revolution_example.svg ) 
*Oben   * Skizze (A) wird um 270 Grad gegen den Uhrzeigersinn um die Achse (B) gedreht; der resultierende Volumenkörper (C) ist rechts dargestellt.*

## Anwendung

1.  Die Skizze auswählen, die rotiert werden soll.  v0.17 und höher  Alternativ kann eine Fläche des vorhandenen Volumenkörpers verwendet werden.

2.  Die Schaltfläche **<img src="images/_PartDesign_Revolution.svg" width=24px> '''Drehteil'''** drücken.

3.  Drehparameter festlegen (siehe nächster Abschnitt).

4.  
    **OK**drücken.

## Optionen

Bei der Erstellung eines Drehteils bietet der Dialog **Parameter der Rotation** einige Parameter an, die angeben, wie die Skizze gedreht werden soll.

  
  ![](images/partdesign_revolution_parameters.png )
  

### Achse

Diese Option gibt die Achse an, um welche die Skizze zu rotieren ist.

-   **Vertikale Skizzenachse**   * Wählt die vertikale Achse der Skizze.
-   **Horizontale Skizzenachse**   * Wählt die horizontale Achse der Skizze.
-   **Skizzenachse**   * v0.16 und älter wählt eine Konstruktionslinie aus der Skizze, die zur Rotation verwendet wurde. Die erste Konstruktionsline aus der Skizze wird als *Sketch axis 0* bezeichnet. Die Aufklappliste enhält eine benutzerspezifische Skizzenachse für jede Konstruktionslinie.
-   **Konstruktionslinie**   * v0.17 und danach wählt eine Konstruktionslinie aus der Skizze, die von der Rotation verwendet wurde. Die Aufklappliste wird eine Eingabe für jede Konstruktionslinie enthalten. Die erste Konstruktionslinie, die in der Skizze erstellt wurde, wird mit *Konstruktionslinie 1* bezeichnet.
-   **Basis (X/Y/Z) Achse**   * v0.17 und danach  wählt die X-, Y- oder Z-Achse aus dem Usrpung der Form (Body);
-   **Referenz auswählen\...**   * v0.17 und danach erlaubt die Auswahl einer Kante der Form oder einer [Bezugslinie](PartDesign_Line/de.md) in der 3D-Ansicht.

### Winkel

Dies steuert den Winkel, über den die Rotation zu bilden ist. 360 ° wäre z.B. eine vollständige, zusammenhängende Rotation. Die Bilder im Abschnitt [ Beispiele](#Examples.md) zeigen einige der Möglichkeiten bei der Angabe verschiedener Winkel. Es ist nicht möglich, negative Winkel anzugeben (verwenden Sie stattdessen die Option *\'Umgekehrt\'*) oder Winkel größer als 360 °.

### Symmetrisch zur Ebene 

Wenn ausgewählt, wird die Rotation um die Hälfte des angegeben Winkels erweiterte in beide Richtungen der Skizzenebene.

### Umgekehrt

Wenn ausgewählt, ist die Rotationsrichtung umgekehrt zur vorgegebenen Richtung im Uhrzeigersinn.

## Eigenschaften

Unterhalb wird beschrieben, welche Eigenschaften im Nachhinein änderbar sind. *Basis* und *Achse* sind nicht änderbar.

-    {{PropertyData/de|Winkel}}   * Drehwinkel der Rotation. Siehe [Winkel](#Angle.md).

-    {{PropertyData/de|Beschriftung}}   * Frei wählbarer Name der Rotation.

-    {{PropertyData/de|Mittelebene}}   * true oder false. Siehe [Symmetrisch zu Ebene](#Symmetric_to_plane/de.md).

-    {{PropertyData/de|Umkekehrt}}   * true oder false. Siehe [Umgekehrt](#Umgekehrt.md).

-    {{PropertyData/de|Verfeinern}}   * v0.17 und höher true oder false. Wenn auf true gesetzt wird die Form von überflüssigen Restkanten bereingt . Siehe [Part Form verfeinern](Part_RefineShape/de.md) für weitere Details.

## Beispiele

![Beispiel Rotation mit einer Konstruktionslinie als Rotationsachse   * In diesem Bild ist der Winkel 75 °, die Rotation ist um die Konstruktionslinie (Skizzenachse 0)](images/PartDesign_Revolution_axis_fromconstructionlines1.jpg )

## Hilfreiche Verweise 

Ein [ausführliches Anwendungsbeispiel](http   *//forum.freecadweb.org/viewtopic.php?f=3&t=3674) im Forum.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Revolution/de
