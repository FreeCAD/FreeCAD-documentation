---
- GuiCommand:/it
   Name:Sketcher_BSplineIncreaseDegree
   Name/it:Aumenta di grado
   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   MenuLocation:Sketch → Strumenti B-spline → Aumenta di grado
   Version:0.17
   SeeAlso:[Crea B-spline](Sketcher_CompCreateBSpline/it.md)
---

# Sketcher BSplineIncreaseDegree/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Aumenta il grado della B-spline (vedere: [B-spline](https://en.wikipedia.org/wiki/B-spline)).


</div>

B-splines are basically a combination of [Bézier curves](https://en.wikipedia.org/wiki/Bezier_curve#Constructing_B%C3%A9zier_curves) (nicely explained in [this](https://www.youtube.com/watch?v=bE1MrrqBAl8) and [this](https://www.youtube.com/watch?v=xXJylM2S72s) video).

In this cubic spline (degree 3) there are 3 segments, meaning 3 curves are connected at 2 knots
(degree is indicated by the number, indication can be changed using the toolbar button **[<img src=images/Sketcher_BSplineDegree.svg style="width:24px"> [Show/hide B-spline degree](Sketcher_BSplineDegree.md)**):

<img alt="" src=images/Sketcher_BSplineDegree3.png  style="width:400px;"> 
*B-spline with degree 3 and 2 knots that each have the multiplicity 1.*

The outer segments have each 2 control points, the inner one none to fulfill the constraint that the knots have multiplicity 1. (see [this page](Sketcher_BSplineDecreaseKnotMultiplicity#Description.md) for an explanation of the multiplicity)

Increasing the degree will add control points and the shape of the spline is not changed:

<img alt="" src=images/Sketcher_BSplineDegree4.png  style="width:400px;"> 
*Same B-spline where the degree was changed from 3 to 4. Note that also the knot multiplicity was increased.*

If you take this result and decrease the degree, you cannot get the initial state of the spline information will be lost by this operation. For our example decreasing the degree again leads to this:

<img alt="" src=images/Sketcher_BSplineDegree3from4.png  style="width:400px;"> 
*Same B-spline where the degree was changed back from 4 to 3. Note that the knot multiplicity was increased. Depending on the spline, the algorithm to decrease the degree may add a lot of knots to preserve the spline shape as happened in this example.*

You can see that now each segment has 2 control points and the knots are coincident with each a further control point. The knots have now *C*^0^ continuity so that the spline will get \"edges\" when you move a control point. So the information of a higher continuity is lost. (see [this page](Sketcher_BSplineDecreaseKnotMultiplicity#Description.md) to for an explanation of the continuity)

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un bordo da una B-spline esistente e premere **[<img src=images/Sketcher_BSplineIncreaseDegree.svg style="width:16px"> [Aumenta di grado](Sketcher_BSplineIncreaseDegree/it.md)**.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseDegree/it
