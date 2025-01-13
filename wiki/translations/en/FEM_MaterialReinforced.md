---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM MaterialReinforced
   MenuLocation:  Model , Materials , Reinforced material 
   Workbenches: FEM_Workbench
   SeeAlso: FEM_tutorial
}}
{{GuiCommandFemInfo
   Solvers: CalculiX
}}
---

# FEM MaterialReinforced/en

## Description

Creates a reinforced matrix material. It combines a matrix material (e.g. concrete) and a reinforcement material (e.g. steel).

## Usage

1.  To create a new MaterialReinforced object do the following:
    -   Click the **<img src="images/FEM_MaterialReinforced.svg" width=16px> [Reinforced material (concrete)](FEM_MaterialReinforced.md)** button or choose the **Model → Materials → <img src="images/FEM_MaterialReinforced.svg" width=16px> Reinforced material (concrete)‏‎** option from the menu.
2.  To edit an existing MaterialReinforced object:
    -   Double-click it in the [Tree view](Tree_view.md).
3.  Select the matrix material.
4.  Optionally press the **Edit** button to edit its properties. The following material properties have to be defined: Young\'s modulus, Poisson\'s ratio, compressive strength and angle of friction.
5.  Select the reinforcement material.
6.  Optionally press the **Edit** button to edit its properties. A yield strength has to be defined.

## Notes

-   In the CalculiX solver settings, one has to set Material Nonlinearity to linear if [FEM MaterialMechanicalNonlinear](FEM_MaterialMechanicalNonlinear.md) is not used.
-   More information about this feature, and an example of its usage, can be found in [Analysis of reinforced concrete with FEM](Analysis_of_reinforced_concrete_with_FEM.md).
-   For a video tutorial (based on the [FEM Tutorial](FEM_tutorial.md)) that uses this tool, watch: [FEM MaterialReinforced tutorial](https://www.youtube.com/watch?v=SZTIqhfCSVc).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialReinforced/en
