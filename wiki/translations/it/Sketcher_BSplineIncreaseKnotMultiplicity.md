---
 GuiCommand:
   Name: Sketcher_BSplineIncreaseKnotMultiplicity
   Name/it: Aumenta la molteplicità di nodo
   MenuLocation: Sketch , Strumeti B-spline , Aumenta la molteplicità di nodo
   Workbenches: Sketcher Workbench/it
   Version: 0.17
   SeeAlso: Sketcher CompCreateBSpline/it
---

# Sketcher BSplineIncreaseKnotMultiplicity/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Aumenta la molteplicità del nodo di curva B-spline (vedere: [B-spline](https://en.wikipedia.org/wiki/B-spline)).


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un nodo di una B-spline
2.  Richiamare lo strumento usando uno di questi metodi:
    -   Premere il pulsante **[<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:16px"> Aumenta la molteplicità del nodo** nella barra degli strumenti.
    -   Usare la voce **Sketch → Strumenti B-spline → [<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:16px"> Aumenta la molteplicità del nodo** dal menu principale.


</div>

## Example

B-splines are basically a combination of [Bézier curves](B-Splines#B.C3.A9zier_curves.md) (nicely explained in [this](https://www.youtube.com/watch?v=bE1MrrqBAl8) and [this](https://www.youtube.com/watch?v=xXJylM2S72s) video). The points where two Bézier pieces are connected are called knots. A knot with multiplicity *m* on a B-spline with degree *d* means the curve to the left and right of the knot has at least an equal *n* order derivative (called *C^n^* continuity) where *n = d - m*.

In this cubic B-spline (degree 3) there are 3 segments, meaning 3 curves are connected at 2 knots. The knots have multiplicity 1.

The multiplicity is indicated by the numbers in round brackets. See <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:16px;"> [Show/hide B-spline knot multiplicity](Sketcher_BSplineKnotMultiplicity.md).

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity1.png  style="width:400px;"> 
*B-spline where both knots have multiplicity 1.*

A multiplicity of 3 will change this B-spline so that even the first order derivatives are not equal (*C^0^* continuity). Here is the same B-spline where the multiplicity of the knot on the left was increased to 3:

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity3.png  style="width:400px;"> 
*Same B-spline with knot multiplicity 3. A control point was moved to show that the knot has ''C<sup>0</sup>'' continuity.*

A consequence of a higher multiplicity is that for the price of loosing continuity you gain local control. Meaning changing one control point will only affect the B-spline locally.

This can be seen in this example, where the B-spline with knot multiplicity 1 from the first image above was taken, and the second control point from the right was moved up. As a result the complete shape of the B-spline has changed:

<img alt="" src=images/Sketcher_KnotMultiplicity_locality1.png  style="width:400px;">

After increasing the multiplicity of the knots to 2, moving the second control point from the right results in significant changes on the right side of the shape only:

<img alt="" src=images/Sketcher_KnotMultiplicity_locality2.png  style="width:400px;">

## Notes

-   Knot multiplicity can also be increased with [Sketcher BSplineInsertKnot](Sketcher_BSplineInsertKnot.md).


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseKnotMultiplicity/it
