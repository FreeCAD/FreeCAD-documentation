---
- GuiCommand:
   Name:TechDraw Dimension Vertical Extent
   MenuLocation:TechDraw → Dimensions → Insert Vertical Extent Dimension 
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.19
   SeeAlso:[TechDraw Dimension Length](TechDraw_Dimension_Length.md), [TechDraw Dimension Horizontal Extent](TechDraw_Dimension_Horizontal_Extent.md)
---

## Description

The Dimension Vertical Extent tool adds a linear dimension to a View. The dimension extends from the bottom most point on the selected objects to the top most point. A CosmeticVertex will be placed at each point.

 <img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;">  
*Vertical Extent dimension of BSpline Face*

## Usage

1.  Select a View or a collection of Edges in a View.
2.  Press the **<img src="images/TechDraw_Dimension_Vertical_Extent.svg" width=16px> [Dimension Vertical Extent](TechDraw_Dimension_Vertical_Extent.md)** button
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.

## Limitations

Dimension objects are vulnerable to \"[topological naming](topological_naming_problem.md)\" issues. See the information in the **<img src="images/TechDraw_Dimension_Length.svg" width=16px> [TechDraw Dimension Length](TechDraw_Dimension_Length.md)** tool for more information.

## Properties

This object has the same properties as the [TechDraw Dimension Length](TechDraw_Dimension_Length.md) tool. See that tool for details. Exceptions noted.

### Data

-    **MeasureType**: `True` - based on 3D geometry or \"Projected\" - based on the drawing. Not normally manipulated directly by the end user. Not yet implemented for Dimension Vertical Extent.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Dimension Vertical Extent tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:

 
```python
selection = [(view1, 'Edge1'), (view1, 'Edge2')]  #or [] for all
hExtentDim = TechDraw.Dimension.makeExtentDim(selection, VERTICAL)
rc = page.addView(hExtentDim)
```




 {{TechDraw Tools navi}}  
