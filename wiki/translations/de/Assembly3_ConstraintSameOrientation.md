---
- GuiCommand:
   Name:Assembly3 ConstraintSameOrientation
   Name/de:Assembly3 RichtungenAngleichen
   Icon:Assembly_ConstraintSameOrientation.svg
   Workbenches:[Assembly3](Assembly3_Workbench/de.md)
---

# Assembly3 ConstraintSameOrientation/de

## Beschreibung

Dieses Werkzeug verbindet zwei oder mehr Objekte eines Zusammenbaus und gleicht ihre Ausrichtungen an. Die gewählten Elemente der einzelnen Objekte oder präziser ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein oder mehrere Objekte im Verhältnis zu einem anderen Objekt zu positionieren.

Davon ausgehend, dass das erste Objekt bereits mittels <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Festsetzen](Assembly3_ConstraintLock/de.md) unbeweglich gemacht wurde, werden die weiteren Objekte auf Positionen bewegt, wo alle LKS die gleiche Ausrichtung besitzen, d.h. dass sich alle X- und Z-Achsen parallel ausrichten (wodurch auch die Y-Achsen parallel liegen).

Der Abstand ihrer Ursprünge in X-, Y- und Z-Richtung ist nicht festgelegt. Im Bezug auf das erste Element, können sich die weiteren Objekte noch in X-, Y- und Z-Richtung bewegen. Dies lässt für jede einzelne Verbindung drei Freiheitsgrade unbestimmt.

Diese Beziehung akzeptiert ebene Flächen.

## Anwendung

1.  Zwei oder mehr Objekte in einen Zusammenbau einfügen.
2.  Je ein ebenes Flächenelement pro Objekt auswählen.
3.  Schaltfläche**<img src="images/Assembly_ConstraintSameOrientation.svg" width=16px> [Richtungen angleichen](Assembly3_ConstraintSameOrientation/de.md)** drücken.



---
![](images/Button_right.svg) [documentation index](../README.md) > Assembly3 ConstraintSameOrientation/de
