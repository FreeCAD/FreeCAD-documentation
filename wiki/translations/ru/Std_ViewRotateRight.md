---
- GuiCommand:/ru
   Name:Std ViewRotateRight
   Name/ru:Std ViewRotateRight
   MenuLocation:Вид → Стандартные виды → Повернуть вправо
   Workbenches:All
   Shortcut:**Shift**+**Right**
   SeeAlso:[Std ViewRotateLeft](Std_ViewRotateLeft/ru.md)
---

# Std ViewRotateRight/ru



## Описание

The **Std ViewRotateRight** command rotates the camera in the active [3D view](3D_view.md) around the view direction in 90-degree increments towards the right (clockwise).



## Применение

1.  There are several ways to invoke the command:
    -   Select the **View → Standard views → <img src="images/Std_ViewRotateRight.svg" width=16px> Rotate Right** option from the menu.
    -   Select the **Standard views → <img src="images/Std_ViewRotateRight.svg" width=16px> Rotate Right** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **Shift**+**Right**.



## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To rotate the view to the right use the `viewRotateRight` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateRight()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewRotateRight/ru
