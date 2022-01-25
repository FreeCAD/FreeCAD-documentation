---
- GuiCommand:
   Name:Arch IfcSpreadsheet
   MenuLocation:Arch → Utilities → Create IFC spreadsheet
   Workbenches:[Arch](Arch_Workbench.md)
   Shortcut:**I** **P**
   SeeAlso:[Arch IFC](Arch_IFC.md), [Arch IfcExplorer](Arch_IfcExplorer.md)
---

# Arch IfcSpreadsheet/pl

## Description

This tool creates a spreadsheet to store [IFC](Arch_IFC.md) properties of an object.

## Usage

1.  Select an object.
2.  Invoke the command using several methods:
    -   Pressing the **<img src="images/Arch_IfcSpreadsheet.svg" width=16px> Create IFC spreadsheet** button on the toolbar.
    -   Using the **I** then **P** keyboard shortcut.
    -   Using the **Arch → Utilities → <img src="images/Arch_IfcSpreadsheet.svg" width=16px> Create IFC spreadsheet** entry from the top menu.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

This tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
```python
spreadsheet = makeIfcSpreadsheet(archobj=None)
```

-   Creates a `spreadsheet` object. Optionally an `archobj` can be given.

Example: 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)
FreeCAD.ActiveDocument.recompute()

spreadsheet = Arch.makeIfcSpreadsheet(Wall)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch IfcSpreadsheet/pl
