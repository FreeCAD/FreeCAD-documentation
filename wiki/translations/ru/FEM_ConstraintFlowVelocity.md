---
- GuiCommand   */ru
   Name   *FEM ConstraintFlowVelocity
   Name/ru   *FEM ConstraintFlowVelocity
   Icon   *Fem-constraint-flow-velocity.svg
   MenuLocation   * Model → Fluid constraints → Constraint flow velocity
   Workbenches   *[FEM](FEM_Workbench/ru.md)
   Shortcut   *
   SeeAlso   *[FEM tutorial](FEM_tutorial/ru.md)
---

# FEM ConstraintFlowVelocity/ru


</div>

## Описание

Устанавливает скорость потока в качестве граничного условия к ребру в 2D или к грани в 3D.

<img alt="" src=images/FEM-constraint-flow-velocity_task-panel.png  style="width   *400px;"> 
*Constraint flow velocity menus within the [task panel](Task_panel.md)*

## Применение

1.  There are several ways to invoke the command   *
    -   Press the **<img src="images/FEM_ConstraintFlowVelocity.svg" width=16px> [FEM ConstraintFlowVelocity](FEM_ConstraintFlowVelocity.md)** button.
    -   Select the **Model → Fluid Constraints → <img src="images/FEM_ConstraintFlowVelocity.svg" width=16px> Constraint flow velocity** option from the menu.
2.  The [task panel](Task_panel.md) will display menus for constraint flow velocity
3.  Select the target Edges or Faces.
4.  Press the **Add** button.
5.  Deselect \"unspecified\" to activate the necessary fields for edition.
6.  Fill in the values in mm/s for the main Cartesian components.

## Примечания

-   Компоненты вектора, отмеченные как *не указана*, будут интерполированы выбранным решателем.

       *   Любой вектор, который должен быть результатом решателя, должен быть помечен как *не указана*.
-   Если целевая грань или ребро не выровнены с основной декартовой системой координат, можно поставить галочку *нормаль к границе*.

       *   Если установлен флажок *нормаль к границе*, вектор нормали к выбранному ребру или грани равен X, и он будет ориентирован от области сетки.
       *   Например, если в домен должен поступать поток воздуха со скоростью 20 мм/с, то после отметки *нормаль к границе* пользователь должен будет ввести -20 мм/с в поле *скорость X*.

-   For a Wall with non-slip condition, the flow will be (0,0,0).
-   For a Symmetry condition, the flow will be (0, Unspecified, Unspecified) if \"normal to boundary\" is ticked.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintFlowVelocity/ru
