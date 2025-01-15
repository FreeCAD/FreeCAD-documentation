---
 GuiCommand:
   Name: Arch Add
   MenuLocation: Modify , Add component
   Workbenches: BIM_Workbench
   SeeAlso: Arch_Remove
---

# Arch Add/pt-br



## Descrição

The Add tool allows you to do 4 kinds of operations:

-   Add [shape](Part_Workbench.md)-based objects to an Arch component, such as a **<img src="images/Arch_Wall.svg" width=16px> [wall](Arch_Wall.md)** or **<img src="images/Arch_Structure.svg" width=16px> [structure](Arch_Structure.md)**. These objects make then part of the Arch component, and allow you to modify its shape but keeping its base properties such as width and height
-   Add Arch components, such as a **<img src="images/Arch_Wall.svg" width=16px> [Arch Walls](Arch_Wall.md)** or **<img src="images/Arch_Structure.svg" width=16px> [Arch Structures](Arch_Structure.md)**, to a group-based arch object such as **<img src="images/Arch_Floor.svg" width=16px> [Arch Floors](Arch_Floor.md)**.
-   Add **<img src="images/Arch_Axis.svg" width=16px> [Axis systems](Arch_Axis.md)
** to **<img src="images/Arch_Structure.svg" width=16px> [structural objects](Arch_Structure.md)**
-   Add objects to **<img src="images/Arch_SectionPlane.svg" width=16px> [section planes](Arch_SectionPlane.md)
**

The counterpart of this tool is the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.

<img alt="" src=images/Arch_Add_example.jpg  style="width:640px;"> 
*A box added to a wall as a component.*



## Utilização

1.  Select the objects to be added together. The last object selected will be the host Arch object.
2.  Press the **<img src="images/Arch_Add.svg" width=16px> [Add component](Arch_Add.md)** button, or use **Modify → <img src="images/Arch_Add.svg" width=16px> Add component** from the top menu.

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


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Add/pt-br
