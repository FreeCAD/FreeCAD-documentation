---
- GuiCommand:
   Name:FEM ConstraintElectrostaticPotential
   MenuLocation: Model → Electrostatic Constraints → Constraint Electrostatic Potential
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM capacitance example](FEM_Example_Capacitance_Two_Balls.md), [FEM tutorial](FEM_tutorial.md)
---

# FEM ConstraintElectrostaticPotential/pt-br

## Descrição

Creates a FEM constraint for the electrostatic potential. To be used together with the [Electrostatic](FEM_EquationElectrostatic.md) or [Electricforce](FEM_EquationElectricforce.md) equation.

## Utilização

#\* Either press the **<img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> [FEM ConstraintElectrostaticPotential](FEM_ConstraintElectrostaticPotential.md)** button

#\* Or use the menu **Model → Electrostatic Constraints → <img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> Constraint electrostatic potential**.

1.  In the [3D view](3D_view.md) select the object the constraint should be applied to.
2.  Press the **Add** button.

## Options

The dialog offers the following settings:

![](images/FEM_ElectrostaticPotential_dialog.png )

-   **Potential**: The electric potential in V.
-   **Potential Constant**: Option to set a constant potential.
-   **Farfield / Electric infinity**: Option to make spherical approximation that the volume above the face extends to infinity.
-   **Calculate Electric Force**: Option to trigger the calculation of the electric for using the [Electricforce](FEM_EquationElectricforce.md) equation.
-   **Capacity Body:**: Counter of the body (or face) with a capacitance.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintElectrostaticPotential/pt-br
