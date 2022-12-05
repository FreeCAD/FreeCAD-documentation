---
- GuiCommand:/de
   Name:TechDraw FaceCenterLine
   Name/de:TechDraw FlächenMittelLinie
   MenuLocation:TechDraw → Linien hinzufügen → Mittellinie zu Fläche(n) hinzufügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Kosmetikknoten](TechDraw_CosmeticVertex/de.md), [TechDraw Mittellinie zwischen 2 Linien](TechDraw_2LineCenterLine/de.md), [TechDraw Mittellinie zwischen 2 Punkten](TechDraw_2PointCenterLine/de.md), [TechDraw Kosmetikradierer](TechDraw_CosmeticEraser/de.md)
---

# TechDraw FaceCenterLine/de

## Beschreibung

Das Werkzeug fügt einer Fläche eine Mittellinie durch ihren Mittelpunkt zu.

<img alt="" src=images/TechDraw_FaceCenterLine_Sample.png  style="width:400px;"> 
*Mittellinie einer Fläche zufügen (links: Fläche ausgewählt / rechts: Mittellinie zugefügt)*

## Anwendung

1.  Wähle eine oder mehrere Flächen in einer Ansicht.
2.  Drücke die **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> Mittellinie zu Fläche(n) hinzufügen**.
3.  Ein Dialogfeld wird geöffnet, in dem du die Attribute der neuen Mittellinie angeben kannst.
4.  Eine Mittellinie wird in der Mitte des Begrenzungsrahmens der ausgewählten Fläche(n) hinzugefügt.

Um eine Mittellinie zu löschen, wähle sie aus und verwende die Werkzeugleistenschaltfläche **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Kosmetikobjekt entfernen](TechDraw_CosmeticEraser/de.md)**.

## Bearbeite Mittellinien 

Alle Werkzeuge für Mittellinien (**<img src="images/TechDraw_FaceCenterLine.svg" width=16px> Mittellinie zu Fläche(n) hinzufügen**, **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> [Mittellinie zwischen 2 Linien hinzufügen](TechDraw_2LineCenterLine/de.md)**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> [Mittellinie zwischen 2 Punkten hinzufügen](TechDraw_2PointCenterLine/de.md)**) können verwendet werden um Mittellinien zu ändern.

1.  Wähle eine Mittellinie.
2.  Drücke eine beliebige Befehlsschaltfläche der Mittellinie.
3.  Ein Dialogfeld wird geöffnet, in dem du die Attribute der Mittellinie ändern kannst.
4.  Drücke **OK**, um deine Änderungen zu sehen.

## Eigenschaften

Mittellinien haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte innerhalb der Zeichnung sind. Sie haben Attribute die im Mittellinienbearbeitungs Dialog geändert werden können.

1.  Modus (Auswahlknöpfe):
    -   **Vertikal**: Erzwingt eine vertikale Mittellinie
    -   **Horizontal**: Erzwingt eine Mittellinie horizontal
    -   **Ausgerichtet**: Folgt der allgemeinen Richtung von Kante für 2 Kanten Mittellinie
2.  **Shift Horiz**: Verschiebt die Mittellinie nach links oder rechts von ihrer normalen Position
3.  **Shift Vert**: Verschiebt die Mittellinie aus ihrer normalen Position nach oben oder unten
4.  **Rotate**: Dreht die Mittellinie um ihren Mittelpunkt (Grad. + gegen den Uhrzeigersinn, - im Uhrzeigersinn)
5.  **Extend**: Macht die Mittellinie um diesen Betrag länger
6.  **Color**: Farbe der Mittellinie
7.  **Weight**: Dicke der Mittellinie
8.  **Style**: <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Durchgehend, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Strich, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Punkt, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> StrichPunkt, <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> StrichPunktPunkt

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Mittellinien sind zur Zeit noch nicht zugänglich über [Makros](Macros/de.md) und die [Python](Python/de.md) Konsole.

## Hinweise

-   FlächenMittelLinie wird eventuell zwei Ansichtseigenschaften ersetzen:
    -   
        **HorizMittelLinie**
        
        : Zeigt eine horizontale Mittellinie durch die Ansicht.

    -   
        **VertMittelLinie**
        
        : Zeigt eine vertikale Mittellinie durch die Ansicht.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw FaceCenterLine/de
