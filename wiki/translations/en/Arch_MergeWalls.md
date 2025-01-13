---
 GuiCommand:
   Name: Arch MergeWalls
   MenuLocation: Utils , Merge Walls
   Workbenches: BIM_Workbench
   SeeAlso: Arch_Wall
---

# Arch MergeWalls/en

## Description

The **Arch MergeWalls** tool merges [Arch Walls](Arch_Wall.md).

## Usage

1.  Do one of the following:
    -   Select a single wall with one or more [additions](Arch_Add.md) that are also walls.
    -   Select two or more walls.
2.  In both cases the walls must have the same **Height**, **Width** and **Align** properties.
3.  Select the **Utils → <img src="images/Arch_MergeWalls.svg" width=16px> Merge Walls** option from the menu.

## Notes

-   [Arch Add](Arch_Add.md) can merge walls even if they have different heights, widths and alignments.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

This tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


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





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch MergeWalls/en
