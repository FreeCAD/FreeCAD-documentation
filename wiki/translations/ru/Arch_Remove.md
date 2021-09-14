---
- GuiCommand:/ru
   Name:Arch Remove
   Name/ru:Arch Remove
   MenuLocation:Архитектура → Удалить компонент
   Workbenches:[Arch](Arch_Workbench/ru.md)
   SeeAlso:[Arch CutLine](Arch_CutLine.md), [Arch CutPlane](Arch_CutPlane.md), [Добавить компонент](Arch_Add/ru.md)
---


</div>

## Описание


<div class="mw-translate-fuzzy">

Инструменты «Удалить» позволяют выполнять 2 вида операций:

-   Удалите подкомпонент из объекта Arch, например, удалите поле, добавленное к стене, например, в примере **<img src="images/Arch_Add.svg" width=16px> [[Arch Add]]
**
-   Вычтите объект на основе [shape](Part_Workbench.md) из компонента Arch, например **<img src="images/Arch_Wall.svg" width=16px> [wall](Arch_Wall.md)
** или **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)**


</div>

The counterpart of this tool is the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool.

<img alt="" src=images/Arch_Remove_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

*В приведенном выше изображении коробка вычитается из стены*


</div>


<div class="mw-translate-fuzzy">

## Использование


</div>

1.  Select a subcomponent inside an Arch object.
2.  Press the **<img src="images/Arch_Remove.svg" width=16px>** button, or **Arch** → **<img src="images/Arch_Remove.svg" width=16px> [Remove](Arch_Remove.md)** from the top menu.

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


{{docnav/ru|[Add component](Arch_Add.md)|[Survey](Arch_Survey.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Add.svg |IconC=Workbench_Arch.svg |IconR=Arch_Survey.svg}}


</div>






