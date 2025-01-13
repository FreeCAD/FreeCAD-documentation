---
 GuiCommand:
   Name: FEM MaterialFluid
   Name/ru: FEM MaterialFluid
   MenuLocation:  Model , Material for fluid
   Workbenches: FEM_Workbench/ru
   Shortcut: 
   SeeAlso: FEM_tutorial/ru
---

# FEM MaterialFluid/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Добавляет свойства жидкости к детали.


</div>

![](images/FEMMaterialFluidProperties.png ) 
*Внешний вид панели материалов верстака МКЭ*



## Применение

1.  To create a new MaterialFluid object do one of the following:
    -   Press the **<img src="images/FEM_MaterialFluid.svg" width=16px> [Material for fluid](FEM_MaterialFluid.md)** button.
    -   Select the **Model → Materials → <img src="images/FEM_MaterialFluid.svg" width=16px> Material for fluid‏‎** option from the menu.
2.  To edit an existing MaterialFluid object:
    -   Double-click it in the [Tree view](Tree_view.md).
3.  The FEM material task panel opens.
4.  Select a fluid material from the drop-down list. For Computational Fluid Dynamics (CFD), *Air* or *Water* are common options.
5.  Optionally, press the **Use this task panel** button to modify material properties such as density, kinematic viscosity, thermal conductivity, etc.
6.  Provided you are applying fluid to the whole object, don\'t select any geometrical entities (leave the reference list empty). Fluid will be applied to the whole model. Otherwise assign fluid to particular model domains manually by selecting some of them for each inserted material, if you do that, do not leave any domain of your model with no fluid assigned.
7.  Press the **Close** button to close the task panel.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialFluid/ru
