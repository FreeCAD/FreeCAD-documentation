---
 GuiCommand:
   Name: Sketcher BSplineIncreaseDegree
   Name/de: Sketcher BSplineGradErhöhen
   MenuLocation: Sketch , B-Spline-Werkzeuge , Grad des B-Splines erhöhen
   Workbenches: Sketcher_Workbench/de
   Version: 0.17
   SeeAlso: Sketcher_BSplineDecreaseDegree/de
---

# Sketcher BSplineIncreaseDegree/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:24px;"> [Sketcher BSplineGradErhöhen](Sketcher_BSplineIncreaseDegree/de.md) Erhöht den Grad (Ordnung) der [B-Splines](B-Splines.md).



## Anwendung

1.  Einen oder mehrere B-Splines auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_BSplineIncreaseDegree.svg" width=16px> [Grad des B-Splines erhöhen](Sketcher_BSplineIncreaseDegree/de.md)** drücken.

    -   Den Menüeintrag **Skizze → B-Spline-Werkzeuge → <img src="images/Sketcher_BSplineIncreaseDegree.svg" width=16px> Grad des B-Splines erhöhen** auswählen.

    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_BSplineIncreaseDegree.svg" width=16px> Grad des B-Splines erhöhen** im Kontextmenü auswählen.



## Beispiel

B-Splines sind im Grunde eine Kombination aus [Bézierkurven](B-Splines/de#B.C3.A9zierkurven.md) (sehr schön erklärt in [diesem](https://www.youtube.com/watch?v=bE1MrrqBAl8) und [diesem](https://www.youtube.com/watch?v=xXJylM2S72s) Video).

In diesem kubischen B-Spline (Grad 3) gibt es 3 Abschnitte, d.h. 3 Kurven, die an 2 Knoten verbunden sind.

Der Grad wird durch die Zahl in der Mitte repräsentiert. Siehe <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:16px;"> [B-Spline-Grad ein- / ausblenden](Sketcher_BSplineDegree/de.md).

<img alt="" src=images/Sketcher_BSplineDegree3.png  style="width:400px;"> 
*B-Spline mit Grad 3 und 2 Knoten, die jeweils die Vielfachheit 1 besitzen.*

The outer segments each have 2 control points, the inner segment has none to ensure the knots have multiplicity 1. See [this page](Sketcher_BSplineDecreaseKnotMultiplicity#Description.md) for an explanation about multiplicity.

Increasing the degree to 4 will add control points without changing the shape of the B-spline:

<img alt="" src=images/Sketcher_BSplineDegree4.png  style="width:400px;"> 
*Same B-spline where the degree was changed from 3 to 4. Note that the knot multiplicity has also increased.*

From this result you cannot get back to the initial state of the B-spline by decreasing the degree. Some information is lost when the degree of a B-spline is changed. Decreasing the degree back to 3 leads to this:

<img alt="" src=images/Sketcher_BSplineDegree3from4.png  style="width:400px;"> 
*Same B-spline where the degree was changed back from 4 to 3. Note that the knot multiplicity has increased again. Depending on the B-spline, the algorithm to decrease the degree may add a lot of knots to preserve the shape as has happened here.*

Each segment now has 2 control points and each knot is coincident with an additional control point. The knots have *C^0^* continuity so that the B-spline will get \"corners\" if you move a control point. The information of a higher continuity is therefore lost. See [this page](Sketcher_BSplineDecreaseKnotMultiplicity#Description.md) for an explanation about continuity.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseDegree/de
