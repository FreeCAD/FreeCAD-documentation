---
- GuiCommand:/de
   Name:TechDraw Dimension Vertical
   Name/de:TechDraw MaßVertikal
   MenuLocation:TechDraw → Bemaßungen → Vertikales Maß einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Shortcut:**Shift** + **V**
   SeeAlso:[TechDraw Längenmaß](TechDraw_LengthDimension/de.md), [TechDraw MaßHorizontal](TechDraw_HorizontalDimension/de.md)
---

# TechDraw VerticalDimension/de

## Beschreibung

Das Werkzeug »Vertikale Längenbemaßung« fügt einer Ansicht ein vertikales Maß hinzu. Die Bemaßung kann zwischen zwei Eckpunkten liegen, die Länge einer Kante oder der vertikale Abstand zwischen zwei Kanten sein. Der Abstand ist zuerst der projizierte Abstand (wie in der Zeichnung dargestellt), kann aber unter Verwendung des Werkzeugs **<img src="images/TechDraw_LinkDimension.svg" width=16px> [MaßVerknüpfen](TechDraw_LinkDimension/de.md)** auf den eigentlichen 3D-Abstand geändert werden.

<img alt="" src=images/TechDraw_Dimension_Vertical_example.png  style="width:220px;"> 
*Längenbemaßung zweier beliebiger Knoten der Ansicht, der Abstand wird in vertikaler Richtung gemessen*

## Anwendung

1.  Die Punkte oder die Kante auswählen, die die Messung definieren.
2.  Die Schaltfläche **<img src="images/TechDraw_VerticalDimension.svg" width=16px> [Vertikales Maß einfügen](TechDraw_VerticalDimension/de.md)** drücken.
3.  Ein Maß wird der Ansicht hinzugefügt. Das Maß kann an die gewünschte Position gezogen werden.
4.  Falls erforderlich, können Toleranzen, wie auf der [GD&T-Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben, hinzugefügt werden.

Um die Eigenschaften eines Dimension-Objekts zu ändern, doppelklickt man sie entweder in der Zeichnung oder in der [Baumansicht](Tree_view/de.md). Dadurch wird der [Bemaßungsdialog](TechDraw_LengthDimension/de#Bemaßungsdialog.md) geöffnet.

## Einschränkungen

Dimension-Objekte (Maße) sind anfällig für das \"[Topological-Naming-Problem](topological_naming_problem/de.md)\" (Problem der topologischen Benennung). Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de.md) für weitere Informationen.

## Eigenschaften

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#Eigenschaften.md).

## Skripten


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug MaßVertikal kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "DistanceX"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw VerticalDimension/de
