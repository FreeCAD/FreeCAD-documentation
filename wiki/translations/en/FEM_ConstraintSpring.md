---
 GuiCommand:
   Name: FEM ConstraintSpring
   MenuLocation: Model , Mechanical boundary conditions and loads , Spring
   Workbenches: FEM_Workbench
   Shortcut: 
   Version: 0.20
   SeeAlso: 
---

# FEM ConstraintSpring/en

## Description

Defines a spring boundary condition to be used for mechanical analyses using the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer solver](FEM_SolverElmer.md).


<small>(v0.21)</small> 

: The spring constraint can be used for the equations <img alt="" src=images/FEM_EquationDeformation.svg  style="width:32px;"> [Deformation](FEM_EquationDeformation.md) and <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Elasticity](FEM_EquationElasticity.md).

## Usage

1.  Either use the toolbar button **<img src="images/FEM_ConstraintSpring.svg" width=16px> [Spring](FEM_ConstraintSpring.md)** or the menu **Model → Mechanical boundary conditions and loads → <img src="images/FEM_ConstraintSpring.svg" width=16px> Spring**.
2.  In the [3D view](3D_view.md) select the faces to which the spring should be applied.
3.  Specify the normal or tangential stiffness (in N/m) and select which one Elmer should use.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSpring/en
