---
 GuiCommand:
   Name: Assembly3 ConstraintAngle
   Name/de: Assembly3 WinkelFestlegen
   Icon: Assembly_ConstraintAngle.svg
   Workbenches: Assembly3_Workbench/de
---

# Assembly3 ConstraintAngle/de

## Beschreibung

Dieses Werkzeug stellt eine Verbindung zwischen zwei Objekten eines Zusammenbaus her und fixiert den Abstand zwischen ihnen sowie ihre Ausrichtung zueinander. Die Gewählten Elemente beider Objekte oder präziser ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein Objekt zum anderen zu positionieren.

Der Winkel zwischen zwei Elementen, d.h. der Winkel zwischen ihren Z-Achsen, wird festgelegt.

Der Abstand ihrer Ursprünge in X-, Y- und Z-Richtung und die Winkel zwischen ihren X-Achsen und Y-Achsen sind nicht festgelegt. Im Bezug auf das erste Element, können sich die weiteren Objekte noch in X-, Y- und Z-Richtung bewegen und um beide Z-Achsen drehen. Dies lässt für jede einzelne Verbindung fünf Freiheitsgrade unbestimmt.

Diese Beziehung akzeptiert gerade Kanten und ebene Flächen.

## Anwendung

1.  Zwei oder mehr Objekte in einen Zusammenbau einfügen.
2.  Je ein ebenes Flächenelement oder eine gerade Kante pro Objekt auswählen.
3.  Schaltfläche**<img src="images/Assembly_ConstraintAngle.svg" width=16px> WinkelFestlegen** drücken.
4.  Optional kann der Wert der {{PropertyData/de|Angle}} (Winkel) geändert werden.

## Hinweise

2D: Diese Randbedingung scheint die einzige Möglichkeit zu sein, einen Winkel in einer Skelettskizze zu steuern (2D kinematischer Zusammenbau); Kann das BITTE jemand wiederlegen?

-   Ihre {{PropertyData/de|Angle|Angle}} erlaubt jeden positiven Wert, aber genau 0° und 180° verwirren den Löser.
-   Die Richtung wird umgekehrt, wenn Winkel größer als 180° angegeben werden und daraus ergibt sich für 135° und 225° die gleiche Position für die beteiligten Elemente.

:   Sie ist nutzlos, wenn man eine komplette Drehung simulieren möchte und ruiniert so das Prinzip eine Skelettskizze zu verwenden für sehr viele kinematische Anwendungen, wie z. B. einen Kolben mit einer Kurbel, verbunden über ein Pleuel, anzutreiben.



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintAngle/de
