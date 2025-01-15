---
 GuiCommand:
   Name: Arch Add
   Name/de: Arch Hinzufügen
   MenuLocation: Modify , Komponente hinzufügen
   Workbenches: BIM_Workbench/de
   SeeAlso: Arch_Remove/de
---

# Arch Add/de



## Beschreibung

Das Werkzeug Hinzufügen ermöglicht vier Arten von Vorgängen durchzuführen:

-   Hinzufügen von Objekten, die auf einer [Form](Part_Workbench/de.md) basieren, zu einer Arch-Komponente, wie einer **<img src="images/Arch_Wall.svg" width=16px> [Wand](Arch_Wall/de.md)** oder **<img src="images/Arch_Structure.svg" width=16px> [Struktur](Arch_Structure/de.md)**. Diese Objekte werden dann Teil der Arch-Komponente und ermöglichen es, ihre Form zu verändern, wobei die Basiseigenschaften wie Breite und Höhe erhalten bleiben.
-   Hinzufügen von Arch-Komponenten, wie **<img src="images/Arch_Wall.svg" width=16px> [Arch Wände](Arch_Wall/de.md)** oder **<img src="images/Arch_Structure.svg" width=16px> [Arch Strukturen](Arch_Structure/de.md)** zu einem gruppierenden Arch-Objekt wie **<img src="images/Arch_Floor.svg" width=16px> [Arch Stockwerk](Arch_Floor.md)**.
-   Hinzufügen von **<img src="images/Arch_Axis.svg" width=16px> [Achsensystemen](Arch_Axis/de.md)** zu **<img src="images/Arch_Structure.svg" width=16px> [Struktur](Arch_Structure/de.md)**-Objekten
-   Objekte zu **<img src="images/Arch_SectionPlane.svg" width=16px>[Schnittebenen](Arch_SectionPlane/de.md)** hinzufügen

Das Gegenstück zu diesem Werkzeug ist das Werkzeug **<img src="images/Arch_Remove.svg" width=16px>[Arch Entfernen](Arch_Remove/de.md)**.

<img alt="" src=images/Arch_Add_example.jpg  style="width:640px;"> 
*Ein Quader wird einer Wand als Komponente hinzugefügt.*



## Anwendung

1.  Ein oder mehrere hinzuzufügende Objekte auswählen, dann das Zielobjekt. Das zuletzt ausgewählte Objekt wird das Zielobjekt.
2.  Die Schaltfläche **<img src="images/Arch_Add.png" width=16px> [Komponente hinzufügen](Arch_Add/de.md)** drücken oder den Menüeintrag **Modify → <img src="images/Arch_Add.svg" width=16px> Komponente hinzufügen** auswählen.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Hinzufügen kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus durch folgende Funktion verwendet werden:

:   
    
```python
    addComponents(objectsList, host)
    
```
    





:   Der obige Code Schnipsel fügt die in `objectsList` angegebenen Objekte zum `host`-Objekt hinzu.
:   **Anmerkung** `objectsList` kann ein einzelnes Objekt oder eine Liste von Objekten sein.

Beispiel:


```python
import FreeCAD, Arch, Draft, Part

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Arch.addComponents(Wall2, Wall)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Add/de
