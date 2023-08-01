---
- GuiCommand:
   Name: TechDraw Dimension Angle
   Name/de: TechDraw Winkelmaß
   MenuLocation: TechDraw - Bemaßungen - Winkelmaß einfügen
   Workbenches: [TechDraw](TechDraw_Workbench/de.md)
   SeeAlso: [TechDraw Winkelmaß3Punkte](TechDraw_3PtAngleDimension/de.md)
---

# TechDraw AngleDimension/de



## Beschreibung


<div class="mw-translate-fuzzy">

Das Werkzeug **TechDraw Winkelmaß** fügt einer Ansicht ein Winkelmaß hinzu. Das Maß kann der Innenwinkel zweier beliebiger gerader Kanten sein. Das Winkelmaß wird zunächst der projizierte Winkel sein (d.h. wie auf der Zeichnung dargestellt), kann aber mit dem Werkzeug **<img src="images/TechDraw_LinkDimension.svg" width=16px> [MaßVerknüpfen](TechDraw_LinkDimension/de.md)** auf den eigentlichen 3D-Winkel geändert werden.


</div>

<img alt="" src=images/TechDraw_Dimension_Angle_example.png  style="width:200px;">


<div class="mw-translate-fuzzy">



*Messen des Winkels zwischen zwei geraden Linien*


</div>



## Anwendung


<div class="mw-translate-fuzzy">

1.  Die Punkte oder die Kante auswählen, die die Messung definieren.
2.  Die Schaltfläche **<img src="images/TechDraw_AngleDimension.svg" width=16px> [Winkelmaß einfügen](TechDraw_AngleDimension/de.md)** drücken.
3.  Ein Maß wird der Ansicht hinzugefügt. Das Maß kann an die gewünschte Position gezogen werden.
4.  Falls erforderlich, können Toleranzen, wie auf der [GD&T-Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben, hinzugefügt werden.


</div>

### Display 3D measurement 

See [TechDraw LengthDimension](TechDraw_LengthDimension#Display_3D_measurement.md).

### Change properties 


<div class="mw-translate-fuzzy">

Um die Eigenschaften eines Dimension-Objekts zu ändern, doppelklickt man es entweder in der Zeichnung oder in der [Baumansicht](Tree_view/de.md) an. Dadurch wird der [Dialog Maßeintrag](TechDraw_LengthDimension/de#Dialog_Maßeintrag.md) geöffnet.


</div>



## Einschränkungen


<div class="mw-translate-fuzzy">

Dimension-Objekte (Maße) sind anfällig für das \"[Topological-Naming-Problem](topological_naming_problem/de.md)\" (Problem der topologischen Benennung). Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de.md) für weitere Informationen.


</div>

## Notes

See [TechDraw LengthDimension](TechDraw_LengthDimension#Notes.md).



## Eigenschaften

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#Eigenschaften.md).



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Winkelmaß kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Angle"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw AngleDimension/de
