---
- GuiCommand:/de
   Name:TechDraw Dimension Angle
   Name/de:TechDraw Winkelbemaßung
   MenuLocation:TechDraw → Winkel bemaßen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Bemaßung Winkel3Punkte](TechDraw_Dimension_Angle3Pt/de.md)
---

## Beschreibung

Das Werkzeug Winkelbemaßung fügt ein Winkelbemaßung einer Ansicht hinzu. Die Bemaßung kann der Innenwinkel zweier beliebiger gerader Kanten sein. Der Winkel wird zunächst der projizierte Winkel sein (d.h. wie auf der Zeichnung dargestellt), aber dieser kann mit der **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Bemaßungen verknüpfen](TechDraw_Dimension_Link/de.md)** Werkzeug zum eigentlichen 3D Winkel geändert werden.

<img alt="" src=images/TechDraw_Dimension_Angle_example.png  style="width:200px;"> 
*Messen des Winkels zwischen zwei geraden Linien*

## Anwendung

1.  Wähle die Punkte oder die Kante, die deine Messung definieren.
2.  Drücke die **<img src="images/TechDraw_Dimension_Angle.svg" width=16px> [Winkel bemaßen](TechDraw_Dimension_Angle/de.md)** Schaltfläche
3.  Eine Bemaßung wird zur Ansicht hinzugefügt. Die Bemaßung kann an die gewünschte Position gezogen werden.
4.  Falls erforderlich, füge Toleranzen, wie in [diese Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben, hinzu.

Um die Eigenschaften eines Bemaßungsobjekts zu ändern, doppel-klicke sie entweder in der Zeichnung oder in der [Baumansicht](Tree_view/de.md). Dadurch wird der [Bemaßungsdialog](TechDraw_Dimension_Length/de#Bemaßung_Dialog.md) geöffnet.

## Begrenzungen

Bemaßungsobjekte sind anfällig für \"[topologische Benennungs](topological_naming_problem/de.md)\" Probleme. Siehe dazu die Informationen im **<img src="images/TechDraw_Dimension_Length.svg" width=16px> [TechDraw Bemaßung Länge](TechDraw_Dimension_Length/de.md)** Werkzeug für weitere Informationen.

## Eigenschaften

Dieses Objekt hat die gleichen Eigenschaften wie das [TechDraw Längenbemassung](TechDraw_Dimension_Length/de.md) Werkzeug. Siehe das Werkzeug für Einzelheiten.

## Skripten


**Siehe auch:**

[TechDraw Anwendungsschnittstelle](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Winkelbemaßung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus mit den folgenden Funktionen verwendet werden:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Angle"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}  
