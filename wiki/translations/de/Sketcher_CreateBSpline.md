---
- GuiCommand   */de
   Name   *Sketcher CreateBSpline
   Name/de   *Sketcher B-SplineErstellen
   MenuLocation   *Sketch → Skizzengeometrien → B-Spline erstellen
   Workbenches   *[Sketcher](Sketcher_Workbench/de.md)
   Shortcut   ***G** **B** **B**
   Version   *0.17
   SeeAlso   *[Sketcher GeschlossenenB-SplineErstellen](Sketcher_CreatePeriodicBSpline/de.md)
---

# Sketcher CreateBSpline/de

## Beschreibung

Dieses Werkzeug erstellt eine offene B-Spline-Kurve aus ihren Kontrollpunkten. (Siehe [diese Seite](B-Splines/de.md) für weitere Informationen über B-Splines).

![](images/Sketcher_B-spline_example01.png ) 
*Eine B-Spline-Kurve (in weiß), definiert durch 4 Kontrollpunkte. Abgebildet sind das Kontrollpolygon in Grün (die Geraden, die die Kontrollpunkte verbinden) und die Gewichtskreise in Dunkelgelb. Die grüne Ziffer "3" in der Mitte bezieht sich auf den [Grad](Sketcher_BSplineIncreaseDegree/de#Beschreibung.md) des B-Splines und die Ziffern "(4)" an den Endpunkten des B-Splines beziehen sich auf deren [Knotenvielfachheit](Sketcher_BSplineDecreaseKnotMultiplicity/de#Beschreibung.md). Die rote Ziffer "3" steht für das Kontrollpunktgewicht, das über die Radiusbedingung am Kontrollpunktkreis definiert ist.*

## Anwendung

1.  Die Schaltfläche **[<img src=images/Sketcher_CreateBSpline.svg style="width   *16px"> [B-spline erstellen](Sketcher_CreateBSpline/de.md)** drücken.
2.  Eine Reihe von Punkten durch Klicken in der [3D-Ansicht](3D_view.md) auswählen. Während der Befehl aktiv ist, werden die erstellten Punkte mit geraden Linien verbunden und um jeden Punkt ein Konstruktionskreis erstellt.
3.  Wahlweise kann **D** gedrückt werden, bevor die Eingabe beendet wird, um den Grad der B-Spline-Kurve festzulegen. {{Version/de|0.20}}
4.  Wahlweise kann **Backspace** (\<-) gedrückt werden, bevor die Eingabe beendet wird, um den zuletzt erstellten Kontrollpunkt zu löschen. {{Version/de|0.20}}
5.  Ein Rechtsklick beendet die Eingabe und generiert die Kurve.
6.  Abhängig von den Voreinstellungen könnte das Werkzeug aktiv bleiben, um eine neue Kurve zu zeichnen. Erneut mit der rechten Maustaste klicken, um den Befehl zu verlassen.

-   Es ist möglich, die Gewichte der Kontrollpunkte festzulegen, indem die Radien der Gewichtskreise geändert werden. Die Gleichheitsbedingungen der Kreise müssen zuerst gelöscht werden. Die Randbedingung Radius ist frei wählbar, das Gewicht der Kontrollpunkte wird durch die relativen Radien der Kreise definiert. Es funktioniert ähnlich wie die Schwerkraft   * Je größer ein Kreis im Verhältnis zu den anderen ist, desto stärker wird die Kurve vom Kontrollpunkt angezogen.
-   Die Sichtbarkeit des Kontrollpolygons, des Krümmungskamms, des Grades und die Knotenvielfachheit können über die Werkzeugleiste [B-Spline-Werkzeuge](Sketcher_Workbench/de#Sketcher-B-Spline-Werkzeuge.md) ein- oder ausgeschaltet werden.
-   Siehe auch die anderen Werkzeuge in der Werkzeugleiste [B-Spline-Werkzeuge](Sketcher_Workbench/de#Sketcher-B-Spline-Werkzeuge.md) für weitere Bearbeitungswerkzeuge.

## Begrenzungen

-   Viele Arten von Randbedingungen werden derzeit nicht unterstützt. Nur die Kontroll- und Endpunkte des B-Splines können festgelegt werden.
-   Die Werkzeuge [Teilen](Sketcher_Split/de.md) und [Verlängern](Sketcher_Extend/de.md) werden nicht unterstützt.
-   Die Form einer B-Spline-Kurve kann nur durch Bewegen (eines) der Kontrollpunkte bearbeitet werden. Die auf der Kurve liegenden Knoten können nicht ausgewählt werden.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateBSpline/de
