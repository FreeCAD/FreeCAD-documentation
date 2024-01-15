---
 GuiCommand:
   Name: TechDraw Dimension Horizontal Extent
   Name/de: TechDraw MaßHorizontaleAusdehnung
   MenuLocation: TechDraw , Maßeinträge , Maß für die horizontale Ausdehnung einfügen
   Workbenches: TechDraw_Workbench/de
   Version: 0.19
   SeeAlso: TechDraw_LengthDimension/de, TechDraw_VerticalExtentDimension/de
---

# TechDraw HorizontalExtentDimension/de



## Beschreibung

Das Werkzeug **TechDraw MaßHorizontaleAusdehnung** fügt einer Ansicht ein lineares Maß hinzu. Das Maß erstreckt sich vom äußersten linken Punkt der ausgewählten Objekte bis zum äußersten rechten Punkt.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Maße für die horizontale und die vertikale Ausdehnung eines B-Splines*



## Anwendung

1.  Eine Ansicht oder mehrere Kanten in einer Ansicht auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_HorizontalExtentDimension.svg" width=16px> [Horizontale Ausdehnung](TechDraw_HorizontalExtentDimension/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Page  → <img src="images/TechDraw_HorizontalExtentDimension.svg" width=16px> Horizontale Ausdehnung** auswählen.
3.  Ein Maß wird zur Ansicht hinzugefügt.
4.  Das Maß kann an die gewünschte Position gezogen werden.
5.  Falls erforderlich, können Toleranzen, wie auf der [GD&T-Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben, hinzugefügt werden.



### Eigenschaften anpassen 

Um die Eigenschaften eines Maßes (Dimension-Objekt) zu ändern, wird es in der Zeichnung oder in der [Baumansicht](Tree_view/de.md) doppelt angeklickt. Dadurch wird der Dialog [Maßeintrag](TechDraw_LengthDimension/de#Dialog_Maßeintrag.md) geöffnet.



## Einschränkungen

Dimension-Objekte (Maße) sind anfällig für das \"[Topological-Naming-Problem](topological_naming_problem/de.md)\" (Problem der topologischen Benennung). Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de.md).



## Hinweise

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#Hinweise.md).



## Eigenschaften

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#Eigenschaften.md). Ausnahmen sind weiter unten angegeben.



### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Measure Type|Enumeration}}: Noch nicht implementiert für Ausdehnungsmaße.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug MaßHorizontaleAusdehnung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


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
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw HorizontalExtentDimension/de
