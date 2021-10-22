---
- GuiCommand:
   Name:Sketcher BSplineApproximate
   MenuLocation:Sketch → Sketcher B-spline tools → Convert geometry to B-spline
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Version:0.17
   SeeAlso:[Sketcher Create B-spline](Sketcher_CompCreateBSpline.md)
---

# Sketcher BSplineApproximate/de

## Beschreibung

Konvertiert kompatible Geometrie, Kanten und Kurven, in einen B-Spline (siehe [diese Seite](B-Splines/de.md) für weitere Informationen über B-Splines).

<img alt="" src=images/sketcher_BSplineConvertToNurb.png  style="width:400px;"> 
*Various objects before conversion.*

<img alt="" src=images/sketcher_BSplineConvertToNurb1.png  style="width:400px;"> 
*The same objects after conversion to B-splines.*

## Anwendung

1.  Select one or several sketch segments and press the the toolbar button **<img src=images/Sketcher_BSplineApproximate.svg style="width:24px"> [Convert Geometry to B-spline](Sketcher_BSplineApproximate.md)**.

Make sure to have either the spline [degree](Sketcher_BSplineDegree.md), [polygon](Sketcher_BSplinePolygon.md), [comb](Sketcher_BSplineComb.md), [multiplicity](Sketcher_BSplineKnotMultiplicity.md) or [weight](Sketcher_BSplinePoleWeight.md) visible, otherwise nothing seems to happen. If you converted straight lines, you first need to [increase the degree](Sketcher_BSplineIncreaseDegree.md) of the lines to make them \"bendable\".





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineApproximate/de
