---
- GuiCommand:
   Name: FEM EquationElectricforce
   Name/pl: MES: Równanie siły elektrostatycznej
   MenuLocation: Rozwiąż -> Równania elektromagnetyczne -> Równanie siły elektrostatycznej
   Workbenches: FEM_Workbench/pl
   Version: 0.19
   SeeAlso: FEM_EquationElectrostatic/pl
---

# FEM EquationElectricforce/pl



## Opis

This equation describes the electrostatic force acting on a surface.

For info about the math of the equation, see the [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Electrostatic force*.

## Usage

1.  After adding an Elmer solver as described [here](FEM_SolverElmer#Equations.md), select it in the [tree view](Tree_view.md).
2.  Either use the toolbar button <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:24px;"> or the menu **Solve → Electromagnetic Equations → Electricforce equation**.
3.  Now either use the toolbar button <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> or the menu **Solve → Electromagnetic Equations → [Electrostatic equation](FEM_EquationElectrostatic.md)**. This is important because the electricforce equation needs the potential field calculated by the Electrostatic equation.
4.  Change the [equation\'s solver settings](#Solver_Settings.md) or the [general solver settings](FEM_SolverElmer_SolverSettings.md) if necessary.

The electricforce equation only calculates the force for faces with a <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [electrostatic potential constraint](FEM_ConstraintElectrostaticPotential.md) if the constraint\'s option **Calculate Electric Force** is used.

## Solver Settings 

For the general solver settings, see the [Elmer solver settings](FEM_SolverElmer_SolverSettings.md).

The electricforce equation provides this special setting:

-    **Exec Solver**: By default the equation is only solved after a timestep passed. This means it is first solved after the solution of other equations converged. When the setting is *Always* the equation is solved after every iteration within a time step. (For [steady-state](FEM_SolverElmer_SolverSettings#Type.md) simulations the whole simulation is one time step.)

## Constraint Information 

The electricforce equation does not have own constraints. It takes the <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [electrostatic potential constraint](FEM_ConstraintElectrostaticPotential.md) from the <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> [Electrostatic equation](FEM_EquationElectrostatic.md). In the constraint it is important to use the option **Calculate Electric Force**.

## Result

The result is the electric force density in $\rm N/m^2$.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationElectricforce/pl
