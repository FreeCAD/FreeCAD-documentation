---
- GuiCommand:/ru
   Name:Std ViewRotateLeft
   Name/ru:Std ViewRotateLeft
   MenuLocation:Вид → Стандартные виды → Повернуть влево
   Workbenches:All
   Shortcut:**Shift**+**Left**
   SeeAlso:[Std ViewRotateRight](Std_ViewRotateRight/ru.md)
---

## Описание

The **Std ViewRotateLeft** command rotates the camera in the active [3D view](3D_view.md) around the view direction in 90-degree increments towards the left (counterclockwise).

## Применение

1.  There are several ways to invoke the command:
    -   Select the {{MenuCommand|View → Standard views → <img src="images/Std_ViewRotateLeft.svg" width=16px> Rotate Left}} option from the menu.
    -   Select the {{MenuCommand|Standard views → <img src="images/Std_ViewRotateLeft.svg" width=16px> Rotate Left}} option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **Shift**+**Left**.

## Scripting


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To rotate the view to the left use the `viewRotateLeft` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateLeft()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```





{{Std Base navi

}}  
