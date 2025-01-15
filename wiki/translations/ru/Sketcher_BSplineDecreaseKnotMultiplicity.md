---
 GuiCommand:
   Name/ru: Уменьшение кратности узлов
   Name: Sketcher_BSplineDecreaseKnotMultiplicity
   MenuLocation: Sketch , B-сплйан инструменты эскиза , Уменьшение кратности узлов
   Workbenches: Sketcher_Workbench/ru
   Version: 0.17
   SeeAlso: Sketcher_BSplineKnotMultiplicity/ru, Sketcher_BSplineIncreaseKnotMultiplicity/ru
---

# Sketcher BSplineDecreaseKnotMultiplicity/ru


</div>



## Описание

The <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:24px;"> [Sketcher BSplineDecreaseKnotMultiplicity](Sketcher_BSplineDecreaseKnotMultiplicity.md) tool decreases the multiplicity of a [B-spline](B-Splines.md) knot.



## Применение

1.  Select a B-spline knot.
2.  There are several ways to invoke the tool:
    -   Press the **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:16px"> [Decrease knot multiplicity](Sketcher_BSplineDecreaseKnotMultiplicity.md)** button.
    -   Select the **Sketch → Sketcher B-spline tools → <img src="images/Sketcher_BSplineDecreaseKnotMultiplicity.svg" width=16px> Decrease knot multiplicity** option from the menu.

## Example

See [Sketcher_BSplineIncreaseKnotMultiplicity](Sketcher_BSplineIncreaseKnotMultiplicity#Example.md)

## Notes

If you decrease the multiplicity of a knot to zero, the knot vanishes. Mathematically it then appears zero times in the knot vector, meaning there is no longer a basis function. Understanding this requires some math, but it will also be clear if you look at the multiplicity. For example a knot with multiplicity 0 on a B-spline with degree 3 means that at the position of the knot two Bézier pieces are connected with *C^3^* continuity. So the third derivative should be equal on both sides of the knot. However for a cubic Bézier curve this means that both sides must be part of the same curve. There is then effectively no longer a knot connecting two Bézier curves.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineDecreaseKnotMultiplicity/ru
