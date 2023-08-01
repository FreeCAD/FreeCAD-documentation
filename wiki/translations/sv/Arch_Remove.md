---
- GuiCommand:
   Name:Arch Remove
   Name/sv:Arch Remove
   MenuLocation:Arch → Remove
   Workbenches:[Arch](Arch_Workbench/sv.md)
   SeeAlso:[[Arch Add/sv]]
---

# Arch Remove/sv


</div>

#### Beskrivning


<div class="mw-translate-fuzzy">

Remove verktyget låter dig göra 2 sorters operationer:

-   Ta bort en delkomponent från ett Arch objekt, till exempel ta bort en låda som har adderats till en vägg, som i [Arch Add](Arch_Add/sv.md) exemplet
-   Subtrahera en [formbaserat](Part_Workbench/sv.md) objekt från en Arch komponent som en [vägg](Arch_Wall/sv.md) eller [struktur](Arch_Structure/sv.md)


</div>

The counterpart of this tool is the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool.

<img alt="" src=images/Arch_Remove_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

*I bilden ovan, så subtraheras en låda från en vägg*


</div>


<div class="mw-translate-fuzzy">

#### Bruk


</div>


<div class="mw-translate-fuzzy">

1.  Välj en delkomponent inuti ett Arch objekt, **eller**:
2.  välj de objekt som ska subtraheras, och sedan den Arch komponent från vilken de ska subtraheras (arch komponenten måste vara den sista saken du väljer)
3.  Klicka på <img alt="" src=images/Arch_Remove.png  style="width:16px;"> **ta bort** knappen


</div>

Or

1.  Select objects to be subtracted, the last object selected must the Arch object from which the other objects will be subtracted.
2.  Press the **<img src="images/Arch_Remove.svg" width=16px>** button, or **Arch** → **<img src="images/Arch_Remove.svg" width=16px> [Remove](Arch_Remove.md)** from the top menu.

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


{{docnav/sv|[Add component](Arch_Add.md)|[Survey](Arch_Survey.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Add.svg |IconC=Workbench_Arch.svg |IconR=Arch_Survey.svg}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Remove/sv
