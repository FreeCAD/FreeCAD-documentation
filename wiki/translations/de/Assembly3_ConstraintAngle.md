---
- GuiCommand   */de
   Name   *Assembly3 ConstraintAngle
   Name/de   *Assembly3 WinkelFestlegen
   Icon   *Assembly_ConstraintAngle.svg
   Workbenches   *[Assembly3](Assembly3_Workbench/de.md)
---

# Assembly3 ConstraintAngle/de

## Beschreibung

Dieses Werkzeug stellt eine Verbindung zwischen zwei Objekten eines Zusammenbaus her und fixiert den Abstand zwischen ihnen sowie ihre Ausrichtung zueinander. Die Gewählten Elemente beider Objekte oder präziser ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein Objekt zum anderen zu positionieren.

Der Winkel zwischen zwei Elementen, d.h. der Winkel zwischen ihren Z-Achsen, wird festgelegt.

Der Abstand ihrer Ursprünge in X-, Y- und Z-Richtung und die Winkel zwischen ihren X-Achsen und Y-Achsen sind nicht festgelegt. Im Bezug auf das erste Element, können sich die weiteren Objekte noch in X-, Y- und Z-Richtung bewegen und um beide Z-Achsen drehen. Dies lässt für jede einzelne Verbindung fünf Freiheitsgrade unbestimmt.

Diese Beziehung akzeptiert gerade Kanten und ebene Flächen.

## Anwendung


<div class="mw-translate-fuzzy">

1.  Zwei oder mehr Objekte in einen Zusammenbau einfügen.
2.  Je ein ebenes Flächenelement oder eine gerade Kante pro Objekt auswählen.
3.  Schaltfläche**<img src="images/Assembly_ConstraintAngle.svg" width=16px> [WinkelFestlegen](Assembly3_ConstraintAngle/de.md)** drücken.


</div>

## Notes

2D   * This constraint seems to be the only way to control an angle in a skeleton sketch (2D kinematic assembly); Prove me wrong, PLEASE!

-   Its **Angle|Angle** property allows any positive value, but 0° and 180° exactly are puzzling the solver.
-   It flips direction if angles greater than 180° are used and as a result 135° and 225° give the same positions for the involved elements.

   *   It is useless if you want to simulate a full rotation and so ruins the principle of using a skeleton sketch for a lot of kinematic tasks such as driving a piston by a rotating crank coupled with a con-rod.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintAngle/de
