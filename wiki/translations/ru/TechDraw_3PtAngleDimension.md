---
- GuiCommand:
   Name/ru: Указать угловой размер по 3 точкам
   Name: TechDraw_3PtAngleDimension
   MenuLocation: TechDraw -> Указать угловой размер по 3 точкам
   Workbenches: TechDraw_Workbench/ru
   Version: 0.18
   SeeAlso: TechDraw_AngleDimension/ru
---

# TechDraw 3PtAngleDimension/ru


</div>



## Описание

The **TechDraw 3PtAngleDimension** tool adds an angular dimension to a View. The dimension shows the interior angle between three points.

<img alt="" src=images/TechDraw_Dimension_Angle3Pt_example.png  style="width:200px;"> 
*Measuring the angle between three points*



## Применение

1.  Select three points. The second point will be the apex of the angle. The geometry may be selected in the [3D view](3D_view.md) or in the drawing.
2.  If you have selected geometry in the 3D view: add the correct TechDraw View to the selection by selecting it in the [Tree view](Tree_view.md).
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_3PtAngleDimension.svg" width=16px> [Insert 3-Point Angle Dimension](TechDraw_3PtAngleDimension.md)** button.
    -   Select the **TechDraw → Dimensions → <img src="images/TechDraw_3PtAngleDimension.svg" width=16px> Insert 3-Point Angle Dimension** option from the menu.
4.  A dimension is added to the View.
5.  The dimension may be dragged to the desired position.
6.  If needed, add tolerances as described on [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

### Display 3D measurement 

See [TechDraw LengthDimension](TechDraw_LengthDimension#Display_3D_measurement.md).

### Change properties 

To change the properties of a dimension object either double-click it in the drawing or in the [Tree view](Tree_view.md). This will open the [Dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).



## Ограничения

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md).

## Notes

See [TechDraw LengthDimension](TechDraw_LengthDimension#Notes.md).



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



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 3PtAngleDimension/ru
