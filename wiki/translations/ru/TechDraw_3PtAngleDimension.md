---
- GuiCommand:/ru
   Name/ru:Указать угловой размер по 3 точкам
   Name:TechDraw_3PtAngleDimension
   MenuLocation:TechDraw → Указать угловой размер по 3 точкам
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   Version:0.18
   SeeAlso:[Указать угловой размер](TechDraw_AngleDimension/ru.md)
---

## Описание

The 3-Point Angle Dimension tool adds a angular dimension to a View. The dimension may be specified by selecting three Vertices on a View. **Note that the second of the three Vertices is the apex of the angle**. The Angle3Pt will initially be the projected angle (ie as shown on the drawing), but this may be changed to the actual 3D distance using the **<img src="images/TechDraw_LinkDimension.svg" width=16px> [TechDraw LinkDimension](TechDraw_LinkDimension.md)** tool.

<img alt="" src=images/TechDraw_Dimension_Angle3Pt_example.png  style="width:200px;"> 
*Measuring the angle between two straight lines using three vertices; the second vertex should be the apex of the angle*

## Применение

1.  Select the points or edge which define your measurement.
2.  Press the **<img src="images/TechDraw_3PtAngleDimension.svg" width=16px> [3-Point Angle Dimension](TechDraw_3PtAngleDimension.md)** button
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

The 3-Point Angle Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Angle3Pt"
dim1.References2D=[(view1, 'Vertex1',(view1, 'Vertex4'),(view1, 'Vertex2'))]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}  
