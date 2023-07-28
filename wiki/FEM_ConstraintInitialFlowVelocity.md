---
- GuiCommand:
   Name:FEM ConstraintInitialFlowVelocity
   MenuLocation:Model → Fluid Constraints → Constraint initial flow velocity
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[Constraint flow velocity](FEM_ConstraintFlowVelocity.md), [Constraint initial pressure](FEM_ConstraintInitialPressure.md)
---

# FEM ConstraintInitialFlowVelocity

## Description

Creates an initial flow velocity constraint for a fluid flow analysis.

## Usage

1.  Either press the toolbar button **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> '''FEM ConstraintInitialFlowVelocity'''** or select the menu **Model → Fluid Constraints → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Constraint initial flow velocity**.
2.  Enter an initial flow velocity value for the analysis. The value is entered as a combination of the 3 main cartesian vectors components (X,Y,Z).
3.  For a 3D analysis, select a \'solid\' (body) from your model, for a 2D analysis select a face. However, it is also possible to select a face (e.g. the inlet of a pipe) in 3D or an edge in 2D.

## Formulas

For a description how to input formulas, see section *Formulas* in the page for the [Flow velocity constraint](FEM_ConstraintFlowVelocity#Formulas.md).

## Notes

In simple analyses, it is not necessary to specify the initial flow velocity, however it is recommended as best practice.




 {{FEM Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialFlowVelocity
