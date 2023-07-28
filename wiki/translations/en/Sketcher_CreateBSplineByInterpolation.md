---
- GuiCommand:
   Name:Sketcher CreateBSplineByInterpolation
   MenuLocation:Sketch → Sketcher geometries → Create B-spline by knots
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Shortcut:**G** **B** **I**
   Version:0.21
   SeeAlso:[Sketcher Periodic B-spline](Sketcher_CreatePeriodicBSpline.md)
---

# Sketcher CreateBSplineByInterpolation/en

## Description

This tool creates a B-spline curve passing through given points. See [this page](B-Splines.md) for more info about B-splines.

## Usage

1.  Press the **[<img src=images/Sketcher_CreateBSplineByInterpolation.svg style="width:16px"> [B-spline by knots](Sketcher_CreateBSplineByInterpolation.md)** button.
2.  Create a series of points by clicking in the [3D view](3D_view.md). While the command is active, the created points are connected with straight lines.
3.  Optionally press **M** before terminating the input to define the multiplicity of the knot at the last defined point (note that this may not always be respected, see [limitations](#Limitations.md) for details).
4.  Optionally press **Backspace** before terminating the input to delete the last created control point.
5.  Right-click to terminate the input and generate the curve.
6.  Depending on preferences, the tool may remain active to trace a new curve. Right-click again to exit the command.

## Notes

See [Sketcher CreateBSpline](Sketcher_CreateBSpline#Notes.md).

## Limitations

-   The resultant curve is no different than a (non-uniform) B-spline defined through control points. So all related limitations apply. See [Sketcher CreateBSpline](Sketcher_CreateBSpline#Limitations.md).
-   The B-splines created are always cubic (i.e. with degree 3).
-   The defined multiplicity may not always be respected:
    -   For a periodic spline, the first knot (coincident with last) always has a multiplicity of 2.
    -   For a non-periodic spline, the first and last knots always have a multiplicity of 4.
    -   If the points just before and just after have multiplicities \>=3, the piece between these two is fully continuous, and this (middle) point will only be constrained with point-on-object. If a knot is needed, consider using the insert knot tool.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateBSplineByInterpolation/en
