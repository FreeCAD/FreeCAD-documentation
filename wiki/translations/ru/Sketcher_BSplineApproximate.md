---
- GuiCommand:/ru
   Name/ru:Преобразовать геометрию в B-Сплайн
   Name:Sketcher_BSplineApproximate
   MenuLocation:Sketch → Эскизирование B-spline tools → Преобразовать геометрию в B-Сплайн
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   Version:0.17
   SeeAlso:[Создать B-сплайн](Sketcher_CompCreateBSpline/ru.md)
---

# Sketcher BSplineApproximate/ru

## Описание

Converts compatible geometry, edges and curves, into a B-spline (see [this page](B-Splines.md) for more info about B-splines).

<img alt="" src=images/sketcher_BSplineConvertToNurb.png  style="width:400px;"> 
*Various objects before conversion.*

<img alt="" src=images/sketcher_BSplineConvertToNurb1.png  style="width:400px;"> 
*The same objects after conversion to B-splines.*

## Применение

1.  Select one or several sketch segments and press the the toolbar button **[<img src=images/Sketcher_BSplineApproximate.svg style="width:24px"> [Convert geometry to B-spline](Sketcher_BSplineApproximate.md)**.

Make sure to have either the spline [degree](Sketcher_BSplineDegree.md), [polygon](Sketcher_BSplinePolygon.md), [comb](Sketcher_BSplineComb.md), [multiplicity](Sketcher_BSplineKnotMultiplicity.md) or [weight](Sketcher_BSplinePoleWeight.md) visible, otherwise nothing seems to happen. If you converted straight lines, you first need to [increase the degree](Sketcher_BSplineIncreaseDegree.md) of the lines to make them \"bendable\".


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineApproximate/ru
