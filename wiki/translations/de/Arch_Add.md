---
- GuiCommand:/de
   Name:Arch Add
   Name/de:Arch hinzufügen
   MenuLocation:Arch → Komponente hinzufügen
   Workbenches:[Arch](Arch_Workbench/de.md)
   SeeAlso:[Arch Komponente entfernen](Arch_Remove/de.md)
---

## Beschreibung

Das Werkzeug Hinzufügen ermöglicht dir vier Arten von Arbeitsschritten durchzuführen:

-   Hinzufügen von [Form](Part_Workbench/de.md)-basierten Objekten zu einer Arch-Komponente, wie einer **<img src="images/Arch_Wall.svg" width=16px> [Mauer](Arch_Wall/de.md)** oder **<img src="images/Arch_Structure.svg" width=16px> [Struktur](Arch_Structure/de.md)**. Diese Objekte werden dann Teil der Arch-Komponente und ermöglichen es dir, ihre Form zu verändern, wobei die Basiseigenschaften wie Breite und Höhe erhalten bleiben.
-   Hinzufügen von Arch-Komponenten, wie ein **<img src="images/Arch_Wall.svg" width=16px> [Arch Wände](Arch_Wall/de.md)** oder **<img src="images/Arch_Structure.svg" width=16px> [Arch Strukturen](Arch_Structure/de.md)**, zu einem gruppenbasierten Arch-Objekt wie **<img src="images/Arch_Floor.svg" width=16px> [Arch Böden](Arch_Floor.md)**.
-   Hinzufügen von **<img src="images/Arch_Axis.svg" width=16px> [Achsensysteme](Arch_Axis/de.md)
** zu **<img src="images/Arch_Structure.svg" width=16px> [Strukturobjekte](Arch_Structure/de.md)**
-   Objekte zu **<img src="images/Arch_SectionPlane.svg" width=16px>[Schnittebenen](Arch_SectionPlane/de.md)** hinzufügen

Das Gegenstück zu diesem Werkzeug ist das **<img src="images/Arch_Remove.svg" width=16px>[Arch Entfernen](Arch_Remove/de.md)** Werkzeug.

<img alt="" src=images/Arch_Add_example.jpg  style="width:640px;"> 
*Ein Quader wird einer Wand als Komponente hinzugefügt.*

## Anwendung

1.  Wähle ein oder mehrere hinzuzufügende Objekte, dann das Zielobjekt. Das Zielobjekt muss das letze ausgewählte Objekt sein.
2.  Drücke die Schaltfläche **<img src="images/Arch_Add.png" width=16px> [Hinzufügen](Arch_Add/de.md)** oder benutze **Arch** → **<img src="images/Arch_Add.svg" width=16px> [Hinzufügen](Arch_Add/de.md)** aus dem Top-Menü.

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Gitter Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus durch folgende Funktion verwendet werden:

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









