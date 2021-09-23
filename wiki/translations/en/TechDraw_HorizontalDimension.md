---
- GuiCommand:
   Name:TechDraw HorizontalDimension
   MenuLocation:TechDraw → Dimensions → Insert Horizontal Dimension
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Shortcut:**Shift** + **H**
   SeeAlso:[TechDraw LengthDimension](TechDraw_LengthDimension.md), [TechDraw VerticalDimension](TechDraw_VerticalDimension.md)
---

# TechDraw HorizontalDimension/en

## Description

The Horizontal Dimension tool adds a horizontal dimension to a View. The dimension may be between two vertices, the length of one edge or the horizontal distance between 2 edges. The distance will initially be the projected distance (ie as shown on the drawing), but this may be changed to the actual 3D distance using the **<img src="images/TechDraw_LinkDimension.svg" width=16px> [TechDraw LinkDimension](TechDraw_LinkDimension.md)** tool.

<img alt="" src=images/TechDraw_Dimension_Horizontal_example.png  style="width:200px;"> 
*Length dimension taken from two arbitrary nodes of the view; the distance is measured horizontally*

## Usage

1.  Select the points or edge which define your measurement.
2.  Press the **<img src="images/TechDraw_HorizontalDimension.svg" width=16px> [Horizontal Dimension](TechDraw_HorizontalDimension.md)** button
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.
4.  If needed, add tolerances as described in [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).

## Limitations

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information.

## Properties

See [TechDraw LengthDimension](TechDraw_LengthDimension#Properties.md).

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Horizontal Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "DistanceX"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw HorizontalDimension/en
