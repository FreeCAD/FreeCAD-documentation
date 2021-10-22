---
- GuiCommand:
   Name:Sketcher CreatePeriodicBSpline
   MenuLocation: Sketch → Sketcher geometries → Create periodic B-spline
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Version:0.17
   SeeAlso:[Sketcher B-spline](Sketcher_CreateBSpline.md)
---

# Sketcher CreatePeriodicBSpline/hr

## Description

This tool traces a periodic (closed) B-spline curve from its control points. (See [this page](B-Splines.md) for more info about B-splines.)

![](images/Sketcher_Periodic_B-spline_example01.png )



*A periodic B-spline curve (in white) made from 5 points. Pictured are the control polygon in green (the straight lines connecting the red points), the weight circles in blue and the curvature comb in green. The (3) digit in the centre refers to the degree of the B-spline, and the (1) and (2) digits on the knots lying on the curve refer to their multiplicity.*

## Usage

1.  Press the **<img src=images/Sketcher_CreatePeriodicBSpline.svg style="width:16px"> [Periodic B-spline](Sketcher_CreatePeriodicBSpline.md)** button.
2.  Create a series of points by clicking in the 3D view. While the command is active, the created points are connected with straight lines, and a construction circle is created centred on each point.
3.  Pick the first curve point, or right-click to terminate the input and generate the curve.
4.  Depending on preferences, the tool may remain active to trace a new curve. Right-click again to exit the command.

-   It is possible to define the weight of the control points by changing the radii of the weight circles. The equality constraints on the circles need to be deleted first. The radius constraint is arbitrary, the weight of the control points will be defined by the relative radii of the circles. It works similar to gravity: the bigger a circle is in relation to the others, the more the curve will be attracted to the control point.
-   The visibility of the control polygon, the curvature comb, the degree and the knot multiplicity can be toggled on/off from the [B-spline tools](Sketcher_Workbench#Sketcher_B-spline_tools.md) toolbar.
-   Check out the other tools in the [B-spline tools](Sketcher_Workbench#Sketcher_B-spline_tools.md) toolbar for more B-spline editing tools.

## Ograničenja

-   Many types of constraints are not supported at this time. Only the B-spline\'s control points and knots can be constrained.
-   [Trimming](Sketcher_Trimming.md) and [extend](Sketcher_Extend.md) tools are not supported.
-   The shape of a B-spline curve can only be edited by dragging one of the control points. The knots lying on the curve cannot be selected.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePeriodicBSpline/hr
