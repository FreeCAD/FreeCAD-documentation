---
 GuiCommand:
   Name: FEM ConstraintInitialFlowVelocity
   MenuLocation: Model , Fluid boundary conditions , Initial flow velocity condition
   Workbenches: FEM_Workbench
   SeeAlso: FEM_ConstraintFlowVelocity, FEM_ConstraintInitialPressure
---

# FEM ConstraintInitialFlowVelocity

## Description

Creates an initial flow velocity condition for a fluid flow analysis.

## Usage

1.  Press the **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> [Initial flow velocity condition](FEM_ConstraintInitialFlowVelocity.md)** button or select the menu **Model → Fluid boundary conditions → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Initial flow velocity condition**.
2.  Enter an initial flow velocity value for the analysis. The value is entered as a combination of the 3 main cartesian vectors components (X,Y,Z).
3.  For a 3D analysis, select a \'solid\' (body) from your model, for a 2D analysis select a face. However, it is also possible to select a face (e.g. the inlet of a pipe) in 3D or an edge in 2D.

## Formulas

For a description how to input formulas, see section *Formulas* in the page for the [Flow velocity constraint](FEM_ConstraintFlowVelocity#Formulas.md).

## Notes

In simple analyses, it is not necessary to specify the initial flow velocity, however it is recommended as best practice.




 {{FEM Tools navi}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialFlowVelocity
