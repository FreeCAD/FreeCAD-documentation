---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ConstraintInitialPressure
   MenuLocation: Model , Fluid boundary conditions , Initial pressure condition
   Workbenches: FEM_Workbench
   Version: 0.21
   SeeAlso: FEM_ConstraintInitialFlowVelocity
}}
{{GuiCommandFemInfo
   Solvers: Elmer
}}
---

# FEM ConstraintInitialPressure

## Description

Creates an initial pressure condition for a fluid flow analysis.

## Usage

1.  Press the **<img src="images/FEM_ConstraintInitialPressure.svg" width=16px> [Initial pressure condition](FEM_ConstraintInitialPressure.md)** button or select the menu **Model → Fluid boundary conditions → <img src="images/FEM_ConstraintInitialPressure.svg" width=16px> Initial pressure condition**.
2.  Enter an initial pressure value.
3.  For a 3D analysis, select a \'solid\' (body) from your model, for a 2D analysis select a face.

## Notes

For simple analyses, it is not necessary to specify the initial pressure, however also in these cases it is recommended as best practice.




 {{FEM Tools navi}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialPressure
