---
- GuiCommand:/ru
   Name/ru:Создать линию
   Name:Sketcher_CreateLine
   MenuLocation:Sketch → Геометрия эскиза → Создать линию
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   Shortcut:**G** **L**
   SeeAlso:[Создать линию](Sketcher_CreatePolyline/ru.md)
---

# Sketcher CreateLine/ru

## Описание


<div class="mw-translate-fuzzy">

Данный инструмент позволят создать отрезок, по двум указанным точкам. При запуске инструмента указатель мыши меняется на белый крест с иконкой красной линии. Кроме того, координаты отображаются в режиме реального времени.


</div>

![](images/Sketcher_LineExample1.png‎ )


<div class="mw-translate-fuzzy">

Созданный объект линии начинается и заканчивается в заданных точках, но линия бесконечна относительно таких ограничений как [Касательная](Sketcher_ConstrainTangent/ru.md), [Точка на Объекте](Sketcher_ConstrainPointOnObject/ru.md) и [Внутренний угол](Sketcher_ConstrainAngle/ru.md). Это означает, например, что точка с ограничением [Точка на Объекте](Sketcher_ConstrainPointOnObject/ru.md) может не располагаться между двумя заданными точками, но может находиться за пределами двух точек на продолжении нарисованной линии.


</div>

## Применение


<div class="mw-translate-fuzzy">

-   Укажите точки на пустой области трехмерного вида, или на существующем объекте (авто ограничения в панели Задачи должны быть включены).
-   Нажмите **Esc** или правую кнопку мыши для отмены функции.


</div>





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateLine/ru
