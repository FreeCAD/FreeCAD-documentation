---
- GuiCommand:/ru
   Name/ru:Сверху
   Name:Std_ViewTop
   MenuLocation:Вид → Стандартные виды‏‎ → Сверху
   Workbenches:Все
   Shortcut:**2**
   SeeAlso:[Спереди](Std_ViewFront/ru.md), [Справа](Std_ViewRight/ru.md)
---

# Std ViewTop/ru

## Описание

The **Std ViewTop** command points the camera in the active [3D view](3D_view.md) in the direction of the negative Z axis.

![](images/FreeCAD_views_front.svg ) 
*Arrow 2 points in the direction of the top view*

## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewTop.svg" width=16px> [Std ViewTop](Std_ViewTop.md)** button.
    -   Select the **View → Standard views → <img src="images/Std_ViewTop.svg" width=16px> Top** option from the menu.
    -   Select the **Standard views → <img src="images/Std_ViewTop.svg" width=16px> Top** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **2**.

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To change to top view use the `viewTop` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewTop()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewTop/ru
