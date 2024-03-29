---
 GuiCommand:
   Name: FEM EquationDeformation
   MenuLocation: Solve , Mechanical equations , Deformation equation
   Workbenches: FEM_Workbench
   Version: 0.21
   SeeAlso: FEM_EquationElasticity, FEM_tutorial
---

# FEM EquationDeformation

## Description

This equation describes the nonlinear elastic deformation of solid bodies.

For info about the math of the equation, see the [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Finite Elasticity*.

## Usage

1.  After adding an Elmer solver as described [here](FEM_SolverElmer#Equations.md), select it in the [tree view](Tree_view.md).
2.  Now either use the toolbar button <img alt="" src=images/FEM_EquationDeformation.svg  style="width:24px;"> or the menu **Solve → Mechanical equations → Deformation equation**.
3.  Change the [equation\'s solver settings](#Solver_Settings.md) or the [general solver settings](FEM_SolverElmer_SolverSettings.md) if necessary.

## Solver Settings 

For the general solver settings, see the [Elmer solver settings](FEM_SolverElmer_SolverSettings.md).

The deformation equation provides these special settings:

-    **Calculate Pangle**: If the principal angles should be calculated.

-    **Calculate Principal**: If all stresses should be calculated.

-    **Calculate Strains**: If strains will be calculated. This will also calculate the stresses, even if **Calculate Principal** or **Calculate Stresses** is *false*.

-    **Calculate Stresses**: If stresses should be calculated. Compared to **Calculate Principal** the Tresca yield criterion and the principal stress will not be calculated.

-    **Initialize State Variables**: See the Elmer manual for more info.

-    **Mixed Formulation**: See the Elmer manual for more info.

-    **Neo Hookean Model**: Uses the neo-Hookean material model.

-    **Variable**: The variable for the deformation equation. Change there the *3* to *2* if you have a 2D geometry. For the special case that you have **Mixed Formulation** and **Neo Hookean Model** set to *true*, the variable number must be geometry dimensions + 1, so for 3D geometry the *3* must be changed to *4*.

Equation:

-    **Plane Stress**: Computes solution according to the plane stress situation. Applies only for 2D geometry.

## Analysis Feature Information 

The deformation equation takes the following analysis features into account if they are set:

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Fixed boundary condition](FEM_ConstraintFixed.md)
-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Displacement boundary condition](FEM_ConstraintDisplacement.md)
-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Force load](FEM_ConstraintForce.md)
-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Initial temperature condition](FEM_ConstraintInitialTemperature.md)
-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Pressure load](FEM_ConstraintPressure.md)
-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Gravity load](FEM_ConstraintSelfWeight.md)
-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Spring](FEM_ConstraintSpring.md)

### Note

-   Except for calculations in 2D, for all the above analysis features it is important that they act on a face. Features in 3D set to lines or vertices are not recognized by the Elmer solver.

## Results

The available results depend on the [solver settings](#Solver_Settings.md). If none of the **Calculate *** settings was set to *true*, only the displacement is calculated. Otherwise also the corresponding results will be available.




 {{FEM Tools navi}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationDeformation
