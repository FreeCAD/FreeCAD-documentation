---
- GuiCommand:
   Name:FEM ConstraintInitialFlowVelocity
   MenuLocation:Model → Fluid Constraints → Constraint initial flow velocity
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM Constraint flow velocity](FEM_ConstraintFlowVelocity.md)
---

# FEM ConstraintInitialFlowVelocity/pl

## Description

Creates an initial flow velocity constraint for a fluid flow analysis.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> [FEM ConstraintInitialFlowVelocity](FEM_ConstraintInitialFlowVelocity.md)** button.
    -   Select the **Model → Fluid Constraints → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Constraint initial flow velocity** option from the menu.
2.  Enter an initial flow velocity value for the analysis.
3.  The value is entered as a combination of the 3 main cartesian vectors components (X,Y,Z).

## Limitations

-   The constraint applies the initial flow velocity to all nodes in the FEA model.
-   The constraint cannot be oriented other then using the main cartesian components.

## Notes

In the most simple analyses, it is not necessary to specify the initial flow velocity, however it is recommended as best practice.





{{FEM Tools navi

}}

---
[documentation index](../README.md) > FEM ConstraintInitialFlowVelocity/pl
