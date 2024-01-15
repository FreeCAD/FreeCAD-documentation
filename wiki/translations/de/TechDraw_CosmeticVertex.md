---
 GuiCommand:
   Name: TechDraw CosmeticVertex
   Name/de: TechDraw Hilfspunkt
   MenuLocation: TechDraw , Knoten hinzufügen , Hilfspunkt hinzufügen
   Workbenches: TechDraw_Workbench/de
   Version: 0.19
   SeeAlso: TechDraw_Midpoints/de, TechDraw_Quadrants/de
---

# TechDraw CosmeticVertex/de



## Beschreibung

Das Werkzeug **TechDraw Hilfspunkt** fügt einer Ansicht einen Hilfspunkt ([Knoten](Glossary/de#Vertex.md)) hinzu, der nicht Teil der Quellgeometrie ist. Dieser Hilfspunkt verhält sich wie jeder andere Knoten und kann für die Bemaßung verwendet werden.

<img alt="" src=images/TechDraw_CosmeticVertex_Sample.png  style="width:300px;"> 
*Hilfspunkte, verwendet, um ein sonst unmögliches Maß einzutragen*



## Anwendung

1.  Eine Ansicht auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_CosmeticVertex.svg" width=16px> [Hilfspunkt hinzufügen](TechDraw_CosmeticVertex/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Knoten hinzufügen → <img src="images/TechDraw_CosmeticVertex.svg" width=16px> Hilfspunkt hinzufügen** auswählen.
3.  Ein Aufgaben-Bereich wird geöffnet.
4.  Wahlweise die Schaltfläche **Punkt-Auswahl** drücken und einen Punkt auf dem Zeichnungsblatt auswählen. Die Schaltfläche **Auswahl abbrechen** drücken, um diesen Vorgang abzubrechen.
5.  Wahlweise die X- und Y-Koordinaten des Punktes anpassen oder festlegen. Die Koordinaten beziehen sich auf das Zentrum der Ansicht.
6.  Die Schaltfläche **OK** drücken.



## Hinweise

-   Die Position eines Hilfspunktes kann nicht geändert werden. Im Moment gibt es keine andere Möglichkeit, als ihn zu löschen und einen neuen zu erstellen.
-   Um einen Hilfspunkt zu löschen, wird <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw HilfsobjektEntfernen](TechDraw_CosmeticEraser.md) verwendet.



## Eigenschaften

Hilfspunkte haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind. Sie verwenden dieselben Farb- und Größeneinstellungen wie reguläre Geometrieknoten.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Hilfspunkte stehen in [Makros](Macros/de.md) oder der [Python](Python/de.md)-Konsole zur Verfügung.


```python
dvp = App.ActiveDocument.View
org = App.Vector(0.0, 0.0, 0.0)
dvp.makeCosmeticVertex(org);

#lines too!
start = FreeCAD.Vector (1.0, 5.0, 0.0)
end = FreeCAD.Vector(1.0, -5.0, 0.0)
style = 2
weight = 0.75
pyGreen = (0.0, 0.0, 1.0, 0.0)
dvp.makeCosmeticLine(start,end,style, weight, pyGreen)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw CosmeticVertex/de
