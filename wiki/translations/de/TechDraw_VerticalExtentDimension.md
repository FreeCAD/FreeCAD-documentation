---
 GuiCommand:
   Name: TechDraw Dimension Vertical Extent
   Name/de: TechDraw MaßVertikaleAusdehnung
   MenuLocation: TechDraw , Maßeinträge , Maß für die vertikale Ausdehnung einfügen
   Workbenches: TechDraw_Workbench/de
   Version: 0.19
   SeeAlso: TechDraw_LengthDimension/de, TechDraw_HorizontalExtentDimension/de
---

# TechDraw VerticalExtentDimension/de



## Beschreibung

Das Werkzeug **TechDraw MaßVertikaleAusdehnung** fügt einer Ansicht ein lineares Maß hinzu. Das Maß erstreckt sich vom tiefsten Punkt der ausgewählten Objekte bis zum höchsten Punkt. An beiden Stellen wird ein Hilfspunkt gesetzt.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Maß für die vertikale Ausdehnung einer B-Spline-Fläche (193,54)*



## Anwendung

1.  Eine Ansicht oder mehrere Kanten in einer Ansicht auswählen.
2.  Schaltfläche **<img src="images/TechDraw_VerticalExtentDimension.svg" width=16px> [Maß für die vertikale Ausdehnung einfügen](TechDraw_VerticalExtentDimension/de.md)** drücken.
3.  Der Ansicht wird ein Maß hinzugefügt. Das Maß kann an die gewünschte Position gezogen werden.



## Begrenzungen

Dimension-Objekte (Maße) sind anfällig für das \"[Topological-Naming-Problem](topological_naming_problem/de.md)\" (Problem der topologischen Benennung). Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de.md) für weitere Informationen.



## Eigenschaften

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de.md). Ausnahmen sind weiter unten angegeben.



### Daten

-    {{PropertyData/de|MeasureType}}: `True` - basierend auf 3D Geometrie oder \"Projiziert\" - basierend auf der Zeichnung. Normalerweise nicht direkt vom Endanwender beeinflusst. Noch nicht implementiert für Bemaßung Vertikale Ausdehnung.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug MaßVertikaleAusdehnung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
selection = [(view1, 'Edge1'), (view1, 'Edge2')]  #or [] for all
hExtentDim = TechDraw.Dimension.makeExtentDim(selection, VERTICAL)
rc = page.addView(hExtentDim)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw VerticalExtentDimension/de
