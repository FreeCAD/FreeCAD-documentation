---
 GuiCommand:
   Name: Arch IfcSpreadsheet
   MenuLocation: Utils , Create IFC spreadsheet...
   Workbenches: BIM_Workbench
   Shortcut: **I** **P**
   SeeAlso: Arch_IFC
---

# Arch IfcSpreadsheet/en

## Description

This tool creates a spreadsheet to store [IFC](Arch_IFC.md) properties of an object.

## Usage

1.  Select an object.
2.  There are several ways to invoke the tool:
    -   Select the **Utils → <img src="images/Arch_IfcSpreadsheet.svg" width=16px> Create IFC spreadsheet...** option from the menu.
    -   Use the keyboard shortcut: **I** then **P**.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

This tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function: 
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





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch IfcSpreadsheet/en
