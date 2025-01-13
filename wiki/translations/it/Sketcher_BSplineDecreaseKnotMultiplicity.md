---
 GuiCommand:
   Name: Sketcher_BSplineDecreaseKnotMultiplicity
   Name/it: Diminuisci la molteplicità
   Workbenches: Sketcher Workbench/it
   MenuLocation: Sketch , Strumenti B-spline , Diminuisci la molteplicità
   Version: 0.17
   SeeAlso: Sketcher CompCreateBSpline/it
---

# Sketcher BSplineDecreaseKnotMultiplicity/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Diminuisce la molteplicità del nodo di curva B-spline (vedere: [B-spline](https://en.wikipedia.org/wiki/B-spline)).


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un nodo di una B-spline
2.  Richiamare lo strumento usando uno di questi metodi:
    -   Premere il pulsante **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:16px"> [Diminuisci la molteplicità](Sketcher_BSplineDecreaseKnotMultiplicity/it.md)** nella barra degli strumenti.
    -   Usare la voce **Sketch → Strumenti B-spline → [<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:16px"> Diminuisci la molteplicità** dal menu principale.


</div>

## Example

See [Sketcher_BSplineIncreaseKnotMultiplicity](Sketcher_BSplineIncreaseKnotMultiplicity#Example.md)

## Notes

If you decrease the multiplicity of a knot to zero, the knot vanishes. Mathematically it then appears zero times in the knot vector, meaning there is no longer a basis function. Understanding this requires some math, but it will also be clear if you look at the multiplicity. For example a knot with multiplicity 0 on a B-spline with degree 3 means that at the position of the knot two Bézier pieces are connected with *C^3^* continuity. So the third derivative should be equal on both sides of the knot. However for a cubic Bézier curve this means that both sides must be part of the same curve. There is then effectively no longer a knot connecting two Bézier curves.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineDecreaseKnotMultiplicity/it
