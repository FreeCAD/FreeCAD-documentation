---
- GuiCommand:/de
   Name:Assembly3 ConstraintAxial
   Name/de:Assembly3 AxialeAusrichtung
   Icon:Assembly_ConstraintAxial.svg
   Workbenches:[Assembly3](Assembly3_Workbench/de.md)
---

## Beschreibung

Dieses Werkzeug verbindet zwei oder mehr Objekte eines Zusammenbaus und gleicht ihre Ausrichtungen an. Die gewählten Elemente der einzelnen Objekte oder präziser ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein oder mehrere Objekte im Verhältnis zu einem anderen Objekt zu positionieren.

Davon ausgehend, dass das erste Objekt bereits mittels <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Festsetzen](Assembly3_ConstraintLock/de.md) unbeweglich gemacht wurde, werden die weiteren Objekte auf Positionen bewegt, wo die Z-Achsen kollinear sind.

Der Abstand ihrer Ursprünge auf der gemeinsamen Z-Achse und die Winkel zwischen ihren X-Achsen (und genauso ihren Y-Achsen) sind nicht festgelegt. Im Bezug auf das erste Element, können sich die weiteren Objekte noch in Z-Richtung bewegen und um die Z-Achse drehen. Dies lässt für jede einzelne Verbindung zwei Freiheitsgrade unbestimmt.

Diese Beziehung akzeptiert

:   \- gerade Kanten, die sich kollinear ausrichten,
:   \- ebene Flächen, die sich über ihre Flächennormalen ausrichten,
:   \- zylindrische Flächen, die sich über ihre Achsrichtung ausrichten.

Die unterschiedliche Geometriearten können gemischt werden.

## Anwendung

1.  Zwei oder mehr Objekte in einen Zusammenbau einfügen.
2.  Je ein Element pro Objekt auswählen.
3.  Schaltfläche**<img src="images/Assembly_ConstraintAxial.svg" width=16px> [Axiale Ausrichtung](Assembly3_ConstraintAxial/de.md)** drücken.






