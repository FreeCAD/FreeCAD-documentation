---
 GuiCommand:
   Name: Sketcher CreateBSpline
   MenuLocation: Sketch , Sketcher geometries , Create B-spline
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **B** **B**
   Version: 0.17
   SeeAlso: Sketcher_CreatePeriodicBSpline
---

# Sketcher CreateBSpline/zh-cn

## Description

The <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:24px;"> [Sketcher CreateBSpline](Sketcher_CreateBSpline.md) tool creates a [B-spline](B-Splines.md) curve by control points. <small>(v1.0)</small> : Or optionally by knot points.

![](images/Sketcher_CreateBSpline_Example.png ) 
*B-spline curve (white) defined by 5 control points.<br>
The control polygon (green) connects the control points (marked with dark yellow weight circles).<br>
The number 3 (green, without brackets) in the center refers to the [degree](Sketcher_BSplineIncreaseDegree#Description.md) of the B-spline.<br>
The numbers (1) and (4) (green, in round brackets) refer to the [multiplicity](Sketcher_BSplineDecreaseKnotMultiplicity#Description.md) of the knot points.<br>
The numbers [1.00] (green, in square brackets) refer to the weights of the control points.*

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_CreateBSpline.svg" width=16px> [B-spline by control points](Sketcher_CreateBSpline.md)** button.
    -   Select the **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreateBSpline.svg" width=16px> Create B-spline** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_CreateBSpline.svg" width=16px> Create B-spline** option from the context menu. <small>(v1.0)</small> 
    -   Use the keyboard shortcut: **G** then **B**, then **B**.
2.  The cursor changes to a cross with the tool icon.
3.  The **BSpline parameters** section (<small>(v1.0)</small> ) is added at the top of the [Sketcher Dialog](Sketcher_Dialog.md).
4.  Optionally press the **M** key or select from the dropdown list in the parameters section to change the tool mode:
    -   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:16px;"> **By control points**:
        1.  Optionally change the **Degree** (also possible after points have been picked):
            -   Enter a number greater than zero.
            -   Press the **U** key to increase the degree.
            -   Press the **J** key to decrease the degree.
    -   <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:16px;"> **By knots**: <small>(v1.0)</small> 
        1.  B-splines by knots are always created with degree 3. But their degree can be changed later. See [Notes](#Notes.md).
5.  Optionally press the **R** key or check the **Periodic** checkbox to create a closed B-spline (also possible after points have been picked). <small>(v1.0)</small> 
6.  Pick several points.
7.  Optionally press the **F** key before finishing to delete the last point. <small>(v1.0)</small> 
8.  Right-click or press **Esc** to finish the input.
9.  The B-spline is created, including a set of internal geometry (weight circles and knot points).
10. If the tool runs in [continue mode](Sketcher_Workbench#Continue_modes.md):
    1.  Optionally keep creating B-splines.
    2.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-   Elements of the internal geometry can be deleted. They can be recreated at any time with [Sketcher RestoreInternalAlignmentGeometry](Sketcher_RestoreInternalAlignmentGeometry.md).
-   After a B-spline is created, it is possible to define the weight of the control points by changing the radii of the weight circles. The equality constraints on the circles need to be deleted first. The radius constraint is arbitrary, the weight of the control points will be defined by the relative radii of the circles. It works similar to gravity: the bigger a circle is in relation to the others, the more the curve will be attracted to that control point.
-   The degree of a created B-spline can be [increased](Sketcher_BSplineIncreaseDegree.md) or [decreased](Sketcher_BSplineDecreaseDegree.md), and the multiplicity of its knots can be [increased](Sketcher_BSplineIncreaseKnotMultiplicity.md) or [decreased](Sketcher_BSplineIncreaseKnotMultiplicity.md) as well.
-   The visibility of the [degree](Sketcher_BSplineDegree.md), the [control polygon](Sketcher_BSplinePolygon.md), the [curvature comb](Sketcher_BSplineComb.md), the [knot multiplicity](Sketcher_BSplineKnotMultiplicity.md) and the [control point weight](Sketcher_BSplinePoleWeight.md) can be toggled on/off from the [Sketcher visual](Sketcher_Workbench#Sketcher_visual.md) toolbar.

## Limitations

-   Several constraints are not supported at this time.
-   The defined knot multiplicity may not always be respected:
    -   For a periodic spline, the first knot (coincident with last) always has a multiplicity of 2.
    -   For a non-periodic spline, the first and last knots always have a multiplicity of 4.
    -   If the points just before and just after have multiplicities \>=3, the piece between these two is fully continuous, and this (middle) point will only be constrained with point-on-object. If a knot is needed, consider using the [insert knot tool](Sketcher_BSplineInsertKnot.md).


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateBSpline/zh-cn
