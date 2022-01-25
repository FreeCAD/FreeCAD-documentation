---
- GuiCommand:/de
   Name:Sketcher CreateEllipseBy3Points
   Name/de:Skizzierer EllipseDurch3Punkte
   MenuLocation:Sketch → Skizzengeometrien → Erstellen einer Ellipse durch 3 Punkte
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Version:0.15
   SeeAlso:[Skizzierer Ellipse durch Zentrum](Sketcher_CreateEllipseByCenter/de.md), [Skizzierer Kreis](Sketcher_CreateCircle/de.md), [Sketcher Ellipsenbogen](Sketcher_CreateArcOfEllipse/de.md)
---

# Sketcher CreateEllipseBy3Points/de

## Beschreibung

Dieses Werkzeug zeichnet eine Ellipse, indem drei Punkte ausgewählt werden: (1) die Periapsis (erste Kreuzung des längeren Durchmessers mit der Ellipse), (2) die Apoapsis (zweite Kreuzung des längeren Durchmessers mit der Ellipse), (3) ein Punkt auf einer Seite des längeren Durchmessers (a), der den kleineren Radius (b) definiert. (c) ist das resultierende Zentrum und (f) sind die Brennpunkte.

Wenn das Werkzeug gestartet wird, ändert sich der Mauszeiger in ein weißes Kreuz mit einem roten Ellipsensymbol.

![](images/Ellipse_3Point.png‎ )



*Die Reihenfolge der Klicks wird durch gelbe Pfeile mit Zahlen angezeigt. 1 ist die Periapsis, 2 ist die Apoapsis, 3 ist der Definitionspunkt für kleinere Durchmesser, grüne Linien sind größere und kleinere Durchmesser. Blaue Linien sind zufällige Konstruktionslinien nur zur Veranschaulichung.*

## Anwendung

-   Drücke die **[<img src=images/Sketcher_CreateEllipseBy3Points.svg style="width:16px"> [Ellipse durch 3 Punkte](Sketcher_CreateEllipseBy3Points/de.md)** Schaltfläche .
-   Der erste Klick in der 3D Ansicht setzt einen Punkt, der den Schnittpunkt des Hauptdurchmessers mit der Ellipse (Periapsis) definiert. Der zweite Klick in der 3D Ansicht legt einen Punkt fest, der die Kreuzung des Hauptdurchmessers mit der Ellipse gegenüber dem Mittelpunkt (Apoapsis) definiert. Dritter Klick legt einen Punkt auf der Ellipse fest, der den Nebenradius definiert.

-   Nach dem dritten Klick wird die Ellipse zusammen mit einer darauf ausgerichteten Konstruktionsgeometrie erstellt (Hauptdurchmesser, kleiner Durchmesser, zwei Brennpunkte). Die Konstruktionsgeometrie kann, falls nicht benötigt, manuell gelöscht und später wieder erstellt werden. Siehe [Interne Ausrichtungsbeschränkung](Sketcher_ConstrainInternalAlignment/de.md) und [Sketcher Innengeometrie einblenden ausblenden](Sketcher_RestoreInternalAlignmentGeometry/de.md).
-   Drücken von **ESC** oder Klicken der rechten Maustaste bricht die Funktion ab.

## Besonderheiten

-   Haupt- und Nebenachsen von Ellipsen sind streng und können nicht durch Größenänderung der Ellipse vertauscht werden. Dies ist eine Folge der verwendeten Löserparametrisierung (Zentrum (x,y), Fokus1 (x,y) und Länge des kleinen Radius (b)) und des gleichen strengen Verhaltens von OpenCascade. Die Ellipse muss gedreht werden, um die Achsen zu vertauschen.
-   Die Ellipse kann als Kreis fungieren, wenn ihre Linien mit Haupt- und Nebenradius gelöscht werden und einer der Brennpunkte gezwungen ist, mit dem Mittelpunkt zusammenzufallen. Die Radiusbeschränkung funktioniert jedoch nicht bei einem solchen Kreis.
-   Das Verschieben der Ellipse durch die Kante ist dasselbe wie das Verschieben des Ellipsenmittelpunkts.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseBy3Points/de
