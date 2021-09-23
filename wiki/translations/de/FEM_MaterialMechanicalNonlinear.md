---
- GuiCommand:
   Name:FEM MaterialMechanicalNonlinear
   MenuLocation:Model → Materials → Nonlinear mechanical material
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM MaterialMechanicalNonlinear/de

## Beschreibung

Adds nonlinear mechanical material model. Currently only plasticity with simple hardening is available.

## Anwendung

1.  To define nonlinear mechanical material model do the following:
    -   Add the **<img src="images/Fem-add-material.svg" width=16px> [MaterialSolid](FEM_MaterialSolid.md)** first and select it.
    -   Click the **<img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> [FEM MaterialMechanicalNonlinear](FEM_MaterialMechanicalNonlinear.md)** button or choose the **Model → Materials → <img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> Nonlinear mechanical material‏‎** option from the menu.
2.  To edit an existing MaterialFluid object:
    -   Click it in the [Tree view](Tree_view.md).
    -   Select the material model (currently only simple hardening is available).
    -   Define yield points (stress vs plastic strain). The first point must have a zero plastic strain specified. Currently only 3 yield points can be defined.





{{FEM Tools navi

}}

---
[documentation index](../README.md) > FEM MaterialMechanicalNonlinear/de
