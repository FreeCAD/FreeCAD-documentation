---
 GuiCommand:
   Name: Arch Remove
   Name/de: Arch Entfernen
   MenuLocation: Modify , Komponente entfernen
   Workbenches: BIM_Workbench/de
   SeeAlso: Arch_CutPlane/de, Arch_Add/de
---

# Arch Remove/de



## Beschreibung

Das Werkzeug **Arch Entfernen** ermöglicht zwei Arten von Operationen:

-   Entfernen einer Unterkomponente aus einem Arch-Objekt, zum Beispiel einen Quader entfernen, der einer Wand hinzugefügt wurde, wie in dem Beispiel unter **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add/de.md)**.
-   Abziehen eines auf einer [Form](Part_Workbench/de.md) basierenden Objekts aus einer Arch-Komponente wie z.B. einer **<img src="images/Arch_Wall.svg" width=16px> [Arch-Wand](Arch_Wall/de.md)
** oder **<img src="images/Arch_Structure.svg" width=16px> [Arch-Struktur](Arch_Structure/de.md)**

Das Gegenstück dieses Werkzeugs ist das **<img src="images/Arch_Add.svg" width=16px> [Arch Hinzufügen](Arch_Add/de.md)** Werkzeug.

<img alt="" src=images/Arch_Remove_example.jpg  style="width:600px;"> 
*Ein Quader wird von einer Wand subtrahiert und hinterlässt in ihr eine Aussparung.*



## Anwendung

1.  Eine Unterkomponente in einem Arch-Objekt auswählen
2.  Die Schaltfläche **<img src="images/Arch_Remove.svg" width=16px> [Komponente entfernen](Arch_Remove/de.md)** drücken oder den Menüeintrag **Modify → <img src="images/Arch_Remove.svg" width=16px> Komponente entfernen** auswählen.

Oder

1.  Abzuziehende Objekte auswählen, das letzte Objekt muss das Arch-Objekt sein, von dem die anderen Objekte abgezogen werden sollen.
2.  Die Schaltfläche **<img src="images/Arch_Remove.svg" width=16px> [Komponente entfernen](Arch_Remove/de.md)** drücken oder den Menüeintrag **Modify → <img src="images/Arch_Remove.svg" width=16px> Komponente entfernen** auswählen.



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





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Remove/de
