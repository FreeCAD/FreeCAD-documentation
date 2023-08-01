---
- GuiCommand:
   Name:FEM ConstraintCurrentDensity
   Name/de:FEM RandbedingungStromdichte
   MenuLocation: Model - Electromagnetic Constraints - Constraint current density
   Workbenches:[FEM](FEM_Workbench/de.md)
   Version:0.21
   SeeAlso:[MagnetodynamischeGleichung](FEM_EquationMagnetodynamic/de.md), [Magnetodynamische2DGleichung](FEM_EquationMagnetodynamic2D/de.md)
---

# FEM ConstraintCurrentDensity/de



## Beschreibung

Erstellt eine FEM-Randbedingung für die Stromdichte, zur Verwendung mit der [magnetodynamischen Gleichung](FEM_EquationMagnetodynamic/de.md) und der [magnetodynamischen 2D-Gleichung](FEM_EquationMagnetodynamic2D/de.md).



## Anwendung

1.  Die Schaltfläche **<img src="images/FEM_ConstraintCurrentDensity.svg" width=16px> [Constraint current density](FEM_ConstraintCurrentDensity/de.md)** drücken oder den Menüeintrag **Model → Electromagnetic Constraints → <img src="images/FEM_ConstraintCurrentDensity.svg" width=16px> Constraint current density** auswählen.
2.  In der [3D-Ansicht](3D_view/de.md) das Objekt auswählen, dem die Randbedingung zugeordnet werden soll.
3.  Die Schaltfläche **Hinzufügen** Drücken.



## Optionen


<div lang="en" dir="ltr" class="mw-content-ltr">

-   **Current density\_\*\_1**: The real/imaginary part of the current density in x-direction in A/m². For other coordinate systems than Cartesian 3D, this will be the first coordinate of the system instead of x.
-   **Current density\_\*\_2**: The real/imaginary part of the current density in y-direction in A/m². For other coordinate systems than Cartesian 3D, this will be the second coordinate of the system instead of y.
-   **Current density\_\*\_3**: The real/imaginary part of the current density in z-direction in A/m². For other coordinate systems than Cartesian 3D, this will be the third coordinate of the system instead of z. If the coordinate system has no third coordinate, this setting will be ignored.
-   **Current density\_\*\_\*\_Disabled**: Whether the corresponding parameter is disabled (assumed as unknown by the solver).


</div>





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintCurrentDensity/de
