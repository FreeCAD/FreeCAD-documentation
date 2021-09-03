---
- GuiCommand:
   Name:TechDraw Dimension Angle3Pt
   MenuLocation:TechDraw → Dimension Angle3Pt
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.18
   SeeAlso:[TechDraw Dimension Angle](TechDraw_Dimension_Angle.md)
---

## Description

The <img alt="" src=images/TechDraw_Dimension_Angle3Pt.svg  style="width:24px;"> Dimension Angle3Pt tool adds a angular dimension to a View. The dimension may be specified by selecting three Vertices on a View. **Note that the second of the three Vertices is the apex of the angle**. The Angle3Pt will initially be the projected angle (ie as shown on the drawing), but this may be changed to the actual 3D angle using the **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Link Dimension](TechDraw_Dimension_Link.md)** tool.

 <img alt="" src=images/TechDraw_Dimension_Angle3Pt_example.png  style="width:200px;">  
*Measuring the angle between two straight lines using three vertices; the second vertex should be the apex of the angle*

## Usage

1.  Select the points or edge which define your measurement.
2.  Press the **<img src="images/TechDraw_Dimension_Angle3Pt.png" width=16px> [Dimension Angle3Pt](TechDraw_Dimension_Angle3Pt.md)** button
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.
4.  If needed, add tolerances as described in [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_Dimension_Length#Dimension_dialog.md).

## Limitations

Dimension objects are vulnerable to \"[topological naming](topological_naming_problem.md)\" issues. See the information in the <img alt="" src=images/TechDraw_Dimension_Length.svg  style="width:16px;"> [TechDraw Dimension Length](TechDraw_Dimension_Length.md) tool for more information.

## Properties

This object has the same properties as the [TechDraw Dimension Length](TechDraw_Dimension_Length.md) tool. See that tool for details.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Dimension Angle3Pt tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:

 
```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Angle3Pt"
dim1.References2D=[(view1, 'Vertex1',(view1, 'Vertex4'),(view1, 'Vertex2'))]
rc = page.addView(dim1)
```




 {{TechDraw Tools navi}}  
