---
- GuiCommand:
   Name:TechDraw HorizontalExtentDimension
   MenuLocation:TechDraw → Dimensions → Insert Horizontal Extent Dimension
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.19
   SeeAlso:[TechDraw LengthDimension](TechDraw_LengthDimension.md), [TechDraw VerticalExtentDimension](TechDraw_VerticalExtentDimension.md)
---

# TechDraw HorizontalExtentDimension/pl

## Description

The Horizontal Extent Dimension tool adds a linear dimension to a View. The dimension extends from the left most point on the selected objects to the right most point. A CosmeticVertex will be placed at each point.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Horizontal Extent dimension of BSpline Face*

## How to use 

1.  Select a View or a collection of Edges in a View.
2.  Press the **<img src="images/TechDraw_HorizontalExtentDimension.svg" width=16px> [Horizontal Extent Dimension](TechDraw_HorizontalExtentDimension.md)** button
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.

## Limitations

Dimension objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information.

## Properties

See [TechDraw LengthDimension](TechDraw_LengthDimension#Properties.md). Exceptions noted below.

### Data

-    **MeasureType**: `True` - based on 3D geometry or \"Projected\" - based on the drawing. Not normally manipulated directly by the end user. Not yet implemented for Dimension Horizontal Extent.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Horizontal Extent Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
selection = [(view1, 'Edge1'), (view1, 'Edge2')]  #or [] for all
hExtentDim = TechDraw.Dimension.makeExtentDim(selection, HORIZONTAL)
rc = page.addView(hExtentDim)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw HorizontalExtentDimension/pl
