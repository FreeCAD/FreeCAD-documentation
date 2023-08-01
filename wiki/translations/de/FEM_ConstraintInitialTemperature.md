---
- GuiCommand:
   Name:FEM ConstraintInitialTemperature
   Name/de:FEM RandbedingungStarttemperatur
   MenuLocation:Modell - Thermische Randbedingungen - Randbedingung Starttemperatur
   Workbenches:[FEM](FEM_Workbench/de.md)
   SeeAlso:[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM ConstraintInitialTemperature/de

## Beschreibung

Erstellt eine Randbedingung Starttemperatur für eine thermo-mechanische Analyse.

## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> [Randbedingung Starttemperatur](FEM_ConstraintInitialTemperature.md)** drücken.
    -   Den Menüeintrag **Modell → Thermische Randbedingungen → <img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> Randbedingung Starttemperatur** auswählen.
2.  Den Startwert der Temperatur für die Analyse eingeben.

## Limitations

Diese Randbedingung ordnet die Starttemperatur allen Knoten im FEA-Modell zu - es ist nicht möglich einzelne Bereiche auszuwählen.

## Hinweise

-   This constraint uses the \*INITIAL CONDITIONS card in CalculiX. The initial temperature constraint is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node215.html>





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialTemperature/de
