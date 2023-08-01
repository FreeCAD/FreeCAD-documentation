---
- GuiCommand:
   Name:FEM ConstraintMagnetization
   Name/de:FEM RandbedingungMagnetisierung
   MenuLocation: Model → Electromagnetic Constraints → Constraint magnetization
   Workbenches:[FEM](FEM_Workbench/de.md)
   Version:0.21
   SeeAlso:[MagnetodynamischeGleichung](FEM_EquationMagnetodynamic/de.md), [Magnetodynamische2DGleichung](FEM_EquationMagnetodynamic2D/de.md)
---

# FEM ConstraintMagnetization/de



## Beschreibung

Erstellt eine FEM-Randbedingung für die Magnetisierung, zur Verwendung mit der [magnetodynamischen Gleichung](FEM_EquationMagnetodynamic/de.md) und der [magnetodynamischen 2D-Gleichung](FEM_EquationMagnetodynamic2D/de.md).



## Anwendung

1.  Die Schaltfläche **<img src="images/FEM_ConstraintMagnetization.svg" width=16px> [ConstraintMagnetization](FEM_ConstraintMagnetization/de.md)** drücken oder den Menüeintrag **Model → Electromagnetic Constraints → <img src="images/FEM_ConstraintMagnetization.svg" width=16px> Constraint magnetization** auswählen.
2.  In der [3D-Ansicht](3D_view/de.md) das Objekt auswählen, demdie Randbedingung zugeordnet werden soll.
3.  Die Schaltfläche **Hinzufügen** drücken.



## Optionen


<div lang="en" dir="ltr" class="mw-content-ltr">

-   **Magnetization\_\*\_1**: The real/imaginary part of the magnetization in x-direction in A/m. For other coordinate systems than Cartesian 3D, this will be the first coordinate of the system instead of x.
-   **Magnetization\_\*\_2**: The real/imaginary part of the magnetization in y-direction in A/m. For other coordinate systems than Cartesian 3D, this will be the second coordinate of the system instead of y.
-   **Magnetization\_\*\_3**: The real/imaginary part of the magnetization in z-direction in A/m. For other coordinate systems than Cartesian 3D, this will be the third coordinate of the system instead of z. If the coordinate system has no third coordinate, this setting will be ignored.
-   **Magnetization\_\*\_\*\_Disabled**: Whether the corresponding parameter is disabled (assumed as unknown by the solver).


</div>





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintMagnetization/de
