---
- GuiCommand   *
   Name   *FEM ConstraintInitialTemperature
   MenuLocation   *Model → Thermal Constraints → Constraint initial temperature
   Workbenches   *[FEM](FEM_Workbench.md)
   SeeAlso   *[FEM tutorial](FEM_tutorial.md)
---

# FEM ConstraintInitialTemperature/pl

## Description

Creates an initial temperature constraint for a thermo-mechanical analysis.

## Usage

1.  There are several ways to invoke the command   *
    -   Press the **<img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> [FEM ConstraintInitialTemperature](FEM_ConstraintInitialTemperature.md)** button.
    -   Select the **Model → Thermal Constraints → <img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> Constraint initial temperature** option from the menu.
2.  Enter an initial temperature value for the analysis.

## Limitations

This constraint applies the initial temperature to all nodes in the FEA model - it\'s not possible to select individual regions.

## Notes

-   This constraint uses the \*INITIAL CONDITIONS card in CalculiX. The initial temperature constraint is explained at <http   *//web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node215.html>





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialTemperature/pl
