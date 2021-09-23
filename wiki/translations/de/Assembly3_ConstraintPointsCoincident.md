---
- GuiCommand:/de
   Name:Assembly3 ConstraintPointsCoincident
   Name/de:Assembly3 PunktAufPunkt
   Icon:Assembly_ConstraintPointCoincident.svg
   Workbenches:[Assembly3](Assembly3_Workbench/de.md)
---

# Assembly3 ConstraintPointsCoincident/de

## Beschreibung

Dieses Werkzeug stellt eine Verbindung zwischen zwei Objekten eines Zusammenbaus her und fixiert den Abstand zwischen ihnen sowie ihre Ausrichtung zueinander. Die Gewählten Elemente beider Objekte oder präziser ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein Objekt zum anderen zu positionieren.

Davon ausgehend, dass das erste Objekt bereits mittels <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Festsetzen](Assembly3_ConstraintLock/de.md) unbeweglich gemacht wurde, wird das nächste Objekt auf eine Position bewegt, wo beide LKS-Ursprünge deckungsgleich sind.

Punktelemente haben keine Ausdehnung egal in welcher Richtung (Länge ist Null) und daher kann auch keine Orientierung ermittelt werden, d.h. dass ihre LKS nur für weitere Elementparameter benötigt werden. Die Ausrichtung der LKS bleibt immer die gleiche, wie die des globalen Koordinatensystems und kann nicht dazu genutzt werden, die Anzahl von Freiheitsgraden im Zusammenhang mit Drehungen zu reduzieren.

Im Bezug auf das erste Element, kann sich das weitere Objekte noch um den Ursprung herum bewegen (um alle drei Achsen). Dies lässt für jede einzelne Verbindung drei Freiheitsgrade unbestimmt.

## Anwendung

1.  Zwei Objekte in einen Zusammenbau einfügen.
2.  Je ein Punktelement pro Objekt auswählen.
3.  Schaltfläche**<img src="images/Assembly_ConstraintPointCoincident.svg" width=16px> [Punkt auf Punkt](Assembly3_ConstraintPointsCoincident/de.md)** drücken.

---
[documentation index](../README.md) > Assembly3 ConstraintPointsCoincident/de
