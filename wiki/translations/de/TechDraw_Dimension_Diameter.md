---
- GuiCommand:/de
   Name:TechDraw Dimension Diameter
   Name/de:TechDraw Durchmesserbemaßung
   MenuLocation:TechDraw → Durchmesserbemaßung
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Radiusbemaßung](TechDraw_Dimension_Radius/de.md)
---

## Beschreibung

Das Werkzeug »Durchmesserbemaßung« fügt eine Durchmessermaß in einer Ansicht hinzu. Die Bemaßung kann auf jeden Kreis in der Zeichnung angewendet werden. Der Abstand ist zuerst der projizierte Abstand (wie in der Zeichnung dargestellt), aber dieser kann unter Verwendung des **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Bemaßungen verlinken](TechDraw_Dimension_Link/de.md)**-Werkzeugs zum eigentlichen 3D-Abstand geändert werden.

<img alt="" src=images/TechDraw_Dimension_Diameter_example.png  style="width:130px;"> 
*Messen eines Kreises, angeben des Durchmessers*

## Anwendung

1.  Wähle eine kreisförmige Kante in der Zeichnung. Beachte, dass einige Bögen, die kreisförmig zu sein scheinen, in Wirklichkeit Ellipsen oder BSplines sind. In diesen Fällen kannst du keine Durchmesserbemaßung vornehmen
2.  Drücke die **<img src="images/TechDraw_Dimension_Diameter.svg" width=24px> [Durchmesserbemaßen](TechDraw_Dimension_Diameter/de.md)** Schaltfläche
3.  Eine Bemaßung wird in die Ansicht eingefügt. Die Bemaßung kann an die gewünschte Position gezogen werden.
4.  Falls erforderlich, füge Toleranzen hinzu, wie in [diese Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben.

Um die Eigenschaften eines Bemaßungsobjekts zu ändern, doppel-klicke sie entweder in der Zeichnung oder in der [Baumansicht](Tree_view/de.md). Dadurch wird der [Bemaßungsdialog](TechDraw_Dimension_Length/de#Bemaßung_Dialog.md) geöffnet.

## Einschränkungen

Bemaßungsobjekte sind anfällig für \"topologsche Benennung\"sprobleme. Siehe die Information im [TechDraw Längenbemaßungs](TechDraw_Dimension_Length/de.md) Werkzeug für weitere Informationen.

## Eigenschaften

Diese Funktion hat die gleichen Eigenschaften wie das [TechDraw Längenbemassungs](TechDraw_Dimension_Length/de.md) Werkzeug. Siehe dieses Werkzeug für weitere Einzelheiten.

## Programmierung


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Durchmesserbemaßungswerkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit den folgenden Funktionen verwendet werden:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Diameter"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}  
