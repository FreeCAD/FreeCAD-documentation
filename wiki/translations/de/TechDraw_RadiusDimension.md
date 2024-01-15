---
 GuiCommand:
   Name: TechDraw RadiusDimension
   Name/de: TechDraw MaßRadius
   MenuLocation: TechDraw , Bemaßungen , Radienmaß einfügen
   Workbenches: TechDraw_Workbench/de
   SeeAlso: TechDraw_DiameterDimension/de
---

# TechDraw RadiusDimension/de



## Beschreibung

Das Werkzeug **TechDraw MaßRadius** fügt einer Ansicht ein Radienmaß hinzu. Das Maß kann an jede Kante gesetzt werden, die ein Kreis oder ein Kreisbogen ist.

<img alt="" src=images/TechDraw_Dimension_Radius_example.png  style="width:130px;"> 
*Bemaßen eines Kreises durch Angabe des Radius*



## Anwendung

1.  Einen Kreis oder Kreisbogen auswählen. Die Geometrie kann in der [3D-Ansicht](3D_view/de.md) oder in der Zeichnung ausgewählt werden. Hinweis: Einige Bögen, die kreisförmig aussehen, können tatsächlich Ellipsen oder B-Splines sein. In diesen Fällen können keine Radienmaße erstellt werden.
2.  Wenn die Geometrie in der 3D-Ansicht ausgewählt wurde, wird die korrekte TechDraw-ansicht in der [Baumansicht](Tree_view/de.md) ausgewählt.
3.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_RadiusDimension.svg" width=16px> [Radienmaß einfügen](TechDraw_RadiusDimension/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Maßeinträge → <img src="images/TechDraw_RadiusDimension.svg" width=16px> Radienmaß einfügen** auswählen.
4.  Ein Maß wird der Ansicht hinzugefügt.
5.  Das Maß kann auf die gewünschte Position gezogen werden.
6.  Falls erforderlich, können Toleranzen, wie auf der [GD&T-Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben, hinzugefügt werden.



### 3D-Abmessungen anzeigen 

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#3D-Abmessungen_anzeigen.md).



### Eigenschaften anpassen 

Um die Eigenschaften eines Maßes (Dimension-Objekt) zu ändern, wird es in der Zeichnung oder in der [Baumansicht](Tree_view/de.md) doppelt angeklickt. Dadurch wird der Dialog [Maßeintrag](TechDraw_LengthDimension/de#Dialog_Maßeintrag.md) geöffnet.



## Einschränkungen

Dimension-Objekte (Maße) sind anfällig für das \"[Topological-Naming-Problem](topological_naming_problem/de.md)\" (Problem der topologischen Benennung). Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de.md).



## Hinweise

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#Hinweise.md).



## Eigenschaften

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#Eigenschaften.md).



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug MaßRadius kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
dim1 = FreeCAD.ActiveDocument.addObject("TechDraw::DrawViewDimension", "Dimension")
dim1.Type = "Radius"
dim1.References2D=[(view1, "Edge1")]
page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw RadiusDimension/de
