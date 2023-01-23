---
- GuiCommand:/de
   Name:Sketcher CreateEllipseByCenter
   Name/de:Skizzierer EllipseDurchMittelpunktErstellen
   MenuLocation:Sketch → Skizzengeometrien → Ellipse um Mittelpunkt erstellen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**G** **E** **E**
   Version:0.15
   SeeAlso:[Sketcher EllipseDurch3PunkteErstellen](Sketcher_CreateEllipseBy3Points/de.md), [Sketcher KreisErstellen](Sketcher_CreateCircle/de.md), [Sketcher EllipsenbogenErstellen](Sketcher_CreateArcOfEllipse/de.md)
---

# Sketcher CreateEllipseByCenter/de



## Beschreibung

Dieses Werkzeug zeichnet eine Ellipse, indem drei Punkte ausgewählt werden: der Mittelpunkt, das Ende des großen Radius und der kleine Radius. Wird das Werkzeug gestartet, ändert sich der Mauszeiger in ein weißes Kreuz mit einem roten Ellipsensymbol. Daneben werden die Koordinaten in Echtzeit angezeigt.

<img alt="" src=images/Sketcher_EllipseExample1.png‎  style="width:500px;"> 
*Die Reihenfolge der Klicks wird durch gelbe Pfeile mit Zahlen angezeigt.<br> C ist das Zentrum, a der große Durchmesser, b der kleine Durchmesser, F1 und F2 sind Brennpunkte.*



## Anwendung

-   Diesen Befehl aufrufen, indem auf die Schaltfläche in der Wekzeugleiste geklickt, der Menüeintrag ausgewählt oder ein Tastaturkürzel verwendet wird (muss zuerst unter [Anpassung der Oberfläche](Interface_Customization/de.md) zugewiesen werden).

-   Zuerst in die 3D-Ansicht klicken, um den Mittelpunkt der Ellipse festzulegen. Der zweite Klick legt den ersten Radius und die Ausrichtung der Ellipse fest. Der dritte Klick legt den anderen Radius fest (der Abstand von der durch die ersten beiden Klicks definierten Linie ist der zweite Radius).

-   Nach dem dritten Klick wird die Ellipse erstellt, zusammen mit einem Satz dazu ausgerichteter Konstruktionsgeometrie (großer Durchmesser, kleiner Durchmesser, zwei Brennpunkte). Die Konstruktionsgeometrie kann manuell gelöscht werden, wenn sie nicht benötigt wird, und später wiederhergestellt werden. Siehe [InterneAusrichtungFestlegen](Sketcher_ConstrainInternalAlignment/de.md) und [Sketcher InterneAusrichtungsgeometrieWiederherstellen](Sketcher_RestoreInternalAlignmentGeometry/de.md).

-    **ESC**oder die rechte Maustaste drücken bricht die Funktion ab.



## Besonderheiten

-   Haupt- und Nebenachsen von Ellipsen sind genau festgelegt und können nicht durch Größenänderung der Ellipse vertauscht werden. Dies ist eine Folge der verwendeten Löserparametrisierung (Zentrum (x,y), Brennpunkt1 (x,y) und Länge des kleinen Radius (b)) und des ebenso genau festgelegten Verhaltens von OpenCascade. Die Ellipse muss gedreht werden, um die Achsen zu tauschen.
-   Die Ellipse kann einen Kreis darstellen, wenn ihre Haupt- und Nebendurchmesserlinien gelöscht werden und einer der Brennpunkte mit der Randbedingung KoinzidentFestlegen auf den Mittelpunkt festgelegt wird. Aber die Randbedingung RadiusFestlegen funktioniert bei einem solchen Kreis nicht.
-   Das Bewegen der Ellipse durch Verschieben einer Kante ist dasselbe wie das Verschieben des Ellipsenmittelpunkts.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseByCenter/de
