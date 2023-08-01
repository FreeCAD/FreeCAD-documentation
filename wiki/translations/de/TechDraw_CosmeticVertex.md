---
- GuiCommand:
   Name:TechDraw CosmeticVertex
   Name/de:TechDraw Hilfspunkt
   MenuLocation:TechDraw → Knoten hinzufügen → Hilfspunkt hinzufügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Mittenpunkt](TechDraw_Midpoints/de.md), [TechDraw Quadrant](TechDraw_Quadrants/de.md)
---

# TechDraw CosmeticVertex/de



## Beschreibung

Das Werkzeug **TechDraw Hilfspunkt** fügt einer Ansicht einen Hilfspunkt ([Knoten](Glossary/de#Vertex.md)) hinzu, der nicht Teil der Quellgeometrie ist. Dieser Hilfspunkt verhält sich wie jeder andere Knoten und kann für die Bemaßung verwendet werden.

<img alt="" src=images/TechDraw_CosmeticVertex_Sample.png  style="width:300px;"> 
*Hilfspunkte, verwendet, um ein sonst unmögliches Maß einzutragen*



## Anwendung


<div class="mw-translate-fuzzy">

1.  Eine Ansicht auf der Zeichnung auswählen.
2.  Die Schaltfläche **<img src="images/TechDraw_CosmeticVertex.svg" width=16px> Hilfspunkt hinzufügen** drücken.
3.  Ein Aufgabendialog wird geöffnet. Er ermöglicht es, die Position des Hilfspunktes entweder durch Auswahl eines Punktes oder durch Eingabe von X- und Y-Abständen von der Mitte der gewählten Ansicht aus festzulegen.
4.  Um eine Position auszuwählen, die Schaltfläche **Punkt-Auswahl** drücken. Auf eine Position in der Ansicht klicken und anschließend **OK** drücken, um den Punkt zu erstellen. Um die Punktauswahl zu beenden, ohne einen Hilfspunkt zu erstellen, die Schaltfläche **Auswahl abbrechen** im Dialogfeld drücken.


</div>

## Notes

-   You cannot change the position of an existing cosmetic vertex. At the moment there is no other way than to delete it and create a new one.
-   To delete a cosmetic vertex use <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw CosmeticEraser](TechDraw_CosmeticEraser.md).



## Eigenschaften

Hilfspunkte haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind. Sie verwenden dieselben Farb- und Größeneinstellungen wie reguläre Geometrieknoten.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

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
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw CosmeticVertex/de
