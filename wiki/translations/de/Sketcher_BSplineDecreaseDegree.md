---
- GuiCommand:/de
   Name:Sketcher BSplineDecreaseDegree
   Name/de:Sketcher BSplineGradVerringern
   MenuLocation:Sketch → B-Spline-Werkzeuge → Grad des B-Splines verringern
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Version:0.19
   SeeAlso:[BSplineGrad](Sketcher_BSplineDegree/de.md), [BSplineGradVerringern](Sketcher_BSplineIncreaseDegree/de.md)
---

# Sketcher BSplineDecreaseDegree/de

## Beschreibung

Verringert den Grad (die Ordnung) eines B-Spline (siehe [diese Seite](B-Splines/de.md) für weitere Informationen über B-Splines).

B-Splines sind im Grunde eine Kombination aus [Bézier-Kurven](https://en.wikipedia.org/wiki/Bezier_curve#Constructing_B%C3%A9zier_curves) (sehr schön erklärt in [dies](https://www.youtube.com/watch?v=bE1MrrqBAl8) und [dieses](https://www.youtube.com/watch?v=xXJylM2S72s) Video).

In diesem kubischen Spline (Grad 3) gibt es 3 Segmente, d.h. 3 Kurven sind an 2 Knoten verbunden
(der Grad wird durch die Zahl angezeigt, die Anzeige kann über die Schaltfläche in der Werkzeugleiste geändert werden **<img src="images/Sketcher_BSplineDegree.svg" width=24px> [B-Spline Grad anzeigen/verbergen](Sketcher_BSplineDegree/de.md)**):

<img alt="" src=images/Sketcher_BSplineDegree3.png  style="width:400px;"> 
*B-Spline mit Grad 3 und 2 Knoten, die jeweils die Vielfachheit 1 haben.*

The outer segments have each 2 control points, the inner one none to fulfill the constraint that the knots have multiplicity 1. (see [this page](Sketcher_BSplineDecreaseKnotMultiplicity#Description.md) for an explanation of the multiplicity)

Decreasing the degree will not delete control points but try instead to conserve the shape of the spline. Therefore segments will be added. For our example you see a lot of new spline segments with each one control point and the shape of the spline has only slightly been changed:

<img alt="" src=images/Sketcher_BSplineDegree2.png  style="width:400px;"> 
*Same B-spline where the degree was changed from 3 to 2. Note that also the knot multiplicity was increased to conserve the spline shape. In effect the knots have now ''C''<sup>0</sup> continuity so that the spline will get "edges" when you move a control point. (see [this page](Sketcher_BSplineDecreaseKnotMultiplicity#Description.md) to for an explanation of the continuity)*

If you take this result and increase the degree, you cannot get the initial state of the spline because information was lost by the prior decrease of the degree. For our example increasing the degree again leads to this:

<img alt="" src=images/Sketcher_BSplineDegree3again.png  style="width:400px;"> 
*Same B-spline where the degree was changed back from 2 to 3. Note that the knot multiplicity increased too because the information for a possible higher continuity was lost.*

## Anwendung

1.  Eine Kante eines existierenden B-Splines auswählen und die Schaltfläche **[<img src=images/Sketcher_BSplineIncreaseDegree.svg style="width:24px"> '''Grad des B-Splines verringern''' drücken**.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineDecreaseDegree/de
