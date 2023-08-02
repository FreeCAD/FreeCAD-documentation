---
- GuiCommand:
   Name: FEM SolverCalculiX
   MenuLocation: Solve -> Solver CalculiX 
   Workbenches: FEM_Workbench
   Shortcut: **S** **C**
   SeeAlso: FEM_CalculiX, FEM_tutorial
---

# FEM SolverCalculiX/pl

## Description

The **Solver CalculiX (new framework)** command creates a SolverCalculix object, which uses the same framework as Elmer and Z88 solvers (the code is not visible for the user). It is preferred to use the original framework <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Solver CalculiX Standard](FEM_SolverCalculixCxxtools.md) because it contains extra checks, e.g. showing the elements with nonpositive Jacobian which might cause solution difficulties.

## Usage

1.  Select **Solve → <img src="images/FEM_SolverCalculiX.svg" width=16px> Solver CalculiX (new framework)** from the menu.

## Related

-   [FEM CalculiX](FEM_CalculiX.md)





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverCalculiX/pl
