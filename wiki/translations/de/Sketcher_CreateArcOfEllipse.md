---
- GuiCommand:/de
   Name:Sketcher CreateArcOfEllipse
   Name/de:Sketcher EllipsenbogenErstellen
   MenuLocation:Sketch → Skizzengeometrien → Ellipsenbogen erstellen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**G** **E** **A**
   Version:0.15
   SeeAlso:[Sketcher EllipseDurchMittelpunktErstellen](Sketcher_CreateEllipseByCenter/de.md), [Sketcher AuswahlBogenErstellen](Sketcher_CompCreateArc/de.md)
---

# Sketcher CreateArcOfEllipse/de



## Beschreibung

Dieses Werkzeug zeichnet einen Ellipsenbogen, indem vier Punkte ausgewählt werden: der Mittelpunkt, das Ende des großen Radius (Scheitelpunkt), der Startpunkt und der Endpunkt. Wenn das Werkzeug gestartet wird, ändert sich der Mauszeiger in ein weißes Kreuz mit einem roten Ellipsenbogensymbol. Daneben werden die Koordinaten in Echtzeit angezeigt.

<img alt="" src=images/Sketcher_ArcOfEllipseExample1.png‎  style="width:500px;"> 
*Die Reihenfolge der Klicks wird durch gelbe Pfeile mit Zahlen angezeigt.<br> C ist das Zentrum, a der große Durchmesser, b der kleine Durchmesser, F1 und F2 sind Brennpunkte.*



## Anwendung

-   Die Schaltfläche **[<img src=images/Sketcher_CreateArcOfEllipse.svg style="width:16px"> [Ellipsenbogen erstellen](Sketcher_CreateArcOfEllipse/de.md)** drücken.
-   Der erster Klick in die 3D-Ansicht setzt den Mittelpunkt der Ellipse. Der zweite Klick legt den Scheitelpunkt (erster Radius) und die Ausrichtung der Ellipse fest. Der dritte Klick legt den zweiten Radius und den Beginn des Bogens fest. Der vierte Klick legt das Ende des Bogens fest.
-   Nach dem vierten Klick wird der Ellipsenbogen zusammen mit darauf ausgerichteter Konstruktionsgeometrie erstellt (großer Durchmesser, kleiner Durchmesser, zwei Brennpunkte). Die Konstruktionsgeometrie kann manuell gelöscht werden, wenn sie nicht benötigt wird, und später neu erstellt werden. Siehe [InterneAusrichtungFestlegen](Sketcher_ConstrainInternalAlignment/de.md) und [InterneAusrichtungsgeometrieWiederherstellen](Sketcher_RestoreInternalAlignmentGeometry/de.md).
-   Das Drücken von **ESC** oder Klicken mit der rechten Maustaste bricht die Funktion ab.



## Besonderheiten

-   Haupt- und Nebenachsen der zugrundeliegenden Ellipse sind genau festgelegt und können nicht durch Größenänderung vertauscht werden. Die zugrundeliegende Ellipse muss gedreht werden, um die Achsen zu tauschen.
-   Im Gegensatz zur Ellipse, die durch geeignete Randbedingungen zu einem Kreis geformt werden kann, kann der Ellipsenbogen keinen Kreisbogen darstellen.
-   Das Verschieben des Ellipsenbogens durch Verschieben einer Kante ist dasselbe wie das Verschieben des Ellipsenmittelpunkts.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfEllipse/de
