---
- GuiCommand:
   Name:FEM ConstraintElectrostaticPotential
   Name/ru:FEM ConstraintElectrostaticPotential
   Icon:Fem-constraint-electrostatic-potential.svg
   MenuLocation: Model → Electrostatic Constraints → Constraint Electrostatic Potential
   Workbenches:[FEM](FEM_Workbench/ru.md)
   Shortcut:
   SeeAlso:[FEM tutorial](FEM_tutorial/ru.md)
---

# FEM ConstraintElectrostaticPotential/ru


</div>

## Описание

Creates a FEM constraint for the electrostatic potential. To be used together with the [Electrostatic](FEM_EquationElectrostatic.md) or [Electricforce](FEM_EquationElectricforce.md) equation.

## Применение

#\* Either press the **<img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> [FEM ConstraintElectrostaticPotential](FEM_ConstraintElectrostaticPotential.md)** button

#\* Or use the menu **Model → Electrostatic Constraints → <img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> Constraint electrostatic potential**.

1.  In the [3D view](3D_view.md) select the object the constraint should be applied to.
2.  Press the **Add** button.

## Опции

The dialog offers the following settings:

![](images/FEM_ElectrostaticPotential_dialog.png )

-   **Potential**: The electric potential in V.
-   **Potential Constant**: Option to set a constant potential.
-   **Farfield / Electric infinity**: Option to make spherical approximation that the volume above the face extends to infinity.
-   **Calculate Electric Force**: Option to trigger the calculation of the electric for using the [Electricforce](FEM_EquationElectricforce.md) equation.
-   **Capacity Body:**: Counter of the body (or face) with a capacitance.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintElectrostaticPotential/ru
