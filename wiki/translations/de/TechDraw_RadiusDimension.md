---
- GuiCommand   */de
   Name/de   *TechDraw MaßRadius
   MenuLocation   *TechDraw → Bemaßungen → Radienmaß einfügen
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso   *[TechDraw Durchmessermaß einfügen](TechDraw_DiameterDimension/de.md)
---

# TechDraw RadiusDimension/de

## Beschreibung

Das Werkzeug MaßRadius fügt einer Ansicht ein Radienmaß hinzu. Das Maß kann an jede Kante gesetzt werden, die ein Kreis oder ein Kreisbogen ist. Der Abstand ist zuerst der projizierte Abstand (wie in der Zeichnung dargestellt), kann aber unter Verwendung des Werkzeugs **<img src="images/TechDraw_LinkDimension.svg" width=16px> [MaßVerknüpfen](TechDraw_LinkDimension/de.md)** auf den eigentlichen 3D Abstand geändert werden.

<img alt="" src=images/TechDraw_Dimension_Radius_example.png  style="width   *130px;"> 
*Messen eines Kreises, angeben des Radius*

## Anwendung

1.  Einen Kreis oder Kreisbogen in der Zeichnung auswählen. (Hinweis   * Einige Bögen, die kreisförmig aussehen, können tatsächlich Ellipsen oder BSplines sein. In diesen Fällen können keine Radienmaße erstellt werden)
2.  Die Schaltfläche **<img src="images/TechDraw_RadiusDimension.svg" width=16px> [Radienmaß einfügen](TechDraw_RadiusDimension/de.md)** drücken.
3.  Ein Maß wird der Ansicht hinzugefügt. Es kann anschließend an die gewünschte Position gezogen werden.
4.  Falls erforderlich, können Toleranzen, wie auf der [GD&T-Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben, hinzugefügt werden.

Um die Eigenschaften eines Dimension-Objekts zu ändern, doppelklickt man sie entweder in der Zeichnung oder in der [Baumansicht](Tree_view/de.md). Dadurch wird der [Bemaßungsdialog](TechDraw_LengthDimension/de#Bemaßungsdialog.md) geöffnet.

## Einschränkungen

Dimension-Objekte (Maße) sind anfällig für das \"[Topological-Naming-Problem](topological_naming_problem/de.md)\" (Problem der topologischen Benennung). Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de.md) für weitere Informationen.

## Eigenschaften

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#Eigenschaften.md).

## Skripten


**Siehe auch   ***

[TechDraw-API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug MaßRadius kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden   *


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewDimension','Dimension')
dim1.Type = "Radius"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw RadiusDimension/de
