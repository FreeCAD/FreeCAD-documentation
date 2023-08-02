---
- GuiCommand:
   Name: Sketcher_BSplineIncreaseKnotMultiplicity
   Name/it: Aumenta la molteplicità di nodo
   MenuLocation: Sketch -> Strumeti B-spline -> Aumenta la molteplicità di nodo
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

B-splines are basically a combination of [Bézier curves](B-Splines#B.C3.A9zier_curves.md) (nicely explained in [this](https://www.youtube.com/watch?v=bE1MrrqBAl8) and [this](https://www.youtube.com/watch?v=xXJylM2S72s) video). The points where two Bézier pieces are connected are called knots. A knot on a spline with degree *d* and with the multiplicity *m* means that the curve left and right to the knot has at least an equal *n* order derivative (called *C*^*n*^ continuity) whereas $n=d-m$.
Here is a cubic spline ($d=3$) whose knots have the multiplicity 1. The multiplicity is indicated by the number in parentheses. The indication can be changed using the toolbar button **[<img src=images/Sketcher_BSplineKnotMultiplicity.svg style="width:24px"> [Show/hide B-spline knot multiplicity](Sketcher_BSplineKnotMultiplicity.md)**:

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity1.png  style="width:400px;"> 
*B-spline where both knots have the multiplicity 1.*

A multiplicity of 3 will change this spline so that even the first order derivatives are not equal (*C*^0^ continuity). Here is the same spline where the left\'s knot multiplicity was increased to 3:

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity3.png  style="width:400px;"> 
*B-spline from above with knot multiplicity 3. A control point was moved to show that the knot has ''C''<sup>0</sup> continuity.*

A consequence of a higher multiplicity is that for the price of loosing continuity you gain local control. This means the change of one control point only affects the spline locally to this changed point. This can be seen in this example, where the spline from the first image above was taken and its second control point from the right side was moved up:

<img alt="" src=images/Sketcher_KnotMultiplicity_locality.png  style="width:400px;"> 
*Effect of locality due to different multiplicity.*

One can see that the spline with knot multiplicity 1 is completely changed while the one with multiplicity 2 kept its form at its left side.



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un nodo di una B-spline
2.  Richiamare lo strumento usando uno di questi metodi:
    -   Premere il pulsante **[<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:16px"> Aumenta la molteplicità del nodo** nella barra degli strumenti.
    -   Usare la voce **Sketch → Strumenti B-spline → [<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:16px"> Aumenta la molteplicità del nodo** dal menu principale.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseKnotMultiplicity/it
