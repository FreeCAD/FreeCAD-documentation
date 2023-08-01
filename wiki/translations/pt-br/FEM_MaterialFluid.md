---
- GuiCommand:
   Name:FEM MaterialFluid
   MenuLocation:Model - Materials - Material for fluid
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM MaterialFluid/pt-br

## Descrição

Adds fluid properties to a part.

![](images/FEMMaterialFluidProperties.png ) 
*The FEM material task panel*

## Utilização

1.  To create a new MaterialFluid object do one of the following:
    -   Press the **<img src="images/FEM_MaterialFluid.svg" width=16px> [FEM MaterialFluid](FEM_MaterialFluid.md)** button.
    -   Select the **Model → Materials → <img src="images/FEM_MaterialFluid.svg" width=16px> Material for fluid‏‎** option from the menu.
2.  To edit an existing MaterialFluid object:
    -   Double-click it in the [Tree view](Tree_view.md).
3.  The FEM material task panel opens.
4.  Select a fluid type. For Computational Fluid Dynamics (CFD), **Air** or **Water** are typical options.
5.  Provided that you are applying fluid to the whole object, don\'t select any geometrical entities (leave reference list empty). Fluid will be applied to the whole model. Otherwise assign fluid to particular model domains manually by selecting some of them for each inserted material, if you do that, do not leave any domain of your model without fluid assigned.
6.  You can adjust fluid properties such as density, kinematic viscosity, thermal conductivity, etc., a few key fluids are already assigned in the list and they don\'t need any tweaking.
7.  If you make modifications, you can save your customized material.
8.  Press the **Close** button to close the task panel.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialFluid/pt-br
