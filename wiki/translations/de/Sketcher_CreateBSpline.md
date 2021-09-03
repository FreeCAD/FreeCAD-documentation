---
- GuiCommand:/de
   Name:Sketcher CreateBSpline
   Name/de:Skizzierer ErstelleBSpline
   MenuLocation: Skizze → Skizzierergeometrien → Erstelle B-spline
   Workbenches: [Skizzierer](Sketcher_Workbench/de.md)
   Version:0.17
   SeeAlso:[Skizzierer periodischer B-spline](Sketcher_CreatePeriodicBSpline/de.md)
---

## Beschreibung


<div class="mw-translate-fuzzy">

Dieses Werkzeug zeichnet von seinen Kontrollpunkten aus eine offene B-Splinekurve auf.


</div>

![](images/Sketcher_B-spline_example01.png )


<div class="mw-translate-fuzzy">


*Eine B-Splinekurve, die aus 4 Punkten (in Weiß) besteht. Dargestellt sind das Kontrollpolygon in grün (die Geraden verbinden die roten Punkte), die Gewichtskreise in blau und der Krümmungskamm in grün. Die (3) Ziffer in der Mitte bezieht sich auf den  
[Grad](Sketcher_BSplineIncreaseDegree/de#Beschreibung.md) der B-Splines, und die (4) Ziffern an den Enden der Kurve beziehen sich auf ihre 
[Knotenvielfalto](Sketcher_BSplineDecreaseKnotMultiplicity/de#Beschreibung.md).''*


</div>

## Anwendung


<div class="mw-translate-fuzzy">

1.  Drücke die **<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [Erzeuge  B-spline](Sketcher_CreateBSpline/de.md)** Taste.
2.  Erstelle eine Reihe von Punkten, durch anklicken in der 3D Ansicht. Während der Befehl aktiv ist, werden die erzeugten Punkte mit geraden Linien verbunden, und es wird ein Konstruktionskreis erstellt, der auf jeden Punkt zentriert ist.
3.  Klicke mit der rechten Maustaste, um die Eingabe zu beenden und die Kurve zu erzeugen.
4.  Abhängig von den Einstellungen kann das Werkzeug aktiv bleiben, um eine neue Kurve zu verfolgen. Klicke erneut mit der rechten Maustaste, um den Befehl zu beenden.

-   Es ist möglich, das Gewicht der Kontrollpunkte zu definieren, indem man die Radien der Gewichtskreise ändert. Die Gleichheitsbeschränkungen für die Kreise müssen zuerst gelöscht werden. Die Radiusbeschränkung ist willkürlich, das Gewicht der Kontrollpunkte wird durch die relativen Radien der Kreise definiert. Es funktioniert ähnlich wie die Schwerkraft: Je größer ein Kreis im Verhältnis zu den anderen ist, desto mehr wird die Kurve zum Kontrollpunkt gezogen.
-   Die Sichtbarkeit des Kontrollpolygons, des Krümmungskamms, des Grades und der Knotenvielfalt kann über die Symbolleiste [B-spline Werkzeuge](Sketcher_Workbench#Skizzierer_B-spline_Werkzeuge.md) ein- und ausgeschaltet werden.
-   Schaue Dir die anderen Werkzeuge in der Werkzeugleiste von [B-spline Werkzeuge](Sketcher_Workbench/de#Skizzierer_B-spline_Werkzeuge.md) an, für weitere B-spline Bearbeitungswerkzeuge.


</div>

## Begrenzungen

-   Viele Arten von Beschränkungen werden derzeit nicht unterstützt. Nur der Kontrollpunkt und die Endpunkte des B-Splines können beschränkt werden.
-   [Trimming](Sketcher_Trimming/de.md) und [extend](Sketcher_Extend/de.md) Werkzeuge werden nicht unterstützt.
-   Die Form einer B-Splinekurve kann nur durch Ziehen eines der Kontrollpunkte bearbeitet werden. Die auf der Kurve liegenden Knoten können nicht ausgewählt werden.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}  
