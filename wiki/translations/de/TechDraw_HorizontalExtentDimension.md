---
- GuiCommand   */de
   Name   *TechDraw Dimension Horizontal Extent
   Name/de   *TechDraw MaßHorizontaleAusdehnung
   MenuLocation   *TechDraw → Bemaßungen → Maß für die horizontale Ausdehnung einfügen
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md)
   Version   *0.19
   SeeAlso   *[TechDraw Längenmaß](TechDraw_LengthDimension/de.md), [TechDraw MaßVertikaleAusdehnung](TechDraw_VerticalExtentDimension/de.md)
---

# TechDraw HorizontalExtentDimension/de

## Beschreibung

Das Werkzeug MaßHorizontaleAusdehnung fügt einer Ansicht ein lineares Maß hinzu. Das Maß erstreckt sich vom äußersten linken Punkt der ausgewählten Objekte bis zum äußersten rechten Punkt. An beiden Stellen wird ein Hilfspunkt gesetzt.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width   *400px;"> 
*Horizontale Ausdehnung Bemaßen von BSpline Fläche*

## Anwendung

1.  Eine Ansicht oder mehrere Kanten in einer Ansicht auswählen.
2.  Die Schaltfläche **<img src="images/TechDraw_HorizontalExtentDimension.svg" width=16px> [Maß für die horizontale Ausdehnung einfügen](TechDraw_HorizontalExtentDimension/de.md)** drücken.
3.  Ein Maß wird der Ansicht hinzugefügt. Das Maß kann an die gewünschte Position gezogen werden.

## Begrenzungen

Dimension-Objekte (Maße) sind anfällig für das \"[Topological-Naming-Problem](topological_naming_problem/de.md)\" (Problem der topologischen Benennung). Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de.md) für weitere Informationen.

## Eigenschaften

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#Eigenschaften.md). Ausnahmen sind weiter unten angegeben.

### Daten

-    {{PropertyData/de|MeasureType}}   * `True` - basierend auf 3D Geometrie oder \"Projizierter Geometrie\" auf der Zeichnung. Normalerweise nicht direkt vom Endbenutzer beeinflusst. Noch nicht implementiert für Bemaßung Horizontale Ausdehnung.

## Skripten

Siehe auch   * [Autogenerierte API Dokumentation](https   *//freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug MaßHorizontaleAusdehnung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden   *


```python
selection = ['Edge1', 'Edge2']                      # or [] for all

TechDraw.makeExtentDim(view1, selection, 0)         # view1 is a DrawViewPart; 0 for horizontal
App.ActiveDocument.DimExtent.Y = -60                # offset dimension line from dimensioned edges in Y direction
App.ActiveDocument.DimExtent.X = 10                 # offset dimension text along dimension line in X direction
App.ActiveDocument.DimExtent.FormatSpec = '%.0f'    # Dimension format

TechDraw.makeExtentDim(view1, selection, 1)         # view1 is a DrawViewPart; 1 for vertical
App.ActiveDocument.DimExtent001.X = -130            # offset dimension line from dimensioned edges in X direction
App.ActiveDocument.DimExtent001.Y = 10              # offset dimension text along dimension line in Y direction
App.ActiveDocument.DimExtent001.FormatSpec = '%.0f'

# Note the dimension names are 'DimExtent', 'DimExtent001' etc in the order created.
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw HorizontalExtentDimension/de
