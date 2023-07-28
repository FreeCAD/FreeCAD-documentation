---
- GuiCommand:/de
   Name:FEM ConstraintElectrostaticPotential
   Name/de:FEM RandbedingungElektrostatischesPotential
   MenuLocation: Model → Electromagnetic Constraints → Constraint Electrostatic Potential
   Workbenches:[FEM](FEM_Workbench/de.md)
   SeeAlso:[FEM Beispiel Kapazität Zweier Kugeln](FEM_Example_Capacitance_Two_Balls/de.md), [FEM Anleitung](FEM_tutorial/de.md)
---

# FEM ConstraintElectrostaticPotential/de



## Beschreibung

Erstellt eine FEM-Randbedingung für das elektrostatische Potential, zur Verwendung mit der [ElektrostatischenGleichung](FEM_EquationElectrostatic/de.md) oder der [ElectricforceGleichung](FEM_EquationElectricforce/de.md).



## Anwendung

#\* Either press the **<img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> [FEM ConstraintElectrostaticPotential](FEM_ConstraintElectrostaticPotential.md)** button or use the menu **Model → Electromagnetic Constraints → <img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> Constraint electrostatic potential**.

1.  In the [3D view](3D_view.md) select the object the constraint should be applied to.
2.  Press the **Add** button.



## Optionen

The dialog offers the following settings:

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
-   **Calculate Electric Force**: Option to trigger the calculation of the electric for using the [Electricforce](FEM_EquationElectricforce.md) equation.
-   **Capacity Body:**: Counter of the body (or face) with a capacitance.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintElectrostaticPotential/de
