---
- GuiCommand:
   Name/ru: Ограничить вращение плоскости
   Name: FEM_ConstraintPlaneRotation
   MenuLocation: Модель -> Geometrical Constraints -> Ограничить вращение плоскости
   Workbenches: FEM_Workbench/ru
   SeeAlso: FEM_ConstraintTransform/ru
---

# FEM ConstraintPlaneRotation/ru

## Описание

Создает ограничение FEM для хранения узлов на плоской поверхности в одной плоскости.

## Применение


<div class="mw-translate-fuzzy">

1.  Нажмите на <img alt="" src=images/FEM_ConstraintPlaneRotation.png  style="width:32px;"> или выберите **Model** → **Механические ограничения** → **<img src="images/FEM_ConstraintPlaneRotation.png" width=32px> Вращение плоскости ограничения** из верхнего меню.
2.  Выберите в [трёхмерном виде](3D_view/ru.md) объект, к которому должно применяться ограничение, которое может быть гранью.


</div>

## Ограничения


<div class="mw-translate-fuzzy">

1.  Ограничение вращения полосы может применяться только к одной плоской грани.
2.  Когда ограничение вращения плоскости применяется к той же самой грани, что и смещение / фиксированное ограничение, предпочтение смещения / фиксирования ограничено.


</div>

## Примечания


<div class="mw-translate-fuzzy">

1.  Ограничение использует в CalculiX карту \*MPC. Ограничения расчёта теплопередачи описаны в <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node220.html>


</div>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPlaneRotation/ru
