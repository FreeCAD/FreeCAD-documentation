---
- GuiCommand:/de
   Name:Sketcher CreateArcOfEllipse
   Name/de:Skizzierer ErstelleEllipsenBogen

   MenuLocation:Skizze → Skizzengeometrien → Erstellen eines Ellipsenbogens
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Version:0.15
   SeeAlso:[Skizzierer Ellipse durch Mittelpunkt](Sketcher_CreateEllipseByCenter/de.md), [Skizzierer Bogen](Sketcher_CompCreateArc/de.md)
---

# Sketcher CreateArcOfEllipse/de

## Beschreibung

Dieses Werkzeug zeichnet einen Ellipsenbogen, indem vier Punkte ausgewählt werden: der Mittelpunkt, das Ende des großen Radius, der Startpunkt und der Endpunkt. Wenn das Werkzeug gestartet wird, ändert sich der Mauszeiger in ein weißes Kreuz mit einem roten Ellipsenbogensymbol. Daneben werden die Koordinaten in Echtzeit angezeigt.

<img alt="" src=images/Sketcher_ArcOfEllipseExample1.png‎  style="width:500px;"> 
*Die Reihenfolge der Klicks wird durch gelbe Pfeile mit Nummern angezeigt. C ist das Zentrum, a - großer Durchmesser, b - kleiner Durchmesser, F1, F2 sind Brennpunkte.*

## Anwendung

-   Drücke die **<img src=images/Sketcher_CreateArcOfEllipse.svg style="width:16px"> [Ellipsenbogen](Sketcher_CreateArcOfEllipse/de.md)** Schaltfläche.
-   Erster Klick in der 3D Ansicht setzt den Mittelpunkt der Ellipse. Zweiter Klick legt den ersten Radius und die Ausrichtung der Ellipse fest. Der dritte Klick legt den zweiten Radius und den Beginn des Bogens fest. Der vierte Klick legt das Ende des Bogens fest.
-   Nach dem vierten Klick wird der Ellipsenbogen zusammen mit einer darauf ausgerichteten Konstruktionsgeometrie (großer Durchmesser, kleiner Durchmesser, zwei Brennpunkte) erzeugt. Die Konstruktionsgeometrie kann manuell gelöscht werden, wenn sie nicht benötigt wird, und später neu erstellt werden. Siehe [Interne Ausrichtungsbeschränkung](Sketcher_ConstrainInternalAlignment/de.md) und [Skizzierer Zeige/ Blende Interne Geometrie aus](Sketcher_RestoreInternalAlignmentGeometry/de.md).
-   Drücken von **ESC** oder Klicken der rechten Maustaste bricht die Funktion ab.

## Besonderheiten

-   Haupt- und Nebenachsen der zugrundeliegenden Ellipse sind streng und können nicht durch Größenänderung vertauscht werden. Die zugrunde liegende Ellipse muss gedreht werden, um die Achsen zu vertauschen.
-   Im Gegensatz zur Ellipse, die zu einem Kreis gezwungen werden kann, kann der Ellipsenbogen keinen Kreisbogen darstellen.
-   Das Verschieben des Ellipsenbogens per Kante ist dasselbe wie das Verschieben des Ellipsenmittelpunkts.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfEllipse/de
