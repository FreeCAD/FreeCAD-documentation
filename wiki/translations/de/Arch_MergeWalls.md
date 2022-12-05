---
- GuiCommand:/de
   Name:Arch MergeWalls
   Name/de:Arch WändeZusammenführen
   MenuLocation:Arch → Dienstprogramme → Wände zusammenführen
   Workbenches:[Arch](Arch_Workbench/de.md)
   SeeAlso:[Arch Wand](Arch_Wall/de.md)
---

# Arch MergeWalls/de

## Beschreibung

Das [Wände zusammenführen](Arch_MergeWalls/de.md) Werkzeug verschmilzt zwei oder mehr ausgewählte **<img src="images/_Arch_Wall.svg" width=16px>[Arch Wände](Arch_Wall/de.md)**.

## Anwendung

1.  Wähle zwei oder mehr Wände.
2.  Drücke die **<img src="images/Arch_MergeWalls.svg" width=16px>** Schaltfläche, oder verwende den **Arch** → **Dienstprogramme** → **<img src="images/Arch_MergeWalls.svg" width=16px> [Wände zusammenführen](Arch_MergeWalls/de.md)** aus dem oberen Menü.

## Eigenschaften

## Begrenzungen

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Dieses Werkzeug kann in [Makros](macros/de.md) ebenso wie aus der Python-Konsole heraus durch folgende Funktion angesprochen werden: 
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


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MergeWalls/de
