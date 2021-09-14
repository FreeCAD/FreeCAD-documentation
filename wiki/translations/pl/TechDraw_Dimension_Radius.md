---
- GuiCommand:
   Name:TechDraw Dimension Radius
   MenuLocation:TechDraw → Dimensions → Insert Radius Dimension
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   SeeAlso:[TechDraw Dimension Diameter](TechDraw_Dimension_Diameter.md)
---

## Description

The Dimension Radius tool adds a radius dimension to a View. The dimension may be applied to any Edge in the drawing which is a circle or circular arc. The distance will initially be the projected distance (ie as shown on the drawing), but this may be changed to the actual 3D distance using the **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Link Dimension](TechDraw_Dimension_Link.md)** tool.

<img alt="" src=images/TechDraw_Dimension_Radius_example.png  style="width:130px;"> 
*Measuring a circle, indicating the radius*

## Usage

1.  Select a circle or circular arc in the drawing. (Note some arcs which appear to be circular are actually ellipses or BSplines. You cannot make a radius dimension in these cases)
2.  Press the **<img src="images/TechDraw_Dimension_Radius.svg" width=16px> [Dimension Radius](TechDraw_Dimension_Radius.md)** button
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.
4.  If needed, add tolerances as described in [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_Dimension_Length#Dimension_dialog.md).

## Limitations

Dimension objects are vulnerable to \"topological naming\" issues. See the information in the [TechDraw Dimension Length](TechDraw_Dimension_Length.md) tool for more information.

## Properties

This object has the same properties as the [TechDraw Dimension Length](TechDraw_Dimension_Length.md) tool. See that tool for details.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Dimension Radius tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Radius"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}  
