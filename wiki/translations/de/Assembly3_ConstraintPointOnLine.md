---
- GuiCommand   */de
   Name   *Assembly3 ConstraintPointOnLine
   Name/de   *Assembly3 PunktAufLinie
   Icon   *Assembly_ConstraintPointOnLine.svg
   Workbenches   *[Assembly3](Assembly3_Workbench/de.md)
---

# Assembly3 ConstraintPointOnLine/de

## Beschreibung

Dieses Werkzeug stellt eine Verbindung zwischen zwei Objekten eines Zusammenbaus her und fixiert den Abstand zwischen ihnen sowie ihre Ausrichtung zueinander. Die Gewählten Elemente beider Objekte oder präziser ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein Objekt zum anderen zu positionieren.

Davon ausgehend, dass ein Objekt bereits mittels <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width   *24px;"> [Festsetzen](Assembly3_ConstraintLock/de.md) unbeweglich gemacht wurde, wird das zweite Objekt auf eine Position bewegt, wo der Ursprung des Punktelements auf der Z-Achse des Linienelements liegt.

Punktelemente haben keine Ausdehnung egal in welcher Richtung (Länge ist Null) und daher kann auch keine Orientierung ermittelt werden, d.h. dass ihre LKS nur für weitere Elementparameter benötigt werden. Die Ausrichtung der LKS bleibt immer die gleiche, wie die des globalen Koordinatensystems und kann nicht dazu genutzt werden, die Anzahl von Freiheitsgraden im Zusammenhang mit Drehungen zu reduzieren. Linienelementehaben einen Ursprung und eine Richtung, die durch die Z-Achse des LKS repräsentiert wird. Eine Richtung für die X- und Y-Achsen kann nicht ermittelt werden und daher kann die Drehung um die Z-Achse nicht zur Reduzierung der Freiheitsgrade genutzt werden. (Es funktioniert im Zusammenhang mit Punktelementen sowieso nicht)

Im Bezug auf das erste Element, kann sich das folgende Objekt noch entlang der Z-Achse bewegen und um den Ursprung herum drehen (um alle drei Achsen). Dies lässt für jede einzelne Verbindung vier Freiheitsgrade unbestimmt.

## Anwendung

1.  Zwei Objekte in einen Zusammenbau einfügen.
2.  Ein Punktelement des einen und ein gerades Kantenelement des anderen Objekts auswählen.
3.  Schaltfläche**<img src="images/Assembly_ConstraintPointOnLine.svg" width=16px> [Punkt auf Line](Assembly3_ConstraintPointOnLine/de.md)** drücken.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintPointOnLine/de
