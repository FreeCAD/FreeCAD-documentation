---
- GuiCommand:/de
   Name:TechDraw Dimension Angle3Pt
   Name/de:TechDraw Winkelmaß3Punkte
   MenuLocation:TechDraw → Winkelmaß über 3 Punkte ???
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.18
   SeeAlso:[TechDraw Winkelmaß](TechDraw_AngleDimension/de.md)
---

# TechDraw 3PtAngleDimension/de

## Beschreibung

Das Werkzeug Winkelmaß3Punkte fügt einer Ansicht ein Winkelmaß hinzu. Das Maß kann durch Auswahl von drei Knoten in einer Ansicht festgelegt werden. **Beachte, dass der zweite der drei Knoten der Scheitelpunkt des Winkels ist**. Das Winkelmaß ist zunächst der projizierte Winkel (d. h. wie in der Zeichnung gezeigt), kann aber mit Hilfe des Werkzeugs **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Bemaßungen verknüpfen](TechDraw_LinkDimension/de.md)** auf den tatsächlichen 3D-Winkel geändert werden.

<img alt="" src=images/TechDraw_Dimension_Angle3Pt_example.png  style="width:200px;"> 
*Beim Messen des Winkels zwischen zwei Geraden unter Verwendung von drei Knoten; der zweite Knoten sollte der Scheitelpunkt des Winkels sein*.

## Anwendung

1.  Die Punkte oder die Kante auswählen, die die Messung definieren.
2.  Die Schaltfläche **<img src="images/TechDraw_3PtAngleDimension.svg" width=16px> [Winkelmaß über 3 Punkte einfügen](TechDraw_3PtAngleDimension/de.md)** drücken.
3.  Ein Maß wird der Ansicht hinzugefügt. Das Maß kann an die gewünschte Position gezogen werden.
4.  Falls erforderlich, können Toleranzen, wie auf der [GD&T-Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben, hinzugefügt werden.

Um die Eigenschaften eines Dimension-Objekts zu ändern, doppelklickt man sie entweder in der Zeichnung oder in der [Baumansicht](Tree_view/de.md). Dadurch wird der [Bemaßungsdialog](TechDraw_LengthDimension/de#Bemaßungsdialog.md) geöffnet.

## Einschränkungen

Dimension-Objekte (Maße) sind anfällig für das \"[Topological-Naming-Problem](topological_naming_problem/de.md)\" (Problem der topologischen Benennung). Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de.md) für weitere Informationen.

## Eigenschaften

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#Eigenschaften.md).

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Winkelmaß3Punkte kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Angle3Pt"
dim1.References2D=[(view1, 'Vertex1',(view1, 'Vertex4'),(view1, 'Vertex2'))]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 3PtAngleDimension/de
