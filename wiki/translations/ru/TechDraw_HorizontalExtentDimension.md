---
- GuiCommand:
   Name/ru: Указать горизонтальный габаритный размер
   Name: TechDraw_HorizontalExtentDimension
   MenuLocation: TechDraw - Размеры - Указать горизонтальный габаритный размер
   Workbenches: [TechDraw](TechDraw_Workbench/ru.md)
   Version: 0.19
   SeeAlso: [Указать длину](TechDraw_LengthDimension/ru.md), [Указать вертикальный габаритный размер](TechDraw_VerticalExtentDimension/ru.md)
---

# TechDraw HorizontalExtentDimension/ru



## Описание

The **TechDraw HorizontalExtentDimension** tool adds a linear dimension to a View. The dimension extends from the left most point on the selected objects to the right most point. A CosmeticVertex will be placed at each point.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Horizontal Extent dimension of B-spline Face*



## Применение

1.  Select a View or a collection of Edges in a View.
2.  Press the **<img src="images/TechDraw_HorizontalExtentDimension.svg" width=16px> [Horizontal Extent Dimension](TechDraw_HorizontalExtentDimension.md)** button
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.



## Ограничения

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information.



## Свойства

See [TechDraw LengthDimension](TechDraw_LengthDimension#Properties.md). Exceptions noted below.



### Данные

-    **MeasureType**: `True` - based on 3D geometry or \"Projected\" - based on the drawing. Not normally manipulated directly by the end user. Not yet implemented for Dimension Horizontal Extent.



## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The Horizontal Extent Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
selection = ['Edge1', 'Edge2']                      # or [] for all

TechDraw.makeExtentDim(view1, selection, 0)         # view1 is a DrawViewPart; 0 for horizontal
App.ActiveDocument.DimExtent.Y = -60                # offset dimension line from dimensioned edges in Y direction
App.ActiveDocument.DimExtent.X = 10                 # offset dimension text along dimension line in X direction
App.ActiveDocument.DimExtent.FormatSpec = '%.0f'    # Dimension format

TechDraw.makeExtentDim(view1, selection, 1)         # view1 is a DrawViewPart; 1 for vertical
App.ActiveDocument.DimExtent001.X = -130            # offset dimension line from dimensioned edges in X direction
App.ActiveDocument.DimExtent001.Y = 10              # offset dimension text along dimension line in Y direction
App.ActiveDocument.DimExtent001.FormatSpec = '%.0f'

# Note the dimension names are 'DimExtent', 'DimExtent001' etc in the order created.
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw HorizontalExtentDimension/ru
