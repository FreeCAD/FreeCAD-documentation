---
- GuiCommand:/de
   Name:TechDraw CosmeticVertex
   Name/de:TechDraw KosmetikKnoten
   MenuLocation:TechDraw → Knoten hinzufügen → Kosmetischen Knoten hinzufügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Mittenpunkt](TechDraw_Midpoints/de.md), [TechDraw Quadrant](TechDraw_Quadrants/de.md)
---

## Beschreibung

Das Kosmetikknoten Werkzeug fügt einer Ansicht einen [Knoten](Glossary/de#V.md) hinzu, der nicht Teil der Quellgeometrie ist. Dieser Knoten verhält sich wie jeder andere Knoten und kann für die Bemaßung verwendet werden.

<img alt="" src=images/TechDraw_CosmeticVertex_Sample.png  style="width:300px;"> 
*Kosmetikknoten, der zur Erzeugung einer sonst unmöglichen Bemaßung verwendet wird*

## Anwendung

1.  Wähle eine Ansicht in der Zeichnung.
2.  Drücke die **<img src="images/TechDraw_CosmeticVertex.svg" width=16px> Kosmetikknoten hinzufügen** Schaltfläche
3.  Ein Aufgabendialog wird geöffnet. Er ermöglicht es, die Position des kosmetischen Knotens entweder durch Auswahl eines Punktes oder durch Eingabe eines x,y-Versatzes von der Mitte der gewählten Ansicht aus festzulegen.
4.  Um eine Position auszuwählen, drücke die Taste **Point Picker**. Klicke auf eine Position in der Ansicht und drücke anschließend **OK** um den Punkt zu erstellen. Um die Punktauswahl zu beenden, ohne einen Kosmetikknoten zu erstellen, drücke die **Escape picking** Schaltfläche im Dialogfeld.

Um einen Kosmetikknoten zu löschen, wähle ihn aus und verwende die Werkzeugleistenschaltfläche **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Kosmetikobjekt entfernen](TechDraw_CosmeticEraser/de.md)**.

**Hinweis:** Du kannst die Position des Kosmetikknoten nicht mehr ändern, nachdem er erstellt wurde. Im Moment gibt es keine andere Möglichkeit, als ihn zu löschen und einen neuen zu erstellen.

## Eigenschaften

Kosmetische Knoten haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind. Sie haben gemeinsame Farb- und Größeneinstellungen mit regulären Geometrieknoten.

## Skripten


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Kosmetische Knoten sind für [Makros](Macros/de.md) oder die [Python](Python/de.md) Konsole verfügbar.


```python
dvp = App.ActiveDocument.View
org = App.Vector(0.0, 0.0, 0.0)
dvp.makeCosmeticVertex(org);

#lines too!
start = FreeCAD.Vector (1.0, 5.0, 0.0)
end = FreeCAD.Vector(1.0, -5.0, 0.0)
style = 2
weight = 0.75
pyGreen = (0.0, 0.0, 1.0, 0.0)
dvp.makeCosmeticLine(start,end,style, weight, pyGreen)
```





{{TechDraw Tools navi

}}  
