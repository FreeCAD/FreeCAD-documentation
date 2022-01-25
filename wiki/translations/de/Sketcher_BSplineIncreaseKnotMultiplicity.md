---
- GuiCommand:/de
   Name:Sketcher BSplineIncreaseKnotMultiplicity
   Name/de:Skizzierer BSplineErhöheKnotenVielfalt
   MenuLocation:Skizze → Skizzierer B-spline Werkzeuge → Erhöhe Knoten Vielfalt
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Version:0.17
   SeeAlso:[Erstelle B-spline](Sketcher_CompCreateBSpline/de.md)
---

# Sketcher BSplineIncreaseKnotMultiplicity/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Erhöht die Knotenvielfalt eines B-Spline Kurvenknotens (siehe [B-Spline](https://en.wikipedia.org/wiki/B-spline)).


</div>

B-splines are basically a combination of [Bézier curves](B-Splines#B.C3.A9zier_curves.md) (nicely explained in [this](https://www.youtube.com/watch?v=bE1MrrqBAl8) and [this](https://www.youtube.com/watch?v=xXJylM2S72s) video). The points where two Bézier curves are connected to form the spline are called knots. A knot on a degree *d* spline with the multiplicity *m* means that the curve left and right to the knot has at least an equal *n* order derivative (called *C*^*n*^ continuity) whereas $n=d-m$.
Here is a cubic spline ($d=3$) whose knots have the multiplicity 1. The multiplicity is indicated by the number in parentheses. The indication can be changed using the toolbar button **[<img src=images/Sketcher_BSplineKnotMultiplicity.svg style="width:24px"> [Show/hide B-spline knot multiplicity](Sketcher_BSplineKnotMultiplicity.md)**):

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity1.png  style="width:400px;"> 
*B-spline where both knots have the multiplicity 1.*

A multiplicity of 3 will change this spline so that even the first order derivatives are not equal (*C*^0^ continuity). Here is the same spline where the left\'s knot multiplicity was increased to 3:

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity3.png  style="width:400px;"> 
*B-spline from above with knot multiplicity 3. A control point was moved to show that the knot has ''C''<sup>0</sup> continuity.*

A consequence of a higher multiplicity is that for the price of loosing continuity you gain local control. This means the change of one control point only affects the spline locally to this changed point. This can be seen in this example, where the spline from the first image above was taken and its second control point from the right side was moved up:

<img alt="" src=images/Sketcher_KnotMultiplicity_locality.png  style="width:400px;"> 
*Effect of locality due to different multiplicity.*

One can see that the spline with knot multiplicity 1 is completely changed while the one with multiplicity 2 kept its form at its left side.

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle einen B-Spline Knoten aus.
2.  Rufe das Werkzeug mit mehreren Methoden auf:
    -   Drücke die **<img src="images/Sketcher_BSplineIncreaseKnotMultiplicity.svg" width=24px>** Schaltfläche in der Werkzeugleiste.
    -   Verwende den **Skizze → Skizzierer B-Spline Werkzeuge → Knotenvervielfalt erhöhen** Eintrag im oberen Menü.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseKnotMultiplicity/de
