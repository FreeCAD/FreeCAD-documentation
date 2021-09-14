---
- GuiCommand:/ru
   Name/ru:Показать/скрыть гребень кривизны B-сплайна
   Name:Sketcher_BSplineComb
   MenuLocation:Sketch → B-сплйан инструменты эскиза → Показать/скрыть гребень кривизны B-сплайна
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   Version:0.17
   SeeAlso:[Создать B-сплайн](Sketcher_CompCreateBSpline/ru.md)
---

## Описание

Shows or hides the display of the Curvature Comb of a B-spline (see [this page](B-Splines.md) for more info about B-splines).

The curvature comb indicates the curvature (value of the second-order derivative) of the B-spline at every position. The higher the curvature at a position, the more is the the comb away from the curve. For positive curvatures (\"turn to the right\"), the comb is at the other side of the curve than for negative curvatures.

![](images/sketcher_BSplineCurvatureShow.png ) *B-spline with a saddle point at its mid position - the curvature comb there is zero.*

## Usage

1.  Select a B-spline
2.  Either use the toolbar button **<img src=images/Sketcher_BSplineComb.svg style="width:16px"> [Show/hide B-spline curvature comb](Sketcher_BSplineComb.md)** or use the menu **Sketch → Sketcher B-spline tools → Show/Hide B-spline curvature comb**.





{{Sketcher Tools navi

}}  
