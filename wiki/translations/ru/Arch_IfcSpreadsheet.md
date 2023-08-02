---
- GuiCommand:
   Name: Arch IfcSpreadsheet
   Name/ru: Arch IfcSpreadsheet
   MenuLocation: Arch -> Utilities -> Создать IFC таблицу
   Workbenches: Arch_Workbench/ru
   Shortcut: **I** **P**
   SeeAlso: Arch_IFC/ru, Arch_IfcExplorer/ru
---

# Arch IfcSpreadsheet/ru


</div>

## Описание

This tool creates a spreadsheet to store [IFC](Arch_IFC.md) properties of an object.

## Использование

1.  Select an object.
2.  Invoke the command using several methods:
    -   Pressing the **<img src="images/Arch_IfcSpreadsheet.svg" width=16px> Create IFC spreadsheet** button on the toolbar.
    -   Using the **I** then **P** keyboard shortcut.
    -   Using the **Arch → Utilities → <img src="images/Arch_IfcSpreadsheet.svg" width=16px> Create IFC spreadsheet** entry from the top menu.

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


{{docnav/ru|[3 Views from mesh](Arch_3Views.md)|[Toggle Subcomponents](Arch_ToggleSubs.md)|[Arch](Arch_Workbench.md)|IconL=Arch_3Views.svg |IconC=Workbench_Arch.svg |IconR=Arch_ToggleSubs.svg}}


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch IfcSpreadsheet/ru
