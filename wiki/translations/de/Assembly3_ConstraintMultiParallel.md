---
 GuiCommand:
   Name: Assembly3 ConstraintMultiParallel
   Name/de: Assembly3 MehrfachParallel
   Icon: Assembly_ConstraintMultiParallel.svg
   Workbenches: Assembly3_Workbench/de
---

# Assembly3 ConstraintMultiParallel/de

## Beschreibung

Dieses Werkzeug verbindet zwei oder mehr Objekte eines Zusammenbaus und gleicht ihre Ausrichtungen an. Die gewählten Elemente der einzelnen Objekte oder präziser ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein oder mehrere Objekte im Verhältnis zu einem anderen Objekt zu positionieren.

Davon ausgehend, dass das erste Objekt bereits mittels <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Festsetzen](Assembly3_ConstraintLock/de.md) unbeweglich gemacht wurde, werden die weiteren Objekte auf Positionen bewegt, wo alle Z-Achsen parallel sind.

Der Abstand ihrer Ursprünge in X-, Y- und Z-Richtung und die Winkel zwischen ihren X-Achsen (und genauso ihren Y-Achsen) sind nicht festgelegt. Im Bezug auf das erste Element, können sich die weiteren Objekte noch in X-, Y- und Z-Richtung bewegen und um die Z-Achse drehen. Dies lässt für jede einzelne Verbindung vier Freiheitsgrade unbestimmt.

Diese Beziehung akzeptiert gerade Kanten und ebene Flächen, die sich parallel ausrichten.

## Anwendung

1.  Zwei oder mehr Objekte in einen Zusammenbau einfügen.
2.  Je ein ebenes Flächenelement pro Objekt auswählen.
3.  Schaltfläche**<img src="images/Assembly_ConstraintMultiParallel.svg" width=16px> [Mehrfach parallel](Assembly3_ConstraintMultiParallel/de.md)** drücken.



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintMultiParallel/de
