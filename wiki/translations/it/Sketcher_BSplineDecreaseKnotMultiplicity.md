---
- GuiCommand:/it
   Name:Sketcher_BSplineDecreaseKnotMultiplicity
   Name/it:Diminuisci la molteplicità
   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   MenuLocation:Sketch → Strumenti B-spline → Diminuisci la molteplicità
   Version:0.17
   SeeAlso:[Crea B-spline](Sketcher_CompCreateBSpline/it.md)
---

# Sketcher BSplineDecreaseKnotMultiplicity/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Diminuisce la molteplicità del nodo di curva B-spline (vedere: [B-spline](https://en.wikipedia.org/wiki/B-spline)).


</div>

B-splines are basically a combination of [Bézier curves](B-Splines#B.C3.A9zier_curves.md) (nicely explained in [this](https://www.youtube.com/watch?v=bE1MrrqBAl8) and [this](https://www.youtube.com/watch?v=xXJylM2S72s) video). The points where two Bézier curves are connected to form the spline are called knots. A knot on a degree *d* spline with the multiplicity *m* means that the curve left and right to the knot has at least an equal *n* order derivative (called *C*^*n*^ continuity) whereas $n=d-m$.
Here is a cubic spline ($d=3$) whose knots have the multiplicity 1. The multiplicity is indicated by the number in parentheses. The indication can be changed using the toolbar button **[<img src=images/Sketcher_BSplineKnotMultiplicity.svg style="width:24px"> [Show/hide B-spline knot multiplicity](Sketcher_BSplineKnotMultiplicity.md)**):

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity1.png  style="width:400px;">


<div class="mw-translate-fuzzy">



*Curva B-spline che mostra una molteplicità di nodi decrescente.*


</div>

A multiplicity of 3 will change this spline so that even the first order derivatives are not equal (*C*^0^ continuity). Here is the same spline where the left\'s knot multiplicity was increased to 3:

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity3.png  style="width:400px;"> 
*B-spline from above with knot multiplicity 3. A control point was moved to show that the knot has ''C''<sup>0</sup> continuity.*

A consequence of a higher multiplicity is that for the price of loosing continuity you gain local control. This means the change of one control point only affects the spline locally to this changed point. This can be seen in this example, where the spline from the first image above was taken and its second control point from the right side was moved up:

<img alt="" src=images/Sketcher_KnotMultiplicity_locality.png  style="width:400px;"> 
*Effect of locality due to different multiplicity.*

One can see that the spline with knot multiplicity 1 is completely changed while the one with multiplicity 2 kept its form at its left side.

**Note:** If you decrease the multiplicity, the knot vanishes, because mathematically it appears then zero times in the knot vector, meaning there is no longer a basis function. Understanding this, requires some math, but it will also be clear when you look at the multiplicity: For example degree = 3 then multiplicity = 0 means that at the position of the knot two Bézier pieces are connected with *C*^3^ continuity. So the third derivative should be equal on both sides of the knot. However for a cubic Bézier curve (that is a polynom with degree 3) , this means both sides must be part of the same curve. So there is then actually no longer a knot connecting 2 different Bézier curves, the former knot is then simply a point onto one Bézier curve.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un nodo di una B-spline
2.  Richiamare lo strumento usando uno di questi metodi:
    -   Premere il pulsante **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:16px"> [Diminuisci la molteplicità](Sketcher_BSplineDecreaseKnotMultiplicity/it.md)** nella barra degli strumenti.
    -   Usare la voce **Sketch → Strumenti B-spline → [<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:16px"> Diminuisci la molteplicità** dal menu principale.


</div>

**Note:** Decreasing the multiplicity from 1 to 0 will remove the knot since the result would be a curve with an \"edge\" at the knot position (*C*^0^ continuity) and this is not supported. (To create curves with an \"edges\", you can create two splines and connect them.)


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineDecreaseKnotMultiplicity/it
