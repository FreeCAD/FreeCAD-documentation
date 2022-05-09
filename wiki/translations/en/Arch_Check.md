---
- GuiCommand   *
   Name   *Arch Check
   MenuLocation   *Arch → Utilities → Check
   Workbenches   *[Arch](Arch_Workbench.md)
   SeeAlso   *[Arch CloseHoles](Arch_CloseHoles.md)
---

# Arch Check/en

## Description

This tool checks the current document or the selected objects for non-solid **<img src="images/_Workbench_Part.svg" width=16px> [Part](Part_Workbench.md)** or **<img src="images/_Workbench_Arch.svg" width=16px> [Arch](Arch_Workbench.md)** objects, that might give problems, since most operations of the Arch Workbench require solid objects.

## Usage

1.  Press the **<img src="images/Arch_Check.svg" width=16px> [Check](Arch_Check.md)** button, or **Arch** → **Utilities** → **<img src="images/Arch_Check.svg" width=16px> [Check](Arch_Check.md)** in the top menu.

## Scripting


**See also   ***

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

This tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function   * 
```python
list_bad = check(objectslist, includehidden=False)
```

-   Checks if the given objects in `objectslist` contain only solids.
-   If `includehidden` is `True` it will include all hidden objects, otherwise it will omit them from the search.
-   Returns `list_bad`, a list with the objects that are not derived from a `Part   *   *Feature`, or components that are not closed, not valid, don\'t contain solids, or that contain faces that are not part of any solid. This is used to detect [Arch](Arch_Workbench.md) or [Draft](Draft_Workbench.md) wires and profiles that aren\'t solids.
    -   Each element in `list_bad` is another list `[object, message]`, where `object` is the detected non-solid, and `message` indicates the reason why it was included in this list.

Example   *


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
FreeCAD.ActiveDocument.recompute()

Circle = Draft.makeCircle(450)
Wire = Draft.makeWire([FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(1500, 1000, 0), FreeCAD.Vector(2500, -1000, 0)])

list_bad = Arch.check([Wall1, Wall2, Circle, Wire], includehidden=True)
print(list_bad)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Check/en
