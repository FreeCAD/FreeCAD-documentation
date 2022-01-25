---
- GuiCommand:
   Name:Sketcher CreateBSpline
   MenuLocation: Sketch → Sketcher geometries → Create B-Spline
   Workbenches: [Sketcher](Sketcher_Workbench.md)
   Version:0.17
   SeeAlso:[Sketcher periodic B-Spline](Sketcher_CreatePeriodicBSpline.md)
---

# Sketcher CreateBSpline

## Description

This tool creates B-Spline curve from its control points. (See [this page](B-Splines.md) for more info about B-Splines.)

 ![](images/Sketcher_B-spline_example01.png )  
*A B-Spline curve (in white) defined by 4 control points. Pictured are the control polygon in green (the straight lines connecting the control points) and the weight circles in dark yellow. The green digit "3" in the center refers to the [degree](Sketcher_BSplineIncreaseDegree#Description.md) of the B-spline and the digits "(4)" at the ends of the B-spline refer to their [knot multiplicity](Sketcher_BSplineDecreaseKnotMultiplicity#Description.md). The red digit "3" denotes the control point weight which is defined as radius constraint to the control point circle.*

## Usage

1.  Press the **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [Create B-Spline](Sketcher_CreateBSpline.md)** button.
2.  Create a series of points by clicking in the 3D view. While the command is active, the created points are connected with straight lines, and a construction circle is created centred on each point.
3.  Right-click to terminate the input and generate the curve.
4.  Depending on preferences, the tool may remain active to trace a new curve. Right-click again to exit the command.

-   It is possible to define the weight of the control points by changing the radii of the weight circles. The equality constraints on the circles need to be deleted first. The radius constraint is arbitrary, the weight of the control points will be defined by the relative radii of the circles. It works similar to gravity: the bigger a circle is in relation to the others, the more the curve will be attracted to the control point.
-   The visibility of the control polygon, the curvature comb, the degree and the knot multiplicity can be toggled on/off from the [B-spline tools](Sketcher_Workbench#Sketcher_B-spline_tools.md) toolbar.
-   Check out the other tools in the [B-spline tools](Sketcher_Workbench#Sketcher_B-spline_tools.md) toolbar for more B-Spline editing tools.

## Limitations

-   Many types of constraints are not supported at this time. Only the B-spline\'s control point and end points can be constrained.
-   [Trimming](Sketcher_Trimming.md) and [extend](Sketcher_Extend.md) tools are not supported.
-   The shape of a B-spline curve can only be edited by dragging one of the control points. The knots lying on the curve cannot be selected.




 {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateBSpline
