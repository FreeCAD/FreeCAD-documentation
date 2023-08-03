---
 GuiCommand:
   Name: Assembly3 ConstraintColinear
   Name/de: Assembly3 Kollinear
   Icon: Assembly_ConstraintColinear.svg
   Workbenches: Assembly3_Workbench/de
---

# Assembly3 ConstraintColinear/de

## Beschreibung

Der Befehl <img alt="" src=images/Assembly_ConstraintColinear.svg  style="width:16px;"> [Kollinear](Assembly3_ConstraintColinear/de.md) setzt zwei nicht unterteilte 2D-Linien, die in der Draft-Arbeitsumgebung in Zusammenhang mit einer Arbeitsebene erzeugt wurden, zueinander in Beziehung.

Er verknüpft die Positionen beider 2D-Linien in einer Weise, dass der Ursprung des lokalen Koordinatensystems (LKS) einer Linie auf der Z-Achse des LKS der anderen Linie liegt, wobei beide Z-Achsen in dieselbe Richtung zeigen.

## Anwendung

1.  Zwei 2D-Linien auswählen.
2.  Den Befehl <img alt="" src=images/Assembly_ConstraintColinear.svg  style="width:16px;"> [Kollinear](Assembly3_ConstraintColinear/de.md) aktivieren durch:
    -   Die Schaltfläche **<img src="images/Assembly_ConstraintColinear.svg" width=16px> [Kollinear](Assembly3_ConstraintColinear/de.md)**.
3.  Schaltfläche **<img src="images/Assembly3_workbench_icon.svg" width=16px> [Beziehungen berechnen](Assembly3_ResolveConstraints/de.md)** oder **<img src="images/Assembly_QuickSolve.svg" width=16px> [Schnelle Berechnung](Assembly3_QuickSolve/de.md)** drücken, um neu zu berechnen

:   

    :   (Wenn **<img src="images/Assembly_AutoRecompute.svg" width=16px> [Automatische Berechnung](Assembly3_AutoRecompute/de.md)** und **<img src="images/Assembly_SmartRecompute.svg" width=16px> [Smarte Berechnung](Assembly3_SmartRecompute/de.md)** nicht aktiviert wurden).

## Hinweise

Dieses Werkzeug akzeptiert auch 3D-Elemente wie z.B. Kanten oder Mittellinien.

-   2D/3D or 3D/2D: Anstatt der Z-Achse des 3D-Elements wird die Projektion dieser Achse auf die Arbeitsebene der 2D-Linie genutzt, um die Linien zu Positionieren.
-   Beide 3D: Die Linie werden zueinander positioniert, aber ich kann nicht erkennen, wie\...



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintColinear/de
