---
- GuiCommand:/ru
   Name/ru:Спереди
   Name:Std_ViewFront
   MenuLocation:Вид → Стандартные виды‏‎ → Спереди
   Workbenches:Все
   Shortcut:**1**
   SeeAlso:[Сверху](Std_ViewTop/ru.md), [Справа](Std_ViewRight/ru.md)
---

# Std ViewFront/ru

## Описание

Команда **Std ViewFront** направляет камеру в активном [окне трёхмерного просмотра](3D_view/ru.md) в положительном направлении оси Y.

![](images/FreeCAD_views_front.svg ) 
*Стрелка 1 указывает в сторону вида спереди*

## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewFront.svg" width=16px> [Std ViewFront](Std_ViewFront.md)** button.
    -   Select the **View → Standard views → <img src="images/Std_ViewFront.svg" width=16px> Front** option from the menu.
    -   Select the **Standard views → <img src="images/Std_ViewFront.svg" width=16px> Front** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **1**.

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To change to front view use the `viewFront` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewFront()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewFront/ru
