---
- GuiCommand:/de
   Name:FEM ConstraintDisplacement
   Name/de:FEM RandbedingungVersatz
   MenuLocation:Modell → Mechanische Randbedingungen → Randbedingung Versatz
   Workbenches:[FEM](FEM_Workbench/de.md)
   Shortcut:
   SeeAlso:[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM ConstraintDisplacement/de

## Beschreibung

Erstellt eine FEM-Randbedingungn für einen festgelegten Versatz eines ausgewählten Objekts für einen bestimmten Freiheitsgrad.

## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintDisplacement.svg" width=16px> [Randbedingung Versatz](FEM_ConstraintDisplacement/de.md)** drücken.
    -   Den Menüeintrag **Modell → Mechanische Randbedingungen → <img src="images/FEM_ConstraintDisplacement.svg" width=16px> Randbedingung Versatz** auswählen.
2.  In der [3D-Ansicht](3D_view.md) as Objekt auswählen, dem die Randbedingung zugeordnet werden soll; dies kann ein Knoten (Ecke), eine Kante, oder eine Fläche sein.
3.  Einen der Freiheitsgrade auswählen oder einen Versatz festlegen.

## Hinweise

-   The constraint uses the \*BOUNDARY card in CalculiX.
-   Fixing a degree of freedom is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node164.html>
-   Prescribing a displacement for a degree of freedom is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node165.html>





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintDisplacement/de
