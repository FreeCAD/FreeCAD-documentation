---
- GuiCommand:/de
   Name:Sketcher CreatePeriodicBSpline
   Name/de:Skizzierer ErstellePeriodischenBSpline
   MenuLocation: Skizze → Skizzierergeometrien → Erstelle periodischen B-spline
   Workbenches: [Skizzierer](Sketcher_Workbench/de.md)
   Version:0.17
   SeeAlso:[Skizzierer B-spline](Sketcher_CreateBSpline/de.md)
---

# Sketcher CreatePeriodicBSpline/de


</div>

## Beschreibung

Dieses Werkzeug zeichnet von seinen Kontrollpunkten aus eine periodische (geschlossene) B-Spline-Kurve auf. (Siehe [diese Seite](B-Splines/de.md) für mehr Informationen über B-Splines).

![](images/Sketcher_Periodic_B-spline_example01.png )



*Eine periodische B-Spline-Kurve (in Weiß) aus 5 Punkten erstellt. Abgebildet sind das Kontrollpolygon in grün (die Geraden verbinden die roten Punkte), die Gewichtskreise in blau und der Krümmungskamm in grün. Die (3) Ziffer in der Mitte bezieht sich auf den Grad des B-Splines, und die (1) und (2) Ziffern auf den Knoten, die auf der Kurve liegen, beziehen sich auf deren Vielzahl.*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Drücke die **[<img src=images/Sketcher_CreatePeriodicBSpline.svg style="width:16px"> [Erstellen von periodischer B-Spline](Sketcher_CreatePeriodicBSpline/de.md)**-Schaltfläche.
2.  Erstelle eine Reihe von Punkte durch Klicken in der 3D-Ansicht. Während der Befehl aktiv ist, werden die erstellten Punkte durch gerade Linien verbunden und um jeden Punkt ein Konstruktionskreis erstellt.
3.  Wähle den ersten Kurvenpunkt oder rechtsklicke, um die Eingabe zu beenden und die Kurve zu generieren.
4.  Abhängig von den Voreinstellungen könnte das Werkzeug aktiv bleiben, um eine neue Kurve zu zeichnen. Rechtsklicke erneut, um den Befehl zu verlassen.

-   Es ist möglich, die Gewichtung der Kontrollpunkte zu definieren, indem die Radien der Gewichtskreise geändert werden. Die Gleichheitsbeschränkungen der Kreise müssen zuerst gelöscht werden. Die Radiusbeschränkung ist frei wählbar, das Gewicht der Kontrollpunkte wird durch die relativen Radien der Kreise definiert. Es funktioniert ähnlich wie Schwerkraft: je größer die Kreise im Vergleich zu anderen sind, um so mehr wird die Kurve vom Kontrollpunkt angezogen.
-   Die Sichtbarkeit des Kontrollpolygons, des Krümmungskamms, der Grad und die Knotenvielzahl können über die [B-Spline Werkzeuge](Sketcher_Workbench/de#Sketcher_B-spline_tools.md)-Werkzeugleiste ein-/ausgeschaltet werden.
-   Wirf einen Blick auf die anderen Werkzeuge in der [B-Spline Werkzeuge](Sketcher_Workbench/de#Sketcher_B-spline_tools.md)-Werkzeugleiste.


</div>

## Begrenzungen

-   Viele Arten von Beschränkungen werden derzeit nicht unterstützt. Nur der Kontrollpunkt und die Endpunkte des B-Splines können beschränkt werden.
-   [Stutzen](Sketcher_Trimming/de.md) und [Erweitern](Sketcher_Extend/de.md) Werkzeuge werden nicht unterstützt.
-   Die Form einer B-Splinekurve kann nur durch Ziehen eines der Kontrollpunkte bearbeitet werden. Die auf der Kurve liegenden Knoten können nicht ausgewählt werden.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePeriodicBSpline/de
