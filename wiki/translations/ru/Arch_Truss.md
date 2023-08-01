---
- GuiCommand:/ru
   Name/ru:Ферма
   Name:Arch_Truss
   MenuLocation:Arch → Ферма
   Workbenches:[Arch](Arch_Workbench/ru.md)
   Version:0.19
---

# Arch Truss/ru

## Описание

The [Arch Truss](Arch_Truss.md) tool builds a [truss](https://en.wikipedia.org/wiki/Truss) object, either from a selected linear object (lie a [Draft Line](Draft_Line.md) or [Sketch](Sketcher_NewSketch.md)), or from scratch, if no object is selected when launching the command.

<img alt="" src=images/Arch_Truss_example.png  style="width:600px;">

## Применение

### Создание из выбранного объекта 

1.  Use a workbench of your choice to create a single line
2.  Select that line
3.  Press the **<img src="images/Arch_Truss.svg" width=16px> [Arch Truss](Arch_Truss.md)** button
4.  Adjust the truss properties to your liking

### Создание с нуля 

1.  Make sure nothing is selected
2.  Press the **<img src="images/Arch_Truss.svg" width=16px> [Arch Truss](Arch_Truss.md)** button
3.  Click in the 3D view to define a first point, or manually enter X, Y and Z coordinates
4.  Click in the 3D view to define a second point, or manually enter X, Y and Z coordinates
5.  Adjust the truss properties to your liking

## Свойства

### Данные

-    **TrussAngle**: The angle of the truss

-    **SlantType**: The slant type of this truss

-    **Normal**: The normal direction of this truss

-    **HeightStart**: The height of the truss at the start position

-    **HeightEnd**: The height of the truss at the end position

-    **StrutStartOffset**: An optional start offset for the top strut

-    **StrutEndOffset**: An optional end offset for the top strut

-    **StrutHeight**: The height of the main top and bottom elements of the truss

-    **StrutWidth**: The width of the main top and bottom elements of the truss

-    **RodType**: The type of the middle element of the truss

-    **RodDirection**: The direction of the rods

-    **RodSize**: The diameter or side of the rods

-    **RodSections**: The number of rod sections

-    **RodEnd**: If the truss has a rod at its endpoint or not

-    **RodMode**: How to draw the rods

## Программирование

The Truss tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
Truss = makeFence([baseobj])
```

Пример:


```python
import FreeCAD
import Draft
import Arch

p1 = FreeCAD.Vector(0,0,0)
p2 = FreeCAD.Vector(2000,0,0)
baseline = Draft.makeLine(p1,p2)
truss = Arch.makeTruss(baseline)
truss.HeightStart = 200
truss.HeightEnd = 400
# adjust other needed properties
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Truss/ru
