---
 GuiCommand:
   Name: Arch MergeWalls
   Name/de: Arch WändeZusammenführen
   MenuLocation: Arch , Dienstprogramme , Wände zusammenführen
   Workbenches: Arch_Workbench/de
   SeeAlso: Arch_Wall/de
---

# Arch MergeWalls/de



## Beschreibung

Das Werkzeug [WändeZusammenführen](Arch_MergeWalls/de.md) verschmilzt zwei oder mehr ausgewählte **<img src="images/_Arch_Wall.svg" width=16px>[Arch Wände](Arch_Wall/de.md)**.



## Anwendung

1.  Zwei oder mehr Wände auswählen.
2.  Die Schaltfläche **<img src="images/Arch_MergeWalls.svg" width=16px>** drücken, oder den Menüeintrag **Arch** → **Dienstprogramme** → **<img src="images/Arch_MergeWalls.svg" width=16px> [Wände zusammenfügen](Arch_MergeWalls/de.md)** auswählen.



## Eigenschaften



## Begrenzungen



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Dieses Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch folgende Funktion verwendet werden: 
```python
base = joinWalls(walls, delete=False)
```

Beispiel: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
FreeCAD.ActiveDocument.recompute() 

base = Arch.joinWalls([Wall1, Wall2])
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MergeWalls/de
