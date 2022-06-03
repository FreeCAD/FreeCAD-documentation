---
- GuiCommand   */de
   Name   *Sketcher CreateEllipseByCenter
   Name/de   *Skizzierer EllipseDurchMittelpunktErstellen
   MenuLocation   *Sketch → Skizzengeometrien → Ellipse um Mittelpunkt erstellen
   Workbenches   *[Sketcher](Sketcher_Workbench/de.md)
   Shortcut   ***G** **E** **E**
   Version   *0.15
   SeeAlso   *[Sketcher EllipseDurch3PunkteErstellen](Sketcher_CreateEllipseBy3Points/de.md), [Sketcher KreisErstellen](Sketcher_CreateCircle/de.md), [Sketcher EllipsenbogenErstellen](Sketcher_CreateArcOfEllipse/de.md)
---

# Sketcher CreateEllipseByCenter/de

## Beschreibung

Dieses Werkzeug zeichnet eine Ellipse, indem drei Punkte ausgewählt werden   * der Mittelpunkt, das Ende des großen Radius und der kleine Radius. Wenn du das Werkzeug startest, ändert sich der Mauszeiger in ein weißes Kreuz mit einem roten Ellipsensymbol. Daneben werden die Koordinaten in Echtzeit angezeigt.

<img alt="" src=images/Sketcher_EllipseExample1.png‎  style="width   *500px;">



*|Die Reihenfolge der Klicks wird durch gelbe Pfeile mit Zahlen angezeigt. C ist das Zentrum, a - großer Durchmesser, b - kleiner Durchmesser, F1, F2 sind Foci.*

## Anwendung

-   Rufen den Befehl auf, indem du auf eine Schaltfläche in der Wekzeugleiste klickst, den Menüeintrag auswählst oder ein Tastaturkürzel verwenden (muss zuerst unter [Oberflächenanpassung](Interface_Customization/de.md) zugewiesen werden).
-   Klicke zuerst in die 3D Ansicht, um den Mittelpunkt der Ellipse festzulegen. Der zweite Klick legt den ersten Radius und die Ausrichtung der Ellipse fest. Dritter Klick legt den anderen Radius fest (der Abstand von der durch die ersten beiden Klicks definierten Linie ist der zweite Radius).
-   Nach dem dritten Klick wird die Ellipse zusammen mit einer darauf ausgerichteten Konstruktionsgeometrie erstellt (großer Durchmesser, kleiner Durchmesser, zwei Brennpunkte). Die Konstruktionsgeometrie kann manuell gelöscht werden, wenn sie nicht benötigt wird, und später wieder erstellt werden. Siehe [Interne Ausrichtungsbeschränkung](Sketcher_ConstrainInternalAlignment/de.md) und [Skizzierer Anzeigen Ausblenden Interne Geometrie](Sketcher_RestoreInternalAlignmentGeometry/de.md).
-   Drücken von **ESC** oder Klicken der rechten Maustaste bricht die Funktion ab.

## Besonderheiten

-   Haupt- und Nebenachsen von Ellipsen sind strikt und können nicht durch Größenänderung der Ellipse vertauscht werden. Dies ist eine Folge der verwendeten Löserparametrisierung (Zentrum (x,y), Fokus1 (x,y) und kleinster Radiuslänge (b)) und des ebenso strikten Verhaltens von OpenCascade. Die Ellipse muss gedreht werden, um die Achsen zu vertauschen.
-   Die Ellipse kann als Kreis funktionieren, wenn ihre Haupt- und Nebendurchmesserlinien gelöscht werden und einer der Brennpunkte auf den Mittelpunkt beschränkt wird. Aber die Radiusbeschränkung funktioniert bei einem solchen Kreis nicht.
-   Das Verschieben der Ellipse um eine Kante ist dasselbe wie das Verschieben des Ellipsenmittelpunkts.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseByCenter/de
