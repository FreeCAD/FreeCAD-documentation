---
- GuiCommand:
   Name/ru:Указать вертикальный габаритный размер
   Name:TechDraw_VerticalExtentDimension
   MenuLocation:TechDraw - Размеры - Указать вертикальный габаритный размер 
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   Version:0.19
   SeeAlso:[Указать длину](TechDraw_LengthDimension/ru.md), [Указать горизонтальный габаритный размер](TechDraw_HorizontalExtentDimension/ru.md)
---

# TechDraw VerticalExtentDimension/ru



## Описание

The **TechDraw VerticalExtentDimension** tool adds a linear dimension to a View. The dimension extends from the bottom most point on the selected objects to the top most point. A CosmeticVertex will be placed at each point.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Vertical Extent dimension of B-spline Face*



## Применение

1.  Select a View or a collection of Edges in a View.
2.  Press the **<img src="images/TechDraw_VerticalExtentDimension.svg" width=16px> [Vertical Extent Dimension](TechDraw_VerticalExtentDimension.md)** button
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.



## Ограничения

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information.



## Свойства

See [TechDraw LengthDimension](TechDraw_LengthDimension#Properties.md). Exceptions noted below.



### Данные

-    **MeasureType**: `True` - based on 3D geometry or \"Projected\" - based on the drawing. Not normally manipulated directly by the end user. Not yet implemented for Dimension Vertical Extent.



## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The Vertical Extent Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
selection = [(view1, 'Edge1'), (view1, 'Edge2')]  #or [] for all
hExtentDim = TechDraw.Dimension.makeExtentDim(selection, VERTICAL)
rc = page.addView(hExtentDim)
```





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw VerticalExtentDimension/ru
