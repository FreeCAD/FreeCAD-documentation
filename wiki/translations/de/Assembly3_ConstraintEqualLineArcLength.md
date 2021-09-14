---
- GuiCommand:/de
   Name:Assembly3 ConstraintEqualLineArcLength
   Name/de:Assembly3 LinienGleichBogenlänge
   Icon:Assembly_ConstraintEqualLineArcLength.svg
   Workbenches:[Assembly3](Assembly3_Workbench/de.md)
---

## Beschreibung

Der Befehl <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg  style="width:16px;"> [Linien- gleich Bogenlänge](Assembly3_ConstraintEqualLineArcLength/de.md) bestimmt die Länge einer 2D-Linie wie z.B. einer nicht unterteilten 2D-Linie, die mit Werkzeugen der <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Draft](Draft_Workbench/de.md)-Arbeitsumgebung in Zusammenhang mit einer <img alt="" src=images/Assembly_Workplane.svg  style="width:16px;"> Arbeitsebene erstellt wurde.

Er verknüpft die Länge einer 2D-Linie mit der Länge eines Bogens (2D or 3D?).

Die Länge der gewählten Linie ist gleich der Länge des gewählten Bogens

Da ich dieses Werkzeug nicht zu Arbeit bewegen konnte, gibt es hier die Aussage des Quick-Info-Fensters:

Add an \"EqualLineArcLength\" constraint to make a line of the same length as an arc.

## Anwendung

1.  Auswahl der 2D-Linie, deren Länge festgelegt werden soll.
2.  Auswahl des 2D-Bogens, dessen Länge verwendet werden soll.
3.  Den Befehl <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg  style="width:16px;"> [Linien- gleich Bogenlänge](Assembly3_ConstraintEqualLineArcLength/de.md) aktivieren durch:
    -   Die Schaltfläche **<img src="images/Assembly_ConstraintEqualLineArcLength.svg" width=16px> [Linien- gleich Bogenlänge](Assembly3_ConstraintEqualLineArcLength/de.md)**.
4.  Schaltfläche **<img src="images/Assembly3_workbench_icon.svg" width=16px> [Beziehungen berechnen](Assembly3_ResolveConstraints/de.md)** oder **<img src="images/Assembly_QuickSolve.svg" width=16px> [Schnelle Berechnung](Assembly3_QuickSolve/de.md)** drücken, um neu zu berechnen

:   

    :   (Wenn **<img src="images/Assembly_AutoRecompute.svg" width=16px> [Automatische Berechnung](Assembly3_AutoRecompute/de.md)** und **<img src="images/Assembly_SmartRecompute.svg" width=16px> [Smarte Berechnung](Assembly3_SmartRecompute/de.md)** nicht aktiviert wurden).

Abhängig von der Reihenfolge der gewählten Linienarten erscheinen folgende Fehlermeldungen:

Constraint "EqualLineArcLength" requires the 1st element to be a linear edge
Constraint "EqualLineArcLength" requires the 2nd element to be an arc edge
Constraint "EqualLineArcLength" requires the 2nd element to be a circular edge






