---
- GuiCommand   *
   Name   *FEM ConstraintInitialFlowVelocity
   MenuLocation   *Model → Fluid Constraints → Constraint initial flow velocity
   Workbenches   *[FEM](FEM_Workbench.md)
   SeeAlso   *[FEM Constraint flow velocity](FEM_ConstraintFlowVelocity.md), [FEM Constraint initial pressure](FEM_ConstraintInitialPressure.md)
---

# FEM ConstraintInitialFlowVelocity

## Description

Creates an initial flow velocity constraint for a fluid flow analysis.

## Usage

1.  Either press the toolbar button **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> '''FEM ConstraintInitialFlowVelocity'''** or select the menu **Model → Fluid Constraints → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Constraint initial flow velocity**.
2.  Enter an initial flow velocity value for the analysis. The value is entered as a combination of the 3 main cartesian vectors components (X,Y,Z).
3.  For a 3D analysis, select a \'solid\' (body) from your model, for a 2D analysis select a face.

## Limitation

-   The constraint cannot be oriented other then using the main Cartesian components. This is a limitation of Elmer.

## Notes

In the most simple analyses, it is not necessary to specify the initial flow velocity, however it is recommended as best practice.




 {{FEM Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialFlowVelocity
