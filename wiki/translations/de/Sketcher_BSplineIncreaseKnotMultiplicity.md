---
- GuiCommand   */de
   Name   *Sketcher BSplineIncreaseKnotMultiplicity
   Name/de   *Sketcher BSplineKnotenVielfachheitErhöhen
   MenuLocation   *Sketch → B-Spline-Werkzeuge → Vielfachheit eines Spline-Knotens erhöhen
   Workbenches   *[Sketcher](Sketcher_Workbench/de.md)
   Version   *0.17
   SeeAlso   *[BSplineKnotenVielfachheit](Sketcher_BSplineKnotMultiplicity/de.md), [BSplineKnotenVielfachheitVerringern](Sketcher_BSplineDecreaseKnotMultiplicity/de.md)
---

# Sketcher BSplineIncreaseKnotMultiplicity/de

## Beschreibung

Erhöht die Vielfachheit eines B-Spline-Knotens. (Siehe die Seite [B-Splines](B-Splines.md) für weitere Informationen über B-Splines).

B-splines are basically a combination of [Bézier curves](B-Splines#B.C3.A9zier_curves.md) (nicely explained in [this](https   *//www.youtube.com/watch?v=bE1MrrqBAl8) and [this](https   *//www.youtube.com/watch?v=xXJylM2S72s) video). The points where two Bézier curves are connected to form the spline are called knots. A knot on a degree *d* spline with the multiplicity *m* means that the curve left and right to the knot has at least an equal *n* order derivative (called *C*^*n*^ continuity) whereas $n=d-m$.
Here is a cubic spline ($d=3$) whose knots have the multiplicity 1. The multiplicity is indicated by the number in parentheses. The indication can be changed using the toolbar button **[<img src=images/Sketcher_BSplineKnotMultiplicity.svg style="width   *24px"> [Show/hide B-spline knot multiplicity](Sketcher_BSplineKnotMultiplicity.md)**)   *

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity1.png  style="width   *400px;"> 
*B-spline where both knots have the multiplicity 1.*

A multiplicity of 3 will change this spline so that even the first order derivatives are not equal (*C*^0^ continuity). Here is the same spline where the left\'s knot multiplicity was increased to 3   *

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity3.png  style="width   *400px;"> 
*B-spline from above with knot multiplicity 3. A control point was moved to show that the knot has ''C''<sup>0</sup> continuity.*

A consequence of a higher multiplicity is that for the price of loosing continuity you gain local control. This means the change of one control point only affects the spline locally to this changed point. This can be seen in this example, where the spline from the first image above was taken and its second control point from the right side was moved up   *

<img alt="" src=images/Sketcher_KnotMultiplicity_locality.png  style="width   *400px;"> 
*Effect of locality due to different multiplicity.*

One can see that the spline with knot multiplicity 1 is completely changed while the one with multiplicity 2 kept its form at its left side.

## Anwendung

1.  Einen B-Spline-Knoten auswählen.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen   *
    -   Die Schaltfläche **[<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width   *16px">  [Vielfachheit eines B-Spline-Knotens erhöhen](Sketcher_BSplineIncreaseKnotMultiplicity/de.md)** drücken.
    -   Den Menüeintrag **Sketch → B-Spline-Werkzeuge → [<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width   *16px"> Vielfachheit eines B-Spline-Knotens erhöhen** auswählen.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseKnotMultiplicity/de
