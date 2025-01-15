---
 GuiCommand:
   Name: Sketcher BSplineApproximate
   Name/de: Sketcher BSplineUmwandelnInNURBS
   MenuLocation: Skizze , B-Spline-Werkzeuge , Geometrie in B-Spline konvertieren
   Workbenches: Sketcher_Workbench/de
   Version: 0.17
   SeeAlso: Sketcher_CreateBSpline/de
---

# Sketcher BSplineConvertToNURBS/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_BSplineConvertToNURBS.svg  style="width:24px;"> [Sketcher BSplineUmwandelnInNURBS](Sketcher_BSplineConvertToNURBS/de.md) wandelt Kanten in [B-Splines](B-Splines/de.md).

<img alt="" src=images/sketcher_BSplineConvertToNurb.png  style="width:300px;"> 
*Verschiedene Objekte vor dem Konvertieren.*

<img alt="" src=images/sketcher_BSplineConvertToNurb1.png  style="width:300px;"> 
*Dieselben Objekte nach dem Konvertieren.*



## Anwendung

1.  Eine oder mehrere Kanten auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **[<img src=images/Sketcher_BSplineConvertToNURBS.svg style="width:16px"> [Geometrie in B-Spline konvertieren](Sketcher_BSplineConvertToNURBS/de.md)** drücken.
    -   Den Menüeintrag **Skizze → B-Spline-Werkzeuge → <img src="images/Sketcher_BSplineConvertToNURBS.svg" width=16px> Geometrie in B-Spline konvertieren** auswählen.
3.  Die Kanten werden umgewandelt.



## Hinweise

-   Sicherstellen, dass [BSplineGrad](Sketcher_BSplineDegree/de.md), [BSplinePolygon](Sketcher_BSplinePolygon/de.md), [BSplineKamm](Sketcher_BSplineComb/de.md), [BSplineKnotenVielfachheit](Sketcher_BSplineKnotMultiplicity/de.md) und/oder [BSplinePolGewicht](Sketcher_BSplinePoleWeight/de.md) sichtbar sind, andernfalls wird scheinbar nichts passieren.
-   Wurden gerade Linien umgewandelt, muss der [B-Spline-Grad erhöht](Sketcher_BSplineIncreaseDegree/de.md) werden, um sie \"biegsam\" zu machen.
-   Das Werkzeug entfernt nicht die interne Geometrie von [Kegelschnitten](Sketcher_Workbench/de#Sketcher_CompCreateConic.md). Dies muss von Hand erfolgen.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineConvertToNURBS/de
