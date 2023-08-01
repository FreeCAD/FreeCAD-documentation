---
- GuiCommand:
   Name:Arch Check
   Name/ru:Arch Check
   Workbenches:[Arch](Arch_Workbench/ru.md)
   MenuLocation:Архитектура - Утилиты - Проверь
   SeeAlso:[Убрать отверстия](Arch_CloseHoles/ru.md)
---

# Arch Check/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Этот инструмент проверяет текущий документ или выбранные объекты для объектов с твердым объектом [ Part](Part_Workbench.md) или [ Arch](Arch_Workbench.md), что может вызвать проблемы, поскольку большинство операций модуля Arch требуют твердых объектов.


</div>




<div class="mw-translate-fuzzy">

## Использование


</div>


<div class="mw-translate-fuzzy">

1.  \# Нажмите кнопку **<img src="images/Arch_Check.png" width=16px> '''Check'''**в меню Arch → Utilities menu


</div>




<div class="mw-translate-fuzzy">

## Скрипты


</div>


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

This tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function: 
```python
list_bad = check(objectslist, includehidden=False)
```

-   Checks if the given objects in `objectslist` contain only solids.
-   If `includehidden` is `True` it will include all hidden objects, otherwise it will omit them from the search.
-   Returns `list_bad`, a list with the objects that are not derived from a `Part::Feature`, or components that are not closed, not valid, don\'t contain solids, or that contain faces that are not part of any solid. This is used to detect [Arch](Arch_Workbench.md) or [Draft](Draft_Workbench.md) wires and profiles that aren\'t solids.
    -   Each element in `list_bad` is another list `[object, message]`, where `object` is the detected non-solid, and `message` indicates the reason why it was included in this list.

Example:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
FreeCAD.ActiveDocument.recompute()

Circle = Draft.makeCircle(450)
Wire = Draft.makeWire([FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(1500, 1000, 0), FreeCAD.Vector(2500, -1000, 0)])

list_bad = Arch.check([Wall1, Wall2, Circle, Wire], includehidden=True)
print(list_bad)
```


<div class="mw-translate-fuzzy">


{{docnav/ru|[Merge Walls](Arch_MergeWalls.md)|[Ifc Explorer](Arch_IfcExplorer.md)|[Arch](Arch_Workbench.md)|IconL=Arch_MergeWalls.svg |IconC=Workbench_Arch.svg |IconR=Arch_IfcExplorer.png}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Check/ru
