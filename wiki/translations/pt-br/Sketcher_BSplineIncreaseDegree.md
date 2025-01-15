---
 GuiCommand:
   Name: Sketcher BSplineIncreaseDegree
   MenuLocation: Sketch , Sketcher B-spline tools , Increase B-spline degree
   Workbenches: Sketcher_Workbench
   Version: 0.17
   SeeAlso: Sketcher_BSplineDecreaseDegree
---

# Sketcher BSplineIncreaseDegree/pt-br

## Description

The <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:24px;"> [Sketcher BSplineIncreaseDegree](Sketcher_BSplineIncreaseDegree.md) tool increases the degree (order) of [B-splines](B-Splines.md).

## Usage

1.  Select one or more B-splines.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_BSplineIncreaseDegree.svg" width=16px> [Increase B-spline degree](Sketcher_BSplineIncreaseDegree.md)** button.

    -   Select the **Sketch → Sketcher B-spline tools → <img src="images/Sketcher_BSplineIncreaseDegree.svg" width=16px> Increase B-spline degree** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_BSplineIncreaseDegree.svg" width=16px> Increase B-spline degree** option from the context menu.

## Example

B-splines are basically a combination of [Bézier curves](B-Splines#B.C3.A9zier_curves.md) (nicely explained in [this](https://www.youtube.com/watch?v=bE1MrrqBAl8) and [this](https://www.youtube.com/watch?v=xXJylM2S72s) video).

In this cubic B-spline (degree 3) there are 3 segments, meaning 3 curves are connected at 2 knots.

The degree is indicated by the number in the center. See <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:16px;"> [Show/hide B-spline degree](Sketcher_BSplineDegree.md).

<img alt="" src=images/Sketcher_BSplineDegree3.png  style="width:400px;"> 
*B-spline with degree 3 and 2 knots that each have multiplicity 1.*

The outer segments each have 2 control points, the inner segment has none to ensure the knots have multiplicity 1. See [this page](Sketcher_BSplineDecreaseKnotMultiplicity#Description.md) for an explanation about multiplicity.

Increasing the degree to 4 will add control points without changing the shape of the B-spline:

<img alt="" src=images/Sketcher_BSplineDegree4.png  style="width:400px;"> 
*Same B-spline where the degree was changed from 3 to 4. Note that the knot multiplicity has also increased.*

From this result you cannot get back to the initial state of the B-spline by decreasing the degree. Some information is lost when the degree of a B-spline is changed. Decreasing the degree back to 3 leads to this:

<img alt="" src=images/Sketcher_BSplineDegree3from4.png  style="width:400px;"> 
*Same B-spline where the degree was changed back from 4 to 3. Note that the knot multiplicity has increased again. Depending on the B-spline, the algorithm to decrease the degree may add a lot of knots to preserve the shape as has happened here.*

Each segment now has 2 control points and each knot is coincident with an additional control point. The knots have *C^0^* continuity so that the B-spline will get \"corners\" if you move a control point. The information of a higher continuity is therefore lost. See [this page](Sketcher_BSplineDecreaseKnotMultiplicity#Description.md) for an explanation about continuity.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseDegree/pt-br
