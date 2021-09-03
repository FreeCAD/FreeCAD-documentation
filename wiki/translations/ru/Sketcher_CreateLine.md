---
- GuiCommand:/ru
   Name:Sketcher CreateLine
   Name/ru:Sketcher CreateLine
   MenuLocation:Эскиз → Геометрия эскиза → Создать линию
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   Shortcut:L
   SeeAlso:[Sketcher Polyline](Sketcher_CreatePolyline/ru.md)
---

## Описание

Этот инструмент рисует линию, в качестве основы выбирая две точки в 3D-виде. При запуске инструмента указатель мыши меняется на белый крест с иконкой красной линии. Кроме того, координаты отображаются в режиме реального времени.

![](images/Sketcher_LineExample1.png‎ )


<div class="mw-translate-fuzzy">

Созданный объект линии начинается и заканчивается в заданных точках, но линия бесконечна относительно таких ограничений как [Касательная](Sketcher_ConstrainTangent/ru.md), [Точка на Объекте](Sketcher_ConstrainPointOnObject/ru.md) и [Внутренний угол](Sketcher_ConstrainAngle/ru.md). Это означает, например, что точка с ограничением [Точка на Объекте](Sketcher_ConstrainPointOnObject/ru.md) может не располагаться между двумя заданными точками, но может находиться за пределами двух точек на продолжении нарисованной линии.


</div>

## Использование

-   Укажите точки на пустой области трехмерного вида, или на существующем объекте (авто ограничения в панели Задачи должны быть включены).
-   Нажмите **Esc** или правую кнопку мыши для отмены функции.





{{Sketcher Tools navi

}}  
