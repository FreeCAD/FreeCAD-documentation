---
- GuiCommand:/de
   Name:TechDraw Quadrants
   Name/de:TechDraw Quadranten
   MenuLocation:TechDraw → Knoten hinzufügen → Quadranten Knoten hinzufügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Kosmetikknoten](TechDraw_CosmeticVertex/de.md), [TechDraw Mittenpunkt](TechDraw_Midpoints/de.md)
---

# TechDraw Quadrants/de

## Beschreibung

Das Quadranten Werkzeug fügt [kosmetische Knoten](TechDraw_CosmeticVertex/de.md) an den 90/180/270° Punkten einer Kreiskante hinzu. Der 0° Knoten sollte bereits als geometrischer Knoten vorhanden sein.

<img alt="" src=images/TechDraw_CosmeticQuadrant_Sample.png  style="width:250px;"> 
*Kosmetische Knoten an Quadrantenpunkten eines Kreises*

## Anwendung

1.  Wähle eine oder mehrere (kreisförmige) Kanten in einer Ansicht aus.
2.  Drücke die **<img src="images/TechDraw_Quadrants.svg" width=16px> Quadrantenknoten hinzufügen** Taste.
3.  Kosmetischen Knoten werden an den Viertelpunkten der Kanten hinzugefügt.

**Anmerkung:**Dieses Werkzeug kann an jeder Kante verwendet werden, nicht nur an Kreisen.

Um einen Quadrantenknoten zu löschen, wähle ihn aus und verwende die Werkzeugleistenschaltfläche **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Kosmetikobjekt entfernen](TechDraw_CosmeticEraser/de.md)**.

## Eigenschaften

Quadrantenknoten haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind. Sie teilen Farb- und Größeneinstellungen mit regulären Geometrieknoten.

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Kosmetische Knoten sind zur Zeit nicht über [Makros](Macros/de.md) oder die [Python](Python/de.md) Konsole zugänglich. Dieser Schnipsel entfernt alle Kosmetische Knoten aus der Ansicht.


```python
>>> v = App.ActiveDocument.View
>>> v.clearCV()
>>> App.activeDocument().recompute()
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Quadrants/de
