---
- GuiCommand   */de
   Name   *Assembly3 ConstraintPointInPlane
   Name/de   *Assembly3 PunktAufEbene
   Icon   *Assembly_ConstraintPointInPlane.svg
   Workbenches   *[Assembly3](Assembly3_Workbench/de.md)
---

# Assembly3 ConstraintPointInPlane/de

## Beschreibung

Dieses Werkzeug stellt eine Verbindung zwischen zwei Objekten eines Zusammenbaus her und fixiert den Abstand zwischen ihnen sowie ihre Ausrichtung zueinander. Die Gewählten Elemente beider Objekte oder präziser ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein Objekt zum anderen zu positionieren.

Davon ausgehend, dass das ein Objekt bereits mittels <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width   *24px;"> [Festsetzen](Assembly3_ConstraintLock/de.md) unbeweglich gemacht wurde, wird das zweite Objekt auf eine Position bewegt, wo der Ursprung des Punktobjekts auf der X-Y-Ebene des Ebenenobjekts liegt.

Punktelemente haben keine Ausdehnung egal in welcher Richtung (Länge ist Null) und daher kann auch keine Orientierung ermittelt werden, d.h. dass ihre LKS nur für weitere Elementparameter benötigt werden. Die Ausrichtung der LKS bleibt immer die gleiche, wie die des globalen Koordinatensystems und kann nicht dazu genutzt werden, die Anzahl von Freiheitsgraden im Zusammenhang mit Drehungen zu reduzieren.

Im Bezug auf das Ebenenobjekt, kann sich das Punktobjekte noch entlang der X- und Y-Achsen und um den Ursprung herum (um alle drei Achsen) bewegen. Dies lässt für jede einzelne Verbindung fünf Freiheitsgrade unbestimmt.

## Anwendung

1.  Zwei Objekte in einen Zusammenbau einfügen.
2.  Ein Punktelement des einen und ein ebenes Flächenelement des anderen Objekts auswählen.
3.  Schaltfläche**<img src="images/Assembly_ConstraintPointInPlane.svg" width=16px> [Punkt auf Ebene](Assembly3_ConstraintPointInPlane/de.md)** drücken.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintPointInPlane/de
