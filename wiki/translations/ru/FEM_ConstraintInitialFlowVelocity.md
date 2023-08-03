---
 GuiCommand:
   Name/ru: Начальное условие скорости потока
   Name: FEM_ConstraintInitialFlowVelocity
   MenuLocation: Модель , Fluid Constraints , Начальное условие скорости потока
   Workbenches: FEM_Workbench/ru
   SeeAlso: FEM_ConstraintFlowVelocity/ru
---

# FEM ConstraintInitialFlowVelocity/ru


</div>



## Описание

Создает ограничение начальной скорости потока для анализа потока жидкости.



## Применение

1.  Either press the toolbar button **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> '''FEM ConstraintInitialFlowVelocity'''** or select the menu **Model → Fluid Constraints → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Constraint initial flow velocity**.
2.  Enter an initial flow velocity value for the analysis. The value is entered as a combination of the 3 main cartesian vectors components (X,Y,Z).
3.  For a 3D analysis, select a \'solid\' (body) from your model, for a 2D analysis select a face. However, it is also possible to select a face (e.g. the inlet of a pipe) in 3D or an edge in 2D.

## Formulas

For a description how to input formulas, see section *Formulas* in the page for the [Flow velocity constraint](FEM_ConstraintFlowVelocity#Formulas.md).



## Примечания


<div class="mw-translate-fuzzy">

В самых простых анализах нет необходимости указывать начальную скорость потока, однако это рекомендуется в порядке хорошего стиля работы.


</div>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialFlowVelocity/ru
