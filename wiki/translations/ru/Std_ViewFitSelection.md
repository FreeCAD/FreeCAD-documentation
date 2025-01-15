---
 GuiCommand:
   Name/ru: Уместить выделенное
   Name: Std_ViewFitSelection
   MenuLocation: Вид , Стандартные виды‏‎ , Уместить выделенное
   Workbenches: Все
   Shortcut: **V** **S**
   SeeAlso: Std_ViewFitAll/ru
---

# Std ViewFitSelection/ru



## Описание


<div class="mw-translate-fuzzy">

Команда **Уместить выделенное** масштабирует и перемещает камеру так, чтобы все выбранные объекты уместились внутри активного [3D Вида](3D_view/ru.md). Данная команда крайне востребована в случаях если по каким-то причинам (сбой программы или в результате действий пользователя) ваш объект ушел далеко за границы текущего 3Д Вида, так что его не возможно отыскать используя обычную навигацию.


</div>



## Применение


<div class="mw-translate-fuzzy">

1.  Выберите один или несколько объектов.
2.  Существует несколько способов вызова команды:
    -   Через нажатие кнопки **<img src="images/Std_ViewFitSelection.svg" width=16px> [Уместить выделенное](Std_ViewFitSelection/ru.md)**.
    -   Через пункт меню **Вид → Стандартные виды → <img src="images/Std_ViewFitSelection.svg" width=16px>Уместить выделенное**.
    -   Через пункт **<img src="images/Std_ViewFitSelection.svg" width=16px> Уместить выделенное** контекстного меню [3D Вида](3D_view/ru.md).
    -   Последовательностью клавиш клавиатуры: **V** и **S**.


</div>



## Программирование


<div class="mw-translate-fuzzy">


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>


<div class="mw-translate-fuzzy">

Чтобы применить команду «Уместить выбранное» к активному 3D Виду, можно также использовать метод `SendMsgToActiveView` объекта FreeCADGui. Этот метод недоступен, если FreeCAD находится в режиме консоли.


</div>


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView("ViewSelection")
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Std ViewFitSelection/ru
