---
 GuiCommand:
   Name/ru: Ограничить точку на объекте
   Name: Sketcher_ConstrainPointOnObject
   MenuLocation: Sketch , Ограничения эскиза , Ограничить точку на объекте
   Workbenches: Sketcher_Workbench/ru
   Shortcut: **O**
   SeeAlso: Sketcher_ConstrainCoincident/ru
---

# Sketcher ConstrainPointOnObject/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Прикрепляет точку к таким объектам как: линия, дуга или ось эскиза.


</div>


<small>(v1.0)</small> 

: This tool is replaced by the [Sketcher ConstrainCoincidentUnified](Sketcher_ConstrainCoincidentUnified.md) tool if the **Unify Coincident and PointOnObject** option is selected in the [preferences](Sketcher_Preferences#General.md).



## Применение

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 


<div class="mw-translate-fuzzy">

1.  Выделите точку, которую Вы хотите прикрепить к линии, дуге и так далее (**Результат:** выделенная точка становится зелёной).
2.  Выделите линию, к которой Вы хотите прикрепить выделенную точку (**Результат:** выделенная точка становится зелёной).
    -   Нажмите на панели инструментов кнопку **[<img src=images/Sketcher_ConstrainPointOnObject.svg style="width:16px"> [Зафиксировать точку на объекте](Sketcher_ConstrainPointOnObject/ru.md)**.
    -   Используйте клавиатурное сокращение **Shift** + **O**.
    -   Используйте пункт верхнего меню **Sketch → Ограничения эскиза → Зафиксировать точку на объекте**.


</div>

### Run-once mode 

1.  Do one of the following:
    -   Select a single point and a single edge (in any order).
    -   Select several points and a single edge (idem).
    -   Select a single point and several edges (idem).
2.  Invoke the tool as explained above.
3.  Depending on the selection one or more constraints are added.



## Программирование

Ограничения можно создавать с помощью [макросов](Macros/ru.md) и в консоли [Python](Python/ru.md), используя следующие команды:


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`


<div class="mw-translate-fuzzy">

-    `Sketch`это объект эскиза.

-    `LineMoving`это номер, обозначающий линию, содержащую точку, которая будет передвинута на `LineFixed` (линию, которая останется на месте).

-    `PointOfLineMoving`это номер вершины линии `LineMoving`, которая будет передвинута на `LineFixed`.

-    `LinedFixed`это номер линии, к которой будет прикреплена точка `PointOfLineMoving`.


</div>

Страница [Sketcher scripting](Sketcher_scripting/ru.md) показывает, как узнать номер, определяющий линии и точки?


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/ru
