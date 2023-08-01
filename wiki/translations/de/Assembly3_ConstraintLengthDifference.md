---
- GuiCommand:
   Name:Assembly3 ConstraintLengthDifference
   Name/de :Assembly3 Längendifferenz
   Icon:Assembly_ConstraintLengthDifference.svg
   Workbenches:[Assembly3](Assembly3_Workbench/de.md)
---

# Assembly3 ConstraintLengthDifference/de

## Beschreibung

Dieses Werkzeug legt die Länge einer nicht unterteilten 2D-Linie fest, die in der Draft-Arbeitsumgebung in Zusammenhang mit einer Arbeitsebene erzeugt wurde.

Es stellt eine Beziehung zwischen der Länge einer 2D-Linie und der Länge einer weiteren 2D- oder 3D-Linie her, z.B. eines geraden Kantenelements oder einer Skizzenlinie.

Der Längenwert der zuerst gewählten Linie ist gleich dem Längenwert der zweiten Linie zuzüglich eines Differenzwertes.

:   (Oder der Längenwert der zweiten gewählten Linie ist gleich dem Längenwert der ersten Linie abzüglich eines Differenzwertes.)

## Anwendung

1.  Zwei Linien auswählen, von denen wenigsten eine eine 2D-Linie sein sollte.
2.  Schaltfläche **<img src="images/Assembly_ConstraintLengthDifference.svg" width=16px> [Längendifferenz](Assembly3_ConstraintLengthDifference/de.md)** drücken.
3.  **Difference**-Parameter im Eigenschaftenfenster auf den gewünschten Wert setzen.
4.  Schaltfläche **<img src="images/Assembly3_workbench_icon.svg" width=16px> [Beziehungen berechnen](Assembly3_ResolveConstraints/de.md)** oder **<img src="images/Assembly_QuickSolve.svg" width=16px> [Schnelle Berechnung](Assembly3_QuickSolve/de.md)** drücken um neu zu berechnen

:   

    :   (wenn **<img src="images/Assembly_AutoRecompute.svg" width=16px> [Automatische Berechnung](Assembly3_AutoRecompute/de.md)** und **<img src="images/Assembly_SmartRecompute.svg" width=16px> [Smarte Berechnung](Assembly3_SmartRecompute/de.md)** nicht aktiviert wurden).



---
![](images/Button_right.svg) [documentation index](../README.md) > Assembly3 ConstraintLengthDifference/de
