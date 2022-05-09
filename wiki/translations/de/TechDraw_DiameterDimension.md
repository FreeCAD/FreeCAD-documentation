---
- GuiCommand   */de
   Name   *TechDraw Dimension Diameter
   Name/de   *TechDraw MaßDurchmesser
   MenuLocation   *TechDraw → Bemaßungen → Durchmessermaß einfügen
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso   *[TechDraw Radienmaß einfügen](TechDraw_RadiusDimension/de.md)
---

# TechDraw DiameterDimension/de

## Beschreibung

Das Werkzeug MaßDurchmesser fügt einer Ansicht ein Durchmessermaß hinzu. Das Maß kann auf jeden Kreis (alles kreisförmige) in der Zeichnung angewendet werden. Der Abstand ist zuerst der projizierte Abstand (wie in der Zeichnung dargestellt), kann aber unter Verwendung des Werkzeugs **<img src="images/TechDraw_LinkDimension.svg" width=16px> [MaßVerknüpfen](TechDraw_LinkDimension/de.md)** auf den eigentlichen 3D-Abstand geändert werden.

<img alt="" src=images/TechDraw_Dimension_Diameter_example.png  style="width   *130px;"> 
*Messen eines Kreises, angeben des Durchmessers*

## Anwendung

1.  Eine kreisförmige Kante in der Zeichnung auswählen. (Hinweis   * Einige Bögen, die kreisförmig aussehen, sind in Wirklichkeit Ellipsen oder BSplines. In diesen Fällen können keine Durchmessermaße erstellt werden)
2.  Die Schaltfläche **<img src="images/TechDraw_DiameterDimension.svg" width=24px> [Durchmessermaß einfügen](TechDraw_DiameterDimension/de.md)** drücken.
3.  Ein Maß wird der Ansicht hinzugefügt. Das Maß kann an die gewünschte Position gezogen werden.
4.  Falls erforderlich, können Toleranzen, wie auf der [GD&T-Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben, hinzugefügt werden.

Um die Eigenschaften eines Dimension-Objekts zu ändern, doppelklickt man sie entweder in der Zeichnung oder in der [Baumansicht](Tree_view/de.md). Dadurch wird der [Bemaßungsdialog](TechDraw_LengthDimension/de#Bemaßungsdialog.md) geöffnet.

## Einschränkungen

Dimension-Objekte (Maße) sind anfällig für das \"[Topological-Naming-Problem](topological_naming_problem/de.md)\" (Problem der topologischen Benennung). Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de.md) für weitere Informationen.

## Eigenschaften

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#Eigenschaften.md).

## Skripten


**Siehe auch   ***

[TechDraw-API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug MaßDurchmesser kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden   *


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewDimension','Dimension')
dim1.Type = "Diameter"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DiameterDimension/de
