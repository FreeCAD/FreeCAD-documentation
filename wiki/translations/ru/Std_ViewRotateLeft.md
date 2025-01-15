---
 GuiCommand:
   Name: Std ViewRotateLeft
   Name/ru: Std ViewRotateLeft
   MenuLocation: Вид , Стандартные виды , Повернуть влево
   Workbenches: All
   Shortcut: **Shift**+**Left**
   SeeAlso: Std_ViewRotateRight/ru
---

# Std ViewRotateLeft/ru



## Описание

The **Std ViewRotateLeft** command rotates the camera in the active [3D view](3D_view.md) around the view direction in 90-degree increments towards the left (counterclockwise).



## Применение

1.  There are several ways to invoke the command:
    -   Select the **View → Standard views → <img src="images/Std_ViewRotateLeft.svg" width=16px> Rotate Left** option from the menu.
    -   Select the **Standard views → <img src="images/Std_ViewRotateLeft.svg" width=16px> Rotate Left** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **Shift**+**Left**.

## Scripting


<div class="mw-translate-fuzzy">


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>

Use the `viewRotateLeft` method of the View object to rotate the view to the left. The `viewRotateRight` method is also available.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.viewRotateLeft()
```



---
⏵ [documentation index](../README.md) > Std ViewRotateLeft/ru
