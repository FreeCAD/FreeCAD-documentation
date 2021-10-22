---
- GuiCommand:
   Name:Arch CloseHoles
   MenuLocation:Arch → Utilities → Close Holes
   Workbenches:[Arch](Arch_Workbench.md)
   SeeAlso:[Arch Check](Arch_Check.md)
---

# Arch CloseHoles

## Description

This tool identifies holes (circular sequence of open edges) in a [Shape](Part_Workbench.md) object and attempts to close it by adding it a new face made from that edges sequence. You must still verify yourself that the result is a solid, though.

## Usage

1.  Select a [Shape](Part_Workbench.md) object.
2.  Press the **<img src="images/Arch_CloseHoles.svg" width=16px> [Close Holes](Arch_CloseHoles.md)** entry in **Arch → Utilities → Close Holes**.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

This tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function:  
```python
solid = closeHole(shape)
```

-   Closes a hole in a `shape`, which is a `Part.Shape`, and returns the new `solid` object.

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

solid = Arch.closeHole(Wall.Shape)
```

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CloseHoles
