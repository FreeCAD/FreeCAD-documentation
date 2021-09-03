---
- GuiCommand:/de
   Name:Sketcher CreatePeriodicBSpline
   Name/de:Skizzierer ErstellePeriodischenBSpline
   MenuLocation: Skizze → Skizzierergeometrien → Erstelle periodischen B-spline
   Workbenches: [Skizzierer](Sketcher_Workbench/de.md)
   Version:0.17
   SeeAlso:[Skizzierer B-spline](Sketcher_CreateBSpline/de.md)
---

## Beschreibung


<div class="mw-translate-fuzzy">

Dieses Werkzeug zeichnet von seinen Kontrollpunkten aus eine periodische (geschlossene) B-Spline Kurve auf.


</div>

![](images/Sketcher_Periodic_B-spline_example01.png )


*Eine periodische B-Spline-Kurve (in Weiß) aus 5 Punkten erstellt. Abgebildet sind das Kontrollpolygon in grün (die Geraden verbinden die roten Punkte), die Gewichtskreise in blau und der Krümmungskamm in grün. Die (3) Ziffer in der Mitte bezieht sich auf den Grad des B-Splines, und die (1) und (2) Ziffern auf den Knoten, die auf der Kurve liegen, beziehen sich auf deren Vielzahl.*

## Anwendung

1.  Press the **<img src=images/Sketcher_CreatePeriodicBSpline.svg style="width:16px"> [Periodic B-spline](Sketcher_CreatePeriodicBSpline.md)** button.
2.  Create a series of points by clicking in the 3D view. While the command is active, the created points are connected with straight lines, and a construction circle is created centred on each point.
3.  Pick the first curve point, or right-click to terminate the input and generate the curve.
4.  Depending on preferences, the tool may remain active to trace a new curve. Right-click again to exit the command.

-   It is possible to define the weight of the control points by changing the radii of the weight circles. The equality constraints on the circles need to be deleted first. The radius constraint is arbitrary, the weight of the control points will be defined by the relative radii of the circles. It works similar to gravity: the bigger a circle is in relation to the others, the more the curve will be attracted to the control point.
-   The visibility of the control polygon, the curvature comb, the degree and the knot multiplicity can be toggled on/off from the [B-spline tools](Sketcher_Workbench#Sketcher_B-spline_tools.md) toolbar.
-   Check out the other tools in the [B-spline tools](Sketcher_Workbench#Sketcher_B-spline_tools.md) toolbar for more B-spline editing tools.

## Begrenzungen

-   Viele Arten von Beschränkungen werden derzeit nicht unterstützt. Nur der Kontrollpunkt und die Endpunkte des B-Splines können beschränkt werden.
-   [Stutzen](Sketcher_Trimming/de.md) und [Erweitern](Sketcher_Extend/de.md) Werkzeuge werden nicht unterstützt.
-   Die Form einer B-Splinekurve kann nur durch Ziehen eines der Kontrollpunkte bearbeitet werden. Die auf der Kurve liegenden Knoten können nicht ausgewählt werden.





{{Sketcher Tools navi

}}  
