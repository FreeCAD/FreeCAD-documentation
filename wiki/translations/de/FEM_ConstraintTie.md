---
 GuiCommand:
   Name: FEM ConstraintTie
   Name/de: FEM RandbedingungVerbinder
   MenuLocation: Modell , Mechanische Randbedingungen und Belastungen , Randbedingung Verbinder
   Workbenches: FEM_Workbench/de
   Version: 0.19
   SeeAlso: FEM_ConstraintPressure/de
---

# FEM ConstraintTie/de



## Beschreibung

Legt eine Randbedingung Verbinder fest, die zwei ausgewählte Flächen in einer Weise verbindet, dass sie (anders als ein Kontakt funktioniert) während der Analyse nicht getrennt werden können und nicht aufeinander gleiten können. So bleiben die Flächen dauerhaft untrennbar verbunden.



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintTie.svg" width=16px> [Randbedingung Verbinder](FEM_ConstraintTie/de.md)** drücken.
    -   Den Menüeintrag **Modell → Mechanische Randbedingungen und Belastungen → <img src="images/FEM_ConstraintTie.svg" width=16px> Randbedingung Verbinder** auswählen.
2.  Die Schaltfläche **Hinzufügen** im Aufgabenbereich drücken und dann nacheinander genau zwei Flächen auswählen.
3.  Wahlweise die Toleranz festlegen - Die Randbedingung Verbinder wird nur auf Knoten angewendet, die zur gegenüberliegenden Fläche einen Abstand haben, der nicht größer ist, als der hier eingegebene.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintTie/de
