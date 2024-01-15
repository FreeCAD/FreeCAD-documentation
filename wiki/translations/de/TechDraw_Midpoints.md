---
 GuiCommand:
   Name: TechDraw Midpoints
   Name/de: TechDraw Mittenpunkte
   MenuLocation: TechDraw , Knoten hinzufügen , Kantenmittelpunkte hinzufügen
   Workbenches: TechDraw_Workbench
   Version: 0.19
   SeeAlso: TechDraw_CosmeticVertex/de, TechDraw_Quadrants/de
---

# TechDraw Midpoints/de



## Beschreibung

Das Werkzeug **TechDraw Mittenpunkte** fügt einer oder mehreren Kanten einen Hilfspunkt ([Knoten](Glossary/de#Vertex.md)) auf halber Länge hinzu.

<img alt="" src=images/TechDraw_CosmeticMidpoint_Sample.png  style="width:250px;"> 
*Hilfspunkte an Kantenmittenpunkten*



## Anwendung

1.  Eine oder mehrere Kanten in einer Ansicht auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_Midpoints.svg" width=16px> [Kantenmittelpunkte hinzufügen](TechDraw_Midpoints.md) ** drücken.
    -   Den Menüeintrag **TechDraw → Knoten hinzufügen → <img src="images/TechDraw_Midpoints.svg" width=16px> Kantenmittelpunkte hinzufügen** auswählen.



## Hinweise

-   Die erstellten Hilfspunkte sind nicht parametrisch mit den ausgewählten Kanten verbunden.
-   Zum Löschen eines Hilfspunktes wird <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw Hilfsobjekte entfernen](TechDraw_CosmeticEraser/de.md) verwendet.



## Eigenschaften

Hilfspunkte haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind. Sie verwenden dieselben Farb- und Größeneinstellungen wie reguläre Geometrieknoten.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Hilfspunkte sind zur Zeit nicht über [Makros](Macros/de.md) oder die [Python](Python/de.md)-Konsole erreichbar. Dieser Schnipsel entfernt alle Hilfspunkte aus der Ansicht.


```python
v = App.ActiveDocument.View
v.clearCV()
App.ActiveDocument.recompute()
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Midpoints/de
