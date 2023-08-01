---
- GuiCommand:
   Name/ru:Ограничить точку на объекте
   Name:Sketcher_ConstrainPointOnObject
   MenuLocation:Sketch - Ограничения эскиза - Ограничить точку на объекте
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   Shortcut:**O**
   SeeAlso:[Ограничение пересечения](Sketcher_ConstrainCoincident/ru.md)
---

# Sketcher ConstrainPointOnObject/ru



## Описание

Прикрепляет точку к таким объектам как: линия, дуга или ось эскиза.



## Применение


<div class="mw-translate-fuzzy">

1.  Выделите точку, которую Вы хотите прикрепить к линии, дуге и так далее (**Результат:** выделенная точка становится зелёной).
2.  Выделите линию, к которой Вы хотите прикрепить выделенную точку (**Результат:** выделенная точка становится зелёной).
    -   Нажмите на панели инструментов кнопку **[<img src=images/Sketcher_ConstrainPointOnObject.svg style="width:16px"> [Зафиксировать точку на объекте](Sketcher_ConstrainPointOnObject/ru.md)**.
    -   Используйте клавиатурное сокращение **Shift** + **O**.
    -   Используйте пункт верхнего меню **Sketch → Ограничения эскиза → Зафиксировать точку на объекте**.


</div>



## Программирование

Ограничения можно создавать с помощью [макросов](Macros/ru.md) и в консоли [Python](Python/ru.md), используя следующие команды:


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Sketch`это объект эскиза.

-    `LineMoving`это номер, обозначающий линию, содержащую точку, которая будет передвинута на `LineFixed` (линию, которая останется на месте).

-    `PointOfLineMoving`это номер вершины линии `LineMoving`, которая будет передвинута на `LineFixed`.

-    `LinedFixed`это номер линии, к которой будет прикреплена точка `PointOfLineMoving`.

Страница [Sketcher scripting](Sketcher_scripting/ru.md) показывает, как узнать номер, определяющий линии и точки?





{{Sketcher Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/ru
