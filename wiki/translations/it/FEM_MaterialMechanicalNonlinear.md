# FEM MaterialMechanicalNonlinear/it
---
- GuiCommand   */it   Name   *FEM_MaterialMechanicalNonlinear   Name/it   *FEM Materiale non lineare   MenuLocation   * Modello → Materiale non lineare   |Workbenches   *[Shortcut   *   SeeAlso   *[[FEM_tutorial/it|Tutorial FEM](FEM_Workbench/it___FEM]].md)---

## Descrizione

Adds nonlinear mechanical material model. Currently only plasticity with simple hardening is available.

## Utilizzo

1.  To define nonlinear mechanical material model do the following   *
    -   Add the **<img src="images/Fem-add-material.svg" width=16px> [MaterialSolid](FEM_MaterialSolid.md)** first and select it.
    -   Click the **<img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> [FEM MaterialMechanicalNonlinear](FEM_MaterialMechanicalNonlinear.md)** button or choose the **Model → Materials → <img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> Nonlinear mechanical material‏‎** option from the menu.
2.  To edit an existing MaterialMechanicalNonlinear object   *
    -   Click it in the [Tree view](Tree_view.md).
    -   Select the material model (currently only simple hardening is available).
    -   Define yield points (stress vs plastic strain). The first point must have a zero plastic strain specified.

## Notes

-   In FreeCAD 0.19 and older versions, it\'s possible to specify only 3 yield points. Since the 0.20 version, this limitation doesn\'t exist and a list of yield point can contain as many of them as needed.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialMechanicalNonlinear/it
