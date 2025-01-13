---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM MaterialMechanicalNonlinear
   MenuLocation: Model , Materials , Nonlinear mechanical material
   Workbenches: FEM_Workbench
   SeeAlso: FEM_tutorial
}}
{{GuiCommandFemInfo
   Solvers: CalculiX
}}
---

# FEM MaterialMechanicalNonlinear

## Description

Creates a nonlinear mechanical material. Currently, only plasticity with simple (isotropic) hardening is available. <small>(v1.0)</small> : Kinematic hardening is also available.

## Usage

1.  To create a new MaterialMechanicalNonlinear object do the following:
    -   Add a **<img src="images/FEM_MaterialSolid.svg" width=16px> [Material for solid](FEM_MaterialSolid.md)** first and select it.
    -   Click the **<img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> [Nonlinear mechanical material](FEM_MaterialMechanicalNonlinear.md)** button or choose the **Model → Materials → <img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> Nonlinear mechanical material‏‎** option from the menu.
2.  To edit an existing MaterialMechanicalNonlinear object:
    -   Select it in the [Tree view](Tree_view.md).
    -   Select the material model (isotropic (simple) hardening or <small>(v1.0)</small> : kinematic hardening).
    -   Define yield points (stress \[MPa\] vs plastic strain). The first point must have a zero plastic strain. Press the **...** button next to **Yield Points** to input the points using a user-friendly list. The syntax is described in the [Notes](#Notes.md) section.

## Notes

-   In FreeCAD 0.19 and older versions, only 3 yield points can be specified. Since version 0.20 a list of yield points can contain as many as required.
-   The syntax should be:



:   
    
```python
    stress_1, 0
    stress_2, plastic_strain_2
    ...
    
```
    



:   With dot as the decimal separator since that\'s what CalculiX uses.





:   For example to define a bilinear model with hardening for S275 steel:



:   
    
```python
    275, 0
    490, 0.2
    
```
    



:   Or, to define perfect plasticity with no hardening for this material:



:   
    
```python
    275, 0
    
```
    






 {{FEM Tools navi}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialMechanicalNonlinear
