---
 GuiCommand:
   Name: Arch_MakeIfcSpreadsheet
   Name/ro: Arch_MakeIfcSpreadsheet
   MenuLocation: Arch , Utilities , Create schedule...
   Workbenches: Arch_Workbench/ro
   Shortcut: **I** **P**
   SeeAlso: Arch IFC, Arch IfcExplorer
   Icon: Arch_Schedule.svg
---

# Arch IfcSpreadsheet/ro


</div>

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


<div class="mw-translate-fuzzy">


{{docnav/ro|[3 Views from mesh](Arch_3Views.md)|[Toggle Subcomponents](Arch_ToggleSubs.md)|[Arch](Arch_Workbench.md)|IconL=Arch_3Views.svg |IconC=Workbench_Arch.svg |IconR=Arch_ToggleSubs.svg}}


</div>



---
⏵ [documentation index](../README.md) > Arch IfcSpreadsheet/ro
