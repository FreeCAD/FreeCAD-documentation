---
- GuiCommand:/ru
   Name:Arch Add
   Name/ru:Arch Add
   MenuLocation:Архитектура → Добавить компонент
   Workbenches:[Arch](Arch_Workbench/ru.md)
   SeeAlso:[Удалить компонент](Arch_Remove/ru.md)
---

# Arch Add/ru


</div>

## Описание


<div class="mw-translate-fuzzy">

Инструмент «Добавить» позволяет вам выполнять 4 вида операций:

-   Добавьте объекты [ shape](Part_Workbench.md) к компоненту Arch, такие как [wall](Arch_Wall.md) или [structures](Arch_Structure.md) . Эти объекты затем составляют часть компонента Arch и позволяют изменять его форму, но сохраняя ее базовые свойства, такие как ширина и высота
-   Добавьте элементы Arch, такие как [walls](Arch_Wall.md) или [structures](Arch_Structure.md), в объект арки на основе группы, такой как [ floors](Arch_Floor.md).
-   Добавить [axis systems](Arch_Axis.md) в [structural objects](Arch_Structure.md)
-   Добавить объекты в плоскость [section planes](Arch_SectionPlane.md)


</div>

The counterpart of this tool is the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.

<img alt="" src=images/Arch_Add_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

\'\' В приведенном выше изображении коробка добавляется к стене. \'\'


</div>


<div class="mw-translate-fuzzy">

## Использование


</div>

1.  Select the objects to be added together. The last object selected will be the host Arch object.
2.  Press the **<img src="images/Arch_Add.svg" width=16px>** button, or use **Arch** → **<img src="images/Arch_Add.svg" width=16px> [Add](Arch_Add.md)** from the top menu.

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
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Add/ru
