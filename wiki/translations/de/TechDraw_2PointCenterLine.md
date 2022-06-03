---
- GuiCommand   */de
   Name   *TechDraw 2PointCenterLine
   Name/de   *TechDraw 2PunktMittelLinie
   MenuLocation   *TechDraw → Linien Hinzufügen → Mittellinie zwischen 2 Punkten hinzufügen
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md)
   Version   *0.19
   SeeAlso   *[TechDraw Mittellinie zu Fläche(n)](TechDraw_FaceCenterLine/de.md), [TechDraw Mittellinie zwischen 2 Linien](TechDraw_2LineCenterLine/de.md)
---

# TechDraw 2PointCenterLine/de

## Beschreibung

Das Werkzeug fügt eine Mittellinie hinzu, die zwischen zwei Punkten verlaufen soll.

<img alt="" src=images/CL2PointsSample.png  style="width   *200px;">



*Mittellinie zwischen zwei Punkten*

## Anwendung

1.  Wähle 2 Knoten in einer Ansicht.
2.  Drücke die **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> Mittellinie zwischen 2 Punkten hinzufügen** Schaltfläche
3.  Ein Dialogfeld wird geöffnet, in dem du die Attribute der neuen Mittellinie angeben kannst.
4.  Eine Mittellinie wird zwischen den 2 ausgewählten Knoten hinzugefügt.

Um eine Mittellinie zu löschen, wähle sie aus und verwende die Werkzeugleisteschaltfläche **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Kosmetikobjekt entfernen](TechDraw_CosmeticEraser/de.md)**.

## Bearbeiten von Mittellinien 

Eine der Befehlsschaltflächen für die Mittellinie ( **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> [Mittellinie zu Fläche(n) hinzufügen](TechDraw_FaceCenterLine/de.md)**, **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> [Mittellinie zwischen 2 Linien hinzufügen](TechDraw_2LineCenterLine/de.md)**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> Mittellinie zwischen 2 Punkten hinzufügen**) kann zur Bearbeitung jeder Mittellinie verwendet werden.

1.  Wähle eine Mittellinie.
2.  Drücke eine beliebige Befehlsschaltfläche der Mittellinie.
3.  Ein Dialogfeld wird geöffnet, in dem du die Attribute der Mittellinie ändern kannst.
4.  Drücke **OK**, um deine Änderungen zu sehen.

## Eigenschaften

Mittellinien haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind. Sie haben Attribute, die im Mittellinien Bearbeitungsdialog geändert werden können.

1.  Modus (Auswahlknöpfe)   *
    -   **Vertikal**   * Erzwingt eine vertikale Mittellinie
    -   **Horizontal**   * Erzwingt eine Mittellinie horizontal
    -   **Ausgerichtet**   * Folgt der allgemeinen Richtung von Kante für 2 Kanten Mittellinie
2.  **Shift Horiz**   * Verschiebt die Mittellinie nach links oder rechts von ihrer normalen Position
3.  **Shift Vert**   * Verschiebt die Mittellinie aus ihrer normalen Position nach oben oder unten
4.  **Rotate**   * Dreht die Mittellinie um ihren Mittelpunkt (Grad. + gegen den Uhrzeigersinn, - im Uhrzeigersinn)
5.  **Extend**   * Macht die Mittellinie um diesen Betrag länger
6.  **Color**   * Farbe der Mittellinie
7.  **Weight**   * Dicke der Mittellinie
8.  **Style**   * <img alt="" src=images/Continuous-line.svg  style="width   *20px;"> Durchgehend, <img alt="" src=images/Dash-line.svg  style="width   *20px;"> Strich, <img alt="" src=images/Dot-line.svg  style="width   *20px;"> Punkt, <img alt="" src=images/DashDot-line.svg  style="width   *20px;"> StrichPunkt, <img alt="" src=images/DashDotDot-line.svg  style="width   *20px;"> StrichPunktPunkt

## Skripten


**Siehe auch   ***

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Mittellinien sind zur Zeit noch nicht zugänglich über [Makros](Macros/de.md) und die [Python](Python/de.md) Konsole.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2PointCenterLine/de
