---
- GuiCommand:
   Name/ru:Arch: AxisSystem/Система осей
   Icon:Arch Axis System.svg
   MenuLocation:Arch - Axis System
   Workbenches:[Arch](Arch_Workbench.md)
   SeeAlso:[Arch Axis](Arch_Axis.md), [Arch Grid](Arch_Grid.md)
---

# Arch AxisSystem/ru


</div>

## Описание


<div class="mw-translate-fuzzy">

Средство Axis System позволяет объединить 2 или 3 объекта [Arch Axis](Arch_Axis.md). Основная функция этого инструмента - рассчитать точки пересечения между различными осями, включенными в эту систему. Объекты Arch могут затем использовать эту систему для дублирования их формы в разных точках пересечения.


</div>

This is useful to define the intersection points between the different axes. Arch objects can then use this system to duplicate their shape on the different intersection points.

<img alt="" src=images/Arch_AxisSystem_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

*На приведенном выше рисунке показаны три объекта [Arch Axis](Arch_Axis.md), объединенные в одну систему Axis. Затем объект столбца использует эту систему как свое свойство **Axis**, чтобы иметь форму, дублируемую в каждой точке пересечения.*


</div>

## Применение

1.  Optionally, select the [Arch Axis](Arch_Axis.md) objects you wish to include in this system.
2.  Press the **<img src="images/Arch_AxisSystem.svg" width=16px> [[Arch AxisSystem]]** button.
3.  Right-click the newly created axes system object in the tree view to add/edit the [Arch Axis](Arch_Axis.md) objects included in this system.
4.  Select any existing [Arch Axis](Arch_Axis.md) and press **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** or **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** buttons to add or remove it to/from this system.
5.  Set the **Axis** property of any Arch object to point to this system, to have its shape duplicated to the intersection points of this system.

## Опции

-   A same [Arch Axis](Arch_Axis.md) object can be part of more than one system
-   Any shape-based object can also be used as the **Axis** property of Arch objects. In this case, the object shape will be duplicated along the vertices of the Axis object

## Scripting


<div class="mw-translate-fuzzy">

## Программирование


**См. так же:**

[Arch API](Arch_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>

The AxisSystem tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function: 
```python
AxisSystem = makeAxisSystem(axes, name="Axis System")
```

-   Creates an `AxisSystem` object from the given `axes`, which is a single [Arch Axis](Arch_Axis.md), or a list of them.

Пример: 
```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()

AxisSystem = Arch.makeAxisSystem([Axes, Axes2])

Structure = Arch.makeStructure(length=200, width=200, height=100)
Draft.move(Structure, FreeCAD.Vector(-100, 0, 0))
Structure.Axis = AxisSystem
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch AxisSystem/ru
