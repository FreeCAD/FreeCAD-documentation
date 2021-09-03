---
- GuiCommand:/ru
   Name:FEM MaterialMechanicalNonlinear
   Name/ru:FEM MaterialMechanicalNonlinear
   MenuLocation: Model → Nonlinear mechanical material
   Workbenches:[FEM](FEM_Workbench/ru.md)
   Shortcut:
   SeeAlso:[FEM tutorial](FEM_tutorial/ru.md)
---


</div>

## Описание

Adds nonlinear mechanical material model. Currently only plasticity with simple hardening is available.

## Использование

1.  To define nonlinear mechanical material model do the following:
    -   Add the **<img src="images/Fem-add-material.svg" width=16px> [MaterialSolid](FEM_MaterialSolid.md)** first and select it.
    -   Click the **<img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> [FEM MaterialMechanicalNonlinear](FEM_MaterialMechanicalNonlinear.md)** button or choose the {{MenuCommand|Model → Materials → <img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> Nonlinear mechanical material‏‎}} option from the menu.
2.  To edit an existing MaterialFluid object:
    -   Click it in the [Tree view](Tree_view.md).
    -   Select the material model (currently only simple hardening is available).
    -   Define yield points (stress vs plastic strain). The first point must have a zero plastic strain specified. Currently only 3 yield points can be defined.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}  
