---
 GuiCommand:
   Name: Sketcher BSplineApproximate
   Name/de: Sketcher BSplineApproximieren
   MenuLocation: Skizze , B-Spline-Werkzeuge , Geometrie in B-Spline wandeln
   Workbenches: Sketcher_Workbench/de
   Version: 0.17
   SeeAlso: Sketcher_CompCreateBSpline/de
---

# Sketcher BSplineApproximate/de



## Beschreibung

Konvertiert kompatible Geometrie, Kanten und Kurven, in einen B-Spline (siehe [diese Seite](B-Splines/de.md) für weitere Informationen über B-Splines).

<img alt="" src=images/sketcher_BSplineConvertToNurb.png  style="width:400px;"> 
*Verschiedene Objekte vor dem Konvertieren.*

<img alt="" src=images/sketcher_BSplineConvertToNurb1.png  style="width:400px;"> 
*Dieselben Objekte nach dem Konvertieren.*



## Anwendung

1.  Einen oder mehrere Skizzenbestandteile auswählen und die Schaltfläche **[<img src=images/Sketcher_BSplineApproximate.svg style="width:24px"> [Geometrie in B-Spline wandeln](Sketcher_BSplineApproximate.md)** drücken.

Eins der B-Spline-Werkzeuge [BSplineGrad](Sketcher_BSplineDegree/de.md), [BSplinePolygon](Sketcher_BSplinePolygon/de.md), [ BSplineKamm](Sketcher_BSplineComb/de.md), [BSplineKnotenVielfachheit](Sketcher_BSplineKnotMultiplicity/de.md) oder [BSplinePolGewicht](Sketcher_BSplinePoleWeight/de.md) sollte sichtbar sein, andernfalls sähe es so aus, als würde nichts passieren. Werden gerade Linien umgewandelt, muss als erstes ein [BSplineGradErhöhen](Sketcher_BSplineIncreaseDegree.md) der Linien erfolgen, um sie \"biegsam\" zu machen.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineApproximate/de
