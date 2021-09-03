---
- GuiCommand:/ru
   Name:FEM ConstraintInitialFlowVelocity
   Name/ru:FEM ConstraintInitialFlowVelocity
   Icon:Fem-constraint-initial-flow-velocity.svg
   MenuLocation: Model → Fluid constraints → Constraint initial flow velocity
   Workbenches:[FEM](FEM_Workbench/ru.md)
   Shortcut:
   SeeAlso:[FEM tutorial](FEM_tutorial/ru.md)
---


</div>

## Описание

Создает ограничение начальной скорости потока для анализа потока жидкости.

## Использование

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> [FEM ConstraintInitialFlowVelocity](FEM_ConstraintInitialFlowVelocity.md)** button.
    -   Select the **Model → Fluid Constraints → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Constraint initial flow velocity** option from the menu.
2.  Enter an initial flow velocity value for the analysis.
3.  The value is entered as a combination of the 3 main cartesian vectors components (X,Y,Z).

## Ограничения

-   Ограничение устанавливает начальную скорость потока ко всем узлам в модели метода конечных элементов.
-   Ограничение не может быть ориентировано иначе, чем с использованием главных декартовых компонентов.

## Примечания

В самых простых анализах нет необходимости указывать начальную скорость потока, однако это рекомендуется в порядке хорошего стиля работы.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}  
