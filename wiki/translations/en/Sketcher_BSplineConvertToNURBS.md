---
 GuiCommand:
   Name: Sketcher BSplineConvertToNURBS
   MenuLocation: Sketch , Sketcher B-spline tools , Convert geometry to B-spline
   Workbenches: Sketcher_Workbench
   Version: 0.17
   SeeAlso: Sketcher_CreateBSpline
---

# Sketcher BSplineConvertToNURBS/en

## Description

The <img alt="" src=images/Sketcher_BSplineConvertToNURBS.svg  style="width:24px;"> [Sketcher BSplineConvertToNURBS](Sketcher_BSplineConvertToNURBS.md) tool converts edges to [B-splines](B-Splines.md).

<img alt="" src=images/sketcher_BSplineConvertToNurb.png  style="width:300px;"> 
*Various objects before conversion.*

<img alt="" src=images/sketcher_BSplineConvertToNurb1.png  style="width:300px;"> 
*The same objects after conversion to B-splines.*

## Usage

1.  Select one or more edges.
2.  There are several ways to invoke the tool:
    -   Press the **[<img src=images/Sketcher_BSplineConvertToNURBS.svg style="width:16px"> [Convert geometry to B-spline](Sketcher_BSplineConvertToNURBS.md)** button.
    -   Select the **Sketch → Sketcher B-spline tools → <img src="images/Sketcher_BSplineConvertToNURBS.svg" width=16px> Convert geometry to B-spline** option from the menu.
3.  The edges are converted.

## Notes

-   Make sure to have the B-spline [degree](Sketcher_BSplineDegree.md), [polygon](Sketcher_BSplinePolygon.md), [comb](Sketcher_BSplineComb.md), [multiplicity](Sketcher_BSplineKnotMultiplicity.md) and/or [weight](Sketcher_BSplinePoleWeight.md) visible, otherwise nothing seems to happen.
-   If you have converted straight lines you need to [increase the degree](Sketcher_BSplineIncreaseDegree.md) of the created B-splines to make them \"bendable\".
-   The tool does not remove the internal geometry of [conics](Sketcher_Workbench#Sketcher_CompCreateConic.md). This has to be deleted manually.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineConvertToNURBS/en
