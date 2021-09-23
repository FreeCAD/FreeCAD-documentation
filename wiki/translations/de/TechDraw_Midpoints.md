---
- GuiCommand:/de
   Name:TechDraw Midpoints
   Name/de:TechDraw Mittenpunkte
   MenuLocation:TechDraw → Knoten hinzufügen → Mittenpunktknoten hinzufügen
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.19
   SeeAlso:[TechDraw Kosmetik Knoten](TechDraw_CosmeticVertex/de.md), [TechDraw Quadrantenknoten](TechDraw_Quadrants/de.md)
---

# TechDraw Midpoints/de

## Beschreibung

Das Mittenpunkte Werkzeug fügt kosmetische [Knoten (=Vertices)](Glossary/de#V.md) an den Mittenpunkten einer oder mehrerer Kanten hinzu.

<img alt="" src=images/TechDraw_CosmeticMidpoint_Sample.png  style="width:250px;"> 
*Kosmetische Knoten an Kantenmittenpunkten*

## Anwendung

1.  Wähle eine oder mehrere Kanten in einer Ansicht aus.
2.  Drücke die **<img src="images/TechDraw_Midpoints.svg" width=16px> Mittenpunktknoten hinzufügen** Taste.
3.  Kosmetischen Knoten werden an den Mittenpunkt(en) der Kante(n) hinzugefügt.

Um einen Mittenpunkt zu löschen, wähle ihn aus und verwende die Werkzeugleistenschaltfläche **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Kosmetikobjekt entfernen](TechDraw_CosmeticEraser/de.md)**.

## Eigenschaften

Kosmetische Knoten haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind. Sie teilen Farb- und Größeneinstellungen mit regulären Geometrieknoten.

## Skripten


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Kosmetikknoten sind zur Zeit nicht über [Makros](Macros/de.md) oder die [Python](Python/de.md) Konsole zugänglich. Dieser Schnipsel entfernt alle Kosmetikknoten aus der Ansicht.


```python
>>> v = App.ActiveDocument.View
>>> v.clearCV()
>>> App.activeDocument().recompute()
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Midpoints/de
