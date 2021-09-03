---
- GuiCommand:
   Name:TechDraw 2PointCosmeticLine
   MenuLocation:TechDraw → Add Lines → Add Cosmetic Line between 2 points
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.19
   SeeAlso:[TechDraw Centerline to Face(s)](TechDraw_FaceCenterLine.md), [TechDraw Centerline between 2 Lines](TechDraw_2LineCenterLine.md)
---

## Описание

The 2PointCosmeticLine tool adds a cosmetic line between two Vertices (Points). The vertices can be 2d or 3d. The resulting line can be used for dimensioning. The line\'s appearance can be modified using the [Remove Cosmetic Object](TechDraw_CosmeticEraser.md) tool.

<img alt="" src=images/CosLine2PointsSample.png  style="width:200px;">


*Cosmetic line between 2 Points*

## Применение

1.  Select 2 Vertexes in a View or 2 Vertexes in the 3D view.
2.  Press the **<img src="images/TechDraw-line2points.svg" width=16px> Add Cosmetic line between 2 Points** button.
3.  A dialog will open where you can adjust the coordinates of the 2 points.
4.  A line will be added to connect the 2 selected Vertices. In the case of 3d points, the line will connect the projection of the selected points.

To delete a cosmetic line, select it and use the toolbar button **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Remove Cosmetic Object](TechDraw_CosmeticEraser.md)**.

## Editing Cosmetic Lines 

To change the endpoints of a cosmetic line, **<img src="images/TechDraw-line2points.svg" width=16px> Add Cosmetic line between 2 Points
**

1.  Select the cosmetic line.
2.  Press **<img src="images/TechDraw-line2points.svg" width=16px> Add Cosmetic line between 2 Points**.
3.  A dialog will open where you can change the coordinates of the endpoints.
4.  Press **OK** to see your changes.

To change the appearance of a cosmetic line, use [Remove Cosmetic Object](TechDraw_CosmeticEraser.md).

## Свойства

Cosmetic lines have no properties of their own, as they are not document objects.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Cosmetic lines can be created using the makeCosmeticLine(v1, v2) or makeCosmeticLine3d(v1, v2) methods of DrawViewPart.





{{TechDraw Tools navi

}}  
