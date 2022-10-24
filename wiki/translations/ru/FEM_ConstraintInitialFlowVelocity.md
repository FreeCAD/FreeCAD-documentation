---
- GuiCommand   */ru
   Name/ru   *Начальное условие скорости потока
   Name   *FEM_ConstraintInitialFlowVelocity
   MenuLocation   *Модель → Fluid Constraints → Начальное условие скорости потока
   Workbenches   *[FEM](FEM_Workbench/ru.md)
   SeeAlso   *[Граничное условие скорости потока](FEM_ConstraintFlowVelocity/ru.md)
---

# FEM ConstraintInitialFlowVelocity/ru


</div>

## Описание

Создает ограничение начальной скорости потока для анализа потока жидкости.

## Применение

1.  Either press the toolbar button **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> '''FEM ConstraintInitialFlowVelocity'''** or select the menu **Model → Fluid Constraints → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Constraint initial flow velocity**.
2.  Enter an initial flow velocity value for the analysis. The value is entered as a combination of the 3 main cartesian vectors components (X,Y,Z).
3.  For a 3D analysis, select a \'solid\' (body) from your model, for a 2D analysis select a face.


<div class="mw-translate-fuzzy">

## Ограничения


</div>


<div class="mw-translate-fuzzy">

-   Ограничение устанавливает начальную скорость потока ко всем узлам в модели метода конечных элементов.
-   Ограничение не может быть ориентировано иначе, чем с использованием главных декартовых компонентов.


</div>

## Примечания

В самых простых анализах нет необходимости указывать начальную скорость потока, однако это рекомендуется в порядке хорошего стиля работы.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialFlowVelocity/ru
