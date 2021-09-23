---
- GuiCommand:/ru
   Name/ru:Указать вертикальный размер
   Name:TechDraw_VerticalDimension
   MenuLocation:TechDraw → Размеры → Указать вертикальный размер
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   Shortcut:**Shift** + **V**
   SeeAlso:[Указать длину](TechDraw_LengthDimension/ru.md), [Указать горизонтальный размер](TechDraw_HorizontalDimension/ru.md)
---

# TechDraw VerticalDimension/ru

## Описание

The Vertical Dimension tool adds a vertical dimension to a View. The dimension may be between two vertices, the length of one edge or the vertical distance between 2 edges. The distance will initially be the projected distance (ie as shown on the drawing), but this may be changed to the actual 3D distance using the **<img src="images/TechDraw_LinkDimension.svg" width=16px> [TechDraw LinkDimension](TechDraw_LinkDimension.md)** tool.

<img alt="" src=images/TechDraw_Dimension_Vertical_example.png  style="width:220px;"> 
*Вертикальное расстояние указанное между двумя произвольными точками фигуры.*

## Применение

1.  Select the points or edge which define your measurement.
2.  Press the **<img src="images/TechDraw_VerticalDimension.svg" width=16px> [Vertical Dimension](TechDraw_VerticalDimension.md)** button
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.
4.  If needed, add tolerances as described in [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).

## Ограничения

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information.

## Свойства

See [TechDraw LengthDimension](TechDraw_LengthDimension#Properties.md).

## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The Vertical Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "DistanceX"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw VerticalDimension/ru
