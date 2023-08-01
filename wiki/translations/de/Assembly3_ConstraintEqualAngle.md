---
- GuiCommand:
   Name: Assembly3 ConstraintEqualAngle
   Name/de: Assembly3 GleicheWinkel
   Icon: Assembly_ConstraintEqualAngle.svg
   Workbenches: [Assembly3](Assembly3_Workbench/de.md)
---

# Assembly3 ConstraintEqualAngle/de

## Beschreibung

Dieses Werkzeug stellt eine Verbindung zwischen zwei Objekten eines Zusammenbaus her und setzt einen Winkel zwischen ihnen, abhängig von dem Wert eines weiteren Winkels, fest. Die Gewählten Elemente beider Objekte oder präziser ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein Objekt zum anderen zu positionieren.

Es arbeitet sowohl mit 3D-Linien-Elementen und planaren Flächenelementen, als auch mit 2D-Linien-Elementen auf einer Skizzenebene.

Die Richtung der Linien und auch die Flächennormalen werden durch die Z-Achse des jeweiligen LKS repräsentiert, wodurch tatsächlich der Winkel zwischen den Z-Achsen beider Elemente festgelegt wird (auf Basis eines weiteren Winkels zwischen zwei Z-Achsen).

## Anwendung

1.  Zwei Objekte in einen Zusammenbau einfügen.
2.  Jeweils ein Linienelement oder ein planeres Flächenelement beider Objekte auswählen.
3.  Schaltfläche **<img src="images/Assembly_ConstraintEqualAngle.svg" width=16px> [Gleiche Winkel](Assembly3_ConstraintEqualAngle/de.md)** drücken.

:   Zusätzlich kann es erforderlich sein die Funktion \"Element umdrehen\" zu nutzen, wenn die LKS nicht wie erwartet ausgerichtet sind.



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintEqualAngle/de
