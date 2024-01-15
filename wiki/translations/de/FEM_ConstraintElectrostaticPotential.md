---
 GuiCommand:
   Name: FEM ConstraintElectrostaticPotential
   Name/de: FEM RandbedingungElektrostatischesPotential
   MenuLocation:  Modell , Elektromagnetische Randbedingungen , Randbedingung elektrostatisches Potential
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_Example_Capacitance_Two_Balls/de, FEM_tutorial/de
---

# FEM ConstraintElectrostaticPotential/de



## Beschreibung

Erstellt eine FEM-Randbedingung für das elektrostatische Potential, zur Verwendung mit der [Elektrostatik-Gleichung](FEM_EquationElectrostatic/de.md) oder der [Gleichung für die elektrische Kraft](FEM_EquationElectricforce/de.md).



## Anwendung

1.  Die Schaltfläche **<img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> [Randbedingung elektrostatisches Potential](FEM_ConstraintElectrostaticPotential/de.md)** drücken oder den Menüeintrag **Modell → Elektromagnetische Randbedingungen → <img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> Randbedingung elektrostatisches Potential** auswählen.
2.  In der [3D-Ansicht](3D_view/de.md) das Objekt auswählen, dem die Randbedingung zugeordnet werden soll.
3.  Die Schaltfläche **Hinzufügen** Drücken.



## Optionen

Der Dialog Eigenschaften der Analyseelemente ermöglicht die folgenden Einstellungen:

![](images/FEM_ElectrostaticPotential_dialog.png )

-   **Potential**: The electric potential in V.
-   *unspecified*\': To declare the potential as unknown for the solver.
-   **Vector Field**: To enable the input of the components of a potential vector field.
-   **x**: The real/imaginary part of the potential in x-direction in V. For other coordinate systems than Cartesian 3D, this will be the first coordinate of the system instead of x.
-   **y**: The real/imaginary part of the potential in y-direction in V. For other coordinate systems than Cartesian 3D, this will be the second coordinate of the system instead of y.
-   **z**: The real/imaginary part of the potential in z-direction in V. For other coordinate systems than Cartesian 3D, this will be the third coordinate of the system instead of z. If the coordinate system has no third coordinate, this setting will be ignored.
-   **x, y, z checkboxes**: To declare the corresponding potential as unknown for the solver.
-   **Potential Constant**: Option to set a constant potential.
-   **Farfield / Electric infinity**: Option to make spherical approximation that the volume above the face extends to infinity.
-   **Calculate Electric Force**: Option to trigger the calculation of the electric force using the [Electricforce](FEM_EquationElectricforce.md) equation.
-   **Capacity Body:**: Counter of the body (or face) with a capacitance.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintElectrostaticPotential/de
