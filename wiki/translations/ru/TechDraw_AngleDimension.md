---
- GuiCommand:/ru
   Name/ru:Указать угловой размер
   Name:TechDraw_AngleDimension
   MenuLocation:TechDraw → Размеры → Указать угловой размер
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   SeeAlso:[Указать угловой размер по 3 точкам](TechDraw_3PtAngleDimension/ru.md)
---

# TechDraw AngleDimension/ru

## Описание

The Angle Dimension tool adds a angular dimension to a View. The dimension may be the interior angle between any two straight line edges. The angle will initially be the projected angle (ie as shown on the drawing), but this may be changed to the actual 3D distance using the **<img src="images/TechDraw_LinkDimension.svg" width=16px> [TechDraw LinkDimension](TechDraw_LinkDimension.md)** tool.

<img alt="" src=images/TechDraw_Dimension_Angle_example.png  style="width:200px;"> 
*Measuring the angle between two straight lines*

## Применение

1.  Select the points or edge which define your measurement.
2.  Press the **<img src="images/TechDraw_AngleDimension.svg" width=16px> [Angle Dimension](TechDraw_AngleDimension.md)** button
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

The Angle Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Angle"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw AngleDimension/ru
