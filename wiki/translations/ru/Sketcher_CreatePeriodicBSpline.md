---
 GuiCommand:
   Name/ru: Создать периодический B-сплайн
   Name: Sketcher_CreatePeriodicBSpline
   MenuLocation:  Sketch , Геометрия эскиза , Создать периодический B-сплайн
   Workbenches: Sketcher_Workbench/ru
   Version: 0.17
   SeeAlso: Sketcher_CreateBSpline/ru
---

# Sketcher CreatePeriodicBSpline/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Этот инструмент рисует периодическую (замкнутую) кривую B-сплайна по его контрольным точкам.


</div>

![](images/Sketcher_Periodic_B-spline_example01.png )


<div class="mw-translate-fuzzy">

*Периодическая кривая B-сплайна (белого цвета) состоит из 5 точек. На рисунке изображены: контрольный многоугольник зеленого цвета (прямые, соединяющие красные точки), синие круги с весом и гребень кривизны зеленым цветом. Цифра (3) в центре относится к степени B-сплайна, а цифры (1) и (2) на узлах, лежащих на кривой, относятся к их множественности.*


</div>



## Применение


<div class="mw-translate-fuzzy">

1.  Нажмите кнопку **[<img src=images/Sketcher_CreatePeriodicBSpline.svg style="width:16px"> [Нарисовать периодический B-сплайн](Sketcher_CreatePeriodicBSpline/ru.md)**.
2.  Создайте серию точек, нажимая в 3D-виде. Пока команда активна, созданные точки соединяются прямыми линиями, и вокруг каждой точки создается круг вспомогательной геометрии.
3.  Нажмите правую кнопку мыши, чтобы завершить ввод и сгенерировать кривую.
4.  В зависимости от настроек инструмент может оставаться активным, чтобы нарисовать новую кривую. Нажмите правую кнопку мыши еще раз, чтобы завершить команду.

-   Можно переопределить вес контрольных точек, изменив радиусы кругов вспомогательной геометрии. Для этого сначала удалите ограничения равенства на кругах. Ограничьте радиусы произвольно, вес контрольных точек будет определяться относительными радиусами окружностей. Это работает подобно гравитации: чем больше круг по отношению к другим, тем больше кривая будет притягиваться к контрольной точке.
-   Видимость управляющего полигона, гребня кривизны, степени и множества узлов можно включать/выключать с помощью панели инструментов [Инструменты B-сплайна](Sketcher_Workbench/ru#Sketcher_B-spline_tools.md).
-   Изучите другие инструменты на панели инструментов [Инструменты B-сплайна](Sketcher_Workbench/ru#Sketcher_B-spline_tools.md), чтобы узнать о них больше.


</div>

## Notes

See [Sketcher CreateBSpline](Sketcher_CreateBSpline#Notes.md).



## Ограничения

See [Sketcher CreateBSpline](Sketcher_CreateBSpline#Limitations.md).


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePeriodicBSpline/ru
