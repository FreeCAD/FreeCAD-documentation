---
- GuiCommand:/de
   Name:TechDraw Dimension Vertical
   Name/de:TechDraw Vertikale Bemaßung
   MenuLocation:TechDraw → Bemaßungen → Vertikales Maß einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Shortcut:**Shift** + **V**
   SeeAlso:[TechDraw Längenbemaßung](TechDraw_LengthDimension/de.md), [TechDraw Horizontale Bemaßung](TechDraw_HorizontalDimension/de.md)
---

# TechDraw VerticalDimension/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das Werkzeug »Vertikale Längenbemaßung« fügt ein vertikales Maß in einer Ansicht hinzu. Die Bemaßung kann zwischen zwei Ecken liegen, die Länge einer Kante oder der vertikale Abstand zwischen zwei Kanten sein. Der Abstand ist zuerst der projizierte Abstand (wie in der Zeichnung dargestellt), aber dieser kann unter Verwendung des **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Bemaßungen verlinken](TechDraw_LinkDimension/de.md)**-Werkzeugs zum eigentlichen 3D-Abstand geändert werden.


</div>

<img alt="" src=images/TechDraw_Dimension_Vertical_example.png  style="width:220px;"> 
*Längenbemaßung zweier beliebiger Knoten der Ansicht, der Abstand wird in vertikaler Richtung gemessen*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Punkte oder Kanten auswählen, die für die Abmessung benötigt werden.
2.  Drücke die **<img src="images/TechDraw_VerticalDimension.svg" width=16px> [Vertikal Bemaßung](TechDraw_VerticalDimension/de.md)** Schaltfläche
3.  Eine Bemaßung wird in die Ansicht eingefügt. Die Bemaßung kann an die gewünschte Position gezogen werden.
4.  Falls erforderlich, füge Toleranzen, wie in [diese Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben, hinzu.


</div>


<div class="mw-translate-fuzzy">

Um die Eigenschaften eines Bemaßungsobjekts zu ändern, doppel-klicke sie entweder in der Zeichnung oder in der [Baumansicht](Tree_view/de.md). Dadurch wird der [Bemaßungsdialog](TechDraw_LengthDimension/de#Bemaßung_Dialog.md) geöffnet.


</div>

## Begrenzungen


<div class="mw-translate-fuzzy">

Bemaßungsobjekte sind anfällig für \"[topologische Benennungs](Topological_naming_problem/de.md)\" Probleme. Siehe die Information im [TechDraw Längenbemaßungs](TechDraw_LengthDimension/de.md) Werkzeug.


</div>

## Eigenschaften


<div class="mw-translate-fuzzy">

Dieses Objekt hat die gleichen Eigenschaften wie das [TechDraw Längenbemassung](TechDraw_LengthDimension/de.md) Werkzeug. Siehe das Werkzeug für Einzelheiten.


</div>

## Skripten


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


<div class="mw-translate-fuzzy">

Das Werkzeug Vertikale Bemaßung kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit den folgenden Funktionen verwendet werden:


</div>


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "DistanceX"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw VerticalDimension/de
