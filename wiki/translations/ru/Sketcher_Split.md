---
 GuiCommand:
   Name/ru: Разделить ребро
   Name: Sketcher_Split
   MenuLocation: Sketch , Геометрия эскиза , Разделить ребро
   Workbenches: Sketcher_Workbench/ru
   Version: 0.20
   SeeAlso: Sketcher_Trimming/ru
---

# Sketcher Split/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Данный инструмент позволяет разделить ребро на две абсолютно одинаковые части, с сохранением большинства ограничений. Ограничения сохраняются для вновь созданных ребер, за исключением точки в которой произошло разделение. Окружность в случае её разделения, делится на дуги концы которых не связанны между собой, при этом ограничения которые имела окружность, переносятя на вновь созданные созданные дуги.


</div>



## Применение

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


<div class="mw-translate-fuzzy">

1.  Нажмите кнопку **[<img src=images/Sketcher_Split.svg style="width:16px"> [Разделить](Sketcher_Split.md)**. Указатель мыши примет форму белого перекрестия с значком разделения.
2.  Кликните на ребро в том месте, где вы хотите его разделить.
3.  Ребра в форме линии или дуги будут поделены на два новых фрагмента, соединенных точкой в месте разделения. Окружность будет разделена на дуги с той же центральной точкой и другими ограничениями, которые были у исходной окружности.
4.  Нажатие **Esc** или нажатие правой кнопки мыши завершит работу функции.


</div>



## Примечания

-   A [Coincident](Sketcher_ConstrainCoincident.md) constraint is applied to the center points of new arcs.
-   [Radius](Sketcher_ConstrainRadius.md) and [Diameter](Sketcher_ConstrainDiameter.md) constraints are copied to new arcs (resulting in a redundancy).
-   Coincident constraints and [Point on object](Sketcher_ConstrainPointOnObject.md) constraints are transferred to the closest new edge.
-   [Horizontal](Sketcher_ConstrainHorizontal.md) and [Vertical](Sketcher_ConstrainVertical.md) constraints between points are transferred to the closest new edge.
-   Horizontal and Vertical constraints attached to lines are copied to new line segments.
-   [Parallel](Sketcher_ConstrainParallel.md) and [Perpendicular](Sketcher_ConstrainPerpendicular.md) constraints are copied to new line segments, for new arcs they are only copied to the closest.
-   [Horizontal distance](Sketcher_ConstrainDistanceX.md), [Vertical distance](Sketcher_ConstrainDistanceY.md) and [Distance](Sketcher_ConstrainDistance.md) constraints are transferred to the closest new edge.
-   [Angle](Sketcher_ConstrainAngle.md), [Symmetric](Sketcher_ConstrainSymmetric.md) and [Block](Sketcher_ConstrainBlock.md) constraints are currently not transferred.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Split/ru
