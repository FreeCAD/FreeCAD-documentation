---
- GuiCommand:
   Name: Sketcher BSplineDecreaseDegree
   MenuLocation: Sketch -> Sketcher B-spline tools -> Decrease B-spline degree
   Workbenches: Sketcher_Workbench
   Version: 0.19
   SeeAlso: Sketcher_BSplineDegree, Sketcher_BSplineIncreaseDegree
---

# Sketcher BSplineDecreaseDegree/pt-br

## Description

Decreases the degree (order) of a B-spline (see [this page](B-Splines.md) for more info about B-splines).

B-splines are basically a combination of [Bézier curves](https://en.wikipedia.org/wiki/Bezier_curve#Constructing_B%C3%A9zier_curves) (nicely explained in [this](https://www.youtube.com/watch?v=bE1MrrqBAl8) and [this](https://www.youtube.com/watch?v=xXJylM2S72s) video).

In this cubic spline (degree 3) there are 3 segments, meaning 3 curves are connected at 2 knots
(the degree is indicated by the number, indication can be changed using the toolbar button **[<img src=images/Sketcher_BSplineDegree.svg style="width:24px"> [Show/hide B-spline degree](Sketcher_BSplineDegree.md)**):

<img alt="" src=images/Sketcher_BSplineDegree3.png  style="width:400px;"> 
*B-spline with degree 3 and 2 knots that each have the multiplicity 1.*

The outer segments have each 2 control points, the inner one none to fulfill the constraint that the knots have multiplicity 1. (see [this page](Sketcher_BSplineDecreaseKnotMultiplicity#Description.md) for an explanation of the multiplicity)

Decreasing the degree will not delete control points but try instead to conserve the shape of the spline. Therefore segments will be added. For our example you see a lot of new spline segments with each one control point and the shape of the spline has only slightly been changed:

<img alt="" src=images/Sketcher_BSplineDegree2.png  style="width:400px;"> 
*Same B-spline where the degree was changed from 3 to 2. Note that also the knot multiplicity was increased to conserve the spline shape. In effect the knots have now ''C''<sup>0</sup> continuity so that the spline will get "edges" when you move a control point. (see [this page](Sketcher_BSplineDecreaseKnotMultiplicity#Description.md) to for an explanation of the continuity)*

If you take this result and increase the degree, you cannot get the initial state of the spline because information was lost by the prior decrease of the degree. For our example increasing the degree again leads to this:

<img alt="" src=images/Sketcher_BSplineDegree3again.png  style="width:400px;"> 
*Same B-spline where the degree was changed back from 2 to 3. Note that the knot multiplicity increased too because the information for a possible higher continuity was lost.*

## Usage

1.  Select an edge from an existing B-spline, and press **[<img src=images/Sketcher_BSplineDecreaseDegree.svg style="width:24px"> '''Decrease B-spline degree'''**.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineDecreaseDegree/pt-br
