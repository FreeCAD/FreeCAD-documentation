---
- GuiCommand:
   Name: Assembly3 ConstraintPerpendicular
   Name/de: Assembly3 RechtwinkligFestlegen
   Icon: Assembly_ConstraintPerpendicular.svg
   Workbenches: Assembly3_Workbench/de
---

# Assembly3 ConstraintPerpendicular/de

## Beschreibung

Dieses Werkzeug stellt eine Verbindung zwischen zwei Objekten eines Zusammenbaus her und fixiert den Abstand zwischen ihnen sowie ihre Ausrichtung zueinander. Die Gewählten Elemente beider Objekte oder präziser ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein Objekt zum anderen zu positionieren.

Davon ausgehend, dass das erste Objekt bereits mittels <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Festsetzen](Assembly3_ConstraintLock/de.md) unbeweglich gemacht wurde, wird das nächste Objekt auf eine Position bewegt, wo beide Z-Achsen rechtwinklig sind.

Der Abstand ihrer Ursprünge in X-, Y- und Z-Richtung und die Winkel zwischen ihren X-Achsen und Y-Achsen sind nicht festgelegt. Im Bezug auf das erste Element, kann sich das zweite Objekt noch in X-, Y- und Z-Richtung bewegen und um beide Z-Achsen drehen. Dies lässt für jede Verbindung fünf Freiheitsgrade unbestimmt.

Diese Beziehung akzeptiert gerade Kanten und ebene Flächen.

## Anwendung

1.  Zwei Objekte in einen Zusammenbau einfügen.
2.  Je eine gerade Kante oder ein ebenes Flächenelement pro Objekt auswählen.
3.  Schaltfläche**<img src="images/Assembly_ConstraintPerpendicular.svg" width=16px> [Rechtwinklig festlegen](Assembly3_ConstraintPerpendicular/de.md)** drücken.



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintPerpendicular/de
