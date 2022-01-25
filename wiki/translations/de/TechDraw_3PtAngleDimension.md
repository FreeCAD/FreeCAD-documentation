---
- GuiCommand:/de
   Name:TechDraw Dimension Angle3Pt
   Name/de:TechDraw Bemaßung Winkel3Punkte
   MenuLocation:TechDraw → Bemaßung Winkel3Punkte
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.18
   SeeAlso:[TechDraw Bemaßung Winkel](TechDraw_AngleDimension/de.md)
---

# TechDraw 3PtAngleDimension/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das <img alt="" src=images/TechDraw_Dimension_Angle3Pt.svg  style="width:24px;"> Bemaßung Winkel3Punkte Werkzeug fügt einer Ansicht eine Winkelbemaßung hinzu. Der Winkel kann durch Auswahl von drei Knoten in einer Ansicht festgelegt werden. **Beachte, dass der zweite der drei Knoten der Scheitelpunkt des Winkels ist.**. Der Winkel3Punkte ist zunächst der projizierte Winkel (d. h. wie in der Zeichnung gezeigt), kann aber mit Hilfe des **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Bemaßungen verknüpfen](TechDraw_LinkDimension/de.md)** Werkzeugs in den tatsächlichen 3D Winkel geändert werden.


</div>

<img alt="" src=images/TechDraw_Dimension_Angle3Pt_example.png  style="width:200px;"> 
*Beim Messen des Winkels zwischen zwei Geraden unter Verwendung von drei Knoten; der zweite Knoten sollte der Scheitelpunkt des Winkels sein*.

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle die Punkte oder die Kante, die die Messung festlegt.
2.  Drücke die **<img src="images/TechDraw_3PtAngleDimension.svg" width=16px> [Bemaßung Winkel3Punkte](TechDraw_3PtAngleDimension/de.md)** Schaltfläche
3.  Eine Bemaßung wird zur Ansicht hinzugefügt. Die Bemaßung kann an die gewünschte Position gezogen werden.
4.  Falls erforderlich, füge Toleranzen, wie in [diese Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben, hinzu.


</div>


<div class="mw-translate-fuzzy">

Um die Eigenschaften eines Bemaßungsobjekts zu ändern, doppel-klicke sie entweder in der Zeichnung oder in der [Baumansicht](Tree_view/de.md). Dadurch wird der [Bemaßungsdialog](TechDraw_LengthDimension/de#Bemaßung_Dialog.md) geöffnet.


</div>

## Begrenzungen


<div class="mw-translate-fuzzy">

Bemaßungsobjekte sind anfällig für \"[topologische Benennungs](topological_naming_problem/de.md)\" Probleme. Siehe dazu die Informationen im **<img src="images/TechDraw_LengthDimension.svg" width=16px> [TechDraw Bemaßung Länge](TechDraw_LengthDimension/de.md)** Werkzeug für weitere Informationen.


</div>

## Eigenschaften


<div class="mw-translate-fuzzy">

Dieses Objekt hat die gleichen Eigenschaften wie das [TechDraw Längenbemassung](TechDraw_LengthDimension/de.md) Werkzeug. Siehe das Werkzeug für Einzelheiten.


</div>

## Skripten


**Siehe auch:**

[TechDraw Anwendungsschnittstelle](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


<div class="mw-translate-fuzzy">

Das Werkzeug Bemaßung Winkel3Punkte kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit den folgenden Funktionen verwendet werden:


</div>


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Angle3Pt"
dim1.References2D=[(view1, 'Vertex1',(view1, 'Vertex4'),(view1, 'Vertex2'))]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 3PtAngleDimension/de
