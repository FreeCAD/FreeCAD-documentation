---
- GuiCommand:/de
   Name:TechDraw Dimension Horizontal
   Name/de:TechDraw Horizontale Bemaßung
   MenuLocation:TechDraw → Horizontale Bemaßung
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Shortcut:**Shift** + **H**
   SeeAlso:[TechDraw Längenbemaßung](TechDraw_Dimension_Length/de.md), [TechDraw Vertikale Bemaßung](TechDraw_Dimension_Vertical/de.md)
---

## Beschreibung

Das Werkzeug »Horizontale Längenbemaßung« fügt ein horizontales Maß in einer Ansicht hinzu. Die Bemaßung kann zwischen zwei Ecken liegen, die Länge einer Kante oder der horizontale Abstand zwischen zwei Kanten sein. Der Abstand ist zuerst der projizierte Abstand (wie in der Zeichnung dargestellt), aber dieser kann unter Verwendung des **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Bemaßungen verlinken](TechDraw_Dimension_Link/de.md)**-Werkzeugs zum eigentlichen 3D-Abstand geändert werden.

<img alt="" src=images/TechDraw_Dimension_Horizontal_example.png  style="width:200px;"> 
*Längenbemaßung zweier beliebiger Knoten der Ansicht, der Abstand wird in horizontaler Richtung gemessen*

## Anwendung

1.  Punkte oder Kanten auswählen, die deine Messung festlegen.
2.  Drücke die **<img src="images/TechDraw_Dimension_Horizontal.svg" width=16px> [Horizontale Bemaßung](TechDraw_Dimension_Horizontal/de.md)** Schaltfläche
3.  Eine Bemaßung wird der Ansicht hinzugefügt. Die Bemaßung kann an die gewünschte Position gezogen werden.
4.  Falls erforderlich, füge Toleranzen, wie in [diese Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben, hinzu.

Um die Eigenschaften eines Bemaßungsobjekts zu ändern, doppel-klicke sie entweder in der Zeichnung oder in der [Baumansicht](Tree_view/de.md). Dadurch wird der [Bemaßungsdialog](TechDraw_Dimension_Length/de#Bemaßung_Dialog.md) geöffnet.

## Begrenzungen

Bemaßungsobjekte sind anfällig für \"topologische Benennung\"sprobleme. Weitere Informationen gibt es unter dem Werkzeug [Längenbemaßung](TechDraw_Dimension_Length/de.md).

## Eigenschaften

Diese Funktion hat die gleichen Eigenschaften wie das [TechDraw Längenbemaßungswerkzeug](TechDraw_Dimension_Length/de.md). Siehe dieses Werkzeug für weitere Einzelheiten.

## Programmierung


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Horizontale Bemaßung kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md)-Konsole mit den folgenden Funktionen verwendet werden:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "DistanceX"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}  
