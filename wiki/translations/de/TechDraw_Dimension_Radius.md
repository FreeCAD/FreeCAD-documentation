---
- GuiCommand:/de
   Name/de:TechDraw Radiusbemaßung
   MenuLocation:TechDraw → Bemaßungen → Radius bemaßen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Durchmesserbemaßung](TechDraw_Dimension_Diameter/de.md)
---

## Beschreibung

Das Werkzeug Radiusbemaßung fügt eine Radiusbemaßung einer Ansicht hinzu. Die Bemaßung kann auf jede Kante angewendet werden, die ein Kreis oder ein kreiförmiger Bogen ist. Der Abstand ist zuerst der projizierte Abstand (wie in der Zeichnung dargestellt), aber dieser kann unter Verwendung des **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Bemaßungen verknüpfen](TechDraw_Dimension_Link/de.md)** Werkzeugs zum eigentlichen 3D Abstand geändert werden.

<img alt="" src=images/TechDraw_Dimension_Radius_example.png  style="width:130px;"> 
*Messen eines Kreises, angeben des Radius*

## Anwendung

1.  Wähle einen Kreis oder Kreisbogen in der Zeichnung. (Hinweis: Einige Bögen, die kreisförmig aussehen, können tatsächlich Ellipsen oder BSplines sein. In diesen Fällen können keine Durchmesserbemaßungen erstellt werden)
2.  Drücke die **<img src="images/Dimension_Radius.png" width=16px> [Einen Radius der gewählten Ansicht bemaßen](TechDraw_Dimension_Radius/de.md)** Schaltfläche.
3.  Eine Bemaßung wird der Ansicht hinzugefügt. Sie kann anschließend an die gewünschte Position gezogen werden.
4.  Falls erforderlich, füge Toleranzen hinzu, wie in [diese Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben.

Um die Eigenschaften eines Bemaßungsobjekts zu ändern, doppel-klicke sie entweder in der Zeichnung oder in der [Baumansicht](Tree_view/de.md). Dadurch wird der [Bemaßungsdialog](TechDraw_Dimension_Length/de#Bemaßung_Dialog.md) geöffnet.

## Begrenzungen

Bemaßungsobjekte sind anfällig für \"topologsche Benennung\"sprobleme. Siehe die Information im [TechDraw Längenbemaßungs](TechDraw_Dimension_Length/de.md) Werkzeug für weitere Informationen.

## Eigenschaften

Dieses Objekt hat die gleichen Eigenschaften wie das [TechDraw Längenbemassungswerkzeug](TechDraw_Dimension_Length/de.md). Siehe dieses Werkzeug für weitere Einzelheiten.

## Programmierung


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Radiusbemaßung kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit den folgenden Funktionen verwendet werden:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Radius"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}  
