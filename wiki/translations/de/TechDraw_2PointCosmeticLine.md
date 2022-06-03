---
- GuiCommand   */de
   Name   *TechDraw 2PointCosmeticLine
   Name/de   *TechDraw 2PunkteHilfslinie
   MenuLocation   *TechDraw → Linien hinzufügen →Hilfslinie durch 2 Punkte hinzufügen
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md)
   Version   *0.19
   SeeAlso   *[TechDraw Mittellinie zu Fläche(n)](TechDraw_FaceCenterLine/de.md), [TechDraw Mittellinie zwischen 2 Linien](TechDraw_2LineCenterLine/de.md)
---

# TechDraw 2PointCosmeticLine/de

## Beschreibung

Das Werkzeug <img alt="" src=images/TechDraw-line2points.svg  style="width   *16px;"> **2PunkteHilfslinie** fügt eine Hilfslinie zwischen zwei Knoten (Points) hinzu. Die Knoten können 2d oder 3d sein. Die resultierende Linie kann zur Bemaßung verwendet werden. Das Aussehen der Linie kann mit dem Werkzeug [Hilfsobjekt entfernen](TechDraw_CosmeticEraser/de.md) geändert werden.

<img alt="" src=images/CosLine2PointsSample.png  style="width   *200px;">



*Hilfslinie durch zwei Punkte*

## Anwendung

1.  Wähle 2 Knoten in einer Ansicht oder 2 Knoten in der 3D Ansicht.
2.  Drücke die **<img src="images/TechDraw-line2points.svg" width=16px> Hilfslinie durch 2 Punkte hinzufügen** Schaltfläche.
3.  Es öffnet sich ein Dialog, in dem du die Koordinaten der 2 Punkte anpassen kannst.
4.  Es wird eine Linie hinzugefügt, um die 2 ausgewählten Knoten zu verbinden. Im Fall von 3d Punkten verbindet die Linie die Projektion der ausgewählten Punkte.

Um eine Kosmetiklinie zu löschen, wähle sie aus und verwende die Werkzeugleistenschaltfläche **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Hilfsobjekt entfernen](TechDraw_CosmeticEraser/de.md)**.

## Kosmetik Linien bearbeiten 

Zum Ändern der Endpunkte einer Kosmetiklinie, **<img src="images/TechDraw-line2points.svg" width=16px> Hilfslinie durch 2 Punkte hinzufügen
**

1.  Wähle die Hilfslinie aus.
2.  Drücke **<img src="images/TechDraw-line2points.svg" width=16px> Hilfslinie durch 2 Punkte hinzufügen**.
3.  Ein Dialogfeld wird geöffnet, in dem du die Koordinaten der Endpunkte ändern kannst.
4.  Drücke **OK** um deine Änderungen zu sehen.

Um das Aussehen einer Kosmetiklinie zu ändern, verwende [Kosmetikobjekt entfernen](TechDraw_CosmeticEraser/de.md).

## Eigenschaften

Kosmetiklinien haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind.

## Skripten


**Siehe auch   ***

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Kosmetiklinien können mit den Methoden makeCosmeticLine(v1, v2) oder makeCosmeticLine3d(v1, v2) von DrawViewPart erzeugt werden.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2PointCosmeticLine/de
