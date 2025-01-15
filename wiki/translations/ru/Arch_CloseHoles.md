---
 GuiCommand:
   Name: Arch CloseHoles
   Name/ru: Arch CloseHoles
   MenuLocation: Архитектура , Утилиты , Убрать отверстия
   Workbenches: Arch_Workbench/ru
   SeeAlso: Arch Check/ru
---

# Arch CloseHoles/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Этот инструмент идентифицирует дыры (круговую последовательность открытых ребер) в объекте [ Shape](Part_Workbench.md) и пытается закрыть его, добавив в него новую грань, сделанную из этой последовательности ребер. Вы все равно должны убедиться, что результат является прочным.


</div>




<div class="mw-translate-fuzzy">

## Использование


</div>

1.  Select a [Shape](Part_Workbench.md) object.
2.  Select the **Utils → <img src="images/Arch_CloseHoles.svg" width=16px> Close holes** option from the menu.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

This tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function: 
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
⏵ [documentation index](../README.md) > Arch CloseHoles/ru
