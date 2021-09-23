---
- GuiCommand:/de
   Name:Assembly3 ConstraintPointOnCircle
   Name/de:Assembly3 PunktAufKreis
   Icon:Assembly_ConstraintPointOnCircle.svg
   Workbenches:[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintPointOnCircle/de

## Beschreibung

Dieses Werkzeug verbindet zwei oder mehr Objekte eines Zusammenbaus und gleicht ihre Ausrichtungen an. Die gewählten Elemente der einzelnen Objekte oder präziser ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein oder mehrere Objekte im Verhältnis zu einem anderen Objekt zu positionieren.

Davon ausgehend, dass ein Objekt bereits mittels <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Festsetzen](Assembly3_ConstraintLock/de.md) unbeweglich gemacht wurde, wird das zweite Objekt auf eine Position bewegt, wo der Ursprung des Punktobjekts auf der X-Y-Ebene des Kreisobjekts liegt und die Z-Achsen parallel zueinander ausgerichtet sind (zusammengehörige X und Y werte, die vom Radius abhängen).

Punktelemente haben keine Ausdehnung egal in welcher Richtung (Länge ist Null) und daher kann auch keine Orientierung ermittelt werden, d.h. dass ihre LKS nur für weitere Elementparameter benötigt werden. Die Ausrichtung der LKS bleibt immer die gleiche, wie die des globalen Koordinatensystems und kann nicht dazu genutzt werden, die Anzahl von Freiheitsgraden im Zusammenhang mit Drehungen zu reduzieren.

Die Position auf dem Kreisobjekt (Bogenlänge vom Startpunkt) ist nicht festgelgt. Im Bezug auf das erste Objekt, kann sich das nächste noch entlang der X- und Y-Achsen und um den Ursprung herum (um alle drei Achsen) bewegen. Dies lässt für jede einzelne Verbindung vier Freiheitsgrade unbestimmt.

## Anwendung

1.  Zwei Objekte in einen Zusammenbau einfügen.
2.  Ein Punktelement des einen und ein kreisförmiges Flächen- oder Kantenelement des anderen Objekts auswählen.
3.  Schaltfläche **<img src="images/Assembly_ConstraintPointOnCircle.svg" width=16px> [Punkt auf Kreis](Assembly3_ConstraintPointOnCircle/de.md)** drücken.

---
[documentation index](../README.md) > Assembly3 ConstraintPointOnCircle/de
