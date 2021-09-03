---
- GuiCommand:/ru
   Name:Sketcher ConstrainPointOnObject
   Name/ru:Sketcher ConstrainPointOnObject
   MenuLocation:Sketch → Ограничения эскиза → Зафиксировать точку на объекте
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   Shortcut:**Shift** + **O**
   SeeAlso:[Ограничение коинциндентности](Sketcher_ConstrainCoincident/ru.md)
---

## Описание

Прикрепляет точку к другому объекту, вроде линии, дуги или оси эскиза.

## Использование


<div class="mw-translate-fuzzy">

1.  Выделите точку, которую Вы хотите прикрепить к линии, дуге и так далее (**Результат:** выделенная точка становится зелёной).
2.  Выделите линию, к которой Вы хотите прикрепить выделенную точку (**Результат:** выделенная точка становится зелёной).
    -   Нажмите на панели инструментов кнопку **<img src=images/Constraint_PointOnObject.svg style="width:24px">**.
    -   Используйте клавиатурное сокращение **Shift** + **O**.
    -   Используйте пункт верхнего меню **Sketch → Ограничения эскиза → Зафиксировать точку на объекте**.


</div>

**Примечание:** Порядок, в котором Вы выбираете линию и точку не важен. Точка всегда переносится на линию, линия остаётся на месте.

## Скрипты

Ограничения можно создавать макросами и в консоли python, используя следующие команды:


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Sketch`это объект эскиза.

-    `LineMoving`это номер, обозначающий линию, содержащую точку, которая будет передвинута на `LineFixed` (линию, которая останется на месте).

-    `PointOfLineMoving`это номер вершины линии `LineMoving`, которая будет передвинута на `LineFixed`.

-    `LinedFixed`это номер линии, к которой будет прикреплена точка `PointOfLineMoving`.

Страница [Sketcher scripting](Sketcher_scripting/ru.md) показывает, как узнать номер, определяющий линии и точки?


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}  
