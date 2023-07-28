---
- GuiCommand:/de
   Name:TechDraw Midpoints
   Name/de:TechDraw Mittenpunkte
   MenuLocation:TechDraw → Knoten hinzufügen → Kantenmittelpunkte hinzufügen
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.19
   SeeAlso:[TechDraw Hilfspunkt](TechDraw_CosmeticVertex/de.md), [TechDraw Quadrantenknoten](TechDraw_Quadrants/de.md)
---

# TechDraw Midpoints/de


</div>



## Beschreibung

Das Werkzeug **TechDraw Mittenpunkte** fügt einer oder mehreren Kanten einen Hilfspunkt ([Knoten](Glossary/de#Vertex.md)) auf halber Länge hinzu.

<img alt="" src=images/TechDraw_CosmeticMidpoint_Sample.png  style="width:250px;"> 
*Hilfspunkte an Kantenmittenpunkten*



## Anwendung


<div class="mw-translate-fuzzy">

1.  Eine oder mehrere Kanten in einer Ansicht auswählen.
2.  Die Schaltfläche **<img src="images/TechDraw_Midpoints.svg" width=16px> Kantenmittelpunkte hinzufügen** drücken.
3.  Hilfspunkte werden auf der halben Länge der Kante(n) hinzugefügt.


</div>

## Notes

-   The created cosmetic vertices are not parametrically linked to the selected edges.
-   To delete a cosmetic vertex use <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw CosmeticEraser](TechDraw_CosmeticEraser.md).



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
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Midpoints/de
