---
- GuiCommand:
   Name:TechDraw FaceCenterLine
   MenuLocation:TechDraw → Add Lines → Add Centerline to Face(s)
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.19
   SeeAlso:[TechDraw Cosmetic Vertex](TechDraw_CosmeticVertex.md), [TechDraw Centerline between 2 Lines](TechDraw_2LineCenterLine.md), [TechDraw Centerline between 2 Points](TechDraw_2PointCenterLine.md), [TechDraw Cosmetic Eraser](TechDraw_CosmeticEraser.md)
---

# TechDraw FaceCenterLine/pl

## Description

The FaceCenterLine tool adds a centerline to selected faces.

<img alt="" src=images/TechDraw_FaceCenterLine_Sample.png  style="width:400px;"> 
*Centerline added to face*

## Usage

1.  Select one or more Faces in a View.
2.  Press the **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> Add Centerline to Face(s)** button
3.  A dialog will open where you can specify attributes of the new centerline.
4.  A centerline will be added at the midpoint of the bounding box of the selected Face(s).

To delete a Centerline, select it and use the toolbar button **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Remove Cosmetic Object](TechDraw_CosmeticEraser.md)**.

## Editing Centerlines 

Any of the centerline command buttons (**<img src="images/TechDraw_FaceCenterLine.svg" width=16px> Add Centerline to Face(s)**, **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> [Add Centerline between 2 Lines](TechDraw_2LineCenterLine.md)**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> [Add Centerline between 2 Points](TechDraw_2PointCenterLine.md)**) can be used to edit any centerline.

1.  Select a centerline.
2.  Press any centerline command button.
3.  A dialog will open where you can change attributes of the centerline.
4.  Press **OK** to see your changes.

## Properties

Centerlines have no properties of their own, as they are no document objects. They have attributes that can be changed in the centerline edit dialog.

1.  Mode (radio buttons):
    -   **Vertical**: Forces a centerline vertical
    -   **Horizontal**: Forces a centerline horizontal
    -   ***Aligned**: This option is not possible for centerline to faces*
2.  **Shift Horiz**: Moves the centerline left or right of its normal position
3.  **Shift Vert**: Moves the centerline up or down from its normal position
4.  **Rotate**: Rotates the centerline around its center (degrees. + counterclockwise, - clockwise)
5.  **Extend**: Makes the centerline longer by this amount
6.  **Color**: Color of centerline
7.  **Weight**: Thickness of the centerline
8.  **Style**: <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continuous, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Dash, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Dot, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> DashDot, <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> DashDotDot

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Centerlines are not accessible from [macros](Macros.md) or the [Python](Python.md) console at this time.

## Notes

-   FaceCenterLine will eventually replace two View properties:
    -   
        **HorizCenterLine**
        
        : Show a horizontal centerline through view.

    -   
        **VertCenterLine**
        
        : Show a vertical centerline through view.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw FaceCenterLine/pl
