---
- GuiCommand:/de
   Name:Arch Remove
   Name/de:Arch Entfernen
   MenuLocation:Architektur → Entfernen
   Workbenches:[Arch](Arch_Workbench/de.md)
   SeeAlso:[Arch SchneideLinie](Arch_CutLine/de.md), [Arch SchneideEbene](Arch_CutPlane/de.md), [Arch Hinzufügen](Arch_Add/de.md)
---

# Arch Remove/de

## Beschreibung

Das Entfernen Werkzeug erlaubt dir zwei Arten von Operationen:

-   Entfernen einer Unterkomponente aus einem Architekturobjekt, zum Beispiel einen Kasten entfernen, der an einer Wand angebracht wurde, wie in dem **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add/de.md)** Beispiel.
-   Subtrahieren eines [Form](Part_Workbench/de.md)-basierten Objektes aus einer Architekturkomponente wie z.B. einer **<img src="images/Arch_Wall.svg" width=16px> [Arch Mauer](Arch_Wall/de.md)
** oder **<img src="images/Arch_Structure.svg" width=16px> [Arch Struktur](Arch_Structure/de.md)**

Das Gegenstück dieses Werkzeugs ist das **<img src="images/Arch_Add.svg" width=16px> [Arch Hinzufügen](Arch_Add/de.md)** Werkzeug.

<img alt="" src=images/Arch_Remove_example.jpg  style="width:600px;"> 
*Ein Quader wird von einer Wand subtrahiert und hinterlässt in ihr eine Aussparung.*

## Anwendung

1.  Wählen Sie eine Unterkomponente in einem Architekturobjekt
2.  Drücke die **<img src="images/Arch_Remove.svg" width=16px>** Schaltfläche oder **Arch** → **<img src="images/Arch_Remove.svg" width=16px> [Entfernen](Arch_Remove/de.md)** aus dem oberen Menü.

Oder

1.  Wähle zu subtrahierende Objekte, das letzte Objekt muss das Arch Objekt sein, von dem die anderen Objekte substrahiert werden sollen.
2.  Drücke die **<img src="images/Arch_Remove.svg" width=16px>** Schaltfläche oder **Arch** → **<img src="images/Arch_Remove.svg" width=16px> [Entfernen](Arch_Remove/de.md)** aus dem oberen Menü.

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Entfernen Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole mit der folgenden Funktion verwendet werden: 
```python
removeComponents(objectsList, host=None)
```

-   Entfernt die in `objectsList` angegebenen Objekte von den Elternobjekten.

1.  Ist ein `Host`-Objekt angegeben, wird stattdessen versucht, die in `objectsList` angegebenen Objekte als Aussparungen zum `host` hinzuzufügen.

Beispiel: 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 900
Box.Width = 450
Box.Height = 2000
FreeCAD.ActiveDocument.recompute()

Draft.rotate(Box, 45)
Draft.move(Box, FreeCAD.Vector(1000, 700, 0))

Arch.removeComponents(Box, Wall)
FreeCAD.ActiveDocument.recompute()
```

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Remove/de
