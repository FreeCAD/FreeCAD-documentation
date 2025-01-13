---
 GuiCommand:
   Name: Arch Remove
   Name/tr: Mimari Kaldır
   MenuLocation: Arch , Remove
   Workbenches: Arch_Workbench
   SeeAlso: Arch Add
---

# Arch Remove/tr


</div>

## Description

The **Arch Remove** tools allows you to do 2 kinds of operations:

-   Remove a subcomponent from an Arch object, for example remove a box that has been added to a wall, like in the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** example.
-   Subtract a [shape](Part_Workbench.md)-based object from an Arch component such as a **<img src="images/Arch_Wall.svg" width=16px> [Arch Wall](Arch_Wall.md)
** or **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)**

The counterpart of this tool is the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool.

<img alt="" src=images/Arch_Remove_example.jpg  style="width:600px;"> 
*A box subtracted from a wall, leaving a hole in it.*

## Usage

1.  Select a subcomponent inside an Arch object.
2.  Press the **<img src="images/Arch_Remove.svg" width=16px> [Remove component](Arch_Remove.md)** button, or **Modify → <img src="images/Arch_Remove.svg" width=16px> Remove component** from the top menu.

Or

1.  Select objects to be subtracted, the last object selected must the Arch object from which the other objects will be subtracted.
2.  Press the **<img src="images/Arch_Remove.svg" width=16px> [Remove component](Arch_Remove.md)** button, or **Modify → <img src="images/Arch_Remove.svg" width=16px> Remove component** from the top menu.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Remove tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
removeComponents(objectsList, host=None)
```

-   Removes the given objects in `objectsList` from their parents.
-   If a `host` object is specified, this function will try adding the objects in `objectsList` as holes to the `host`.

Example:


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


<div class="mw-translate-fuzzy">





</div>


{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Remove/tr
