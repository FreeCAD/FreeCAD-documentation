# Arch Add/sv
---
- GuiCommand:/sv   Name:Arch Add   Name/sv:Arch Add   Workbenches:[MenuLocation:Arch → Add   SeeAlso:[[Arch Remove/sv|Arch Remove](Arch_Workbench/sv___Arch]].md)---


</div>

## Beskrivning


<div class="mw-translate-fuzzy">

Add verkytget låter dig göra 2 olika operationer:

-   Lägga till [form](Part_Workbench/sv.md)-baserade objekt till en Arch komponent, som en [vägg](Arch_Wall/sv.md) eller [struktur](Arch_Structure/sv.md). Dessa objekt blir sedan en del av Arch komponenten, och låter dig förändra dess form men behåller dess grundegenskaper som bredd och höjd
-   lägga till Arch komponenter, som [väggar](Arch_Wall/sv.md) eller [strukturer](Arch_Structure/sv.md), till en [cell](Arch_Cell/sv.md) eller andra cell-baserade objekt som [golv](Arch_Floor/sv.md).


</div>

The counterpart of this tool is the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.

<img alt="" src=images/Arch_Add_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

*I bilden ovan adderas en låda till en vägg.*


</div>


<div class="mw-translate-fuzzy">

## Bruk


</div>


<div class="mw-translate-fuzzy">

1.  Välj de objekt som ska läggas till, och sedan \"värd\" objektet (värdobjektet måste väljas sist)
2.  Klicka på <img alt="" src=images/Arch_Add.png  style="width:16px;"> **Add** knappen


</div>

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Add tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:

:   
    
```python
    addComponents(objectsList, host)
    
```
    





:   The above code snippet adds the given objects in `objectsList` to the given `host` object.
:   **Note:** `objectsList` can be a single object or a list of objects.

Example:


```python
import FreeCAD, Arch, Draft, Part

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Arch.addComponents(Wall2, Wall)
FreeCAD.ActiveDocument.recompute()
```

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Add/sv
