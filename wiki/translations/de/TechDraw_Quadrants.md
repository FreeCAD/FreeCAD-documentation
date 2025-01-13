---
 GuiCommand:
   Name: TechDraw Quadrants
   Name/de: TechDraw Quadranten
   MenuLocation: TechDraw , Knoten hinzufügen , Quadrantengrenzpunkte hinzufügen
   Workbenches: TechDraw_Workbench/de
   Version: 0.19
   SeeAlso: TechDraw_CosmeticVertex/de, TechDraw_Midpoints/de
---

# TechDraw Quadrants/de



## Beschreibung

Das Werkzeug **TechDraw Quadranten** fügt einer oder mehreren ausgewählten Kanten der Länge nach drei [Hilfspunkte](TechDraw_CosmeticVertex/de.md) hinzu. Die Punkte werden bei 25%, 50% und 75% der Länge jeder Kante positioniert. Für eine Kreiskante ergeben sich so Hilfspunkte bei 90°, 180° and 270°, zusätzlich zu ihrem geometrischen Knotenpunkt bei 0°.

<img alt="" src=images/TechDraw_CosmeticQuadrant_Sample.png  style="width:250px;"> 
*Hilfspunkte an Quadrantengrenzpunkten eines Kreises*



## Anwendung

1.  Eine oder mehrere Kanten in einer Ansicht auswählen. Jede Kante kann ausgewählt werden, nicht nur Kreise.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_Quadrants.svg" width=16px> [Quadrantengrenzpunkte hinzufügen](TechDraw_Quadrants/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Knoten hinzufügen → <img src="images/TechDraw_Quadrants.svg" width=16px> Quadrantengrenzpunkte hinzufügen** auswählen.



## Hinweise

-   Die erstellten Hilfspunkte sind nicht parametrisch mit den ausgewählten Kanten verbunden.
-   Um einen Hilfspunkt zu löschen, wird er ausgewählt und die **Entf**-Taste gedrückt. {{Version/de|1.0}}



## Eigenschaften

Quadrantenknoten haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind. Sie teilen Farb- und Größeneinstellungen mit regulären Geometrieknoten.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Kosmetische Knoten sind zur Zeit nicht über [Makros](Macros/de.md) oder die [Python](Python/de.md) Konsole zugänglich. Dieser Schnipsel entfernt alle Kosmetische Knoten aus der Ansicht.


```python
v = App.ActiveDocument.View
v.clearCV()
App.ActiveDocument.recompute()
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Quadrants/de
