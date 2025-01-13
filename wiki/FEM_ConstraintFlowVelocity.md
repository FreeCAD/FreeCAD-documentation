---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ConstraintFlowVelocity
   MenuLocation: Model , Fluid boundary conditions , Flow velocity boundary condition
   Workbenches: FEM_Workbench
   SeeAlso: FEM_ConstraintInitialFlowVelocity
}}
{{GuiCommandFemInfo
   Solvers: Elmer
}}
---

# FEM ConstraintFlowVelocity

## Description

Applies a flow velocity as boundary condition to an edge in 2D or to a face in 3D.

## Usage

1.  Press the **<img src="images/FEM_ConstraintFlowVelocity.svg" width=16px> [Flow velocity boundary condition](FEM_ConstraintFlowVelocity.md)** button or select the menu **Model → Fluid boundary conditions → <img src="images/FEM_ConstraintFlowVelocity.svg" width=16px> Flow velocity boundary condition**.
2.  Press the **Add** button.
3.  Select the target Edges or Faces.
4.  Uncheck *unspecified* to activate the necessary fields for editing.
5.  Set the velocity values or (<small>(v0.21)</small> ) specify a formula.

## Formulas


<small>(v0.21)</small> 

It is possible to define a velocity by specifying the velocity profile as formula. In this case the solver sets the velocities at the different positions according to the profile.

To specify for example the velocity profile

$\quad
v_{x} (y)=6\left(y-1\right)\left(2-y\right)$

for $y\in[1;2]$ (assuming that e.g. a pipe has the wall at y = 1 m and y = 2 m)

enter this to the *Formula* field: ` Variable Coordinate 2; Real MATC "6*(tx-1)*(2-tx)"`

This code has the following syntax:

-   the prefix *Variable* specifies that the velocity is not a constant but a variable
-   the variable to calculate the velocity is *Coordinate 2*, meaning y
-   the velocity values are returned as *Real* (floating point value)
-   *MATC* is the prefix for the Elmer solver that the following code is a formula
-   *tx* is always the name of the variable in *MATC* formulas, no matter that *tx* in our case is actually *y*

That *y* will only be in the range $y\in[1;2]$ is set because *MATC* only evaluates the *tx* range where the result is positive. This behavior is a bit special but has the advantage that one does not need to specify the range manually.

It is also possible to use more than one variable. See as example the definition of rotations in the [displacement constraint](FEM_ConstraintDisplacement#Rotations.md).

## Notes

-   Any vector component that should be the result of the solver must be set as *Unspecified*.
-   If the target face or edge is not aligned with the main Cartesian coordinate system, it is possible to set the option **Normal to boundary**.

    :   If **Normal to boundary** is checked, the normal vector to the selected edge or face is X and it will be oriented away from the mesh domain.
    :   For example, if a flow of 20 mm/s of air should enter the domain, then with **Normal to boundary** one must input -20 mm/s in the *Velocity x* field.

-   For a wall with non-slip condition, set all velocity components to 0.
-   For a symmetry condition, set the the flow to (0, Unspecified, Unspecified) if **Normal to boundary** is checked.




 {{FEM Tools navi}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintFlowVelocity
