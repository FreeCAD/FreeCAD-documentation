---
- GuiCommand:/ru
   Name:Arch MergeWalls
   Name/ru:Arch MergeWalls
   MenuLocation:Архитектура → Утилиты → Объединить стенки
   Workbenches:[Arch](Arch_Workbench/ru.md)
   SeeAlso:[[Arch Wall]]
---

# Arch MergeWalls/ru


</div>

## Описание

The [MergeWalls](Arch_MergeWalls.md) tool fuses two or more selected **<img src="images/_Arch_Wall.svg" width=16px> [Arch Walls](Arch_Wall.md)**.

## Использование

1.  Select two or more walls.
2.  Press the **<img src="images/Arch_MergeWalls.svg" width=16px>** button, or use the **Arch** → **Utilities** → **<img src="images/Arch_MergeWalls.svg" width=16px> [Merge Walls](Arch_MergeWalls.md)** from the top menu.

## Properties

## Limitations

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

This tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
```python
base = joinWalls(walls, delete=False)
```

Example: 
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


{{docnav/ru|[Close Holes](Arch_CloseHoles.md)|[Check](Arch_Check.md)|[Arch](Arch_Workbench.md)|IconL=Arch_CloseHoles.svg |IconC=Workbench_Arch.svg |IconR=Arch_Check.svg}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MergeWalls/ru
