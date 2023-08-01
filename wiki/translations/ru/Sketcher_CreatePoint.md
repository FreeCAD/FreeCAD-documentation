---
- GuiCommand:
   Name:Sketcher CreatePoint
   Name/ru:Точка
   MenuLocation:Эскиз - Геометрия эскиза - Точка
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   Shortcut:**G** **Y**
---

# Sketcher CreatePoint/ru



## Описание

Инструмент Точка создает точку в текущем эскизе, которую можно использовать для построения геометрических элементов.

[480px\|Point in the sketcher](IMAGE:Sketcher_Point_fr_01.png.md) 

## Применение

-   Нажмите на кнопку **<img src="images/Sketcher_CreatePoint.svg" width=24px> Создать точку**, что бы активировать функцию.
-   Нажатие на эскизе создает точку.
-   Нажатие **Esc** или щелчок правой кнопкой мыши отменяет функцию.



## Опции


<div class="mw-translate-fuzzy">

-   По умолчанию точки создаются как геометрия построения и поэтому не видны вне режима редактирования эскиза. Используйте инструмент <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:16px;"> [Переключить построительную геометрию](Sketcher_ToggleConstruction/ru.md), чтобы изменить их на нормальную геометрию. {{Version/ru|0.19}}
-   Режим привязки (прилипания) к сетке можно установить в [Настройках](Sketcher_Preferences/ru.md). Точка привязывается к сетке, если расстояние от сетки до линии сетки составляет менее 25%. Режим привязки не прикрепляет точку окончательно к сетке. Она по-прежнему имеет две степени свободы и может быть перемещена с помощью мыши или её местоположение может быть изменено ограничениями.


</div>





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePoint/ru
