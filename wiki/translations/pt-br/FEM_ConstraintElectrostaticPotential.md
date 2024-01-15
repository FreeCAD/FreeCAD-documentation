---
 GuiCommand:
   Name: FEM ConstraintElectrostaticPotential
   MenuLocation: Model , Electromagnetic boundary conditions , Electrostatic potential boundary condition
   Workbenches: FEM_Workbench
   SeeAlso: FEM_Example_Capacitance_Two_Balls, FEM_tutorial
---

# FEM ConstraintElectrostaticPotential/pt-br



## Descrição

Creates a FEM boundary condition for the electrostatic potential. To be used together with the [Electrostatic](FEM_EquationElectrostatic.md) or [Electricforce](FEM_EquationElectricforce.md) equation.



## Utilização

1.  Press the **<img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> [Electrostatic potential boundary condition](FEM_ConstraintElectrostaticPotential.md)** button or use the menu **Model → Electromagnetic boundary conditions → <img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> Electrostatic potential boundary condition**.
2.  In the [3D view](3D_view.md) select the object the boundary condition should be applied to.
3.  Press the **Add** button.

## Options

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
-   **Calculate Electric Force**: Option to trigger the calculation of the electric force using the [Electricforce](FEM_EquationElectricforce.md) equation.
-   **Capacity Body:**: Counter of the body (or face) with a capacitance.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintElectrostaticPotential/pt-br
