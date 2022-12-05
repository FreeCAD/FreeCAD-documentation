---
- GuiCommand:/ru
   Name/ru:Указать диаметр
   Name:TechDraw_DiameterDimension
   MenuLocation:TechDraw → Размеры → Указать диаметр
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   SeeAlso:[Указать радиус](TechDraw_RadiusDimension/ru.md)
---

# TechDraw DiameterDimension/ru

## Описание

The Diameter Dimension tool adds a diameter dimension to a View. The dimension may be applied to any circular in the drawing. The distance will initially be the projected distance (ie as shown on the drawing), but this may be changed to the actual 3D distance using the **<img src="images/TechDraw_LinkDimension.svg" width=16px> [TechDraw LinkDimension](TechDraw_LinkDimension.md)** tool.

<img alt="" src=images/TechDraw_Dimension_Diameter_example.png  style="width:130px;"> 
*Measuring a circle, indicating the diameter*

## Применение

1.  Select a circular edge in the drawing. (Note some arcs which appear to be circular are actually ellipses or BSplines. You cannot make a diameter dimension in these cases)
2.  Press the **<img src="images/TechDraw_DiameterDimension.svg" width=16px> [Diameter Dimension](TechDraw_DiameterDimension.md)** button
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

The Diameter Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Diameter"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DiameterDimension/ru
