---
 GuiCommand:
   Name/ru: Эллиптическая дуга
   Name: Sketcher_CreateArcOfEllipse
   MenuLocation: Sketch , Геометрия эскиза , Эллиптическая дуга
   Workbenches: Sketcher_Workbench/ru
   Shortcut: **G** **E** **A**
   Version: 0.15
   SeeAlso: Sketcher_CreateEllipseByCenter/ru, Sketcher_CompCreateArc/ru
---

# Sketcher CreateArcOfEllipse/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Этот инструмент рисует дугу по эллипсу, по четырем указанным точкам: центральной, большому радиусу, начальной и конечной точкам. При запуске инструмента указатель мыши меняется на белый крест с красным значком дуги по эллипсу. Кроме того, координаты отображаются в режиме реального времени.


</div>

![](images/Sketcher_CreateArcOfEllipse_Example.png ) 
*Arc of ellipse (white) with internal geometry (dark yellow)*



## Применение

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


<div class="mw-translate-fuzzy">

-   Нажмите кнопку **[<img src=images/Sketcher_CreateArcOfEllipse.svg style="width:16px"> [Дуга по эллипсу](Sketcher_CreateArcOfEllipse.md)**.
-   Первым нажатием в 3D виде задайте точку центра эллипса. Вторым нажатием задайте первый радиус и ориентацию эллипса. Третьим нажатием задайте другой радиус и начало дуги. Четвертым нажатием задайте конец дуги.
-   После четвертого нажатия создается дуга по эллипсу вместе с набором вспомогательной геометрии, привязанной к нему (большой диаметр, малый диаметр, два фокуса). Вспомогательная геометрия может быть удалена вручную, если не нужна, и воссоздана позже. Смотрите [Sketcher Показать Скрытую Внутреннюю Геометрию](Sketcher_RestoreInternalAlignmentGeometry/ru.md).
-   Нажатие **ESC** или правой кнопки мыши отменяет функцию.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Особенности

-   Большая и малая оси эллипсов являются строго определенными и не могут быть поменяны путем изменения размера эллипса. Что бы поменять оси местами, необходимо вращать лежащий в основе эллипс.
-   В отличие от эллипса, который может быть ограничен до круга, дуга эллипса не может стать дугой круга.
-   Перемещение эллипса за ребро - это то же самое, что перемещение эллипса за центр.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfEllipse/ru
