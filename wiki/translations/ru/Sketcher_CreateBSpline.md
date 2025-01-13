---
 GuiCommand:
   Name/ru: Создать B-сплайн
   Name: Sketcher_CreateBSpline
   MenuLocation:  Sketch , Геометрия эскиза , Create B-Spline
   Workbenches:  Sketcher_Workbench/ru
   Version: 0.17
   SeeAlso: Sketcher_CreatePeriodicBSpline/ru
---

# Sketcher CreateBSpline/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Этот инструмент рисует незамкнутую кривую B-сплайна по его контрольным точкам.


</div>

![](images/Sketcher_CreateBSpline_Example.png )


<div class="mw-translate-fuzzy">

*Кривая B-сплайна построена по 4 точкам (белого цвета). На рисунке изображены контрольные многоугольники зеленым цветом (прямые, соединяющие красные точки), синие круги с весами и гребень кривизны зеленым цветом. Цифра (3) в центре относится к степени B-сплайна, а цифры (4) на концах кривой относятся к множественности их узлов.*


</div>



## Применение

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


<div class="mw-translate-fuzzy">

1.  Нажмите кнопку **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [B-сплайн](Sketcher_CreateBSpline.md)**.
2.  Создайте серию точек, нажимая в 3D-виде. Пока команда активна, созданные точки соединяются прямыми линиями, и вокруг каждой точки создается круг вспомогательной геометрии.
3.  Нажмите правую кнопку мыши, чтобы завершить ввод и сгенерировать кривую.
4.  В зависимости от настроек инструмент может оставаться активным, чтобы нарисовать новую кривую. Нажмите правую кнопку мыши еще раз, чтобы завершить команду.

-   Можно переопределить вес контрольных точек, изменив радиусы кругов вспомогательной геометрии. Для этого сначала удалите ограничения равенства на кругах. Ограничьте радиусы произвольно, вес контрольных точек будет определяться относительными радиусами окружностей. Это работает подобно гравитации: чем больше круг по отношению к другим, тем больше кривая будет притягиваться к контрольной точке.
-   Видимость управляющего полигона, гребня кривизны, степени и множества узлов можно включать/выключать с помощью панели инструментов [Инструменты B-сплайна](Sketcher_Workbench/ru#Sketcher_B-spline_tools.md).
-   Изучите другие инструменты на панели инструментов [Инструменты B-сплайна](Sketcher_Workbench/ru#Sketcher_B-spline_tools.md), чтобы узнать о них больше.


</div>

## Notes

-   Elements of the internal geometry can be deleted. They can be recreated at any time with [Sketcher RestoreInternalAlignmentGeometry](Sketcher_RestoreInternalAlignmentGeometry.md).
-   After a B-spline is created, it is possible to define the weight of the control points by changing the radii of the weight circles. The equality constraints on the circles need to be deleted first. The radius constraint is arbitrary, the weight of the control points will be defined by the relative radii of the circles. It works similar to gravity: the bigger a circle is in relation to the others, the more the curve will be attracted to that control point.
-   The degree of a created B-spline can be [increased](Sketcher_BSplineIncreaseDegree.md) or [decreased](Sketcher_BSplineDecreaseDegree.md), and the multiplicity of its knots can be [increased](Sketcher_BSplineIncreaseKnotMultiplicity.md) or [decreased](Sketcher_BSplineIncreaseKnotMultiplicity.md) as well.
-   The visibility of the [degree](Sketcher_BSplineDegree.md), the [control polygon](Sketcher_BSplinePolygon.md), the [curvature comb](Sketcher_BSplineComb.md), the [knot multiplicity](Sketcher_BSplineKnotMultiplicity.md) and the [control point weight](Sketcher_BSplinePoleWeight.md) can be toggled on/off from the [Sketcher visual](Sketcher_Workbench#Sketcher_visual.md) toolbar.



## Ограничения


<div class="mw-translate-fuzzy">

-   В настоящее время не поддерживается большое количество ограничений. Могут быть ограничены только контрольные точки и конечные точки B-сплайна.
-   Инструменты [Обрезать](Sketcher_Trimming/ru.md) и [Продлить](Sketcher_Extend/ru.md) не поддерживаются.
-   Форма кривой B-сплайна может быть отредактирована только путем перетаскивания одной из контрольных точек. Узлы, лежащие на кривой, не могут быть выбраны.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateBSpline/ru
