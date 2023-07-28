---
- GuiCommand:
   Name:TechDraw AxoHorizontalDimension
   MenuLocation:TechDraw → Annotations → Axonometric length dimension
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.21
---

# TechDraw AxoLengthDimension/en

## Description

The **TechDraw AxoLengthDimension** tool adds a length dimension to an axonometric view. The dimension may be the length of an edge or the distance between two points.

<img alt="" src=images/TechDraw_AxoLengthDimensionExample.png  style="width:300px;"> 
*Axonometric length dimensions based on an edge (blue) and two points (red)*

## Usage

1.  Do one of the following:
    -   Select two edges (e1 and e2 in the image). The first edge defines the direction of the dimension line and the measured distance. The second edge defines the direction of the extension lines.
    -   Select two edges (e3 and e4 in the image) and two points (v1 and v2 in the image). The first edge defines the direction of the dimension line. The second edge defines the direction of the extension lines. The points determine the measured distance.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_AxoLengthDimension.svg" width=16px> [Axonometric length dimension](TechDraw_AxoLengthDimension.md)** button.
    -   Select the **TechDraw → Dimensions → <img src="images/TechDraw_AxoLengthDimension.svg" width=16px> Axonometric length dimension** option from the menu.
3.  An axonometric dimension is added to the View.
4.  The dimension may be dragged to the desired position.
5.  If needed, add tolerances as described on [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

### Display 3D measurement 

See [TechDraw LengthDimension](TechDraw_LengthDimension#Display_3D_measurement.md).

### Change properties 

To change the properties of a dimension object either double-click it in the drawing or in the [Tree view](Tree_view.md). This will open the [Dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw AxoLengthDimension/en
