---
 GuiCommand:
   Name/ru: Спереди
   Name: Std_ViewFront
   MenuLocation: Вид , Стандартные виды‏‎ , Спереди
   Workbenches: Все
   Shortcut: **1**
   SeeAlso: Std_ViewTop/ru, Std_ViewRight/ru
---

# Std ViewFront/ru



## Описание

Команда **Std ViewFront** направляет камеру в активном [окне трёхмерного просмотра](3D_view/ru.md) в положительном направлении оси Y.

![](images/FreeCAD_views_front.svg ) 
*Стрелка 1 указывает в сторону вида спереди*



## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewFront.svg" width=16px> [Front](Std_ViewFront.md)** button.
    -   Select the **View → Standard views → <img src="images/Std_ViewFront.svg" width=16px> Front** option from the menu.
    -   Select the **Standard views → <img src="images/Std_ViewFront.svg" width=16px> Front** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **1**.



## Программирование


<div class="mw-translate-fuzzy">


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>

Use the `viewFront` method of the View object to change to front view. Methods for the other main view orientations are also available: `viewTop`, `viewRight`, `viewRear`, `viewBottom` and `viewRight`.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.viewFront()
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ViewFront/ru
