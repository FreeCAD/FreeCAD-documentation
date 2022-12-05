---
- GuiCommand:/de
   Name:TechDraw 2PointCosmeticLine
   Name/de:TechDraw 2PunkteHilfslinie
   MenuLocation:TechDraw → Linien hinzufügen →Mittellinie zwischen 2 Punkten hinzufügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Mittellinie zu Fläche(n) hinzufügen](TechDraw_FaceCenterLine/de.md), [TechDraw Mittellinie zwischen 2 Linien hinzufügen](TechDraw_2LineCenterLine/de.md)
---

# TechDraw 2PointCosmeticLine/de

## Beschreibung

Das Werkzeug <img alt="" src=images/TechDraw-line2points.svg  style="width:16px;"> **2PunkteHilfslinie** fügt eine Hilfslinie zwischen zwei Knoten (Points) hinzu. Die Knoten können 2D oder 3D sein. Die resultierende Linie kann zur Bemaßung verwendet werden. Das Aussehen der Linie kann mit dem Werkzeug [Liniendarstellung ändern](TechDraw_DecorateLine/de.md) geändert werden.

<img alt="" src=images/CosLine2PointsSample.png  style="width:200px;">



*Hilfslinie durch zwei Punkte*

## Anwendung

1.  2 Knoten in einer Ansicht auswählen oder 2 Knoten in der 3D-Ansicht.
2.  Die Schaltfläche **<img src="images/TechDraw-line2points.svg" width=16px> Hilfslinie durch 2 Punkte hinzufügen** drücken.
3.  Ein Dialog wird geöffnet, in dem die Koordinaten der 2 Punkte angepasst werden können.
4.  Eine Linie wird hinzugefügt, die die 2 ausgewählten Knoten verbindet. Im Fall von 3D-Punkten verbindet die Linie die Projektion der ausgewählten Punkte.

## Hilfslinien bearbeiten 

Zum Ändern der Endpunkte einer Hilfslinie:

1.  Eine Hilfslinie auswählen.

2.  Die Schaltfläche **<img src="images/TechDraw-line2points.svg" width=16px> Hilfslinie durch 2 Punkte hinzufügen** drücken.

3.  Ein Dialogfeld wird geöffnet, in dem die Koordinaten der Endpunkte geändert werden können.

4.  
    **OK**drücken, um die Änderungen zu sehen.

Zum Löschen einer Hilfslinie wird die Schaltfläche **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Hilfsobjekt entfernen](TechDraw_CosmeticEraser/de.md)** verwendet.

Um das Aussehen einer Hilfslinie zu ändern, wird <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [Liniendarstellung ändern](TechDraw_DecorateLine/de.md) verwendet.

## Eigenschaften

Hilfslinien haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind.

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Hilfslinien können mit den Methoden makeCosmeticLine(v1, v2) oder makeCosmeticLine3d(v1, v2) von DrawViewPart erzeugt werden.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2PointCosmeticLine/de
