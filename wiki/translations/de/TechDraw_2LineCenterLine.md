---
- GuiCommand:/de
   Name:TechDraw 2LineCenterLine
   Name/de:TechDraw 2LinienMittelLinie
   MenuLocation:TechDraw → Linien hinzufügen → Mittellinie zwischen 2 Linien hinzufügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Mittellinie zu Fläche(n)](TechDraw_FaceCenterLine/de.md), [TechDraw Mittellinie zwischen 2 Punkten](TechDraw_2PointCenterLine/de.md)
---

# TechDraw 2LineCenterLine/de

## Beschreibung

Das 2LinienMittelLinie Werkzeug fügt eine Mittellinie zwischen zwei Kanten hinzu.

<img alt="" src=images/CL2LinesSample.png  style="width:350px;">



*Ausgerichtete Mittellinie zwischen 2 Kanten*

## Anwendung

1.  Wähle zwei Kanten in einer Ansicht. Die Kanten sollten mehr oder weniger parallel sein.
2.  Drücke den **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> Mittellinie zwischen 2 Linien hinzufügen** Schaltfläche
3.  Ein Dialogfeld wird geöffnet, in dem du die Attribute der neuen Mittellinie angeben kannst.
4.  Eine Mittellinie wird zwischen den 2 ausgewählten Kanten hinzugefügt.**Wenn die erzeugte Linie seltsam aussieht oder überhaupt nicht erzeugt wurde, musst du eventuell die Option** [**Klappe Enden**](#Flip_Ends.md) verwenden.

Um eine Mittellinie zu löschen, wähle sie aus und verwende die Werkzeugleisteschaltfläche **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Kosmetikobjekt entfernen](TechDraw_CosmeticEraser/de.md)**.

## Bearbeiten von Mittellinien 

Eine der Befehlsschaltflächen für die Mittellinie ( **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> [Mittellinie zu Fläche(n) hinzufügen](TechDraw_FaceCenterLine/de.md)**, **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> [Mittellinie zwischen 2 Linien hinzufügen](TechDraw_2LineCenterLine/de.md)**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> [Mittellinie zwischen 2 Punkten hinzufügen](TechDraw_2PointCenterLine.md)**) kann zur Bearbeitung jeder Mittellinie verwendet werden.

1.  Wähle eine Mittellinie.
2.  Drücke eine beliebige Befehlsschaltfläche der Mittellinie.
3.  Ein Dialogfeld wird geöffnet, in dem du die Attribute der Mittellinie ändern kannst.
4.  Drücke **OK**, um deine Änderungen zu sehen.

## Eigenschaften

Mittellinien haben keine eigenen Eigenschaften, da sie keine Objekte innerhalb der Zeichnung sind. Sie besitzen Attribute die im zugehörigen Dialogfeld geändert werden können.

-   **Orientation**:
    -   **Vertikal**: Erzwingt eine vertikale Mittellinie
    -   **Horizontal**: Erzwingt eine Mittellinie horizontal
    -   **Ausgerichtet**: Folgt der allgemeinen Richtung von Kante für 2 Kanten Mittellinie
-   **Shift Horizontal**: Verschiebt die Mittellinie nach links oder rechts von ihrer normalen Position
-   **Shift Vertical**: Verschiebt die Mittellinie aus ihrer normalen Position nach oben oder unten
-   **Rotate**: Dreht die Mittellinie um ihren Mittelpunkt (Grad. + gegen den Uhrzeigersinn, - im Uhrzeigersinn)
-   **Extend By**: Macht die Mittellinie um diesen Betrag länger
-   **Color**: Farbe der Mittellinie
-   **Weight**: Dicke der Mittellinie
-   **Style**: <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Durchgehend, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Strich, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Punkt, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> StrichPunkt, <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> StrichPunktPunkt
-   **Enden Umklappen**: Klappt Endpunkte für die Erstellung wie unten beschrieben um (Attribut entfernt für FreeCAD 0.20)

## Enden Umklappen 

<img alt="Darstellung zur Erstellung einer Mittellinie" src=images/TD-CenterLineFlip.png  style="width:350px;"> Die Mittellinie zwischen zwei schrägen Linien (Linie 1 und Linie 2), wird erstellt aus den Mittelpunkten (m0 und m1) der Verbindunsglinien der Endpunkte der beiden Linien - siehe Darstellung. Abhängig von den gewählten Endpunkten ergeben sich mehrere Möglichkeiten für die Verbindungslinien. Das Attribut **Flip Ends** klappt die Weise um, wie Verbindungslinien gezeichnet werden. In FreeCAD 0.20 wird die Punktreihenfolge automatisch festgelegt, so dass das **Flip Ends**-Attribut nicht länger notwendig ist.

## Skripten


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Programmierung/Skripte](FreeCAD_Scripting_Basics/de.md).

Mittellinien sind zur Zeit noch nicht zugänglich über [Makros](Macros/de.md) und die [Python](Python/de.md) Konsole.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2LineCenterLine/de
