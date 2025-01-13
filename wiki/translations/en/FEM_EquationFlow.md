---
 GuiCommand:
   Name: FEM EquationFlow
   MenuLocation:  Solve , Flow equation
   Workbenches: FEM_Workbench
   Version: 0.17
   SeeAlso: 
---

# FEM EquationFlow/en

## Description

This equation calculates viscous fluid flows using the [Navier-Stokes equations](https://en.wikipedia.org/wiki/Navier-Stokes_Equations).

For info about the math of the equation, see the [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Navier-Stokes Equations*.

## Usage

1.  After adding an Elmer solver as described [here](FEM_SolverElmer#Equations.md), select it in the [tree view](Tree_view.md).
2.  Now either use the toolbar button <img alt="" src=images/FEM_EquationFlow.svg  style="width:24px;"> or the menu **Solve → Flow equation**.
3.  Change the [equation\'s solver settings](#Solver_Settings.md) or the [general solver settings](FEM_SolverElmer_SolverSettings.md) if necessary.

## Solver Settings 

For the general solver settings, see the [Elmer solver settings](FEM_SolverElmer_SolverSettings.md).

The flow equation provides these special settings:

-    **Div Discretization**: To be set to *true* for incompressible flow for more stable discretization when the [Reynolds number](https://en.wikipedia.org/wiki/Reynolds_number) increases.

-    **Flow Model**: The flow model that should be used. The default *Full* includes convection and time derivative terms in the model. *No convection* switches off the convection terms and the *Stokes* model switches off the convection terms and the (explicit) time derivative terms.

-    **Gradp Discretization**: If set to *true* pressure [Dirichlet boundary conditions](https://en.wikipedia.org/wiki/Dirichlet_boundary_condition) can be used. Also the mass flux is available as a natural boundary condition.

-    **Variable**: Optional only for calculations in 2D: You can change the default of *3* to *2*.**Note**: In this case none of the flow velocity boundary conditions can have a specified z-component.

Equation:

-    **Convection**: The type of convection to be used in the <img alt="" src=images/FEM_EquationHeat.svg  style="width:24px;"> [Heat equation](FEM_EquationHeat.md).**Note**: For thermal flows it must be set to *Computed* (the default).

-    **Magnetic Induction**: If set to *true* the magnetic induction equation will be solved along with the [Navier-Stokes equations](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations).

### Notes for Convergence 

If the solver results do not converge, you can try these things (in the given order):

1.  Reduce the **Relaxation Factor**, see the [nonlinear system settings](FEM_SolverElmer_SolverSettings#Relaxation_Factor.md).
2.  Increase the value for **Nonlinear Newton After Iterations**, see the [nonlinear system settings](FEM_SolverElmer_SolverSettings#Nonlinear_System.md).
3.  Reduce the number of CPU cores used, see the [FEM preferences](FEM_Preferences#Elmer.md).
4.  Increase the mesh density (make it more fine).

## Analysis Feature Information 

The flow equation takes the following analysis features into account if they are set:

-   <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Flow velocity boundary condition](FEM_ConstraintFlowVelocity.md)
-   <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Initial flow velocity condition](FEM_ConstraintInitialFlowVelocity.md)
-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Pressure load](FEM_ConstraintPressure.md)
-   <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:32px;"> [Initial pressure condition](FEM_ConstraintInitialPressure.md) (<small>(v0.21)</small> )

### Notes

-   Except for calculations in 2D, for all above boundary conditions it is important that they act on a face or body. Boundary conditions for 3D set to lines or vertices are not recognized by the Elmer solver.
-   Since <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:24px;"> [Pressure load](FEM_ConstraintPressure.md) can only be set to faces, pressure loads cannot be used for calculations in 2D.
-   If there is no <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:24px;"> [Pressure load](FEM_ConstraintPressure.md) set, <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:24px;"> [Initial pressure condition](FEM_ConstraintInitialPressure.md) will only be taken into account if **Gradp Discretization** is set to *true*.

## Results

The results are the velocity in $\rm m/s$ and the pressure in $\rm Pa$. If there is no <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:24px;"> [Initial pressure condition](FEM_ConstraintInitialPressure.md) and <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:24px;"> [Pressure load](FEM_ConstraintPressure.md) given, the resulting pressure will be relative not absolute. Since pressure must act on a face, absolute pressure results cannot be obtained in 2D simulations.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationFlow/en
