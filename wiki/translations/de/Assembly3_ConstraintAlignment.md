---
- GuiCommand:/de
   Name:Assembly3 ConstraintAlignment
   Name/de:Assembly3 EbenenAusrichten
   Icon:Assembly_ConstraintAlignment.svg
   Workbenches:[Assembly3](Assembly3_Workbench/de.md)
---

# Assembly3 ConstraintAlignment/de

## Beschreibung

Dieses Werkzeug verbindet zwei oder mehr Objekte eines Zusammenbaus und gleicht ihre Ausrichtungen an. Die gewählten Elemente der einzelnen Objekte oder präziser ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein oder mehrere Objekte im Verhältnis zu einem anderen Objekt zu positionieren.

Davon ausgehend, dass das erste Objekt bereits mittels <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Festsetzen](Assembly3_ConstraintLock/de.md) unbeweglich gemacht wurde, werden die weiteren Objekte auf Positionen bewegt, wo die X-Y-Ebenen aller LKS komplanar sind und die Z-Achsen in die selbe Richtung zeigen.

Der Abstand ihrer Z-Achsen und die Winkel zwischen ihren X-Achsen (und genauso ihren Y-Achsen) sind nicht festgelegt. Im Bezug auf das erste Element, können sich die weiteren Objekte noch in X- und Y-Richtung bewegen und um die Z-Achse drehen. Dies lässt für jede einzelne Verbindung drei Freiheitsgrade unbestimmt.

## Anwendung

1.  Zwei oder mehr Objekte in einen Zusammenbau einfügen.
2.  Je ein planeres Flächenelement pro Objekt auswählen.
3.  Schaltfläche**<img src="images/Assembly_ConstraintAlignment.svg" width=16px> [Ebenen ausrichten](Assembly3_ConstraintAlignment/de.md)** drücken.

---
[documentation index](../README.md) > Assembly3 ConstraintAlignment/de
