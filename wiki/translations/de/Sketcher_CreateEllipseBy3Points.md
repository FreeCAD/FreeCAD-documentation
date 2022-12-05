---
- GuiCommand:/de
   Name:Sketcher CreateEllipseBy3Points
   Name/de:Sketcher EllipseDurch3PunkteErstellen
   MenuLocation:Sketch → Skizzengeometrien → Ellipse durch 3 Punkte erstellen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**G** **3** **E**
   Version:0.15
   SeeAlso:[Sketcher EllipseDurchMittelpunktErstellen](Sketcher_CreateEllipseByCenter/de.md), [Sketcher KreisErstellen](Sketcher_CreateCircle/de.md), [Sketcher EllipsenbogenErstellen](Sketcher_CreateArcOfEllipse/de.md)
---

# Sketcher CreateEllipseBy3Points/de

## Beschreibung

Dieses Werkzeug zeichnet eine Ellipse, indem drei Punkte ausgewählt werden: (1) die Periapsis (erste Kreuzung des Hauptdurchmessers mit der Ellipse), (2) die Apoapsis (zweite Kreuzung des Hauptdurchmessers mit der Ellipse), (3) ein Punkt auf einer Seite neben dem längeren Durchmesser (a), der den kleineren Radius (b) definiert. (c) ist der resultierende Mittelpunkt und (f) sind die Brennpunkte.

Wenn das Werkzeug gestartet wird, ändert sich der Mauszeiger in ein weißes Kreuz mit einem roten Ellipsensymbol.

![](images/Ellipse_3Point.png‎ )



*Die Reihenfolge der Klicks wird durch gelbe Pfeile mit Zahlen angezeigt. 1 ist die Periapsis, 2 ist die Apoapsis, 3 ist der Punkt, der den kleine Durchmesser festlegt, grüne Linien sind größere und kleinere Durchmesser. Blaue Linien sind zufällige Konstruktionslinien nur zur Veranschaulichung.*

## Anwendung

-   Die Schaltfläche **[<img src=images/Sketcher_CreateEllipseBy3Points.svg style="width:16px"> [Ellipse durch 3 Punkte erstellen](Sketcher_CreateEllipseBy3Points/de.md)** drücken.
-   Der erste Klick in die 3D-Ansicht setzt einen Scheitelpunkt, der den Schnittpunkt des Hauptdurchmessers mit der Ellipse (Periapsis) definiert. Der zweite Klick in die 3D-Ansicht legt den gegenüberliegenden Scheitelpunkt fest, die Kreuzung des Hauptdurchmessers mit der Ellipse auf der gegenüberligenden Seite des Mittelpunktes (Apoapsis). Der dritte Klick legt einen Punkt auf der Ellipse fest, der den Nebenradius definiert.

-   Nach dem dritten Klick wird die Ellipse zusammen mit darauf ausgerichteter Konstruktionsgeometrie erstellt (großer Durchmesser, kleiner Durchmesser, zwei Brennpunkte). Die Konstruktionsgeometrie kann manuell gelöscht werden, wenn sie nicht benötigt wird, und später wiederhergestellt werden. Siehe [InterneAusrichtungFestlegen](Sketcher_ConstrainInternalAlignment/de.md) und [InterneAusrichtungsgeometrieWiederherstellen](Sketcher_RestoreInternalAlignmentGeometry/de.md).
-   Das Drücken von **ESC** oder Klicken mit der rechten Maustaste bricht die Funktion ab.

## Besonderheiten

-   Haupt- und Nebenachsen von Ellipsen sind streng festgelegt und können nicht durch Größenänderung der Ellipse vertauscht werden. Dies ist eine Folge der verwendeten Löserparametrisierung (Zentrum (x,y), Fokus1 (x,y) und Länge des kleinen Radius (b)) und des gleichen strengen Verhaltens von OpenCascade. Die Ellipse muss gedreht werden, um die Achsen zu vertauschen.
-   Die Ellipse kann als Kreis fungieren, wenn ihre Haupt- und Nebenradiuslinien gelöscht werden und einer der Brennpunkte mit dem Mittelpunkt zusammenfallend festgelegt wird. Die Randbedingung RadiusFestlegen funktioniert jedoch nicht bei einem solchen Kreis.
-   Das Verschieben der Ellipse durch die Kante ist dasselbe wie das Verschieben des Ellipsenmittelpunkts.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseBy3Points/de
